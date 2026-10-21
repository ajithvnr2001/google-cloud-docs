---
url: https://docs.cloud.google.com/gemini/enterprise/docs/identity/
title: Configure access controls for custom data sources \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:12.327606+00:00
---

# Configure access controls for custom data sources  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/identity/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure access controls for custom data sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enforce data source access control (also referred to as ACLs) for search apps you create using Cloud Storage or BigQuery.

## Overview

Access control for your data sources in Gemini Enterprise limits the data that users can view in your search app's results. Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents that are returned as results.

For example, say that employees at your company search across BigQuery documents using your search app. However, you need to make sure they can't view content through the app that they aren't allowed to access. If you have set up a workforce pool in Google Cloud for your organization's identity provider, then you can also specify that workforce pool in Gemini Enterprise. Now, if an employee uses your app, they get search results only for documents that their account already has access to in BigQuery.

Turning on access control is a one-time procedure. To apply access control to a BigQuery or Cloud Storage data source, use the following steps depending on your data type, such as structured or unstructured data.

  * Unstructured data from Cloud Storage
  * Structured data from Cloud Storage
  * Unstructured data from BigQuery
  * Structured data from BigQuery



## Unstructured data from Cloud Storage

When setting up a data store for unstructured data from Cloud Storage, you need to also upload ACL metadata and set the data store as access controlled:

  1. When preparing your data, include ACL information in your metadata using the `acl_info` field. For example:
         
         {
            "id": "<your-id>",
            "jsonData": "<JSON string>",
            "content": {
              "mimeType": "<application/pdf or text/html>",
              "uri": "gs://<your-gcs-bucket>/directory/filename.pdf"
            },
            "acl_info": {
              "readers": [
                {
                  "principals": [
                    { "group_id": "group_1" },
                    { "user_id": "user_1" }
                  ]
                }
              ]
            }
          }
         

For more information about unstructured data with metadata, see the Unstructured data section of [Prepare data for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data#unstructured).

  2. When following the steps for data store creation in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), you can enable access control by doing the following in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the field `"aclEnabled": "true"` in your JSON payload.
  3. When following the steps for data import in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), make sure to do the following:

     * Upload your metadata with ACL information from the same bucket as your unstructured data
     * If using the API, set [`GcsSource.dataSchema`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/GcsSource) to `document`



## Structured data from Cloud Storage

When setting up a data store for structured data from Cloud Storage, you need to also upload ACL metadata and set the data store as access controlled:

  1. When preparing your data, include ACL information in your metadata using the `acl_info` field. For example:
         
         {
            "id": "<your-id>",
            "jsonData": "<JSON string>",
            "acl_info": {
              "readers": [
                {
                  "principals": [
                    { "group_id": "group_1" },
                    { "user_id": "user_1" }
                  ]
                }
              ]
            }
          }
         

  2. When following the steps for data store creation in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), you can enable access control by doing the following in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the field `"aclEnabled": "true"` in your JSON payload.
  3. When following the steps for data import in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), make sure to do the following:

     * Upload your metadata with ACL information from the same bucket as your structured data
     * If using the API, set [`GcsSource.dataSchema`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/GcsSource) to `document`



## Unstructured data from BigQuery

When setting up a data store for unstructured data from BigQuery, you need to set the data store as access controlled and provide ACL metadata using a predefined schema for Gemini Enterprise:

  1. When preparing your data, specify the following schema. Don't use a custom schema.
         
         [
           {
             "name": "id",
             "mode": "REQUIRED",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "jsonData",
             "mode": "NULLABLE",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "content",
             "type": "RECORD",
             "mode": "NULLABLE",
             "fields": [
               {
                 "name": "mimeType",
                 "type": "STRING",
                 "mode": "NULLABLE"
               },
               {
                 "name": "uri",
                 "type": "STRING",
                 "mode": "NULLABLE"
               }
             ]
           },
           {
             "name": "acl_info",
             "type": "RECORD",
             "mode": "NULLABLE",
             "fields": [
               {
                 "name": "readers",
                 "type": "RECORD",
                 "mode": "REPEATED",
                 "fields": [
                   {
                     "name": "principals",
                     "type": "RECORD",
                     "mode": "REPEATED",
                     "fields": [
                       {
                         "name": "user_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       },
                       {
                         "name": "group_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       }
                     ]
                   }
                 ]
               }
             ]
           }
         ]
         

  2. Include your ACL metadata as a column in your BigQuery table.

  3. When following the steps in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), enable access control in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the field `"aclEnabled": "true"` in your JSON payload.
  4. When following the steps for data import in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), if using the API, set [`BigQuerySource.dataSchema`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/BigQuerySource) to `document`.




## Structured data from BigQuery

When setting up a data store for structured data from BigQuery, you need to set the data store as access controlled and provide ACL metadata using a predefined schema for Gemini Enterprise:

  1. When preparing your data, specify the following schema. Don't use a custom schema.
         
         [
           {
             "name": "id",
             "mode": "REQUIRED",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "jsonData",
             "mode": "NULLABLE",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "acl_info",
             "type": "RECORD",
             "mode": "NULLABLE",
             "fields": [
               {
                 "name": "readers",
                 "type": "RECORD",
                 "mode": "REPEATED",
                 "fields": [
                   {
                     "name": "principals",
                     "type": "RECORD",
                     "mode": "REPEATED",
                     "fields": [
                       {
                         "name": "user_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       },
                       {
                         "name": "group_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       }
                     ]
                   }
                 ]
               }
             ]
           }
         ]
         

  2. Include your ACL metadata as a column in your BigQuery table.

  3. When following the steps in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), enable access control in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the field `"aclEnabled": "true"` in your JSON payload.
  4. When following the steps for data import in [Create a first-party data store](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store), make sure to do the following:

     * If using the console, then when specifying the kind of data you're uploading, select **JSONL for structured data with metadata**.
     * If using the API, set [`BigQuerySource.dataSchema`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/BigQuerySource) to `document`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
