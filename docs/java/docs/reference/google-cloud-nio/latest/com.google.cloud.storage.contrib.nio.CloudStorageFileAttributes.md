---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributes
title: Interface CloudStorageFileAttributes (0.139.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:33.214303+00:00
---

# Interface CloudStorageFileAttributes (0.139.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudStorageFileAttributes (0.139.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.139.0 (latest)  0.135.0  0.134.0  0.133.0  0.131.0  0.128.13  0.127.38  0.126.19  0.125.0  0.124.21  0.123.28 
    
    
    public interface CloudStorageFileAttributes extends BasicFileAttributes

Interface for attributes on a Cloud Storage file or pseudo-directory.

## Implements

[BasicFileAttributes](https://docs.oracle.com/javase/8/docs/api/java/nio/file/attribute/BasicFileAttributes.html)

## Methods 

### acl()
    
    
    public abstract Optional<List<Acl>> acl()

Returns access control list. See Also: "<https://developers.google.com/storage/docs/reference-headers#acl>"

**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Optional<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.cloud.storage.Acl>>` |   
  
### cacheControl()
    
    
    public abstract Optional<String> cacheControl()

Returns `Cache-Control` HTTP header value, if set. See Also: "<https://developers.google.com/storage/docs/reference-headers#cachecontrol>"

**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Optional<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### contentDisposition()
    
    
    public abstract Optional<String> contentDisposition()

Returns `Content-Disposition` HTTP header value, if set. See Also: "<https://developers.google.com/storage/docs/reference-headers#contentdisposition>"

**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Optional<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### contentEncoding()
    
    
    public abstract Optional<String> contentEncoding()

Returns `Content-Encoding` HTTP header value, if set. See Also: "<https://developers.google.com/storage/docs/reference-headers#contentencoding>"

**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Optional<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### etag()
    
    
    public abstract Optional<String> etag()

Returns HTTP etag hash of object contents. See Also: "<https://developers.google.com/storage/docs/hashes-etags>"

**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Optional<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### mimeType()
    
    
    public abstract Optional<String> mimeType()

Returns mime type (e.g. text/plain), if set. See Also: "<http://en.wikipedia.org/wiki/Internet_media_type#List_of_common_media_types>"

**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Optional<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### userMetadata()
    
    
    public abstract Map<String,String> userMetadata()

Returns user-specified metadata. See Also: "<https://developers.google.com/storage/docs/reference-headers#contentdisposition>"

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
