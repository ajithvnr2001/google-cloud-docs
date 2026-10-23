---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose/
title: Objects: compose \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:32.181667+00:00
---

# Objects: compose  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: compose Stay organized with collections  Save and categorize content based on your preferences. 

Concatenates a list of existing objects into a new object in the same bucket.

If the source objects are meant to be temporary, you can hard delete the source objects as part of the composition process. If you don't delete the source objects during the composition process, the source objects are unaffected.

For a general discussion of object composition, see [Composite objects](https://docs.cloud.google.com/storage/docs/composite-objects), and for tool-specific guides to performing a composition, see [Compose objects](https://docs.cloud.google.com/storage/docs/composing-objects).

## Required permissions

The authenticated user must have the `storage.objects.create` and `storage.objects.get` IAM permissions to use this method. The authenticated user must also have the following permissions in the specified scenarios:

  * `storage.objects.delete`: If the new composite object overwrites an existing object.
  * `storage.objects.setRetention`: If the request body includes the `retention` property.
  * `storage.objects.createContext`: If the request body includes a non-empty `destination.contexts.custom` property.
  * `storage.objects.dropContexts`: If the `dropContextGroups` parameter is used.



## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/o/destinationObject/compose

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket containing the source objects. The destination object is stored in this bucket.   
`destinationObject` | `string` |  Name of the new object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Optional query parameters**  
`destinationPredefinedAcl` | `string` |  Apply a predefined set of access controls to the destination object.   
  
Acceptable values are: 

  * `authenticatedRead`: Object owner gets `OWNER` access, and `allAuthenticatedUsers` get `READER` access.
  * `bucketOwnerFullControl`: Object owner gets `OWNER` access, and project team owners get `OWNER` access.
  * `bucketOwnerRead`: Object owner gets `OWNER` access, and project team owners get `READER` access.
  * `private`: Object owner gets `OWNER` access.
  * `projectPrivate`: Object owner gets `OWNER` access, and project team members get access according to their roles.
  * `publicRead`: Object owner gets `OWNER` access, and `allUsers` get `READER` access.

If `iamConfiguration.uniformBucketLevelAccess.enabled` is set to `true`, requests that include this parameter fail with a `400 Bad Request` response.   
`dropContextGroups` | `string` |  Specifies which groups of [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) from the source objects should be dropped on the destination object during the compose operation. The accepted value is `custom`, which discards all object contexts.   
`ifGenerationMatch` | `long` |  Makes the operation conditional on there being a live destination object with a generation number that matches the given value. Setting `ifGenerationMatch` to 0 makes the operation succeed only if there is no live destination object.   
`ifMetagenerationMatch` | `long` |  Makes the operation conditional on there being a live destination object with a metageneration number that matches the given value.   
`kmsKeyName` | `string` |  [Resource name of the Cloud KMS key](https://docs.cloud.google.com/kms/docs/resource-hierarchy#retrieve_resource_id) that will be used to encrypt the composed object. If not specified, the request uses the bucket's default Cloud KMS key, if any, or else it uses [standard Cloud Storage encryption](https://docs.cloud.google.com/storage/docs/encryption/default-keys).   
**Optional extension headers**  
`X-Goog-Encryption-Algorithm` | `string` |  The encryption algorithm to use, which must be `AES256`. Used when encrypting the composed object with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Encryption-Key` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of your AES-256 encryption key. Used when encrypting the composed object with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
`X-Goog-Encryption-Key-Sha256` | `string` |  An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of the SHA256 hash of your encryption key. Used when encrypting the composed object with a [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
  
### Request body

In the request body, supply data with the following structure:
    
    
    {
      "kind": "storage#composeRequest",
      "sourceObjects": [
        {
          "name": "string",
          "generation": "long",
          "objectPreconditions": {
            "ifGenerationMatch": "long"
          }
        }
      ],
      "destination": [objects Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource),
      "deleteSourceObjects": boolean
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. |   
`deleteSourceObjects` | `boolean` | Whether to hard delete the source objects. The default is `false`. | writable  
`destination` | `nested object` | Properties of the resulting object. |  writable   
`sourceObjects[]` | `list` | The list of source objects that will be concatenated into a single object. This list can contain up to 32 source objects. |   
`sourceObjects[].name` | `string` | The source object's name. All source objects must reside in the same bucket and use the same [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). |  writable   
`sourceObjects[].generation` | `long`1 | The generation of this object to use as the source. |  writable   
`sourceObjects[].objectPreconditions` | `object` | Conditions that must be met for this operation to execute. |   
`sourceObjects[].objectPreconditions.ifGenerationMatch` | `long`1 | Only perform the composition if the generation of the source object that would be used matches this value. If this value and a generation are both specified, they must be the same value or the call will fail. |  writable   
1 This property is a string formatted as the specified value type. 

## Response

If successful, this method returns an [object resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource) in the response body, with the `owner` and `acl` properties omitted.

For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
