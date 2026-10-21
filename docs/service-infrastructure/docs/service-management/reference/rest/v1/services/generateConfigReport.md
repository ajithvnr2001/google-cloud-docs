---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport/
title: Method: services.generateConfigReport \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:26.602655+00:00
---

# Method: services.generateConfigReport  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.generateConfigReport Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * ChangeReport
    * JSON representation
  * ConfigChange
    * JSON representation
  * ChangeType
  * Advice
    * JSON representation
  * Diagnostic
    * JSON representation
  * Kind



Generates and returns a report (errors, warnings and changes from existing configurations) associated with GenerateConfigReportRequest.new_value

If GenerateConfigReportRequest.old_value is specified, GenerateConfigReportRequest will contain a single ChangeReport based on the comparison between GenerateConfigReportRequest.new_value and GenerateConfigReportRequest.old_value. If GenerateConfigReportRequest.old_value is not specified, this method will compare GenerateConfigReportRequest.new_value with the last pushed service configuration.

### HTTP request

`POST https://servicemanagement.googleapis.com/v1/services:generateConfigReport`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "newConfig": {
        "@type": string,
        field1: ...,
        ...
      },
      "oldConfig": {
        "@type": string,
        field1: ...,
        ...
      }
    }  
  
Fields  
---  
`newConfig` |  `object` Required. Service configuration for which we want to generate the report. For this version of API, the supported types are `[google.api.servicemanagement.v1.ConfigRef](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/ConfigRef)`, `[google.api.servicemanagement.v1.ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#ConfigSource)`, and `[google.api.Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service)`An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`oldConfig` |  `object` Optional. Service configuration against which the comparison will be done. For this version of API, the supported types are `[google.api.servicemanagement.v1.ConfigRef](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/ConfigRef)`, `[google.api.servicemanagement.v1.ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs/submit#ConfigSource)`, and `[google.api.Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#Service)`An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Response body

If successful, the response body contains data with the following structure:

Response message for services.generateConfigReport method.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "id": string,
      "changeReports": [
        {
          object ([ChangeReport](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#ChangeReport))
        }
      ],
      "diagnostics": [
        {
          object ([Diagnostic](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#Diagnostic))
        }
      ]
    }  
  
Fields  
---  
`serviceName` |  `string` name of the service this report belongs to.  
`id` |  `string` ID of the service configuration this report belongs to.  
`changeReports[]` |  `object (`[ChangeReport](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#ChangeReport)`)` list of ChangeReport, each corresponding to comparison between two service configurations.  
`diagnostics[]` |  `object (`[Diagnostic](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#Diagnostic)`)` Errors / Linter warnings associated with the service definition this report belongs to.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ChangeReport

Change report associated with a particular service configuration.

It contains a list of ConfigChanges based on the comparison between two service configurations.

JSON representation  
---  
      
    
    {
      "configChanges": [
        {
          object ([ConfigChange](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#ConfigChange))
        }
      ]
    }  
  
Fields  
---  
`configChanges[]` |  `object (`[ConfigChange](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#ConfigChange)`)` List of changes between two service configurations. The changes will be alphabetically sorted based on the identifier of each change. A ConfigChange identifier is a dot separated path to the configuration. Example: visibility.rules[selector='LibraryService.CreateBook'].restriction  
  
## ConfigChange

Output generated from semantically comparing two versions of a service configuration.

Includes detailed information about a field that have changed with applicable advice about potential consequences for the change, such as backwards-incompatibility.

JSON representation  
---  
      
    
    {
      "element": string,
      "oldValue": string,
      "newValue": string,
      "changeType": enum ([ChangeType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#ChangeType)),
      "advices": [
        {
          object ([Advice](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#Advice))
        }
      ]
    }  
  
Fields  
---  
`element` |  `string` Object hierarchy path to the change, with levels separated by a '.' character. For repeated fields, an applicable unique identifier field is used for the index (usually selector, name, or id). For maps, the term 'key' is used. If the field has no unique identifier, the numeric index is used. Examples: - visibility.rules[selector=="google.LibraryService.ListBooks"].restriction - quota.metric_rules[selector=="google"].metric_costs[key=="reads"].value - logging.producer_destinations[0]  
`oldValue` |  `string` Value of the changed object in the old Service configuration, in JSON format. This field will not be populated if changetype == ADDED.  
`newValue` |  `string` Value of the changed object in the new Service configuration, in JSON format. This field will not be populated if changetype == REMOVED.  
`changeType` |  `enum (`[ChangeType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#ChangeType)`)` The type for this change, either ADDED, REMOVED, or MODIFIED.  
`advices[]` |  `object (`[Advice](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#Advice)`)` Collection of advice provided for this change, useful for determining the possible impact of this change.  
  
## ChangeType

Classifies set of possible modifications to an object in the service configuration.

Enums  
---  
`CHANGE_TYPE_UNSPECIFIED` | No value was provided.  
`ADDED` | The changed object exists in the 'new' service configuration, but not in the 'old' service configuration.  
`REMOVED` | The changed object exists in the 'old' service configuration, but not in the 'new' service configuration.  
`MODIFIED` | The changed object exists in both service configurations, but its value is different.  
  
## Advice

Generated advice about this change, used for providing more information about how a change will affect the existing service.

JSON representation  
---  
      
    
    {
      "description": string
    }  
  
Fields  
---  
`description` |  `string` Useful description for why this advice was applied and what actions should be taken to mitigate any implied risks.  
  
## Diagnostic

Represents a diagnostic message (error or warning)

JSON representation  
---  
      
    
    {
      "location": string,
      "kind": enum ([Kind](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#Kind)),
      "message": string
    }  
  
Fields  
---  
`location` |  `string` File name and line number of the error or warning.  
`kind` |  `enum (`[Kind](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services/generateConfigReport#Kind)`)` The kind of diagnostic information provided.  
`message` |  `string` Message describing the error or warning.  
  
## Kind

The kind of diagnostic information possible.

Enums  
---  
`WARNING` | Warnings and errors  
`ERROR` | Only errors  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
