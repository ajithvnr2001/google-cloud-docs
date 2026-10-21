---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-object-acls/
title: Set object ACLs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:06.004084+00:00
---

# Set object ACLs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-object-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Set object ACLs Stay organized with collections  Save and categorize content based on your preferences. 

To change the ACLs on an object you make a PUT request that is scoped to the bucket and object and you use the `acl` query string parameter. You must also include an XML document in the request body that contains the ACL settings you want to apply.

You can also specify ACLs when you upload an object. To do this you can use the `x-goog-acl` request header. When you use the `x-goog-acl` request header you can apply one of the predefined ACLs. If you don't use the `x-goog-acl` request header when you upload an object, the default ACL (private) is applied to the object.

Keep in mind, a bucket's ACLs determines whether a user has permission to upload objects into the bucket. If a bucket grants `WRITE` permission to anonymous users, then users can upload objects without authenticating. Otherwise, all upload requests must be authenticated and only those users with `WRITE` permission can upload objects into a bucket.

You must have `FULL_CONTROL` permission to apply ACLs to an existing object.

**Note:** You can also set the ACLs on an existing object to a [predefined ACL](https://docs.cloud.google.com/storage/docs/access-control/lists#predefined-acl) by using the `x-goog-acl` request header in conjunction with the `acl` query string parameter. You must not include an XML document with the request and you must specify a predefined ACL in the request. When you do this, the `x-goog-acl` header takes precedence over the `acl` query string parameter and the predefined ACL is applied to the object.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#acl)` | Scopes the request to ACL changes only. You can use this only if you are using the PUT Object method to change ACLs on an existing object. You must specify the ACLs in an XML document in the request body. | No  
`[generation](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generation)` | Specifies the generation to update ACLs for. You can use this only if you are using the PUT Object method to change ACLs on an existing object. You must specify the ACLs in an XML document in the request body. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-object#request-headers).

## Request body elements

The following request body elements are applicable only if you use the `acl` query string parameter to apply ACLs to an existing object.

Element | Description  
---|---  
`Owner` | Container for object owner information.  
`ID` | The Cloud Storage ID of the object owner or the Cloud Storage ID of the user or group for whom the ACLs are being applied.  
`Name` | Comment field for `GroupByEmail`, `GroupById`, `UserByEmail`, and `UserById`. If you don't specify anything in `Name` when you apply an ACL, Cloud Storage populates this field with the email address you specified in `EmailAddress`.   
`AccessControlList` | Container for the ACLs you are applying.  
`Entries` | Container for the ACL entries you are applying.  
`Entry` | The ACL entry you are applying.  
`Scope` | The scope to which the ACLs apply.  
`Permission` | The permission you are granting. Can be any of the Cloud Storage permissions, including `READ`, `WRITE`, or `FULL_CONTROL`  
`EmailAddress` | A user account email address, a service account email address, or a Google group email address.  
`Domain` | A Google Workspace or Cloud Identity domain.  
  
## Request syntax

The following syntax applies to PUT Object requests that use the `acl` query string parameter.
    
    
    PUT /OBJECT_NAME?acl HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE
    Authorization: AUTHENTICATION_STRING
    
    XML_DOCUMENT_DEFINING_ACLS
    

The following syntax applies to conditional PUT Object requests that use the `acl` query string parameter as well as `generation` and `metageneration`.
    
    
    PUT /object?acl HTTP/1.1
    Host: bucket.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE
    Authorization: AUTHENTICATION_STRING
    x-goog-if-generation: GENERATION_NUMBER
    x-goog-if-metageneration: META_GENERATION_NUMBER
    
    XML_DOCUMENT_DEFINING_ACLS
    

The following syntax applies to conditional PUT Object for a history object that use the `acl` query string parameter as well as `generation` and `metageneration`.
    
    
    PUT /object?acl&generation=136088769710500 HTTP/1.1
    Host: bucket.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE
    Authorization: AUTHENTICATION_STRING
    x-goog-if-metageneration: META_GENERATION_NUMBER
    
    XML_DOCUMENT_DEFINING_ACLS
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample applies ACLs to the `london.jpg` object, which is stored in the `travel-maps` bucket. The ACLs grant jane@example.com `FULL_CONTROL` permission, which lets Jane download `london.jpg` and change the ACLs on `london.jpg`. The ACLs also grant joe@example.com `READ` permission to `london.jpg`, which lets Joe download `london.jpg`.

**Request**
    
    
    PUT /london.jpg?acl HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Sat, 20 Feb 2010 17:08:44 GMT
    Content-Length: 682
    Content-Type=application/xml; charset=UTF-8
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
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
          <Scope type="UserByEmail">
            <EmailAddress>jane@example.com</EmailAddress>
            <Name></Name>
          </Scope>
          <Permission>FULL_CONTROL</Permission>
        </Entry>
        <Entry>
          <Scope type="UserByEmail">
            <EmailAddress>joe@example.com</EmailAddress>
            <Name></Name>
          </Scope>
          <Permission>READ</Permission>
        </Entry>
      </Entries>
    </AccessControlList>
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date: Sat, 20 Feb 2010 17:08:45 GMT
    Content-Length: 0
    Content-Type: text/html
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
