---
url: https://docs.cloud.google.com/storage/docs/data-validation/
title: Data validation and change detection with checksums \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:40.289245+00:00
---

# Data validation and change detection with checksums  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/data-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Data validation and change detection with checksums Stay organized with collections  Save and categorize content based on your preferences. 

To validate data integrity and detect changes, Cloud Storage encourages you to use checksums when transferring data to and from your buckets. This page provides information about how checksums are used within Cloud Storage and how to specify checksums when sending requests.

## Prevent data corruption by using checksums

Data can sometimes get corrupted while being transferred to or from the cloud because of software or hardware bugs, memory or router errors, electrical disturbances, or changes to the source data during extended period file uploads.

To help protect you against data corruption, Cloud Storage supports the use of [CRC32C and MD5 checksums](https://docs.cloud.google.com/storage/docs/metadata#checksums) for verifying the integrity of your data and detecting changes in your data.

CRC32C is the recommended validation method for performing integrity checks. Validation using MD5 hashes is supported for single-file uploads but [isn't supported for objects that are uploaded in chunks](https://docs.cloud.google.com/storage/docs/metadata#md5), such as composite objects and objects uploaded using an XML API multipart upload.

## Checksums for data writes

For object writes, the client calculates the checksum of the local file and attaches it to the HTTP headers of the object upload request. The server receives the data payload, calculates its own checksum, and validates the data by comparing both checksums after the upload completes. If the checksums match, the object is stored in Cloud Storage along with its checksums. If the checksums don't match, the write request is rejected with a `BadRequestException: 400` error.

### Server-side validation for data writes

Cloud Storage performs server-side validation in the following cases:

  * When you supply an object's MD5 or CRC32C hash in an object upload request. To learn about types of object uploads, see [Object uploads](https://docs.cloud.google.com/storage/docs/uploads).

  * When you perform a copy or rewrite request within Cloud Storage. For object copy and rewrite requests, Cloud Storage automatically performs server-side validation based on a [non-editable checksum](https://docs.cloud.google.com/storage/docs/metadata#checksums) stored with the source object.




#### JSON API single-request (media) uploads

For JSON API media uploads, you can specify checksums in the `X-Goog-Hash` header of the request. For example:
    
    
    curl -X POST --data-binary @Desktop/dog-pic.jpeg \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: image/jpeg" \
        -H "X-Goog-Hash: crc32c=n03x6A==" \
        "https://storage.googleapis.com/upload/storage/v1/b/my-bucket/o?uploadType=media&name=dog-pic.jpeg"

#### JSON API multipart uploads

For JSON API multipart uploads, you can specify checksums as part of the request container, either in the object metadata section or under a third boundary string. For details on the JSON structure and valid keys of an object, see the [Objects resource representation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects).

The following example specifies a CRC32C checksum in the object metadata portion of a request container:
    
    
    --separator_string
    Content-Type: application/json; charset=UTF-8
    
    {
    "name":"my-document.txt",
    "crc32c": "n03x6A=="
    }
    
    --separator_string
    Content-Type: text/plain
    
    This is a text file.
    --separator_string--
    

The following example specifies a CRC32C checksum in the third boundary string of a request container:
    
    
    --separator_string
    Content-Type: application/json; charset=UTF-8
    
    {
    "name":"my-document.txt"
    }
    
    --separator_string
    Content-Type: text/plain
    
    This is a text file.
    
    --separator_string
    Content-Type: application/json; charset=UTF-8
    
    { "crc32c": "n03x6A==" }
    --separator_string--
    

#### JSON API resumable uploads

For JSON API resumable uploads, you can specify checksums in the `X-Goog-Hash` header of the final request that completes the upload. For example:
    
    
    curl -i -X PUT --data-binary @Desktop/dog-pic.jpeg \
          -H "Content-Length: 2000000" \
          -H "X-Goog-Hash: crc32c=n03x6A==" \
          "SESSION_URI"

The checksum specified in the final request is calculated from the whole object, not just the object data in the final request.

#### XML API single-request uploads

For XML API single-request uploads, you can specify checksums in the [`x-goog-hash` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooghash) of the request.

For example:
    
    
    curl -X PUT --data-binary @Desktop/dog-pic.jpeg \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: image/jpeg" \
        -H "x-goog-hash: crc32c=n03x6A==" \
        "https://storage.googleapis.com/my-bucket/dog-pic.jpeg"

XML API single-request uploads also accept the standard HTTP [Content-MD5 header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentmd5). For details, refer to the [Content-MD5 specification](https://datatracker.ietf.org/doc/html/rfc1864#section-2).

#### XML API multipart uploads

For XML API multipart uploads, you can specify a checksum for each individual upload part. To specify an individual checksum for an upload part, include the [`x-goog-hash` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooghash) in the request for that specific part.

For example:
    
    
    PUT /dog-pic.jpeg?partNumber=1&uploadId=ABgVH8 HTTP/1.1
    Host: my-bucket.storage.googleapis.com
    Content-Length: 1000000
    x-goog-hash: crc32c=n03x6A==

Only CRC32C checksums can be used to verify the integrity of XML API multipart uploads. MD5 checksums aren't supported.

#### gRPC uploads

When uploading objects using [gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api), you can specify object-level checksums in the first or last `WriteObject` message of any upload request, whether it's a single-shot upload or a resumable upload.

Additionally, gRPC supports per-message checksums. Each `WriteObject` message contains data chunks of up to 2 MiB, and each chunk can include its own checksum. You can specify per-message checksums in place of or alongside an object-level checksum.

#### Parallel composite uploads

In the case of [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads), you should perform an integrity check for each component upload and then use [preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) with the upload compose request to protect against race conditions. Compose requests don't get server-side validation, so you should perform client-side validation on the new composite object if you want an end-to-end integrity check.

#### Google Cloud CLI copies and rewrites

In the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage), data copied to or from a Cloud Storage bucket gets automatically validated. For `cp`, `mv`, and `rsync` commands, the gcloud CLI uses MD5 or CRC32C checksums to determine if there is a difference between the version of an object found at the source and the version found at the destination. If the checksum of the source data doesn't match the checksum of the destination data, the gcloud CLI deletes the invalid copy and prints a warning message. This very rarely happens. If it does, you should retry the operation.

This automatic validation occurs after the object is finalized and invalid objects are visible for 1-3 seconds before they're identified and deleted. Additionally, the gcloud CLI might be interrupted after the upload completes but before it performs the validation, leaving the invalid object in place. These issues can be avoided when uploading single files to Cloud Storage by using server-side validation, which occurs when you use the `--content-md5` flag to specify an MD5 hash.

The Google Cloud CLI ignores the `--content-md5` flag for objects that don't have an MD5 hash.

#### Change detection for `rsync`

The [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync) command compares checksums in the following scenarios to determine whether to skip a transfer:

  * The source and destination are both Cloud Storage buckets and the object has an MD5 or CRC32C checksum in both buckets.

  * The object does not have a file modification time (`mtime`) in either the source or destination.




In cases where an object has an `mtime` value in both the source and destination, such as when the source and destination are file systems, the `rsync` command compares the objects' size and `mtime` value instead of using checksums. Similarly, if the source is a bucket and the destination is a local file system, the `rsync` command uses the time created for the source object as a substitute for `mtime`, and the command does not use checksums.

If neither `mtime` nor checksums are available, `rsync` only compares file sizes when determining if there is a change between the source version of an object and the destination version. For example, neither `mtime` nor checksums are available when comparing [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects) with objects at a cloud provider that doesn't support CRC32C, because composite objects don't have MD5 checksums.

### Client-side validation for data writes

You can perform client-side validation of your uploads by issuing a request for the uploaded object's metadata, comparing the uploaded object's hash value to the expected value, and deleting the object in case of a mismatch. This method is useful if the object's MD5 or CRC32C hash isn't known at the start of the upload.

The following table contains the minimum version of each Cloud Storage client that supports object write checksums.

Client | Version that supports object write checksums  
---|---  
[Cloud Storage C++ client library](https://docs.cloud.google.com/cpp/docs/reference/storage/latest) | 2.46 and later  
[Cloud Storage Go client library](https://godoc.org/cloud.google.com/go/storage) | 1.60.0 and later  
[Cloud Storage Java client library](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview) | 2.62 and later  
[Cloud Storage Node.js client library](https://googleapis.dev/nodejs/storage/latest/) | 7.19.0 and later  
[Cloud Storage PHP client library](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.122.0/storage/storageclient) | 1.51.0 and later  
[Cloud Storage Python client library](https://docs.cloud.google.com/python/docs/reference/storage/latest) | 3.7.0 and later  
[Cloud Storage Ruby client library](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest) | 1.60.0  
[Cloud Storage .NET client library](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest) | 2.3.0 and later. We recommend 4.15.0, which provides server-side checksum validation.  
[Cloud Storage connector](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage) | 

  * 3.0.18 and later for the 3.0.x Cloud Storage connector
  * 3.1.14 and later for the 3.1.x Cloud Storage connector
  * 4.0.3 and later for the 4.0.x Cloud Storage connector 

  
[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) | 3.8.0 and later  
[Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage) | **Note:** The Google Cloud CLI performs object integrity validation only after the object upload is complete.  
  
## Checksums for data reads and downloads

For object reads and downloads, the server sends the object along with its stored checksum in the response. The client calculates its own checksum of the file that was read or downloaded based on the bytes it received and compares the two checksums to verify data integrity.

### Client-side validation for reads and downloads

By default, all Cloud Storage client library SDKs support calculating checksums for object downloads and reads. The following table contains information on how to disable object download or read checksums for each client library SDK.

Client library | Instructions on disabling object read or download checksums  
---|---  
[Cloud Storage C++ client library](https://docs.cloud.google.com/cpp/docs/reference/storage/latest) | In the C++ client library, you disable checksum verification by setting `DownloadChecksumValidationOption` to the value `ChecksumAlgorithm::kNone`.  
[Cloud Storage Go client library](https://godoc.org/cloud.google.com/go/storage) | In the Go client library, you disable checksum verification by providing reader options at initialization. Pass `WithDisableReaderChecksum()` when calling `NewReader` or pass `WithDisableMRDReadChecksum()` when calling `NewMultiRangeDownloader`.  
[Cloud Storage Java client library](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview) | To disable internal CRC32C checksum validation on read paths in the Java client library, pass the JVM system property `-Dcom.google.cloud.storage.Hasher.read=disabled`, which turns off the internal hasher for reads. If you want to disable checksumming globally across both reads and writes, use `-Dcom.google.cloud.storage.Hasher.default=disabled` instead.   
[Cloud Storage Node.js client library](https://googleapis.dev/nodejs/storage/latest/) | In the Node.js client library, you disable checksum validation by passing `{ validation: false }` within the configuration option object provided to download method calls.  
[Cloud Storage PHP client library](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.122.0/storage/storageclient) | In the PHP client library, you disable checksum validation across both JSON and XML API read paths by passing `'validate' => false` or `'validate' => 'none'` inside the associative options array `($options['validate'])` when calling download methods.  
[Cloud Storage Python client library](https://docs.cloud.google.com/python/docs/reference/storage/latest) | In the Python client library, disabling checksum verification depends on the client transport: for the JSON client, pass `checksum=None` (supported in methods such as `download_to_file`), whereas for the gRPC client, set `enable_checksum=False`.  
[Cloud Storage Ruby client library](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest) | In the Ruby client library, you disable checksum verification by passing keyword arguments (`checksum:` or `verify:`) directly to download methods, specifically setting `verify: none` or `verify: false`.  
[Cloud Storage .NET client library](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest) | In the .NET client library, you disable checksum verification by setting the `ChecksumValidation` property to `DownloadValidationMode.Never` on the `DownloadObjectOptions` object passed to download method calls.  
  
### Performing data integrity checks on objects that were downloaded or read

In some cases, your application might need to independently calculate the checksum of the file that was downloaded or read by using the received bytes and compare it against the server-supplied hash to verify data integrity.

To perform an integrity check for downloaded data, calculate the checksum as the data is received and compare your results to the server-supplied checksum.

Server-side checksums are based on the complete object as it's stored in Cloud Storage, which means that the following types of downloads can't be validated against server-supplied checksums:

  * Downloads that undergo [decompressive transcoding](https://docs.cloud.google.com/storage/docs/transcoding): the server-supplied checksum represents the object in its compressed state, while the served data has compression removed and consequently has a different checksum value.

  * A response that contains only a [portion of the object data](https://docs.cloud.google.com/storage/docs/downloading-objects#downloading-an-object-portion): this type of response occurs for `Range` requests.

gRPC ranged reads are an exception to this bullet and support end-to-end validation. In gRPC ranged reads, Cloud Storage validates data by including a unique CRC32C checksum inside every individual response chunk of a stream, which lets you client instantly verify that the specific block of data wasn't corrupted in transit. For broader validation, the stream also provides the entire object's full checksum, which advanced clients can use to calculate a rolling total and verify the integrity of the larger file.

If your application needs to read object ranges instead of full objects at once, we recommend [using gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api). Otherwise, we recommend using ranged requests only for restarting the download of a full object after the last received offset, where you can calculate and validate the checksum after the full download completes.




When validating your download, a mismatch between your calculated checksum and the server-supplied checksum indicates that the data was corrupted in transit. In these cases, you should discard the corrupted data and use the [recommended retry logic](https://docs.cloud.google.com/storage/docs/retry-strategy) to retry the request.

## What's next

  * Learn about [object uploads](https://docs.cloud.google.com/storage/docs/uploads) and [object downloads](https://docs.cloud.google.com/storage/docs/reads-and-downloads) in Cloud Storage.
  * Learn about [retry strategies](https://docs.cloud.google.com/storage/docs/retry-strategy) for Cloud Storage.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
