---
title: "R Notebook"
output:
  html_document:
    df_print: paged
    keep_md: true
  html_notebook: default
  pdf_document: default
  word_document: default
---


```r
library(knitr)
library(tidyverse)
```

```
## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
## ✔ dplyr     1.1.4     ✔ readr     2.1.5
## ✔ forcats   1.0.0     ✔ stringr   1.5.1
## ✔ ggplot2   3.4.4     ✔ tibble    3.2.1
## ✔ lubridate 1.9.3     ✔ tidyr     1.3.0
## ✔ purrr     1.0.2     
## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
## ✖ dplyr::filter() masks stats::filter()
## ✖ dplyr::lag()    masks stats::lag()
## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors
```

```r
library(tidymodels)
```

```
## ── Attaching packages ────────────────────────────────────── tidymodels 1.1.1 ──
## ✔ broom        1.0.5     ✔ rsample      1.2.0
## ✔ dials        1.2.0     ✔ tune         1.1.2
## ✔ infer        1.0.6     ✔ workflows    1.1.3
## ✔ modeldata    1.3.0     ✔ workflowsets 1.0.1
## ✔ parsnip      1.1.1     ✔ yardstick    1.3.0
## ✔ recipes      1.0.9     
## ── Conflicts ───────────────────────────────────────── tidymodels_conflicts() ──
## ✖ scales::discard() masks purrr::discard()
## ✖ dplyr::filter()   masks stats::filter()
## ✖ recipes::fixed()  masks stringr::fixed()
## ✖ dplyr::lag()      masks stats::lag()
## ✖ yardstick::spec() masks readr::spec()
## ✖ recipes::step()   masks stats::step()
## • Use suppressPackageStartupMessages() to eliminate package startup messages
```

```r
library(Matrix)
```

```
## 
## Attaching package: 'Matrix'
## 
## The following objects are masked from 'package:tidyr':
## 
##     expand, pack, unpack
```

```r
library(car)
```

```
## Loading required package: carData
## 
## Attaching package: 'car'
## 
## The following object is masked from 'package:dplyr':
## 
##     recode
## 
## The following object is masked from 'package:purrr':
## 
##     some
```

```r
library(skimr)
library(caret)
```

```
## Loading required package: lattice
## 
## Attaching package: 'caret'
## 
## The following objects are masked from 'package:yardstick':
## 
##     precision, recall, sensitivity, specificity
## 
## The following object is masked from 'package:purrr':
## 
##     lift
```

```r
library(pROC)
```

```
## Type 'citation("pROC")' for a citation.
## 
## Attaching package: 'pROC'
## 
## The following objects are masked from 'package:stats':
## 
##     cov, smooth, var
```

# What is Logistic Regression and How does it predict probabilities of a binary outcome?

Logistic regression is a type of statistical model that is utilized for inference and prediction. For inference, logistic regression can give insight into the strength/relationship between input variables to the output variable while for prediction, it is often used for binary classification. Therefore, given a dataset that contains independent variables, logistic regression can be used to predict the probability of an event occurring and then also assess which variables are most relevant and important to that outcome’s probability of occurring. The predicted value of logistic regression (or the dependent variable) is bound by an interval between 0 and 1. The closer to 1, the higher the probability of an event occurring.

At the foundation of this calculation is quantifying the odds of a binary outcome (ratio of success to failures). In this case, the odds are just a probability of success p divided by 1-p (probability of failure). However, mapping input variables to this output is not linear and is bounded from [0,inf].

$$  odds \ ratio=\frac{p}{1-p} $$

Because of this, the odds function must be transformed. The log of the odds is taken which is also known as the logit function. Here, the log transformation allows for the expression of the odds function as a linear function. The logit function can now be expressed as a linear combination of variables and coefficients. In addition, the bounds are also transformed from [-inf, +inf]. Since the output of log odds after this transformation is symmetric, this helps to increase the interpretation of the output of log odds. A negative value is the odds of failure while a positive value is the odds of success.

$$   log \ odds=log(\frac{p}{1-p}) = \beta_{0} + \beta_{1}w \ ... $$

To return values between 0 and 1 for probability, however, the log odds (logit) must be transformed into a probability. This is done by using the sigmoid function. When you take the sigmoid of the log odds, the output is transformed to be between 0 and 1.

$$  Sigmoid(log \ odds) = \frac{1}{1 + e^{-(\beta_{0} + \beta_{1}w \ ...)}} $$

Since the logit can be expressed as a linear combination of variables and coefficients, that linear expression is the input for the sigmoid function. Therefore, we get inputs that are a linear combination of variables (independent variables) and coefficients with an output between 0 and 1 (dependent variable expressed as a probability of success).

So, in this form of input and output, it is clear that the coefficients of each variable will affect the output. To estimate the coefficients that best describe the relationship of input data to the labeled output, Maximum Likelihood Estimation must be used. This method uses a likelihood function (the probability that observed values of an output can be predicted by inputs) and iteratively applies fundamental calculus to maximize the likelihood function given the different coefficients (parameters).

Maximizing the likelihood function in logistic regression to get the Maximum Likelihood Estimates (MLE) allows the model to determine parameter values that optimize the probability of observing the given data. This process allows logistic regression to effectively learn and adapt to the input data which then generates a prediction of binary outcomes for each labeled output. Furthermore, the estimated coefficients obtained through MLE provide a quantitative representation of the relationships between input variables and the output. This feature of logistic regression enables both prediction and increased understanding of how each variable contributes to the prediction of binary outcomes (inference).

The code below creates functions to inspect the behavior/anatomy of the logistic regression curve and errors based on different parameter values (slope, intercept, and threshold):


```r
# sigmoid function that takes logit expressed as linear function as input
sigmoid <- function(x) {
  return(1 / (1 + exp(-x)))
}

# to calculate x value, given a threshold y (cross hair)
inverse_sigmoid <- function(y, m, b) {
  return((log(y / (1 - y)) - b) / m)
}

# fake data 
generate_fake_data <- function(m, b, num_points, noise=0.1) {
  x <- seq(-10, 10, length.out = num_points)
  y <- sigmoid(m * x + b)
  y <- y + runif(num_points) * noise - noise / 2
  y <- ifelse(y >= 0.5, 1, 0)
  return(list(x=x, y=y))
}

# logistic regression curve with fake data and colored dots based on classification
plot_logistic_regression <- function(m, b, num_points, noise=0.1) {
  x_y_data <- generate_fake_data(m, b, num_points, noise)
  x <- x_y_data$x
  y <- x_y_data$y
  
  x_line <- seq(-10, 10, length.out = 100)
  y_line <- sigmoid(m * x_line + b)
  decision_boundary <- sigmoid(m * x + b)
  
  colors <- ifelse(y > decision_boundary, 'blue', 'red')
  
  plot(x, y, col=colors, pch=16, main=sprintf('m = %.2f, b = %.2f', m, b), xlab='x', ylab='y = sigmoid(mx+b)')
  lines(x_line, y_line, col='black', lty=1, lwd=2)
}

# logistic regression curve that allows threshold value as input to get Type 1/2 Errors
plot_logistic_regression_errors <- function(m, b, threshold, num_points=100, noise=0.1) {
  x_y_data <- generate_fake_data(m, b, num_points, noise)
  x <- x_y_data$x
  y <- x_y_data$y
  
  x_line <- seq(-10, 10, length.out = 100)
  y_line <- sigmoid(m * x_line + b)
  decision_boundary <- sigmoid(m * x + b)
  
  predictions <- ifelse(decision_boundary > threshold, 1, 0)
  colors <- ifelse(predictions == 1, 'blue', 'red')
  
  # dots
  plot(x, predictions, col=colors, pch=16, main=sprintf('m = %.2f, b = %.2f, thresh = %.2f', m, b, threshold), xlab='x', ylab='y = sigmoid(mx+b)')
  lines(x_line, y_line, col='black', lty=1, lwd=2)
  
  # type errors
  type1_errors <- which(predictions == 1 & y == 0)
  type2_errors <- which(predictions == 0 & y == 1)
  
  points(x[type1_errors], predictions[type1_errors], col='orange', pch='x', cex=1.5)
  points(x[type2_errors], predictions[type2_errors], col='purple', pch='x', cex=1.5)
  
  # cross hairs
  abline(h = threshold, col = 'black', lty = 2)
  abline(v = inverse_sigmoid(threshold, m, b), col = 'black', lty = 2)
  

  legend('bottomright', legend=c('Type 1 Error', 'Type 2 Error'), col=c('orange', 'purple'), pch=c('x', 'x'), lty=0, lwd=c(1.5, 1.5))
}
```

