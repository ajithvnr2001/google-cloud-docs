---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportIntentsResponse/
title: ExportIntentsResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:03.152511+00:00
---

# ExportIntentsResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportIntentsResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ExportIntentsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[Intents.ExportIntents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/export#google.cloud.dialogflow.cx.v3.Intents.ExportIntents)`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "intentsUri": string,
      "intentsContent": {
        object ([InlineDestination](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineDestination))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The exported intents. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`intentsUri` |  `string` The URI to a file containing the exported intents. This field is populated only if `intentsUri` is specified in `ExportIntentsRequest`.  
`intentsContent` |  `object (`[InlineDestination](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineDestination)`)` Uncompressed byte content for intents. This field is populated only if `intentsContentInline` is set to true in `ExportIntentsRequest`.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
