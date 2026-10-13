---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetApiWorkflowStepParameterDataModel/
title: WidgetApiWorkflowStepParameterDataModel \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:03.267000+00:00
---

# WidgetApiWorkflowStepParameterDataModel  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetApiWorkflowStepParameterDataModel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  WidgetApiWorkflowStepParameterDataModel Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * CustomActionParameterType



The parameter of the step.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string,
      "defaultValue": string,
      "type": enum ([CustomActionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetApiWorkflowStepParameterDataModel#CustomActionParameterType)),
      "isMandatory": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the parameter.  
`value` |  `string` Output only. The value of the parameter.  
`defaultValue` |  `string` Output only. The default value of the parameter.  
`type` |  `enum (`[CustomActionParameterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/WidgetApiWorkflowStepParameterDataModel#CustomActionParameterType)`)` Output only. The type of the parameter.  
`isMandatory` |  `boolean` Output only. Whether the parameter is mandatory.  
  
## CustomActionParameterType

The type of the parameter.

Enums  
---  
`CUSTOM_ACTION_PARAMETER_TYPE_UNSPECIFIED` | Unspecified custom action parameter type.  
`STRING` | String custom action parameter type.  
`BOOLEAN` | Boolean custom action parameter type.  
`WFS_REPOSITORY` | WFS repository custom action parameter type.  
`USER_REPOSITORY` | User repository custom action parameter type.  
`STAGES_REPOSITORY` | Stages repository custom action parameter type.  
`CLOSE_CASE_REASON_REPOSITORY` | Close case reason repository custom action parameter type.  
`CLOSE_CASE_ROOT_CAUSE_REPOSITORY` | Close case root cause repository custom action parameter type.  
`PRIORITIES_REPOSITORY` | Priorities repository custom action parameter type.  
`EMAIL_CONTENT` | Email content custom action parameter type.  
`CONTENT` | Content custom action parameter type.  
`PASSWORD` | Password custom action parameter type.  
`ENTITY_TYPE` | Entity type custom action parameter type.  
`MULTI_VALUES` | Multi values custom action parameter type.  
`LIST` | List custom action parameter type.  
`CODE` | Code custom action parameter type.  
`TIME_SPAN_SECONDS` | Time span seconds custom action parameter type.  
`MULTIPLE_CHOICE_PARAMETER` | Multiple choice parameter custom action parameter type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-10 UTC."],[],[]] 