# Anatomy of Logistic Regression

1.  Shape of the curve
2.  Slope affect on curve
3.  Intercept affect on curve
4.  Decsision threshold affect on curve (Type I Error & Type 2 Errors)

# Shape of the Curve

As you will see below, the shape of the logistic regression curve is an "S" shape. This is due to the sigmoid function being used to take the linear expression of the log odds as input and mapping the outcomes to probability values between 0 and 1. The "S" shape is significant because it shows that as the input values increase on the x-axis, the predicted probabilities will have a clear transition from the negative outcome 0 to the positive outcome 1. This curve is known as the decision boundary and will separate the binary outcomes based on the threshold value that is set.


```r
plot_logistic_regression(m=0.5, b=-2, 10)
```

![](logistic_regression_covid_final2_files/figure-html/compare different values of m-1.png)<!-- -->

```r
plot_logistic_regression(m=1, b=-2, 10)
```

![](logistic_regression_covid_final2_files/figure-html/compare different values of m-2.png)<!-- -->

```r
plot_logistic_regression(m=3, b=-2, 10)
```

![](logistic_regression_covid_final2_files/figure-html/compare different values of m-3.png)<!-- -->

### What happens when you change (increase) the slope, m?

As m increases, the slope of the logistic regression curve becomes steeper. Again, the curve acts as the decision boundary and is necessary in being able to separate the data into binary outcomes. With larger values of m, the decision boundary will shift towards higher values of x. This can be seen as more points get classified as blue as m is increased. In addition, with a steeper curve, the classification will be more sensitive to changes in x. Therefore, with a higher m and a steeper slope, the logistic regression will have a clearer separation between the binary classes. While it is ideal to have a curve that is steep and that which clearly separates the data at x=0 (similar to the 3rd plot), that scenario is not realistic. More often, you will get less steep curves with less of a "separation".

In more detail, the sign of the slope, m, will determine the shape of the slope's direction. A positive slope will have a concave curve that shows a stronger relationship of x with the positive outcome (1) while a negative slope will have a convex curve that shows a stronger relationship of x with the negative outcome (0).

The overall magnitude of m directly impacts steepness of the slope. As stated, a higher m leads to a steeper slope. The slope m represents the log odds of an event occurring.


```r
plot_logistic_regression(m=0.5, b=-1, 10)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-3-1.png)<!-- -->

```r
plot_logistic_regression(m=0.5, b=0, 10)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-3-2.png)<!-- -->

```r
plot_logistic_regression(m=0.5, b=2, 10)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-3-3.png)<!-- -->

### What happens when you change (increase) the slope, b?

Similar to m, b plays an important role in shaping the decision boundary. As b increases, the intercept of the logistic regression line will shift upward. This means that the decision boundary will shift up which will increase the probability of predicting the positive class for lower feature values as seen in the plot above. The reverse can be said when decreasing b.

Therefore, slope directly effects the bias of the model since choosing a "bad" slope can affect the models outcome of choosing more of one binary outcome than the other.


```r
plot_logistic_regression_errors(m=0.5, b=1, threshold=0.2, num_points = 25)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-4-1.png)<!-- -->

```r
plot_logistic_regression_errors(m=0.5, b=1, threshold=0.5, num_points = 25)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-4-2.png)<!-- -->

```r
plot_logistic_regression_errors(m=0.5, b=1, threshold=0.8, num_points = 25)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-4-3.png)<!-- -->

The graphs above show a realistic scenario where the decision boundary does not lead to separable data. This curve represents non-separable data that includes different type errors and different threshold cut-offs. The cut-off threshold is the decided value for which a calculated probability will lead to a classification of 0 or 1. For example, if the threshold is 0.5, a probability of 0.51 will lead to a positive classification (1) while a probability of 0.49 will lead to a negative classification (0).

Type 1 errors are false positives which is when the model incorrectly predicts a 1 when the value should be a 0. A Type 2 error is a false negative where the model predicts that a value is 0 when it is actually a 1.

As seen, changing the threshold from 0.5 to 0.2 increases the amount of Type 1 errors. Decreasing the threshold means that it will be easier to predict a positive outcome since the needed probability threshold is lower. Therefore the model will predict more positive outcomes which can lead to more false positives.

In contrast, changing the threshold from 0.5 to 0.8 increases the amount of Type 2 errors. Increasing the threshold means that it will be harder to predict a positive outcome since the needed probability threshold is higher. Therefore, the model will predict more negative outcomes which can lead to more false negatives.

In the context of predicting risk of death for COVID-19 patients, setting a threshold that favors Type 1 errors is preferred since you would rather notify that someone is at risk of death even if they are not. On the contrary, you want to avoid the opposite scenario where you fail to notify someone who is actually at risk (Type 2 error). In a later a section, this preference will be discussed in the context of model assessment and weighing precision versus recall.

# Error Function

The error function used in logistic regression is the cross-entropy loss function A.K.A the log loss:

$$ H(p,q) = -\sum_{}^{}p(x)log(q(x)) $$

p(x) is the true probability distribution and q(x) is the logistic regression's predicted probability distribution over all classes in the distribution. As seen in the equation above, the more the two probability distributions (true vs predicted) diverge, the larger the cross entropy loss becomes.

Therefore, this function quantifies the difference between predicted probabilities and the actual labels. The smaller the cross-entropy loss, the more accurate the predicted class. Therefore, minimizing the cross-entropy loss function will help the logistic regression model learn the optimal parameters (coefficients and slope) to most accurately predict the classes of the data.

As mentioned in the introduction, a likelihood function must be maximized to find the MLE of the logistic regression. Specifically, the cross-entropy loss function is the negative log likelihood of the true label under the predicted probability distribution. Maximizing the likelihood is equivalent to minimizing the negative log-likelihood (cross-entropy loss). Therefore the cross-entropy loss function must be minimized in order to get the optimal parameter values.

With this in mind, we can see the relationship between the logistic regression equation, the log odds, and the cross-entropy loss.

The logistic regression equation represents the linear combination of variables and coefficients that are transformed by the sigmoid function to output probabilities between 0 and 1. The log odds is the unit values of the coefficients of the logistic regression which are found via the minimization of the cross-entropy loss function.

# Interpretation of Logistic Regression

### Odds ratio

-   the ratio of the odds of an event happening (success) to the odds of it not happening (failure)
    -   odds ratio \> 1: there is higher odds of success
    -   odds ratio = 1: equal odds of success and failure
    -   odds ratio \< 1: there is lower odds of success

### Log of Odds (logit)

-   the natural logarithm of the odds ratio
-   this allows the odds to be expressed in a linear form
-   log of odds represents the linear relationship between the independent variables and the log-odds of the event occurring
    -   Logit \> 0: positive relationship with successful outcome (increases chances of success)
    -   Logit = 0: no relationship
    -   Logit \< 0: negative relationship with successful outcome (decreases chances of success)

### Interpretation of Coefficients (Continuous Variables)

-   the coefficients in linear regression are the log odds of the probability of the outcome
-   therefore, with one unit increase in a variable input x, the log-odds of that event will change by the magnitude of the coefficient

#### if logit(p) = b0 + b1x1:

"With one unit increase in x1, the log odds of that event will change by b1"

Therefore, with one unit increase in x1, the odds ratio will change by e\^b1.

Logistic regression interprets the impact of independent variables on the log-odds of an event. To see how the odds ratio of an event changes due to a one unit increase in a variable with a coefficient b1, you can simply calculate e\^b1. This will tell you the magnitude in which a variable will change the odds ratio of an event happening. Overall, the coefficients allow you to see the magnitude and direction of the relationship between the variables and the odds of the event occurring.

### Interpretation of Coefficients (Categorical Variables)

-   the coefficients in linear regression are the log odds of the probability of the outcome
-   therefore, with one unit increase in a variable input x, the log-odds of that event will change by the magnitude of the coefficient

#### if logit(p) = b0 + b1x1:

"Compared to the reference category, the log odds of the event occurring for category x1 will change by b1"

Therefore, the odds ratio for category x1 compared to the reference category will change by ​e\^b1.

If x1 = sex and the reference variable is male (0), then you can say:

-   the odds ratio for sex will change by x1 if you go from male to female

### Interaction Terms

Another aspect of logistic regression we can dive into involves interaction terms.

Example:

$$ \log(odds)=\beta_0+\beta_1 X_1+\beta_2 X_2+\beta_3\left(X_1 \times X_2\right) $$

where the log(odds) is the input to the sigmoid function.

