---
url: https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.Volume
title: Google Cloud Life Sciences V2beta Client - Class Volume (0.10.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:59.770260+00:00
---

# Google Cloud Life Sciences V2beta Client - Class Volume (0.10.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.Volume

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Life Sciences V2beta Client - Class Volume (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.9.0  0.8.1  0.7.3  0.6.8  0.5.4  0.4.0  0.3.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Life Sciences V2beta Client class Volume.

Carries information about storage that can be attached to a VM.

Specify either [`Volume`](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.Volume) or [`Disk`](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.Disk), but not both.

Generated from protobuf message `google.cloud.lifesciences.v2beta.Volume`

## Namespace

Google \ Cloud \ LifeSciences \ V2beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ volume` |  `string`   
A user-supplied name for the volume. Used when mounting the volume into `Actions`. The name must contain only upper and lowercase alphanumeric characters and hyphens and cannot start with a hyphen.  
`↳ persistent_disk` |  `[PersistentDisk](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PersistentDisk)`   
Configuration for a persistent disk.  
`↳ existing_disk` |  `[ExistingDisk](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ExistingDisk)`   
Configuration for a existing disk.  
`↳ nfs_mount` |  `[NFSMount](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.NFSMount)`   
Configuration for an NFS mount.  
  
### getVolume

A user-supplied name for the volume. Used when mounting the volume into `Actions`. The name must contain only upper and lowercase alphanumeric characters and hyphens and cannot start with a hyphen.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setVolume

A user-supplied name for the volume. Used when mounting the volume into `Actions`. The name must contain only upper and lowercase alphanumeric characters and hyphens and cannot start with a hyphen.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPersistentDisk

Configuration for a persistent disk.

**Returns**  
---  
**Type** | **Description**  
`[PersistentDisk](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PersistentDisk)|null` |   
  
### hasPersistentDisk

### setPersistentDisk

Configuration for a persistent disk.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PersistentDisk](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PersistentDisk)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExistingDisk

Configuration for a existing disk.

**Returns**  
---  
**Type** | **Description**  
`[ExistingDisk](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ExistingDisk)|null` |   
  
### hasExistingDisk

### setExistingDisk

Configuration for a existing disk.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ExistingDisk](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ExistingDisk)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNfsMount

Configuration for an NFS mount.

**Returns**  
---  
**Type** | **Description**  
`[NFSMount](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.NFSMount)|null` |   
  
### hasNfsMount

### setNfsMount

Configuration for an NFS mount.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[NFSMount](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.NFSMount)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStorage

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
