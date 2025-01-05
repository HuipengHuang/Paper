1.Technical challenge of previous works

2.Technical contribution 

3.Theoretical insight

4.Limitation


# [Classification with Valid and Adaptive Coverage](https://proceedings.neurips.cc/paper/2020/file/244edd7e85dc81602b7615cd705545f5-Paper.pdf)

1. Previous methods do not have good conditional coverage.

2. It proposes adaptive prediction set, which has(not guarantees. Distribution-free guarantees on conditional coverage are impossible) good conditional coverage approximately and mitigate the limitation of THR described in (3).

3. The estimated probability of Y = y given X = x, often lead to poor
conditional coverage because the same threshold t is applied both to easy-to-classify samples (where
one label has probability close to 1 given X) and to hard-to-classify samples (where all probabilities
are close to 1/|Y| given X).
Thus, THR undercovers hard examples while overcovering trivial ones, resulting in high conditional coverage violations.

4. Naive method can not guarantee marginal coverage as the predicted probability of model is inaccurate.
APS will have lower efficiency compared with THR.(RAPS tries to address the problem and improve efficiency through regularization.)

# [Uncertainty Sets for Image Classifiers using Conformal Prediction](https://arxiv.org/pdf/2009.14193)

1. APS is inefficient.

2. It proposes RAPS, which is more efficient and adaptive than APS.

3. Add a regularization term to bound prediction sets' size.
The regularization causes the algorithm to avoid using the unreliable probabilities in the tail.

4. It is said to achieve better conditional coverage result but suppose we have a oracle model, it does not have theoretical guarantee for conditional coverage like APS.
RAPS also has this limitation, though performing well in experiments.

# [Conformal Prediction for Deep Classifier via Label Ranking](https://arxiv.org/pdf/2310.06430)

1. Softmax probability results in long-tail distribution, theoretically making APS's prediction set become large.
We expect that for easier data, the prediction set's length will be smaller.
Using label rank only, the prediction set's size is highly regularized with value between k-1 and k if Ar denote the accuracy of the top r
predictions for a trained model πˆ on an infinite calibration set.
k is the integer satisfying Ak ≥ 1 − α > Ak−1 

2. This paper propose SAPS(Sorted Adaptive Prediction Set).
It promises tight and small prediciton set.
The size of the prediction set is not highly regularized.
Easier data will result in a smaller prediction set.

3. It finds that softmax probability's information is redundant for conformal prediction, maximum softmax probability contains enough information for conformal prediction and the true label's ranking is negatively correlated to the MSP.
Using MSM avoid using those small prediction probability value in softmax probability.

# [Learning Optimal Conformal Classifiers](https://arxiv.org/pdf/2110.09192)

1. Previous methods do not modify training process and tend to be inefficient(prediction set's size being large)

2. In training process, split the train data into prediction set and calibration set.  Add another term in loss function to reduce the prediction set's size.

4. ConfTr optimizes the efficiency of conformal predictors at a predetermined
error rate (e.g., α = 0.01), which may result in suboptimal performance when predicting with a
different coverage rate.(C-adapter tries to address this problem by introducing a specially designed loss function)


# [Conformal Prediction Under Covariate Shift](https://arxiv.org/pdf/1904.06019)

1. The lower bound of 1 - α is not guaranteed when test data and train data are not exchangeable, especially when train distribution and test distribution are different.

2. This paper propose Weighted Conformal Prediction to address Covariate Shift and achieve probability bound even when train and test data are not exchangeable.

3. How to achieve conformity when known the difference of train and test distribution and known that P(Y|X) is the same for train and test.
When train and test distribution are different, effective sample size will change (could be understood as calibration data set's size become smaller), making the beta distribution of test data's 1 - α quantile be less tight.

# [C-ADAPTER: ADAPTING DEEP CLASSIFIERS FOR EFFICIENT CONFORMAL PREDICTION SETS](https://arxiv.org/pdf/2410.09408)

1. ConfTr's loss function has a term L_size, which inevitably deteriorates the accuracy of the classifier.
Experiments show that worse accuracy's effect on prediction sets' size will outperform the effect of penalizing L_size.
When the strength of penalizing L_size is stronger, the prediciton sets' size become even larger.

2. This article proposes conformal-adapter which improves both efficiency and accuracy. It proposes a loss function that could implicitly improve efficiency.

# [Conformal Risk Control](https://arxiv.org/pdf/2208.02814)Not Quite Understand

1. No previous research has discussed about controlling loss using conformal prediction.

2. This article proposes an analysis on controlling the expectation of loss when loss is non-increasing to confidence.

3. Results of controlling loss for some bounded, nondecreasing loss function like F1 score.

4. It can't be used to loss function like Cross Entropy Loss

# [Class-Conditional Conformal Prediction with Many Classes](https://arxiv.org/pdf/2306.09335)

1. With many classes, typical class-conditional conformal prediction will have very low inefficiency.

2. Use cluster method to gather classes with similar distribution to approximate conditional coverage.

4. It did not discuss how to choose hyperparameter K to gain better cluster result.
When many classes' distribution are all distinct, could this method still work well?

# [Does confidence calibration improve conformal prediction?](https://arxiv.org/pdf/2402.04344)

1. Existing methods of confidence calibration increase the size of prediction sets generated by adaptive conformal prediction methods.

2. This paper proposes a method and design a loss function to get optimal temperature scaling.

3. As temperature decreases, typically the average size of prediction set will first decrease and then increase.



To do
https://arxiv.org/pdf/1903.04684
https://arxiv.org/pdf/1904.01685