Here, $X_1$ and $X_2$are predictor variables. The combination of these variables $\left(X_1 \times X_2\right)$ represent the interaction term of these two predictors. The coefficient $\beta_3$ quantifies the relationship by measuring the change in the log-odds of the outcome as one predictor changes, contingent on the level of the other predictor.

The coefficient associated with an interaction terms represent the change in the log-odds of the outcome for a one-unit change in one predictor variable, given the value of the other predictor variable remains constant. A significant coefficient for an interaction term indicates that the joint effect of the two predictor variables on the outcome is different from what would be expected based on their individual effects alone. This can help uncover relationships between variables that may not be apparent when considering them singularly.

**One-way interaction terms:** A one-way interaction term indicates that the impact of one predictor on the outcome is contingent upon a specific level of another predictor. It reflects a scenario where the predictors do not operate independently but in conjunction with one another.

**Two-way interaction terms:** Two-way interaction terms involve a higher level of complexity, where the effect of one predictor on the outcome is influenced by the combined levels of two other predictor variables.

**Higher order terms:** Higher order terms are when a variable term is raised to a power that is greater than 1. This type of interaction allows variables to capture non-linear relationships between inputs and output. This allows for more complex relationships to be expressed in the data.

Model Fit: Integrating interaction and higher-order terms can substantially enrich model fit by accounting for these complex, real-world variable interactions. These "signals" represent the genuine effects or associations that we aim to model and understand, which will hold true even on new, unseen data. However, this comes with the caveat of potential over fitting. Over fitting is the risk of tailoring a model too closely to the training data, which provides a poor fit when new data is encountered, commonly referred to as "noise."

Ultimately too much noise can drop the performance of a model, so more simple models that focus on capturing broad patterns (signal) rather than fitting to every data point (noise) ensure that the model is robust and can generalize its predictions to new, unseen data.

Interpretive Implications: Interaction terms add a layer of sophistication to models, allowing us to see beyond the surface of direct effects into inter-variable dynamics that influence outcomes. Despite this, the inclusion of interaction terms alters the interpretive dynamics of logistic regression models. Each predictor's main effect cannot be viewed in isolation because it's conditional on the levels of other variables. Interaction terms necessitate a multifaceted approach for interpreting, often requiring the use of data visualization or additional statistical measures to fully capture predictors relationships on an outcome. For this logisitic regression model, we will not include such interactions.

**NOTE:** In a previous office hours, Julian told our group that we did not have to implement the interavtion terms in our model since we had a lot going on already. We discussed with him again (3/12/24) and he instructued us to take note of this for grading purposes.

# Conducting Logistic Regression:

## Goal 1: Make inferences on which variables have a significant effect on outcomes of death

## Goal 2: Predict binary outcomes of death in Covid-19 Patients

## Columns

The dataset was provided by the [Mexican government](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico). This dataset contains an enormous number of anonymized patient-related information including pre-conditions. The raw dataset consists of 21 unique features and 1,048,576 unique patients. In the Boolean features, 1 means "yes" and 2 means "no". values as 97 and 99 are missing data.

-   **sex:** 1 for female and 2 for male.
-   **age:** Age of the patient.
-   **classification:** Covid test findings. Values 1-3 mean that the patient was diagnosed with covid in different degrees. 4 or higher means that the patient is not a carrier of covid or that the test is inconclusive.
-   **patient type:** Type of care the patient received in the unit. 1 for returned home and 2 for hospitalization.
-   **pneumonia:** Whether the patient already has air sacs inflammation or not.
-   **pregnancy:** Whether the patient is pregnant or not.
-   **diabetes:** Whether the patient has diabetes or not.
-   **copd:** Indicates whether the patient has Chronic obstructive pulmonary disease or not.
-   **asthma:** Whether the patient has asthma or not.
-   **inmsupr:** Whether the patient is immunosuppressed or not.
-   **hypertension:** Whether the patient has hypertension or not.
-   **cardiovascular:** Whether the patient has heart or blood vessels related disease.
-   **renal chronic:** Whether the patient has chronic renal disease or not.
-   **other disease:** Whether the patient has other disease or not.
-   **obesity:** Whether the patient is obese or not.
-   **tobacco:** Whether the patient is a tobacco user.
-   **usmr:** Indicates whether the patient treated medical units of the first, second or third level.
-   **medical unit:** Type of institution of the National Health System that provided the care.
-   **intubed:** Whether the patient was connected to the ventilator.
-   **icu:** Indicates whether the patient had been admitted to an Intensive Care Unit.
-   **date died:** If the patient died indicate the date of death, and 9999-99-99 otherwise.
-   **has_died:** Added column. If patient is deceased or not.

### **Note:**

-   For Boolean features, 1 means "yes" and 2 means "no".
    -   Boolean features will be converted to 1's and 0's
-   Missing values are represented as either 97, 98, or 99
    -   Missing values will be converted to NAs

## Data Cleaning and Processing


```r
# load data
df <- read.csv('covid_data.csv')

# clean data
# make all columns lowercase 
colnames(df) <- tolower(colnames(df))

# boolean mask set to where date is not equal to '9999-99-99' (provides boolean basis to create 'has_died' column)
mask_valid_dates <- df$date_died != '9999-99-99'

# create has_died column based off boolean mask and drop date_died column
df <- df %>%
  mutate(has_died = ifelse(mask_valid_dates, 1, 0)) %>%
  select(-date_died)


# get categorical_cols to use for later EDA
# categorical_cols are columns besides age since age is continuous
categorical_cols <- setdiff(names(df), 'age')

# replace all vlues of 97/98/99 with NA
df[df == 97 | df == 98 | df == 99] <- NA

# get binary_cols (subset of categorical_cols) for later EDA/data preprocessing
# clasiffication_final and medical_unit are excluded since they have more than 2 categories
binary_cols <- setdiff(categorical_cols, c('clasiffication_final', 'medical_unit'))

# replace '2' values as '0' for binary_cols
df[binary_cols][df[binary_cols] == 2] <- 0

# creat multiclass_cols for EDA
multiclass_cols <- setdiff(categorical_cols, binary_cols)

# create num_medical_conditions column
df <- df %>%
  mutate(num_medical_conditions = pneumonia + diabetes + copd 
         + asthma + inmsupr + hipertension + other_disease +
        cardiovascular + obesity + renal_chronic)

# set null in pregnant to 0 if row contains male
df$pregnant[is.na(df$pregnant) & df$sex == 0] <- 0

# drop all rows that contain a null
df <- na.omit(df)
```

# EDA: Fisher's Exact Tests for Independence


```r
df_clean <- data.frame(df)

# For num_med_conditions: categorize into "0" and "1+" groups
df_clean$num_med_group <- ifelse(df_clean$num_medical_conditions == 0, "0", "1+")

# Creates 2x2 contingency table for num_med_group and has_died
medical_conditions_table <- table(df_clean$num_med_group, df_clean$has_died)
colnames(medical_conditions_table) <- c("Survived", "Died")
rownames(medical_conditions_table) <- c("0 Medical Conditions", "1+ Medical Conditions")
print(medical_conditions_table)
```

```
##                        
##                         Survived  Died
##   0 Medical Conditions     28514  5651
##   1+ Medical Conditions    94052 60895
```

```r
# Createes 2x2 contingency table for diabetes and has_died
diabetes_table <- table(df_clean$diabetes, df_clean$has_died)
colnames(diabetes_table) <- c("Survived", "Died")
rownames(diabetes_table) <- c("No Diabetes", "Diabetes")
print(diabetes_table)
```

```
##              
##               Survived  Died
##   No Diabetes    91906 41696
##   Diabetes       30660 24850
```

Utilizing our derived variable num_medical_conditions, we categorized the data into two groups: "0 Medical Conditions" and "1+ Medical Conditions."Similarly, for the variable diabetes, we have two groups: "No Diabetes" and "Diabetes."

We used the table() function to create 2x2 contingency tables for each pair of categorical variables (num_med_group and has_died, and diabetes and has_died).The contingency tables display the frequency distribution of the variables, categorizing them based on survival status ("Survived" or "Died").

### Fisher's Test for multiple medical conditions and diabetes vs dying

Fisher's exact test serves as a robust statistical method to assess the presence of significant associations between categorical variables, particularly in scenarios characterized by small sample sizes or sparse data. In our study, we utilized Fisher's exact test to analyze 2x2 contingency tables derived from categorical variables (num_medical_conditions and diabetes), in relation to the output variable of mortality (has_died) among COVID-19 patients.

The test is based on the calculation of probabilities using the observed data and marginal totals of a contingency table. Here's a brief explanation of how Fisher's exact test works:

