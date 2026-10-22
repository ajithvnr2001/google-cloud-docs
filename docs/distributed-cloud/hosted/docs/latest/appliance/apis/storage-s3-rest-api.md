---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-s3-rest-api/
title: Storage S3 REST API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:29.744155+00:00
---

# Storage S3 REST API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-s3-rest-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Storage S3 REST API Stay organized with collections  Save and categorize content based on your preferences. 

### GET Bucket (List Objects in Bucket)

This operation returns some or all of the objects in a bucket, up to 1,000.

**Request example:**
    
    
    GET /{bucket_name} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
        x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
        x-amz-request-id: B34E94CACB2CEF6D
        Date: Mon, 17 Oct 2022 22:47:09 GMT
        <ListBucketResult>
            <Name>{bucket_name}</Name>
            <Prefix></Prefix>
            <Marker></Marker>
            <Contents>
                    <Key>example-object.jpg</Key>
                    <LastModified>2022-10-17T01:56:20.000Z</LastModified>
                    <ETag>"bf1d937a4d46a19f3basdfeg5cc8b902"</ETag>
                    <Size>32347</Size>
                    <Owner>
                    <ID>canonical-user-id</ID>
                    <DisplayName>example-display-name</DisplayName>
                    </Owner>
                    <StorageClass>STANDARD</StorageClass>
            </Contents>
      </ListBucketResult>
    

### GET Bucket Versioning

This operation uses the versioning subresource to return the versioning state of a bucket:

  * Blank: Versioning has never been enabled and the bucket is Unversioned.
  * Enabled: Versioning is enabled.
  * Suspended: Versioning was previously enabled and is suspended.



**Request example:**
    
    
    GET /{bucket_name}?versioning HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    X-amz-expected-bucket-owner: ExpectedBucketOwner (optional)
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
        x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
        x-amz-request-id: B34E94CACB2CEF6D
        Date: Mon, 17 Oct 2022 22:47:09 GMT
      <VersioningConfiguration>
        <Status>Enabled</Status>
      </VersioningConfiguration>
    

### GET Object

This operation retrieves an object from a bucket.

**Request example:**
    
    
    GET /{bucket_name}/{object_name} HTTP/1.1
    Host: host
    Content-MD5: request header
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
    Content-Length: 13432
    [13432 bytes of object data]
    

### GET Object Retention (versionId optional)

This operation retrieves the retention mode for the specified object and the date on which the Object Lock Retention expires.

**Request example:**
    
    
    GET /{bucket_name}/{object_name}?retention&versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    X-amz-expected-bucket-owner: ExpectedBucketOwner (optional)
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    <Retention>
        <Mode>COMPLIANCE</Mode>
        <Timestamp>2022-10-17T01:56:20.000Z</Timestamp>
    </Retention>
    

### GET Object Tagging (versionId optional)

This operation uses the tagging subresource to return all tags for an object. If the `versionId` parameter is not specified, the operation returns all tags from the most recent version of the object in a versioned bucket. If the current version of the object is a delete marker, a `MethodNotAllowed` status is returned with the `x-amz-deletemarker` response header set to `true`.

**Request example:**
    
    
    GET /{bucket_name}/{object_name}?tagging&versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    X-amz-expected-bucket-owner: ExpectedBucketOwner (optional)
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    <Tagging>
      <TagSet>
            <Tag>
            <Key>tag1</Key>
            <Value>val1</Value>
          </Tag>
          <Tag>
            <Key>tag2</Key>
            <Value>val2</Value>
          </Tag>
      </TagSet>
    </Tagging>
    

### PUT Object

This operation adds an object to a bucket. You must have the correct WRITE permissions on a bucket to add an object to it.

**Request example:**
    
    
    PUT /{bucket_name}/{object_name} HTTP/1.1
    Host: host
    Content-MD5: request header
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-Length: 5233
    Content-type: text/plain
    [5233 bytes of object data]
    

**Response example (success):**
    
    
    HTTP/1.1 100 Continue
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
    

### PUT Object Tagging

This operation uses the tagging subresource to add a set of tags to an existing object.

**Request example:**
    
    
    PUT /{bucket_name}/{object_name}?tagging HTTP/1.1
    Host: host
    Content-MD5: +b9TrAB9F8ne7rJpPkqavQ==
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-Length: {length}
    Content-type: text/plain
    <Tagging>
        <TagSet>
            <Tag>
                <key>my-tag-key</key>
                <value>my-tag-value</value>
            </Tag>
        </TagSet>
    </Tagging>
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

### DELETE Object (versionId optional)

This operation removes all copies of the object from all stored locations.

