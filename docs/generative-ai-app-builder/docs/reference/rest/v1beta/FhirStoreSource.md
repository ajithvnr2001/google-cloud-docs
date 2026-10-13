---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FhirStoreSource/
title: FhirStoreSource \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:58.992423+00:00
---

# FhirStoreSource  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FhirStoreSource/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  FhirStoreSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Cloud FhirStore source import data from.

JSON representation  
---  
      
    
    {
      "fhirStore": string,
      "gcsStagingDir": string,
      "resourceTypes": [
        string
      ],
      "updateFromLatestPredefinedSchema": boolean
    }  
  
Fields  
---  
`fhirStore` |  `string` Required. The full resource name of the FHIR store to import data from, in the format of `projects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhirStore}`.  
`gcsStagingDir` |  `string` Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the FhirStore export to a specific Cloud Storage directory.  
`resourceTypes[]` |  `string` The FHIR resource types to import. The resource types should be a subset of all [supported FHIR resource types](https://cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference#resource-level-specification). Default to all supported FHIR resource types if empty.  
`updateFromLatestPredefinedSchema` |  `boolean` Optional. Whether to update the DataStore schema to the latest predefined schema.If true, the DataStore schema will be updated to include any FHIR fields or resource types that have been added since the last import and corresponding FHIR resources will be imported from the FHIR store.Note this field cannot be used in conjunction with `resourceTypes`. It should be used after initial import.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
