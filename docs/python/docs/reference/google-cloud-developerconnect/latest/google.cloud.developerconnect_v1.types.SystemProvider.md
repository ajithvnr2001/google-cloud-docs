---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.SystemProvider
title: Class SystemProvider (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:44.873263+00:00
---

# Class SystemProvider (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.SystemProvider

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SystemProvider (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    SystemProvider(value)

SystemProvider is a list of providers that are owned by Developer Connect.
    
    
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/documents.readonly".
    SENTRY (4):
        Sentry provider.
        Scopes can be found at
        https://docs.sentry.io/api/permissions/
    ROVO (5):
        Rovo provider.
        Must select the "rovo" scope.
    NEW_RELIC (6):
        New Relic provider.
        No scopes are allowed.
    DATASTAX (7):
        Datastax provider.
        No scopes are allowed.
    DYNATRACE (8):
        Dynatrace provider.
    

## Enums  
  
---  
**Name** | **Description**  
`SYSTEM_PROVIDER_UNSPECIFIED` | No system provider specified.  
`GITHUB` | GitHub provider. Scopes can be found at https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes  
`GITLAB` | GitLab provider. Scopes can be found at https://docs.gitlab.com/user/profile/personal_access_tokens/#personal-access-token-scopes  
`GOOGLE` | Google provider. Recommended scopes:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
