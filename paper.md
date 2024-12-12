Technical challenge of previous works

Technical contribution 

Theoretical insight

Method Limitation

# [Conformal Prediction for Deep Classifier via Label Ranking](https://arxiv.org/pdf/2310.06430)

Softmax probability results in long-tail distribution, theoretically making APS's prediction set become large.
We expect that for easier data, the prediction set's length will be smaller.
However, RAPS (Regularized Adaptive Prediction Set)'s prediction set is highly regularized with value between k-1 and k if Ar denote the accuracy of the top r
predictions for a trained model πˆ on an infinite calibration set.
k is the integer satisfying Ak ≥ 1 − α > Ak−1 

This paper propose SAPS(Sorted Adaptive Prediction Set).
It promises tight and small prediciton set.
Besides, the length of the prediction set is not highly regularized.
Easier data will result in a smaller prediction set.

This paper finds that softmax probability's information is redundant for conformal prediction, maximum softmax probability contains enough information for conformal prediction and the true label's ranking is negatively correlated to the MSP.


