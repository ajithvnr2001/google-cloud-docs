---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/storage-s3-rest-api/
title: Storage S3 REST API \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:34.924511+00:00
---

# Storage S3 REST API  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/storage-s3-rest-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Storage S3 REST API Stay organized with collections  Save and categorize content based on your preferences. 

### ListObjects

This operation returns some or all of the objects in a bucket, up to 1,000.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
        x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
        x-amz-request-id: B34E94CACB2CEF6D
        Date: Mon, 17 Oct 2022 22:47:09 GMT
        <ListBucketResult>
            <Name>{fully_qualified_bucket_name}</Name>
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
    

### ListObjectsV2

This operation returns some or all of the objects in a bucket, up to 1,000.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}?list-type=2 HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
        x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
        x-amz-request-id: B34E94CACB2CEF6D
        Date: Mon, 17 Oct 2022 22:47:09 GMT
        <ListBucketResult>
            <Name>{fully_qualified_bucket_name}</Name>
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
    

### GetObject (versionId optional)

This operation retrieves an object from a bucket with an optional version ID supplied.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}/{object_name}?versionId={object_version_id} HTTP/1.1
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
    

### GetObjectAcl (versionId optional)

This operation returns a positive response and the ID, DisplayName, and Permission of the object owner, indicating that the owner has full access to the object. Access credentials for the account need to be provided for this operation.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}/{object_name}?acl&versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    Content-Length: 157
    <AccessControlPolicy>
        <Owner>
            <ID>canonical-user-id</ID>
            <DisplayName>example-display-name</DisplayName>
        </Owner>
        <AccessControlList>
            <Grant>
                <Grantee>
            <ID>canonical-user-id</ID>
                    <DisplayName>example-display-name</DisplayName>
                    <Type>CanonicalUser</Type>
                </Grantee>
                <Permission>FULL_CONTROL</Permission>
            </Grant>
    </AccessControlList>
    </AccessControlPolicy>
    

### GetObjectRetention (versionId optional)

This operation retrieves the retention mode for the specified object and the date on which the Object Lock Retention expires. The bucket must have an object locking configuration.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}/{object_name}?retention&versionId={VersionId} HTTP/1.1
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
    

### GetObjectLegalHold (versionId optional)

This operation gets an object's latest legal hold status. The bucket must have an object locking configuration.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}/{object_name}?legal-hold&versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    X-amz-expected-bucket-owner: ExpectedBucketOwner (optional)
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    <LegalHold>
        <Status>ON</Status>
    </LegalHold>
    

### GetObjectTagging (versionId optional)

This operation uses the tagging subresource to return all tags for an object. If the `versionId` parameter is not specified, the operation returns all tags from the most recent version of the object in a versioned bucket. If the current version of the object is a delete marker, a `MethodNotAllowed` status is returned with the `x-amz-deletemarker` response header set to `true`.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}/{object_name}?tagging&versionId={VersionId} HTTP/1.1
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
    

### PutObject

This operation adds an object to a bucket. You must have the correct WRITE permissions on a bucket to add an object to it.

#### Encryption Version 2

For an EV2 (Encryption Version 2) bucket, the request will use a default AEAD key for encryption if no custom keys are specified.

To use a custom AEAD key for encryption, there are two headers that must be set:

  * `x-amz-server-side-encryption: SSE-KMS` \- Indicates that this request is attempting to use a custom AEAD key.
  * `x-amz-server-side-encryption-aws-kms-key-id: {custom_key_namespace}/{custom_key_name}` \- Specifies the key intended for use. The key namespace must be in the same project as the bucket.



**Request example:**
    
    
    PUT /{fully_qualified_bucket_name}/{object_name} HTTP/1.1
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
    

### PutObjectTagging

This operation uses the tagging subresource to add a set of tags to an existing object.

**Request example:**
    
    
    PUT /{fully_qualified_bucket_name}/{object_name}?tagging HTTP/1.1
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
    

### DeleteObject (versionId optional)

This operation lets you delete multiple objects from a single bucket with one request. The request can contain a list of up to 1000 keys that you want to delete.

**Request example:**
    
    
    DELETE /{fully_qualified_bucket_name}/{object_name}?versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    <Delete xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
       <Object>
          <Key>object_one.jpg</Key>
          <VersionId>1234568892</VersionId>
       </Object>
       <Object>
          <Key>object_two.jpg</Key>
       </Object>
    </Delete>
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: 5h4FxSNCUS7wP5z92eGCWDshNpMnRuXvETa4HH3LvvH6VAIr0jU7tH9kM7X+njXx
    x-amz-request-id: A437B3B641629AEE
    Date: Fri, 02 Oct 2023 01:53:42 GMT
    Content-Type: application/xml
    Content-Length: 251
    <?xml version="1.0" encoding="UTF-8"?>
    <DeleteResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Deleted>
            <Key>object_one.jpg</Key>
        </Deleted>
        <Error>
            <Key>object_two.jpg</Key>
            <Code>AccessDenied</Code>
            <Message>Access Denied</Message>
        </Error>
    </DeleteResult>
    

