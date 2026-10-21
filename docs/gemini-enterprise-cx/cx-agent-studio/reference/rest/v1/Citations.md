---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Citations/
title: Citations \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:39.623407+00:00
---

# Citations  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Citations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Citations Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Citations.CitedChunk
    * JSON representation
  * Citations.InlineCitation
    * JSON representation



Citations associated with the agent response.

JSON representation  
---  
      
    
    {
      "citedChunks": [
        {
          object ([Citations.CitedChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Citations#Citations.CitedChunk))
        }
      ],
      "inlineCitations": [
        {
          object ([Citations.InlineCitation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Citations#Citations.InlineCitation))
        }
      ]
    }  
  
Fields  
---  
`citedChunks[]` |  `object (`[Citations.CitedChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Citations#Citations.CitedChunk)`)` List of cited pieces of information.  
`inlineCitations[]` |  `object (`[Citations.InlineCitation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Citations#Citations.InlineCitation)`)` Optional. List of inline citations in the agent response.  
  
## Citations.CitedChunk

Piece of cited information.

JSON representation  
---  
      
    
    {
      "uri": string,
      "title": string,
      "text": string,
      "requiresAttribution": boolean
    }  
  
Fields  
---  
`uri` |  `string` URI used for citation.  
`title` |  `string` Title of the cited document.  
`text` |  `string` Text used for citation.  
`requiresAttribution` |  `boolean` Whether this citation requires attribution to be shown to the end users.  
  
## Citations.InlineCitation

An inline citation in the response text.

JSON representation  
---  
      
    
    {
      "startIndex": integer,
      "endIndex": integer,
      "citedChunkIndices": [
        integer
      ]
    }  
  
Fields  
---  
`startIndex` |  `integer` The starting index (in bytes) of the text segment in the agent response.  
`endIndex` |  `integer` The ending index (in bytes) of the text segment in the agent response.  
`citedChunkIndices[]` |  `integer` The indices of the cited chunks that back this text segment. Indices refer to the elements in `citedChunks`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