The first step in conducting Fisher's exact test is to create a contingency table. This table displays the frequency distribution of the categorical variables being analyzed. Fisher's exact test then is utilized to calculate the probability of observing the data under the assumption that there is no association between the two variables (i.e., the null hypothesis is true). To do this, it considers all possible arrangements of the data that have the same marginal totals (i.e., row and column totals) as the observed data.

The test statistic used in Fisher's exact test is the probability of observing the data or more extreme data, given the marginal totals. This probability is calculated by summing the probabilities of all possible arrangements of the data that are as extreme or more extreme than the observed data.

If the probability of observing the data under the null hypothesis is sufficiently low (typically below 0.05), then the null hypothesis is rejected. This indicates that there is a significant association between the two variables. In addition to the p-value obtained from Fisher's exact test, we can calculate the odds ratio, which quantifies the strength and direction of the association between the two variables. The odds ratio represents the odds of one outcome occurring compared to another outcome, given exposure to a particular factor.

There are several key reasons Fisher's test was chosen to asses the association between variables in our data set. First, as stated, the test is designed to asses the association between two categorical variables, which are the types of variables we were working with. Utilizing 2x2 contingency tables, we could generate a p-value and odds ratios which would lend statistical evidence to our findings.

Equally as important is the fact that Fisher's exact test is a non-parametric statistical test, meaning it does not rely on specific (or any) assumptions regarding the distribution of the data or the expected counts of the data (unlike chi-squared). This characteristic allows the test to be suitable for analyzing categorical data of any size. Thus, Fisher's exact test offers a thorough and robust approach to our data.

Fisher's exact test also generates straightforward and interpretable results. A significant p-value obtained from the test allows for compelling evidence against the null hypothesis of no association between variables. This simplicity in interpretation allowed us to gain important insights regarding variable associations and ultimately, forming larger conclusions about the study as a whole.

Lastly, in contrast to a chi-squared test, as stated above, Fisher's test has more utility as it can give the direction and magnitude of the association between variables (odds ratio). This helps to get a better understanding of the actual relationship and not just seeing if a relationship exists.


```r
# Run Fisher's exact test for num_medical_conditions  and has_died
fisher_medical_conditions <- fisher.test(medical_conditions_table)
print(fisher_medical_conditions)
```

```
## 
## 	Fisher's Exact Test for Count Data
## 
## data:  medical_conditions_table
## p-value < 2.2e-16
## alternative hypothesis: true odds ratio is not equal to 1
## 95 percent confidence interval:
##  3.169266 3.368068
## sample estimates:
## odds ratio 
##   3.267283
```

```r
# Run Fisher's exact test for diabetes and has_died
fisher_diabetes <- fisher.test(diabetes_table)
print(fisher_diabetes)
```

```
## 
## 	Fisher's Exact Test for Count Data
## 
## data:  diabetes_table
## p-value < 2.2e-16
## alternative hypothesis: true odds ratio is not equal to 1
## 95 percent confidence interval:
##  1.750364 1.823357
## sample estimates:
## odds ratio 
##   1.786539
```

## Running Fisher's Exact Test:

After creating the contingency tables, we used the fisher.test() function to perform Fisher's exact test for each pair of variables (1+ Medical Conditions and has_died, and diabetes and has_died). This function calculates the p-value associated with the observed data under the null hypothesis of independence between the variables. The output of fisher.test() includes the test statistic, p-value, and an odds ratio for the test.

The odds ratio is a measure of how strongly an event is associated (effect on likelihood) with the output. It serves as a ratio of an event (death) occurring in the group afflicted vs. not afflicted with the input variable of question. Through our Fisher's tests, we calculated odds ratio for those with multiple conditions/diabetes with has_died.

The results of the Fisher's exact tests indicate strong evidence of associations between the predictor variables (multiple medical conditions and having diabetes) and the outcome variable (has_died). The outputs we generated show that for each Fisher's test performed, the p-value is very close to zero (p-value \< 2.2e-16). This indicates strong evidence against the null hypothesis that there is no association between the input variables and the outcome has_died.

Based on our results we observe that there is a significant association between having multiple conditions and dying. In addition, we also observe that there is a significant association between having diabetes and dying.

The calculated odds ratio for 1+ Medical Conditions and dying is 3.27. This indicates the estimated odds of a patient dying is approximately 3.27x higher if they have 1 or more pre-existing medical conditions at the time they had COVID. Further, the 95% confidence interval suggests two things: first, the range is greater than 1, which indicates a positive association between the presence of multiple medical conditions and the likelihood of death. Second, the odds ratio ranges form 3.17 - 3.37. This suggests that we can say with 95% confidence that the true odds of dying with more than one medical conditions is between 3.17-3.37 times greater than patients without multiple conditions.

The calculated odds ratio for diabetes and dying is 1.79. Similarly, this indicates the estimated odds of a patient dying is approximately 1.79x higher if they had diabetes at the time they were COVID positive. The 95% confidence interval ranged from 1.75 to 1.82, which indicates a positive association (odds ratio greater than 1). This suggests that we can say with 95% confidence that the true odds of dying is between 1.75 - 1.82 times greater in patients with diabetes vs those without it.

In conclusion, both Fisher's tests indicate a strong likelihood that there is a significant association between having multiple medical conditions and dying, as well as a significant association between having diabetes and dying.

## Comparing 2x2 contingency tables to logistic regression.

Logistic regression is more powerful than using a two by two table analysis for several reasons...

First, logistic regression has greater flexibility with multiple variables that can be assessed/compared within the same model/test, With this characteristic, we can asses more than one variable's effect on the outcome at the same time. In contrast, a two by two table analysis typically considers only one predictor variable at a time. This allows us to assess the independent effects of each predictor variable on the outcome while controlling for other variables in the model.

Secondly, logistic regression can handle both categorical and continuous predictor variables, whereas a two by two table analysis is typically limited to categorical variables. This allows us to asses a wider range of predictor variables data types in the analysis which provides a more comprehensive understanding of the relationship between the predictors and the outcome.

Third, logistic regression provides estimates of odds ratios. This quantifies the strength and direction of the association between each predictor variable and the outcome. This gives a more nuanced interpretation of the results compared to simply comparing proportions or percentages as in a two by two table analysis and working off a p-value.

In general, while a two-by-two table analysis can be simple in comparing two categorical variables and assessing their relationship, logistic regression has better capabilities in terms of its flexibility to analyze complex relationships that involve multiple variables of different data types and its ability to return interpretable results that can give more insight/utility.

# Exploratory Graphs to Identify Relationships

Exploratory data analysis (EDA) is a crucial step in the model-building process as it allows us to gain insights into the underlying patterns and relationships within the data. When investigating the predictive power of various factors on the outcome of death versus survival, EDA plays a fundamental role in identifying key variables and understanding their impact.

One of the primary reasons for conducting EDA is to visually explore the distribution and relationships of variables, particularly in relation to the outcome variable of interest. In our case, we were interested in understanding how different variables or conditions might influence the likelihood of a patient succumbing to COVID-19 (death).

Bar graphs focused on calculated odds are an effective visualization tool for categorical variables, making them an excellent choice for exploring the relationship between variables. By plotting the odds of individuals that have died with a positive occurrence of a specific variable and the odds of individuals that have died without a positive occurrence of a specific variable, we can get a baseline understanding if there exists an association/effect between a variable and an outcome. If the heights of these two bar graphs, are approximately the same, then we can reasonably say that there is no effect/association between the variable and the outcome (odds are similar and due to random chance). If the heights of the two bar graphs are different, then you can reasonably say that there may exist an effect/association between the variable and outcome (odds are different).

In the subsequent analysis, we delved deeper into these findings, focusing on variables that showed the most pronounced differences in mortality rates. By investigating these variables more closely, we aimed to gain a deeper understanding of their potential impact on the outcome of interest and inform our selection of features for inclusion in our predictive model.


```r
calculate_death_odds <- function(variable, df) {
  # odds of death with and without the variable
  odds_with <- sum(df$has_died[df[[variable]] == 1 & df$has_died == 1]) / sum(df[[variable]] == 1 & df$has_died == 0)
  odds_without <- sum(df$has_died[df[[variable]] == 0 & df$has_died == 1]) / sum(df[[variable]] == 0 & df$has_died == 0)
  
  
  # bar plot
  bar_data <- c(odds_with, odds_without)
  names(bar_data) <- c(paste("Odds w/", variable), paste("Odds w/out", variable))
  barplot(bar_data, 
          main = "Odds of individuals dying",
          xlab = "Groups",
          ylab = "Odds",
          col = "skyblue",
          ylim = c(0, max(bar_data) + 0.5))
  
  cat("Odds of dying with", variable, ":", odds_with, "\n")
  cat("Odds of dying without", variable, ":", odds_without, "\n")
}

calculate_death_odds('intubed', df)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-7-1.png)<!-- -->

```
## Odds of dying with intubed : 3.667896 
## Odds of dying without intubed : 0.3521651
```

```r
calculate_death_odds('diabetes', df)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-7-2.png)<!-- -->

