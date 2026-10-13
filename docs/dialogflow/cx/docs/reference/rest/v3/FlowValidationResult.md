---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult/
title: FlowValidationResult \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:32.021768+00:00
---

# FlowValidationResult  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  FlowValidationResult Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ValidationMessage
    * JSON representation
  * ResourceType
  * ResourceName
    * JSON representation
  * Severity



The response message for `[Flows.GetFlowValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/getValidationResult#google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "validationMessages": [
        {
          object ([ValidationMessage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#ValidationMessage))
        }
      ],
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the flow validation result. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/validationResult`.  
`validationMessages[]` |  `object (`[ValidationMessage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#ValidationMessage)`)` Contains all validation messages.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the flow was validated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ValidationMessage

Agent/flow validation message.

JSON representation  
---  
      
    
    {
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#ResourceType)),
      "resources": [
        string
      ],
      "resourceNames": [
        {
          object ([ResourceName](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#ResourceName))
        }
      ],
      "severity": enum ([Severity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#Severity)),
      "detail": string
    }  
  
Fields  
---  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#ResourceType)`)` The type of the resources where the message is found.  
`resources[]  
**(deprecated)**` |  `string` This item is deprecated!The names of the resources where the message is found.  
`resourceNames[]` |  `object (`[ResourceName](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#ResourceName)`)` The resource names of the resources where the message is found.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FlowValidationResult#Severity)`)` Indicates the severity of the message.  
`detail` |  `string` The message detail.  
  
## ResourceType

Resource types.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Unspecified.  
`AGENT` | Agent.  
`INTENT` | Intent.  
`INTENT_TRAINING_PHRASE` | Intent training phrase.  
`INTENT_PARAMETER` | Intent parameter.  
`INTENTS` | Multiple intents.  
`INTENT_TRAINING_PHRASES` | Multiple training phrases.  
`ENTITY_TYPE` | Entity type.  
`ENTITY_TYPES` | Multiple entity types.  
`WEBHOOK` | Webhook.  
`FLOW` | Flow.  
`PAGE` | Page.  
`PAGES` | Multiple pages.  
`TRANSITION_ROUTE_GROUP` | Transition route group.  
`AGENT_TRANSITION_ROUTE_GROUP` | Agent transition route group.  
  
## ResourceName

Resource name and display name.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Name.  
`displayName` |  `string` Display name.  
  
## Severity

Severity level.

Enums  
---  
`SEVERITY_UNSPECIFIED` | Unspecified.  
`INFO` | The agent doesn't follow Dialogflow best practices.  
`WARNING` | The agent may not behave as expected.  
`ERROR` | The agent may experience failures.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
