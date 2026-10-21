---
url: https://docs.cloud.google.com/storage/docs/xml-api/post-object-v2/
title: POST Object with the V2 signing process \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:06.865396+00:00
---

# POST Object with the V2 signing process  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/post-object-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)



Send feedback 

#  POST Object with the V2 signing process Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This page covers legacy material related to the V2 signing process. See [`POST` Object](https://docs.cloud.google.com/storage/docs/xml-api/post-object-forms) and [Signatures](https://docs.cloud.google.com/storage/docs/authentication/signatures) for the recommended workflow when using HTML forms.

Uploads objects by using HTML forms. For tips on uploading to Cloud Storage, see [best practices](https://docs.cloud.google.com/storage/docs/best-practices#uploading).

Unless you need to use HTML forms (usually through a web browser) to upload objects, we strongly recommend using [`PUT` object](https://docs.cloud.google.com/storage/docs/xml-api/put-object) instead of `POST`.

**Note:** The `POST` object method does not support [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls), except in the case of [resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads).

## Query string parameters

This request does not include query string parameters.

## Form fields

Field | Description | Required  
---|---|---  
`acl` | The predefined ACL that you want to apply to the object that is being uploaded. If you do not specify this field the bucket's `default` ACL is applied. | No  
`bucket` | The name of the bucket that you want to upload to. Alternatively, you can include the bucket name in the `key` field or in the URI (for example, storage.googleapis.com/BUCKET_NAME). | No  
[` Cache-Control`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol) | The cache control for the object. You can only set cache control for an object that is accessible to all users. For instance, an object's ACL must be `public-read` or `public-read-write` to be able to set the cache-control. | No  
[ `Content-Disposition`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition) | Specifies how the object data should be transmitted. For example, a `Content-Disposition` value of `inline` means that the object should be displayed immediately. | No  
[ `Content-Encoding`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding) | The compression algorithm for the object, such as `gzip`. | No  
[ `Content-Length`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength) | Specifies that uploaded files can only be between a certain size range in bytes. You can specify this condition using the following syntax: ["content-length-range", MIN_RANGE, MAX_RANGE]. | No  
[ `Content-Type`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype) | The MIME type of the file you are uploading via the form. If you do not specify a content type, the Cloud Storage system defaults to [`application/octet-stream`](https://datatracker.ietf.org/doc/html/rfc2046#section-4.5.1){:.external} when it serves the content. | No  
`Expires` | An [ISO8601 timestamp](http://www.w3.org/TR/NOTE-datetime) that specifies the date and time before an object is considered stale by the browser. | No  
`file` | The file you are uploading. Must be the last field in the form. You can upload only one object per request. | Yes  
`GoogleAccessId` | Email address of the entity responsible for creating the `signature`. This entity is typically a [service account](https://docs.cloud.google.com/iam/docs/service-accounts), but may also be a user account. | Only if you specify a `policy`  
`key` | The name of the object that you are uploading. If you specify the object name without the bucket name, you must append the bucket name to the URI (for example, storage.googleapis.com/BUCKET_NAME). If you specify the bucket name and object name (for example, bucket/object), you must specify only the URI (for example, storage.googleapis.com). You can also use the ${filename} variable if a user is providing a file name. Also, if you are using a bucket name that is a `CNAME` redirect, be sure that the bucket name is specified only once in your request. | Yes  
`policy` | The security policy that describes what can and cannot be uploaded in the form. The policy document must be Base64 encoded. See the policy document section for more information. *If you do not provide a security policy, requests are considered to be anonymous and will only work with buckets that have granted `WRITE` or `FULL_CONTROL` permission to anonymous users. | No*  
`signature` | The signature of the Base64-encoded policy document you are including in the request. Your signature must be signed using a [ secret key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) that is associated with the `GoogleAccessID` you specified. | Only if you specify a `policy`  
`success_action_redirect` | A URL that users are redirected to when an upload is successful. If you do not provide a URL, Cloud Storage responds with the status code that you specified in `success_action_status`. | No  
`success_action_status` | The status code that you want Cloud Storage to respond with when an upload is successful. The default is 204, but you can change this to 200 or 201. If you choose 200 or 204, Cloud Storage returns an empty document with those status codes. If you choose 201, Cloud Storage returns an XML document with the elements that are described in Response Body Elements. Note: The Adobe Flash player might not handle responses with an empty document body. You should use status code 201 if this is the case. | No  
`x-goog-meta-*` | A field for custom metadata. You can use this to specify any additional metadata that is not provided by the other form fields. For example, `x-goog-meta-reviewer: jane` or `x-goog-meta-project-manager: john` is custom metadata. | No  
  
## Response body elements

The following response body elements are returned in an XML document only if you set `success_action_redirect` to 201.

Element | Description  
---|---  
`Bucket` | Bucket in which the object was stored.  
`ETag` | [HTTP 1.1 entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the object.  
`Key` | The object's name.  
`Location` | The URI for the object.  
  
## Usage and examples

The form must be UTF-8 encoded. You can specify form encoding in the form's HTML `head` tag or by using the `Content-Type` request header.

Your `form` tag must specify the following three items:

  * An action.

The `action` attribute specifies the bucket that you want the form to upload an object to.

  * A method.

The `method` attribute specifies the method that you are using to submit the form. It must be `post`.

  * An enclosure type.

The `enctype` attribute specifies the enclosure type you are using and must always be `multipart/form-data`.




### Policy Document

A policy document defines what a user (with or without a user account) can upload with a form POST, and provides authorization to ensure that the form can upload files into the target bucket. You can use policy documents to allow visitors to a website to upload files to Cloud Storage. You do not need to include a policy document in a form if your form uploads files to a bucket that grants anonymous users `WRITE` permission. For more information about configuring access to buckets and objects in Cloud Storage, see [Access Control](https://docs.cloud.google.com/storage/docs/access-control).

A policy document is constructed in JavaScript Object Notation (JSON) and contains the following sections:

Entry | Description  
---|---  
`expiration` | The expiration time of the policy document. An expired policy document will cause the HTML form to break. This must be in [ISO8601](http://www.w3.org/TR/NOTE-datetime) format.  
`conditions` | An array of conditions that every upload must satisfy.  
  
The `conditions` section must include a condition statement for every field in your HTML form except the `GoogleAccessId`, `signature`, `file`, and `policy` fields. It is possible to express three types of conditions in your `conditions` section:

  * **Exact Matching**

Performs exact matching for a field. The value of the input field's value must match the specified expected value. You can specify this condition using either of the following syntax styles:
        
        {"FIELD" : "VALUE"}
        ["eq", "$FIELD", "VALUE"]

All valid policy document fields specified in the table below can use exact matching.

  * **Starts With**

If a value of a field must start with a certain value, you can use the `starts-with` condition. You can specify this condition using the following syntax:
        
        ["starts-with", "$FIELD", "VALUE"]

All valid policy document fields specified in the table below can use the `starts-with` condition.

  * **Content Length Range**

Specifies that uploaded files can only be between a certain size range in bytes. You can specify this condition using the following syntax:
        
        ["content-length-range", MIN_RANGE, MAX_RANGE]




You can express the following fields in the `conditions` section, using exact matching, `content-length-range` or `starts- with` conditions:

**Warning:** Not specifying a `"bucket"` condition in the policy document will put your system at risk, including man-in-the-middle attacks that redirect the upload to other buckets. Such a policy document is strongly discouraged.Element | Description | `acl` | ACL values for the object from possible predefined ACLs.  
---|---  
`bucket` | The bucket that will hold the object.  
[ `cache-control`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#cachecontrol) | Cache-control for the object.  
[ `content-disposition`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentdisposition) | Specifies how the object data should be transmitted.  
[ `content-encoding`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentencoding) | The compression algorithm for the object.  
[ `content-length`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength) | The byte length of the request body.  
[ `content-type`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contenttype) | The MIME type of the file that is being uploaded.  
`expires` | An [ISO8601 timestamp](http://www.w3.org/TR/NOTE-datetime) that specifies the data and time before an object is considered stale by the browser.  
`key` | The name of the object you are uploading.  
`success_action_redirect` | The URL the user's client is redirected to when the upload is successful.  
`success_action_status` | The status code that you want Cloud Storage to respond with when an upload is successful.  
`x-goog-meta-*` | An extension header that can be used to store additional metadata that is not provided by the other fields.  
  
The following is an example of a typical policy document:
    
    
    {"expiration": "2010-06-16T11:11:11Z",
     "conditions": [
      ["starts-with", "$key", "" ],
      {"acl": "bucket-owner-read" },
      {"bucket": "travel-maps"},
      {"success_action_redirect": "http://www.example.com/success_notification.html" },
      ["eq", "$Content-Type", "image/jpeg" ],
      ["content-length-range", 0, 1000000]
      ]
    }
    

The previous policy document defines the following conditions:

  * The form expires on June 16, 2010 at 11:11:11 UTC.
  * The file name can start with any valid character. To specify this, you use the `starts-with` condition modifier and the empty string ("").
  * The `bucket-owner-read` ACL is applied to the file.
  * If the upload is successful, the user is redirected to `http://www.example.com/success_notification.html`.
  * The form allows only images to be uploaded.
  * A user cannot upload a file larger than 1 MB.

**Note:** The date and time in the `expiration` field must be represented in ISO 8601 format.

If you are including a policy document in your form, you must include a signature in the `signature` form field. The following procedure shows you how to create the signature:

  1. Create a policy document for your form and make sure it is UTF-8 encoded.
  2. Encode the policy document as a Base64 representation.
  3. Sign your policy document using RSA with SHA-256 using a [secret key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) associated with the `GoogleAccessID` specified in the form field. If you are using [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys), sign instead using SHA-1.
  4. Encode the message digest as a Base64 representation.



The following pseudocode combines the steps above to create your signature:
    
    
    Policy = Base-64-Encoding-Of(PolicyDocument)
    MessageDigest = SHA256withRSA(SecretKey, Policy)
    Signature = Base64-Encoding-Of(MessageDigest)
    

Below is the Python implementation of the code to create your signature. Note that because the M2Crypto library only supports PKCS1 (PEM) formatting, `key.pem` is your service account PKCS12 key converted into the PKCS1 format.
    
    
    from base64 import b64encode
    from M2Crypto import EVP
    def Sign(pem_key, message):
        assert pem_key
        key = EVP.load_key_string(pem_key)
        key.reset_context(md='sha256')
        key.sign_init()
        key.sign_update(str(message))
        return key.sign_final()
    
    SecretKey = open('key.pem', 'r').read()
    Policy = b64encode(open('policy.txt', 'r').read())
    Signature = b64encode(Sign(SecretKey, Policy))
    print Policy
    print
    print Signature
    

The following is an example HTML using the policy document above:
    
    
    <form action="http://travel-maps.storage.googleapis.com" method="post" enctype="multipart/form-data">
    <input type="text" name="key" value="">
    <input type="hidden" name="bucket" value="travel-maps">
    <input type="hidden" name="Content-Type" value="image/jpeg">
    <input type="hidden" name="GoogleAccessId" value="1234567890123@developer.gserviceaccount.com">
    <input type="hidden" name="acl" value="bucket-owner-read">
    <input type="hidden" name="success_action_redirect" value="http://www.example.com/success_notification.html">
    <input type="hidden" name="policy" value="eyJleHBpcmF0aW9uIjogIjIwMTAtMDYtMTZUMTE6MTE6MTFaIiwNCiAiY29uZGl0aW9ucyI6IFsNCiAgWyJzdGFydHMtd2l0aCIsICJrZXkiLCAiIiBdLA0KICB7ImFjbCI6ICJidWNrZXQtb3duZXItcmVhZCIgfSwNCiAgeyJidWNrZXQiOiAidHJhdmVsLW1hcHMifSwNCiAgeyJzdWNjZXNzX2FjdGlvbl9yZWRpcmVjdCI6ICJodHRwOi8vd3d3LmV4YW1wbGUuY29tL3N1Y2Nlc3Nfbm90aWZpY2F0aW9uLmh0bWwiIH0sDQogIFsiZXEiLCAiQ29udGVudC1UeXBlIiwgImltYWdlL2pwZWciIF0sDQogIFsiY29udGVudC1sZW5ndGgtcmFuZ2UiLCAwLCAxMDAwMDAwXQ0KICBdDQp9">
    <input type="hidden" name="signature" value="BSAMPLEaASAMPLE6SAMPLE+SAMPPLEqSAMPLEPSAMPLE+SAMPLEgSAMPLEzCPlgWREeF7oPGowkeKk7J4WApzkzxERdOQmAdrvshKSzUHg8Jqp1lw9tbiJfE2ExdOOIoJVmGLoDeAGnfzCd4fTsWcLbal9sFpqXsQI8IQi1493mw=">
    
    <input name="file" type="file">
    <input type="submit" value="Upload">
    </form>
    

As a best practice you should use the `Expect: 100-continue` header with POST requests. This allows you to verify that the server will handle the request before you send the object. If you receive a status code 100 Continue you should proceed with the request. If you receive a status code 417 Expectation Failed then you should not send the object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