```
## Odds of dying with diabetes : 0.8105023 
## Odds of dying without diabetes : 0.4536809
```

```r
calculate_death_odds('copd', df)
```

![](logistic_regression_covid_final2_files/figure-html/unnamed-chunk-7-3.png)<!-- -->

```
## Odds of dying with copd : 0.7526339 
## Odds of dying without copd : 0.5348445
```

Through our EDA using bar graphs, we were able to identify notable differences in mortality odds across different features. To assess the strength of the association between the variables and the outcome of interest (death vs. survival), we considered both the visual difference in bar heights and the context of the variables. A strong effect was indicated by a large discrepancy in the odds of deaths between the two groups (dying with a positive instance of a variable vs. dying without a positive instance of a variable). Conversely, a weak association would be suggested by bars that are approximately even in height across the two groups, indicating that the condition does not have a substantial impact on the death outcome (the odds being the similar or the same).

The three variables we were interested in were diabetes, intubed, and copd.

For diabetes, we see that that odds of individuals that have died with diabetes versus without diabetes was 0.81 vs 0.45. This difference suggests that having diabetes has an effect on increasing the odds of an individual dying. Looking at intubed, we see that the odds of individuals that have died that were intubed versus not being intubed was 3.67 vs 0.35. This large difference suggests a very strong effect on increasing the odds of an individual dying. For copd, we see that the odds of individuals that have died with copd versus without copd was 0.75 versus 0.53. This is the smallest difference and suggests that while copd may increase the odds of dying, that effect may not be as strong as the first two.

These visualizations allowed us to build more insight as to which variables might have a significant impact on the outcome of death and helped guide further analysis and the selection of features for predictive modeling, focusing on those with stronger associations for more accurate predictions.

### Logistic Regression Assumptions to Consider:

1.  **Dependent/response variable is binary**
    -   Yes. Died (1) versus has not died (0).
2.  **Little or no multicollinearity between the predictor/explanatory variables**
    -   Multicollinearity does exist. We will violate these :)
3.  **Linear relationship of independent variables to log odds**
    -   As out data is virtually ALL binary, categorical data, we cannot check this assumption for the majority of our data.
4.  **Prefers large sample size**
    -   Yes, even with omitting NULLs, the dataset is about \~189,000 rows long.
5.  **Problem with extreme outliers**
    -   None identified. Age, the only column with outliers, follows a relatively normal distribution.
6.  **Independent observations**
    -   Yes, assuming independence of individual outcomes. It is reasonable to say that one person's death should not affect another's.


```r
# logistic regression model (penalty = 0; no regularizaion)

set.seed(123)
split <- initial_split(df, prop = 0.8, strata = has_died)
train_data <- training(split)
test_data <- testing(split)

df$has_died = as.factor(df$has_died)

# summary 
covid_model_all <- glm(has_died ~ ., data = train_data, family = "binomial")
summary(covid_model_all)
```

```
## 
## Call:
## glm(formula = has_died ~ ., family = "binomial", data = train_data)
## 
## Coefficients: (2 not defined because of singularities)
##                          Estimate Std. Error z value Pr(>|z|)    
## (Intercept)            -2.4914344  0.0345384 -72.135  < 2e-16 ***
## usmer                   0.1985486  0.0129499  15.332  < 2e-16 ***
## medical_unit           -0.0416198  0.0018716 -22.237  < 2e-16 ***
## sex                    -0.2822253  0.0134609 -20.966  < 2e-16 ***
## patient_type                   NA         NA      NA       NA    
## intubed                 2.3742392  0.0193282 122.838  < 2e-16 ***
## pneumonia               0.6326187  0.0141589  44.680  < 2e-16 ***
## age                     0.0373380  0.0004287  87.097  < 2e-16 ***
## pregnant               -0.8997110  0.1381796  -6.511 7.46e-11 ***
## diabetes                0.2039590  0.0144852  14.081  < 2e-16 ***
## copd                   -0.0903531  0.0306585  -2.947  0.00321 ** 
## asthma                 -0.2385795  0.0446973  -5.338 9.41e-08 ***
## inmsupr                 0.1904785  0.0364844   5.221 1.78e-07 ***
## hipertension            0.0632051  0.0148161   4.266 1.99e-05 ***
## other_disease           0.2483636  0.0282011   8.807  < 2e-16 ***
## cardiovascular         -0.1347660  0.0290594  -4.638 3.52e-06 ***
## obesity                 0.1091474  0.0159054   6.862 6.78e-12 ***
## renal_chronic           0.3732931  0.0265413  14.065  < 2e-16 ***
## tobacco                -0.1102598  0.0232581  -4.741 2.13e-06 ***
## clasiffication_final   -0.1910321  0.0035898 -53.216  < 2e-16 ***
## icu                    -0.3486518  0.0254999 -13.673  < 2e-16 ***
## num_medical_conditions         NA         NA      NA       NA    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 196253  on 151287  degrees of freedom
## Residual deviance: 148513  on 151268  degrees of freedom
## AIC: 148553
## 
## Number of Fisher Scoring iterations: 5
```

Based on the above results, we will remove coefficients with p-values greater than 0.05/have minimal impact based on EDA and remove any coefficients that have NULL values.


```r
remove_columns <- c('patient_type', 'copd', 'num_medical_conditions')
covid_model_subset <- glm(has_died ~ ., data = train_data[, !(colnames(df) %in% remove_columns)], family = "binomial")
summary(covid_model_subset)
```

```
## 
## Call:
## glm(formula = has_died ~ ., family = "binomial", data = train_data[, 
##     !(colnames(df) %in% remove_columns)])
## 
## Coefficients:
##                        Estimate Std. Error z value Pr(>|z|)    
## (Intercept)          -2.4799632  0.0343066 -72.288  < 2e-16 ***
## usmer                 0.1986064  0.0129494  15.337  < 2e-16 ***
## medical_unit         -0.0416228  0.0018715 -22.240  < 2e-16 ***
## sex                  -0.2834356  0.0134547 -21.066  < 2e-16 ***
## intubed               2.3744221  0.0193272 122.854  < 2e-16 ***
## pneumonia             0.6326235  0.0141584  44.682  < 2e-16 ***
## age                   0.0371528  0.0004239  87.653  < 2e-16 ***
## pregnant             -0.9007012  0.1381781  -6.518 7.11e-11 ***
## diabetes              0.2038462  0.0144849  14.073  < 2e-16 ***
## asthma               -0.2457017  0.0446461  -5.503 3.73e-08 ***
## inmsupr               0.1868795  0.0364687   5.124 2.99e-07 ***
## hipertension          0.0624762  0.0148140   4.217 2.47e-05 ***
## other_disease         0.2477226  0.0281999   8.785  < 2e-16 ***
## cardiovascular       -0.1409721  0.0289833  -4.864 1.15e-06 ***
## obesity               0.1083282  0.0159030   6.812 9.64e-12 ***
## renal_chronic         0.3724469  0.0265414  14.033  < 2e-16 ***
## tobacco              -0.1180334  0.0231138  -5.107 3.28e-07 ***
## clasiffication_final -0.1917024  0.0035829 -53.505  < 2e-16 ***
## icu                  -0.3487030  0.0254979 -13.676  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 196253  on 151287  degrees of freedom
## Residual deviance: 148522  on 151269  degrees of freedom
## AIC: 148560
## 
## Number of Fisher Scoring iterations: 5
```

## Creating the function that trains data on logistic regression model and returns relevant metrics:


