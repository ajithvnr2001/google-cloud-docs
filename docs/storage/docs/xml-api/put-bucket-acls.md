---
url: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-acls/
title: Set bucket ACLs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:06.492192+00:00
---

# Set bucket ACLs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Set bucket ACLs Stay organized with collections  Save and categorize content based on your preferences. 

To set or modify the ACLs on an existing bucket you make a PUT request that is scoped to the bucket and you use the `acl` query string parameter. You must include an XML document in the request body that contains the ACL settings you want to apply. Notice that you cannot set the ACLs on a new bucket you are creating. (When you create a new bucket, the default ACL (project- private) is automatically applied to the bucket.)

You must have `FULL_CONTROL` permission to apply ACLs to an existing bucket. Also, you must be authenticated to use the PUT Bucket method. Anonymous bucket creation requests will fail.

**Note:** You can also set the ACLs on an existing bucket to a [predefined ACL](https://docs.cloud.google.com/storage/docs/access-control/lists#predefined-acl) by using the `x-goog-acl` request header in conjunction with the `acl` query string parameter. You must include an XML document with the request and you must specify a predefined ACL in the request. When you do this, the `x-goog-acl` header takes precedence over the `acl` query string parameter and the predefined ACL is applied to the bucket.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[acl](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#acl)` | You use this to change ACLs on an existing bucket. You must provide the ACL XML document in the request body. | No  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket#request-headers).

## Request body elements

The following request body elements are applicable only if you use the `acl` query string parameter to apply ACLs to an existing bucket.

Element | Description  
---|---  
`Owner` | Container for bucket owner information.  
`ID` | The Cloud Storage ID of the bucket owner or the Cloud Storage ID of the user or group for whom the ACLs are being applied.  
`Name` | Comment field for `GroupByEmail`, `GroupById`, `UserByEmail`, and `UserById`. If you don't specify anything in `Name` when you apply an ACL, Cloud Storage populates this field with the email address you specified in `EmailAddress`.   
`AccessControlList` | Container for the ACLs you are applying.  
`Entries` | Container for the ACL entries you are applying.  
`Entry` | The ACL entry you are applying.  
`Scope` | The scope to which the ACLs apply.  
`Permission` | The permission you are granting. Can be any of the Cloud Storage permissions, including `READ`, `WRITE`, or `FULL_CONTROL`  
`EmailAddress` | A user account email address, a service account email address, or a Google group email address.  
`Domain` | A Google Workspace or Cloud Identity domain.  
  
## Request syntax
    
    
    PUT /?acl HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: REQUEST_BODY_LENGTH
    Content-Type: MIME_TYPE_OF_THE_BODY
    Authorization: AUTHENTICATION_STRING
    
    XML_DOCUMENT_DEFINING_ACLS
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The response does not include an XML document in the response body.

## Example

The following sample applies ACLs to a bucket named `acme-pets`. The ACLs grant `WRITE` permission to joe@example.com. Granting `WRITE` permission lets Joe upload, delete, and list objects in the `acme-pets` bucket. The ACLs also grant jane@example.com `FULL_CONTROL` of the `acme-pets` bucket, which lets Jane upload objects, delete objects, list objects, and modify ACLs on the `acme-pets` bucket.

**Request**
    
    
    PUT /?acl HTTP/1.1
    Host: acme-pets.storage.googleapis.com
    Date: Thu, 10 Jun 2010 03:38:42 GMT
    Content-Length: 705
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
          <Permission>WRITE</Permission>
        </Entry>
      </Entries>
    </AccessControlList>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
