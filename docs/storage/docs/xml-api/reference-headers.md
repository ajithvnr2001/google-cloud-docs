---
url: https://docs.cloud.google.com/storage/docs/xml-api/reference-headers/
title: HTTP headers and query string parameters for XML API \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:55.328814+00:00
---

# HTTP headers and query string parameters for XML API  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/reference-headers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  HTTP headers and query string parameters for XML API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage XML API uses several standard HTTP headers as well as several extension (custom) HTTP headers. Several of the HTTP methods also support query string parameters. The headers and parameters are described below.

## HTTP headers and query string parameters summary

The XML API uses the following standard HTTP headers:

Request | Response | Both  
---|---|---  
`Authorization`  
`Content-MD5`  
`Host`  
`If-Match`  
`If-Modified-Since`  
`If-None-Match`  
`If-Unmodified-Since` |  `ETag`  
`Last-Modified`  
`Location` |  `Cache-Control`  
`Content-Disposition`  
`Content-Encoding`  
`Content-Language`  
`Content-Length`  
`Content-Range`  
`Content-Type`  
`Date`  
`Range`  
`Transfer-Encoding`  
  
The XML API uses the following extension (custom) HTTP headers:

Request | Response | Both  
---|---|---  
`x-amz-decoded-content-length`  
`x-goog-acl`  
`x-goog-allowed-resources`  
`x-goog-api-version`  
`x-goog-bucket-object-lock-enabled`  
`x-goog-bucket-retention-period`  
`x-goog-bypass-governance-retention`  
`x-goog-content-length-range`  
`x-goog-content-sha256`  
`x-goog-copy-source`  
`x-goog-copy-source-generation`  
`x-goog-copy-source-if-generation-match`  
`x-goog-copy-source-if-match`  
`x-goog-copy-source-if-metageneration-match`  
`x-goog-copy-source-if-modified-since`  
`x-goog-copy-source-if-none-match`  
`x-goog-copy-source-if-unmodified-since`  
`x-goog-custom-audit-KEY`  
`x-goog-date`  
`x-goog-encryption-key`  
`x-goog-encryption-kms-key-name`  
`x-goog-if-generation-match`  
`x-goog-if-metageneration-match`  
`x-goog-interop-list-objects-format`  
`x-goog-metadata-directive`  
`x-goog-project-id`  
`x-goog-resumable`  
`x-goog-user-project` |  `x-goog-component-count`  
`x-goog-expiration`  
`x-goog-generation`  
`x-goog-metageneration`  
`x-goog-stored-content-encoding`  
`x-goog-stored-content-length`  
`x-guploader-uploadid` |  `x-goog-custom-time`  
`x-goog-encryption-algorithm`  
`x-goog-encryption-key-sha256`  
`x-goog-hash`  
`x-goog-meta-KEY`  
`x-goog-object-lock-mode`  
`x-goog-object-lock-retain-until-date`  
`x-goog-storage-class`  
  
The XML API uses the following query string parameters:

`AccessKeyId`  
`acl`  
`Action`  
`billing`  
`compose`  
`continuation-token`  
`cors`  
`customPlacementConfig`  
`defaultObjectAcl`  
`delete`  
`delimiter`  
`encoding-type`  
`encryption`  
`encryptionConfig`  
`fetch-owner`  
`generation`  
`generation-marker`  
`key-marker`  
`lifecycle` |  `list-type`  
`location`  
`logging`  
`marker`  
`Marker`  
`max-keys`  
`max-parts`  
`max-uploads`  
`MaxItems`  
`object-lock`  
`part-number-marker`  
`partNumber`  
`prefix`  
`response-content-disposition`  
`response-content-type`  
`retention`  
`start-after`  
`Status`  
`storageClass` |  `tagging`  
`upload_id`  
`upload-id-marker`  
`uploadId`  
`uploads`  
`UserName`  
`userProject`  
`version-id-marker`  
`versioning`  
`versions`  
`websiteConfig`  
`X-Goog-Algorithm`  
`X-Goog-Credential`  
`X-Goog-Custom-Audit-KEY`  
`X-Goog-Date`  
`X-Goog-Expires`  
`X-Goog-SignedHeaders`  
`X-Goog-Signature`  
---|---|---  
  
## Standard HTTP headers

#### Authorization

A request header that contains a string used to authenticate requests.

