---
url: https://docs.cloud.google.com/storage/docs/reads-and-downloads/
title: Object reads and downloads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:22.418592+00:00
---

# Object reads and downloads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/reads-and-downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Object reads and downloads Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses concepts related to reading and downloading objects in Cloud Storage.

## Reading objects

Reading an object refers to streaming, consuming, or inspecting object data or a specific byte range over an open network connection directly in memory. Rather than being saved locally, the retrieved payload is ephemeral and lives in an application memory stream, buffer, pipeline, or directly in CPU/GPU memory. Reading objects is suitable for high-performance, throughput-intensive workloads, such as streaming training datasets and tensor batches into Artificial Intelligence (AI) and Machine Learning (ML) frameworks like Pytorch or Jax.

The following list describes the types of object reads available in Cloud Storage:

  * [Reading objects into memory or interactive object reads](https://docs.cloud.google.com/storage/docs/reading-objects): A method where data is consumed interactively or into memory. The client retrieves the entire object and loads all of its bytes into a contiguous variable, byte array, or in-memory string.

  * [Streaming reads](https://docs.cloud.google.com/storage/docs/streaming-reads): A method where data is consumed as a stream of bytes directly as it's being received from the network, rather than waiting for the entire transfer to finish.




## Downloading objects

Downloading an object is an end-to-end task that transfers object data from Cloud Storage into a persistent file on a local file system, disk, or target storage device. Unlike in-memory streaming reads, downloading encompasses both fetching the remote bytes and committing them to local storage. Downloading objects is primarily suited for general-purpose file management, local archiving, data backup, and offline utility usage.

When using REST APIs, downloads are performed using HTTP or HTTPS `GET` requests that can include an optional `Range` header, which defines a specific portion of the object to download to persistent or local storage. You can also use the `Range` header to resume interrupted downloads. When using gRPC, downloads use `storage.v2.Storage/ReadObject` or `BidiReadObject` streams.

The following list describes the types of object downloads available in Cloud Storage:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects): The most basic form of object downloading. The client sends a single request to retrieve either the entire object or a specified byte range in one continuous transfer.

  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads): A high-performance strategy where a single large object is divided into multiple smaller "slices" (also known as "chunks"). The client downloads these slices in parallel using multiple independent and concurrent requests, then reassembles the slices locally into a single file.




## Tool support for reading and downloading objects

### Console

When using the Google Cloud console, you can perform the following object reads and downloads:

  * [Interactive object reads](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects), typically [authenticated browser downloads](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth)



### Command line

You can perform the following object reads and downloads when using the Google Cloud CLI:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)
  * [Interactive object reads](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### Client libraries

### C++

You can perform the following types of reads and downloads when using the C++ client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### C#

You can perform the following types of reads and downloads when using the C# client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### Go

You can perform the following types of reads and downloads when using the Go client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### Java

You can perform the following types of reads and downloads when using the Java client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### Node.js

You can perform the following types of reads and downloads when using the Node.js client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### PHP

You can perform the following types of reads and downloads when using the PHP client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### Python

You can perform the following types of reads and downloads when using the Python client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### Ruby

You can perform the following types of reads and downloads when using the Ruby client library:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)



### REST APIs

If you use REST APIs to download objects, see [Request endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) for a complete discussion on the request endpoints you can use.

### JSON API

You can perform the following types of downloads when using the JSON API:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



### XML API

You can perform the following types of downloads when using the XML API:

  * [Simple downloads](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)
  * [Reading objects into memory](https://docs.cloud.google.com/storage/docs/reading-objects)
  * [Streamed object reads](https://docs.cloud.google.com/storage/docs/streaming-reads)



## What's next

  * [Make your data publicly accessible](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).
  * [Learn how checksums are used for object downloads](https://docs.cloud.google.com/storage/docs/data-validation).
  * Learn about [object uploads](https://docs.cloud.google.com/storage/docs/uploads).
  * [View and edit your object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata).
  * Learn how to [transfer data to Cloud Storage using Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).
  * [Transfer objects from your Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/transfer-files#gcstransfer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
