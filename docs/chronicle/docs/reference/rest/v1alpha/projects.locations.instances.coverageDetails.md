---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.coverageDetails
title: REST Resource: projects.locations.instances.coverageDetails \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:04.021551+00:00
---

# REST Resource: projects.locations.instances.coverageDetails  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.coverageDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.coverageDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CoverageDetails
    * JSON representation
  * Methods



## Resource: CoverageDetails

Provides coverage details for a threat collection and rule combination.

JSON representation  
---  
      
    
    {
      "name": string,
      "threatCollection": string,
      "rule": string,
      "coveredAttackDetails": {
        object ([AttackDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/SecurityResult#AttackDetails))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the coverage details. Format: projects/{project}/locations/{location}/instances/{instance}/coverageDetails/{coverageDetails}  
`threatCollection` |  `string` Output only. Resource name of the matching ThreatCollection  
`rule` |  `string` Output only. Resource name of the matching Rule  
`coveredAttackDetails` |  `object (`[AttackDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/SecurityResult#AttackDetails)`)` Output only. MITRE ATT&CK TTPs used in the campaign that were detected by this rule.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.coverageDetails/get)`

|  Get coverage details for a threat collection and rule combination.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.coverageDetails/list)`

|  List coverage details for threat collection and rule combinations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-13 UTC."],[],[]] 
