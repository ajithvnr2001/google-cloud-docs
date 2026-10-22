---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/
title: Projects.hmacKeys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:50.066525+00:00
---

# Projects.hmacKeys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Projects.hmacKeys Stay organized with collections  Save and categorize content based on your preferences. 

The Projects.hmacKeys resource represents an HMAC key within Cloud Storage. The resource consists of a secret and HMAC key metadata. HMAC keys can be used as credentials for service accounts. For more information, see [HMAC Keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

Note that the Projects.hmacKeys resource is **only** returned when you use `hmacKey.create`. Other methods, such as `hmacKey.get`, return the metadata portion of the HMAC key resource.

For a list of methods for this resource, see the end of this page.

## Resource representations
    
    
    {
      "kind": "storage#hmacKey",
      "metadata": {
        "kind": "storage#hmacKeyMetadata",
        "id": string,
        "selfLink": string,
        "accessId": string,
        "projectId": string,
        "serviceAccountEmail": string,
        "state": string,
        "timeCreated": "datetime",
        "updated": "datetime",
        "etag": string
      },
      "secret": string
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For HMAC keys, this is always `"storage#hmacKey"`. |   
`metadata` | `object` | HMAC key metadata. |   
`metadata.accessId` | `string` | The access ID of the HMAC Key. |   
`metadata.etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the HMAC key. |   
`metadata.id` | `string` | The ID of the HMAC key, including the Project ID and the Access ID. |   
`metadata.kind` | `string` | The kind of item this is. For HMAC key metadata, this is always `"storage#hmacKeyMetadata"`. |   
`metadata.projectId` | `string` | The Project ID of the project that owns the service account to which the key authenticates. |   
`metadata.selfLink` | `string` | The link to this resource. |   
`metadata.serviceAccountEmail` | `string` | The email address of the key's associated service account. |   
`metadata.state` | `string` | The state of the key. Can be one of ACTIVE, INACTIVE, or DELETED. | writable  
`metadata.timeCreated` | `datetime`1 | The creation time of the HMAC key in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`metadata.updated` | `datetime`1 | The last modification time of the HMAC key metadata in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`secret` | `string` | HMAC secret key material. |   
1 This property is a string formatted as the specified value type. 

## Methods

Available methods for Projects.hmacKeys resources are as follows:

[create](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/create)
    Creates a new HMAC key for the specified service account.

[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/delete)
    Deletes an HMAC key.

[get](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/get)
    Retrieves an HMAC key's metadata.

[list](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/list)
    Retrieves a list of HMAC keys matching the criteria.

[update](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys/update)
    Updates the state of an HMAC key.

For information about status and error codes returned by these APIs, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
