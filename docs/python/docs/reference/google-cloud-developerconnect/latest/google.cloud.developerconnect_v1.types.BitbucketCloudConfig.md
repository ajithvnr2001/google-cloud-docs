---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.BitbucketCloudConfig
title: Class BitbucketCloudConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:29.265635+00:00
---

# Class BitbucketCloudConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.BitbucketCloudConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BitbucketCloudConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    BitbucketCloudConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for connections to an instance of Bitbucket Cloud.

## Attributes  
  
---  
**Name** | **Description**  
`workspace` |  `str`   
Required. The Bitbucket Cloud Workspace ID to be connected to Google Cloud Platform.   
`webhook_secret_secret_version` |  `str`   
Required. Immutable. SecretManager resource containing the webhook secret used to verify webhook events, formatted as `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*` (if regional secrets are supported in that location). This is used to validate and create webhooks.   
`read_authorizer_credential` |  `[google.cloud.developerconnect_v1.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UserCredential)`   
Required. An access token with the minimum `repository` access. It can either be a workspace, project or repository access token. It's recommended to use a system account to generate the credentials.   
`authorizer_credential` |  `[google.cloud.developerconnect_v1.types.UserCredential](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UserCredential)`   
Required. An access token with the minimum `repository`, `pullrequest` and `webhook` scope access. It can either be a workspace, project or repository access token. This is needed to create webhooks. It's recommended to use a system account to generate these credentials.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
