---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/best-practices-investigation-process/
title: Best practices for your investigation process \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:48.360044+00:00
---

# Best practices for your investigation process  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/best-practices-investigation-process/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Best practices for your investigation process Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines best practices for using risk scores and explainability.

## Using risk scores

Risk scores can be used in your investigation process to prioritize investigations of high-risk parties.

Common approaches include alerting based on investigator load or based on a chosen risk level:

  * _Capacity led:_ Alert or investigate the top _n_ parties in the output table based on risk score in descending order, depending on available investigator volume.

**Note:** Consider modifying investigator volume over time through assessment of the implied risk level (for example, a marginal conversion rate of lowest scoring alerted cases).
  * _Risk led:_ Alert or investigate all parties with a risk score above a fixed threshold that is fixed month-to-month. This is also based on backtest results which give an acceptable level of a recall of previous cases and discovery of new risk. For more information, see [Collect model and risk governance artifacts](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/collect-model-risk-governance-artifacts).

**Note:** Risk score threshold should be re-evaluated when using a new or retrained model, because the same threshold may correspond to a different risk level depending on the dataset or other aspects of the model.



## Using explainability

The feature families with the highest positive attribution scores can be provided to investigators to direct their investigations, to decrease the time needed per investigation or increase success rate. Experience suggests that negative scores (which indicates a feature family has reduced the risk of a case) can be difficult for an investigator to use and some AML AI customers don't show these to their investigators. For best results, consider what training or guidance your investigators need to handle investigations related to different feature families.

You might also use explainability for other purposes:

  * determining if a customer's behavior has changed enough to merit a fresh investigation for a 2nd or repeated alert for this customer
  * deriving aggregate insights from feature family contributions over time



## Filtering out repeated alerts

AML AI risk scores identify high-risk parties, but don't separate out repeat alerts. For example, a customer presenting a high risk in March 2023 may have a similarly high score in April 2023, generating two consecutive cases despite their behavior remaining the same. You might want to apply rules to filter out repeated alerts to avoid re-alerting a party with a current or recently completed investigation without significant change in risk score or explainability.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
