---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileParsingConfig/
title: RagFileParsingConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:51:17.182340+00:00
---

# RagFileParsingConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileParsingConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RagFileParsingConfig Stay organized with collections  Save and categorize content based on your preferences. 

Specifies the parsing config for RagFiles.

Fields  
  
`useAdvancedPdfParsing  
**(deprecated)**` `boolean` This item is deprecated!Whether to use advanced PDF parsing. | `parser` `Union type`  
  
The parser to use for RagFiles. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`advancedParser` `object (`[AdvancedParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileParsingConfig#AdvancedParser)`)` The Advanced Parser to use for RagFiles. | `layoutParser` `object (`[LayoutParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileParsingConfig#LayoutParser)`)` The Layout Parser to use for RagFiles. | `llmParser` `object (`[LlmParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora#LlmParser)`)` The LLM Parser to use for RagFiles. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "useAdvancedPdfParsing": boolean,
    
      // parser
      "advancedParser": {
        object ([AdvancedParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileParsingConfig#AdvancedParser))
      },
      "layoutParser": {
        object ([LayoutParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileParsingConfig#LayoutParser))
      },
      "llmParser": {
        object ([LlmParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora#LlmParser))
      }
      // Union type
    }  
  
## AdvancedParser

Specifies the advanced parsing for RagFiles.

Fields  
  
`useAdvancedPdfParsing` `boolean` Whether to use advanced PDF parsing. | JSON representation  
---  
      
    
    {
      "useAdvancedPdfParsing": boolean
    }  
  
## LayoutParser

Document AI Layout Parser config.

Fields  
  
`processorName` `string` The full resource name of a Document AI processor or processor version. The processor must have type `LAYOUT_PARSER_PROCESSOR`. If specified, the `additionalConfig.parse_as_scanned_pdf` field must be false. Format: * `projects/{projectId}/locations/{location}/processors/{processorId}` * `projects/{projectId}/locations/{location}/processors/{processorId}/processorVersions/{processor_version_id}` | `maxParsingRequestsPerMin` `integer` The maximum number of requests the job is allowed to make to the Document AI processor per minute. Consult <https://cloud.google.com/document-ai/quotas> and the Quota page for your project to set an appropriate value here. If unspecified, a default value of 120 QPM would be used. | `globalMaxParsingRequestsPerMin` `integer` The maximum number of requests the job is allowed to make to the Document AI processor per minute in this project. Consult <https://cloud.google.com/document-ai/quotas> and the Quota page for your project to set an appropriate value here. If this value is not specified, maxParsingRequestsPerMin will be used by indexing pipeline as the global limit. | JSON representation  
---  
      
    
    {
      "processorName": string,
      "maxParsingRequestsPerMin": integer,
      "globalMaxParsingRequestsPerMin": integer
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