```r
logistic_regression_metrics <- function(df, threshold = 0.5, prop = 0.8) {
  # train-test split
  set.seed(123)
  split <- initial_split(df, prop = prop, strata = has_died)
  train_data <- training(split)
  test_data <- testing(split)
  
  actual_classes <- test_data$has_died
  
  covid_model_subset <- glm(has_died ~ ., data = test_data, family = "binomial")

  predicted_probs <- predict(covid_model_subset, newdata = test_data, type = "response")
  predicted_classes <- ifelse( predicted_probs > threshold, 1, 0)
   
  # calculate accuracy using caret's confusionMatrix function
  conf_matrix <- confusionMatrix(factor(predicted_classes), test_data$has_died, positive = '1')
  accuracy_value <- conf_matrix$overall["Accuracy"]
  precision <- conf_matrix$byClass[["Pos Pred Value"]]
  recall <- conf_matrix$byClass[["Sensitivity"]]
  f1_score <- 2 * (precision * recall) / (precision + recall)
  
  
  cat("Accuracy:", round(accuracy_value['Accuracy'], 4), "\n")
  cat("Precision:", round(precision, 4), "\n")
  cat("Recall:", round(recall, 4), "\n")
  
  return(list(actual_classes = actual_classes, predicted_classes = predicted_classes, predicted_probabilities = predicted_probs))
}
```

## Model Building 1: EDA & Inference

In the context of model building, we conducted exploratory data analysis (EDA) and inference to better tailor our selection process for building a logistic regression model. We utilized bar graphs to visually explore the relationships of odds between various categorical features and the outcome variable, mortality (has_died). Additionally, we examined the coefficients obtained from the logistic regression model trained on all available data to identify the most influential features.

The logistic regression model trained on all data provided insights into the significance and direction of the relationships between predictor variables and the likelihood of death. The coefficients (log odds) from this model indicated the strength of association between each predictor variable and the outcome, allowing us to prioritize features for inclusion in our final model.

Using the results from both the EDA and the logistic regression model, we made decisions regarding which features to include in our model. Features that demonstrated a statistically significant association (p\<0.05) with the outcome variable and had visually distinct patterns in the bar graphs were kept. Conversely, features with poor statistical significance (p\>0.05) and minimal visual impact on the outcome were considered for exclusion.

Based on our EDA and our inference test, we removed 'copd', 'patient_type', and 'num_medical_conditions'. The resulting filtered dataset will be referred as the subset data in the sections below.

In the code below, we look at our "model build one" logistic regression model trained on all data, on the subset data, and a model with a lower threshold for all the data. This analysis allowed us to assess the impact of feature selection on model performance metrics, such as accuracy, precision, and recall. By systematically adjusting thresholds and subsets of features, we could make better decisions on our model's behavior and performance.

Please note, that both inference and training were conducted on a training set only. The inference was based on the training set and helped make our decisions with model build one. In addition, the model was tested on the test set.


```r
results_all <- logistic_regression_metrics(df, threshold=0.5, prop=0.8)
```

```
## Accuracy: 0.7626 
## Precision: 0.7407 
## Recall: 0.5007
```


```r
remove_columns <- c('patient_type', 'num_medical_conditions', 'copd')
df_subset = df[, !(colnames(df) %in% remove_columns)]

results_subset <- logistic_regression_metrics(df_subset, threshold=0.5, prop=0.8)
```

```
## Accuracy: 0.7624 
## Precision: 0.7406 
## Recall: 0.4997
```


```r
results_all <- logistic_regression_metrics(df, threshold=0.3, prop=0.8)
```

```
## Accuracy: 0.71 
## Precision: 0.5642 
## Recall: 0.7729
```

As stated above, we examined three models so far: one incorporating all available predictor variables, another that had a subset of the features, and a third that had the subset of features with a decreased threshold. Before we continue, we will define accuracy, precision, and recall.

**Accuracy:** Out of all predictions, returns ratio of how many were predicted correctly $$ \text{Accuracy} = \frac{\text{TP + TN}}{\text{TP + TN + FP + FN}} $$

**Precision:** Out of all positive predictions, returns ratio of how many were truly positive $$ \text{Precision} = \frac{TP}{TP + FP} $$

**Recall:** Out of all true labels, returns ratio of correctly predicted positives $$ \text{Recall} = \frac{TP}{TP + FN} $$

Across the three performance metrics, the logistic model trained on all data marginally performed better than the model trained on the feature selected data. Despite the difference in feature selection, both models showed similar performance with moderate to high accuracy (76.26% all data and 76.24% subset). Similarly, both models had similar precision percentages of 74.07% for all data and 74.06% for the subset data. Likewise, recall scores were again similar with 50.07% for all data and 49.97% for the subset data. **We will discuss in more detail how to interpret accuracy, recall, precision with the context of our problem in the Final Model Selection section.**

Since the model trained on all data performed better than the subset data model (though very marginally), we decided to continue with the full data model.

As we decided that the full data model was the initial "winner", we then generated a third model that contained decreased threshold values. As discussed in the theory section on Type Errors, lowering the threshold favors recall. In terms of our study, our aim was to correctly predict the outcome of death based on the presence of certain conditions/variables. As a medical analysis, we found it more wise to err on the side of caution because missing an actual case (false negative) can be more detrimental than incorrectly identifying a non-case as a case (false positive).

We observed that reducing the threshold for classification of the full data model to 0.3 (instead of 0.5) lead to higher recall which we intended (\~77.29%) but at the cost of lower precision (\~56.42%). This trade-off infers that while the model becomes more sensitive in identifying positive cases (deceased patients), it also becomes less specific, leading to more false positives.

Considering these factors, we determined that utilizing the full-data model with a decreased threshold would be a suitable choice for our purposes.

However, we also wanted to attempt a second model build (fourth model) using a different method. In the next section, we discuss how we used backwards select model building to create yet another model.

## Model Building 2: Backwards Model Selection

Backwards model building is a process used in statistical modeling to algorithmically choose variables to include in the model. Specifically, backwards model selection starts with all predictor variables and then iterately removes variables until a final condition is met.

This algorithm starts with the full model, fits it to the logistic regression, and determines which variables have the least impact/significance on the outcome variable through specific statistical significance criteria. Once identified, the least impact variables are removed and the model is trained again, repeating this process until only significantly impact variables remain.

For the implementation of the backwards model selection, we use the stats::step() function which automatically carries out the process mentioned above. We supply the function with the fully trained model, choose the direction parameter to be backwards, and set trace to false so the output of the iterative training is not seen. In addition, while there is a criterion parameter, we just kept the value to the default = 'AIC' which is the Alkaline Information Criterion (AIC).

The Alkaline Information Criterion estimates prediction error of model and thus, gives a quantitative approach to model assessment. AIC is used within this backward model selection method as the main means of model selection.


```r
covid_model_all <- glm(has_died ~ ., data = train_data, family = "binomial")

backwards_select_model <- stats::step(covid_model_all, direction = "backward", trace = FALSE)
```

Final output of backwards model selection:


```r
summary(backwards_select_model)
```

```
## 
## Call:
## glm(formula = has_died ~ usmer + medical_unit + sex + intubed + 
##     pneumonia + age + pregnant + diabetes + copd + asthma + inmsupr + 
##     hipertension + other_disease + cardiovascular + obesity + 
##     renal_chronic + tobacco + clasiffication_final + icu, family = "binomial", 
##     data = train_data)
## 
## Coefficients:
##                        Estimate Std. Error z value Pr(>|z|)    
## (Intercept)          -2.4914344  0.0345384 -72.135  < 2e-16 ***
## usmer                 0.1985486  0.0129499  15.332  < 2e-16 ***
## medical_unit         -0.0416198  0.0018716 -22.237  < 2e-16 ***
## sex                  -0.2822253  0.0134609 -20.966  < 2e-16 ***
## intubed               2.3742392  0.0193282 122.838  < 2e-16 ***
## pneumonia             0.6326187  0.0141589  44.680  < 2e-16 ***
## age                   0.0373380  0.0004287  87.097  < 2e-16 ***
## pregnant             -0.8997110  0.1381796  -6.511 7.46e-11 ***
## diabetes              0.2039590  0.0144852  14.081  < 2e-16 ***
## copd                 -0.0903531  0.0306585  -2.947  0.00321 ** 
## asthma               -0.2385795  0.0446973  -5.338 9.41e-08 ***
## inmsupr               0.1904785  0.0364844   5.221 1.78e-07 ***
## hipertension          0.0632051  0.0148161   4.266 1.99e-05 ***
## other_disease         0.2483636  0.0282011   8.807  < 2e-16 ***
## cardiovascular       -0.1347660  0.0290594  -4.638 3.52e-06 ***
## obesity               0.1091474  0.0159054   6.862 6.78e-12 ***
## renal_chronic         0.3732931  0.0265413  14.065  < 2e-16 ***
## tobacco              -0.1102598  0.0232581  -4.741 2.13e-06 ***
## clasiffication_final -0.1910321  0.0035898 -53.216  < 2e-16 ***
## icu                  -0.3486518  0.0254999 -13.673  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 196253  on 151287  degrees of freedom
## Residual deviance: 148513  on 151268  degrees of freedom
## AIC: 148553
## 
## Number of Fisher Scoring iterations: 5
```

