---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec/
title: EndUserSpec \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:45.504824+00:00
---

# EndUserSpec  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  EndUserSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EndUserMetaData
    * JSON representation
  * ChunkInfo
    * JSON representation
  * DocumentMetadata
    * JSON representation



End user specification.

JSON representation  
---  
      
    
    {
      "endUserMetadata": [
        {
          object ([EndUserMetaData](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec#EndUserMetaData))
        }
      ]
    }  
  
Fields  
---  
`endUserMetadata[]` |  `object (`[EndUserMetaData](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec#EndUserMetaData)`)` Optional. End user metadata.  
  
## EndUserMetaData

End user metadata.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "chunkInfo": {
        object ([ChunkInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec#ChunkInfo))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Search result content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`chunkInfo` |  `object (`[ChunkInfo](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec#ChunkInfo)`)` Chunk information.  
End of mutually exclusive fields.  
  
## ChunkInfo

Chunk information.

JSON representation  
---  
      
    
    {
      "content": string,
      "documentMetadata": {
        object ([DocumentMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec#DocumentMetadata))
      }
    }  
  
Fields  
---  
`content` |  `string` Chunk textual content. It is limited to 8000 characters.  
`documentMetadata` |  `object (`[DocumentMetadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/EndUserSpec#DocumentMetadata)`)` Metadata of the document from the current chunk.  
  
## DocumentMetadata

Document metadata contains the information of the document of the current chunk.

JSON representation  
---  
      
    
    {
      "title": string
    }  
  
Fields  
---  
`title` |  `string` Title of the document.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