**Request example:**
    
    
    DELETE /{bucket_name}/{object_name}?versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 204 NoContent
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

### DELETE Object Tagging (versionId optional)

This operation uses the tagging subresource to remove all tags from an object.

**Request example:**
    
    
    DELETE /{bucket_name}/{object_name}?tagging&versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 204 NoContent
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

### Create Multipart Upload

This action initiates a multipart upload and returns an upload ID.

A multipart upload allows you to add a single object as a set of parts. Each part is a contiguous portion of the object's data. Upload these object parts independently and in any order.

The returned upload ID is used to associate all of the parts in the specific multipart upload. You specify this upload ID in each of your subsequent upload part requests. You also use this upload ID in the final request to either complete or abort the multipart upload request.

**Request example:**
    
    
    POST /{bucket_name}/{object_name}?uploads HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
        <InitiateMultipartUploadResult>
            <Bucket>{bucket_name}</Bucket>
            <Key>{object_name}</Key>
            <UploadId>VXBsb2FkIElEIGZvciA2aWWpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
      </InitiateMultipartUploadResult>
    

### List Multipart Uploads (max-uploads optional)

This operation lists in-progress multipart uploads for a bucket.

**Request example:**
    
    
    GET /{bucket_name}?uploads&max-uploads={max-uploads} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    <ListMultipartUploadsResult>
    <Bucket>{bucket_name}</Bucket>
    <KeyMarker></KeyMarker>
    <UploadIdMarker></UploadIdMarker>
    <NextKeyMarker>my-movie.m2ts</NextKeyMarker>
        <NextUploadIdMarker>YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</NextUploadIdMarker>
        <MaxUploads>3</MaxUploads>
        <IsTruncated>true</IsTruncated>
        <Upload>
                <Key>{object_name}</Key>
                <UploadId>VXBsb2FkIElEIGZvciA2aWWpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
                <Initiator>
                <ID>{canonical-user-id}</ID>
                <DisplayName>InitiatorDisplayName</DisplayName>
                </Initiator>
                <Owner>
                <ID>{canonical-owner-user-id}</ID>
                <DisplayName>OwnerDisplayName</DisplayName>
                </Owner>
                <StorageClass>STANDARD</StorageClass>
                <Initiated>2022-10-17T01:56:20.000Z</Initiated>
        </Upload>
    </ListMultipartUploadsResult>
    

### List Parts of a Multipart Upload (max-parts optional)

This operation lists the parts that are uploaded for a specific multipart upload and returns a default maximum of 1,000 uploaded parts. You must include the upload ID, which is obtained with the `CreateMultipartUpload` request.

**Request example:**
    
    
    GET /{bucket_name}/{object_name}?uploadId={uploadId}&max-parts={max-parts} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    <ListPartsResult>
            <Bucket>{bucket_name}</Bucket>
            <Key>{object_name}</Key>
            <UploadId>{uploadId}</UploadId>
            <Initiator>
                <ID>{canonical-user-id}</ID>
                <DisplayName>InitiatorDisplayName</DisplayName>
              </Initiator>
            <Owner>
                    <ID>{canonical-owner-id}</ID>
                    <DisplayName>OwnerDisplayName</DisplayName>
            </Owner>
            <StorageClass>STANDARD</StorageClass>
            <PartNumberMarker></PartNumberMarker>
            <NextPartNumberMarker></NextPartNumberMarker>
            <MaxParts>{max-parts}</MaxParts>
            <IsTruncated>true</IsTruncated>
            <Part>
                    <PartNumber>2</PartNumber>
                    <LastModified>2022-10-17T01:56:20.000Z</LastModified>
                    <ETag>"7778aef8t866abc1fa1e8466f296d394"</ETag>
                    <Size>10485769</Size>
            </Part>
            <Part>
                    <PartNumber>3</PartNumber>
                    <LastModified>2022-10-17T01:56:20.000Z</LastModified>
                    <ETag>"aaab18db4cc2f85cedef854fccci24x8"</ETag>
                    <Size>10423760</Size>
            </Part>
    </ListPartsResult>
    

### Upload Part

This operation uploads a part in a multipart upload for an object.

**Request example:**
    
    
    PUT /{bucket_name}/{object_name}?uploadId={uploadId}&partNumber={partNumber} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-Length: 345442
    Content-MD5: +b9TrAB9F8ne7rJpPkqavQ==
    [part data omitted, 345442 bytes of part data]
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
    

### Abort MultiPart Upload

This action aborts a multipart upload and renders the upload ID invalid for uploading any additional parts. The storage consumed by any previously uploaded parts is freed.

**Request example:**
    
    
    DELETE /{bucket_name}/{object_name}?uploadId={uploadId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 204 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
