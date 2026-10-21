---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata/
title: PutMetadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:55:46.139867+00:00
---

# PutMetadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  PutMetadata Stay organized with collections  Save and categorize content based on your preferences. 

Describes options for object metadata update.

JSON representation  
---  
      
    
    {
      "customMetadata": {
        string: string,
        ...
      },
      "contentDisposition": string,
      "contentEncoding": string,
      "contentLanguage": string,
      "contentType": string,
      "cacheControl": string,
      "customTime": string,
      "objectRetention": {
        object ([ObjectRetention](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata#ObjectRetention))
      }
    }  
  
Fields  
---  
`customMetadata` |  `map (key: string, value: string)` Optional. Updates the object's custom metadata. This operation adds or sets individual custom metadata key-value pairs. Keys specified with empty values have their values cleared. Existing custom metadata keys not included in the request remain unchanged. For details, see [Custom metadata](https://cloud.google.com/storage/docs/metadata#custom-metadata).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`contentDisposition` |  `string` Optional. Updates objects `Content-Disposition` fixed metadata. Unset values in the request are ignored. To clear the metadata, set an empty value. For details, see [Content-Disposition](https://cloud.google.com/storage/docs/metadata#content-disposition).  
`contentEncoding` |  `string` Optional. Updates the objects `Content-Encoding` fixed metadata. Unset values in the request are ignored. To clear the metadata, set an empty value. For details, see [Content-Encoding](https://cloud.google.com/storage/docs/metadata#content-encoding).  
`contentLanguage` |  `string` Optional. Updates the objects `Content-Language` fixed metadata. Metadata values must use ISO 639-1 language codes. The maximum length for metadata values is 100 characters. Unset values in the request are ignored. To clear the metadata, set an empty value. For details, see [Content-Language](https://cloud.google.com/storage/docs/metadata#content-language).  
`contentType` |  `string` Optional. Updates objects `Content-Type` fixed metadata. Unset values in the request are ignored. To clear the metadata, set an empty value. For details, see [Content-Type](https://cloud.google.com/storage/docs/metadata#content-type).  
`cacheControl` |  `string` Optional. Updates the objects `Cache-Control` fixed metadata. Unset values in the request are ignored. To clear the metadata, set an empty value. Additionally, the value for `Custom-Time` can't decrease. For details, see [Cache-Control](https://cloud.google.com/storage/docs/metadata#caching_data).  
`customTime` |  `string` Optional. Updates the objects `Custom-Time` fixed metadata. Unset values in the request are ignored. To clear the metadata, set an empty value. The time must be specified in RFC 3339 format, for example `YYYY-MM-DD'T'HH:MM:SS'Z'` or `YYYY-MM-DD'T'HH:MM:SS.SS'Z'`. For details, see [Custom-Time](https://cloud.google.com/storage/docs/metadata#custom-time).  
`objectRetention` |  `object (`[ObjectRetention](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata#ObjectRetention)`)` Optional. Updates an object's retention configuration. To clear an object's retention, both `retentionMode` and `retainUntilTime` must be left unset (omitted). Setting `retentionMode` to `RETENTION_MODE_UNSPECIFIED` is treated as a no-op. Unlike an unset field, it doesn't modify or clear the retention settings. An object with `LOCKED` retention mode can't have its retention cleared or its `retainUntilTime` reduced. For more information, see [Object retention](https://cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#retain-until-time).  
  
## ObjectRetention

Describes options for object retention update.

JSON representation  
---  
      
    
    {
      "retainUntilTime": string,
      "retentionMode": enum ([RetentionMode](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata#RetentionMode))
    }  
  
Fields  
---  
`retainUntilTime` |  `string` Required. The object's retention expiration time, during which, the object is protected from being deleted or overwritten. The time must be specified in RFC 3339 format, for example `YYYY-MM-DD'T'HH:MM:SS'Z'` or `YYYY-MM-DD'T'HH:MM:SS.SS'Z'`. To clear an object's retention, both `retentionMode` and `retainUntilTime` must be left unset (omitted). Setting `retentionMode` to `RETENTION_MODE_UNSPECIFIED` is treated as a no-op. Unlike an unset field, it doesn't modify or clear the retention settings.  
`retentionMode` |  `enum (`[RetentionMode](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/PutMetadata#RetentionMode)`)` Required. The retention mode.  
  
## RetentionMode

The retention mode.

Enums  
---  
`RETENTION_MODE_UNSPECIFIED` | The retention mode isn't specified.  
`LOCKED` | When the retention mode is `LOCKED`, the `retainUntilTime` can't be removed or reduced.  
`UNLOCKED` | When the retention mode is `UNLOCKED`, the `retainUntilTime` can be removed or modified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
