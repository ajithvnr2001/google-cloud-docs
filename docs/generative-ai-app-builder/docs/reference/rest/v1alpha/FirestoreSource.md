---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/FirestoreSource/
title: FirestoreSource \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:31.591668+00:00
---

# FirestoreSource  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/FirestoreSource/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  FirestoreSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Firestore source import data from.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "databaseId": string,
      "collectionId": string,
      "gcsStagingDir": string
    }  
  
Fields  
---  
`projectId` |  `string` The project ID that the Cloud SQL source is in with a length limit of 128 characters. If not specified, inherits the project ID from the parent request.  
`databaseId` |  `string` Required. The Firestore database to copy the data from with a length limit of 256 characters.  
`collectionId` |  `string` Required. The Firestore collection (or entity) to copy the data from with a length limit of 1,500 characters.  
`gcsStagingDir` |  `string` Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the Firestore export to a specific Cloud Storage directory.Ensure that the Firestore service account has the necessary Cloud Storage Admin permissions to access the specified Cloud Storage directory.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
