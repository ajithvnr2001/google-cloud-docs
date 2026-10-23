---
url: https://docs.cloud.google.com/storage/docs/paginate-results/
title: Paginate results \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:55.008579+00:00
---

# Paginate results  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/paginate-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Paginate results Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how different Cloud Storage tools and libraries paginate results. Pagination is required when listing a high number of [objects](https://docs.cloud.google.com/storage/docs/objects) or [buckets](https://docs.cloud.google.com/storage/docs/buckets).

### Console

The Google Cloud console automatically paginates bucket and object lists in the **Buckets** and **Bucket details** pages.

  
[Open the Buckets page](https://console.cloud.google.com/storage/browser)

### Command line

The Google Cloud CLI automatically paginates bucket and object lists.

### Client libraries

### C++

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size by specifying options in the request. For an example of how this iterator is used, see the C++ reference documentation for [`ListObjects()`](https://googleapis.dev/cpp/google-cloud-storage/latest/classgoogle_1_1cloud_1_1storage_1_1Client.html#ac632b30c61f6447eb35ce393a63070f5).

### C#

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size by specifying options in the request. For an example of how this iterator is used, see the C# reference documentation for [`ListObjects()`](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient#Google_Cloud_Storage_V1_StorageClient_ListObjects_System_String_System_String_Google_Cloud_Storage_V1_ListObjectsOptions_).

### Go

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size using query or pager options. For an example of how this iterator is used, see the Go reference documentation for [`Bucket.Objects`](https://pkg.go.dev/cloud.google.com/go/storage#hdr-Listing_objects).

### Java

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns a page token. You can control the page size using `pageSize` options. For an example of how this is used, see the [Java reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage#com_google_cloud_storage_Storage_list_java_lang_String_com_google_cloud_storage_Storage_BlobListOption____).

### Node.js

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size using query options (such as `maxResults`). For an example of how this iterator is used, see the Node.js reference documentation for [`getFiles()`](https://googleapis.dev/nodejs/storage/latest/Bucket.html#getFiles).

### PHP

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size using options such as `maxResults`. For an example of how this iterator is used, see the PHP reference documentation for [`Objects`](https://docs.cloud.google.com/php/docs/reference/cloud-storage/latest/Bucket#_Google_Cloud_Storage_Bucket__objects__).

### Python

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size using options such as `max_results` or `page_size`. For an example of how this iterator is used, see the Python reference documentation for [page iterators](https://googleapis.dev/python/google-api-core/latest/page_iterator.html).

### Ruby

Client libraries perform pagination by default. When you call a function that supports pagination, the method returns an iterator. You can control the page size using options such as `max`. For an example of how this iterator is used, see the Ruby reference documentation for [`Google::Cloud::Storage::File::List`](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage/File/List.html).

### REST APIs

### JSON API

To control the number of results returned per page, use the `maxResults` query parameter in requests to [`Objects: list`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) or [`Buckets: list`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list). For example, to list a maximum of 5 objects at a time:
    
    
    GET https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o?maxResults=5

When you call a function that supports pagination, the continuation token `nextPageToken` is returned in the response if the listing is incomplete. The `nextPageToken` represents the last result that's returned.

For example, a request to list objects in BUCKET_NAME might return a `nextPageToken` in the response:
    
    
    {
      "kind": "storage#objects",
      "nextPageToken": "CgtzaGliYS0yLmpwZw==",
      "items": [
        {
          OBJECT_1_METADATA
        },
        {
          OBJECT_2_METADATA
        },
        …
      ]
    }

To return the next page of results, starting after the last result, pass the value of `nextPageToken` to the `pageToken` parameter of a subsequent request:
    
    
    GET https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o?pageToken=CgtzaGliYS0yLmpwZw==

You can combine `maxResults` and `pageToken` in the same request to continue listing with a specific page size.

For more information on paginating results, see the JSON reference documentation for [`Objects: list`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) or [`Buckets: list`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list).

### XML API

To control the number of results returned per page, use the `max-keys` query parameter in requests to [`List Objects`](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list). For example, to list a maximum of 5 objects at a time:
    
    
    GET /?max-keys=5 HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com

When you call a function that supports pagination, the continuation token `NextContinuationToken` is returned in the response if the listing is incomplete. The `NextContinuationToken` represents the last result that's returned.

For example, a request to list objects in BUCKET_NAME might return a `NextContinuationToken` in the response:
    
    
    <?xml version='1.0' encoding='UTF-8'?>
    <ListBucketResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
      <Name>my-bucket</Name>
      <NextContinuationToken>CgtzaGliYS0yLmpwZw==</NextContinuationToken>
      <KeyCount>2</KeyCount>
      <MaxKeys>2</MaxKeys>
      <IsTruncated>true</IsTruncated>
      <Contents>
        ...
      </Contents>
      ...
    </ListBucketResult>

Note that `list-type` must be set to `2` to return a `NextContinuationToken` when listing objects.

To return the next page of results, starting after the last result, pass the value of `NextContinuationToken` to the `continuation-token` parameter of a subsequent request:
    
    
    GET /?continuation-token=CgtzaGliYS0yLmpwZw==&list-type=2 HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com

You can combine `max-keys` and `continuation-token` in the same request.

For more detailed instructions on paginating through results from a bucket, see the XML reference documentation for [`List Objects`](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list).

## Next steps

  * [List objects in a bucket](https://docs.cloud.google.com/storage/docs/listing-objects).
  * [List buckets in a project](https://docs.cloud.google.com/storage/docs/listing-buckets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
