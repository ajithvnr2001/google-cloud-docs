---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions
title: REST Resource: projects.locations.instances.caseTagDefinitions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:51.929669+00:00
---

# REST Resource: projects.locations.instances.caseTagDefinitions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.caseTagDefinitions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseTagDefinition
    * JSON representation
  * MatchCriteria
  * CompareType
  * Methods



## Resource: CaseTagDefinition

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Tags are assigned to cases by Google Security Operations based on predefined rules and can be used to classify cases or find specific cases faster. Note that you can manually add tags to a case from the Cases page. These tags can be removed from the case, but NOT removed entirely from the system.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "matchCriteria": enum ([MatchCriteria](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions#MatchCriteria)),
      "value": string,
      "propertyName": string,
      "comparisonType": enum ([CompareType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions#CompareType)),
      "priority": integer,
      "canBeCaseTitle": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the CaseTagDefinition. Format: projects/{project}/locations/{location}/instances/{instance}/caseTagDefinitions/{caseTagDefinition}  
`displayName` |  `string` Required. This is the name of the tag that will be applied to the case.  
`matchCriteria` |  `enum (`[MatchCriteria](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions#MatchCriteria)`)` Required. Classify cases based on a criteria.  
`value` |  `string` Required. Specific value to search in case - in addition to SearchIn property.  
`propertyName` |  `string` Optional. Specific Entity property name to search in case. this is relevant only when a SearchIn of type BY_ENTITY_PROPERTY_NAME was chosen.  
`comparisonType` |  `enum (`[CompareType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions#CompareType)`)` Required. The type of comparison to be used when comparing the value to the case. This is relevant only when a SearchIn of type BY_ENTITY_PROPERTY_NAME was chosen.  
`priority` |  `integer` Required. Note that Google Security Operations merges priority with other alerts and entities and events so that the priority here is not absolute.  
`canBeCaseTitle` |  `boolean` Required. When checked, the tag will be assigned as the title of the case if it meets the conditions. default is false.  
  
## MatchCriteria

The criteria to match the case against.

Enums  
---  
`MATCH_CRITERIA_UNSPECIFIED` | Unspecified match criteria.  
`BY_VENDOR` | e.g. Palo alto.  
`BY_PRODUCT` | e.g. IPS, EDR.  
`BY_RULE_GENERATOR` | e.g. Data exfiltration.  
`BY_ENTITY_PROPERTY_NAME` | e.g. by one of the unique entities.  
`DATA_DRIVEN` | e.g. data driven tags.  
`SYSTEM` | e.g. system tags.  
  
## CompareType

The type of comparison to be used when comparing the value to the case.

Enums  
---  
`COMPARE_TYPE_UNSPECIFIED` | Unspecified compare type.  
`EXACT` | Exact match.  
`START_WITH` | Starts with.  
`CONTAIN` | Contains.  
`ENDS_WITH` | Ends with.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions/create)`

|  Creates a new CaseTagDefinition.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions/delete)`

|  Deletes a CaseTagDefinition.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions/get)`

|  Gets a single CaseTagDefinition by its resource name.  
  
### `[import](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions/import)`

|  Imports CaseTagDefinitions from a CSV file.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions/list)`

|  Lists all CaseTagDefinitions available in the instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseTagDefinitions/patch)`

|  Updates an existing CaseTagDefinition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
