---
url: https://docs.cloud.google.com/api-keys/docs/create-manage-api-keys/
title: Creating and managing API keys \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:10.578048+00:00
---

# Creating and managing API keys  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/create-manage-api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Guides ](https://docs.cloud.google.com/api-keys/docs/how-to)



Send feedback 

#  Creating and managing API keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create and manage API keys using the API Keys API.

For information on how to use an API key with your calls to Google Cloud APIs, see [Using API keys](https://docs.cloud.google.com/docs/authentication/api-keys).

## Creating an API key

You can create an API key by using the [`CreateKey`](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys/create) method. The method requires a [`Key`](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key) parameter. You can only specify `displayName` and `restrictions` fields of the `Key` object. The `CreateKey` isn't a synchronous method. Instead, when you issue a call to `CreateKey`, you initiate a long-running [operation](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/operations). The following example issues a `CreateKey` call to create an API key with no restrictions:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "Example API key"
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys'

On success, the method returns a long-running operation in the response. As described in [Polling long running operations](https://docs.cloud.google.com/api-keys/docs/polling-operations), you repeatedly make [`operations.get`](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/operations/get) calls with the value from the `name` field. When the response from `operations.get` contains `"done": true`, the `response` object contains a `Key`, similar to the following:
    
    
    {
      "name": "operations/akmf.p7-103621867718-06f94db2-7e91-4c58-b826-e6b80e4dc3eb",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.api.apikeys.v2.Key",
        "name": "projects/PROJECT_NUMBER/locations/global/keys/aecd7943-98ff-4ce2-a876-ec1b37c671ca",
        "displayName": "Example API key",
        "keyString": "----REDACTED----",
        "createTime": "2021-03-23T17:39:46.721099Z",
        "uid": "aecd7943-98ff-4ce2-a876-ec1b37c671ca",
        "updateTime": "2021-03-23T17:39:47.046746Z",
        "etag": "k0bsYGkIvSxDVwNxyw49NQ=="
      }
    }

In the `response` object:

  * The `name` field contains a unique identifier for the API key. You use the value in the `name` field in the other methods that require a key name. This value isn't displayed in the Google Cloud console, but you can call the [`ListKeys`](https://docs.cloud.google.com/api-keys/docs/get-info-api-keys#list-keys) method to get the `names` for all of your API keys. The `Key.name` field is always in the following format: `projects/PROJECT_NUMBER/locations/global/keys/KEY_ID`.
  * The `displayName` field maps to the `Name` field in the Google Cloud console, so you might want to provide a `displayName` when you call `CreateKey`.
  * The `keyString` field contains the string that you send to the APIs that require an API key. The `keyString` maps to the `API key` field in the Google Cloud console. You can call the [`GetKeyString`](https://docs.cloud.google.com/api-keys/docs/get-info-api-keys#get-key-string) method to get the `keyString` for an API key.
  * The `etag` field contains a checksum computed by the server based on the current value of the key. Please pass the `etag` value when you call `UpdateKey` and `DeleteKey` methods.



### User-specified key ID

You can specify a [`keyId`](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys/create#query-parameters) as a query parameter for `CreateKey` method. When specified, the value becomes the final component of the `Key.name`.

For example, consider the following call to `CreateKey`:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName" : "Example API key with user-specified ID"
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys?keyId=my-test-key1'

For this example, the `Key.name` field has the following value:
    
    
    "name": "projects/PROJECT_NUMBER/locations/global/keys/my-test-key1"
    

## Updating the display name

To change the `displayName` of an API key or to add a `displayName` to an API key that was created without one, call the `UpdateKey` method. When you call `UpdateKey`, you initiate a long-running operation that updates the key.

The following example illustrates how to call `UpdateKey`:
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
              "displayName": "New display name",
              "etag" : "ETAG"
            }' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys/KEY_ID?updateMask=displayName'

When the response from `operations.get` contains `"done": true`, the `response` contains an `Key` object with the updated `displayName`.

## Deleting an API key

To delete an API key, use the `DeleteKey` method. When you call `DeleteKey`, you initiate a long-running operation that marks the key as `DELETED`.

The following example illustrates how to call `DeleteKey`:
    
    
    curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H 'If-Match: "ETAG"' \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys/KEY_ID'

When the response from `operations.get` contains `"done": true`, the `response` is similar to the following:
    
    
    {
      "name": "operations/akmf.cdabc4df-cbff-4420-8c7e-65dc832c945d",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.api.apikeys.v2.Key"
        "name": "projects/PROJECT_NUMBER/locations/global/keys/aecd7943-98ff-4ce2-a876-ec1b37c671ca",
        "displayName": "Example API key",
        "keyString": "----REDACTED----",
        "createTime": "2021-03-23T17:39:46.721099Z",
        "uid": "aecd7943-98ff-4ce2-a876-ec1b37c671ca",
        "updateTime": "2021-03-23T17:39:47.046746Z",
        "deleteTime": "2021-03-24T22:35:37.290544Z",
        "etag": "k0bsYGkIvSxDVwNxyw49NQ=="
      }
    }

An API key that is marked as `DELETED` can't be used, but it isn't completely removed from our system either. To list the API keys that still exist but that are marked as `DELETED`, set `show_deleted` to true for `ListKeys` method:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys?show_deleted=true'

After 30 days, the API key is permanently deleted.

## Restoring an API key

To restore an API key before it is permanently deleted, call the `UndeleteKey` method. When you call `UndeleteKey`, you initiate a long-running operation that marks the key as `ACTIVE`.

The following example illustrates how to call `UndeleteKey`:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         'https://apikeys.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/keys/KEY_ID/:undelete'

## What's next

  * [Getting information about API keys](https://docs.cloud.google.com/api-keys/docs/get-info-api-keys)
  * [Adding restrictions to API keys](https://docs.cloud.google.com/api-keys/docs/add-restrictions-api-keys)
  * [Viewing Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)
  * [Troubleshooting](https://docs.cloud.google.com/api-keys/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
