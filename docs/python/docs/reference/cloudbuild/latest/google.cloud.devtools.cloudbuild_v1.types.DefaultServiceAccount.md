---
url: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount
title: Class DefaultServiceAccount (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:35.606823+00:00
---

# Class DefaultServiceAccount (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DefaultServiceAccount (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.1  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.3  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.2  3.23.3  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.1  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.1  3.10.0  3.9.3  3.8.3  3.7.1  3.6.0  3.5.2  3.4.0  3.3.2  3.2.1  3.1.1  3.0.2  2.0.2  1.1.2  1.0.0  0.1.0 
    
    
    DefaultServiceAccount(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The default service account used for `Builds`.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Format: `projects/{project}/locations/{location}/defaultServiceAccount`  
`service_account_email` |  `str`   
Output only. The email address of the service account identity that will be used for a build by default. This is returned in the format `projects/{project}/serviceAccounts/{service_account}` where `{service_account}` could be the legacy Cloud Build SA, in the format [PROJECT_NUMBER]@cloudbuild.gserviceaccount.com or the Compute SA, in the format [PROJECT_NUMBER]-compute@developer.gserviceaccount.com. If no service account will be used by default, this will be empty.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
