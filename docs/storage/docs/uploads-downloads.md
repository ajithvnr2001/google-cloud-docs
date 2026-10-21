---
url: https://docs.cloud.google.com/storage/docs/uploads-downloads/
title: Object uploads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:02:50.487658+00:00
---

# Object uploads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/uploads-downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Object uploads Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses concepts related to uploading objects. You can upload and store any MIME type of data up to 5 TiB in size.

## Upload types

You can send upload requests to Cloud Storage in the following ways:

  * **Single-request upload**. An upload method where an object is uploaded as a single request. Use this if the file is small enough to upload in its entirety if the connection fails. See [Upload object from file](https://docs.cloud.google.com/storage/docs/uploading-objects) or [Upload object from memory](https://docs.cloud.google.com/storage/docs/uploading-objects-from-memory) for guides to single-request uploads.

    * [**JSON API multipart upload**](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert). An upload method that lets you upload both object data and its metadata in a single request. The XML API, however, allows setting object metadata in all types of uploads.
**Note:** JSON API multipart uploads are an implementation detail when you use high-level libraries to construct HTTP requests.
  * [**Resumable upload**](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads). An upload method that provides a more reliable transfer, which is especially important with large files. Resumable uploads are a good choice for most applications, since they also work for small files at the cost of one additional HTTP request per upload. You can also use resumable uploads to perform streaming transfers, which lets you upload an object of unknown size.

  * [**XML API multipart upload**](https://docs.cloud.google.com/storage/docs/multipart-uploads). An upload method that is compatible with Amazon S3 multipart uploads. Files are uploaded in parts and assembled into a single object with the final request. XML API multipart uploads allow you to upload the parts in parallel, potentially reducing the time to complete the overall upload.




Using these basic upload types, more advanced upload strategies are possible:

  * [**Parallel composite upload**](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads). An upload strategy in which you chunk a file and upload the chunks in parallel. Unlike XML API multipart uploads, parallel composite uploads use the compose operation, and the final object is stored as a composite object.

  * [**Streaming upload**](https://docs.cloud.google.com/storage/docs/streaming-uploads). An upload method that lets you upload data without requiring that the data first be saved to a file, which is useful when you don't know the total size of the upload at the start of the upload.

  * **Chunked transfer encoding upload**. A single-request upload that includes the header `Transfer-Encoding: chunked`, allowing the upload to be sent in multiple, sequential chunks of data.


**Note:** If you upload a file with the same name as an existing object in your Cloud Storage bucket, the existing object is overwritten. To keep earlier versions of the object, [enable Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning).

## Upload size considerations

When choosing whether to use a single-request upload instead of a resumable upload or XML API multipart upload, consider the amount of time that you're willing to lose should a network failure occur and you need to restart the upload from the beginning. For faster connections, your cutoff size can typically be larger.

For example, say you're willing to tolerate 30 seconds of lost time:

  * If you upload from a local system with an average upload speed of 8 Mbps, you can use single-request uploads for files as large as 30 MB.

  * If you upload from an in-region service that averages 500 Mbps for its upload speed, the cutoff size for files is almost 2 GB.




## Support per tool

### Console

You can perform the following types of uploads when using the Google Cloud console:

  * [Single-request uploads](https://docs.cloud.google.com/storage/docs/uploading-objects), with [resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior) automatically managed on your behalf



### Command line

You can perform the following types of uploads when using the Google Cloud CLI:

  * [Single-request uploads](https://docs.cloud.google.com/storage/docs/uploading-objects), with [resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior) automatically managed on your behalf
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)
  * [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads#behavior)



### Client libraries

### C++

You can perform the following types of uploads when using the C++ client library:

  * [Single-request and resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)
  * [Parallel composite uploads](https://googleapis.dev/cpp/google-cloud-storage/latest/namespacegoogle_1_1cloud_1_1storage.html#a7d0262bd98e8d193841fda3c97567ec9)



### C#

You can perform the following types of uploads when using the C# client library:

  * [Single-request and resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)



### Go

You can perform the following types of uploads when using the Go client library:

  * Single-request and resumable uploads, [depending on file size](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)



### Java

You can perform the following types of uploads when using the Java client library:

  * [Single-request and resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)
  * [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads#behavior)



### Node.js

You can perform the following types of uploads when using the Node.js client library:

  * [Single-request and resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)
  * [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads)



### PHP

You can perform the following types of uploads when using the PHP client library:

  * [Single-request and resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)



### Python

You can perform the following types of uploads when using the Python client library:

  * Single-request and resumable uploads, [depending on file size](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)
  * [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads)



### Ruby

You can perform the following types of uploads when using the Ruby client library:

  * [Resumable uploads](https://docs.cloud.google.com/storage/docs/resumable-uploads#behavior)



### Terraform

You can perform [single-request uploads](https://docs.cloud.google.com/storage/docs/uploading-objects) when using Terraform. Resumable uploads occur automatically when the file being uploaded is larger than 16 MiB.

### REST APIs

### JSON API

You can perform the following types of uploads when using the JSON API:

  * [Single-request uploads](https://docs.cloud.google.com/storage/docs/uploading-objects)
  * [Resumable uploads](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads)
  * [Chunked transfer encoding uploads](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#transferencoding)
  * [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)



### XML API

You can perform the following types of uploads when using the XML API:

  * [Single-request uploads](https://docs.cloud.google.com/storage/docs/uploading-objects)
  * [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads)
  * [Resumable uploads](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads)
  * [Chunked transfer encoding uploads](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#chunked)
  * [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads#behavior)
  * [Streaming uploads](https://docs.cloud.google.com/storage/docs/streaming-uploads)



If you use REST APIs to upload objects, see [Request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) for a complete discussion on the request endpoints you can use.

## What's next

  * [Learn how to supply checksums in upload requests](https://docs.cloud.google.com/storage/docs/data-validation).
  * [Make your data publicly accessible](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).
  * [View and edit your object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata).
  * Learn how to [transfer data to Cloud Storage using Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).
  * [Transfer objects from your Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/transfer-files#gcstransfer).
  * Learn about [object downloads](https://docs.cloud.google.com/storage/docs/reads-and-downloads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
