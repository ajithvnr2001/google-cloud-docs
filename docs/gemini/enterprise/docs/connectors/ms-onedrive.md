---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:43.622081+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Microsoft OneDrive data store for Gemini Enterprise lets you search and perform actions on your files and folders.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported Microsoft OneDrive versions

The Microsoft OneDrive data store supports all hosted versions of Microsoft OneDrive through the Microsoft Graph API v1.0.

## Supported actions

When the Microsoft OneDrive data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create folder | Creates a new folder at a specified path in Microsoft OneDrive.  
Copy file | Copies a file from a source to a destination in Microsoft OneDrive.  
Upload file | Uploads a file to a specified location in Microsoft OneDrive.  
Download file | Downloads a file from Microsoft OneDrive to a specified location.  
Copy folder | Copies a folder from a source to a destination in Microsoft OneDrive.  
Move file | Moves a file from a source to a destination in Microsoft OneDrive.  
Move folder | Moves a folder from a source to a destination in Microsoft OneDrive.  
Rename file | Renames a file in Microsoft OneDrive.  
Rename folder | Renames a folder in Microsoft OneDrive.  
Share file or folder | Shares a file or folder with specified recipients or generates a share link.  
Update file properties | Updates metadata properties of a file in Microsoft OneDrive.  
**Notes** : 

  * Additional read-only actions are also available.
  * The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB.



### Required permissions

To enable Gemini Enterprise to perform search and data ingestion using the Microsoft OneDrive data store, you need the following permissions:

#### Microsoft Graph API permissions

The table below outlines the permissions required for each connection mode.

**Note:** The following table outlines the permissions required for each connection mode. If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the permissions listed in the **Actions** row. 

**Connection mode** | **Scope** | **Purpose**  
---|---|---  
**Federated search** | `Files.Read.All` | (Delegated) Allows the data store to read all files that the user can access.  
`Sites.Read.All` | (Delegated) Allows the data store to read documents and list items in all site collections that the user can access.  
`User.Read.All` | (Delegated) Allows the data store to resolve user drive locations for content discovery.  
**Data ingestion** | `GroupMember.Read.All` | (Federated credentials & OAuth 2.0 refresh token) Allows the data store to read memberships and basic group properties for all groups without a signed-in user.  
`User.Read` | (Federated credentials & OAuth 2.0 refresh token) Allows the data store to read the profile of signed-in users. It also allows the data store to read basic company information of signed-in users.  
`User.Read.All` | (OAuth 2.0 refresh token only) Allows the data store to read user profiles.  
`Sites.FullControl.All` (Option 1)  
`Sites.Selected` (Option 2) | (Federated credentials & OAuth 2.0 refresh token) Option 1 allows the data store to have full control of all site collections. Option 2 allows the data store to access a subset of site collections. The specific site collections and the permissions granted can be configured in Microsoft OneDrive.  
`User.Read.All` (Option 1)  
`User.ReadBasic.All` (Option 2) | (Federated credentials only) Option 1 allows the data store to read user profiles. Option 2 allows the data store to read a basic set of profile properties of other users in the organization.  
**Actions** | `Files.ReadWrite.AppFolder` | (Delegated) Allows the data store to read, create, update and delete files in the Microsoft OneDrive folder.  
`Files.ReadWrite` | Delegated: Allows the data store to read, download, create, upload, update, and delete the files that the user can access.  
`Files.ReadWrite.All` | (Delegated) Allows the data store to read and update files across all drives the user has access to. Required for the file and folder mutation actions (copy, move, rename, share, update properties) that operate on files stored in drives beyond the user's own Microsoft OneDrive.  
  
For information on how to add the permissions for Microsoft OneDrive, see [Configure Microsoft OneDrive and set the necessary permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config#configure-api-permissions).

## Limitations

This section outlines known issues and limitations that may affect your use of the Microsoft OneDrive data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Microsoft OneDrive data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Microsoft OneDrive data store is supported only in the `global`, `us`, and `eu` locations.



The following are the limitations for the Microsoft OneDrive federated data store:

  * **Search limitations** : Search results may vary and are not always comprehensive for all file types. Content in archived or encrypted folders may not be accessible for search. Federated search does not support searching within attachments.
  * **Delegated access:** Access to shared Microsoft OneDrive files or folders may require specific permissions not covered by standard user authorization.
  * **Layout parser in federated search mode:** While the layout parser is standard, its effectiveness on complex PDFs (with tables, multi-column layouts, or needing OCR) is limited in federated search mode. This mode's real-time API calls might not provide the complete data or time required for the deep analysis the layout parser performs during data ingestion.
  * **Unsupported PDF Features:** Consequently, complex PDF structures might not be fully analyzed or searchable. This includes:

    * Multi-column text layouts
    * Data within embedded tables and charts
    * Text in scanned documents requiring Optical Character Recognition (OCR)
    * Documents with non-linear reading orders or intricate formatting.



The following are the limitations for the Microsoft OneDrive ingestion data store:

  * Incremental sync does not detect folder-level actions like **Copy** , **Move** , or **Rename**.



## Recommendation

For Microsoft OneDrive data containing PDFs with complex features (like tables, multi-column layouts, or OCR-dependent content), we recommend using data ingestion mode for effective search. This mode allows the layout parser to deeply process and index the entire document content.

## What's next

  * To create and configure a data store with Microsoft OneDrive, see [Set up a Microsoft OneDrive data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
