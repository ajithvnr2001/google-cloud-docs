---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/SheetsDestination/
title: SheetsDestination \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:20:45.416849+00:00
---

# SheetsDestination  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/SheetsDestination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  SheetsDestination Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Google Sheets document details to write the feedback labels to.

JSON representation  
---  
      
    
    {
      "spreadsheetUri": string,
      "sheetTitle": string
    }  
  
Fields  
---  
`spreadsheetUri` |  `string` Required. The Google Sheets document to write the feedback labels to. Retrieved from Google Sheets URI. E.g. `https://docs.google.com/spreadsheets/d/1234567890` The spreadsheet must be shared with the Insights P4SA. The spreadsheet ID written to will be returned as `fileNames` in the BulkDownloadFeedbackLabelsMetadata.  
`sheetTitle` |  `string` Optional. The title of the new sheet to write the feedback labels to.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
