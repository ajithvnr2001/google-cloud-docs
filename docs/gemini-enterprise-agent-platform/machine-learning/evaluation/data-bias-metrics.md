---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/data-bias-metrics/
title: Data bias metrics for Agent Platform \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:42.637317+00:00
---

# Data bias metrics for Agent Platform  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/data-bias-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Data bias metrics for Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes evaluation metrics you can use to detect _data bias_ , which can appear in raw data and ground truth values even before you train the model. For the examples and notation on this page, we use a hypothetical college application dataset that we describe in detail in [Introduction to model evaluation for fairness](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/intro-evaluation-fairness).

For descriptions of metrics that are generated from post-training data, see [Model bias metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/model-bias-metrics).

## Overview

In our example college application dataset, we have 200 applicants from California in slice 1, and 100 Florida applicants in slice 2, labeled as follows:

Slice | Reject | Accept  
---|---|---  
California | 140 | 60  
Florida | 80 | 20  
  
You can generally interpret the sign for most metrics as follows:

  * Positive value: indicates a potential bias favoring slice 1 over slice 2.

  * Zero value: indicates no bias in between slice 1 and slice 2.

  * Negative value: indicates a potential bias in favoring slice 2 over slice 1.




We make a note where this doesn't apply to a metric.

## Difference in Population Size

_Difference in Population Size_ measures whether there are more examples in slice 1 versus slice 2, normalized by total population of the two slices:

$$ \frac{n_1-n_2}{n_1+n_2} $$ 

(total population of slice 1 - total population of slice 2) / (sum of populations in slice 1 and 2)

**In our example dataset** :

(200 California applicants - 100 Florida applicants)/ 300 total applicants = 100/300 = 0.33.

The positive value of the Difference in Population Size indicates that there are disproportionately more California applicants than Florida applicants. The positive value may or may not indicate bias by itself, but when a model is trained on this data, the model might learn to perform better for California applicants.

## Difference in Positive Proportions in True Labels (DPPTL)

The _Difference in Positive Proportions in True Labels_ measures whether a dataset has disproportionately more positive ground truth labels for one slice over the other. This metric calculates the difference in Positive Proportions in True Labels between slice 1 and slice 2, where Positive Proportions in True Labels for a slice is (Labeled positive outcomes / Total population size). This metric is also known as _Label Imbalance_ :

**Note:** This metric is analogous to the [model bias metric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/model-bias-metrics) of _Difference in Positive Proportions in Predicted Labels_ , which focuses on predicted positive outcomes instead of labeled positive outcomes.

$$ \frac{l^1_1}{n_1} - \frac{l^1_2}{n_2} $$ 

(Labeled positive outcomes for slice 1/Total population size of slice 1) - (Labeled positive outcomes for slice 2/Total population size of slice 2)

**In our example dataset** :

(60 accepted California applicants/200 California applicants) - (20 accepted Florida applicants/100 Florida applicants) = 60/200 - 20/100 = 0.1.

The positive value of the DPPTL indicates that the dataset has disproportionately higher positive outcomes for California applicants compared to Florida applicants. The positive value may or may not indicate bias by itself, but when a model is trained on this data, the model might learn to predict disproportionately more positive outcomes for California applicants.

## What's next

  * Learn about the [model bias metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/evaluation/model-bias-metrics) supported by Gemini Enterprise Agent Platform.

  * Read the [model evaluation pipeline component reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/model-evaluation-component#fairness).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
