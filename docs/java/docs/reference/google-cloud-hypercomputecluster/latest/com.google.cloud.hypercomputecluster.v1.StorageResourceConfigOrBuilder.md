---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.StorageResourceConfigOrBuilder
title: Interface StorageResourceConfigOrBuilder (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:49.228014+00:00
---

# Interface StorageResourceConfigOrBuilder (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.StorageResourceConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StorageResourceConfigOrBuilder (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StorageResourceConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConfigCase()
    
    
    public abstract StorageResourceConfig.ConfigCase getConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.ConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.StorageResourceConfig.ConfigCase)` |   
  
### getExistingBucket()
    
    
    public abstract ExistingBucketConfig getExistingBucket()

Optional. Immutable. If set, indicates that an existing Cloud Storage bucket should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingBucketConfig existing_bucket = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingBucketConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.ExistingBucketConfig)` | The existingBucket.  
  
### getExistingBucketOrBuilder()
    
    
    public abstract ExistingBucketConfigOrBuilder getExistingBucketOrBuilder()

Optional. Immutable. If set, indicates that an existing Cloud Storage bucket should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingBucketConfig existing_bucket = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingBucketConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.ExistingBucketConfigOrBuilder)` |   
  
### getExistingFilestore()
    
    
    public abstract ExistingFilestoreConfig getExistingFilestore()

Optional. Immutable. If set, indicates that an existing Filestore instance should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingFilestoreConfig existing_filestore = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingFilestoreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.ExistingFilestoreConfig)` | The existingFilestore.  
  
### getExistingFilestoreOrBuilder()
    
    
    public abstract ExistingFilestoreConfigOrBuilder getExistingFilestoreOrBuilder()

Optional. Immutable. If set, indicates that an existing Filestore instance should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingFilestoreConfig existing_filestore = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingFilestoreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.ExistingFilestoreConfigOrBuilder)` |   
  
### getExistingLustre()
    
    
    public abstract ExistingLustreConfig getExistingLustre()

Optional. Immutable. If set, indicates that an existing Managed Lustre instance should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingLustreConfig existing_lustre = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingLustreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.ExistingLustreConfig)` | The existingLustre.  
  
### getExistingLustreOrBuilder()
    
    
    public abstract ExistingLustreConfigOrBuilder getExistingLustreOrBuilder()

Optional. Immutable. If set, indicates that an existing Managed Lustre instance should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingLustreConfig existing_lustre = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingLustreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.ExistingLustreConfigOrBuilder)` |   
  
### getNewBucket()
    
    
    public abstract NewBucketConfig getNewBucket()

Optional. Immutable. If set, indicates that a new Cloud Storage bucket should be created.

` .google.cloud.hypercomputecluster.v1.NewBucketConfig new_bucket = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewBucketConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.NewBucketConfig)` | The newBucket.  
  
### getNewBucketOrBuilder()
    
    
    public abstract NewBucketConfigOrBuilder getNewBucketOrBuilder()

Optional. Immutable. If set, indicates that a new Cloud Storage bucket should be created.

` .google.cloud.hypercomputecluster.v1.NewBucketConfig new_bucket = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewBucketConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.NewBucketConfigOrBuilder)` |   
  
### getNewFilestore()
    
    
    public abstract NewFilestoreConfig getNewFilestore()

Optional. Immutable. If set, indicates that a new Filestore instance should be created.

` .google.cloud.hypercomputecluster.v1.NewFilestoreConfig new_filestore = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewFilestoreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.NewFilestoreConfig)` | The newFilestore.  
  
### getNewFilestoreOrBuilder()
    
    
    public abstract NewFilestoreConfigOrBuilder getNewFilestoreOrBuilder()

Optional. Immutable. If set, indicates that a new Filestore instance should be created.

` .google.cloud.hypercomputecluster.v1.NewFilestoreConfig new_filestore = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewFilestoreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.NewFilestoreConfigOrBuilder)` |   
  
### getNewLustre()
    
    
    public abstract NewLustreConfig getNewLustre()

Optional. Immutable. If set, indicates that a new Managed Lustre instance should be created.

` .google.cloud.hypercomputecluster.v1.NewLustreConfig new_lustre = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewLustreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.NewLustreConfig)` | The newLustre.  
  
### getNewLustreOrBuilder()
    
    
    public abstract NewLustreConfigOrBuilder getNewLustreOrBuilder()

Optional. Immutable. If set, indicates that a new Managed Lustre instance should be created.

` .google.cloud.hypercomputecluster.v1.NewLustreConfig new_lustre = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewLustreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1.NewLustreConfigOrBuilder)` |   
  
### hasExistingBucket()
    
    
    public abstract boolean hasExistingBucket()

Optional. Immutable. If set, indicates that an existing Cloud Storage bucket should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingBucketConfig existing_bucket = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the existingBucket field is set.  
  
### hasExistingFilestore()
    
    
    public abstract boolean hasExistingFilestore()

Optional. Immutable. If set, indicates that an existing Filestore instance should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingFilestoreConfig existing_filestore = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the existingFilestore field is set.  
  
### hasExistingLustre()
    
    
    public abstract boolean hasExistingLustre()

Optional. Immutable. If set, indicates that an existing Managed Lustre instance should be imported.

` .google.cloud.hypercomputecluster.v1.ExistingLustreConfig existing_lustre = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the existingLustre field is set.  
  
### hasNewBucket()
    
    
    public abstract boolean hasNewBucket()

Optional. Immutable. If set, indicates that a new Cloud Storage bucket should be created.

` .google.cloud.hypercomputecluster.v1.NewBucketConfig new_bucket = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newBucket field is set.  
  
### hasNewFilestore()
    
    
    public abstract boolean hasNewFilestore()

Optional. Immutable. If set, indicates that a new Filestore instance should be created.

` .google.cloud.hypercomputecluster.v1.NewFilestoreConfig new_filestore = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newFilestore field is set.  
  
### hasNewLustre()
    
    
    public abstract boolean hasNewLustre()

Optional. Immutable. If set, indicates that a new Managed Lustre instance should be created.

` .google.cloud.hypercomputecluster.v1.NewLustreConfig new_lustre = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newLustre field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