The backwards model select model arrived at virtually the same results as what we chose via EDA/Inference. For model build 2, the backwards select model included 'copd' while we removed it in model build one. The code below shows the performance metrics of the backwards select model. Looking at these results, the backwards model select performs better than the subset data from model build one at the same threshold of 0.5 in accuracy/precision but performs slightly worse at recall. Accuracy, precision, and recall between Model Build 1 (EDA/Inference) and Model Build 2 (backwards select) were (76.26% vs 76.29%), (74.07% vs 74.56%), and (50.07.60% vs 49.51%) respectively. The decision on which model we preferred will be further discussed in the Final Model section.


```r
set.seed(123)
split <- initial_split(df, prop = .8, strata = has_died)
train_data <- training(split)
test_data <- testing(split)

actual_classes <- test_data$has_died

predicted_probs <- predict(backwards_select_model, newdata = test_data, type = "response")
predicted_classes <- ifelse( predicted_probs > 0.5, 1, 0)
 
# calculate accuracy using caret's confusionMatrix function
conf_matrix <- confusionMatrix(factor(predicted_classes), test_data$has_died, positive='1')
accuracy_value <- conf_matrix$overall["Accuracy"]
precision <- conf_matrix$byClass[["Pos Pred Value"]]
recall <- conf_matrix$byClass[["Sensitivity"]]
f1_score <- 2 * (precision * recall) / (precision + recall)


cat("Accuracy:", round(accuracy_value['Accuracy'], 4), "\n")
```

```
## Accuracy: 0.7629
```

```r
cat("Precision:", round(precision, 4), "\n")
```

```
## Precision: 0.7456
```

```r
cat("Recall:", round(recall, 4), "\n")
```

```
## Recall: 0.4951
```

## ROC Curve

In binary classification, you can assess the performance of a model by looking at the rate of true positives (sensitivity) and the rate of false positives (1 - specificity) of its predictions. The ROC curve (Receiver Operating Characteristic) graphically represents this relationship between the True Positive Rate (TPR) and the False Positive Rate (FPR) with respect to different decision thresholds. In essence, the ROC curve not only gives a visual representation of the binary classification model's performance, but also provides a way to assess how you want choose a threshold based on the requirements of your prediction problem.

The ROC curve has sensitivity [0,1] on the y-axis and 1-specificity [0,1] on the x-axis. The curve on the plot shows TPR vs FPR for different decision thresholds. The solid diagonal line represents an ROC curve that comes from a prediction model that is purely based on random chance.

Therefore, the closer the ROC curve is to the diagonal line, the worse the performance. In addition, in an ideal world where you get 100% TPR and 0% FPR, the ROC curve would "hug" the left/upper part of the graph, forming an elbow at the upper-left corner. Again, this represents perfect performance. With this in mind, the closer the ROC curve is to hugging the graph's upper-left corner, the better the performance since you approach achieving higher TPR values while minimizing the FPR. In the curve below, we see that it's shape approaches the upper left corner which is a positive sign that our model is not predicting randomly but based on the data it was trained on.

In addition to the ROC curve, you can also look at the Area Under the Curve (AUC). This area represents the probability that the model decides that a random positive instance is ranked higher than a random negative instance. It is another way to evaluate the performance of the model. As the model approaches the "ideal upper-left elbow" scenario, the AUC will approach 1. Therefore, AUCs that are closer to 1 are higher performing binary classification models. In our current model, the AUC is 0.8091816.