### DeleteObjects (versionId optional)

Removes an object from a bucket. The behavior depends on the bucket's versioning state: \- If bucket versioning is not enabled, the operation permanently deletes the object. \- If bucket versioning is enabled, the operation inserts a delete marker, which becomes the current version of the object. To permanently delete an object in a versioned bucket, you must include the object's versionId in the request.

**Request example:**
    
    
    DELETE /{fully_qualified_bucket_name}/{object_name}?versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 204 NoContent
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

### DeleteObjectTagging (versionId optional)

This operation uses the tagging subresource to remove all tags from an object.

**Request example:**
    
    
    DELETE /{fully_qualified_bucket_name}/{object_name}?tagging&versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 204 NoContent
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

### HeadObject (versionId optional)

The HEAD operation retrieves metadata from an object without returning the object itself. This operation is useful if you're interested only in an object's metadata.

**Request example:**
    
    
    HEAD /{fully_qualified_bucket_name}/{object_name}?versionId={VersionId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 200
    x-amz-id-2: ef8yU9AS1ed4OpIszj7UDNEHGran
    x-amz-request-id: 318BC8BC143432E5
    x-amz-version-id: 3HL4kqtJlcpXroDTDmjVBH40Nrjfkd
    Date: Wed, 28 Oct 2023 22:32:00 GMT
    Last-Modified: Sun, 1 Jan 2006 12:00:00 GMT
    ETag: "fba9dede5f27731c9771645a39863328"
    Content-Length: 434234
    Content-Type: text/plain
    Connection: close
    

### CreateMultipartUpload

This action initiates a multipart upload and returns an upload ID.

A multipart upload lets you add a single object as a set of parts. Each part is a contiguous portion of the object's data. Upload these object parts independently and in any order.

The returned upload ID is used to associate all of the parts in the specific multipart upload. You specify this upload ID in each of your subsequent upload part requests. You also use this upload ID in the final request to either complete or abort the multipart upload request.

#### Encryption Version 2

The returned upload ID for an EV2(Encryption Version 2) bucket will only be minted **once**. If the upload ID returned from this operation is lost it cannot be recovered from ListMultipartUploads. However, the upload IDs returned from ListMultipartUploads can be used for AbortMultipartUpload or ListParts. Only the ID returned from CreateMultipartUpload can be used for UploadPart or CompleteMultipartUpload.

**Request example:**
    
    
    POST /{fully_qualified_bucket_name}/{object_name}?uploads HTTP/1.1
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
            <Bucket>{fully_qualified_bucket_name}</Bucket>
            <Key>{object_name}</Key>
            <UploadId>VXBsb2FkIElEIGZvciA2aWWpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId>
      </InitiateMultipartUploadResult>
    

### ListMultipartUploads (max-uploads optional)

This operation lists in-progress multipart uploads for a bucket.

#### Encryption Version 2

The upload IDs returned from this operation will **only** work with ListParts and AbortMultipartUpload.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}?uploads&max-uploads={max-uploads} HTTP/1.1
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
    <Bucket>{fully_qualified_bucket_name}</Bucket>
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
    

### ListParts (max-parts optional)

This operation lists the parts that are uploaded for a specific multipart upload and returns a default maximum of 1,000 uploaded parts. You must include the upload ID, which is obtained with the CreateMultipartUpload request.

#### Encryption Version 2

The returned upload ID from CreateMultipartUpload or ListMultipartUploads may be used for this request.

**Request example:**
    
    
    GET /{fully_qualified_bucket_name}/{object_name}?uploadId={uploadId}&max-parts={max-parts} HTTP/1.1
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
            <Bucket>{fully_qualified_bucket_name}</Bucket>
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
    

### UploadPart

This operation uploads a part in a multipart upload for an object.

#### Encryption Version 2

For an EV2 (Encryption Version 2) bucket, you **must** use the ID returned from CreateMultipartUpload. The IDs returned from ListMutlipartUploads will **not** work for this request.

**Request example:**
    
    
    PUT /{fully_qualified_bucket_name}/{object_name}?uploadId={uploadId}&partNumber={partNumber} HTTP/1.1
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
    

### AbortMultipartUpload

This action aborts a multipart upload and renders the upload ID invalid for uploading any additional parts. The storage consumed by any previously uploaded parts is freed.

#### Encryption Version 2

For an EV2 (Encryption Version 2) bucket, you may either use the ID returned from CreateMultipartUpload or ListMultipartUploads for this operation.

