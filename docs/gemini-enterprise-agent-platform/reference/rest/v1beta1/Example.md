---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example/
title: Example \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:59:59.294040+00:00
---

# Example  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Example Stay organized with collections  Save and categorize content based on your preferences. 

Fields  
  
`displayName` `string` Optional. The display name for Example. | `exampleId` `string` Optional. Immutable. Unique identifier of an example. If not specified when upserting new examples, the exampleId will be generated. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Example was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `example_type` `Union type`  
  
The type of the example. Each example type has a defined format The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`storedContentsExample` `object (`[StoredContentsExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example#StoredContentsExample)`)` An example of chat history and its expected outcome to be used with GenerateContent. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "displayName": string,
      "exampleId": string,
      "createTime": string,
    
      // example_type
      "storedContentsExample": {
        object ([StoredContentsExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example#StoredContentsExample))
      }
      // Union type
    }  
  
## StoredContentsExample

A ContentsExample to be used with GenerateContent alongside information required for storage and retrieval with Example Store.

Fields  
  
`searchKey` `string` Optional. (Optional) the search key used for retrieval. If not provided at upload-time, the search key will be generated from `contentsExample.contents` using the method provided by `searchKeyGenerationMethod`. The generated search key will be included in retrieved examples. | `contentsExample` `object (`[ContentsExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example#ContentsExample)`)` Required. The example to be used with GenerateContent. | `searchKeyGenerationMethod` `object (`[SearchKeyGenerationMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SearchKeyGenerationMethod)`)` Optional. The method used to generate the search key from `contentsExample.contents`. This is ignored when uploading an example if `searchKey` is provided. | JSON representation  
---  
      
    
    {
      "searchKey": string,
      "contentsExample": {
        object ([ContentsExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example#ContentsExample))
      },
      "searchKeyGenerationMethod": {
        object ([SearchKeyGenerationMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SearchKeyGenerationMethod))
      }
    }  
  
## ContentsExample

A single example of a conversation with the model.

Fields  
  
`contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Required. The content of the conversation with the model that resulted in the expected output. | `expectedContents[]` `object (`[ExpectedContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example#ExpectedContent)`)` Required. The expected output for the given `contents`. To represent multi-step reasoning, this is a repeated field that contains the iterative steps of the expected output. | JSON representation  
---  
      
    
    {
      "contents": [
        {
          object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
        }
      ],
      "expectedContents": [
        {
          object ([ExpectedContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example#ExpectedContent))
        }
      ]
    }  
  
## ExpectedContent

A single step of the expected output.

Fields  
  
`content` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Required. A single step's content. | JSON representation  
---  
      
    
    {
      "content": {
        object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
