---
url: https://docs.cloud.google.com/storage/docs/access-control/signed-urls-v2/
title: V2 Signing Process \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:36.640516+00:00
---

# V2 Signing Process  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/signed-urls-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)



Send feedback 

#  V2 Signing Process Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This page covers legacy material related to the V2 signing process. We recommend that you work with the [V4 signing process](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) instead.

This page provides an overview of signed URLs when working with the V2 signing process, which is a mechanism for query string authentication for buckets and objects. Signed URLs provide a way to give time-limited read or write access to anyone in possession of the URL, regardless of whether they have a user account.

**Important:** Signed URLs can only be used to access resources in Cloud Storage through [XML API endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints).

## Components of the string that requires signing

When creating a signed URL using a program, your program constructs a string that will be signed. This string should be defined in your program as:
    
    
    StringToSign = HTTP_Verb + "\n" +
                   Content_MD5 + "\n" +
                   Content_Type + "\n" +
                   Expires + "\n" +
                   Canonicalized_Extension_Headers +
                   Canonicalized_Resource
    

The components that make up this structure are described in the following table:

String Component | Example | Description  
---|---|---  
`HTTP_Verb` | `GET` | _Required_. The [HTTP verb](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) to be used with the signed URL. **Note:** The HTTP verb `POST` is not supported in signed URL strings, except as noted above. You can use POST to define signed policy documents, which specify the characteristics of objects that can be uploaded to a bucket. Learn more in the [POST Object](https://docs.cloud.google.com/storage/docs/xml-api/post-object) documentation.  
`Content_MD5` | `rmYdCNHKFXam78uCt7xQLw==` | _Optional_. The [MD5 digest value](https://docs.cloud.google.com/storage/docs/metadata#md5) in Base64. If you provide this in the string, the client (usually a browser) must provide this HTTP header with this same value in its request.  
`Content_Type` | `text/plain` | _As needed_. If you provide a [content-type](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5), the client (browser) must provide this HTTP header set to the same value.  
`Expires` | `1388534400` | _Required_. This is the timestamp (represented as the number of seconds since the Unix Epoch of 00:00:00 UTC on January 1, 1970) when the signature expires. The server rejects any requests received after this timestamp, as well as any requests received after the key used to generate the signed URL is rotated. For security and for compatibility with the V4 signing process, you should set `Expires` to correspond to at most 1 week (604800 seconds) in the future.  
`Canonicalized_Extension_Headers` | `x-goog-acl:public-read\nx-goog-meta-foo:bar,baz\n` | _As needed_. The server checks to make sure that the client provides matching values in requests using the signed URL. For information about how to create canonical headers for signing, see Canonical extension headers.  
`Canonicalized_Resource` | `/bucket/objectname` | _Required_. The resource being addressed in the URL. For more details, see Canonical resources.  
**Note:** Query String Parameters like `response-content-disposition` and `response-content-type` are not verified by the signature. To force a `Content-Disposition` or `Content-Type` in the response, [set those parameters in the object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#edit).

## Signing strings with the App Engine App Identity service

When creating a signed URL using a program, you can either sign the string from within your program, or else from within a App Engine application using the App Engine Identity service, which uses App Engine's service account credentials. For example, using the [Python App Identity API](https://docs.cloud.google.com/appengine/docs/python/appidentity), you can:

  * Use `google.appengine.api.app_identity.sign_blob()` to sign the bytes from your constructed string, providing the `Signature` you need when assembling the signed URL.

  * Use `google.appengine.api.app_identity.get_service_account_name()` to retrieve a service account name, which is the `GoogleAccessId` you need when assembling the signed URL.




For support in other languages, see [App Identity API for Java Overview](https://docs.cloud.google.com/appengine/docs/standard/services/appidentity?tab=java), [App Identity API for PHP Overview](https://docs.cloud.google.com/appengine/docs/standard/services/appidentity?tab=php), and [App Identity Go Functions](https://docs.cloud.google.com/appengine/docs/standard/services/appidentity?tab=go).

The App Identity service rotates the private keys when it signs blobs. Signed URLs generated from the App Identity service are good for at least one hour, and are best used for short-lived access to resources.

## Canonical extension headers

When creating a signed URL using a program, you construct the Canonical Extension Headers portion of the message by concatenating all extension (custom) headers that begin with `x-goog-`. However, you cannot perform a simple concatenation. Keep the following algorithm in mind as you create the headers:

  1. Make all custom header names lowercase.

  2. Sort all custom headers by header name using a lexicographical sort by code point value.

  3. If present, remove the `x-goog-encryption-key` and `x-goog-encryption-key-sha256` headers. These headers contain sensitive information that must not be included in the string-to-sign; however, these headers must still be used in any requests that use the generated signed URL.

  4. Eliminate duplicate header names by creating one header name with a comma-separated list of values. Be sure there is no whitespace between the values, and be sure that the order of the comma-separated list matches the order that the headers appear in your request. For more information, see [RFC 7230 section 3.2](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2).

  5. Replace any folding whitespace or newlines (CRLF or LF) with a single space. For more information about folding whitespace, see [RFC 7230, section 3.2.4.](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.4).

  6. Remove any whitespace around the colon that appears after the header name.

  7. Append a newline "\n" (U+000A) to each custom header.

  8. Concatenate all custom headers.


**Important:** You must use both the header name and the header value when you construct the Canonical Extension Headers portion of the query string. Be sure to remove any whitespace around the colon that separates the header name and value. For example, using the custom header `x-goog-acl: private` without removing the space after the colon returns a `403 Forbidden` error, because the request signature you calculate does not match the signature Cloud Storage calculates.

## Canonical resources

When creating a signed URL using a program, you construct the Canonicalized Resource portion of the message by concatenating the resource path (bucket and object and subresource) that the request is acting on. Keep the following in mind as you create the resource:

  * The canonical resource is everything that follows the host name. For example, if the Cloud Storage URL is `https://storage.googleapis.com/example-bucket/cat-pics/tabby.jpeg`, then the canonical resource is `/example-bucket/cat-pics/tabby.jpeg`.

  * If the request is scoped to a subresource, such as `?cors`, add this subresource, including the question mark, to the end of the string.

  * Be sure to copy the HTTP request path literally: that is, you should include all URL encoding (percent signs) in the string that you create. Also, be sure that you include only query string parameters that designate subresources (such as `cors`). You should not include query string parameters such as `?prefix`, `?max-keys`, `?marker`, and `?delimiter`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
