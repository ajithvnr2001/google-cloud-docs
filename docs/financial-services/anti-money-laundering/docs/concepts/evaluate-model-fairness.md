---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/evaluate-model-fairness/
title: Evaluate model fairness \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:48.868387+00:00
---

# Evaluate model fairness  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/evaluate-model-fairness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Evaluate model fairness Stay organized with collections  Save and categorize content based on your preferences. 

It is crucial to evaluate model fairness to avoid perpetuating biases and discrimination. This page focuses on the importance of fairness assessment in AML risk scoring models, provides insights into the application of equality of odds (as one example measure), and provides potential routes for mitigations.

## Relevance

There are several reasons why model fairness should be evaluated, including the following:

  * Creating or amplifying negative societal biases and harms: Model fairness is vital to prevent discrimination against individuals based on their demographic attributes, such as gender, race, or age.
  * Regulatory compliance: Banks must adhere to legal and ethical standards, including anti-discrimination laws and regulations.
  * Maintaining trust: Fairness in AML risk scoring models helps maintain customer trust and promotes a positive reputation for the bank.



## How to calculate model fairness

There are several ways to assess fairness in machine learning (see [general best practices](https://ai.google/responsibility/responsible-ai-practices/)). We recommend considering [equality of odds](https://developers.google.com/machine-learning/glossary/fairness#equalized-odds) to assess model fairness. In this context, equality of odds measures whether the model provides equal treatment to parties from different demographic groups with respect to their risk scores.

To calculate equality of odds, do the following:

  * Define protected groups that you want to test model fairness for: 
    * Your bank typically has model governance in place on protected categories. These may include gender, race, bucketed age, and other categories.
    * In the [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) table, the fields we recommend to use have a note saying "Typically also used for fairness evaluation".
  * For each protected category, calculate the following metrics:

    * **True Positive Rate (TPR)** : The proportion of individuals correctly classified as high risk among those who are truly high risk based on the risk scores assigned by the model.

The **False Negative Rate (FNR)** is (1 - TPR). This is another way to measure how often a model incorrectly misses the target for a certain group.

    * **False Positive Rate (FPR)** : The proportion of individuals incorrectly classified as high risk among those who are actually low risk based on the risk scores assigned by the model.

You can use this [SQL script template](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/docs/reference/scripts/fairness.sql) for the calculation, adjusting as needed to the particular sensitive dimensions for which you need to do fairness analysis.

  * Compare the TPR and FPR values across different demographic groups.




Important considerations in computing TPR and FPR include the following:

  * Carefully specify the complete set of examples for which TPR and FPR will be calculated; for example, counting all parties in a single line of business once at a specific date _d_.
  * Carefully specify what defines an actual positive example; for example, a party for whom any alert from any system and investigation starting after date _d_ resulted in triggering of the customer exit process for AML-related reasons.
  * Carefully specify what counts as a positive prediction; for example, all customers for whom AML AI risk scores for the date _d_ are above a chosen risk score threshold, which you would use to trigger alerts.



## How to interpret results and mitigation approaches

A **higher false positive rate** for a specific slice or demographic group means that the model is more likely to incorrectly classify individuals from that group as high risk, leading to unnecessary investigations. This indicates that individuals from that demographic group are being disproportionately flagged for investigation, potentially resulting in increased scrutiny or inconvenience for individuals who may not actually pose a higher risk.

A **lower true positive rate** for a specific slice or demographic group means that the model is less effective at correctly classifying individuals from that group as high risk, resulting in a higher rate of false negatives. This indicates that individuals from that demographic group who should be flagged for investigation are more likely to be missed or overlooked by the model compared to other groups.

Disparities in the FPRs and TPRs, and thresholds on when to investigate those further should be considered in your model risk governance process. Where you decide the risk merits further investigation, the following are possible root causes and mitigations to consider.

### Potential root causes

The following list outlines potential root causes for disparities in the false positive rate and the true positive rate between demographic groups:

  * Insufficient positive examples: You have not caught enough of this sort of customer (not enough positive investigations or alerts). You may not be investigating enough or this sort of customer is not risky very often.
  * Many positive examples that are not properly justified: You detect defensive suspicious activity report (SAR) bias or customer exit bias toward a particular customer group.
  * Insufficient total examples: You don't have enough of this sort of customer in your customer base.



Other aspects of data quality and model generation can also impact fairness.

### Mitigation options

The following list outlines mitigation options for the root causes in the previous section:

  * Consider redirecting investigator capacity toward customer groups with higher TPR and / or lower FPR in order to rebalance these values in the future
  * Review the investigation process and historical investigations for biased outcomes for slices with significant disparity in FPR or TPR
  * Randomize the investigations to get more positive examples
  * Review your party supplementary data (see [Supplementary data](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#supplementary-data-tables)). Consider removing data that heavily correlates to sensitive categories and adding data that expresses the underlying (unbiased) risk factor. For example, consider a case where model alerts are concentrated in a few certain ZIP codes. The underlying risk factor could be a concentration of cash-intensive businesses there rather than the geographical area itself.



The following is **not recommended** :

  * Remove parties or risk case events for specific customer groups to rebalance FPR or TPR (in effect, undersampling). Due to the networked nature of AML AI data and features, this may have unpredictable impact on model behavior and performance.



If you still find that model risk governance is blocked on fairness, then we suggest you continue using your current engine version or dataset and [contact support](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/get-support) for additional guidance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
