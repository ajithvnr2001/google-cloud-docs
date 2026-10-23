---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles-remediation/
title: Remediate findings from the data profiler \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:51.330680+00:00
---

# Remediate findings from the data profiler  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles-remediation/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Remediate findings from the data profiler Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps you can take to remediate [findings](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation) from data profiles.

## High data risk

Data assets with high data risk have evidence of sensitive information without additional protections. To lower the data risk score, consider doing the following:

  * For BigQuery columns that contain sensitive data, apply a [BigQuery policy tag](https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags) to restrict access to accounts with specific access rights.

Before you make this change, make sure your service agent has the permissions required to profile tables with column-level restrictions. Otherwise, Sensitive Data Protection shows an error. For more information, see [Troubleshoot issues with the data profiler](https://docs.cloud.google.com/sensitive-data-protection/docs/troubleshoot-data-profiles#policy-tags).

  * De-identify the raw sensitive data using de-identification techniques like [masking](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#charactermaskconfig) and [tokenization](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization).

  * [Enable automatic tagging](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity#enable-automatic-tagging-discovery) and opt to automatically set the data risk of the profiled data assets to `Low`.

  * If the high-risk data is not needed, consider removing it.

**Note:** If you delete a column from a table and that table is reprofiled, no [column data profile](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#column-data-profile) is generated for the deleted column. If you want to keep a history of past data profiles—for example, for auditing purposes—[configure the profiler to export data profiles to BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#save-to-bq). 




## High free-text score

A column with a high [free-text score](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#free-text-score), especially one that has evidence of multiple infoTypes (like `PHONE_NUMBER`, `US_SOCIAL_SECURITY_NUMBER`, and `DATE_OF_BIRTH`), might contain unstructured data and instances of personally identifiable information (PII). This column can be a note or comment field. Freeform text presents a potential risk. For example, in such fields, someone might enter "Customer was born on January 1, 1985".

Sensitive Data Protection is built to handle unstructured data. To better understand this kind of data, consider doing the following:

  * For BigQuery and Cloud Storage data, you can identify the exact locations of the PII by running an [on-demand inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) on the BigQuery table or Cloud Storage bucket.

  * De-identify the raw sensitive data using techniques like [masking](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#charactermaskconfig) and [tokenization](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization).




## What's next

  * Learn about how Sensitive Data Protection [calculates the data risk and sensitivity levels of your data assets](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

  * Learn about how [tokenization makes data usable without sacrificing privacy](https://cloud.google.com/blog/products/identity-security/take-charge-of-your-data-how-tokenization-makes-data-usable-without-sacrificing-privacy).

  * Learn about how [Forrester named Google Cloud a leader in unstructured data security platforms](https://cloud.google.com/blog/products/identity-security/google-a-leader-in-unstructured-data-security-platforms).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
