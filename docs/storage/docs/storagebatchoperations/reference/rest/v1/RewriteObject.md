---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject/
title: RewriteObject \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:49.429895+00:00
---

# RewriteObject  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  RewriteObject Stay organized with collections  Save and categorize content based on your preferences. 

Describes options for object rewrite.

JSON representation  
---  
      
    
    {
      "kmsKey": string,
      "storageClass": enum ([StorageClass](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject#StorageClass))
    }  
  
Fields  
---  
`kmsKey` |  `string` Optional. Resource name of the Cloud KMS key that is used to encrypt the object. The Cloud KMS key must be located in the same location as the object. For details, see [customer-managed encryption keys](https://cloud.google.com/storage/docs/encryption/customer-managed-keys#add-object-key).Format: `projects/{projectId}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}`For example: `projects/123456/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key`. The object will be rewritten and set with the specified KMS key.  
`storageClass` |  `enum (`[StorageClass](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/RewriteObject#StorageClass)`)` Optional. Rewrites the object to the specified storage class. Setting this field will perform a full byte copy of the object if the storage class is different from the object's current storage class. If Autoclass is enabled on the bucket, storage class changes are ignored by Cloud Storage.  
  
## StorageClass

The Google Cloud Storage class of an object. For more details, see [Storage classes](https://cloud.google.com/storage/docs/storage-classes). New storage classes can be added in the future.

Enums  
---  
`STORAGE_CLASS_UNSPECIFIED` | The storage class is not specified.  
`STANDARD` | Standard storage class.  
`NEARLINE` | Nearline storage class.  
`COLDLINE` | Coldline storage class.  
`ARCHIVE` | Archive storage class.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
