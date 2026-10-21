---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis/
title: Measuring re-identification and disclosure risk \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:46.621400+00:00
---

# Measuring re-identification and disclosure risk  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Measuring re-identification and disclosure risk Stay organized with collections  Save and categorize content based on your preferences. 

_Re-identification risk analysis_ , or just _risk analysis_ , is the process of analyzing sensitive data to find properties that might increase the risk of subjects being identified. You can use risk analysis methods before de-identification to help determine an effective de-identification strategy or after de-identification to monitor for any changes or outliers.

Sensitive Data Protection can compute four re-identification risk metrics: _k_ -anonymity, _l_ -diversity, _k_ -map, and _δ_ -presence. If you're not familiar with risk analysis or these metrics, see the [risk analysis concept topic](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) before continuing on.

This section provides overviews of how to use Sensitive Data Protection for risk analysis of structured data using any of these metrics, plus other related topics.

## Calculate re-identification risk

Sensitive Data Protection can analyze your structured data stored in BigQuery tables and compute the following re-identification risk metrics. Click the link for the metric you want to calculate to learn more.

Metric | Description  
---|---  
[_k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity) | A property of a dataset that indicates the re-identifiability of its records. A dataset is _k_ -anonymous if quasi-identifiers for each person in the dataset are identical to at least _k_ – 1 other people also in the dataset.  
[_l_ -diversity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity) | An extension of _k_ -anonymity that additionally measures the diversity of sensitive values for each column in which they occur. A dataset has _l_ -diversity if, for every set of rows with identical quasi-identifiers, there are at least _l_ distinct values for each sensitive attribute.  
[_k_ -map](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-map) | Computes re-identifiability risk by comparing a given de-identified dataset of subjects with a larger re-identification—or "attack"—dataset.  
[_δ_ -presence](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-d-presence) | Estimates the probability that a given user in a larger population is present in the dataset. This is used when membership in the dataset is itself sensitive information.  
  
## Calculate other statistics

Sensitive Data Protection can also compute numerical and categorical statistics for data stored in BigQuery tables using the same [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource as the risk analysis APIs.

Metric | Description  
---|---  
[Numerical statistics](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-stats#compute-num-stats) | Determines minimum, maximum, and quantile values for an individual BigQuery column.  
[Categorical numerical statistics](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-stats#compute-cat-num-stats) | Computes categorical numerical statistics for the individual histogram buckets within a BigQuery column.  
  
For more information, see [Computing numerical and categorical statistics](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-stats).

## Visualize re-identification risk

You can visualize the risk metrics that Sensitive Data Protection calculates directly in the Google Cloud console using Sensitive Data Protection ([_k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity#viewing-results) or [_l_ -diversity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity#viewing-results)), or using other Google Cloud products.

Product | Description  
---|---  
[Data Studio](https://docs.cloud.google.com/sensitive-data-protection/docs/visualizing_re-id_risk) | After calculating [_k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-anonymity) values for a dataset using Sensitive Data Protection, you can visualize the results in Data Studio. By doing so, you'll also be able to better understand re-identification risk and help evaluate the trade-offs in utility you might be making if you redact or de-identify data.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
