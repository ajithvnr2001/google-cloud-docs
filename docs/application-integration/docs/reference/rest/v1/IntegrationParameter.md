---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameter/
title: IntegrationParameter \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:09.203167+00:00
---

# IntegrationParameter  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  IntegrationParameter Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * InOutType



Integration Parameter is defined in the integration config and are used to provide information about data types of the expected parameters and provide any default values if needed. They can also be used to add custom attributes. These are static in nature and should not be used for dynamic event definition.

JSON representation  
---  
      
    
    {
      "key": string,
      "dataType": enum ([IntegrationParameterDataType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameterDataType)),
      "defaultValue": {
        object ([ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType))
      },
      "searchable": boolean,
      "displayName": string,
      "inputOutputType": enum ([InOutType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameter#InOutType)),
      "isTransient": boolean,
      "producer": string,
      "jsonSchema": string,
      "containsLargeData": boolean,
      "masked": boolean,
      "description": string
    }  
  
Fields  
---  
`key` |  `string` Key is used to retrieve the corresponding parameter value. This should be unique for a given fired event. These parameters must be predefined in the integration definition.  
`dataType` |  `enum (`[IntegrationParameterDataType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameterDataType)`)` type of the parameter.  
`defaultValue` |  `object (`[ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType)`)` Default values for the defined keys. Each value can either be string, int, double or any proto message or a serialized object.  
`searchable` |  `boolean` Searchable in the execution log or not.  
`displayName` |  `string` The name (without prefix) to be displayed in the UI for this parameter. E.g. if the key is "foo.bar.myName", then the name would be "myName".  
`inputOutputType` |  `enum (`[InOutType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/IntegrationParameter#InOutType)`)` Specifies the input/output type for the parameter.  
`isTransient` |  `boolean` Whether this parameter is a transient parameter.  
`producer` |  `string` The identifier of the node (TaskConfig/TriggerConfig) this parameter was produced by, if it is a transient param or a copy of an input param.  
`jsonSchema` |  `string` This schema will be used to validate runtime JSON-typed values of this parameter.  
`containsLargeData` |  `boolean` Indicates whether this variable contains large data and need to be uploaded to Cloud Storage.  
`masked` |  `boolean` True if this parameter should be masked in the logs  
`description` |  `string` Optional. Description of the parameter.  
  
## InOutType

Is the parameter input, output of a integration.

Enums  
---  
`IN_OUT_TYPE_UNSPECIFIED` | Default.  
`IN` | Input parameters for the integration. EventBus validates that these parameters exist in the integrations before execution.  
`OUT` | Output Parameters for the integration. EventBus will only return the integration parameters tagged with OUT in the response back.  
`IN_OUT` | Input and Output Parameters. These can be used as both input and output. EventBus will validate for the existence of these parameters before execution and will also return this parameter back in the response.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
