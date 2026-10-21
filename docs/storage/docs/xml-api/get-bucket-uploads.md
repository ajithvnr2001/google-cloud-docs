---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-uploads/
title: List multipart uploads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:09.484860+00:00
---

# List multipart uploads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-uploads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  List multipart uploads Stay organized with collections  Save and categorize content based on your preferences. 

Lists the ongoing [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) for a bucket, returned in an XML document in the response body.

Uploads in the list are ordered lexicographically by the name of their associated objects, and the XML API does not return lists longer than 1000 uploads. If there are more uploads to return than can fit in the response, the response returns an `IsTruncated` element with a value of `true`. In this case, the response also contains a `NextKeyMarker` and a `NextUploadIdMarker` element which you can use in subsequent listing requests.

You can restrict and organize the list of uploads returned in the request by using the listed query string parameters.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[delimiter](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#delimiter)` | A character or multiple characters that can be used to simplify a list of uploads when their associated objects use a directory-like naming scheme. Can be used in conjunction with a `prefix`. | No  
`[encoding-type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#encodingtype)` | When set to `url`, object names are URL-encoded in the response. | No  
`[key-marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#keymarker)` | The object name after which you want to start listing. Uploads that are associated with objects whose names are lexicographically greater than the `key-marker` are returned in the list of uploads. | No  
`[max-uploads](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#maxuploads)` | The maximum number of uploads to return in the response. | No  
`[prefix](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#prefix)` | A string that limits the returned uploads to only those associated with objects whose names begin with the specified value. Can be used in conjunction with a `delimiter`. | No  
`[upload-id-marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#uploadidmarker)` | The upload ID after which you want to start listing uploads. If you use `upload-id-marker`, you must also use `key-marker`, or else `upload-id-marker` is ignored. Uploads that are associated with the object whose names matches the `key-marker` and that are lexicographically greater than the `upload-id-marker` are returned in the list of uploads. | No  
`[uploads](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#uploads)` | Indicates that the list request applies to ongoing multipart uploads in the bucket. | Yes  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Bucket requests that use the `uploads` query string parameter.
    
    
    GET /?uploads&prefix=OBJECT_PREFIX&key-marker=OBJECT_NAME&upload-id-marker=UPLOAD_ID&max-uploads=MAX_NUM_UPLOADS&delimiter=OBJECT_DELIMITER HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response body elements apply to GET Bucket requests that use the `uploads` query string parameter.

Element | Description  
---|---  
`ListMultipartUploadsResult` | Container for the upload information you are requesting.  
`Bucket` | The name of the bucket that contains the requested multipart uploads.  
`KeyMarker` | The object name at or after which the current listing begins.  
`UploadIdMarker` | The upload ID after which the current listing begins.  
`NextKeyMarker` | The name of the last object whose uploads were returned in this listing. This is included in the response only if the list is truncated. Use this value in the `key-marker` query string parameter of a future listing request in order to list the uploads that follow the current set of results.  
`NextUploadIdMarker` | The ID of the last upload that was returned in this listing. This is included in the response only if the list is truncated. Use this value in the `upload-id-marker` query string parameter of a future listing request in order to list the uploads that follow the current set of results.  
`Delimiter` | The `delimiter` that you specified in the request.  
`Prefix` | The `prefix` that you specified in the request.  
`MaxUploads` | The maximum number of uploads that were allowed in the response, as given by `max-uploads` in the request or 1000, whichever is smaller.  
`IsTruncated` | Indicates whether or not there are uploads that do not appear in the current results due to the response containing a maximum number of uploads.  
`Upload` | A container for each ongoing multipart upload in the bucket. A response can contain zero or more `Upload` elements.  
`Key` | The name of the object for which the multipart upload was initiated.  
`UploadId` | The upload ID that identifies the multipart upload.  
`StorageClass` | The storage class for the multipart upload.  
`Initiated` | The date and time when the multipart upload was initiated.  
`CommonPrefixes` | Container for prefixes that satisfy your `prefix` and `delimiter` constraints. This container is used only if you specify a `delimiter` in the request, and duplicate entries are omitted. Within each `CommonPrefixes` container is a single `Prefixes` element with a prefix value.  
  
## Examples

The following sample lists the ongoing multipart uploads in a bucket named `travel-maps`.

**Request**
    
    
    GET /?uploads&max-uploads=2 HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Wed, 24 Mar 2021 15:31:56 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
     Content-Length: 827
     Content-Type: application/xml
     Date: Wed, 24 Mar 2021 23:31:57 GMT
     Expires: Wed, 24 Mar 2021 23:31:57 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <ListMultipartUploadsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
      <Bucket>travel-maps</Bucket>
      <KeyMarker></KeyMarker>
      <UploadIdMarker></UploadIdMarker>
      <NextKeyMarker>cannes.jpeg</NextKeyMarker>
      <NextUploadIdMarker>YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</NextUploadIdMarker>
      <MaxUploads>2</MaxUploads>
      <IsTruncated>true</IsTruncated>
      <Upload>
        <Key>paris.jpeg</Key>
        <UploadId>VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
        <StorageClass>STANDARD</StorageClass>
        <Initiated>2021-11-10T20:48:33.000Z</Initiated>
      </Upload>
      <Upload>
        <Key>tokyo.jpeg</Key>
        <UploadId>YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</UploadId>
        <StorageClass>STANDARD</StorageClass>
        <Initiated>2021-11-10T20:49:33.000Z</Initiated>
      </Upload>
    </ListMultipartUploadsResult>
    

For an example of listing with the `prefix` and `delimiter` query string parameters, see the [List objects reference page](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list#delimiter-example).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
