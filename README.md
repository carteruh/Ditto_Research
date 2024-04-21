# Follow Up Study on Ditto: Building Digital Twins of Articulated Objects from Interaction

Based on: [Zhenyu Jiang](http://zhenyujiang.me), [Cheng-Chun Hsu](https://chengchunhsu.github.io/), [Yuke Zhu](https://www.cs.utexas.edu/~yukez/)


[Project](https://ut-austin-rpl.github.io/Ditto/) | [arxiv](https://arxiv.org/abs/2202.08227)

![intro](assets/pipeline.png)

## News

**`2022-04-28`**: We released the data generation code of Ditto [here](https://github.com/UT-Austin-RPL/Ditto_data_gen).

## Introduction
<ins></ins>Ditto (<ins>Di</ins>gital <ins>T</ins>wins of Ar<ins>t</ins>iculated <ins>O</ins>bjects) is a model that reconstructs part-level geometry and articulation model of an articulated object given observations before and after an interaction. Specifically, we use a PointNet++ encoder to encoder the input point cloud observations, and fuse the subsampled point features with a simple attention layer. Then we use two independent decoders to propagate the fused point features into two sets of dense point features, for geometry reconstruction and articulation estimation separately. We construct feature grid/planes by projecting and pooling the point features, and query local features from the constructed feature grid/planes. Conditioning on local features, we use different decoders to predict occupancy, segmentation and joint parameters with respect to the query points. At then end, we can extract explicit geometry and articulation model from the implicit decoders. This project aims to follow up on Ditto and provide an evaluation of their model to improve.



## Citing
```
@inproceedings{jiang2022ditto,
   title={Ditto: Building Digital Twins of Articulated Objects from Interaction},
   author={Jiang, Zhenyu and Hsu, Cheng-Chun and Zhu, Yuke},
   booktitle={arXiv preprint arXiv:2202.08227},
   year={2022}
}
```
