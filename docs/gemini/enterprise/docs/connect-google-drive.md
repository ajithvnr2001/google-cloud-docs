---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connect-google-drive/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:02:36.410192+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connect-google-drive/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Google Drive data store for Gemini Enterprise lets you search and perform actions on your Google Drive data, including files and folders.

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Google Drive, Gmail, Google Chat, and Google Calendar. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Google Drive setup instructions, see [Set up a Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store).

## Supported actions

When the Google Drive data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Copy file | Copies a file in Google Drive.  
Create file | Creates a new file in Google Drive.  
Download file content | Downloads the content of a Google Drive file.  
Get cell values | Reads cell values from a Google Sheets spreadsheet.  
Get file metadata | Fetches metadata for a Google Drive file.  
Get file permissions | Lists the permissions on a Google Drive file.  
Get spreadsheet |  Reads the contents and metadata of a Google Sheets spreadsheet.   
Insert dimension | Inserts rows or columns into a Google Sheets spreadsheet.  
List recent files | Lists recent files in Google Drive.  
List shared drives | Lists shared drives in Google Drive.  
Read document | Reads the contents of a Google Docs document.  
Read file content | Reads the contents of a Google Drive file.  
Read presentation | Reads the contents of a Google Slides presentation.  
Search files | Searches for Google Drive files matching a query.  
Share file | Shares a Google Drive file with one or more users.  
Trash file | Moves a Google Drive file to the trash.  
Update cell values | Writes cell values to a Google Sheets spreadsheet.  
Update file | Updates an existing Google Drive file.  
Update formulas | Writes formulas to a Google Sheets spreadsheet.  
**Note:** The maximum file size for file uploads and downloads in Gemini Enterprise is 75 MB.

### Required scopes

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector:

Scope | Purpose  
---|---  
`https://www.googleapis.com/auth/drive.readonly` | Search and retrieve Google Drive content. Lets the data store list files and folders, view metadata, list permissions, and read file content.  
`https://www.googleapis.com/auth/drive.metadata.readonly` | Read Google Drive file metadata.  
`https://www.googleapis.com/auth/drive.file` | Create and update files that the user opens or creates with the connector.  
`https://www.googleapis.com/auth/drive.appdata` | Store application-specific data in Google Drive.  
`https://www.googleapis.com/auth/drive` | Perform write actions on Google Drive files (for example, copy, share, trash, and update).  
  
## Limitations

  * The Google Drive data store is supported only in the `global`, `us`, and `eu` locations.


  * If you use security controls, be aware of their limitations related to data in Google Drive, as discussed in the following table:

Security control | Note the following  
---|---  
[Data Residency (DRZ)](https://docs.cloud.google.com/gemini/enterprise/docs/locations) | Gemini Enterprise only guarantees data residency in Google Cloud. For information about data residency and Google Drive, see Google Workspace compliance guidance and documentation, including [Data regions for Google Workspace](https://support.google.com/a/answer/9223653). Also review examples like [Choose the region where data is stored](https://support.google.com/a/topic/7631290) and [ Digital sovereignty](https://workspace.google.com/intl/en_in/security/digital-sovereignty/).   
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/enterprise/docs/cmek) |  Your keys only encrypt data within Google Cloud. Cloud Key Management Service controls don't apply to data stored in Google Drive.   
[ Access Transparency](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency) |  Access Transparency logs actions taken by Google personnel on the Google Cloud project. You'll also need to review the Access Transparency logs created by Google Workspace. For more information, see [Access Transparency log events](https://support.google.com/a/answer/9230979) in the Google Workspace Admin Help documentation.   



## Common search issues

If your search doesn't return the file you're looking for, it might be due to one of the following search index limitations of Google Drive:

  * Google Drive only extracts 1 MB of text and formatting data from your file to make it searchable. Keywords exceeding the 1 MB index limit aren't searchable.

  * For most file types, file size cannot exceed 10 MB. The following are exceptions:

    * XLSX files (.xlsx) cannot exceed 20 MB.

    * PDF files (.pdf) cannot exceed 30 MB.

    * Text files (.txt) cannot exceed 100 MB.

**Note:** Files exceeding the size limit are not searchable and won't appear in your search results.
  * Optical character recognition in PDF files is limited to 80 pages. Google Drive doesn't index any PDF that is larger than 50 MB or 80 pages.




## What's next

  * To create and configure a data store with Google Drive, see [Set up a Google Drive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
