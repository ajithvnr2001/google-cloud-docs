---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnosticConfig
title: Class DiagnosticConfig (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:38.718333+00:00
---

# Class DiagnosticConfig (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnosticConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DiagnosticConfig (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    DiagnosticConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines flags that are used to run the diagnostic tool

## Attributes  
  
---  
**Name** | **Description**  
`gcs_bucket` |  `str`   
Required. User Cloud Storage bucket location (REQUIRED). Must be formatted with path prefix (`gs://$GCS_BUCKET`). Permissions: User Managed Notebooks: \- storage.buckets.writer: Must be given to the project's service account attached to VM. Google Managed Notebooks: \- storage.buckets.writer: Must be given to the project's service account or user credentials attached to VM depending on authentication mode. Cloud Storage bucket Log file will be written to `gs://$GCS_BUCKET/$RELATIVE_PATH/$VM_DATE_$TIME.tar.gz`  
`relative_path` |  `str`   
Optional. Defines the relative storage path in the Cloud Storage bucket where the diagnostic logs will be written: Default path will be the root directory of the Cloud Storage bucket (`gs://$GCS_BUCKET/$DATE_$TIME.tar.gz`) Example of full path where Log file will be written: `gs://$GCS_BUCKET/$RELATIVE_PATH/`  
`repair_flag_enabled` |  `bool`   
Optional. Enables flag to repair service for instance   
`packet_capture_flag_enabled` |  `bool`   
Optional. Enables flag to capture packets from the instance for 30 seconds   
`copy_home_files_flag_enabled` |  `bool`   
Optional. Enables flag to copy all `/home/jupyter` folder contents   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
