---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-object-acls/
title: Get object ACLs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:41.021666+00:00
---

# Get object ACLs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-object-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Get object ACLs Stay organized with collections  Save and categorize content based on your preferences. 

Lists an object's ACLs.

You must have `READ` permission to download an object, and you must have `FULL_CONTROL` permission to retrieve an object's ACLs.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#acl)` | You can use this only if you are using the GET Object method to list an object's ACLs. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-object#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Object requests that use the `acl` query string parameter.
    
    
    GET /OBJECT_NAME?acl HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Content-Length: 0
    Content-Type: TYPE
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use, including: [Cache-Control](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol), [Content-Length](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength), [Content-Type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype), [Content-Disposition](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition), [ETag](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#etag), and [Last-Modified.](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#lastmodified)

## Response body elements

The following response body elements are applicable only if you use the `acl` query string parameter to list an object's ACLs.

Element | Description  
---|---  
`Owner` | Container for object owner information.  
`ID` | The Cloud Storage ID of the object owner or the Cloud Storage ID of the user or group for whom the ACLs apply.  
`Name` | Comment field for `GroupByEmail`, `GroupById`, `UserByEmail`, and `UserById`.  
`AccessControlList` | Container for the ACLs you are retrieving.  
`Entries` | Container for the ACL entries you are retrieving.  
`Entry` | The ACL entry you are retrieving.  
`Scope` | The scope to which the ACLs apply.  
`Permission` | The permission that has been granted. Can be any of the Cloud Storage permissions, including `READ`, `WRITE`, or `FULL_CONTROL`  
`EmailAddress` | A user account email address, a service account email address, or a Google group email address.  
`Domain` | A Google Workspace or Cloud Identity domain.  
  
## Example

The following example lists the ACLs for an object named `paris.jpg` that is in a bucket named `travel-maps`. In this sample, the object's ACL grants jane@example.com `FULL_CONTROL` permission on the `paris.jpg` object, which lets that user download the object and change the ACLs on the object.

**Request**
    
    
    GET /paris.jpg?acl HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    

**Response**
    
    
    HTTP/1.1 200 OK
    Content-Length: 485
    Content-Type: application/xml
    Date: Fri, 19 Feb 2010 14:05:08 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <AccessControlList>
      <Owner>
        <ID>84fac329bceSAMPLE777d5d22b8SAMPLE77d85ac2SAMPLE2dfcf7c4adf34da46</ID>
        <Name></Name>
      </Owner>
      <Entries>
        <Entry>
          <Scope type="UserById">
            <ID>84fac329bceSAMPLE777d5d22b8SAMPLE77d85ac2SAMPLE2dfcf7c4adf34da46</ID>
            <Name></Name>
          </Scope>
          <Permission>FULL_CONTROL</Permission>
        </Entry>
        <Entry>
          <Scope type="UserById">
            <ID>76fac329bceSAMPLE777d5d22b8SAMPLE77d85ac2SAMPLE2dfcf7c4adf34da79</ID>
            <Name>jane@example.com</Name>
          </Scope>
          <Permission>FULL_CONTROL</Permission>
        </Entry>
        </Entries>
      </AccessControlList>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
