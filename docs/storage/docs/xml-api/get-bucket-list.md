---
url: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list/
title: List objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:56.445363+00:00
---

# List objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  List objects Stay organized with collections  Save and categorize content based on your preferences. 

To list the objects in a bucket you make a GET request that is scoped to a bucket. You can also use query string parameters to further scope the request. The request returns the list of objects in an XML document in the response body, and objects in the list are ordered lexicographically by name.

You must have bucket `READ` permission to get the list of objects that are in a bucket, and you must have bucket `FULL_CONTROL` permission to list a bucket's ACLs or CORS.

You can restrict and organize the list of objects returned in a GET Bucket request by using the `delimiter`, `max-keys`, and `prefix` query string parameters.

## Query string parameters

Parameter | Description | Required  
---|---|---  
`[continuation-token](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#continuationtoken)2` | An encoded representation of an object name and generation number, given in the `NextContinuationToken` element of a previous object listing response. Only objects whose names are lexicographically greater than the object represented by the `continuation-token` are returned in the list of objects. | No  
`[delimiter](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#delimiter)` | A character or multiple characters that can be used to simplify a list of objects that use a directory-like naming scheme. Can be used in conjunction with a `prefix`. | No  
`[encoding-type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#encodingtype)` | When set to `url`, object names are URL-encoded in the response. | No  
`[fetch-owner](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#fetchowner)2` | A lowercase boolean indicating whether or not to include `Owner` information for objects in the listing. | No  
`[generation-marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generationmarker)1` | The object generation after which you want to start listing objects. If you use `generation-marker`, you must also use `marker`. | No  
`[key-marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#keymarker)1` | The object name after which you want to start listing objects. Objects whose names are lexicographically greater than the `key-marker` are returned in the list of objects. | No  
`[list-type](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#listtype)` | An indicator of which version of object listing your request is using. The default value is `1`. | No  
`[marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#marker)1` | The object name after which you want to start listing objects. Objects whose names are lexicographically greater than the `marker` are returned in the list of objects. | No  
`[max-keys](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#maxkeys)` | The maximum number of objects to return in a single list object response. Note that fewer objects than `max-keys` may be returned so `IsTruncated` should always be checked. | No  
`[prefix](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#prefix)` | A string that can be used to limit the number of objects that are returned in a GET Bucket request to only those whose names begin with the specified value. Can be used in conjunction with a `delimiter`. | No  
`[start-after](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#startafter)2` | The object name after which you want to start listing objects. Objects whose names are lexicographically greater than the `start-after` are returned in the list of objects. If you include `continuation-token` in your request as well, `start-after` is ignored. | No  
`[version-id-marker](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versionidmarker)1` | The object generation after which you want to start listing objects. If you use `version-id-marker`, you must also use `key-marker`. | No  
`[versions](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versions)` | If specified on a versioned bucket, returns the list of all object versions. If omitted, only lists current versions. | No  
  
1 This query parameter is not valid for requests that include `list-type=2`.

2 This query parameter is only valid for requests that include `list-type=2`.

