---
url: https://docs.cloud.google.com/storage/docs/xml-api/post-bucket/
title: Delete multiple objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:42.728778+00:00
---

# Delete multiple objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/post-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Delete multiple objects Stay organized with collections  Save and categorize content based on your preferences. 

To delete up to 1,000 objects from a bucket in a single request, you make a `POST` request to the bucket's URI and include the `delete` query string parameter. The request body must contain an XML document that specifies the objects you want to delete.

## Query string parameters

This request includes the [`delete`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#delete) query string parameter.

## Request headers

Include the following request headers:

Header | Description | Required  
---|---|---  
`[Authorization](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization)` | The authentication string for the request. | Yes  
`[Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength)` | The size of the request body in bytes. | Yes  
`[Date](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#date)` | The date and time of the request. | Yes  
`[Host](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#host)` | The URI for Cloud Storage. For more information, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints). | Yes  
`[x-goog-user-project](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject)` | The project to be billed for charges associated with the request. | No  
  
## Request body elements

The request body for a multi-object delete operation must be an XML document with the following elements:

Element | Description  
---|---  
`Delete` | The container for the objects you want to delete.  
`Object` | A container for a single object you want to delete.  
`Key` | The name of the object to be deleted.  
`VersionId` (Optional) | The version ID of the object to be deleted. If omitted, Cloud Storage attempts to delete the live version of the object. The result depends on whether [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) or [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) are enabled for the bucket:

  * If Object Versioning is enabled, deleting the live version makes it noncurrent, and has the same version id.
  * If Object Versioning is disabled but Soft delete is enabled, deleting the live version makes it soft-deleted and recoverable during its retention period.
  * If neither Object Versioning nor Soft delete are enabled, deleting the live version permanently deletes it.

If you include `VersionId`, you target a specific version for deletion. If Soft delete is enabled, the specified version becomes soft-deleted; otherwise it is permanently deleted.  
`Quiet` (Optional) | If set to `True`, the response body doesn't list successfully deleted objects. If you don't include this element or set it to `False`, the response lists every object that was successfully deleted. We recommend setting the `Quiet` element to `False` to receive a verbose response. A verbose response lets you do the following:

  * Identify which objects were successfully deleted.
  * Identify which objects failed to delete and the associated error codes.

  
  
## Request syntax
    
    
    POST /?delete HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Authorization: AUTHENTICATION_STRING
    
    <Delete>
      <Object>
        <Key>OBJECT_NAME_1</Key>
        <VersionId>VERSION_ID_1</VersionId>
      </Object>
      <Object>
        <Key>OBJECT_NAME_2</Key>
        <VersionId>VERSION_ID_2</VersionId>
      </Object>
      <Quiet>False</Quiet>
    </Delete>
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response body is an XML document that provides a status for each object you requested to delete.

Element | Description  
---|---  
`DeleteResult` | The container for the entire response.  
`Deleted` | A container for an object that was successfully deleted.If the `Quiet` element in the request body is set to `True`, this element isn't included in the response.  
`Key` | The name of the successfully deleted object.  
`VersionId` | The version ID of the successfully deleted object.  
`Error` | A container for an object that wasn't deleted due to an error.  
`Code` | The error code for the object that failed to delete.  
`Message` | A detailed error message.  
  
## Example

The following example attempts to delete multiple objects from a bucket named `my-bucket`. It includes the `Quiet` element set to `False` to receive a verbose response, showing two successfully deleted objects and a failed object deletion.

### Request
    
    
    POST /?delete HTTP/1.1
    Host: my-bucket.storage.googleapis.com
    Date: Thu, 12 Mar 2026 03:38:42 GMT
    Content-Length: 1320
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    <Delete>
      <Object>
        <Key>image1.jpg</Key>
      </Object>
      <Object>
        <Key>document.pdf</Key>
      </Object>
      <Object>
        <Key>private/financial_data.xlsx</Key>
      </Object>
      <Quiet>False</Quiet>
    </Delete>
    

### Response
    
    
    <DeleteResult>
      <Deleted>
        <Key>image1.jpg</Key>
      </Deleted>
      <Deleted>
        <Key>document.pdf</Key>
      </Deleted>
      <Error>
        <Code>AccessDenied</Code>
        <Key>private/financial_data.xlsx</Key>
        <Message>Access Denied. You don't have permission to delete this object.</Message>
      </Error>
    </DeleteResult>

## What's next

  * Learn about [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).
  * Learn about [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) for automated object deletions.
  * Learn about [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) for deleting more than 1,000 objects.
  * Learn how to [delete a bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
