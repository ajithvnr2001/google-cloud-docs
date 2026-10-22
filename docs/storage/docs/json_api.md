---
url: https://docs.cloud.google.com/storage/docs/json_api/
title: Cloud Storage JSON API overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:04.248253+00:00
---

# Cloud Storage JSON API overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Cloud Storage JSON API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage JSON API is a simple, JSON-backed interface for accessing and manipulating Cloud Storage projects in a programmatic way. It is fully compatible with the [Cloud Storage Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries).

The JSON API is intended for software developers. To use it you should be familiar with web programming and be comfortable creating applications that consume web services through HTTP requests. If this does not describe you, consider one of the following alternatives:

  * If you are just starting out with Cloud Storage, you should first try either the [Google Cloud console Quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-console) or the [Google Cloud CLI Quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud). These tutorials demonstrate the basics of using Cloud Storage without the need to use the API directly.

  * If you are a mobile or web app developer, you can use the [Firebase SDKs](https://firebase.google.com/docs/storage/) for Cloud Storage.

  * If you are not a software developer and want to store your personal data in the cloud and share it with others, you can use [Google Drive](https://www.google.com/drive/).




The current release of the JSON API is `v1`.

## Partial response

By default, when Cloud Storage sends a resource in a response, it sends the full representation of the resource. For better performance, you can ask Cloud Storage to send only the fields you specify. This is called a _partial response_.

To request a partial response, use the `fields` request parameter to specify the fields you want returned. You can use this parameter with any request that returns response data. The `fields` parameter only affects the response data; it does not affect the data that you need to send, if any. To reduce the amount of data you send when modifying resources, use a `PATCH` request.

**Note:** As with all query parameter values, the `fields` parameter value must be URL encoded. For better readability, the examples in this page omit the encoding.

#### Syntax summary

The format of the `fields` request parameter value is loosely based on XPath syntax. When using the `fields` parameter, follow these guidelines:

  * Use a comma-separated list to return multiple fields.

For example, `fields=name,generation,size`.

  * Use `a/b` to return a field `b` that is nested within field `a`; use `a/b/c` to return a field `c` nested within `b`.

For example, `fields=metadata/key1`.

  * By default, if your request specifies particular fields, the server returns the objects or array elements in their entirety.Use a sub-selector to request a set of specific sub-fields of arrays or objects by placing expressions in parentheses.

For example: `fields=items(id,metadata/key1)` returns only the item ID and the `key1` custom metadata for each element in the items array. You can also specify a single sub-field, where `fields=items(id)` is equivalent to `fields=items/id`.

  * Each field specified in `fields` is relative to the root of the response. So if you are performing an operation to list objects, the response is a collection that includes as part of it an array of objects. If you are performing an operation that returns a single object or bucket, fields are specified relative to that particular resource. If the field you select is (or is part of) an array, the server returns the selected portion of all elements in the array.




Here are some collection-level examples, which typically apply when listing resources such as buckets and objects:

Example | Effect  
---|---  
`items` | Returns all elements in the items array, including all fields in each element, but no other fields.  
`etag,items` | Returns both the `etag` field and all elements in the items array.  
`items/metadata/key` | Returns only the `key` field for all members of the `metadata` object, which is itself nested under the `items` array.  
  
Whenever a nested field is returned, the response includes the enclosing parent objects. The parent fields do not include any other child fields unless they are also selected explicitly.  
`items(id,metadata/key)` | Returns only the values of the `id` and metadata `key` for each element in the items array.  
  
#### Handling partial responses

After a server processes a valid request that includes the `fields` query parameter, it sends back an HTTP `200 OK` status code, along with the requested data. If the `fields` query parameter has an error or is otherwise invalid, the server returns an HTTP `400 Bad Request` status code, along with an error message telling the user what was wrong with their fields selection (for example, `"Invalid field selection a/b"`).

#### Example

In a normal [JSON API request to retrieve object metadata](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get), Cloud Storage returns the [full object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource-representations) in the response.

However, by using the `fields` parameter in your request, you can significantly reduce the amount of data returned in the response:
    
    
    https://storage.googleapis.com/storage/v1/b/my-bucketT/o/my-object?**fields=id,name,metadata/key1**
    

**Partial response:** In response to the request above, the server sends back a response that contains only the kind information along with a pared-down items array that includes only the id, name, and the metadata/key property in each item, if present.
    
    
    **200 OK**
    
    
    {
      "id": "my-bucket/my-object.png/456456456456",
      "name": "my-object.png",
      "metadata": {
        "key1": "val1"
      }
    }

Note that the response is a JSON object that includes only the selected fields and their enclosing parent objects.

## Partial updates

You can avoid sending unnecessary data when modifying resources. To send updated values for specific fields of a resource's metadata, instead of replacing the resource's metadata in its entirety, use the HTTP `PATCH` verb.

The following Cloud Storage resources support `PATCH` requests:

  * [buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch)
  * [objects](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch)
  * [defaultObjectAccessControls](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls/patch)
  * [objectAccessControls](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls/patch)
  * [bucketAccessControls](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls/patch)



#### Semantics of a patch request

The body of the `PATCH` request includes only the resource fields you want to modify. When you specify a field, you must include any enclosing parent objects, just as the enclosing parents are returned with a partial response. The modified data you send is merged into the data for the parent object, if there is one.

  * **Add:** To add a field that doesn't already exist, specify the new field and its value.
  * **Modify:** To change the value of an existing field, specify the field and set it to the new value.
  * **Delete:** Although many fields cannot be deleted, some, such as [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) configurations and [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata), can be deleted. To do so, specify the field and set it to `null`. For example, `"metadata": null`.



**Note about arrays:** Patch requests that contain arrays replace the existing array with the one you provide. You cannot modify, add, or delete items in an array in a piecemeal fashion.

#### Handling the response to a patch

After processing a valid `PATCH` request, the API returns a `200 OK` HTTP response code along with the complete representation of the modified resource.

The patch request returns the entire resource representation unless you use the `fields` parameter to reduce the amount of data it returns.

If a patch request results in a new resource state that is syntactically or semantically invalid, the server returns a `400 Bad Request` or `422 Unprocessable Entity` HTTP status code, and the resource state remains unchanged. For example, if you attempt to delete the value for a required field, the server returns an error.

#### Alternate notation when PATCH HTTP verb is not supported

If your firewall does not allow HTTP `PATCH` requests, then you can send an HTTP `POST` request and set the override header to `PATCH`, as shown below:
    
    
    POST https://storage.googleapis.com/...
    X-HTTP-Method-Override: PATCH
    ...
    

#### Example

This example shows a simple patch request to update only the metadata of a Cloud Storage JSON API object. The object also has an id, a name, generation, and many other fields, but this request only sends the `metadata` field, since that's the only field being modified:
    
    
    PATCH https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME
    Authorization: Bearer OAUTH2_TOKEN
    Content-Type: application/json
    
    {
      "metadata": {"NEW_KEY" : "NEW_VALUE"}
    }

Response:
    
    
    **200 OK**
    
    
    {
      "id": "OBJECT_ID",
      "name": "OBJECT_NAME",
      "bucket": "BUCKET_NAME",
      "metadata": {
        "EXISTING_KEY" : "EXISTING_VALUE",
        "NEW_KEY" : "NEW_VALUE"
      },
      ...
    }

The server returns a `200 OK` status code, along with the full representation of the updated resource. Since only the `metadata` field was included in the patch request, that's the only value that is different from before.

## Query parameters

To use query parameters with a request, add `?`, the name of the query parameter, and the desired value to the end of the request URL. You can use this syntax with all JSON query parameters:
    
    
    https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?QUERY_PARAMETER=VALUE

For an example, see [Accessing noncurrent object versions](https://docs.cloud.google.com/storage/docs/using-versioned-objects#access).

You can specify multiple query parameters in the same request by using an `&` between each one:
    
    
    https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?QUERY_PARAMETER=VALUE&QUERY_PARAMETER_2=VALUE_2

For an example, see the [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects#upload-object-json) page.

## What's next

  * Learn more about [authenticating to the API](https://docs.cloud.google.com/storage/docs/authentication).

  * Learn about [request endpoints and URI path encoding](https://docs.cloud.google.com/storage/docs/request-endpoints).

  * [Read the JSON API reference pages](https://docs.cloud.google.com/storage/docs/json_api/v1).




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
