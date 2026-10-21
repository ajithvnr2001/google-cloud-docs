---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsSource/
title: GcsSource \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:58:06.231269+00:00
---

# GcsSource  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  GcsSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Format



Google Cloud Storage Object details to get the feedback label file from.

JSON representation  
---  
      
    
    {
      "format": enum ([Format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsSource#Format)),
      "objectUri": string
    }  
  
Fields  
---  
`format` |  `enum (`[Format](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsSource#Format)`)` Required. File format which will be ingested.  
`objectUri` |  `string` Required. The Google Cloud Storage URI of the file to import. Format: `gs://bucket_name/object_name`  
  
## Format

All permissible file formats.

Enums  
---  
`FORMAT_UNSPECIFIED` | Unspecified format.  
`CSV` | CSV format.  
`JSON` | JSON format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
