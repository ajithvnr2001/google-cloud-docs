---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportFlowResponse/
title: ExportFlowResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:11.945772+00:00
---

# ExportFlowResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportFlowResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ExportFlowResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[Flows.ExportFlow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows/export#google.cloud.dialogflow.cx.v3.Flows.ExportFlow)`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "flowUri": string,
      "flowContent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The exported flow. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`flowUri` |  `string` The URI to a file containing the exported flow. This field is populated only if `flowUri` is specified in `ExportFlowRequest`.  
`flowContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Uncompressed raw byte content for flow.A base64-encoded string.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
