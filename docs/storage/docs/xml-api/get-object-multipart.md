---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-object-multipart/
title: List object parts \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:43.202292+00:00
---

# List object parts  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-object-multipart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  List object parts Stay organized with collections  Save and categorize content based on your preferences. 

Lists the uploaded parts for an ongoing [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads), returned in an XML document in the response body.

Parts in the list are ordered sequentially, and the XML API does not return lists longer than 1000 parts. If there are more parts to return than can fit in the response, the response returns an `IsTruncated` element with a value of `true` and a `NextPartNumberMarker` element which you can use in subsequent listing requests.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[max-parts](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#maxparts)` | The maximum number of parts to return in the response. | No  
`[part-number-marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#partnumbermarker)` | The part number that you want the listing to begin after. Parts whose numbers are greater than the `part-number-marker` are returned in the list of parts. | No  
`[uploadId](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#uploadid-multipart)` | The multipart upload for which you want to list the parts. | Yes  
  
See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

See [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket#request-headers).

## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax applies to GET Object requests that use the `uploadId` query string parameter.
    
    
    GET /OBJECT_NAME?uploadId=UPLOAD_ID&max-parts=MAX_NUM_PARTS&part-number-marker=PART_NUMBER HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response body elements apply to GET Object requests that use the `uploadId` query string parameter.

Element | Description  
---|---  
`ListPartsResult` | Container for the part information you are requesting.  
`Bucket` | The name of the bucket that contains the requested multipart upload.  
`Key` | The name of the object the multipart upload was initiated for.  
`UploadId` | The upload ID of the requested multipart upload.  
`StorageClass` | The storage class that parts in the multipart upload are stored as.  
`PartNumberMarker` | The part number after which the current listing begins.  
`NextPartNumberMarker` | The number of the last part returned in this listing. This is included in the response only if the list is truncated. Use this value in the `part-number-marker` query string parameter of a future listing request in order to list the parts that follow the current set of results.  
`MaxParts` | The maximum number of parts that were allowed in the response, as given by `max-parts` in the request or 1000, whichever is smaller.  
`IsTruncated` | Indicates whether or not there are parts for the upload that do not appear in the current results due to the response containing a maximum number of parts.  
`Part` | A container for each part of the multipart upload. A response can contain zero or more `Part` elements.  
`PartNumber` | The number that identifies the part.  
`LastModified` | The date and time when the part was uploaded.  
`ETag` | The [HTTP 1.1 entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) that was returned when the part was uploaded.  
`Size` | Size of the part in bytes.  
  
## Examples

The following sample lists the uploaded parts for an object named `paris.jpeg` in a bucket named `travel-maps`.

**Request**
    
    
    GET /paris.jpeg?uploadId=VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA&max-parts=2 HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Wed, 24 Mar 2021 15:31:56 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
     Content-Length: 764
     Content-Type: application/xml
     Date: Wed, 24 Mar 2021 23:31:57 GMT
     Expires: Wed, 24 Mar 2021 23:31:57 GMT
    
    <?xml version="1.0" encoding="UTF-8"?>
    <ListPartsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
      <Bucket>travel-maps</Bucket>
      <Key>paris.jpg</Key>
      <UploadId>VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
      <StorageClass>STANDARD</StorageClass>
      <PartNumberMarker>1</PartNumberMarker>
      <NextPartNumberMarker>5</NextPartNumberMarker>
      <MaxParts>2</MaxParts>
      <IsTruncated>true</IsTruncated>
      <Part>
        <PartNumber>2</PartNumber>
        <LastModified>2020-11-10T20:48:34.000Z</LastModified>
        <ETag>"7778aef83f66abc1fa1e8477f296d394"</ETag>
        <Size>10485760</Size>
      </Part>
      <Part>
        <PartNumber>5</PartNumber>
        <LastModified>2020-11-10T20:48:33.000Z</LastModified>
        <ETag>"aaaa18db4cc2f85cedef654fccc4a4x8"</ETag>
        <Size>10485760</Size>
      </Part>
    </ListPartsResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
