---
url: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/ListSecurityCenterServicesResponse/
title: ListSecurityCenterServicesResponse \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:53.226469+00:00
---

# ListSecurityCenterServicesResponse  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/ListSecurityCenterServicesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  ListSecurityCenterServicesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `[SecurityCenterManagement.ListSecurityCenterServices](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/projects.locations.securityCenterServices/list#google.cloud.securitycentermanagement.v1.SecurityCenterManagement.ListSecurityCenterServices)`.

JSON representation  
---  
      
    
    {
      "securityCenterServices": [
        {
          object ([SecurityCenterService](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.securityCenterServices#SecurityCenterService))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`securityCenterServices[]` |  `object (`[SecurityCenterService](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.securityCenterServices#SecurityCenterService)`)` The list of services.  
`nextPageToken` |  `string` A pagination token. To retrieve the next page of results, call the method again with this token.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-01 UTC."],[],[]] 
