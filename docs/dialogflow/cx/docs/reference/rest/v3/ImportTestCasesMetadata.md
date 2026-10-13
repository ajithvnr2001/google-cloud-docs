---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportTestCasesMetadata/
title: ImportTestCasesMetadata \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:33.672635+00:00
---

# ImportTestCasesMetadata  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportTestCasesMetadata/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ImportTestCasesMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TestCaseError
    * JSON representation



Metadata returned for the `[TestCases.ImportTestCases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases/import#google.cloud.dialogflow.cx.v3.TestCases.ImportTestCases)` long running operation.

JSON representation  
---  
      
    
    {
      "errors": [
        {
          object ([TestCaseError](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportTestCasesMetadata#TestCaseError))
        }
      ]
    }  
  
Fields  
---  
`errors[]` |  `object (`[TestCaseError](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportTestCasesMetadata#TestCaseError)`)` Errors for failed test cases.  
  
## TestCaseError

Error info for importing a test.

JSON representation  
---  
      
    
    {
      "testCase": {
        object ([TestCase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases#TestCase))
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Status))
      }
    }  
  
Fields  
---  
`testCase` |  `object (`[TestCase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases#TestCase)`)` The test case.  
`status` |  `object (`[Status](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Status)`)` The status associated with the test case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
