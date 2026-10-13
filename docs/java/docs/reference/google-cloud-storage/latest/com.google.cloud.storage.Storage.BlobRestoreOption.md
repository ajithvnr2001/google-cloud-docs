---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption
title: Class Storage.BlobRestoreOption (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:54.935634+00:00
---

# Class Storage.BlobRestoreOption (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Storage.BlobRestoreOption (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public static class Storage.BlobRestoreOption extends Option<UnifiedOpts.ObjectSourceOpt>

Class for specifying blob restore options *

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.storage.UnifiedOpts.OptionShim > [Option](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Option) > Storage.BlobRestoreOption

## Inherited Members

com.google.cloud.storage.UnifiedOpts.OptionShim.equals(java.lang.Object)

com.google.cloud.storage.UnifiedOpts.OptionShim.hashCode()

com.google.cloud.storage.UnifiedOpts.OptionShim.toString()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### copySourceAcl(boolean copySourceAcl)
    
    
    public static Storage.BlobRestoreOption copySourceAcl(boolean copySourceAcl)

Returns an option for whether the restored object should copy the access controls of the source object.

**Parameter**  
---  
**Name** | **Description**  
`copySourceAcl` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.BlobRestoreOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption)` |   
  
### extraHeaders(@NonNull ImmutableMap<String,String> extraHeaders)
    
    
    public static Storage.BlobRestoreOption extraHeaders(@NonNull ImmutableMap<String,String> extraHeaders)

A set of extra headers to be set for all requests performed within the scope of the operation this option is passed to (a get, read, resumable upload etc).

If the same header name is specified across multiple options provided to a method, the first occurrence will be the value included in the request(s).

The following headers are not allowed to be specified, and will result in an IllegalArgumentException.

  1. `Accept-Encoding`
  2. `Cache-Control`
  3. `Connection`
  4. `Content-ID`
  5. `Content-Length`
  6. `Content-Range`
  7. `Content-Transfer-Encoding`
  8. `Content-Type`
  9. `Date`
  10. `ETag`
  11. `If-Match`
  12. `If-None-Match`
  13. `Keep-Alive`
  14. `Range`
  15. `TE`
  16. `Trailer`
  17. `Transfer-Encoding`
  18. `User-Agent`
  19. `X-Goog-Api-Client`
  20. `X-Goog-Content-Length-Range`
  21. `X-Goog-Copy-Source-Encryption-Algorithm`
  22. `X-Goog-Copy-Source-Encryption-Key`
  23. `X-Goog-Copy-Source-Encryption-Key-Sha256`
  24. `X-Goog-Encryption-Algorithm`
  25. `X-Goog-Encryption-Key`
  26. `X-Goog-Encryption-Key-Sha256`
  27. `X-Goog-Gcs-Idempotency-Token`
  28. `X-Goog-Meta-*`
  29. `X-Goog-User-Project`
  30. `X-HTTP-Method-Override`
  31. `X-Upload-Content-Length`
  32. `X-Upload-Content-Type`



**Parameter**  
---  
**Name** | **Description**  
`extraHeaders` | `@org.checkerframework.checker.nullness.qual.NonNull com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.BlobRestoreOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption)` |   
  
### generationMatch(long generation)
    
    
    public static Storage.BlobRestoreOption generationMatch(long generation)

Returns an option for blob's data generation match. If this option is used the request will fail if generation does not match.

**Parameter**  
---  
**Name** | **Description**  
`generation` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.BlobRestoreOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption)` |   
  
### generationNotMatch(long generation)
    
    
    public static Storage.BlobRestoreOption generationNotMatch(long generation)

Returns an option for blob's data generation mismatch. If this option is used the request will fail if blob's generation matches the provided value.

**Parameter**  
---  
**Name** | **Description**  
`generation` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.BlobRestoreOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption)` |   
  
### metagenerationMatch(long generation)
    
    
    public static Storage.BlobRestoreOption metagenerationMatch(long generation)

Returns an option for blob's metageneration match. If this option is used the request will fail if blob's metageneration does not match the provided value.

**Parameter**  
---  
**Name** | **Description**  
`generation` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.BlobRestoreOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption)` |   
  
### metagenerationNotMatch(long generation)
    
    
    public static Storage.BlobRestoreOption metagenerationNotMatch(long generation)

Returns an option for blob's metageneration mismatch. If this option is used the request will fail if blob's metageneration matches the provided value.

**Parameter**  
---  
**Name** | **Description**  
`generation` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Storage.BlobRestoreOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BlobRestoreOption)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
