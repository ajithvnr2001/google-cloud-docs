---
url: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/AccessSecretVersionResponse/
title: AccessSecretVersionResponse \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:37:33.118733+00:00
---

# AccessSecretVersionResponse  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/AccessSecretVersionResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/secret-manager/docs/apis)



Send feedback 

#  AccessSecretVersionResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `[SecretManagerService.AccessSecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/access#google.cloud.secretmanager.v1.SecretManagerService.AccessSecretVersion)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "payload": {
        object ([SecretPayload](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/SecretPayload))
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name of the `[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions#SecretVersion)` in the format `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*`.  
`payload` |  `object (`[SecretPayload](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/SecretPayload)`)` Secret payload  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
