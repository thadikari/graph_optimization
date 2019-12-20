import tensorflow as tf
from utils import Registry


reg = Registry()
def register_(func):
    reg.put(func.__name__, lambda: Evaluator(func))
    return func


plhd = lambda sh_: tf.placeholder(tf.float32, shape=sh_)
smax = tf.compat.v1.losses.softmax_cross_entropy

# create a single parameter vector and split it to a bunch of vars
def params(*shapes):
    size_ = lambda shape: shape if isinstance(shape, int) else shape[0]*shape[1]
    w_ = plhd(sum([size_(shape) for shape in shapes]))
    ret, start = [w_], 0
    for shape in shapes:
        end = start+size_(shape)
        vv = w_[start : end]
        if not isinstance(shape, int): vv = tf.compat.v1.reshape(vv,shape)
        ret.append(vv)
        start = end
    return ret


class Evaluator:
    def __init__(self, func):
        self.pl_x = plhd((None, 784))
        self.pl_y = plhd((None, 10))
        self.pl_w, logits_ = func(self.pl_x)
        self.loss = tf.reduce_mean(smax(self.pl_y, logits_, reduction='none'))
        self.w_len = self.pl_w.get_shape().as_list()[0]
        self.grad = tf.gradients(self.loss, self.pl_w)[0]
        self.sess = tf.compat.v1.Session()

    def get_size(self):
        return self.w_len

    def eval(self, w_, xy_):
        x_, y_ = xy_
        dd = {self.pl_w:w_, self.pl_x:x_, self.pl_y:y_}
        loss, grad = self.sess.run([self.loss, self.grad], feed_dict=dd)
        return loss, grad


@register_
def linear0(x_):
    w_, w, b = params((784,10), 10)
    return w_, x_@w+b

@register_
def linear1(x_):
    w_, w1, b1, w2, b2 = params((784,500), 500, (500,10), 10)
    return w_, (x_@w1+b1)@w2+b2

@register_
def relu1(x_):
    w_, w1, b1, w2, b2 = params((784,500), 500, (500,10), 10)
    return w_, tf.nn.relu(x_@w1+b1)@w2+b2


if __name__ == '__main__':
    '''
    Test for @params function. Should print the following.
    [0. 1. 2. 3. 4. 5. 6. 7. 8.]
    [0.]
    [1. 2.]
    [[3. 4.]
     [5. 6.]
     [7. 8.]]
    '''
    w_, w1, w2, w3 = params(1, 2, (3,2))
    with tf.train.MonitoredTrainingSession() as ss:
        lenw = w_.get_shape().as_list()[0]
        output = ss.run([w_, w1, w2, w3], feed_dict={w_:range(lenw)})
        print(*output, sep = '\n')