Valid Values | One of the following: 

  * The authentication identifier `Bearer` followed by a valid OAuth 2.0 token.
  * A valid signature header, as defined in the [Simple migration documentation](https://docs.cloud.google.com/storage/docs/aws-simple-migration#authheader).
  * The authentication identifier `GOOG1` or `AWS` followed by `KEY_ACCESS_ID:V2_SIGNATURE`.

  
---|---  
Example | `Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s- ... `  
Details |  To create a sample OAuth 2.0 access token for testing, you can use the [OAuth 2.0 playground](https://developers.google.com/oauthplayground/). **Note:** If your requests are being routed through a proxy, you may need to check with your network administrator to verify that the `Authorization` header containing your credentials is not stripped out by the proxy. Without the `Authorization` header, you receive a `MissingSecurityHeader` error and your request is rejected. For more information about accessing Cloud Storage through a proxy server, see the [ Troubleshooting topic](https://docs.cloud.google.com/storage/docs/troubleshooting#proxy-server).  
  
#### Cache-Control

A request and response header that specifies the cache-control setting.

Valid Values | Any valid cache-control value (see the [specification](https://datatracker.ietf.org/doc/html/rfc7234#section-5.2)).  
---|---  
Example | `Cache-Control: public, max-age=6000`  
Details | You should specify `Cache-Control` only for objects that are accessible to all anonymous users. To be anonymously accessible, an object's ACL must grant `READ` or `FULL_CONTROL` permission to `AllUsers`. If an object is accessible to all anonymous users and you don't specify a `Cache-Control` setting, Cloud Storage applies a `Cache-Control` setting of 3600 seconds. When serving via XML, Cloud Storage respects the `Cache-Control` of the object as set by its metadata.  
  
#### Content-Disposition

A request and response header that specifies presentational information about the data being transmitted.

Valid Values | Any valid content disposition value (see the [specification](https://datatracker.ietf.org/doc/html/rfc6266)).  
---|---  
Example | `Content-Disposition: attachment; filename=FILENAME`  
Details | If you set the `Content-Disposition` header when uploading an object, it will be served at download time (and subsequently interpreted by web browsers and other HTTP clients). A common use for `Content-Disposition` is setting it to `attachment;filename=FILENAME`, typically causing the web browser to open a "Save As..." dialog box.  
  
#### Content-Encoding

A request and response header that specifies the compression algorithm for an object. This header is also used for requests that use a [V4 signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) in the `Authorization` header and upload data in chunks.

Valid Values | Any valid compression algorithm (see the [specification](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.2.2)) or `aws-chunked`  
---|---  
Example | `Content-Encoding: gzip`  
Details | Cloud Storage does not compress objects and only decompresses objects in [certain scenarios](https://docs.cloud.google.com/storage/docs/transcoding). If you use this header to specify a compression type algorithm (for example, `deflate`), Cloud Storage preserves the header as [object metadata](https://docs.cloud.google.com/storage/docs/metadata), but does not compress or decompress the object. If an upload request uses `Content-Encoding: aws-chunked`, the request should authenticate using a [V4 Signature](https://docs.cloud.google.com/storage/docs/authentication/signatures), and its body should include chunked object data that meets the [specification](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-streaming.html). The value `aws-chunked` is not stored as part of an object's metadata.  
  
#### Content-Language

Language code of the content.

Valid Values | A string of up to 100 characters. See the ISO 639-1 column of [Codes for the Representation of Names of Languages](https://www.loc.gov/standards/iso639-2/php/code_list.php) for a list of language codes.  
---|---  
Example | `Content-Language: en`  
  
#### Content-Length

The length (in bytes) of the request or response body.

Valid Values | Any value of zero or greater.  
---|---  
Example | `Content-Length: 1234`  
Details | This is required for all requests except those that use chunked transfer encoding (see the [specification](https://datatracker.ietf.org/doc/html/rfc7230#section-4.1)). If you don't use chunked transfer encoding and you don't include the `Content-Length` header in a request, the request fails and Cloud Storage responds with a 411 Length Required status code.  
  
#### Content-MD5

The MD5 digest of the request body.

Valid Values | A valid MD5 digest.  
---|---  
Example | `Content-MD5: iB94gawbwUSiZy5FuruIOQ==`  
Details | See the [specification](https://datatracker.ietf.org/doc/html/rfc1864#section-2). Cloud Storage can use this to check the integrity of a `PUT` operation.  
  
#### Content-Range

A request or response header that specifies a byte range.

Valid Values | Any valid byte range.  
---|---  
Example | `Content-Range: bytes 456-987/1234`  
Details | When appearing in a response, the `Content-Range` header indicates the range of bytes being returned as a result of a request that included a `Range` header. When included as part of a [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads) request, `Content-Range` is used to query for the current position of the upload or as an indicator of the starting point of the block of data being uploaded in the current request. Byte ranges are inclusive; that is, `bytes 0-999` represent the first 1000 bytes in a file or object. For additional details, particularly regarding download responses, see the [specification](https://datatracker.ietf.org/doc/html/rfc7233#section-4.2).  
  
#### Content-Type

The MIME type of the request or response.

Valid Values | Any valid MIME type (see the [specification](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5)).  
---|---  
Example | `Content-Type: text/html`  
Details | If you don't specify a content type when you upload an object, the Cloud Storage system defaults to `[application/octet-stream](https://datatracker.ietf.org/doc/html/rfc2046#section-4.5.1)` when it serves the object.  
  
#### Date

The date and time of the request or response.

Valid Values | A date and time represented in conventional HTTP format (see the [specification](https://datatracker.ietf.org/doc/html/rfc7231#section-7.1.1.2)).  
---|---  
Example | `Date: Wed, 16 Jun 2010 11:11:11 GMT`  
Details | When used to create [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) using the V2 signing process, the format should be in conventional HTTP format; see [section 7.1.1.2 of the specification](https://www.ietf.org/rfc/rfc7231.txt). When using the V4 signing process, the format should be in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) basic format `YYYYMMDD'T'HHMMSS'Z'`.  
  
#### ETag

A response header that contains the entity tag of the object being accessed.

Valid Values | A string of characters enclosed by quotes. For more information, see [Object metadata](https://docs.cloud.google.com/storage/docs/metadata#etags).  
---|---  
Examples | `ETag: "39a59594290b0f9a30662a56d695b71d"`  
`ETag: "-CKicn4fknbUCEAE="`  
Details | See the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3).  
  
#### Host

A request header that specifies the URI for Cloud Storage.

Valid Values | A valid format for the URI.  
---|---  
Example | `Host: storage.googleapis.com`  
Details | For more information about valid URIs, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints) and the [host specification](https://datatracker.ietf.org/doc/html/rfc7230#section-5.4).  
  
#### If-Match

A request header that specifies an entity tag ([ETag](https://docs.cloud.google.com/storage/docs/metadata#etags)).

Valid Values | A valid entity tag.  
---|---  
Example | `If-Match: "881f7881ac1bc144a2672e45babb8839"`  
Details | You can use this header with the HEAD Object and GET Object methods. If the ETag you specify with this header is the same as the ETag for the object, then the metadata or the object is returned. If the ETag you specify with this header is different than the ETag for the object, then the metadata or the object is not returned and Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. For more details, see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.1).  
  
#### If-Modified-Since

A request header that specifies a date and time.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `If-Modified-Since: Fri, 19 Feb 2010 22:04:23 GMT`  
Details | You can use this header with the HEAD Object and GET Object methods. If an object has been modified later than the date and time you specify with this header, then the metadata or the object is returned. If an object has been modified earlier than the date and time you specify with this header, then the metadata or the object is not returned and Cloud Storage returns a [304 Not Modified](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code. For more information about the If-Modified-Since header, see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.3). For more detail about HTTP date formats, see the [specification](https://www.ietf.org/rfc/rfc7231.txt), Section 7.1.1.2.  
  
#### If-None-Match

A request header that specifies an entity tag ([ETag](https://docs.cloud.google.com/storage/docs/metadata#etags)).

Valid Values | A valid entity tag.  
---|---  
Example | `If-None-Match: "881f7881ac1bc144a2672e45babb8839"`  
Details | You can use this header with the HEAD Object and GET Object methods. If the ETag you specify with this header is different from the ETag for the object, then the metadata or the object is returned. If the ETag you specify with this header is the same as the ETag of the object, then the metadata or the object is not returned and Cloud Storage returns a [304 Not Modified](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code. For more details, see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.2).  
  
#### If-Unmodified-Since

A request header that specifies a date and time.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `If-Unmodified-Since: Fri, 19 Feb 2010 22:04:23 GMT`  
Details | You can use this header with the HEAD Object and GET Object methods. If the object has not been modified later than the date you specify with this header, then the metadata or the object is returned. If the object has been modified later than the date you specify with this header, then the metadata or the object is not returned and Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. For more information about the If-Unmodified-Since header, see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.4). For more information about HTTP date formats, see the [specification](https://www.ietf.org/rfc/rfc7231.txt), Section 7.1.1.2.  
  
#### Last-Modified

A response header that contains the date and time that the object was last modified.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `Last-Modified: Fri, 19 Feb 2010 22:04:23 GMT`  
Details |  For more information about the Last-Modified header, see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-2.2). For more information about HTTP date formats, see the [specification](https://www.ietf.org/rfc/rfc7231.txt), Section 7.1.1.2.  
  
#### Location

A response header used for several purposes:

  * In response to initiating a resumable upload it provides you with a session URI for a resumable upload operation.
  * In response to completing a multipart upload it provides you with an endpoint for accessing the assembled object.
  * In response to a [Cookie-based authentication request](https://docs.cloud.google.com/storage/docs/request-endpoints#cookieauth) it provides you with a unique web origin response URL for the request.
  * In response to a JSON API download request made at a URL other than `www.googleapis.com/download` it provides a redirect to the JSON API URL where the download can be made.

Valid Values | Any valid URI.  
---|---  
Example | `Location: https://example.storage.googleapis.com/?upload_id=tvA0...rot`  
Details | The `Location` response header is returned when you initiate a resumable upload.  
  
#### Range

A request header indicating the range of bytes that you want returned, and a response header indicating the range of bytes that have been uploaded to the Cloud Storage system.

Valid Values | A single, contiguous range of bytes.  
---|---  
Examples | `Range: bytes=0-1999` (first 2000 bytes)  
`Range: bytes=-2000` (last 2000 bytes)  
`Range: bytes=2000-` (from byte 2000 to end of file)  
Details |  When included as a header in a request for object data, only the specified range of bytes for the object gets returned in the response body, which is useful when downloading an object in parallel requests or when resuming an interrupted download. A valid and successful request results in a [206 Partial Content](https://datatracker.ietf.org/doc/html/rfc7233#section-4.1) response code. Multiple byte ranges in a single request are not accepted, and in [certain circumstances](https://docs.cloud.google.com/storage/docs/transcoding#range) the `Range` request header is ignored. When returned as part of a response associated with a resumable upload, `Range` indicates the number of bytes currently uploaded. You can subsequently use this information to [continue the upload](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads#resume-upload). Byte ranges are inclusive. For example, `bytes=0-999` represent the first 1000 bytes in a file or object. For more information about this header, see the [specification](https://datatracker.ietf.org/doc/html/rfc7233#section-3.1).  
  
#### Transfer-Encoding

A request and response header that specifies if transfer-encoding had been applied to the message body.

Valid Values | `chunked`  
---|---  
Example | `Transfer-Encoding: chunked`  
Details | This header specifies if the message body of a request or response has been chunked. If it is, content is received or served in a series of chunks, with the final chunk having a length of zero. If you specify `Transfer-Encoding: Chunked`, you don't need to specify a `Content-Length`. This can be useful if you don't know the length of the message body in advance, such as when performing a streaming upload. In an upload request that uses `Transfer-Encoding: Chunked` and a [V4 Signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) in the `Authorization` header, the request must include a `x-amz-decoded-content-length` header. As a result, for such requests you must know the total length of the message body in advance, and you cannot use `x-goog-*` headers. In addition to a `x-amz-decoded-content-length` header, the request should also use the header `Content-Encoding: aws-chunked`. For more details about Transfer-Encodings, see the [specification](https://datatracker.ietf.org/doc/html/rfc7230#section-3.3.1). For more details about chunked transfer encoding, see the [specification](https://datatracker.ietf.org/doc/html/rfc7230#section-4.1).  
  
## Extension (custom) HTTP headers

#### x-amz-decoded-content-length

A request header that indicates the size of an upload that uses chunked transfer encoding.

Valid Values | An integer indicating the total size of the data being uploaded  
---|---  
Example | `x-amz-decoded-content-length: 66560`  
Details | This header is required when a request that has a [V4 Signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) in its `Authorization` header uses the header `Transfer-Encoding: Chunked`. The value of the `x-amz-decoded-content-length` header must equal the total decoded size of the object data being uploaded in the request. Cloud Storage does not support a `x-goog-decoded-content-length` header.   
  
#### x-goog-acl

A request header that applies [predefined ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#predefined-acl) to a bucket or object when you upload it or create it.

Valid Values | For buckets: `project-private`, `private`, `public-read`, `public-read-write`, `authenticated-read` For objects: `project-private`, `private`, `bucket-owner-read`, `bucket-owner-full-control`, `public-read`, `authenticated-read`  
---|---  
Example | `x-goog-acl: private`  
Details | When a user uploads an object or creates a bucket without specifying any ACLs, the `private` ACL is applied.  
  
#### x-goog-allowed-resources

A request header that restricts the resources the request is allowed to act on.

Valid Values | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-5) Base64-encoded string of the [organization restriction definition](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/configure-organization-restrictions#create_the_header).  
---|---  
Example | `x-goog-allowed-resources: ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiLCAib3JnYW5pemF0aW9ucy8xMDExMTIxMzE0Il0sCiAib3B0aW9ucyI6ICJzdHJpY3QiCn0K`  
Details | This request header prevents a request from proceeding unless each resource in the request is within an organization specified by the header. For more information, see [Introduction to organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/overview).  
  
#### x-goog-api-version

This header is deprecated and is not used.

#### x-goog-bucket-object-lock-enabled

A request header that enables [object retention configurations](https://docs.cloud.google.com/storage/docs/object-lock) for a new bucket.

Valid Values | `true`  
---|---  
Example | `x-goog-bucket-object-lock-enabled: true`  
Details | This request header can only be used when creating a new bucket. When the header is included and set to `true`, objects added to the bucket can be configured to have a retention configuration. Values other than `true` cause this header to be ignored.  
  
#### x-goog-bucket-retention-period

A request header that adds a [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock) to a new bucket.

Valid Values | An integer between 1 and 3,155,760,000.  
---|---  
Example | `x-goog-bucket-retention-period: 32000`  
Details | This request header can only be used when creating a new bucket. When the header is included, the new bucket gains an unlocked retention policy with a duration, in seconds, determined by this header's value.  
  
#### x-goog-bypass-governance-retention

A request header that enables you to shorten, remove, or lock a [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) for an object.

Valid Values | `true`  
---|---  
Example | `x-goog-bypass-governance-retention: true`  
Details | This request header is used as part of a request to change an existing retention configuration on an object. This header must be set to `true` in order to remove the retention configuration, make the retention configuration shorter, or set the mode of the retention configuration to `COMPLIANCE`. Note that a retention configuration cannot be removed or shortened if its mode is set to `COMPLIANCE`.  
  
#### x-goog-custom-audit-KEY

A request header that adds [custom information to audit logs](https://docs.cloud.google.com/storage/docs/audit-logging#add-custom-metadata) generated by Cloud Audit Logs.

Valid Values | Any valid header name and value. The `KEY` in the header name can contain up to 64 characters, including the `x-goog-custom-audit` prefix. The value can contain up to 1,200 characters.  
---|---  
Example | `x-goog-custom-audit-job: test-job-id`  
Details | Each request can contain up to four header entries. Custom information is added to the [`metadata`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) field of the `protoPayload` in the audit log entry.  
  
#### x-goog-component-count

A response header that indicates the number of components that make up a composite object.

Valid Values | An integer greater than or equal to 1.  
---|---  
Example | `x-goog-component-count: 32`  
Details | This response header is only returned when the accessed object is a [composite object](https://docs.cloud.google.com/storage/docs/composite-objects). The header returns the number of components that make up the object.  
  
#### x-goog-content-length-range

A `PUT` request header. When used, Cloud Storage only accepts the request if the size of the request's content is within the header's specified range.

Valid Values | A `MIN,MAX` pair  
---|---  
Example | `x-goog-content-length-range: 0,256`  
Details | The values for content size are inclusive and given in bytes. If the size of the request's content is in the specified range, it's delivered as requested. If the size of the request's content is outside the specified range, the request fails and a `400 Bad Request` code is returned in the response. If the `x-goog-content-length-range` is used in a request other than `PUT`, the header is silently ignored.  
  
#### x-goog-content-sha256

A request header that contains a hash of the request body.

Valid Values | A lowercase, hex-encoded, SHA-256 hash or `UNSIGNED-PAYLOAD`  
---|---  
Example | `x-goog-content-sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`  
Details | This header is required for requests that use a [signature](https://docs.cloud.google.com/storage/docs/authentication/signatures) in the Authorization header. The value of `x-goog-content-sha256` must match the value you used for the [payload portion of your canonical request](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#payload). 

  * For requests that initiate a [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads), the `x-goog-content-sha256` header is ignored, but the header is still required. To be consistent with the canonical request payload, you should set `x-goog-content-sha256` to `UNSIGNED-PAYLOAD`.

  
  
#### x-goog-copy-source

A request header that specifies the source bucket and object for a copy operation.

Valid Values | A `/BUCKET_NAME/OBJECT_NAME` path  
---|---  
Example | `x-goog-copy-source: travel-maps/paris.jpg`  
Details | This request header specifies the path to the source object. A valid path must include the bucket and object, separated by a slash (/). Note that the source object path must be a legal URL, so should generally be [percent encoded](https://wikipedia.org/wiki/Percent-encoding). You must have `READ` permission on the source object and at least `WRITE` permission on the destination bucket to use this header. If the source and destination objects are the same (including the generation), the copy is treated as an update of the metadata. For details on controlling the update/replace behavior, see x-goog-metadata-directive.  
  
#### x-goog-copy-source-generation

A request header that specifies the generation of the object to copy.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `x-goog-copy-source-generation: 1360044097839000`  
Details | This request header can be used with x-goog-copy-source to specify the generation of the object to copy from. It's not valid without the x-goog-copy-source header. If no such generation of the source object exists, Cloud Storage returns a [404 Not Found](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) status code. If the source and destination objects are the same (including the generation), the copy is treated as an update of the metadata. For details on controlling the update/replace behavior, see x-goog-metadata-directive.  
  
#### x-goog-copy-source-if-generation-match

A request header that specifies the corresponding copy request will only be executed if the source object `x-goog-generation` matches the specified value. This header is only valid when used with `x-goog-copy-source`.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `x-goog-copy-source-if-generation-match: 1360044097835000`  
Details | This request header can be used to conditionally copy the source object only if it has the specified generation. If the generation does not match, Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. For more information, see [Request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions).  
  
#### x-goog-copy-source-if-match

A request header that specifies the conditions for a copy operation.

Valid Values | An entity tag (ETag)  
---|---  
Example | `x-goog-copy-source-if-match: 53fc311c15eda0a031809982ccf92aac`  
Details | Only a single entity tag (not a comma-separated list of entity tags) can be specified. This request header can be used only if you are performing a copy operation with the `x-goog-copy-source` request header. If the ETag you specify with this request header matches the ETag of the source object, then the copy operation proceeds. If the ETag does not match, Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code.  
  
#### x-goog-copy-source-if-metageneration-match

A request header that specifies the corresponding request will only be allowed if the `metageneration` of the source object matches the value of this header.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `x-goog-copy-source-if-metageneration-match: 4`  
Details | If the source object metageneration matches the `x-goog-copy-source-if-metageneration-match` header, the request will be completed successfully and Cloud Storage returns a `HTTP 200 OK` status. If the metageneration does not match, Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. This value can only be used with x-goog-copy-source-if-generation-match or x-goog-copy-source-generation, and trying to use it without either of them will result in a `HTTP 400 BadRequest` Invalid Argument error code. For more information, see [Request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions).  
  
#### x-goog-copy-source-if-modified-since

A request header that specifies the conditions for a copy operation.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `x-goog-copy-source-if-modified-since: Fri, 19 Feb 2010 14:05:04 GMT`  
Details | This request header can be used only if you are performing a copy operation with the `x-goog-copy-source` request header. If the date and time you specify is earlier than the `Last-Modified` date of the source object, then the object is copied. If the date and time is later, Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. For more information about the If-Modified-Since HTTP header (which, other than the copy source, applies to this use case), see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.3). For more information about HTTP date formats, see the [specification](https://www.ietf.org/rfc/rfc7231.txt), Section 7.1.1.2  
  
#### x-goog-copy-source-if-none-match

A request header that specifies the conditions for a copy operation.

Valid Values | An entity tag (ETag)  
---|---  
Example | `x-goog-copy-source-if-none-match: 53fc311c15eda0a031809982ccf92aac`  
Details | This request header can be used only if you are performing a copy operation with the `x-goog-copy-source` request header. If the ETag you specify with this request header does not match the ETag of the source object, then the copy operation proceeds. If the ETag matches, Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. For more information about the If-None-Match HTTP header (which, other than the copy source, applies to this use case), see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.2).  
  
#### x-goog-copy-source-if-unmodified-since

A request header that specifies the conditions for a copy operation.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `x-goog-copy-source-if-unmodified-since: Fri, 19 Feb 2010 14:05:04 GMT`  
Details | This request header can be used only if you are performing a copy operation with the `x-goog-copy-source` request header. If the date and time you specify is later than the `Last-Modified` date of the source object, then the object is copied. If the date and time is earlier, Cloud Storage returns a [412 Precondition Failed](https://docs.cloud.google.com/storage/docs/xml-api/reference-status) error code. For more information about the If-Unmodified-Since HTTP header (which, other than the copy source, applies to this use case), see the [specification](https://datatracker.ietf.org/doc/html/rfc7232#section-3.4). For more information about HTTP date formats, see the [specification](https://www.ietf.org/rfc/rfc7231.txt), Section 7.1.1.2.  
  
#### x-goog-custom-time

A request and response header for [custom timestamp object metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-time).

Valid Values | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.  
---|---  
Example | `x-goog-custom-time: 2020-04-12T23:20:50.52Z`  
Details | This header can be included during object PUT or POST requests. The value you specify in the header is stored with the object and gets returned in a response header when you make a GET or HEAD request on the object. The custom time for an object is typically used with [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).  
  
#### x-goog-date

A request header that specifies a time stamp for authenticated requests.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `x-goog-date: Fri, 19 Feb 2010 14:05:04 GMT`  
Details | When used to create [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) using the V2 signing process, the format should be in conventional HTTP format; see [section 7.1.1.2 of the specification](https://www.ietf.org/rfc/rfc7231.txt). When using the V4 signing process, the format should be in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) basic format `YYYYMMDD'T'HHMMSS'Z'`.  
  
#### x-goog-encryption-algorithm

A request and response header that specifies the encryption algorithm to use.

Valid Values | `AES256`  
---|---  
Example | `x-goog-encryption-algorithm: AES256`  
Details | This request and response header is used when you provide [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption).  
  
#### x-goog-encryption-key

A request header that specifies an AES-256 encryption key.

Valid Values | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of a valid AES-256 encryption key  
---|---  
Example | `x-goog-encryption-key: NwbyGGmcKAX4FxGpOERG2Ap33m5NVOgmXznSGTEvG0I=`  
Details | This request header is used when you provide [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption).  
  
#### x-goog-encryption-key-sha256

A request and response header that specifies the SHA256 hash of the encryption key.

Valid Values | An [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-4) Base64-encoded string of a valid SHA256 hash for an encryption key  
---|---  
Example | `x-goog-encryption-key-sha256: +eBzkZBt1Mj2CZx69L3c8yXoZB6DtRLlSvXMJB9JGIQ=`  
Details | This request header is used when you provide [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption).  
  
#### x-goog-encryption-kms-key-name

A request and response header that specifies a Cloud KMS encryption key.

Valid Values | A [Cloud KMS encryption key resource](https://docs.cloud.google.com/kms/docs/object-hierarchy#key).  
---|---  
Example | `x-goog-encryption-kms-key-name: projects/my-project/locations/LOCATION_NAME/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`  
Details | This request header is used when you want to encrypt a specific object with a [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys). When you do so, the header appears in the response and includes the key version as part of the returned value.  
  
#### x-goog-expiration

A response header that specifies when the accessed object will be deleted, per the lifecycle configuration.

Valid Values | A date and time represented in conventional HTTP format.  
---|---  
Example | `x-goog-expiration: Tue, 25 June 2013 00:00:00 GMT`  
Details | This response header is only returned for objects in a bucket with lifecycle management enabled if certain conditions are met. For more information, see [object lifecycle behavior](https://docs.cloud.google.com/storage/docs/lifecycle#expirationtime).  
  
#### x-goog-generation

A response header that indicates which version of the object data you are accessing.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `x-goog-generation: 1360044097835000`  
Details | Whenever an object is created or replaced, Cloud Storage automatically assigns a generation to it. The generation changes whenever object data is replaced. However, there is no defined relationship between the generations on different objects. For more information, see [generation and metageneration numbers](https://docs.cloud.google.com/storage/docs/metadata#generation-number).  
  
#### x-goog-if-generation-match

A request header that specifies the corresponding request is only allowed if the `x-goog-generation` of the object matches the value of this header.

Valid Values | Zero or any positive number (64 bit value)  
---|---  
Example | `x-goog-if-generation-match: 1360044097835000`  
Details | If the object generation matches the `x-goog-if-generation-match` header, the request will be completed successfully and Cloud Storage returns a `HTTP 200 OK` status. If the generation does not match, Cloud Storage returns a `HTTP 412 Precondition Failed` error code. If you set the `x-goog-if-generation-match` header to 0, Cloud Storage only performs the specified request if the object does not currently exist. For example, you can perform a PUT request to create a new object with a `x-goog-if-generation-match`, and the object will only get created if it doesn't already exist as a live version. If the object exists, the request is aborted. For more information, see [Request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions).  
  
#### x-goog-if-metageneration-match

A request header that specifies the corresponding request is only allowed if the `x-goog-metageneration` of the object or bucket matches the value of this header.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `x-goog-if-metageneration-match: 4`  
Details | If the metageneration of the requested resource matches the `x-goog-if-metageneration-match` header, the request proceeds as it normally would. If the metageneration does not match, Cloud Storage returns a `HTTP 412 Precondition Failed` error code. For object requests, this header should only be used in conjunction with x-goog-if-generation-match to validate that metadata updates are performed against the generation of the object you are planning to update and hence allows you to perform read-modify-write operations safely. For more information, see [Request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions).  
  
#### x-goog-interop-list-objects-format

A request header that enables an interoperability fix to the GET bucket response.

Valid Values | `enabled` | `disabled`.  
---|---  
Example | `x-goog-interop-list-objects-format: enabled`  
Details | Only use with the `versions` query parameter. Default is `disabled`. If you specify `enabled`, an interoperable set of tags will be used. If you specify `disabled`, the legacy set of tags will be used. |  | `enabled` interoperable tag | `disabled` legacy tag  
---|---|---  
Root XML tag | `<ListVersionsResult>` | `<ListBucketResult>`  
Key marker tag | `<NextKeyMarker>` | `<NextMarker>`  
Version Id marker tag | `<NextVersionIdMarker>` | `<NextGenerationMarker>`  
Version id tag | `<VersionId>` | `<Generation>`  
  
#### x-goog-metadata-directive

A request header that specifies metadata handling during a copy operation.

Note that object ACLs, when present, are never copied. If applicable, the new object receives ACLs specified in the `x-goog-acl` request header or the default object ACLs set for the bucket that contains the new object.

Valid Values | `COPY` | `REPLACE`  
---|---  
Example | `x-goog-metadata-directive: REPLACE`  
Details | Only used with the `x-goog-copy-source` request header. Default value is `COPY`. If you specify `COPY`, the metadata of the source object is applied to the newly-created object. If you specify `REPLACE`, the operation applies the metadata provided in the request to the newly-created object. When copying an object such it rewrites the source object, you must include `x-goog-metadata-directive: REPLACE`. The header is optional in all other cases.  
  
#### x-goog-metageneration

A response header that indicates which version of the object metadata you are accessing.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `x-goog-metageneration: 1`  
Details | Whenever an object is created or replaced, Cloud Storage automatically assigns a metageneration of 1. The metageneration increases whenever object metadata is updated (ACL update, or other metadata updates). This means that a larger metageneration always implies a newer version of the object metadata. However, there is no defined relationship between different generations on different objects, nor even different generations of the same object. Each generation of the object has its own metageneration version that only pertains to its generation. For more information, see [generation and metageneration numbers](https://docs.cloud.google.com/storage/docs/metadata#generation-number).  
  
#### x-goog-hash

A request and response header for expressing an object's MD5 and/or CRC32C base64-encoded checksums. As a request header for upload requests, the supplied hashes are validated against the values calculated by Cloud Storage.

Valid Values | Either `md5=BASE64_ENCODED_MD5` or `crc32c=BASE64_ENCODED_CRC32C`. Specify CRC32c values in big-endian byte order. Also, note that [HTTP](https://www.ietf.org/rfc/rfc7231.txt) considers comma separated header values as equivalent to separate headers with identical keys.  
---|---  
Examples | `x-goog-hash: crc32c=n03x6A==`  
`x-goog-hash: md5=Ojk9c3dhfxgoKVVHYwFbHQ==`  
`x-goog-hash: crc32c=n03x6A==,md5=Ojk9c3dhfxgoKVVHYwFbHQ==`  
Details | Cloud Storage stores MD5 hashes for all non-composite objects. CRC32Cs are available for all objects.  
  
#### x-goog-meta-KEY

A request and response header that lets you define [custom metadata](https://docs.cloud.google.com/storage/docs/metadata#custom-metadata) for an object.

Valid Values | Any valid header name and value, with a maximum combined size of 8 KiB.  
---|---  
Example | `x-goog-meta-reviewer: jane`  
Details | To use this header you append your custom header name to the `x-goog-meta-` prefix and then add the header and its associated value to your PUT or POST request. For example, if your objects are associated with various projects, you can add the project-specific information to your object metadata by creating several request headers, such as: `x-goog-meta-project-name`, `x-goog-meta-project-number`, and `x-goog-meta-project-manager`. You could then set a value for these request headers during a PUT or POST request as shown in the following example: 
    
    
    PUT /kitten.jpg HTTP/1.1
    Host: my-bucket.storage.googleapis.com
    Date: Wed, 17 Jun 2020 11:11:11 GMT
    Content-Type: image/jpg
    Content-Length: 554
    Authorization: Bearer 1/zVNpoQNsOSxZKqOZgckhpQ
    x-goog-meta-project-name: Sales Projections
    x-goog-meta-project-number: 878973
    x-goog-meta-project-manager: W. Loman
        

`x-goog-meta-` headers are stored with an object and are always returned in a response header when you do a GET or HEAD request on an object.  
  
#### x-goog-object-lock-mode

A request and response header for the mode associated with an object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock).

Valid Values | `GOVERNANCE` or `COMPLIANCE`  
---|---  
Example | `x-goog-object-lock-mode: COMPLIANCE`  
Details | This header can be included in requests that upload, copy, or compose an object. The value you specify in the header is stored as part of the object's metadata. A value of `GOVERNANCE` corresponds to the object's retention configuration being unlocked and a value of `COMPLIANCE` corresponds to the object's retention configuration being locked. If this header is specified in a request, the request must also include the `x-goog-object-lock-retain-until-date` header. This header gets returned as part of the response when you make a HEAD request or object download GET request if the requested object has a retention configuration. For more information, see [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock).  
  
#### x-goog-object-lock-retain-until-date

A request and response header indicating the time until which an object subject to a [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) remains immutable.

Valid Values | A date and time represented in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format.  
---|---  
Example | `x-goog-object-lock-retain-until-date: 2028-04-12T23:20:50.52Z`  
Details | This header can be included in requests that upload, copy, or compose an object. The value you specify in the header is stored as part of the object's metadata and indicates the earliest point in time that the object can be deleted or replaced. If this header is specified in a request, the request must also include the `x-goog-object-lock-mode` header. This header gets returned as part of the response when you make a HEAD request or object download GET request if the requested object has a retention configuration. For more information, see [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock).  
  
#### x-goog-project-id

A request header that specifies which project you are working on.

Valid Values | Any valid project number or name.  
---|---  
Examples | `x-goog-project-id: 000111222333`  
`x-goog-project-id: my-project-name`  
`x-goog-project-id: example.com:my-apps-for-work-project-name`  
Details | This request header tells Cloud Storage which project to create a bucket in or which project to list buckets for. This header is optional for creating and listing buckets if you have [set a default project](https://docs.cloud.google.com/storage/docs/aws-simple-migration#defaultproj) for interoperable access.  
  
#### x-goog-resumable

A request header that initiates a resumable upload operation.

Valid Values | start  
---|---  
Example | `x-goog-resumable: start`  
Details | This request header notifies the Cloud Storage system that you want to initiate a resumable upload. The header can be used only with a POST Object request and can be used only for resumable uploads.  
  
#### x-goog-storage-class

A request and response header that indicates the storage class of an object.

Valid Values | `STANDARD`, `NEARLINE`, `COLDLINE`, `ARCHIVE`, `MULTI_REGIONAL`, `REGIONAL`  
---|---  
Example | `x-goog-storage-class: NEARLINE`  
Details | This header can be included in `PUT Object` and `POST Object` requests in order to set an object to a storage class besides the default storage class of the associated bucket. The header is included in all `GET Object` responses.  
  
#### x-goog-stored-content-encoding

A response header that indicates the content encoding of the object as stored in Cloud Storage, independent of any server-driven negotiation that might occur for individual requests for the object.

Valid Values | The content-encoding specified in the stored object's metadata or `identity`.  
---|---  
Example | `x-goog-stored-content-encoding: gzip`  
Details | If the object has no stored metadata value for `content-encoding`, then the value of this header is `identity`.  
  
#### x-goog-stored-content-length

A response header that indicates the content length (in bytes) of the object as stored in Cloud Storage, independent of any server-driven negotiation that might occur for individual requests for the object.

Valid Values | Any byte value of zero or greater.  
---|---  
Example | `x-goog-stored-content-length: 350`  
Details | None  
  
#### x-goog-user-project

A request header that specifies a user project to bill for access charges associated with the request.

Valid Values | The [Project ID](https://docs.cloud.google.com/docs/overview#projects) for an existing Google Cloud project  
---|---  
Example | `x-goog-user-project: my-project`  
Details | The project specified in the header is billed for charges associated with the request. This header is used, for example, when making requests to buckets that have [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled.  
  
#### x-guploader-uploadid

A response header returned for Cloud Storage requests.

Valid Values | A string of characters.  
---|---  
Example | `x-guploader-uploadid: ADPycdvYczN-TgGGp1mvqlCLVKg2m0Cp9niWTV2kc8MLJG6W6Xw7aPMYj1YU8Pxskb5C9lUM8hVEtBG6DubMif3xhXkgTpfhpg`  
Details | The `x-guploader-uploadid` header is a unique identifier provided in Cloud Storage responses. This value can be helpful when troubleshooting with Google Cloud support.  
  
## Query string parameters

In the examples of query string parameters described in this section, the URIs are not shown but are assumed to be relative to `storage.googleapis.com`. As described in [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints), you can also specify the bucket name as part of the hostname, for example, `BUCKET-NAME.storage.googleapis.com`. If you are specifying the bucket as part of the hostname, then don't include the bucket name as part of the URI path. For example, the following are equivalent for getting the ACL of an object:

  * `https://storage.googleapis.com/BUCKET-NAME/object-name?acl`
  * `https://BUCKET-NAME.storage.googleapis.com/object-name?acl`



#### AccessKeyId

A query string parameter that enables you to identify which [HMAC key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) you want to update or delete.

Valid Values | An access ID associated with an HMAC key.  
---|---  
Example | `/?Action=UpdateAccessKey&AccessKeyId=GOOG1EXAMPLE&Status=Inactive`  
`/?Action=DeleteAccessKey&AccessKeyId=GOOG1EXAMPLE`  
Details | The `AccessKeyId` query string parameter allows you to specify which HMAC key you are updating or deleting. You must use `AccessKeyId` in conjunction with the `Action` query parameter. For information on how to retrieve the access ID for your HMAC key, see [Getting HMAC key information](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys#list).  
  
#### acl

A query string parameter that enables you to retrieve or change the access control list for a bucket or object.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?acl`  
`/BUCKET_NAME/OBJECT_NAME?acl`  
Details | Optional for the following requests: PUT Bucket, PUT Object, GET Bucket, GET Object. If sending a PUT request, you must include an XML document in the request body that specifies the ACLs you want to apply. You cannot use any additional subresources with this query parameter.  
  
#### Action

A query string parameter that enables you to identify which [HMAC key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) operation to perform.

Valid Values | `ListAccessKeys`, `CreateAccessKey`, `UpdateAccessKey`, `DeleteAccessKey`  
---|---  
Example | `/?Action=ListAccessKeys`  
Details | The `Action` query string parameter allows you to specify which HMAC key operation to perform: [`list`](https://docs.cloud.google.com/storage/docs/xml-api/get-hmac-list), [`create`](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-create), [`update`](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-update), or [`delete`](https://docs.cloud.google.com/storage/docs/xml-api/post-hmac-delete).  
  
#### billing

A query string parameter that allows you to enable, disable, or check the status of the [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) feature for a bucket.

Valid Values | Within the request body: `Enabled`, `Disabled`.  
---|---  
Example | `/BUCKET_NAME?billing`  
Details | Optional for the following requests: `GET Bucket`, `PUT Bucket`. When used in a `GET Bucket` request, the current status of the Requester Pays feature is returned in the response body. When used in a `PUT Bucket` request, the request body should contain a `<BillingConfiguration>` element that specifies whether to enable or disable the feature. You cannot use any additional subresources with this query parameter. For more information on setting the Requester Pays feature using the XML API, see [Set Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata).  
  
#### compose

A query string parameter that enables you to compose a sequence of existing objects into a new composite object (used only with the XML API).

Valid Values | none  
---|---  
Example | `/BUCKET_NAME/OBJECT_NAME?compose`  
Details | Optional for [PUT Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-compose) requests. A ComposeRequest XML document must be supplied in the request body. You cannot use any additional subresources with this query parameter.  
  
#### continuation-token

A token that indicates where you want a list of objects to start.

Valid Values | A `NextContinuationToken` value provided in the response body of a previous listing request.  
---|---  
Example | `?continuation-token=CglibHViLmdvc2g=`  
Details | When using `continuation-token`, the request must also include `list-type=2` as a query string parameter. The `continuation-token` is an encoded field that marks the name and generation of the last object returned in a previous list request. The list of objects returned in the current request are those that are lexicographically greater than the object represented by `continuation-token`.  
  
#### cors

A query string parameter that enables you to retrieve or change the Cross-Origin Resource Sharing (CORS) for a bucket.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?cors`  
Details | Optional for the following requests: PUT Bucket, GET Bucket. If sending a PUT request, you must include an XML document in the request body that specifies the CORS you want to apply. You cannot use any additional subresources with this query parameter.  
  
#### customPlacementConfig

A query string parameter that lets you set or retrieve the regions that make up a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr). If the bucket was created as a region, multi-region, or predefined dual-region, the returned custom placement configuration is empty.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?customPlacementConfig`  
Details | Optional for GET Bucket requests. Required for PUT Bucket requests for configurable dual-regions. If sending a PUT request, you must include an XML document in the request body that specifies the regions you want to use.  
  
#### defaultObjectAcl

A query string parameter that enables you to retrieve or change the default object access control list for a bucket.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?defaultObjectAcl`  
Details | Optional for PUT Bucket and GET Bucket requests. If sending a PUT request, you must include an XML document in the request body that specifies the ACL that applies by default to new objects added to the bucket. You cannot use any additional subresources with this query parameter. See [Setting default object ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#defaultobjects) for more information.  
  
#### delete

A query string parameter used with a `POST` request to delete multiple objects in a single operation.

Valid Values | none  
---|---  
Example | `POST /?delete HTTP/1.1`  
Details | Required to delete multiple objects. When you include this parameter in a `POST` request to the root of a bucket, you must provide an XML document in the request body that specifies the objects you want to delete. For more information, see [Delete multiple objects](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket).  
  
#### delimiter

A character or group of characters that is used to restrict a list of objects or multipart uploads during a GET Bucket request.

Valid Values | Any Unicode character or characters.  
---|---  
Example | `/?delimiter=/`  
Details | The `delimiter` simplifies an objects or multipart uploads list for objects that use a directory-like naming scheme.

  * When specified in an object listing, objects whose names don't contain the delimiter are returned as they normally would be in the `Contents` elements of the response. If an object name contains the delimiter, the portion of the object name up to and including the first instance of the delimiter appears in a `CommonPrefixes` element of the response.
  * When specified in a multipart upload listing, multipart uploads associated with objects whose names don't contain the delimiter are returned as they normally would be in the `Upload` elements of the response. If an object name contains the delimiter, the portion of the object name up to and including the first instance of the delimiter appears in a `CommonPrefixes` element of the response, and no multipart uploads associated with the object are returned in the listing.

You can use a `delimiter` in conjunction with a `prefix` parameter. In this case, the `prefix` limits results only to objects whose name matches `prefix`. The `delimiter` is usually set to `/`, but it can be any sequence of characters. For an example of how to use a `delimiter`, see the [delimiter example](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list#delimiter-example).  
  
#### encoding-type

A query string parameter to URL-encode object names in responses to object listing requests.

Valid Values | `url`  
---|---  
Example | `/bucket?encoding-type=url`  
Details | Optional when [listing objects](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list) in a bucket. When included in the request, returned object names are URL-encoded. This is useful if any of your object names include Unicode characters that XML 1.0 cannot parse.  
  
#### encryption

A query string parameter that enables you to retrieve an object's encryption information.

Valid Values | none  
---|---  
Example | `/object?encryption`  
Details | Optional for [GET Object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-encryption) requests. When the queried object is encrypted by a customer-supplied encryption key, the encryption algorithm and the key's SHA-256 are returned in an `Encryption` element. When the queried object is encrypted by a customer-managed encryption key, the Cloud Key Management Service key resource is returned in an `Encryption` element. In all other cases, an empty `Encryption` element is returned. You cannot use any additional subresources with this query parameter.  
  
#### encryptionConfig

A query string parameter that enables you to set or retrieve the encryption settings for a bucket.

Valid Values | none  
---|---  
Example | `/bucket?encryptionConfig`  
Details |  Optional for [GET Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata) requests. The response includes an `EncryptionConfiguration` element that lists which encryption methods are allowed or restricted for creating new objects in the bucket. If the bucket has a default customer-managed encryption key set on it, the name of the Cloud Key Management Service key resource is also returned. Optional for [PUT Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) requests. In the request body, provide an `EncryptionConfiguration` element that specifies which encryption methods are allowed or restricted for creating new objects in the bucket. You can also set the default customer-managed encryption key for the bucket by providing a Cloud KMS key resource in the request body. If the request includes an empty `EncryptionConfiguration` element, all encryption methods are allowed and any existing default key is removed from the bucket.  
  
#### fetch-owner

A boolean used in object listing requests to indicate if object owner information can be included in the response.

Valid Values | `true` or `false`  
---|---  
Example | `?fetch-owner=true`  
Details | When using `fetch-owner`, the request must also include `list-type=2` as a query string parameter. The default value for `fetch-owner` is `false`. If the bucket used in the object listing request has [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) enabled, `fetch-owner=true` has no effect, because no `Owner` values are set on objects in the bucket.  
  
#### generation

A value that indicates which generation of the object to fetch.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `?generation=1360887759327000`  
Details | The `generation` query string parameter allows you to specify which version of the object to operate on.  
  
#### generation-marker

A value that indicates the generation number at which you want a list of objects to start.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `?generation-marker=1360887759327000`  
Details | When using `generation-marker`, the request cannot include `list-type=2` as a query string parameter. The `generation-marker` query string parameter is a starting point for paged listings on versioned buckets. Must be used in conjunction with `marker`, in order to fully specify the object and generation of where to start the listing after. Any object versions with greater than the specified `generation-marker` (including the live version if it has a greater generation) are returned in the list of objects, as are objects that are lexicographically greater than the `marker`.  
  
#### key-marker

A string that indicates where you want a list of objects or ongoing multipart uploads to start.

Valid Values | Any string.  
---|---  
Example | `?uploads&key-marker=myobject.jpeg`  
Details | When listing multipart uploads, the `key-marker` query string parameter is a string of Unicode characters that specifies which object you want a list of ongoing multipart uploads to begin after. The list of multipart uploads returned are those associated with objects that are lexicographically greater than `key-marker`. When listing objects, `key-marker` is interchangeable with the `marker` query parameter.  
  
#### lifecycle

A query string parameter that enables you to retrieve or change the [lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) policies for a bucket.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?lifecycle`  
Details | Optional for the following requests: PUT Bucket, GET Bucket. If sending a PUT request, you must include an XML document in the request body that specifies the [lifecycle configuration](https://docs.cloud.google.com/storage/docs/lifecycle#configuration). You cannot use any additional subresources with this query parameter.  
  
#### list-type

An indicator of which version of object listing your request is using.

Valid Values | `1` or `2`  
---|---  
Example | `?list-type=2`  
Details | The XML API has two formats for listing objects in a bucket. `list-type` indicates which format is being used in the current request, as well as how the response should be handled. The default value for `list-type` is `1`. For more information, see the [List objects reference documentation](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list).  
  
#### location

A query string parameter that enables you to retrieve the [location](https://docs.cloud.google.com/storage/docs/locations) constraint for a bucket.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?location`  
Details | Optional for the following requests: GET Bucket. Returned values can include the name of a region, predefined dual-region, or multi-region. For buckets located in [configurable dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr), additional location information can be obtained by making a request that uses the `?customPlacementConfig` query parameter.  
  
#### logging

A query string parameter that enables you to retrieve or change the [logging configuration](https://docs.cloud.google.com/storage/docs/access-logs) for a bucket.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?logging`  
Details | Optional for the following requests: PUT Bucket, GET Bucket. If sending a PUT request, you must include an XML document in the request body that specifies the logging configuration. You cannot use any additional subresources with this query parameter.  
  
#### marker

A string that indicates where you want a list of objects to start.

Valid Values | Any string.  
---|---  
Example | `?marker=test`  
Details | When using `marker`, the request cannot include `list-type=2` as a query string parameter. The `marker` query string parameter is a string of Unicode characters that specifies which object you want a list of objects to begin after. The list of objects returned are those that are lexicographically greater than the `marker`.  
  
#### Marker

A page token that enables you to list subsequent pages of [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

Valid Values | A string provided in a previous `list` response if `IsTruncated` is `true`.  
---|---  
Example | `?Action=ListAccessKeys&Marker=AERPALERN/NEXT/TOKEN`  
Details | The `Marker` query string parameter is a continuation token, used to page through large result sets when listing HMAC keys for a given project. If `IsTruncated` is `true` in a previous `list`response, use the provided `Marker` token in subsequent `list` requests until `IsTruncated` is `false`. You must use `Marker` in conjunction with the `Action` query parameter. For more information, see [GET HMAC Key](https://docs.cloud.google.com/storage/docs/xml-api/get-hmac-list).  
  
#### max-keys

An integer that limits the number of objects returned in a single result "page".

Valid Values | Any number greater than 0.  
---|---  
Example | `?max-keys=100`  
Details | The `max-keys` query string parameter is an integer that specifies the maximum number of objects you want returned in a list of objects. If a request can return more objects than `max-keys` allows, the `IsTruncated` response element contains a `True` value. The recommended upper value for `max-keys` is 1000 objects in a single response.  
  
#### max-parts

A number that limits how many parts of a multipart upload can be returned in the response.

Valid Values | An integer greater than or equal to 0.  
---|---  
Example | `?uploadId=VALID_ID&max-parts=10`  
Details | The `max-parts` query string parameter is an integer that specifies the maximum number of parts you want returned in a request to [list the uploaded parts of a multipart upload](https://docs.cloud.google.com/storage/docs/xml-api/get-object-multipart). If `max-parts=0`, then the response omits all `Part` elements. If a request can return more parts than `max-parts` allows, the `IsTruncated` response element contains a `True` value.  
  
#### max-uploads

A number that limits how many multipart uploads are returned in the response.

Valid Values | An integer greater than or equal to 0  
---|---  
Example | `?uploads&max-uploads=10`  
Details | The `max-uploads` query string parameter is an integer that specifies the maximum number of multipart uploads you want returned in a request to [list the ongoing multipart uploads in a bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-uploads). If `max-uploads=0`, then the response omits all `Upload` elements. If a request can return more uploads than `max-uploads` allows, the `IsTruncated` response element contains a `True` value.  
  
#### MaxItems

An integer that limits the number of [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) returned in a single result page.

Valid Values | Any number greater than 0.  
---|---  
Example | `?Action=ListAccessKeys&MaxItems=100`  
Details | The `MaxItems` query string parameter is an integer that specifies the maximum number of HMAC keys returned in a single result page. If a request can return more keys than `MaxItems` allows, the `IsTruncated` response element contains a `true` value. You must use `MaxItems` in conjunction with the `Action` query parameter. The service may return fewer results than the specified maximum.  
  
#### object-lock

A query string parameter that enables you to retrieve the object retention configuration of a bucket.

Valid Values | none  
---|---  
Example | `?object-lock`  
Details | Optional for GET Bucket requests. If object retention is not enabled for the bucket, a request using this query string parameter fails with a 404 response. You cannot use any additional subresources with this parameter.  
  
#### part-number-marker

A number that indicates where you want a list of multipart upload parts to start.

Valid Values | An integer greater than or equal to 0  
---|---  
Example | `?uploadId=VALID_ID&part-number-marker=10`  
Details | The `part-number-marker` query string parameter is an integer that specifies which part you want a [list of parts](https://docs.cloud.google.com/storage/docs/xml-api/get-object-multipart) to begin after. The list of parts returned are those that are greater than the `part-number-marker`.  
  
#### partNumber

A number that defines a piece of an [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads).

Valid Values | A integer greater than 0 and up to 10,000.  
---|---  
Example | ?uploadId=VALID_ID&partNumber=1  
Details | The `partNumber` query string parameter is used in a [`PUT Object` request](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart) for a multipart upload. The `partNumber` defines where the current part is ordered in the overall object.  
  
#### prefix

A string that restricts a list of objects or multipart uploads based on the prefix of the object's name.

Valid Values | Any valid prefix.  
---|---  
Example | ?prefix=/europe/france  
Details | The `prefix` query string parameter is a string of Unicode characters that restricts the listing.

  * For object listing, `prefix` restricts the results to objects whose names begin with the specified `prefix` value.
  * For multipart upload listing, `prefix` restricts the results to multipart uploads whose associated object names begin with the specified `prefix` value.

You can use the `prefix` query string parameter in conjunction with the `delimiter` query string parameter to create a smaller subset of results.  
  
#### response-content-disposition

A query string parameter that allows content-disposition to be overridden for authenticated GET requests.

Valid Values | URL-encoded header to return instead of the content-disposition of the underlying object.  
---|---  
Example | `?response-content-disposition=attachment%3B%20filename%3D%22foo%22`  
Details | Allows authenticated GET requests to override the content-disposition returned in the headers. For more information, see the [specification](https://datatracker.ietf.org/doc/html/rfc6266).  
  
#### response-content-type

A query string parameter that allows content-type to be overridden for authenticated GET requests.

Valid Values | URL-encoded header to return instead of the content-type of the underlying object.  
---|---  
Example | `?response-content-type=text%2Fhtml`  
Details | Allows authenticated GET requests to override the content-type returned in the headers. For more information, see the [specification](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5).  
  
#### retention

A query string parameter that allows you to set, modify, or check the status of an existing object's [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock).

Valid Values | None  
---|---  
Example | `/OBJECT_NAME?retention`  
Details | Optional for the following requests: `GET Object`, `PUT Object`. When used in a `GET Object` request, the object's current retention configuration is returned in the response body if it exists, and the requests fails with a `404 Not Found` response otherwise. When used in a `PUT Object` request, you must include an XML document in the request body that specifies the [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock).  
  
#### start-after

A string that indicates where you want a list of objects to start.

Valid Values | Any string.  
---|---  
Example | `?start-after=test`  
Details | When using `start-after`, the request must also include `list-type=2` as a query string parameter. The `start-after` query string parameter is a string of Unicode characters that specifies which object you want a list of objects to begin after. The list of objects returned are those that are lexicographically greater than the `start-after`. If you include `continuation-token` in your request as well, `start-after` is ignored.  
  
#### Status

A query string parameter that allows you to enable or disable an [HMAC key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

Valid Values | `Active`, `Inactive`  
---|---  
Example | `?Action=UpdateAccessKey&AccessKeyId=GOOG1EXAMPLE&Status=Inactive`  
Details | The `Status` query string parameter allows you to change the status of an HMAC key between `Active` and `Inactive`. You must use `Status` in conjunction with the `Action` and `AccessKeyId` query parameters.  
  
#### storageClass

A query string parameter that enables you to set or retrieve the default storage class of a bucket.

Valid Values | Within the request body: `STANDARD`, `NEARLINE`, `ARCHIVE`, `COLDLINE`, `MULTI_REGIONAL`, `REGIONAL`, `DURABLE_REDUCED_AVAILABILITY`  
---|---  
Example | `/BUCKET_NAME?storageClass`  
Details | Optional for the following requests: `GET Bucket`, `PUT Bucket`. When used in a `GET Bucket` request, the default storage class of the specified bucket is returned in the response body. When used in a `PUT Bucket` request, the request body should contain a `<StorageClass>` element that specifies the default storage class you want to assign to the bucket. For more information on setting the default storage class of a bucket using the XML API, see [Set Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata).  
  
#### tagging

A query string parameter that enables you to set or retrieve the [labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels) applied to a bucket.

Valid Values | Within the request body: A label, given as a `key:value` pair.  
---|---  
Example | `/BUCKET_NAME?tagging`  
Details | Optional for the following requests: `GET Bucket`, `PUT Bucket`. When used in a `GET Bucket` request, the labels applied to the specified bucket are returned in the response body. When used in a `PUT Bucket` request, the request body should contain a `<Tagging>` element that specifies the labels you want to apply to the bucket. For more information on applying labels using the XML API, see [Set Bucket Metadata](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata).  
  
#### upload_id

A query string parameter that specifies that upload ID for a resumable upload operation. The `upload_id` is part of the session URI, but you should save the entire session URI because it uniquely defines the request URI for subsequent resumable uploads operations. The session URI is obtained from the `Location` response header.

Valid Values | Any valid upload ID.  
---|---  
Example | `/?upload_id=tvA0ExBntDaOKdxL46u1NkHxNb...B2Uowrot`  
Details | An upload ID expires after one week. We recommend that you start a resumable upload as soon as you obtain the upload ID, and that you resume an interrupted upload shortly after the interruption occurred. If you use an expired upload ID in a request, you will receive a 404 Not Found status code. In this case, you will have to re-initiate the resumable upload, obtain a new upload ID, and start the upload from the beginning using the new upload ID. The upload ID is bound to the location it was created, so if you create in one location and use it in another location, your performance will suffer. The upload ID is a Bearer token, meaning possession of this token acts as an authenticator. Thus, you should be careful not to leak upload IDs.  
  
#### upload-id-marker

A value that indicates the upload at which you want a list of multipart uploads to start.

Valid Values | A `NextUploadIdMarker` returned in a previous listing request.  
---|---  
Example | `?uploads&key-marker=myobject.jpeg&upload-id-marker=VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA`  
Details | The `upload-id-marker` query string parameter marks the starting point for a list of ongoing multipart uploads in a bucket. In order to fully specify an object and upload, `upload-id-marker` can only be used in conjunction with `key-marker`. Any ongoing multipart uploads for `key-marker` with an `upload-id` greater than `upload-id-marker` are returned in the list, and any ongoing multipart uploads for objects that are lexicographically greater than `key-marker` are also returned in the list.  
  
#### uploadId

A string that identifies the multipart upload the request applies to.

Valid Values | An `UploadId` returned in a request to initiate a multipart upload.  
---|---  
Example | `/?uploadId=VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA`  
Details | The `uploadId` query string parameter is used to identify a multipart upload after you have [initiated the upload](https://docs.cloud.google.com/storage/docs/xml-api/post-object-multipart). For example, you use an `uploadId` when making a `PUT Object` request to [upload a part](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart) for an object. A multipart upload ID differs from a resumable upload ID in several important ways:

  * A multipart upload ID never expires. It remains valid until you either abort the upload or complete the upload.
  * A multipart upload ID is not an authenticator. You must still include valid authorization in requests that use a multipart upload ID.

  
  
#### uploads

A query string parameter used to [initiate an XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) or [retrieve a list of multipart uploads](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-uploads) in progress for a bucket.

Valid Values | none  
---|---  
Example | `/OBJECT_NAME?uploads`  
Details | When used in a `POST Object` request, the request initiates an XML multipart upload and returns an upload ID, which you use in subsequent `PUT` requests to upload the data. When used in a `GET Bucket` request, the request returns a list of multipart uploads in the bucket that have been initiated, but that have not yet been completed or aborted.  
  
#### UserName

A query string parameter that enables you to identify the service account for which you want to create, update, or list an [HMAC key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys).

Valid Values | A valid service account email address.  
---|---  
Example | `/?Action=CreateAccessKey&UserName=serviceAccount@proj.iam.gserviceaccount.com`  
Details | `UserName` is required for creating an HMAC key and optional for updating a key or listing keys associated with a project. You must use `UserName` in conjunction with the `Action` query parameter.  
  
#### userProject

A query string parameter that specifies a project ID to bill for access charges associated with the request.

Valid Values | Any valid project ID.  
---|---  
Example | `?userProject=example-project`  
Details | The project specified in this parameter is billed for charges associated with the request. `userProject` is used, for example, when making requests to buckets that have [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled. Generally, XML requests that require a project ID should supply one in the `x-goog-user-project` header instead of the `userProject` parameter.  
  
#### version-id-marker

A value that indicates the generation number at which you want a list of objects to start.

Valid Values | Any positive number (64 bit value)  
---|---  
Example | `?version-id-marker=1360887759327000`  
Details | When using `version-id-marker`, the request cannot include `list-type=2` as a query string parameter. The `version-id-marker` query string parameter is a starting point for paged listings on versioned buckets. Must be used in conjunction with `key-marker`, in order to fully specify the object and generation of where to start the listing after. Any object versions with greater than the specified `version-id-marker` (including the live version if it has a greater generation) are returned in the list of objects, as are objects that are lexicographically greater than the `key-marker`.  
  
#### versioning

A query string parameter that enables you to retrieve or change versioning configuration of a bucket.

Valid Values | none  
---|---  
Example | `/OBJECT_NAME?versioning`  
Details | Optional for the following requests: PUT Bucket, GET Bucket. If sending a PUT request, you must include an XML document in the request body that specifies the Versioning Configuration you want to apply. You cannot use any additional subresources with this query parameter.  
  
#### versions

A query string parameter that enables you to retrieve all generation of objects in a versioned bucket.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?versions=True`  
Details | Optional for the following requests: GET Bucket.  
  
#### websiteConfig

A query string parameter that enables you to retrieve or change a bucket's website configuration.

Valid Values | none  
---|---  
Example | `/BUCKET_NAME?websiteConfig`  
Details | Optional for the following requests: PUT Bucket, GET Bucket. If sending a PUT request, you must include an XML document in the request body that specifies the Website Configuration you want to apply. You cannot use any additional subresources with this query parameter.  
  
#### X-Goog-Algorithm

A query string parameter to determine the V4 signed URL algorithm.

Valid Values | `GOOG4-RSA-SHA256`  
`GOOG4-HMAC-SHA256`  
`AWS4-HMAC-SHA256`  
---|---  
Details | Used specifically for V4 signed requests such as [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).  
  
#### X-Goog-Credential

A query string parameter to determine the credential type used.

Valid Values | `Service_Account_Email/Date/Region/goog4_request`  
`Google_HMAC_Access_Key_ID/Date/Region/goog4_request`  
`AWS_HMAC_Access_Key_ID/Date/Region/aws4_request`  
---|---  
Example | Using a service account: `example%40example-project.iam.gserviceaccount.com%2F20181026%2Fus-central1%2Fstorage%2Fgoog4_request`  
Using HMAC: `GOOGTS7C7FUP3AIRVJTE2BCD%2F20181026%2Fus-central1%2Fstorage%2Fgoog4_request`  
Details | Used specifically for V4 signed requests such as [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).  
  
#### X-Goog-Custom-Audit-KEY

A query string parameter to pass custom metadata to be included in audit logs.

Valid Values | Any entry in the form `x-goog-custom-audit-KEY=VALUE`  
---|---  
Example | x-goog-custom-audit-jobID=Job123  
Details | Each `KEY` can contain up to 64 characters, while each `VALUE` can contain up to 1,200 characters. Each `KEY` can only contain alphanumeric characters and dashes. Each request can contain up to 4 audit entries. [Add custom information to audit logs](https://docs.cloud.google.com/storage/docs/audit-logging#add-custom-metadata).  
  
#### X-Goog-Date (Query Parameter)

The date and time the signed URL became usable.

Valid Values | Any date that follows: YYYYMMDD'T'HHMMSS'Z'  
---|---  
Example | `?X-Goog-Date=20181026T181309Z`  
Details | Format used is the [ISO 8601 basic format](https://en.wikipedia.org/wiki/ISO_8601) YYYYMMDD'T'HHMMSS'Z'.  
  
#### X-Goog-Expires

A query string parameter to determine how long a V4 signed URL is active.

Valid Values | 1 second up to and including 604800 seconds  
---|---  
Example | `?X-Goog-Expires=900`  
Details | The length of time the signed URL remained valid, measured in seconds from the value in X-Goog-Date (Query Parameter). Maximum value is 7 days or 604800 seconds.  
  
#### X-Goog-SignedHeaders

A query string parameter to determine the headers signed in a V4 signed URL.

Valid Values | The only required header is **host**. Any header that is signed in a V4 signed URL signature should must be in this list.  
---|---  
Examples | `?X-Goog-SignedHeaders=host`  
`?X-Goog-SignedHeaders=host,x-goog-acl`  
Details | Headers that had to be included as part of any request that used the signed URL.  
  
#### X-Goog-Signature

A query string parameter with the value of a V4 signed URL signature.

Valid Values | Signature of the signed URL.  
---|---  
Example | `?X-Goog-Signature=247a2aa45f169edf4d187d54e7cc46e4731b1e6273242c4f4c39a1d2507a0e58706e25e3a85a7dbb891d62afa8496def8e260c1db863d9ace85ff0a184b894b117fe46d1225c82f2aa19efd52cf21d3e2022b3b868dcc1aca2741951ed5bf3bb25a34f5e9316a2841e8ff4c530b22ceaa1c5ce09c7cbb5732631510c20580e61723f5594de3aea497f195456a2ff2bdd0d13bad47289d8611b6f9cfeef0c46c91a455b94e90a66924f722292d21e24d31dcfb38ce0c0f353ffa5a9756fc2a9f2b40bc2113206a81e324fc4fd6823a29163fa845c8ae7eca1fcf6e5bb48b3200983c56c5ca81fffb151cca7402beddfc4a76b133447032ea7abedc098d2eb14a7`  
Details | The authentication string that allowed requests using this signed URL to access the designated resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
