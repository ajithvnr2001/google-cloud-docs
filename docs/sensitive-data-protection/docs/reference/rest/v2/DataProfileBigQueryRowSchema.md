---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileBigQueryRowSchema/
title: DataProfileBigQueryRowSchema \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:43.704237+00:00
---

# DataProfileBigQueryRowSchema  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileBigQueryRowSchema/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  DataProfileBigQueryRowSchema Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The schema of data to be saved to the BigQuery table when the `DataProfileAction` is enabled.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tableProfile": {
        object ([TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile))
      },
      "columnProfile": {
        object ([ColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile))
      },
      "fileStoreProfile": {
        object ([FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Data profile type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tableProfile` |  `object (`[TableDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile)`)` Table data profile column  
`columnProfile` |  `object (`[ColumnDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile)`)` Column data profile column  
`fileStoreProfile` |  `object (`[FileStoreDataProfile](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile)`)` File store data profile column.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
