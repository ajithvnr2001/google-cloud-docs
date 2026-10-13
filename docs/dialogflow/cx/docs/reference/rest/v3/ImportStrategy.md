---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportStrategy/
title: ImportStrategy \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:33.370786+00:00
---

# ImportStrategy  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportStrategy/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ImportStrategy Stay organized with collections  Save and categorize content based on your preferences. 

Import strategies for the conflict resolution of resources (i.e. intents, entities, and webhooks) with identical display names during import operations.

Enums  
---  
`IMPORT_STRATEGY_UNSPECIFIED` | Unspecified. Treated as 'CREATE_NEW'.  
`IMPORT_STRATEGY_CREATE_NEW` | Create a new resource with a numeric suffix appended to the end of the existing display name.  
`IMPORT_STRATEGY_REPLACE` | Replace existing resource with incoming resource in the content to be imported.  
`IMPORT_STRATEGY_KEEP` | Keep existing resource and discard incoming resource in the content to be imported.  
`IMPORT_STRATEGY_MERGE` | Combine existing and incoming resources when a conflict is encountered.  
`IMPORT_STRATEGY_THROW_ERROR` | Throw error if a conflict is encountered.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
