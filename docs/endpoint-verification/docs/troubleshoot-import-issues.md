---
url: https://docs.cloud.google.com/endpoint-verification/docs/troubleshoot-import-issues/
title: Troubleshoot device import issues \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:50.715912+00:00
---

# Troubleshoot device import issues  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/troubleshoot-import-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Troubleshoot device import issues Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how administrators can resolve the device import issues when importing the company-owned devices.

The following table lists error messages that you might encounter when importing the company-owned devices and provides suggestions for how to fix each of them.

Error message | Workaround | There was a problem uploading your file. The file could not be uploaded. | Upload the file again.  
---|---  
The file is empty. The uploaded CSV file is empty. | Add details for your company-owned devices and upload the file again.  
The file might be damaged or the format might be wrong. |  The uploaded CSV file does not have a header. Ensure that the header format matches the import template and upload the file again.  
There's a problem in the file header. | The uploaded CSV file has an invalid header. Ensure that the header format matches the import template and upload the file again.  
There's a formatting problem in the CSV file. | The uploaded CSV file contains some errors. Ensure that the format of each row is correct and upload the file again.  
The file type must be CSV. | Ensure that the file type is CSV and upload the file again.  
The CSV file is too large. | The maximum file size is 10 MB. Split the data into two CSV files and upload the files.  
The uploaded CSV file has some unsupported columns. |  Some extra columns were added to the import template. Remove the columns and upload the file again.  
The column-name column is missing from the file. | Add the missing column to the import template and upload the file again.  
There's more than 1 column-name column in the file. | Remove the duplicate column from the file and upload the file again.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
