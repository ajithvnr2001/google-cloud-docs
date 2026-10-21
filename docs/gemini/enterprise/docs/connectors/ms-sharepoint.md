---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:44.719405+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Microsoft SharePoint data store for Gemini Enterprise lets you search and perform actions on your _Microsoft SharePoint Online_ data, including documents, lists, and sites.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported Microsoft SharePoint versions

The Microsoft SharePoint data store supports the latest cloud version of Microsoft SharePoint Online.

## Supported actions

When the Microsoft SharePoint data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions.

Action | Description  
---|---  
Create folder | Creates a new folder in a specified path.  
Add list | Creates a new structured data list (for example, tasks, contacts) on the Microsoft SharePoint site.  
Upload document | Uploads a document to a Microsoft SharePoint site or library.  
Download document | Downloads a document from a Microsoft SharePoint site or library.  
Add page | Creates a new page on the Microsoft SharePoint site.  
Check out document | Check out a document from a Microsoft SharePoint library.  
Check in document | Check a document into a Microsoft SharePoint library.  
Rename attachment or document | Rename an attachment or document in a Microsoft SharePoint library.  
Move attachment or document | Move a document from a Microsoft SharePoint library to a destination library, folder, or another SharePoint site.   
Discard check out document | Discards a check-out on a document, reverting it without saving changes.  
Share resource | Shares a document, folder, or resource with specified recipients or generates a share link.  
Update file properties | Updates metadata properties of a document in a Microsoft SharePoint library.  
Update page | Updates an existing page on the Microsoft SharePoint site.  
Update list | Updates settings of an existing structured data list on the Microsoft SharePoint site.  
Create list item | Creates a new item in a specified list on the Microsoft SharePoint site.  
Update list item | Updates fields of an existing item in a specified list.  
List lists | Retrieves all lists and document libraries in a specified Microsoft SharePoint site.  
Get list item | Returns a single list item, including all of its column values.  
Get list fields | Returns the schema of a specified list, including all of its fields and their properties.  
**Notes** : 

  * Additional read-only actions are also available.
  * The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB.



### Required permissions

To enable Gemini Enterprise to perform search and data ingestion using the Microsoft SharePoint data store, you need the following permissions:

#### Microsoft Graph API permissions

The table below outlines the permissions required for each connection mode.

**Note:** The following table outlines the permissions required for each connection mode. If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the permissions listed in the **Actions** row. 

**Connection mode** | **Scope** | **Purpose**  
---|---|---  
**Federated search** | N/A | No Graph API permissions are required.  
**Data ingestion** | `GroupMember.Read.All` | (Federated credentials & OAuth 2.0 refresh token) Allows the data store to read memberships and basic group properties for all groups without a signed-in user.  
`User.Read` | (Federated credentials & OAuth 2.0 refresh token) Allows the data store to read the profile of signed-in users. It also allows the data store to read basic company information of signed-in users.  
`User.Read.All` | (OAuth 2.0 refresh token only) Allows the data store to read user profiles.  
`Sites.FullControl.All` (Option 1)  
`Sites.Selected` (Option 2) | (Federated credentials & OAuth 2.0 refresh token) Option 1 allows the data store to have full control of all site collections. Option 2 allows the data store to access a subset of site collections. The specific site collections and the permissions granted can be configured in SharePoint Online.  
`User.Read.All` (Option 1)  
`User.ReadBasic.All` (Option 2) | (Federated credentials only) Option 1 allows the data store to read user profiles. Option 2 allows the data store to read a basic set of profile properties of other users in the organization.  
**Actions** | `Sites.ReadWrite.All` | (Federated search & Data ingestion) Allows the data store to edit or delete documents and list items in all site collections on behalf of the signed-in user.  
`Sites.Read.All` | (Federated search & Data ingestion) Allows the data store to read lists, list items, and list schemas in all site collections on behalf of the signed-in user. Required for the list lists, get list item, and get list fields actions.  
`Files.ReadWrite` | Allows the data store to read, create, update and delete the signed-in user's files.  
`Files.ReadWrite.All` | Allows the data store to read, create, update, delete, upload, and download all files the signed-in user can access.  
`Sites.Manage.All` | Allows the data store to create or delete document libraries and lists in all site collections on behalf of the user.  
  
#### Microsoft SharePoint API permissions

The table below outlines the permissions required for each connection mode.

