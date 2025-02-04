![GitHub Repo](https://img.shields.io/badge/Research-Paper-blue)
# **A GA-based algorithm meets the fair ranking problem**
## 📜 Abstract
<p align="justify">
Ranking items is a vital component in almost every application dealing with selecting the most
suitable items among a pool of candidates. Yet, specific individuals or groups may be systematically
disadvantaged in getting the opportunity to appear on the ranking list. The fair ranking
problem aims at mitigating the bias imposed on protected groups (i.e., disadvantaged groups)
while preserving the total quality of the ranking list as high as possible. FA*IR is one of the
existing algorithms, which finds the exact solutions for only one protected group, considering a
given minimum number of protected items at every prefix of a ranking list. However, when an
item belongs to more than two protected groups achieving optimal solutions gets more difficult.
This paper proposes an algorithm called FARGO, a fair ranking algorithm based on the genetic
algorithm (GA) enhanced by the simulated annealing (SA) that is able to handle any number of
protected groups. A new objective function is also proposed by incorporating the main goals of
the problem, which is utilized as FARGO’s fitness function. Furthermore, a novel evaluation
metric named Expected Gain Ratio (EGR) is introduced to assess a fair ranking algorithm’s output.
Experimental results on real-world datasets demonstrate that FARGO attains comparative performance
with FA*IR for one protected group and finds near-optimal solutions for more than one
protected group in terms of NDCG and EGR. Note that involving other concepts such as exposure
is not a matter of this paper and can be an interesting subject for further studies.
</p>

## 📊 Results
<p align="justify">
The table below presents a <strong>sample of our results</strong> from the paper, demonstrating that <strong>FARGO achieves the optimal solutions</strong> returned by the exhaustive search algorithm in terms of <strong>NDCG and EGR</strong>. This confirms that FARGO effectively addresses the fair ranking problem for  <strong>multiple protected groups</strong>. Moreover, it is promising that our algorithm will be capable of finding feasible solutions for <em>higher values of k</em>.
</p>

| Dataset      | C  | k  | **FARGO NDCG** | **FARGO EGR** | **Exhaustive NDCG** | **Exhaustive EGR** |
|-------------|----|----|---------------|--------------|--------------------|-------------------|
| **German Credit** | 2  | 3  | 0.999 | 0.998 | 0.999 | 0.998 |
|             |   | 4  | 0.992 | 0.962 | 0.992 | 0.963 |
|             |    | 5  | 0.994 | 0.967 | 0.994 | 0.969 |
|             | 3  | 3  | 0.999 | 0.998 | 0.999 | 0.998 |
|             |    | 4  | 0.992 | 0.963 | 0.992 | 0.963 |
|             |    | 5  | 0.994 | 0.969 | 0.994 | 0.969 |
|             | 4  | 3  | 0.999 | 0.918 | 0.999 | 0.918 |
|             |    | 4  | 0.992 | 0.853 | 0.992 | 0.853 |
|             |    | 5  | 0.994 | 0.832 | 0.994 | 0.832 |
| **COMPAS**  | 2  | 3  | 1.000 | 0.857 | 1.000 | 0.857 |
|             |    | 4  | 0.960 | 0.807 | 0.960 | 0.807 |
|             |    | 5  | 0.939 | 0.795 | 0.939 | 0.795 |
|             | 3  | 3  | 0.999 | 0.891 | 0.999 | 0.891 |
|             |    | 4  | 0.997 | 0.837 | 0.997 | 0.837 |
|             |    | 5  | 0.996 | 0.813 | 0.996 | 0.813 |
|             | 4  | 3  | 0.999 | 0.915 | 0.999 | 0.915 |
|             |    | 4  | 0.997 | 0.870 | 0.997 | 0.870 |
|             |    | 5  | 0.996 | 0.850 | 0.996 | 0.850 |
| **LSAC**   | 2  | 3  | 0.994 | 0.969 | 0.994 | 0.969 |
|             |    | 4  | 0.995 | 0.969 | 0.995 | 0.969 |
|             |    | 5  | 0.992 | 0.968 | 0.992 | 0.968 |

<p align="justify">
  <strong>NDCG</strong>: Normalized Discounted Cumulative Gain<br>
  <strong>EGR</strong>: Expected Gain Ratio
</p>

## 📌 Citation

If you use this work, please cite our [paper](https://www.sciencedirect.com/science/article/abs/pii/S0306457321001953) as follows:

```bibtex
@article{FARGO,
  author    = {Saedeh Tahery and Seyyede Zahra Aftabi and Saeed Farzi},
  title     = {A GA-based algorithm meets the fair ranking problem},
  journal   = {Information Processing & Management},
  year      = {2021},
  url       = {https://www.sciencedirect.com/science/article/abs/pii/S0306457321001953}
}
```
