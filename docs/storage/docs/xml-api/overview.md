---
url: https://docs.cloud.google.com/storage/docs/xml-api/overview/
title: XML API overview \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:42.668695+00:00
---

# XML API overview  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  XML API overview Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an overview of the Cloud Storage XML API and is intended for software developers. It assumes that you are familiar with RESTful services and web programming and that you are comfortable creating applications that operate through HTTP requests. If this does not describe you, consider one of the following alternatives:

  * If you are just starting out with Cloud Storage, you should first try either the [Google Cloud console Quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-console) or the [Google Cloud CLI Quickstart](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud). These tutorials demonstrate the basics of using Cloud Storage without the need to use the API directly.

  * If you work in certain programming languages, you can use the [Cloud Storage Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries).

  * If you are a mobile or web app developer, you can use the [Firebase SDKs](https://firebase.google.com/docs/storage/) for Cloud Storage.

  * If you are not a software developer and want to store your personal data in the cloud and share it with others, you can use [Google Drive](https://www.google.com/drive/).




## Overview

The Cloud Storage XML API is a RESTful interface that lets you manage Cloud Storage data in a programmatic way. As a RESTful API, it relies on _method information_ and _scoping information_ to define the operations to perform:

  * **Method information**

You specify the method information with standard HTTP methods, such as `DELETE`, `GET`, `HEAD`, `POST`, and `PUT`.

  * **Scoping information**

You specify the scoping information with a [publicly-accessible endpoint](https://docs.cloud.google.com/storage/docs/request-endpoints) (URI) and various scoping parameters. For the XML API, the primary scoping parameters are the bucket and object names. You can further scope your operations by using [HTTP headers and query string parameters](https://docs.cloud.google.com/storage/docs/reference-headers).




You use HTTP methods to perform operations on the resource you specify in the scope. For a list of operations available in the XML API, see [XML API Request Methods](https://docs.cloud.google.com/storage/docs/xml-api/reference-methods). Key capabilities include:

  * Standard object operations such as `PUT`, `GET`, `HEAD`, `POST`, and `DELETE`.
  * Bucket management.
  * Access Control List (ACL) management.



Access to Cloud Storage through the XML API is useful when you are using tools and libraries that must work across different storage providers, or when you are migrating from another storage provider to Cloud Storage. In the latter case, you only need to make a few simple changes to your existing tools and libraries to begin sending requests to Cloud Storage. For more information about migrating to Cloud Storage, see [Simple migration from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/aws-simple-migration).

## Requests

**Note:** We recommend that you use HTTPS when reading or writing data to Cloud Storage so that your data is encrypted during transfer. Cloud Storage automatically encrypts your data before it is written to disk. For more information, see [Encryption](https://docs.cloud.google.com/storage/docs/encryption).

The Cloud Storage XML API provides a web interface for making HTTP requests and handling HTTP responses. The API is compatible with HTTP/1.1, HTTP/2, and HTTP/3 protocols. Each request implements a standard HTTP method. Along with these methods, you can use various HTTP request headers.

### Authentication

All requests to Cloud Storage must be authenticated, with the exception of requests made to anonymously accessible objects or buckets. Requests are typically authenticated using the [`Authorization` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#authorization).

### Endpoints

**Important:** If you intend to serve content through a browser, note that the XML API serves content from the same origin as the request endpoint. If you need to serve content from a unique origin, consider using the JSON API or [Authenticated browser downloads](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth).

Most Cloud Storage XML API requests use the following URI for accessing buckets and objects:
    
    
    storage.googleapis.com

You can scope this further by adding a bucket and object to the URI. The resulting URL can take two forms:
    
    
    BUCKET_NAME.storage.googleapis.com/OBJECT_NAME
    storage.googleapis.com/BUCKET_NAME/OBJECT_NAME

You can use the Cloud Storage URI with unsecured requests (HTTP) and secured requests (HTTPS) that use secure sockets layer (SSL) encryption.

For additional endpoints, such as dedicated upload and download endpoints for the XML API, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints).

### Headers and query string parameters

The Cloud Storage XML API supports HTTP request headers. It also supports several extension (custom) request headers, which have an `x-goog-` prefix. Request header requirements vary depending on the kind of request you're making. Some frequently used request headers include:

Request Header | Description | Usage  
---|---|---  
`Authorization` | The authentication string for requests. | Required for all authenticated requests.  
`Content-Length` | The size of the request body (excluding headers) in bytes. | Required for all PUT and POST requests, except chunked transfers.  
`Content-Type` | The MIME type of the request body, such as `application/xml` or `text/html`. | Recommended for requests that contain an entity body.  
`Date` | The date and time of the request. | Required for all requests, except for [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls), which can use `x-goog-date` instead.  
`Host` | The URI for the request. | Required for all requests.  
`x-goog-project-id` | The ID of the project you want to use. | Required for creating buckets or listing buckets except when you are using the XML API for interoperability, such as for compatibility with Amazon S3. For more information, see [Simple migration from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/aws-simple-migration).  
  
The Cloud Storage XML API also supports a variety of query string parameters, which you can use to scope your requests. Append query string parameters to the HTTP path portion of the request with the following syntax:
    
    
    PATH_TO_OBJECT/?PARAMETER=VALUE&PARAMETER=VALUE...

For a complete list of XML API headers and query string parameters, see [HTTP headers and query string parameters](https://docs.cloud.google.com/storage/docs/reference-headers).

### Example request

A typical authenticated Cloud Storage request is shown in the following example. This request [retrieves a list of objects](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list) that are stored in a bucket named `travel-maps`. The request limits the list of objects to only those objects that have the prefix `/europe/france`.
    
    
    GET /?list-type=2&prefix=/europe/france/ HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Wed, 17 Feb 2010 15:31:56 -0800
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

## Responses

The Cloud Storage XML API returns standard HTTP response headers and several extension (custom) response headers. The response headers vary according to the operation you perform. Some frequently used response headers include:

Response Header | Description  
---|---  
`Cache-Control` | The cache control setting for the response.  
`Content-Length` | The size of the response body (excluding headers) in bytes.  
`Content-Type` | The MIME type of the response body, such as `application/xml` or `text/html`.  
`Date` | The date and time of the response.  
`ETag` | An [HTTP 1.1 entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3), which you can use to determine whether an object has changed.  
  
Responses can also include a status code. Cloud Storage uses standard HTTP status codes. An error response includes an XML document in the response body, which contains information about the error conditions. For a list of status codes used by the XML API, see [HTTP Status and Error Codes](https://docs.cloud.google.com/storage/docs/reference-status).

A typical Cloud Storage response is shown in the following example. This example is a response to a request for [listing a bucket's contents](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list). The bucket name is `travel-maps` and the request is scoped so that only objects with the prefix `/europe/france/` are returned in the list.
    
    
    HTTP/1.1 200 OK
    Content-Length: 4061
    Content-Type: application/xml
    Date: Wed, 17 Feb 2010 23:31:57 GMT
    Cache-Control: private, max-age=0
    
    <?xml version='1.0' encoding='utf-8'?>
    <ListBucketResult xmlns='http://doc.storage.googleapis.com/2010-03-01'>
      <Name>travel-maps</Name>
      <Prefix>/europe/france/</Prefix>
      <StartAfter></StartAfter>
      <IsTruncated>false</IsTruncated>
      <Contents>
        <Key>europe/france/cannes.jpg</Key>
        <LastModified>2010-02-17T22:11:12.487Z</LastModified>
        <ETag>"53fc311c15eda0a031809982ccf92aac"</ETag>
        <Size>5061631</Size>
        <StorageClass>STANDARD</StorageClass>
      </Contents>
      <Contents>
        <Key>europe/france/paris.jpg</Key>
        <LastModified>2010-02-17T22:09:57.457Z</LastModified>
        <ETag>"53fc311c15eda0a031809982ccf92aac"</ETag>
        <Size>5061631</Size>
        <StorageClass>STANDARD</StorageClass>
      </Contents>
    </ListBucketResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
