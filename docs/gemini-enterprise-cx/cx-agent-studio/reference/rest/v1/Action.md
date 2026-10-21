---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Action/
title: Action \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:39.356894+00:00
---

# Action  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Action Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Action.EntityOperation
    * JSON representation
  * Action.EntityOperation.OperationType



Configuration of an Action for the tool to use. Note: This can be either an Action or an Operation. See <https://cloud.google.com/integration-connectors/docs/entities-operation-action> for details.

JSON representation  
---  
      
    
    {
      "inputFields": [
        string
      ],
      "outputFields": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "connectionActionId": string,
      "entityOperation": {
        object ([Action.EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Action#Action.EntityOperation))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`inputFields[]` |  `string` Optional. Entity fields to use as inputs for the operation. If no fields are specified, all fields of the Entity will be used.  
`outputFields[]` |  `string` Optional. Entity fields to return from the operation. If no fields are specified, all fields of the Entity will be returned.  
Specification for an action to configure for the tool to use. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`connectionActionId` |  `string` ID of a Connection action for the tool to use.  
`entityOperation` |  `object (`[Action.EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Action#Action.EntityOperation)`)` Entity operation configuration for the tool to use.  
End of mutually exclusive fields.  
  
## Action.EntityOperation

Entity CRUD operation specification.

JSON representation  
---  
      
    
    {
      "entityId": string,
      "operation": enum ([Action.EntityOperation.OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Action#Action.EntityOperation.OperationType))
    }  
  
Fields  
---  
`entityId` |  `string` Required. ID of the entity.  
`operation` |  `enum (`[Action.EntityOperation.OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Action#Action.EntityOperation.OperationType)`)` Required. Operation to perform on the entity.  
  
## Action.EntityOperation.OperationType

The operation to perform on the entity.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. Invalid, ConnectorTool create/update will fail.  
`LIST` | List operation.  
`GET` | Get operation.  
`CREATE` | Create operation.  
`UPDATE` | Update operation.  
`DELETE` | Delete operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
