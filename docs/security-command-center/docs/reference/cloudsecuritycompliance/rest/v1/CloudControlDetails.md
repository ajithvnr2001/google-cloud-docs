---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/CloudControlDetails/
title: CloudControlDetails \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:09.936369+00:00
---

# CloudControlDetails  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/CloudControlDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  CloudControlDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The details of a cloud control.

JSON representation  
---  
      
    
    {
      "name": string,
      "majorRevisionId": string,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Parameter))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the cloud control, in one of the following formats: `organizations/{organization}/locations/{location}/cloudControls/{cloudControl}` or `projects/{project}/locations/{location}/cloudControls/{cloudControl}`.The only supported location is `global`.  
`majorRevisionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The major version of the cloud control.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Parameter)`)` Optional. Parameters are key-value pairs that let you provide your custom location requirements, environment requirements, or other settings that are relevant to the cloud control. An example parameter is `{"name": "location","value": "us-west-1"}`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
