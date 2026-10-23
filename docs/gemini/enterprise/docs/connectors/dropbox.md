---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/
title: Overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:15.307169+00:00
---

# Overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The Dropbox data store for Gemini Enterprise lets you search and perform actions on your Dropbox data.

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service.

## Supported actions

When a Dropbox data store is configured and enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions:

Action | Description  
---|---  
Create folder |  Create a folder in the user's Dropbox.   
Copy file or folder |  Copy a file or folder in the user's Dropbox.   
Upload file |  Upload a file to the user's Dropbox.   
Download file |  Download a file from the user's Dropbox.   
**Notes** : 

  * Additional read-only actions are also available.
  * The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB.



### Minimum permissions for actions

To enable Gemini Enterprise to perform search and necessary actions for Dropbox, you need the following minimum permissions.

Scope | Description  
---|---  
account_info.read |  Required to be registered for user-linked apps.   
files.metadata.read |  Allows the data store to read the metadata of files and folders in the user's account.   
files.content.read |  Allows the data store to read file contents and download files from the user's account.   
files.content.write |  Allows the data store to upload files to the user's account.   
  
For information about how to configure these permissions, see [Dropbox configuration](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/config).

## Limitations

The Dropbox data store for Gemini Enterprise has the following limitations:

  * When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type.


  * Enforcing a VPC Service Controls perimeter on existing Dropbox data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).


  * The Dropbox data store is supported only in the `global`, `us`, and `eu` locations.



## What's next

  * To create and configure a Dropbox data store for use with Gemini Enterprise, see [Set up a Dropbox data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/data-store).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
