# Consensus optimization - ICASSP '20

## Generating data:
* `python run_main.py --data_dist distinct_10 --func linear1 --opt PG --consensus perfect --strag_dist bern --strag_dist_param 0.8 --num_samples 60 --grad_combine Equal Proportional --save --graph_def amb_iclr_10 --num_iters 10000`
* `python run_main.py --data_dist distinct_10 --func linear1 --opt PG --consensus rand_walk --num_consensus_rounds 70 --strag_dist bern --strag_dist_param 0.8 --num_samples 60 --grad_combine Equal Proportional --save --graph_def amb_iclr_10 --num_iters 10000`
* `python run_main.py --data_dist distinct_10 --func relu1 --opt PG --consensus rand_walk --num_consensus_rounds 70 --strag_dist bern --strag_dist_param 0.8 --num_samples 60 --grad_combine Equal Proportional --save --graph_def amb_iclr_10 --num_iters 10000`
* Change accordingly and execute [`run_main.sh`](run_main.sh) to parallelly run all simulations.

## Generating plots:
* `python plot_run_main.py --ext pdf --ylog --all_workers --num_iters 4000 --no_dots`

## Other:
* `python run_main.py rand_walk round --save --loss_eval_freq 10 --num_consensus_rounds 10 --doubly_stoch metro`
* `python run_main.py rand_walk round --loss_eval_freq 10 --graph_def wk_4 --numw 4`

## Graph vs. distribution
* `python run_main.py --data_dist PQQQ --graph_def wk_4 --consensus rand_walk --num_consensus_rounds 5 --strag_dist equal --num_samples 64 --grad_combine Equal --weights_seed 99 --save --loss_eval_freq 10`


## Compare variances of "equal weighting" and "proportional weighting"
* Sample commands:
```
python plot_dist_mu2.py bern --trials 1000000 --bern_max 200 --bern_min 50
python plot_dist_mu2.py gauss --trials 1000000 --gauss_loc 200 --gauss_max_std 400
python plot_dist_mu2.py exp --trials 1000000 --exp_max 60 --exp_max_scale 15
```
* Change content in [`plot_dist_mu2.sh`](plot_dist_mu2.sh) and execute to generate all plots.
