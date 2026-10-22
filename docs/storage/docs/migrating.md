---
url: https://docs.cloud.google.com/storage/docs/migrating/
title: Fully migrate from Amazon S3 to Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:27.720111+00:00
---

# Fully migrate from Amazon S3 to Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Fully migrate from Amazon S3 to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to fully migrate from Amazon Simple Storage Service (Amazon S3) to Cloud Storage for users sending requests using an API. After you fully migrate, you can use all the features of Cloud Storage, including multiple projects and OAuth 2.0 for authentication.

If you want to get started with Cloud Storage quickly, you can choose a [simple migration](https://docs.cloud.google.com/storage/docs/aws-simple-migration), which requires just a few changes to the tools and libraries you're using with Amazon S3.

## Migrate from Amazon S3 to Cloud Storage

To fully migrate from Amazon S3 to Cloud Storage, you need to complete the following steps:

  * Change any existing `x-amz-*` headers to corresponding `x-goog-*` headers.
  * Change AWS Access Control List (ACL) XML to the corresponding Cloud Storage ACL XML (see [Creating and managing access control lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists)).
  * Set the [x-goog-project-id](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogprojectid) header in your requests.
  * Get set up to use [OAuth 2.0 authentication](https://datatracker.ietf.org/doc/html/rfc6749). Using OAuth 2.0 means that your `Authorization` header looks like this:
        
        Authorization: Bearer OAUTH2_TOKEN

OAuth 2.0 relies on SSL for security instead of requiring your application to do cryptographic signing directly and is easier to implement. With OAuth, your application can request access to data associated with a user's account, and access can be scoped to several levels, including read-only, read-write, and full-control. For more information, see [Cloud Storage OAuth 2.0 scopes](https://docs.cloud.google.com/storage/docs/oauth-scopes) and [Accessing data on a user's behalf](https://docs.cloud.google.com/storage/docs/user-accounts).




## Access control

This section shows a few examples of access control to help you migrate from Amazon S3 to Cloud Storage. For an overview of access control in Cloud Storage, see [Access Control](https://docs.cloud.google.com/storage/docs/access-control).

In Cloud Storage, there are several ways to apply ACLs to buckets and objects (see [Creating and managing access control lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists)). Two of the ways you specify ACLs are analogous to what you do in Amazon S3:

  * The `acl` query string parameter lets you apply ACLs for specific scopes.
  * The `x-goog-acl` request header lets you apply predefined ACLs, which are sometimes known as canned ACLs.



### Using the acl query string parameter

You can use the `acl` query string parameter for a Cloud Storage request exactly the same way you would use it for an Amazon S3 request. The `acl` parameter is used in conjunction with the `PUT` method to apply ACLs to the following: an existing object, an existing bucket, or a bucket you are creating. When you use the `acl` query string parameter in a `PUT` request, you must attach an XML document (using Cloud Storage ACL syntax) to the body of your request. The XML document contains the individual ACL entries that you want to apply to the bucket or object.

The following example shows a `PUT` request to Amazon S3 that uses the `acl` query string parameter. ACLs are defined in an XML document sent in the request body. The `PUT` request changes the ACLs on an object named `europe/france/paris.jpg` that is in a bucket named `my-travel-maps`. The ACL grants jeffersonloveshiking@gmail.com `FULL_CONTROL` permission.
    
    
    PUT europe/france/paris.jpg?acl HTTP/1.1
    Host: my-travel-maps.**s3.amazonaws.com**
    Date: Wed, 06 Nov 2013 19:28:18 GMT
    Content-Length: 598
    Content-Type: application/xml
    **Authorization: AWS4-HMAC-SHA256 Credential=AWS-ACCESS-KEY/20131106/us-east-1/s3/aws4_request, SignedHeaders=content-length;content-type;date;host, Signature=4c45f25bb679fdab0de5a287625d6a143414728d93c9aeb9f4cc91c33a1c45fg**
    
    <?xml version='1.0' encoding='utf-8'?>
    **< AccessControlPolicy>**
      <Owner>
        <ID>5a6557ba40f7c86496ffceae789fcd888abc1b62a7149873a0fe12c0f60a7d95</ID>
        <DisplayName>ownerEmail@example.com</DisplayName>
      </Owner>
      <AccessControlList>
        <Grant>
          <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
            <ID>fd447671d60b979f78ee6fcec7b22afc80e6b26a4db16eed01afb8064047949b</ID>
            <DisplayName>jeffersonloveshiking@gmail.com</DisplayName>
          </Grantee>
          <Permission>FULL_CONTROL</Permission>
        </Grant>
      </AccessControlList>
    **< /AccessControlPolicy>**
    

Here is the same request to Cloud Storage:
    
    
    PUT europe/france/paris.jpg?acl HTTP/1.1
    Host: my-travel-maps.**storage.googleapis.com**
    Date: Wed, 06 Nov 2013 19:37:33 GMT
    Content-Length: 268
    Content-Type: application/xml
    **Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg**
    
    <?xml version='1.0' encoding='utf-8'?>
    **< AccessControlList>**
      <Entries>
      <Entry>
        <Permission>FULL_CONTROL</Permission>
        <Scope type="UserByEmail">
          <EmailAddress>jeffersonloveshiking@gmail.com</EmailAddress>
        </Scope>
      </Entry>
      </Entries>
    **< /AccessControlList>**
    

Note that Cloud Storage does not require an `<Owner/>` element in the ACL XML document. For more information, see [Bucket and object ownership](https://docs.cloud.google.com/storage/docs/access-control/lists#ownership).

You can also retrieve bucket and object ACLs by using the `acl` query string parameter with the `GET` method. The ACLs are described in an XML document, which is attached to the body of the response. You must have `FULL_CONTROL` permission to apply or retrieve ACLs on an object or bucket.

### Apply ACLs with an extension request header

You can use the `x-goog-acl` header in a Cloud Storage request to apply predefined ACLs to buckets and objects exactly the same way you would use the `x-amz-acl` header in an Amazon S3 request. You typically use the `x-goog-acl` (`x-amz-acl`) header to apply a predefined ACL to a bucket or object when you are creating or uploading the bucket or object. The Cloud Storage predefined ACLs are similar to Amazon S3 [Canned ACLs](http://docs.aws.amazon.com/AmazonS3/latest/dev/ACLOverview.html#CannedACL), including private, public-read, public-read-write, as well as others. For a list of Cloud Storage predefined ACLs, see [Predefined ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#predefined-acl).

The following example shows a `PUT` Object request that applies the `public-read` ACL to an object named `europe/france/paris.jpg` that is being uploaded into a bucket named `my-travel-maps` in Amazon S3.
    
    
    PUT europe/france/paris.jpg HTTP/1.1
    Host: my-travel-maps.**s3.amazonaws.com**
    Date: Wed, 06 Nov 2013 20:48:42 GMT
    Content-Length: 888814
    Content-Type: image/jpg
    **x-amz-acl** : public-read
    **Authorization: AWS4-HMAC-SHA256 Credential=AWS-ACCESS-KEY/20131106/us-east-1/s3/aws4_request, SignedHeaders=content-length;content-type;date;host, Signature=808150c37dbd1b425b2398421d6fc3dd6d4942dfaae9e519fd5835aa62fd62ab**
    
    <_888814 bytes in entity body_ >
    

Here is the same request to Cloud Storage:
    
    
    PUT europe/france/paris.jpg HTTP/1.1
    Host: my-travel-maps.**storage.googleapis.com**
    Date: Wed, 06 Nov 2013 20:49:57 GMT
    Content-Length: 888814
    Content-Type: image/jpg
    **x-goog-acl** : public-read
    **Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg**
    
    <_888814 bytes in entity body_ >
    

You can also use the `x-goog-acl` header to apply a predefined ACL to an existing bucket or object. To do this, include the `acl` query string parameter in your request but don't include an XML document in your request. Applying a predefined ACL to an existing object or bucket is useful if you want to change from one predefined ACL to another, or you want to update custom ACLs to a predefined ACL. For example, the following `PUT` Object request applies the predefined ACL `private` to an object named `europe/france/paris.jpg` that is in a bucket named `my-travel-maps`.
    
    
    PUT europe/france/paris.jpg?acl HTTP/1.1
    Host: my-travel-maps.storage.googleapis.com
    Date: Wed, 06 Nov 2013 00:26:36 GMT
    Content-Length: 0
    **x-goog-acl: private**
    **Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg**
    
    <_empty entity body_ >
    

For more information about managing ACLs, see [Creating and managing access control lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists).

## Migrate from Amazon S3 to Cloud Storage request methods

Cloud Storage supports the same standard HTTP request methods for reading and writing data to your buckets as are supported in Amazon S3. Therefore, the majority of your tools and libraries that you use with Amazon S3, work as-is with Cloud Storage. Cloud Storage supports the following request methods:

  * Service request for `GET`.
  * Bucket requests, including `PUT`, `GET`, `DELETE`, and `POST`.
  * Object requests, including `GET`, `POST`, `PUT`, `HEAD`, and `DELETE`.



For more information, see XML API [Reference Methods](https://docs.cloud.google.com/storage/docs/xml-api/reference-methods). Keep in mind that when you send requests to Cloud Storage, you need to change the request body, when applicable, to use the appropriate Cloud Storage syntax. For example, when you create a lifecycle configuration for a bucket, use the Cloud Storage lifecycle XML, which is different than the Amazon S3 lifecycle XML.

There are a few differences between Cloud Storage XML API and Amazon S3 which are summarized below:

Amazon S3 Functionality | Cloud Storage XML API Functionality  
---|---  
When using customer-supplied encryption keys in a [multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads), the final request does not include the customer-supplied encryption key. | In the Cloud Storage XML API, all requests in a multipart upload, including the final request, require you to supply the same customer-supplied encryption key. This requirement exists because Cloud Storage does not store your encryption key information while it waits for the request to complete the upload, but it requires the key to calculate a checksum for the completed object.  
GET/POST bucket query string parameters: 

  * "policy" - Working with Amazon S3 bucket policies.
  * "notification" - Notifying for bucket events.
  * "requestPayment" - Configuring who pays for the request and the data download from a bucket.

| Alternatives: 

  * "policy" - Cloud Storage ACLs, project team membership, and the ability to use multiple projects address many of the scenarios where bucket policies are used.
  * "notification" - Use gcloud CLI or JSON API [Pub/Sub Notifications](https://docs.cloud.google.com/storage/docs/pubsub-notifications).
  * "requestPayment" - In Cloud Storage, the equivalent query string parameter to `requestPayment` is `billing`.

  
  
## Migrate from Amazon S3 to Cloud Storage headers

Cloud Storage uses several standard HTTP headers as well as several custom (extension) HTTP headers. If you are transitioning from Amazon S3 to Cloud Storage, you can convert your custom Amazon S3 headers to the equivalent Cloud Storage custom header or similar functionality as shown in the tables below.

For many Amazon S3 headers, you simply need to replace the `x-amz` prefix with `x-goog`:

Amazon S3 Header | Cloud Storage Header  
---|---  
`x-amz-storage-class` | `x-goog-storage-class`  
`x-amz-acl` | `x-goog-acl`  
`x-amz-date` | `x-goog-date`  
`x-amz-meta-*` | `x-goog-meta-*`  
`x-amz-copy-source` | `x-goog-copy-source`  
`x-amz-metadata-directive` | `x-goog-metadata-directive`  
`x-amz-copy-source-if-match` | `x-goog-copy-source-if-match`  
`x-amz-copy-source-if-none-match` | `x-goog-copy-source-if-none-match`  
`x-amz-copy-source-if-unmodified-since` | `x-goog-copy-source-if-unmodified-since`  
`x-amz-copy-source-if-modified-since` | `x-goog-copy-source-if-modified-since`  
**Note:** While Amazon S3 does not have an equivalent header to `x-goog-project-id`, Cloud Storage accepts `x-amz-project-id` for [simple migrations](https://docs.cloud.google.com/storage/docs/aws-simple-migration).

Several headers differ or don't apply in Cloud Storage:

Amazon S3 Header | Cloud Storage Header  
---|---  
`x-amz-server-side-encryption` | Not required. Cloud Storage automatically encrypts all data before it is written to disk. For more information, see [Encryption](https://docs.cloud.google.com/storage/docs/encryption).  
`x-amz-grant-*` | [`x-goog-acl`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogacl) with a predefined ACL value.  
`x-amz-version-id` | [`x-goog-generation`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooggeneration)  
`x-amz-mfa` | Use [OAuth 2.0 Authentication](https://datatracker.ietf.org/doc/html/rfc6749).  
[`x-amz-decoded-content-length`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xamzdecodedcontentlength) | Not supported as an `x-goog` header  
`x-amz-website-redirect-location`, `x-amz-copy-source-range` | n/a  
  
See [HTTP headers and query string parameters for XML API](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers) for a reference to Cloud Storage headers.

## Impact of organization policies on HMAC key authentication

If the workloads you're migrating from Amazon S3 to Cloud Storage depend on [hash-based message authentication code (HMAC) keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) for authentication, be aware that the [Google Cloud Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) allows administrators to enforce security constraints. The `constraints/storage.restrictAuthTypes` policy can be used to prevent the use of specific authentication types. For more information about each authentication type, see [Restrict authentication types](https://docs.cloud.google.com/storage/docs/org-policy-constraints#restrict-auth-types).

If your organization has a policy in place that denies the type of HMAC keys your tools are configured to use, your attempts to connect to Cloud Storage fail with a `403 Forbidden` error.

To prevent this error from occurring, before migrating workflows that depend on HMAC key authentication, consult with your Google Cloud organization administrator to determine if the `constraints/storage.restrictAuthTypes` policy is enforced and which authentication types, if any, are restricted. If HMAC key usage isn't permitted, you need to adapt your tools and applications to use alternative Google Cloud authentication methods, such as service account credentials with OAuth 2.0.

## What's next

  * [Plan a migration from Amazon S3](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage).
  * [Transfer your data to Cloud Storage from external sources](https://docs.cloud.google.com/storage-transfer/docs/create-transfers), such as Amazon S3 and Microsoft Azure Blob Storage, using Storage Transfer Service.
  * [Create event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers) that use Amazon S3 Event Notifications to keep a Cloud Storage bucket in sync with Amazon S3.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
