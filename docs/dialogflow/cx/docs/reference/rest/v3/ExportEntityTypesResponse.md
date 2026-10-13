---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportEntityTypesResponse/
title: ExportEntityTypesResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:30.722281+00:00
---

# ExportEntityTypesResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ExportEntityTypesResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ExportEntityTypesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[EntityTypes.ExportEntityTypes](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes/export#google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes)`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "entityTypesUri": string,
      "entityTypesContent": {
        object ([InlineDestination](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineDestination))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Exported entity types can be either in cloud storage or local download. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entityTypesUri` |  `string` The URI to a file containing the exported entity types. This field is populated only if `entityTypesUri` is specified in `ExportEntityTypesRequest`.  
`entityTypesContent` |  `object (`[InlineDestination](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/InlineDestination)`)` Uncompressed byte content for entity types. This field is populated only if `entityTypesContentInline` is set to true in `ExportEntityTypesRequest`.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