For determining the optimal decision threshold, that point occurs where Sensitivity and Specificity are maximized. In the case of the ROC curve below it is the part of the curve that is furthest away from the solid diagonal line. This point maximizes true positive (sensitivity) while minimizing the false positives (1-specificity). However, to get the actual threshold value, we must use a command in R to calculate it based off the ROC curve. Using the ROC curve and specifically, the pROC package, we can use the coords() function. The input parameters are the roc_curve object, the method to detect the best threshold (default with "best" is Youden's J statistic), and then which coordinates to return (threshold). Using this method, we get an optimal threshold of around 0.3364265.

While we can calculate the optimal decision threshold, our final threshold decision will take more thought and nuance. For assessing how we want to choose the final threshold for our specified prediction problem, we have to understand the trade-off between False Positives (FP) and False Negatives (FN). FPs are predictions with true labels when they are actually false. FNs are predictions of false labels when they are actually true. A binary classification model cannot optimize the threshold for both FPs and FNs. Intuitively this makes sense as increasing the threshold for predicting a positive class will favor FNs over FPs and decreasing the threshold will favor FPs over FNs. Depending on you problem, you will favor one or the other.

Again, to predict the risk factors of death in Covid-19 patients, you want to exercise the most caution. Therefore, you would favor having higher rates of false positives than false negatives since you want to warn more people about their risk even if some are not at risk of death at all. This opposes a high rate of false negatives where you will see more patients with an actual risk who will not be informed that they are at risk. Therefore, for this binary classification model, a higher rate of FP is preferred and with that, a lower decision threshold. Interestingly, when exploring with threshold values below 0.5 to optimize accuracy and recall, we manually found that a threshold of 0.3 returned the best results. While 0.3 is lower than the optimal threshold found of 0.3364265, we can further take into account exploring an even lower threshold to further prioritize recall.


```r
predicted_probabilities <- predict(backwards_select_model, newdata = test_data, type = "response")
true_labels <- test_data$has_died

# plot ROC
roc_curve <- roc(true_labels, predicted_probabilities)
```

```
## Setting levels: control = 0, case = 1
```

```
## Setting direction: controls < cases
```

```r
# get AUC
auc_value <- auc(roc_curve)

par(pty="s")

plot(roc_curve, main = "ROC Curve",
     col = "blue", lwd = 2, lty = 1, 
     cex.main = 1.2, cex.lab = 1.1, cex.axis = 1.1,
     legacy.axes=TRUE)
# diagonal reference line
abline(a = 0, b = 1, col = "gray", lty = 2, lwd = 2)
```

![](logistic_regression_covid_final2_files/figure-html/ROC Curve backwards select model-1.png)<!-- -->

```r
# decesion thresh
optimal_threshold <- coords(roc_curve, "best", ret = "threshold")$threshold

cat("Optimal Threshold:", optimal_threshold, "\n")
```

```
## Optimal Threshold: 0.3364265
```

```r
cat("Area Under the ROC Curve (AUC-ROC):", auc_value)
```

```
## Area Under the ROC Curve (AUC-ROC): 0.8091816
```

# Final Model


```r
set.seed(123)
split <- initial_split(df, prop = .8, strata = has_died)
train_data <- training(split)
test_data <- testing(split)

actual_classes <- test_data$has_died

predicted_probs <- predict(backwards_select_model, newdata = test_data, type = "response")
predicted_classes <- ifelse( predicted_probs > 0.28, 1, 0)
 
# calculate accuracy using caret's confusionMatrix function
conf_matrix <- confusionMatrix(factor(predicted_classes), test_data$has_died, positive='1')
accuracy_value <- conf_matrix$overall["Accuracy"]
precision <- conf_matrix$byClass[["Pos Pred Value"]]
recall <- conf_matrix$byClass[["Sensitivity"]]
f1_score <- 2 * (precision * recall) / (precision + recall)


cat("Accuracy:", round(accuracy_value['Accuracy'], 4), "\n")
```

```
## Accuracy: 0.6977
```

```r
cat("Precision:", round(precision, 4), "\n")
```

```
## Precision: 0.5489
```

```r
cat("Recall:", round(recall, 4), "\n")
```

```
## Recall: 0.7916
```

### Looking through all our results:

**Model 1: All data, threshold = 0.5**

```         
Accuracy: 0.7626 
Precision: 0.7407 
Recall: 0.5007 
```

**Model 2: Subset of data, threshold = 0.5**

```         
Accuracy: 0.7624 
Precision: 0.7406 
Recall: 0.4997 
```

**Model 3: All data, threshold = 0.3**

```         
Accuracy: 0.71 
Precision: 0.5642 
Recall: 0.7729 
```

**Model 4: Backwards select model, threshold = 0.5**

```         
Accuracy: 0.7629 
Precision: 0.7456 
Recall: 0.4951 
```

**Model 5: Backwards select, threshold = 0.28 (FINAL MODEL)**

```         
Accuracy: 0.6977 
Precision: 0.5489 
Recall: 0.7916 
```

Based on the EDA, model building, model exploration at different parameter values, and the ROC curve, we chose to use the backwards model select with a threshold of 0.28.

### Overview of Final Model Selection:

Using inference with logistic regression in combination with EDA, we observed that there were variables that were statistically insignificant OR had low-impact on the final outcome. These variables were patient_type, copd, and, num_medical_conditons. In our initial exploration, these variables were removed. The remaining features formed the new subset data which we wanted to further train with and explore.

Comparing between the logistic regression with all data and the subset of data (threshold = 0.5), we saw that the model trained on all data performed better. While the feature selected model took out copd, this feature still had significance which may have led to deleterious effects.

For the model built on all data, we then looked at different threshold values [0.1, 0.5] since we wanted to increase recall while maintaining relatively high accuracy. From manually lowering the threshold and testing different values, we found that 0.3 was a good balance between increasing recall and maintaining accuracy.

Next, we looked at another method of model building: backwards select. Through this method, we got nearly identical results as our work done manually with EDA/inference. The results of the backwards model when compared to our all-data model at the same threshold performed better (though moderately) in accuracy/precision, but slightly worse in recall . Because of this, we preferred the backwards model select model.

Lastly, we created an ROC curve based on the backwards select logistic regression model and we used that to assess overall performance while also looking at the optimal decision threshold. The ROC curve showed general positive performance with an AUC of 0.8091816 a curve that bent towards the upper-left corner of the 1-Specificity vs Sensitivity graph. In addition to this, we found that the optimal threshold for our model was 0.3364265 which was very close to our manual analysis. With all of this data, keeping our specific prediction problem in mind, and the desire to maximize recall, we decided on using a final model that was based off backwards select and used a decision threshold of 0.28.

This result leads to a model that has \~80% recall, \~70% accuracy, and \~55% precision. In terms of accuracy, our model is able to correctly predict 70% of at-risk patients out of all patients. For recall, the model can correctly predict 80% of at-risk patients out of all truly at-risk patients. Lastly, for precision, for every time the model predicted that a patient was at risk, 54% of those patients were truly at risk.

With these results, it is clear that we want to exercise the most caution by prioritizing recall in order to warn the most people while also trying to maintain accuracy. On the other hand, while the precision is poor, the harm of a false positive far outweighs the harm of a false negative. Model selection is a nuanced process and takes technical considerations, practical considerations, and ethical ones. It is always important to balance both mathematical results with the real-world outcomes of your model.

# Impact of Variables

Exploring the impact of variables in the final model involved assessing the coefficients associated with each predictor variable and understanding how changes in these variables affect the odds of death. Again, these coefficients represent the log odds. Positive coefficients indicate that an increase in the predictor variable is associated with an increased log odds of the outcome (death), while negative coefficients indicate the opposite.

From the log odds, we also calculated the odds ratio for each predictor variable. For our categorical data the odds ratio represents the change in odds of the outcome (death) associated when comparing a reference variable to another. An odds ratio greater than 1 indicates an increased likelihood of the outcome, while an odds ratio less than 1 indicates a decreased likelihood.

With this information, we could then rank the predictor variables based on their odds ratios to assess their relative importance in predicting the outcome. Variables with a larger magnitude of odds ratios have grater effect on and association with the outcome variable.

In addition, the output of logistic regression also gave significance codes which indicated the statistical significance of each coefficient. The more asterisks $*$, the more statistically significant the variable is in predicting the outcome. For instance, variables with a significance level of 0.001 $***$, 0.01 $**$, or 0.05 $*$ are considered significant. Variables with smaller p-values (and thus more asterisks) are typically considered more influential.

Generating the coefficients from the logistic regression model trained on our subset of data, gave us insights into the impact of each predictor variable on the odds of death among COVID-19 patients.


```r
summary(backwards_select_model)
```

```
## 
## Call:
## glm(formula = has_died ~ usmer + medical_unit + sex + intubed + 
##     pneumonia + age + pregnant + diabetes + copd + asthma + inmsupr + 
##     hipertension + other_disease + cardiovascular + obesity + 
##     renal_chronic + tobacco + clasiffication_final + icu, family = "binomial", 
##     data = train_data)
## 
## Coefficients:
##                        Estimate Std. Error z value Pr(>|z|)    
## (Intercept)          -2.4914344  0.0345384 -72.135  < 2e-16 ***
## usmer                 0.1985486  0.0129499  15.332  < 2e-16 ***
## medical_unit         -0.0416198  0.0018716 -22.237  < 2e-16 ***
## sex                  -0.2822253  0.0134609 -20.966  < 2e-16 ***
## intubed               2.3742392  0.0193282 122.838  < 2e-16 ***
## pneumonia             0.6326187  0.0141589  44.680  < 2e-16 ***
## age                   0.0373380  0.0004287  87.097  < 2e-16 ***
## pregnant             -0.8997110  0.1381796  -6.511 7.46e-11 ***
## diabetes              0.2039590  0.0144852  14.081  < 2e-16 ***
## copd                 -0.0903531  0.0306585  -2.947  0.00321 ** 
## asthma               -0.2385795  0.0446973  -5.338 9.41e-08 ***
## inmsupr               0.1904785  0.0364844   5.221 1.78e-07 ***
## hipertension          0.0632051  0.0148161   4.266 1.99e-05 ***
## other_disease         0.2483636  0.0282011   8.807  < 2e-16 ***
## cardiovascular       -0.1347660  0.0290594  -4.638 3.52e-06 ***
## obesity               0.1091474  0.0159054   6.862 6.78e-12 ***
## renal_chronic         0.3732931  0.0265413  14.065  < 2e-16 ***
## tobacco              -0.1102598  0.0232581  -4.741 2.13e-06 ***
## clasiffication_final -0.1910321  0.0035898 -53.216  < 2e-16 ***
## icu                  -0.3486518  0.0254999 -13.673  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 196253  on 151287  degrees of freedom
## Residual deviance: 148513  on 151268  degrees of freedom
## AIC: 148553
## 
## Number of Fisher Scoring iterations: 5
```

# Variables

### Significant Predictors with Positive Associations:

1.  **Intubated**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of 2.3742392. Indication that when a patient is intubated, the log odds of dying are increased by approximately 2.37, compared to when they are not intubated.
    3.  Odds Ratio (OR): e\^2.3742392, indicating the odds of death are 10.74284 times greater for patients who are intubated vs. not.
2.  **Pneumonia**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of 0.6326187. Indication that when a patient has pneumonia, the log odds of dying are increased by approximately 0.63, compared to when they do not have pneumonia.
    3.  Odds Ratio (OR): e\^0.6326187, indicating the odds of death are 1.882534 times greater for patients who have pneumonia vs. not.
3.  **Renal Chronic**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of 0.3732931. Indication that when a patient has chronic renal disease, the log odds of dying are increased by approximately 0.37, compared to when they do not have the disease.
    3.  Odds Ratio (OR): e\^0.3732931, indicating the odds of death are 1.45251 times greater for patients with chronic renal disease vs those who do not.
4.  **Diabetes**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of 0.2039590. Indication that when a patient is diabetic, the log odds of dying are increased by approximately 0.20, compared to when they are not diabetic.
    3.  Odds Ratio (OR): e\^0.2039590, indicating the odds of death are 1.226248 times greater for patients with a diabetic condition vs. those without the condition.
5.  **Age**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of 0.0373380. Indication that for each additional year in age, the log odds of dying are increased by approximately 0.04.
    3.  Odds Ratio (OR): e\^0.0373380, indicating the odds of death are 1.038044 times greater for each additional year old a patient is.

### Significant Predictors with Negative Associations:

1.  **Pregnant**
    1.  P-value: 7.46e-11, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of -0.8997110. Indication that patients who are pregnant, the log odds of dying are decreased by approximately -0.90, compared to non-pregnant patients.
    3.  Odds Ratio (OR):e\^-0.8997110, indicating the odds of death are 0.4066872 times less for patients who are pregnant vs. those who are not.
2.  **ICU**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of -0.3486518. Indication that patients admitted to the ICU, the log odds of dying are decreased by approximately -0.35, compared to non-ICU admitted patients.
    3.  Odds Ratio (OR):e\^-0.3486518, indicating the odds of death are 0.7056388 times less for patients in the ICU compared to other areas.
3.  **Sex**
    1.  P-value: \< 2e-16, extremely statistically significant. Strong evidence against the null hypothesis of no association.
    2.  Coefficient: Coefficient (Estimate) of -0.2822253. Indication that for females patients, the log odds of dying are decreased by approximately -0.05, compared to male patients.
    3.  Odds Ratio (OR): e\^-0.2822253, indicating the odds of death are 0.7541038 times less for female patients