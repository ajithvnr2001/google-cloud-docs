---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.simulations.valuedResources
title: REST Resource: organizations.locations.simulations.valuedResources \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:58.084656+00:00
---

# REST Resource: organizations.locations.simulations.valuedResources  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.simulations.valuedResources

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  REST Resource: organizations.locations.simulations.valuedResources Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ValuedResource
    * JSON representation
    * ResourceValue
  * Methods



## Resource: ValuedResource

A resource that is determined to have value to a user's system

JSON representation  
---  
      
    
    {
      "name": string,
      "resource": string,
      "resourceType": string,
      "displayName": string,
      "resourceValue": enum ([ResourceValue](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.simulations.valuedResources#ValuedResource.ResourceValue)),
      "exposedScore": number,
      "resourceValueConfigsUsed": [
        {
          object ([ResourceValueConfigMetadata](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/ResourceValueConfigMetadata))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Valued resource name, for example, e.g.: `organizations/123/simulations/456/valuedResources/789`  
`resource` |  `string` The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the valued resource.  
`resourceType` |  `string` The [resource type](https://cloud.google.com/asset-inventory/docs/supported-asset-types) of the valued resource.  
`displayName` |  `string` Human-readable name of the valued resource.  
`resourceValue` |  `enum (`[ResourceValue](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.simulations.valuedResources#ValuedResource.ResourceValue)`)` How valuable this resource is.  
`exposedScore` |  `number` Exposed score for this valued resource. A value of 0 means no exposure was detected exposure.  
`resourceValueConfigsUsed[]` |  `object (`[ResourceValueConfigMetadata](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/ResourceValueConfigMetadata)`)` List of resource value configurations' metadata used to determine the value of this resource. Maximum of 100.  
  
### ResourceValue

How valuable the resource is.

Enums  
---  
`RESOURCE_VALUE_UNSPECIFIED` | The resource value isn't specified.  
`RESOURCE_VALUE_LOW` | This is a low-value resource.  
`RESOURCE_VALUE_MEDIUM` | This is a medium-value resource.  
`RESOURCE_VALUE_HIGH` | This is a high-value resource.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.simulations.valuedResources/get)`

|  Get the valued resource by name  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
