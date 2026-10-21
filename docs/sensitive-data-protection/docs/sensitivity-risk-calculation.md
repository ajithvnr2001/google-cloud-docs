---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation/
title: Sensitivity and data risk levels \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:00.555203+00:00
---

# Sensitivity and data risk levels  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Sensitivity and data risk levels Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the data risk and sensitivity levels that Sensitive Data Protection assigns to [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). To understand the data risk levels, it's important to understand the sensitivity levels first.

**Note:** When generating data profiles, Sensitive Data Protection scans for only the infoTypes that you specify in your [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template). For example, suppose credit card numbers are present in a column. If the `CREDIT_CARD_NUMBER` infoType isn't listed in your inspection template, then the resulting sensitivity and data risk levels for that column don't reflect the presence of credit card numbers.

## Sensitivity level

_Sensitivity level_ is an indication of how sensitive the data in a project, table, or file store is. Data is sensitive if it contains detected elements, such as personally identifiable information (PII), financial data, and credentials.

You can also set the sensitivity of each built-in or custom infoType that you scan for. The sensitivity of each detected infoType affects the resulting sensitivity rating of the profiled resource. For information about how to override the sensitivity of a built-in infoType or set the sensitivity of a custom infoType, see [Manage infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-infotypes-console).

A data profile can have any of the following sensitivity levels:

High
    [Highly sensitive information](https://docs.cloud.google.com/sensitive-data-protection/docs/high-sensitivity-infotypes-reference) might be present, including credit card numbers and certain national identifiers.
Moderate
    Sensitive information that is not classified as highly sensitive might be present. Examples are email addresses and phone numbers, which can be considered personally identifiable. The data might also include freeform text or unstructured data, such as comments.
Low
    Sensitive information wasn't detected, and the data doesn't include freeform text or unstructured data.
Unknown
    The data couldn't be scanned successfully. It is uncertain if sensitive data exists.

### Sensitivity signals

To calculate sensitivity, Sensitive Data Protection considers the following:

  * Both the default sensitivity of each infoType found along with any user overrides of the sensitivity.
  * The [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) that [highly sensitive infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/high-sensitivity-infotypes-reference) are present.
  * Whether the data has an unstructured format and contains mostly freeform text, like comments.



## Data risk level

_Data risk level_ is the risk associated with the data in its current state. It considers the sensitivity level of the data in the resource and the presence of access controls to protect that data.

High
    [High-sensitivity data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#high-sensitivity) might be present, and there are no access controls to restrict data exposure. Alternatively, moderate or high-sensitivity data is widely accessible.
Moderate
    [Moderate-sensitivity data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#moderate-sensitivity) might be present, and there are no access controls to restrict data exposure.
Low
    

The sensitivity level of the data is low. Alternatively, access to the data has been further restricted, for example, through access controls.

A profiled data asset can also get a `Low` data risk level if you [enabled automatic tagging](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity#enable-automatic-tagging-discovery) and opted to automatically set the data risk of the profiled data assets to `Low`.

Unknown
    

The data couldn't be scanned successfully. It is uncertain if sensitive data exists.

### Data risk signals

To calculate data risk, Sensitive Data Protection considers the following:

  * The calculated sensitivity level of the data.
  * The presence of access controls that limit access to the data.
  * Whether discovery is configured to set the data risk level to `Low` when automatic tagging is enabled. For more information, see [Enable the automatic tagging in the discovery configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity#enable-automatic-tagging-discovery). This option automatically overrides any of the storage-specific formulas.



### BigQuery data risk calculation

The following table shows how data risk signals affect the resulting data risk level that Sensitive Data Protection assigns to profiled BigQuery resources. The **Data risk** column shows the resulting data risk level.

Data sensitivity | Is public | Column policy tag applied | **Data risk**  
---|---|---|---  
Low, moderate, or high| No| Yes| Low  
Low, moderate, or high| Yes| Yes| Low  
Low| No| No| Low  
Moderate| No| No| Moderate  
High| No| No| High  
  
### Cloud SQL data risk calculation

The following table shows how data risk signals affect the resulting data risk level that Sensitive Data Protection assigns to profiled Cloud SQL resources. The **Data risk** column shows the resulting data risk level.

Data sensitivity | Requires SSL | Public IP | **Data risk**  
---|---|---|---  
Low| Yes| Yes| Low  
Low| Yes| No| Low  
Low| No| Yes| Low  
Low| No| No| Low  
Moderate| Yes| Yes| Moderate  
Moderate| Yes| No| Low  
Moderate| No| Yes| High  
Moderate| No| No| Moderate  
High| Yes| Yes| High  
High| Yes| No| Moderate  
High| No| Yes| High  
High| No| No| High  
  
### File store data risk calculation

The following table shows how data risk signals affect the resulting data risk level that Sensitive Data Protection assigns to profiled file store resources. The **Data risk** column shows the resulting data risk level.

Data sensitivity | Could contain public files | **Data risk**  
---|---|---  
Low| No| Low  
Low| Inconclusive [`resourceVisibility`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)| Low  
Low| Yes| Low  
Moderate| No| Low  
Moderate| Inconclusive [`resourceVisibility`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)| Moderate  
Moderate| Yes| High  
High| No| Moderate  
High| Inconclusive [`resourceVisibility`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)| High  
High| Yes| High  
Unknown| No| Unknown  
Unknown| Inconclusive [`resourceVisibility`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)| Unknown  
Unknown| Yes| Unknown  
  
## What's next

  * Learn about [remediations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles-remediation) you can take to reduce data risk and sensitivity.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
