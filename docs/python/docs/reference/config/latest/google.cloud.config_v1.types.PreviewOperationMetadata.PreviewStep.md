---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewOperationMetadata.PreviewStep
title: Class PreviewStep (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:46.784776+00:00
---

# Class PreviewStep (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.PreviewOperationMetadata.PreviewStep

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PreviewStep (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    PreviewStep(value)

The possible steps a preview may be running.

## Enums  
  
---  
**Name** | **Description**  
`PREVIEW_STEP_UNSPECIFIED` | Unspecified preview step.  
`PREPARING_STORAGE_BUCKET` | Infra Manager is creating a Google Cloud Storage bucket to store artifacts and metadata about the preview.  
`DOWNLOADING_BLUEPRINT` | Downloading the blueprint onto the Google Cloud Storage bucket.  
`RUNNING_TF_INIT` | Initializing Terraform using `terraform init`.  
`RUNNING_TF_PLAN` | Running `terraform plan`.  
`FETCHING_DEPLOYMENT` | Fetching a deployment.  
`LOCKING_DEPLOYMENT` | Locking a deployment.  
`UNLOCKING_DEPLOYMENT` | Unlocking a deployment.  
`SUCCEEDED` | Operation was successful.  
`FAILED` | Operation failed.  
`VALIDATING_REPOSITORY` | Validating the provided repository.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