See [signed URL query string parameters](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests#required-query-parameters) for information on the parameters you include when creating and using [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Request headers

In addition to [common request headers](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket#request-headers), the following can be used.

Header | Description | Required  
---|---|---  
`[x-goog-interop-list-objects-format](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooginteroplistobjectsformat)` | If this header is set to `enabled` and the request uses the `[versions](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versions)` parameter, the response returns a list of objects in an interoperable format. If the header is set to `disabled`, the response returns a list of objects in the legacy format. The default value for `x-goog-interop-list-objects-format` is `disabled`. | No  
  
## Request body elements

This request does not include an XML document in the request body.

## Request syntax

The following syntax is an example GET Bucket request for listing objects.
    
    
    GET /?prefix=a_prefix&marker=a_marker&max-keys=max_number_of_keys&delimiter=a_delimiter HTTP/1.1
    Host: BUCKET_NAME.storage.googleapis.com
    Date: DATE
    Content-Length: 0
    Authorization: AUTHENTICATION_STRING
    

## Response headers

The request can return a variety of response headers depending on the request headers you use.

## Response body elements

The following response body elements are applicable for GET Bucket requests to list objects.

Element | Description  
---|---  
`ListBucketResult` | Container for the object information you are requesting.  
`ListVersionsResult`3 | Container for the object information you are requesting.  
`Name` | The bucket name.  
`CommonPrefixes` | Container for prefixes that satisfy your `prefix` and `delimiter` constraints. This container is used only if you specify a `delimiter` in the request, and duplicate entries are omitted.  
`Delimiter` | The `delimiter` that you specified in the request.  
`EncodingType`2 | The `encoding-type` that you specified in the request. If this is present in the response, then the response also includes encoded key name values in the `Delimiter`, `Prefix`, `Key`, `Marker`, and `StartAfter` response elements.  
`MaxKeys` | The `max-keys` that you specified in the request.  
`Prefix` | The `prefix` that you specified in the request.  
`GenerationMarker`1 | The `generation-marker` that you specified in the request.  
`NextGenerationMarker`1 | `NextGenerationMarker` provides the generation of the last object version that was returned. The value of `NextGenerationMarker` can be provided in the [`generation-marker`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#generationmarker) query string parameter in a future GET Bucket call to continue listing the bucket after this set of results. Note that the next call might return no results. `NextGenerationMarker` is returned only when the `versions` parameter is used in the request and there is also a `NextMarker` element in the response. If there are no more object versions in the bucket that follow the last object version in the list, `NextGenerationMarker` is not returned.  
`NextVersionIdMarker`1 3 | `NextVersionIdMarker` provides the generation of the last object version that was returned. The value of `NextVersionIdMarker` can be provided in the [`version-id-marker`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versionidmarker) query string parameter in a future GET Bucket call to continue listing the bucket after this set of results. Note that the next call might return no results. `NextVersionIdMarker` is returned only when the `versions` parameter is used in the request and there is also a `NextKeyMarker` element in the response. If there are no more object versions in the bucket that follow the last object version in the list, `NextVersionIdMarker` is not returned.  
`Marker`1 | The `marker` that you specified in the request.  
`NextMarker`1 | `NextMarker` provides the name of the last object that was returned. The value of `NextMarker` can be provided in the [`marker`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#marker) query string parameter in a future GET Bucket call to continue listing the bucket after this set of results. Note that the next call might return no results. If there are no more objects in the bucket that follow the last object in the list, `NextMarker` is not returned.  
`NextKeyMarker`1 3 | `NextKeyMarker` provides the name of the last object that was returned. The value of `NextKeyMarker` can be provided in the [`key-marker`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#keymarker) query string parameter in a future GET Bucket call to continue listing the bucket after this set of results. Note that the next call might return no results. If there are no more objects in the bucket that follow the last object in the list, `NextKeyMarker` is not returned.  
`StartAfter`2 | The `start-after` that you specified in the request.  
`ContinuationToken`2 | The `continuation-token` that you specified in the request.  
`NextContinuationToken`2 | `NextContinuationToken` is present when `IsTruncated` is `True`, and it provides an encoded representation of the last object that was returned. The value of `NextContinuationToken` can be provided in the [`continuation-token`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#continuationtoken) query string parameter of a future GET Bucket call to continue listing the bucket contents after this set of results. If there are no more objects in the bucket that follow the last object in the list, `NextContinuationToken` is not returned.  
`IsTruncated` | Indicates whether there are still more objects to be returned in the next GET Bucket call. The presence of this parameter in the response should always be checked to ensure a complete listing of all the results.  
`KeyCount`2 | The number of keys returned with this request, which is always less than or equal to any `max-keys` value specified in the request.  
`Contents` | Container for object information if `versions` query parameter is not used.  
`Version` | Container for object information if `versions` query parameter is used.  
`Key` | The name of an object.  
`Generation` | The generation of the object.  
`VersionId`3 | The generation of the object.  
`MetaGeneration` | Generation of the metadata of the object.  
`IsLatest` | If `versions` query parameter specified, this is set to true if the object is currently live. Live meaning that if this object is requested without generation, this object is returned.  
`LastModified` | The date and time that the object metadata was last modified.  
`DeletedTime` | If `versions` query parameter was specified, contains the date and time that an object was replaced or deleted for non-current objects (if the bucket has versioning enabled).  
`ETag` | An [HTTP 1.1 entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the object.  
`Size` | Size of the object in bytes.  
`Owner`2 | Container for owner information for the object. Relevant only if the bucket does not have uniform bucket-level access enabled, and included only if the request uses `fetch-owner=true`.  
`ID`2 | The ID of the owner of the object. The owner is always the uploader of the object.  
`DisplayName`2 | The name of the owner of the object. The owner is always the uploader of the object.  
`KmsKeyName` | The name of the KMS key used to encrypt the object. This element is only present if the object is encrypted with [Customer-Managed Encryption Keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).  
  
1 This response element is applicable for requests that do not include `list-type=2`.

2 This response element is only applicable for requests that include `list-type=2`.

3 This response element is only applicable for requests that include the query parameter [`versions`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#versions) and the header `x-goog-interop-list-objects-format=enabled`.

## Examples

The following sample lists the objects in a bucket named travel-maps.

**Request**
    
    
    GET / HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Wed, 17 Feb 2010 15:31:56 GMT
    Content-Length: 0
    Content-Type: text/plain
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
     Content-Length: 4061
     Content-Type: application/xml
     Date: Wed, 17 Feb 2010 23:31:57 GMT
     Expires: Wed, 17 Feb 2010 23:31:57 GMT
    
    <?xml version='1.0' encoding='utf-8'?>
    <ListBucketResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
      <Name>travel-maps</Name>
      <Prefix></Prefix>
      <Marker></Marker>
      <IsTruncated>false</IsTruncated>
      <Contents>
        <Key>europe/france/cannes.pdf</Key>
        <Generation>1360887759327000</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2010-02-17T22:11:12.487Z</LastModified>
        <ETag>"53fc311c15eda0a031809982ccf92aac"</ETag>
        <Size>5061631</Size>
      </Contents>
      <Contents>
        <Key>europe/france/paris.pdf</Key>
        <Generation>1360887759329000</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2010-02-17T22:09:57.457Z</LastModified>
        <ETag>"53fc311c15eda0a031809982ccf92aac"</ETag>
        <Size>5061631</Size>
      </Contents>
    </ListBucketResult>
    

The following sample lists the objects in travel-maps, but it restricts the list to 25 objects that begin with the letter "t" and come after "test".

**Request**
    
    
    GET /?prefix=t&marker=test&max-keys=25 HTTP/1.1
    Host: travel-maps.storage.googleapis.com
    Date: Mon, 16 Feb 2010 22:58:38 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date: Mon, 15 Feb 2010 12:30:40 GMT
    Content-Length: 2705
    Content-Type: application/xml
    
    <?xml version='1.0' encoding='utf-8'?>
    <ListBucketResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
      <Name>travel-maps</Name>
      <Prefix>t</Prefix>
      <Marker>test</Marker>
      <MaxKeys>25</MaxKeys>
      <IsTruncated>false</IsTruncated>
      <Contents>
        <Key>test_a.jpg</Key>
        <Generation>1360887659329000</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2010-02-17T03:12:55.561Z</LastModified>
        <ETag>"2281880ef78388266ecd7d4c1b472a0e"</ETag>
        <Size>328</Size>
      </Contents>
      <Contents>
        <Key>test_b.jpg</Key>
        <Generation>1360887659323000</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2010-02-17T03:12:54.606Z</LastModified>
        <ETag>"2281880ef78388266ecd7d4c1b472a0e"</ETag>
        <Size>328</Size>
      </Contents>
      <Contents>
        <Key>test_c.jpg</Key>
        <LastModified>2010-02-17T03:12:53.734Z</LastModified>
        <ETag>"2281880ef78388266ecd7d4c1b472a0e"</ETag>
        <Size>328</Size>
      </Contents>
    </ListBucketResult>
    

### Example using prefix and delimiter

The following example uses a `prefix` and a `delimiter` to return a list of objects that are named using a directory-like schema. By using `prefix=europe/` and `delimiter=/`, only those objects that are in the `europe/` "directory" are returned. Objects that are in "subdirectories" of the europe directory are not listed, but instead have the leading portion of their names included in the `CommonPrefixes` elements of the response. The sample assumes that the following objects are contained in a bucket named `travel-maps`:

  * africa/ghana.jpg
  * africa/egypt/cairo.jpg
  * europe/finland.jpg
  * europe/norway.jpg
  * europe/france/paris.jpg
  * europe/italy/rome.jpg
  * europe/sweden/stockholm.jpg
  * europe/sweden/stockholm/nordic_museum.jpg



The sample request returns an XML document that lists the following two objects in the `Contents` element:

  * europe/finland.jpg
  * europe/norway.jpg



The following europe subdirectories are listed in the `CommonPrefixes` element:

  * europe/france/
  * europe/italy/
  * europe/sweden/



**Request**
    
    
    GET /travel-maps?delimiter=/&prefix=europe/ HTTP/1.1
    Host: storage.googleapis.com
    Date: Mon, 16 Feb 2010 22:58:38 GMT
    Content-Length: 0
    Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s-6Uw7p8vtgSwg
    

**Response**
    
    
    HTTP/1.1 200 OK
    Date: Mon, 15 Feb 2010 12:30:40 GMT
    Content-Length: 1200
    Content-Type: application/xml
    
    <?xml version="1.0"?>
    <ListBucketResult xmlns='http://doc.s3.amazonaws.com/2006-03-01'>
      <Name>mybucket</Name>
      <Prefix>europe/</Prefix>
      <Marker />
      <IsTruncated>false</IsTruncated>
      <Contents>
        <Key>europe/finland.jpg</Key>
        <Generation>1360887659323000</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2010-02-17T03:12:55.561Z</LastModified>
        <ETag>"781e5e245d69b566979b86e28d23f2c7"</ETag>
        <Size>10</Size>
      </Contents>
      <Contents>
        <Key>europe/norway.jpg</Key>
        <Generation>1360887659323000</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2010-02-17T03:12:55.561Z</LastModified>
        <ETag>"781e5e245d69b566979b86e28d23f2c7"</ETag>
        <Size>10</Size>
      </Contents>
      <CommonPrefixes>
        <Prefix>europe/france/</Prefix>
      </CommonPrefixes>
      <CommonPrefixes>
        <Prefix>europe/italy/</Prefix>
      </CommonPrefixes>
      <CommonPrefixes>
        <Prefix>europe/sweden/</Prefix>
      </CommonPrefixes>
    </ListBucketResult>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
