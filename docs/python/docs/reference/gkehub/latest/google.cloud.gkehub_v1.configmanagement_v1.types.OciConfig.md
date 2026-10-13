---
url: https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1.configmanagement_v1.types.OciConfig
title: Class OciConfig (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:13.041271+00:00
---

# Class OciConfig (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1.configmanagement_v1.types.OciConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OciConfig (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.1  1.24.0  1.23.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.3  1.16.0  1.15.1  1.14.2  1.13.1  1.12.1  1.11.0  1.10.2  1.9.0  1.8.1  1.7.1  1.6.0  1.5.3  1.4.3  1.3.0  1.2.0  1.1.0  1.0.0  0.2.2  0.1.2 
    
    
    OciConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

OCI repo configuration for a single cluster

## Attributes  
  
---  
**Name** | **Description**  
`sync_repo` |  `str`   
The OCI image repository URL for the package to sync from. e.g. `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`.   
`policy_dir` |  `str`   
The absolute path of the directory that contains the local resources. Default: the root directory of the image.   
`sync_wait_secs` |  `int`   
Period in seconds between consecutive syncs. Default: 15.   
`secret_type` |  `str`   
Type of secret configured for access to the Git repo.   
`gcp_service_account_email` |  `str`   
The Google Cloud Service Account Email used for auth when secret_type is gcpServiceAccount.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
