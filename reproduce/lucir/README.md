# Learning a Unified Classifier Incrementally via Rebalancing

## Abstract
Conventionally, deep neural networks are trained offline, relying on a large dataset prepared in advance. This paradigm is often challenged in real-world applications, e.g. online services that involve continuous streams of incoming data. Recently, incremental learning receives increasing attention, and is considered as a promising solution to the practical challenges mentioned above. However, it has been observed that incremental learning is subject to a fundamental difficulty – catastrophic forgetting, namely adapting a model to new data often results in severe performance degradation on previous tasks or classes. Our study reveals that the imbalance between previous and new data is a crucial cause to this problem. In this work, we develop a new framework for incrementally learning a unified classifier, i.e. a classifier that treats both old and new classes uniformly. Specifically, we incorporate three components, cosine normalization, less-forget constraint, and inter-class separation, to mitigate the adverse effects of the imbalance. Experiments show that the proposed method can effectively rebalance the training process, thus obtaining superior performance compared to the existing methods. On CIFAR100 and ImageNet, our method can reduce the classification errors by more than 6% and 13% respectively, under the incremental setting of 10 phases.

## Citation
```
@inproceedings{hou2019learning,
  title={Learning a unified classifier incrementally via rebalancing},
  author={Hou, Saihui and Pan, Xinyu and Loy, Chen Change and Wang, Zilei and Lin, Dahua},
  booktitle={Proceedings of the IEEE/CVF conference on computer vision and pattern recognition},
  pages={831--839},
  year={2019}
}
```

## How to Reproduce EWC

- **Step1: 修改`run_trainer.py`中`Config`参数为`./config/ewc.yaml`**

- **Step2: python run_trainer.py**:


## Results


|backbone | buffer_size | Dataset | init_cls | inc_cls | acc|
| --- | --- | --- | --- | --- | --- |
| cifar_resnet32|  0 | CIFAR-100 | 50 | 50 | 39.00 | 