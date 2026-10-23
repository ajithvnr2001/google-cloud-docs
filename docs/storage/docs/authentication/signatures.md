---
url: https://docs.cloud.google.com/storage/docs/authentication/signatures/
title: Signatures \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:36.720774+00:00
---

# Signatures  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/authentication/signatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Signatures Stay organized with collections  Save and categorize content based on your preferences. 

Signatures are one method for authenticating requests being sent to the [Cloud Storage XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview). Signatures are used, for example, when working with signed URLs or HTML forms. This page applies to signatures created using the V4 signing process, which is the recommended process for creating signatures.

Signatures are specific to the Cloud Storage XML API and are distinct from [OAuth 2.0](https://docs.cloud.google.com/storage/docs/authentication) tokens; OAuth 2.0 tokens can also be used with the XML API and are more generally applicable across Google Cloud services, including the [Cloud Storage JSON API](https://docs.cloud.google.com/storage/docs/json_api).

## Overview

_Signatures_ provides both identity and strong authentication, which ensures that requests to Cloud Storage are processed using the authority of a specific account. Signatures achieve such authentication without revealing the sensitive key information, called _secrets_ or _private keys_ , associated with that account.

When you make a request with a signature, Cloud Storage uses its copy of the key information to calculate an equivalent signature for the request. If the signature included in the request matches the signature calculated by Cloud Storage, then Cloud Storage knows that the signature was created using the relevant secret or private key.

In Cloud Storage, signatures must be used when working with:

  * [Signed URLS](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).
  * [HTML forms](https://docs.cloud.google.com/storage/docs/xml-api/post-object-forms).



Additionally, signatures can be used in the [`Authorization` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization) of XML API requests.

Using signatures in direct requests is useful when performing [simple migrations from Amazon S3](https://docs.cloud.google.com/storage/docs/aws-simple-migration); however, the recommended authentication flow for direct requests is to use [OAuth 2.0](https://docs.cloud.google.com/storage/docs/authentication) tokens.

### Structure

The components and process for creating a signature depend on what you will use it for and the authentication key you're working with; broadly, there are two components to a signature: the _signing key_ and _request information_. You apply a _signing algorithm_ to these two components to create the signature. The table below summarizes the different use cases for signatures and the components you need in each case to construct the signature:

Use case | Signing Key | Request information  
---|---|---  
HTML form with an RSA key | Directly use RSA private key | Base64-encoded policy document  
HTML form with an HMAC key | Derive from HMAC key's secret | Base64-encoded policy document  
Signed URL or signed header with an RSA key | Directly use RSA private key | String-to-sign  
Signed URL or signed header with an HMAC key | Derive from HMAC key's secret | String-to-sign  
  
## String-to-sign

A _string-to-sign_ includes meta information about your request and a hash of the [canonical request](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests) that you want to sign.

### Structure

A string-to-sign must be UTF-8 encoded and has the following structure, including the use of newlines between each element:
    
    
    SIGNING_ALGORITHM
    ACTIVE_DATETIME
    CREDENTIAL_SCOPE
    HASHED_CANONICAL_REQUEST

#### Signing algorithm

The value you use for SIGNING_ALGORITHM depends on the type of key you use and the extensions you use for your headers or query parameters:

Use case | Value for SIGNING_ALGORITHM  
---|---  
`x-goog-*` extensions and an RSA key | `GOOG4-RSA-SHA256`  
`x-goog-*` extensions and an HMAC key | `GOOG4-HMAC-SHA256`  
`x-amz-*` extensions and an HMAC key | `AWS4-HMAC-SHA256`  
  
#### Active datetime

The date and time the signature can be used, in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) basic format `YYYYMMDD'T'HHMMSS'Z'`.

  * For signed URLs, the signature is usable from 15 minutes prior to the active datetime until the expiration time you specify. The active datetime must match the signed URL's `X-Goog-Date` query string parameter and must use the same day that you specify in the credential scope.

  * For requests with signed headers, the signature is usable from 15 minutes prior to the active datetime until 15 minutes after the active datetime. The active datetime must match the `x-goog-date` header of the request using the signature, and the active datetime must use the same day that you specify in the credential scope.




#### Credential Scope

The credential scope for the request.

#### Hash of the canonical request

The hex-encoded SHA-256 hash of a [canonical request](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests). Use a SHA-256 hashing function to create a hash value of the canonical request. Your programming language should have a library for creating SHA-256 hashes. An example hash value looks like:
    
    
    436b7ce722d03b17d3f790255dd57904f7ed61c02ac5127a0ca8063877e4e42c

### Example

The following is an example of a properly formed string-to-sign, with newlines shown as actual new lines and not `\n`:
    
    
    GOOG4-RSA-SHA256
    20191201T190859Z
    20191201/us-central1/storage/goog4_request
    54f3076005db23fbecdb409d25c0ccb9fb8b5e24c59f12634654c0be13459af0

## Policy document

A policy document defines what users with access to the corresponding [HTML form](https://docs.cloud.google.com/storage/docs/xml-api/post-object-forms) can upload to Cloud Storage. A policy document provides authorization to ensure that the HTML form can upload files into the target bucket. You can use policy documents to allow visitors to a website to upload files to Cloud Storage.

A policy document is constructed in JavaScript Object Notation (JSON). The policy document must be both UTF-8 and Base64-encoded. A policy document contains the following sections:

Entry | Description  
---|---  
`expiration` | The expiration time of the policy document, in the [ISO 8601](http://www.w3.org/TR/NOTE-datetime) basic format `YYYYMMDD'T'HHMMSS'Z'`. An expired policy document causes the HTML form to break.  
`conditions` | An array of conditions that every upload must satisfy.  
  
The `conditions` section must include:

  * A condition statement for each [field](https://docs.cloud.google.com/storage/docs/xml-api/post-object-forms#form_fields) that you use in your HTML form, except for the `x-goog-signature`, `file`, and `policy` fields.

  * A `"bucket"` condition statement, even if you don't use the bucket field in your HTML form.




If you want to use multiple condition statements for the same field, you should make a separate HTML form for each. Three types of conditions can be used in your condition statements:

  * **Exact Matching**

Performs exact matching for a field. The value used in the specified field of the HTML form must match the value set in this condition. Set this condition using either of the following syntax styles:
        
        {"field" : "value"}
        
        ["eq", "$field", "value"]

All valid HTML form fields except `Content-Length` can use exact matching.

  * **Starts With**

If a field's value must start with a certain prefix, use the `starts-with` condition with the following syntax:
        
        ["starts-with", "$field", "value"]

If a field's value has no restrictions, use the `starts-with` condition with the following syntax:
        
        ["starts-with", "$field", ""]

All valid HTML form fields except `Content-Length` can use the `starts-with` condition.

  * **Content Length Range**

Specifies a range of acceptable values that can be used in the `Content-Length` field. Specify this condition using the following syntax:
        
        ["content-length-range", min_range, max_range]




### Example

The following is an example of a policy document:
    
    
    {"expiration": "2020-06-16T11:11:11Z",
     "conditions": [
      ["starts-with", "$key", ""],
      {"bucket": "travel-maps"},
      {"success_action_redirect": "http://www.example.com/success_notification.html"},
      ["eq", "$Content-Type", "image/jpeg"],
      ["content-length-range", 0, 1000000],
      {"x-goog-algorithm": "GOOG4-RSA-SHA256"},
      {"x-goog-credential": "example_account@example_project.iam.gserviceaccount.com/20191102/us-central1/storage/goog4_request"},
      {"x-goog-date": "20191102T043530Z"}
      ]
    }
    

This policy document defines the following conditions:

  * The form expires on June 16, 2020 at 11:11:11 UTC.
  * The file name can start with any valid character.
  * The file must be uploaded to the bucket `travel-maps`.
  * If the upload is successful, the user is redirected to `http://www.example.com/success_notification.html`.
  * The form allows only images to be uploaded.
  * A user cannot upload a file larger than 1 MB.



## Credential scope

The credential scope is a string that appears in both string-to-signs and policy documents. The credential scope has the following structure:
    
    
    DATE/LOCATION/SERVICE/REQUEST_TYPE

The credential scope has the following components:

  * DATE: The date the signature becomes usable, formatted as YYYYMMDD.
  * LOCATION: For Cloud Storage resources, you can use any value for LOCATION. The recommended value to use is the [location](https://docs.cloud.google.com/storage/docs/locations) associated with the resource that the signature applies to. For example, `us-central1`. This parameter exists to maintain compatibility with Amazon S3.
  * SERVICE: The service name. In most cases when accessing Cloud Storage resources, this value is `storage`. When using Amazon S3 `x-amz` extensions, this value is `s3`.
  * REQUEST_TYPE: The request type. In most cases when accessing Cloud Storage resources, this value is `goog4_request`. When using Amazon S3 `x-amz` extensions, this value is `aws4_request`.



For example, a typical credential scope looks like:
    
    
    20191102/us-central1/storage/goog4_request

While a credential scope when using a string-to-sign with `x-amz` extensions looks like:
    
    
    20150830/us-east1/s3/aws4_request

## Signing

To create a signature, you use a _signing algorithm_ , also known as a cryptographic hash function, to sign your string-to-sign or policy document. The signing algorithm produces a _message digest_ , which must be hex-encoded to create the final signature. The signing algorithm that you use depends on the type of authentication key you have:

Authentication key | Signing algorithm | Signing key  
---|---|---  
[RSA key](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types) | [RSA-SHA256](https://datatracker.ietf.org/doc/html/rfc8332.html) | Directly use RSA [private key](https://docs.cloud.google.com/iam/docs/keys-create-delete)  
[HMAC key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) | [HMAC-SHA256](https://datatracker.ietf.org/doc/html/rfc4868) | Derive from HMAC key's secret  
  
The RSA-SHA256 signing algorithm can be [run using the IAM `signBlob` method](https://docs.cloud.google.com/storage/docs/authentication/creating-signatures). Tools such as the gcloud CLI and most Google Cloud client libraries [let you create signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers) using the `signBlob` method.

You can also create RSA key signatures locally using a programming language that has a library for performing RSA signatures, such as the [pyopenssl library](https://pyopenssl.org/en/stable/); however, this method is [discouraged](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys), because it requires you to create and download the private key of a service account.

#### Derive the signing key from the HMAC key

When signing with an HMAC key, you must create a UTF-8 encoded signing key that is derived from your HMAC key secret. The derived key is specific to the date, location, service, and request type associated with your request. The following pseudocode shows how to derive the signing key:
    
    
    key_date = HMAC-SHA256("PREFIX" + HMAC_KEY_SECRET, "DATE")
    key_region = HMAC-SHA256(key_date, "LOCATION")
    key_service = HMAC-SHA256(key_region, "SERVICE")
    signing_key = HMAC-SHA256(key_service, "REQUEST_TYPE")

The pseudocode has the following components:

  * PREFIX: In most cases when accessing Cloud Storage resources, this value is `GOOG4`. When using Amazon S3 `x-amz` extensions, this value is `AWS4`.
  * HMAC_KEY_SECRET: The secret for the HMAC key that you are using to make and sign the request.
  * DATE, LOCATION, SERVICE, REQUEST_TYPE: These values must match the values specified in the credential scope.



Once you've derived the signing key, you create the signature locally using a programming language that includes a library with the HMAC-SHA256 signing algorithm.

### After signing

To complete the signature, the output of the signing, called the _message digest_ must be hex-encoded.

### Example

The following is pseudocode for signing a policy document:
    
    
    EncodedPolicy = Base64Encode(PolicyDocument)
    MessageDigest = SigningAlgorithm(SigningKey, EncodedPolicy)
    Signature = HexEncode(MessageDigest)
    

The following is pseudocode for signing a string-to-sign:
    
    
    MessageDigest = SigningAlgorithm(SigningKey, StringToSign)
    Signature = HexEncode(MessageDigest)
    

## What's next

  * Use your signature in a [signed URL](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually).
  * Use your signature in a [request with an `Authorization` header](https://docs.cloud.google.com/storage/docs/aws-simple-migration).
  * Use your signature in an [HTML form](https://docs.cloud.google.com/storage/docs/xml-api/post-object-forms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