**Connection mode** | **Scope** | **Purpose**  
---|---|---  
**Federated search** | `Sites.Search.All` (Delegated) | Allows the data store to run search queries and to read basic site info on behalf of the current signed-in user. Search results are based on the user's permissions instead of the app's permissions.  
`AllSites.Read` (Option 1, Delegated) | Allows the data store to read documents and list items in all site collections on behalf of the signed-in user.  
`Sites.Selected` (Option 2, Delegated) | Allows the data store to access a subset of site collections with a signed-in user. The specific site collections and the permissions granted can be configured in SharePoint Online.  
**Data ingestion (Federated credentials)** | `Sites.FullControl.All` (Option 1, Application) | Allows the data store to have full control of all site collections.  
`Sites.Selected` (Option 2, Application) | Allows the data store to access a subset of site collections with a signed-in user. The specific site collections and the permissions granted can be configured in SharePoint Online.  
**Data ingestion (OAuth 2.0 refresh token)** | `AllSites.FullControl` (Option 1, Delegated) | Allows the data store to have full control of all site collections on behalf of the signed-in user.  
`Sites.Selected` (Option 2, Delegated) | Allows the data store to access a subset of site collections with a signed-in user. The specific site collections and the permissions granted can be configured in SharePoint Online.  
**Actions** | `AllSites.Write` (Delegated) | Allows the data store to create, read, update, delete, upload, and download documents and list items in all site collections on behalf of the signed-in user.  
  
For information on how to add the permissions for Microsoft SharePoint, see [Configure Microsoft SharePoint and set the necessary permissions](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#configure-api-permissions).

## Limitations

This section outlines known issues and limitations that may affect your use of the Microsoft SharePoint data store.

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Microsoft SharePoint data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Microsoft SharePoint data store is supported only in the `global`, `us`, and `eu` locations.


  * **Search quality prerequisite:** To achieve optimal search results and fully leverage Knowledge Graph features, we recommend configuring and syncing the [People search data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people) in addition to the Microsoft SharePoint data store.



The following are the limitations for the Microsoft SharePoint federated data store:

  * **Search limitations** : Search results may vary and are not always comprehensive for all file types. Content in archived or encrypted folders may not be accessible for search. Federated search does not support searching within attachments.
  * **Delegated access:** Access to shared sites or libraries may require specific permissions not covered by standard user authorization.
  * **Layout parser in federated search mode:** While the layout parser is standard, its effectiveness on complex PDFs (with tables, multi-column layouts, or needing OCR) is limited in federated search mode. This mode's real-time API calls might not provide the complete data or time required for the deep analysis the layout parser performs during data ingestion.
  * **Unsupported PDF Features:** Consequently, complex PDF structures might not be fully analyzed or searchable. This includes: 
    * Multi-column text layouts
    * Data within embedded tables and charts
    * Text in scanned documents requiring Optical Character Recognition (OCR)
    * Documents with non-linear reading orders or intricate formatting.



### Recommendation

For Microsoft Sharepoint data containing PDFs with complex features (like tables, multi-column layouts, or OCR-dependent content), we recommend using standard ingestion mode for effective search. This mode allows the layout parser to deeply process and index the entire document content.

## Troubleshooting SharePoint connector search results

If you are experiencing issues with missing documents, incorrect results, or poor search relevance, check the following diagnostic areas:

  * **Check the People data store:** Ensure the [People search data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people) is set up and syncing if you face relevance or entity-matching issues.
  * **Authentication errors:** Persistent authentication errors, such as "Error when retrieving Graph API access token," will prevent searches from functioning. To resolve this, check the Microsoft Entra ID logs for details and then re-authenticate the connection.
  * **Identity mismatch:** If using Google Identity, verify that the user's Google email exactly matches their Microsoft SharePoint email. Mismatches prevent results from returning.
  * **Targeted folder searches (.aspx URLs):** Searching with full browser URLs that end in `/Forms/AllItems.aspx` executes a search across the whole site, not just the specific folder. Always use absolute folder paths for targeted searches.
  * **Result limits:** Be aware that federated searches may have limits on the number of documents returned per query (typically capping around 20 results).
  * **Citation issues:** Intermittent incorrect citations can occur. If persistent, report the issue to support and include your diagnostic tokens.
  * **Connector-model compatibility:** Ensure you are using the latest Gemini model versions. Some older models (for example, 3.x) have known issues resolving tools for SharePoint actions, such as `download_document` within Agent Builder.



## What's next

  * To create and configure a data store with Microsoft SharePoint, see [Set up a Microsoft SharePoint data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