**Request example:**
    
    
    DELETE /{fully_qualified_bucket_name}/{object_name}?uploadId={uploadId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-type: text/plain
    

**Response example (success):**
    
    
    HTTP/1.1 204 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    

### CompleteMultipartUpload

This operation completes a multipart upload of an object by assembling the previously uploaded parts.

#### Encryption Version 2

For an EV2 (Encryption Version 2) bucket, you **must** use the ID returned from CreateMultipartUpload. The IDs returned from ListMutlipartUploads will NOT work for this request.

To use a custom AEAD key for encryption, there are two headers that must be set:

  * `x-amz-server-side-encryption: SSE-KMS` \- Indicates that this request is attempting to use a custom AEAD key.
  * `x-amz-server-side-encryption-aws-kms-key-id: {custom_key_namespace}/{custom_key_name}` \- Specifies the key intended for use. The key namespace must be in the same project as the bucket.



**Request example:**
    
    
    POST /{fully_qualified_bucket_name}/{object_name}?uploadId={uploadId} HTTP/1.1
    Host: host
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    Content-Length: 391
    Content-type: text/plain
    <CompleteMultipartUpload>
    <Part>
        <PartNumber>1</PartNumber>
        <ETag>"a54357aff0632cce46d942af68356b38"</ETag>
    </Part>
    <Part>
        <PartNumber>2</PartNumber>
        <ETag>"0c78aef83f66abc1fa1e8477f296d394"</ETag>
    </Part>
    <Part>
          <PartNumber>3</PartNumber>
          <ETag>"acbd18db4cc2f85cedef654fccc4a4d8"</ETag>
    </Part>
    </CompleteMultipartUpload>
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6D
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    <CompleteMultipartUploadResult>
    <Location>http://{host}/{fully_qualified_bucket_name}/{object_name}</Location>
            <Bucket>{fully_qualified_bucket_name}</Bucket>
            <Key>{object_name}</Key>
            <ETag>"acbd18db4cc2f85cedef654fccc4a4d8"</ETag>
    </CompleteMultipartUploadResult>
    

### CopyObject

This operation is a special type of PutObject where the data will be pulled from a source object already present in object storage.

The source bucket and object key is specified as the value for the `x-amz-copy-source` header separated by a `/`. For example, to copy the object `images/my_image.jpg` from the bucket `my_bucket`, the value to be set is `my_bucket/images/my_image.jpg`.

#### Encryption Version 2

For an EV2 (Encryption Version 2) bucket, this source object **_must_** be from an Encryption V2 bucket, otherwise the operation will fail.

To use a custom AEAD key for encryption, there are two headers that must be set:

  * `x-amz-server-side-encryption: SSE-KMS` \- Indicates that this request is attempting to use a custom AEAD key.
  * `x-amz-server-side-encryption-aws-kms-key-id: {custom_key_namespace}/{custom_key_name}` \- Specifies the key intended for use. The key namespace must be in the same project as the bucket.



**Request example:**
    
    
    PUT /{fully_qualified_bucket_name}/{object_name} HTTP/1.1
    Host: host
    X-Amz-Copy-Source: my_bucket/images/my_image.jpg
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    x-amz-copy-source-version-id: 3/L4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    
    <CopyObjectResult>
        <LastModified>2009-10-12T17:50:30.000Z</LastModified>
        <ETag>"9b2cf535f27731c974343645a3985328"</ETag>
    </CopyObjectResult>
    

### UploadPartCopy

This operation will use an object already present in object storage as the data for a single part in a multipart upload.

The source bucket and object key is specified as the value for the `x-amz-copy-source` header separated by a `/`. For example, to copy the object `images/my_image.jpg` from the bucket `my_bucket`, the value to be set is `my_bucket/images/my_image.jpg`.

#### Encryption Version 2

This operation is **not** supported for EV2 (Encryption Version 2) buckets.

**Request example:**
    
    
    PUT /{fully_qualified_bucket_name}/{object_name}?uploadId={uploadId}&partNumber={partNumber} HTTP/1.1
    Host: host
    X-Amz-Copy-Source: my_bucket/images/my_image.jpg
    X-Amz-Date: date
    X-Amz-Content-SHA256: authorization string
    

**Response example (success):**
    
    
    HTTP/1.1 200 OK
    x-amz-id-2: iVmcB7OXXJRkRH1FiVq1151/T24gRfpwpuZrEG11Bb9ImOMAAe98oxSpXlknabA0LTvBYJpSIX
    x-amz-request-id: B34E94CACB2CEF6C
    x-amz-copy-source-version-id: 3/L4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo
    Date: Mon, 17 Oct 2022 22:47:09 GMT
    
    <CopyPartResult>
       <ETag>string</ETag>
       <LastModified>timestamp</LastModified>
       <ChecksumCRC32>string</ChecksumCRC32>
       <ChecksumCRC32C>string</ChecksumCRC32C>
       <ChecksumSHA1>string</ChecksumSHA1>
       <ChecksumSHA256>string</ChecksumSHA256>
    </CopyPartResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
