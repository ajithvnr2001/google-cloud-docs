---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption
title: Class Blob.BlobSourceOption (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:18.196611+00:00
---

# Class Blob.BlobSourceOption (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Blob.BlobSourceOption (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public static class Blob.BlobSourceOption extends Option<UnifiedOpts.ObjectSourceOpt>

Class for specifying blob source options when `Blob` methods are used.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.storage.UnifiedOpts.OptionShim > [Option](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Option) > Blob.BlobSourceOption

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

### decryptionKey(@NonNull String key)
    
    
    public static Blob.BlobSourceOption decryptionKey(@NonNull String key)

Returns an option to set a customer-supplied AES256 key for server-side encryption of the blob.

**Parameter**  
---  
**Name** | **Description**  
`key` | `@org.checkerframework.checker.nullness.qual.NonNull java.lang.String`  
the AES256 encoded in base64  
**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### decryptionKey(@NonNull Key key)
    
    
    public static Blob.BlobSourceOption decryptionKey(@NonNull Key key)

Returns an option to set a customer-supplied AES256 key for server-side encryption of the blob.

**Parameter**  
---  
**Name** | **Description**  
`key` | `@org.checkerframework.checker.nullness.qual.NonNull java.security.Key`  
  
**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### dedupe(Blob.BlobSourceOption[] os)
    
    
    public static Blob.BlobSourceOption[] dedupe(Blob.BlobSourceOption[] os)

Deduplicate any options which are the same parameter. The value which comes last in ` os` will be the value included in the return.

**Parameter**  
---  
**Name** | **Description**  
`os` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]` |   
  
### dedupe(Blob.BlobSourceOption[] array, Blob.BlobSourceOption[] os)
    
    
    public static Blob.BlobSourceOption[] dedupe(Blob.BlobSourceOption[] array, Blob.BlobSourceOption[] os)

Deduplicate any options which are the same parameter.

The value which comes last in `collection` and `os` will be the value included in the return. All options from `os` will override their counterparts in ` collection`.

**Parameters**  
---  
**Name** | **Description**  
`array` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
  
`os` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]` |   
  
### dedupe(Collection<Blob.BlobSourceOption> collection, Blob.BlobSourceOption[] os)
    
    
    public static Blob.BlobSourceOption[] dedupe(Collection<Blob.BlobSourceOption> collection, Blob.BlobSourceOption[] os)

Deduplicate any options which are the same parameter.

The value which comes last in `collection` and `os` will be the value included in the return. All options from `os` will override their counterparts in ` collection`.

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)>`  
  
`os` | `[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)[]` |   
  
### generationMatch()
    
    
    public static Blob.BlobSourceOption generationMatch()

Returns an option for blob's generation match. If this option is used the request will fail if generation does not match.

**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### generationNotMatch() (deprecated)
    
    
    public static Blob.BlobSourceOption generationNotMatch()

**Deprecated.** _This option is invalid, and can never result in a valid response from the server._

Returns an option for blob's generation mismatch. If this option is used the request will fail if generation matches.

**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### metagenerationMatch()
    
    
    public static Blob.BlobSourceOption metagenerationMatch()

Returns an option for blob's metageneration match. If this option is used the request will fail if metageneration does not match.

**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### metagenerationNotMatch()
    
    
    public static Blob.BlobSourceOption metagenerationNotMatch()

Returns an option for blob's metageneration mismatch. If this option is used the request will fail if metageneration matches.

**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### shouldReturnRawInputStream(boolean shouldReturnRawInputStream)
    
    
    public static Blob.BlobSourceOption shouldReturnRawInputStream(boolean shouldReturnRawInputStream)

Returns an option for whether the request should return the raw input stream, instead of automatically decompressing the content. By default, this is false for Blob.downloadTo(), but true for ReadChannel.read().

**Parameter**  
---  
**Name** | **Description**  
`shouldReturnRawInputStream` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
### userProject(@NonNull String userProject)
    
    
    public static Blob.BlobSourceOption userProject(@NonNull String userProject)

Returns an option for blob's billing user project. This option is used only if the blob's bucket has requester_pays flag enabled.

**Parameter**  
---  
**Name** | **Description**  
`userProject` | `@org.checkerframework.checker.nullness.qual.NonNull java.lang.String`  
  
**Returns**  
---  
**Type** | **Description**  
`[Blob.BlobSourceOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.BlobSourceOption)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
