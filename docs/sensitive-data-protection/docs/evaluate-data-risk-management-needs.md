---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/evaluate-data-risk-management-needs/
title: Evaluate your data risk management needs \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:50.995558+00:00
---

# Evaluate your data risk management needs  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/evaluate-data-risk-management-needs/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Evaluate your data risk management needs Stay organized with collections  Save and categorize content based on your preferences. 

This series of documents provides strategies for evaluating and mitigating data risk in your organization. It also describes and compares two Sensitive Data Protection services that help you learn more about your current data security posture.

## Objectives of data risk management

Managing data risk involves storing, processing, and using your data within the appropriate risk levels for your business. When you perform data risk management, we recommend that you aim for the following objectives:

  * Your data is properly discovered and classified.
  * Risk of data exposure is properly understood.
  * Data is protected by appropriate controls or de-risked through obfuscation.



As you evaluate your data workloads you can start by asking these questions:

  * What kind of data does this workload handle and is any of it sensitive?
  * Is this data properly exposed? For example, is access to the data restricted to the right users, in the right environment, and for an approved purpose?
  * Can the risk of this data be reduced through data minimization and obfuscation strategies?



Taking a well-informed and risk-based approach can help you make the most of your data without compromising the privacy of your users.

## Example analysis

For this example, suppose your data team is trying to build a machine learning model based on customer feedback in product reviews.

### What kind of data does this workload handle and is any of it sensitive?

In the data workload, you found that the primary key used is the customer email address. Customer email addresses often contain the customers' names. Additionally, the actual product reviews contain unstructured data (or _freeform data_) submitted by the customer. Unstructured data can contain intermittent instances of sensitive data like phone numbers and addresses.

### Is this data properly exposed?

You found that the data is accessible only to the product team. However, you want to share the data to your data analytics team, so that they can use it to build a machine learning model. Exposing the data to more people also means exposing it to more development environments where this data will be stored and processed. You determined that the exposure risk will increase.

### Can the risk of this data be reduced through data minimization and obfuscation strategies?

You know that the analytics team doesn't need any of the actual sensitive personally identifiable information (PII) in the dataset. However, they need to aggregate the data per customer. They need a way to determine which reviews belong to the same customer. To address this need, you decide to tokenize all the structured PII—the customer email addresses—to keep the referential integrity of your data. You also decide to inspect the unstructured data—the reviews—and mask any intermittent sensitive data within it.

## What's next

  * [Compare Sensitive Data Protection services that help you learn about your data](https://docs.cloud.google.com/sensitive-data-protection/docs/learn-about-your-data) (next document in this series) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
