---
url: https://docs.cloud.google.com/storage-transfer/docs/cmek/
title: Customer-managed encryption keys \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:49.523498+00:00
---

# Customer-managed encryption keys  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

If you're using Secret Manager to store and pass your Amazon S3 or Microsoft Azure credentials, you can additionally use a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/cmek) (CMEK) to encrypt those credentials at rest.

See [Enable Customer-Managed Encryption Keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek) for instructions.

## Enforce CMEK with organization policy

To enforce the use of CMEK through an [organizational policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview), add Storage Transfer Service and Secret Manager to the `constraints/gcp.restrictNonCmekServices` deny list. Specifically, add:

  * `secretmanager.googleapis.com`
  * `storagetransfer.googleapis.com`



See [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) for instructions.

Storage Transfer Service checks for and enforces this restriction at job creation and update. Existing transfer jobs are not affected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
