---
url: https://docs.cloud.google.com/storage/docs/batch/
title: Sending batch requests \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:24.700430+00:00
---

# Sending batch requests  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Sending batch requests Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to batch JSON API calls together to reduce the number of HTTP connections your client has to make when accessing Cloud Storage.

## Overview of batch requests

Each HTTP connection that your client makes results in a certain amount of overhead. The Cloud Storage JSON API supports batching requests, which allows your client to group several API calls into a single HTTP request. Grouping together multiple API calls into a single request lets you reduce network overhead and latency when you need to perform many operations.

Examples of operations you might want to use batch requests for:

  * Updating metadata, such as permissions, on many objects
  * Deleting many objects



Cloud Storage does not support batch operations for uploading or downloading.

## Batch request structure

**Note:** The batch system for the Cloud Storage JSON API uses the same syntax as the [OData batch processing](http://www.odata.org/documentation/odata-version-3-0/batch-processing/) system, but the semantics differ.

A batch request is a single standard HTTP request containing multiple Cloud Storage JSON API calls. The outer batch request uses `multipart/mixed` in the `Content-Type` request header, with a body composed of multiple parts that each contain an individual HTTP sub-request.

The outer batch request is sent to the batch endpoint:
    
    
    https://storage.googleapis.com/batch/storage/v1

Each sub-request inside the batch body specifies a standard Cloud Storage JSON API request path, such as:
    
    
    https://storage.googleapis.com/storage/v1/BUCKET_NAME/o/OBJECT_NAME

To view the format of an example batch request, see Example.

You shouldn't include more than 100 calls in a single batch request to avoid HTTP `400` errors, gateway timeouts, and dropped connections. If you need to make more than 100 calls, use multiple batch requests. The total batch request payload must be less than 10MB. Larger requests are rejected by Cloud Storage.

**Note:** A set of `n` requests batched together counts toward your [usage limit](https://docs.cloud.google.com/storage/quotas) and [operations costs](https://docs.cloud.google.com/storage/pricing#operations-pricing) as `n` requests, not as one request. The batch request is taken apart into a set of `n` requests before processing.

### Batch request format

This section describes the format of a batch request.

Within the body of the outer request, each part begins with its own `Content-Type: application/http` HTTP header. The part can also have an optional `Content-ID` header. These headers mark the beginning of the part, but they're separate from the nested HTTP request. This means that after the server unwraps the batch request into separate requests, the part headers are ignored.

The body of each part is itself a complete HTTP request, with its own verb, URL, headers, and body. These HTTP requests must only contain the path portion of the URL; full URLs can have undefined behavior.

The HTTP headers for the outer batch request, except for the `Content-` headers such as `Content-Type`, apply to every nested request as well. However, if you specify a given HTTP header in both the outer request and a nested request, then the nested request's header value overrides the outer batch request header's value for that specific request.

For example, if you provide an `Authorization` header for a specific nested request, then that header applies only to the request that specified it. If you provide an `Authorization` header for the outer request, then that header applies to all of the nested requests unless they override it with an `Authorization` header of their own.

When Cloud Storage receives the batched request, it applies the outer request's query parameters and headers (as appropriate) to each part and then treats each part as if it were a separate HTTP request.

### Response to a batch request

The Cloud Storage response is a single standard HTTP response with a `multipart/mixed` content type; each part of this main response is the response to one of the requests in the batched request. The order of responses is the same as the requests.

Like all the parts in a request, each response part contains a complete HTTP response, including a status code, headers, and a body. And like the parts in the request, each response part is preceded by a `Content-Type` header that marks the beginning of the part. For more information on status codes, see [HTTP status and error codes for the Cloud Storage JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

If a given part of the request had a `Content-ID` header, then the corresponding part of the response has a matching `Content-ID` header. The `Content-ID` header of the response begins with `response-`, followed by the `Content-ID` value used in the request, as shown in the example.

**Caution:** The server may perform your requests in any order. Do not rely on requests executing in the order you specify them. To ensure that two calls occur in a specific order, send the first one by itself, then wait for the response to the first one before sending the second one.

## Example

The following batch example updates the [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata) for three objects in `example-bucket`.

### Example batch HTTP request

### HTTP
    
    
    POST /batch/storage/v1 HTTP/1.1
    Host: storage.googleapis.com
    Content-Length: 960
    Content-Type: multipart/mixed; boundary="===============7330845974216740156=="
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    
    --===============7330845974216740156==
    Content-Type: application/http
    Content-Transfer-Encoding: binary
    Content-ID: <b29c5de2-0db4-490b-b421-6a51b598bd22+1>
    
    PATCH /storage/v1/b/example-bucket/o/obj1 HTTP/1.1
    Content-Type: application/json
    accept: application/json
    content-length: 31
    
    {"metadata": {"type": "tabby"}}
    --===============7330845974216740156==
    Content-Type: application/http
    Content-Transfer-Encoding: binary
    Content-ID: <b29c5de2-0db4-490b-b421-6a51b598bd22+2>
    
    PATCH /storage/v1/b/example-bucket/o/obj2 HTTP/1.1
    Content-Type: application/json
    accept: application/json
    content-length: 32
    
    {"metadata": {"type": "tuxedo"}}
    --===============7330845974216740156==
    Content-Type: application/http
    Content-Transfer-Encoding: binary
    Content-ID: <b29c5de2-0db4-490b-b421-6a51b598bd22+3>
    
    PATCH /storage/v1/b/example-bucket/o/obj3 HTTP/1.1
    Content-Type: application/json
    accept: application/json
    content-length: 32
    
    {"metadata": {"type": "calico"}}
    --===============7330845974216740156==--
    

### Client libraries

### C++

The C++ client library does not support batched requests.

### C#

The C# client library does not support batched requests.

### Go

The Go client library does not support batched requests.

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://docs.cloud.google.com/storage/docs/reference/libraries).
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageBatch.html);
    import com.google.cloud.storage.[StorageBatchResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageBatchResult.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import java.util.Objects;
    import java.util.stream.Collectors;
    
    public class BatchSetObjectMetadata {
      public static void batchSetObjectMetadata(
          String projectId, String bucketName, String pathPrefix) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The directory prefix. All objects in the bucket with this prefix will have their metadata
        // updated
        // String pathPrefix = "yourPath/";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        Map<String, String> newMetadata = new HashMap<>();
        newMetadata.put("keyToAddOrUpdate", "value");
        Page<Blob> blobs =
            storage.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____)(
                bucketName,
                Storage.BlobListOption.prefix(pathPrefix),
                Storage.BlobListOption.delimiter("/"));
        [StorageBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageBatch.html) batchRequest = storage.[batch](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_batch__)();
    
        // Add all blobs with the given prefix to the batch request
        List<StorageBatchResult<Blob>> batchResults =
            blobs
                .[streamAll](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html#com_google_api_gax_paging_Page_streamAll__)()
                .map(blob -> batchRequest.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageBatch.html#com_google_cloud_storage_StorageBatch_update_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_Storage_BlobTargetOption____)(blob.toBuilder().setMetadata(newMetadata).build()))
                .collect(Collectors.toList());
    
        // Execute the batch request
        batchRequest.[submit](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageBatch.html#com_google_cloud_storage_StorageBatch_submit__)();
        List<StorageException> failures =
            batchResults.stream()
                .map(
                    r -> {
                      try {
                        BlobInfo blob = r.get();
                        return null;
                      } catch ([StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) e) {
                        return e;
                      }
                    })
                .filter(Objects::nonNull)
                .collect(Collectors.toList());
    
        System.out.println(
            (batchResults.size() - failures.size())
                + " blobs in bucket "
                + bucketName
                + " with prefix '"
                + pathPrefix
                + "' had their metadata updated successfully.");
    
        if (!failures.isEmpty()) {
          System.out.println("While processing, there were " + failures.size() + " failures");
    
          for ([StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) failure : failures) {
            failure.printStackTrace(System.out);
          }
        }
      }
    }

### Node.js

The Node.js client library does not support batched requests.

### PHP

The PHP client library does not support batched requests.

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://docs.cloud.google.com/storage/docs/reference/libraries).
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def batch_request(bucket_name, prefix=None):
        """
        Use a batch request to patch a list of objects with the given prefix in a bucket.
    
        Note that Cloud Storage does not support batch operations for uploading or downloading.
        Additionally, the current batch design does not support library methods whose return values
        depend on the response payload.
        See https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.batch
        """
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
        # The prefix of the object paths
        # prefix = "directory-prefix/"
    
        client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Accumulate in a list the objects with a given prefix.
        blobs_to_patch = [blob for blob in bucket.list_blobs(prefix=prefix)]
    
        # Use a batch context manager to edit metadata in the list of blobs.
        # The batch request is sent out when the context manager closes.
        # No more than 100 calls should be included in a single batch request.
        with client.[batch](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_batch)():
            for blob in blobs_to_patch:
                metadata = {"your-metadata-key": "your-metadata-value"}
                blob.[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata) = metadata
                blob.patch()
    
        print(
            f"Batch request edited metadata for all objects with the given prefix in {bucket.name}."
        )
    
    

### Ruby

To learn how to make a batch request using Ruby, see the [Cloud Storage Ruby API reference documentation](https://docs.cloud.google.com/storage/docs/reference/libraries).

### Rust

The Rust client library does not support batched requests.

### Example batch HTTP response

This is the response to the HTTP example request in the previous section.
    
    
    HTTP/1.1 200 OK
    Content-Type: multipart/mixed; boundary=batch_pK7JBAk73-E=_AA5eFwv4m2Q=
    Date: Mon, 22 Jan 2018 18:56:00 GMT
    Expires: Mon, 22 Jan 2018 18:56:00 GMT
    Cache-Control: private, max-age=0
    Content-Length: 3767
    
    --batch_pK7JBAk73-E=_AA5eFwv4m2Q=
    Content-Type: application/http
    Content-ID: <response-b29c5de2-0db4-490b-b421-6a51b598bd22+1>
    
    HTTP/1.1 200 OK
    ETag: "lGaP-E0memYDumK16YuUDM_6Gf0/V43j6azD55CPRGb9b6uytDYl61Y"
    Content-Type: application/json; charset=UTF-8
    Date: Mon, 22 Jan 2018 18:56:00 GMT
    Expires: Mon, 22 Jan 2018 18:56:00 GMT
    Cache-Control: private, max-age=0
    Content-Length: 846
    
    {
     "kind": "storage#object",
     "id": "example-bucket/obj1/1495822576643790",
     .
     .
     .
     "metadata": {
      "type": "tabby"
      },
      .
      .
      .
    }
    
    --batch_pK7JBAk73-E=_AA5eFwv4m2Q=
    Content-Type: application/http
    Content-ID: <response-b29c5de2-0db4-490b-b421-6a51b598bd22+2>
    
    HTTP/1.1 200 OK
    ETag: "lGaP-E0memYDumK16YuUDM_6Gf0/91POdd-sxSAkJnS8Dm7wMxBSDKk"
    Content-Type: application/json; charset=UTF-8
    Date: Mon, 22 Jan 2018 18:56:00 GMT
    Expires: Mon, 22 Jan 2018 18:56:00 GMT
    Cache-Control: private, max-age=0
    Content-Length: 846
    
    {
     "kind": "storage#object",
     "id": "example-bucket/obj2/1495822576643790",
     .
     .
     .
     "metadata": {
      "type": "tuxedo"
      },
      .
      .
      .
    }
    
    --batch_pK7JBAk73-E=_AA5eFwv4m2Q=
    Content-Type: application/http
    Content-ID: <response-b29c5de2-0db4-490b-b421-6a51b598bd22+3>
    
    HTTP/1.1 200 OK
    ETag: "lGaP-E0memYDumK16YuUDM_6Gf0/d2Z1F1_ZVbB1dC0YKM9rX5VAgIQ"
    Content-Type: application/json; charset=UTF-8
    Date: Mon, 22 Jan 2018 18:56:00 GMT
    Expires: Mon, 22 Jan 2018 18:56:00 GMT
    Cache-Control: private, max-age=0
    Content-Length: 846
    
    {
     "kind": "storage#object",
     "id": "example-bucket/obj3/1495822576643790",
     .
     .
     .
     "metadata": {
      "type": "calico"
      },
      .
      .
      .
    }
    
    --batch_pK7JBAk73-E=_AA5eFwv4m2Q=--
    

If the overall request isn't formatted correctly and Cloud Storage is unable to parse it into sub-requests, you receive a [`400`](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes#400_Bad_Request) error. Otherwise, Cloud Storage returns a `200` status code, even if some or all of the sub-requests fail.

When the overall request returns with a `200` status code, the response contains results for each sub-request, including a status code for each, which indicates whether the sub-request succeeded or failed. For example, when batch deleting objects, each successful sub-request contains a `204 No Content` status code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
