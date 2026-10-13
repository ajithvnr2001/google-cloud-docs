---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues
title: REST Resource: projects.locations.instances.cases.alerts.customFieldValues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:59.594925+00:00
---

# REST Resource: projects.locations.instances.cases.alerts.customFieldValues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.cases.alerts.customFieldValues Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CustomFieldValue
    * JSON representation
    * CustomFieldScope
  * Methods



## Resource: CustomFieldValue

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Custom Fields are fields defined on a global level for alert and/or case scope. Custom fields are values set for a specific identifier and scope

JSON representation  
---  
      
    
    {
      "name": string,
      "customFieldId": string,
      "scope": enum ([CustomFieldScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues#CustomFieldValue.CustomFieldScope)),
      "scopeId": string,
      "values": [
        string
      ],
      "valuesSearchText": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique identifier of the resource.  
`customFieldId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The id of the parent CustomField that owns this CustomFieldValue  
`scope` |  `enum (`[CustomFieldScope](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues#CustomFieldValue.CustomFieldScope)`)` Output only. Scope of the value.  
`scopeId` |  `string` Required. Identifier of the value referencing case or alert.  
`values[]` |  `string` Required. The custom field value.  
`valuesSearchText` |  `string` Output only. Specific field represents the `values` field for faster search.  
  
### CustomFieldScope

Whether the custom field is associated with an alert or a case.

Enums  
---  
`CUSTOM_FIELD_SCOPE_UNSPECIFIED` | Unspecified scope.  
`ALERT` | Belnogs to Alert scope.  
`CASE` | Belongs to Case scope.  
  
## Methods  
  
---  
  
### `[batchUpdate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues/batchUpdate)`

|  Performs a bulk update of multiple custom field values in a single operation.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues/get)`

|  Gets a single custom field value by its resource name.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues/list)`

|  Lists all custom field values for a specific case or alert.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.cases.alerts.customFieldValues/patch)`

|  Updates (or creates if not present) the value of a custom field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
