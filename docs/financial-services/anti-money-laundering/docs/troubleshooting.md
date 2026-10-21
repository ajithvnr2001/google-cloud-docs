---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/troubleshooting/
title: Troubleshoot AML AI \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:49.215750+00:00
---

# Troubleshoot AML AI  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Troubleshoot AML AI Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with AML AI.

## Permission errors

This section lists permission errors that you might encounter and provides suggestions for how to fix each of them.

### The service account doesn't have permission to access the KMS key

The API automatically creates a service account in your project. The service account needs access to the CMEK key so it can use the key to encrypt and decrypt the underlying data. (It also needs read access to the BigQuery input dataset to be used for creating models, and it needs write access to the BigQuery output dataset.) The following error occurs when the service account does not have permission to access the KMS key:
    
    
    Error code 400 - service-account@gcp-sa-financialservices.iam.gserviceaccount.com
    lacks permissions to KMS key
    

To resolve this issue, grant access to the key. For more information, see [Grant access to the CMEK key](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance#grant-access-cmek).

## Dataset issues

This section lists dataset issues that you might encounter and provides suggestions for how to fix each of them.

### Unexpected results

A Financial Services API dataset resource is a pointer to data in BigQuery. It does not hold or point to any specific snapshot of the data in these tables. If data is modified after a dataset is created (for example, if records are deleted), this will be reflected in the results of other calls to the API (for example, the creation of new models or when running predictions).

To reduce the occurrences of unexpected results, be sure to maintain the integrity of the data in BigQuery.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
