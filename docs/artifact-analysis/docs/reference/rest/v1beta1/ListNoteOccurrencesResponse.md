---
url: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/ListNoteOccurrencesResponse/
title: ListNoteOccurrencesResponse \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:25.851725+00:00
---

# ListNoteOccurrencesResponse  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/ListNoteOccurrencesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-analysis/docs/apis)



Send feedback 

#  ListNoteOccurrencesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response for listing occurrences for a note.

JSON representation  
---  
      
    
    {
      "occurrences": [
        {
          object ([Occurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`occurrences[]` |  `object (`[Occurrence](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1beta1/projects.locations.occurrences#Occurrence)`)` The occurrences attached to the specified note.  
`nextPageToken` |  `string` Token to provide to skip to a particular spot in the list.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
