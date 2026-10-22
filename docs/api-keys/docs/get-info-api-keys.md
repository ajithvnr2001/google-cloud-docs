---
url: https://docs.cloud.google.com/api-keys/docs/get-info-api-keys/
title: Getting information about API keys \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:14.690939+00:00
---

# Getting information about API keys  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/get-info-api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Guides ](https://docs.cloud.google.com/api-keys/docs/how-to)



Send feedback 

#  Getting information about API keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the API key methods to:

  * List API keys in a project
  * Get metadata for an API key
  * Get the key string
  * Get the key name and project for a key string



## Listing API keys in a project

You can get a list of all the keys owned by a Google Cloud project with the `ListKeys` method:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

On success, you get a response similar to the following:
    
    
    {
      "keys": [
        {
          "name": "projects/12345678/locations/global/keys/2885bf87-5b84-47fa-92af-08c3e9337349",
          "displayName": "API key 2",
          "createTime": "2019-05-29T22:07:22.036Z",
          "uid": "2885bf87-5b84-47fa-92af-08c3e9337349",
          "updateTime": "2019-05-29T22:07:22.058623Z",
          "restrictions": {
            "androidKeyRestrictions": {}
          },
          "etag": "zHib8eXEMCxe4ayQEbIaZg=="
        },
        {
          "name": "projects/12345678/locations/global/keys/a4db08b7-5729-4ba9-8c08-f2df493465a1",
          "displayName": "API key 1",
          "createTime": "2019-05-29T22:06:58.844Z",
          "uid": "a4db08b7-5729-4ba9-8c08-f2df493465a1",
          "updateTime": "2019-05-29T22:06:58.855103Z",
          "restrictions": {
            "androidKeyRestrictions": {}
          },
          "etag": "0L5KcPMGoNi53K5+FqPxiw=="
        }
      ]
    }

By default, the `ListKeys` method returns a list of the usable API keys. To view the list of all keys, including keys that are marked for deletion, add the query parameter `show_deleted=true`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys?show_deleted=true'

On success, you get a response similar to the following:
    
    
    {
      "keys": [
        {
          "name": "projects/12345678/locations/global/keys/5d3564ad-f08e-48df-b0ca-0f50858ba3f2",
          "displayName": "Key 1",
          "createTime": "2019-06-12T04:47:30.214Z",
          "uid": "5d3564ad-f08e-48df-b0ca-0f50858ba3f2",
          "updateTime": "2021-03-05T22:35:37.387645Z",
          "deleteTime": "2021-03-05T22:35:37.290544Z",
          "etag": "V96UGAyyz+6sUHttzK42pQ=="
        },
        {
          "name": "projects/12345678/locations/global/keys/7ad567fa-c11b-4903-99dc-88f89da7d73a",
          "displayName": "Key 2",
          "createTime": "2019-06-12T00:47:27.778Z",
          "uid": "7ad567fa-c11b-4903-99dc-88f89da7d73a",
          "updateTime": "2021-03-05T22:23:57.002187Z",
          "deleteTime": "2021-03-05T22:23:56.350234Z",
          "etag": "njPE6YjwHlrh6TLyxHibBg=="
        },
        {
          "name": "projects/12345678/locations/global/keys/a4db08b7-5729-4ba9-8c08-f2df493465a1",
          "displayName": "API key 1",
          "createTime": "2019-05-29T22:06:58.844Z",
          "uid": "a4db08b7-5729-4ba9-8c08-f2df493465a1",
          "updateTime": "2019-05-29T22:06:58.855103Z",
          "restrictions": {
            "androidKeyRestrictions": {}
          },
          "etag": "0L5KcPMGoNi53K5+FqPxiw=="
        }
      ]
    }

The `deleteTime` field stores when the delete command was issued. Keys are permanently deleted 30 days after the delete command was issued.

If you have a lot of API keys in your project, you might prefer to page the results rather than having all of the keys returned. To control the number or results per page, add the `pageSize` query parameter set to the number of results that you want returned:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys?pageSize=25'

The end of the response contains the `nextPageToken` field. To get the next page of results, include the token in the next call by adding the `pageToken` query parameter:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys?pageSize=25&pageToken=TOKEN'

## Getting metadata for an API key

To get metadata about a specific API key, call the `GetKey` method with the `Key.name`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys/KEY_ID'

## Getting the key string

For security, the `ListKeys` and `GetKey` methods don't return the `Key.keyString`. To get the `keyString` for an API key, call the `GetKeyString` method with the `Key.name`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/Key.name/keyString'

The calling user must have the `apikeys.keys.getKeyString` permission to call the `GetKeyString` method.

## Looking up a key name and project by key string

If you have a `keyString` and you need to lookup the key `name` and the project that owns the API key, call the `LookupKey` method and specify the `keyString` query parameter:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/keys:lookupKey?keyString=KEY_STRING'

The response is similar to the following: 
    
    
    {
      "parent": "projects/12345678/locations/global",
      "name": "projects/12345678/locations/global/keys/2c437be3-1c77-417b-8f6f-748189760227"
    }

In the response:

  * The `parent` field contains the project number of the Google Cloud project in which the API key was created.
  * The `name` field contains the unique identifier for the API key.



## What's next

  * [Adding restrictions to API keys](https://docs.cloud.google.com/api-keys/docs/add-restrictions-api-keys)
  * [Viewing Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)
  * [Troubleshooting](https://docs.cloud.google.com/api-keys/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
