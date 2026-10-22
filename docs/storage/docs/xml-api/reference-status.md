---
url: https://docs.cloud.google.com/storage/docs/xml-api/reference-status/
title: Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:55.499207+00:00
---

# Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/reference-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HTTP status and error codes for XML

The following document provides reference information about the error messages and status codes that are used in the Cloud Storage XML API. For error messages and status codes used by the Cloud Storage JSON API, see [this page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

## Error Response Format

Cloud Storage uses the standard HTTP error reporting format. Successful requests return HTTP status codes in the 2xx range. Failed requests return status codes in the 4xx and 5xx ranges. Requests that require a redirect returns status codes in the 3xx range. Error responses usually include an XML document in the response body, which contains information about the error.

The following is an example of an error response.
    
    
    HTTP/1.1 409 Conflict
    Content-Type: application/xml
    Content-Length: 182
    Date: Wed, 03 Mar 2010 00:22:00 GMT
    Expires: Wed, 03 Mar 2010 00:22:00 GMT
    Cache-Control: private, max-age=0
    
    
    
    <?xml version='1.0' encoding='utf-8'?>
    <Error>
      <Code>BucketNameUnavailable</Code>
      <Message>
        The requested bucket name is not available. The bucket namespace is shared by all users
        of the system. Please select a different name and try again.
      </Message>
    </Error>
    

The following table describes the elements that are in the response body:

Element | Description  
---|---  
`Error` | Container for the error information.  
`Code` | Error name.  
`Message` | Description of the error.  
  
## HTTP Status and Error Codes

The following are descriptions of the HTTP status and error codes that Cloud Storage uses.

### 301—Moved Permanently

Error Name | Description  
---|---  
PermanentRedirect | The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint.  
  
### 304—Not Modified

Error Name | Description  
---|---  
NotModified | The resource you requested has not been modified according to the condition you specified.  
  
### 307—Temporary Redirect

Error Name | Description  
---|---  
Redirect | Temporary redirect.  
TemporaryRedirect | You are being redirected to the bucket while DNS updates.  
  
### 308—Resume Incomplete

Error Name | Description  
---|---  
Resume Incomplete | Indicates an incomplete resumable upload and provides the range of bytes already received by Cloud Storage.  
  
### 400—Bad Request

Error Name | Description  
---|---  
AmbiguousGrantByEmailAddress | The e-mail address you provided is associated with more than one account.  
BadDigest | The `Content-MD5` or `x-goog-hash` you specified did not match what we received.  
CloudKmsBadKey | Bad Cloud KMS key.  
CloudKmsCannotChangeKeyName | Cloud KMS key name cannot be changed.  
CloudKmsDecryptionKeyNotFound | Resource's Cloud KMS decryption key not found.  
CloudKmsDisabledKey | Cloud KMS key is disabled, destroyed, or scheduled to be destroyed.  
CloudKmsEncryptionKeyNotFound | Cloud KMS encryption key not found.  
CloudKmsKeyLocationNotAllowed | Cloud KMS key location not allowed.  
CredentialsNotSupported | This request does not support credentials.  
CrcMismatch | The CRC32C you specified did not match what we computed.  
CustomerEncryptionAlgorithmIsInvalid | Missing an encryption algorithm, or the provided algorithm is not "AE256."  
CustomerEncryptionKeyFormatIsInvalid | Missing an encryption key, or it is not Base64 encoded, or it does not meet the required length of the encryption algorithm.  
CustomerEncryptionKeyIsIncorrect | The provided encryption key is incorrect.  
CustomerEncryptionKeySha256IsInvalid | Missing a SHA256 hash of the encryption key, or it is not Base64 encoded, or it does not match the encryption key.  
DotfulBucketNameNotUnderTld | The specified bucket contains a '.' but is not under a currently recognized top-level domain.  
EntityTooSmall | Your proposed upload is smaller than the minimum allowed object size.  
EntityTooLarge | Your proposed upload exceeds the maximum allowed object size.  
ExcessHeaderValues | Multiple HTTP header values where one was expected.  
ExpiredToken | The provided token has expired.  
IncompleteBody | You did not provide the number of bytes specified by the Content-Length HTTP header.  
IncorrectNumberOfFilesInPostRequest | POST requires exactly one file upload per request.  
IllegalEndpoint | Upload-only and download-only endpoints may only be used for uploading or downloading object, respectively.  
InlineDataTooLarge | Inline data exceeds the maximum allowed size.  
InvalidArgument | Invalid argument.  
InvalidAuthentication | The authentication header provided in the request is not supported or is invalid.  
InvalidBucketName | The specified bucket is not valid.  
InvalidComponentCount | Composite attempted with too many or too few components in the request.  
InvalidCrc | The CRC32c you specified was invalid.  
InvalidDigest | The Content-MD5 you specified was invalid.  
InvalidDotfulBucketName | The specified bucket contains a '.' but is not syntactically valid.  
InvalidHash | The [`x-goog-hash`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooghash) header you specified was invalid.  
InvalidLocationConstraint | The specified location constraint is not valid. You cannot specify locations with the Cloud Storage API.  
InvalidPart | One or more of the specified parts could not be found. The part might not have been uploaded, or the specified entity tag might not match the part's entity tag.  
InvalidPartOrder | The parts list given in the request to complete a multipart upload is invalid. The parts list must be in ascending order by part number.  
InvalidPolicyDocument | The content of the form does not meet the conditions specified in the policy document.  
InvalidStorageClass | The storage class you specified is not valid.  
InvalidLocationConstraintStorageClassCombination | The combination of location and [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) specified is not supported. For example, buckets in regions cannot use the `MULTI_REGIONAL` storage class, and buckets in multi-regions cannot use the `REGIONAL` storage class.  
InvalidObjectName | The specified object name is not valid.  
InvalidTargetBucketForLogging | The target bucket for logging does not exist, or does not grant write permission to the group "cloud-storage-analytics@google.com". See [setting up log delivery](https://docs.cloud.google.com/storage/docs/access-logs#delivery).  
InvalidToken | The provided token is malformed or otherwise invalid.  
InvalidURI | Couldn't parse the specified URI.  
KeyTooLong | Your object name is too long.  
MalformedACLError | The XML you provided was not well-formed or did not validate against our published schema.  
MalformedHeaderValue | An HTTP header value was malformed.  
MalformedPOSTRequest | The body of your POST request is not well-formed multipart/form-data.  
MalformedXML | This happens when the user sends a malformed XML (XML that doesn't conform to the published XSD) for the configuration.  
MaxMessageLengthExceeded | Your request was too big.  
MaxPostPreDataLengthExceededError | Your POST request fields preceding the upload file were too large.  
MetadataTooLarge | Your metadata headers exceed the maximum allowed metadata size.  
MissingRequestBodyError | This happens when the user sends an empty XML document as a request.  
MissingSecurityHeader | Your request was missing a required header.  
NoLoggingStatusForKey | There is no such thing as a logging status sub-resource for a key.  
NotImplemented | A header or query you provided requested a function that is not implemented.  
NoMd5Provided | MD5 is required for the requested operation but was not provided.  
RequestIsNotMultiPartContent | Bucket POST must be of the enclosure-type multipart/form-data.  
RequestTimeout | Your socket connection to the server was not read from or written to within the timeout period.  
ResourceIsEncryptedWithCustomerEncryptionKey | The resource is encrypted with a customer-supplied encryption key, but the request did not provide one.  
ResourceNotEncryptedWithCustomerEncryptionKey | The resource is not encrypted with a customer-supplied encryption key, but the request provided one.  
SecureConnectionRequired | A secure connection is required to process this request.  
TokenRefreshRequired | The provided token must be refreshed.  
UnexpectedContent | This request does not support content.  
UnresolvableGrantByEmailAddress | The e-mail address you provided does not match any account on record.  
UnsupportedAcl | The ACL you specified is not supported. For more information about the ACLs that Cloud Storage supports, see [Access Control](https://docs.cloud.google.com/storage/docs/access-control).  
UserKeyMustBeSpecified | The bucket POST must contain the specified field name. If it is specified, please check the order of the fields.  
UserProjectInvalid | The user project specified in the request is invalid, either because it is a malformed project id or because it refers to a non-existent project.  
UserProjectMissing | The requested bucket has Requester Pays enabled, the requester is not an owner of the bucket, and no user project was present in the request.  
ConditionalDeleteNotAllowed | The Cloud Storage multi-object delete API method doesn't support conditional deletes based on `ETag`, `Last-Modified`, or `Size`.  
  
### 401—Unauthorized

Error Name | Description  
---|---  
AccountProblem | Access to Google Cloud using this account is disabled or restricted. Contact your Organization Administrator for access.  
AuthenticationRequired | The requested access requires an authentication credential, but no credential was provided as part of the request. Retry the request with a valid credential.  
AuthenticationRequiredRequesterPays | Access to a Requester Pays bucket requires authentication.  
InvalidAuthentication | The authentication credential provided in the request has expired. Reauthenticate and retry the request with the refreshed credential.  
  
### 403—Forbidden

Error Name | Description  
---|---  
AccessDenied | Access denied. This applies to any object you don't have access to, regardless of whether or not the object actually exists. In a multi-object delete request, this error indicates that you lack permission to delete a specific object.  
AccountProblem | There is a problem with your user account that prevents the operation from completing successfully. One issue could be billing. Check [the billing page](https://console.cloud.google.com/billing) to see if you have a past due balance or if the credit card (or other payment mechanism) on your account is expired.  
AnotherUserOwnsDomain | The bucket you tried to create is a domain name owned by another user.  
BucketAlreadyExists | The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.  
CrossLocationLoggingProhibited | Cross location logging not allowed. A bucket in one location cannot log information to a bucket in another location.  
DomainVerificationRequired | The bucket you tried to create requires [domain ownership verification](https://docs.cloud.google.com/storage/docs/domain-name-verification).  
InsufficientQuota | The user does not have enough quota to complete this operation.  
InvalidAccessKeyId | The User Id you provided does not exist in our records.  
InvalidPayer | All access to this object has been disabled.  
InvalidSecurity | The provided security credentials are not valid.  
ObjectUnderActiveHold | Object replacement or deletion is not allowed due to an [active hold](https://docs.cloud.google.com/storage/docs/object-holds) on the object.  
RequestTimeTooSkewed | The difference between the request time and the server's time is too large. For a request that uses a signature in its `Authorization` header, the maximum difference in time allowed between the request and the backend system time is 15 minutes.  
RetentionPolicyNotMet | Object replacement or deletion is not allowed until the object meets the retention period set by the [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) on the bucket.  
SignatureDoesNotMatch | The request signature we calculated does not match the signature you provided. Check your Google secret and signing method.  
The requester is not authorized to use the project specified in the `x-goog-user-project` header of their request. The requester must have the `serviceusage.services.use` permission for the specified project.  
UserProjectAccountProblem | There is a problem with the project used in the request that prevents the operation from completing successfully. One issue could be billing. Check [the billing page](https://console.cloud.google.com/billing) to see if you have a past due balance or if the credit card (or other payment mechanism) on your account is expired. For project creation, [see the Projects page](https://console.cloud.google.com/project) in the Google Cloud console.  
  
### 404—Not Found

Error Name | Description  
---|---  
NoSuchBucket | The specified bucket does not exist.  
NoSuchKey | The specified object name does not exist.  
NoSuchUpload | The specified multipart upload does not exist. The upload ID might be invalid, or the multipart upload might have been aborted or completed.  
  
### 405—Method Not Allowed

Error Name | Description  
---|---  
AccessDenied | Access denied.  
MethodNotAllowed | The specified method is not allowed against this resource.  
  
### 408—Request Timeout

Error Name | Description  
---|---  
uploadBrokenConnection | The request timed out. Retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
  
### 409—Conflict

Error Name | Description  
---|---  
BucketAlreadyOwnedByYou | Your previous request to create the named bucket succeeded and you already own it.  
BucketNameUnavailable | The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again. This error can occur when you try to create a bucket name that already exists or you try to create a bucket name that does not meet the [bucket naming requirements.](https://docs.cloud.google.com/storage/docs/buckets#naming)  
BucketNotEmpty | The bucket you tried to delete is not empty.  
OperationAborted | A conflicting conditional operation is currently in progress against this resource. Please try again.  
RewriteTokenDestAlreadyFinalized | Attempt to call Rewrite with a RewriteToken for an already completed Rewrite operation.  
  
### 411—Length Required

Error Name | Description  
---|---  
MissingContentLength | You must provide the Content-Length HTTP header.  
  
### 412—Precondition Failed

Error Name | Description  
---|---  
PreconditionFailed | At least one of the pre-conditions you specified did not hold.  
  
### 413—Payload Too Large

Error Name | Description  
---|---  
EntityTooLarge | The [copy request](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy) took longer than 30 seconds to complete and involved an object larger than 2.5 GiB.  
  
### 416—Requested Range Not Satisfiable

Error Name | Description  
---|---  
InvalidRange | The requested range cannot be satisfied.  
  
### 429—Too Many Requests

Error Name | Description  
---|---  
CloudEkmNetworkingError | The Cloud Storage service agent encountered an external networking error when accessing the Cloud KMS in Cloud EKM. Retry later; if the issue persists, contact your external key manager.  
InsufficientQuota | The App Engine rate limit was exceeded. Retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
LroLimitExceeded | The number of running LROs of this type exceeds the limit. Cancel existing LROs or wait for them to complete and then retry.  
RateLimitExceeded | The Cloud Storage rate limit was exceeded. Retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
SlowDown | You are sending requests too frequently. For example, object updates have a limit of approximately 1 update/second. For additional information, see [Limits and quotas](https://docs.cloud.google.com/storage/quotas). Slow down the rate at which you send requests and retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
  
### 500—Internal Server Error

Error Name (if present) | Description  
---|---  
InternalError | We encountered an internal error. Retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
  
### 503—Service Unavailable

Error Name (if present) | Description  
---|---  
SlowDown | The service is temporarily unavailable. Retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
  
### 504—Gateway Timeout

Error Name | Description  
---|---  
N/A | The service is temporarily unable to reach another service. Retry using [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
