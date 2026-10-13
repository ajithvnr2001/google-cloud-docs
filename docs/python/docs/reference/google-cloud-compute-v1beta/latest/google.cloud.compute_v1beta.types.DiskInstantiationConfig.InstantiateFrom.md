---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DiskInstantiationConfig.InstantiateFrom
title: Class InstantiateFrom (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:50.037679+00:00
---

# Class InstantiateFrom (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DiskInstantiationConfig.InstantiateFrom

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstantiateFrom (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    InstantiateFrom(value)

Specifies whether to include the disk and what image to use. Possible values are:
    
    
     - source-image: to use the same image that was used to
    

create the source instance's corresponding disk. Applicable to the boot disk and additional read-write disks.

  * source-image-family: to use the same image family that was used to create the source instance's corresponding disk. Applicable to the boot disk and additional read-write disks.
  * custom-image: to use a user-provided image url for disk creation. Applicable to the boot disk and additional read-write disks.
    * attach-read-only: to attach a read-only disk. Applicable to read-only disks.
  * do-not-include: to exclude a disk from the template. Applicable to additional read-write disks, local SSDs, and read-only disks.

boot disk, additional read-write disks.




## Enums  
  
---  
**Name** | **Description**  
`UNDEFINED_INSTANTIATE_FROM` | A value indicating that the enum field is not set.  
`ATTACH_READ_ONLY` | Attach the existing disk in read-only mode. The request will fail if the disk was attached in read-write mode on the source instance. Applicable to: read-only disks.  
`BLANK` | Create a blank disk. The disk will be created unformatted. Applicable to: additional read-write disks, local SSDs.  
`CUSTOM_IMAGE` | Use the custom image specified in the custom_image field. Applicable to: boot disk, additional read-write disks.  
`DEFAULT` | Use the default instantiation option for the corresponding type of disk. For boot disk and any other R/W disks, new custom images will be created from each disk. For read-only disks, they will be attached in read-only mode. Local SSD disks will be created as blank volumes.  
`DO_NOT_INCLUDE` | Do not include the disk in the instance template. Applicable to: additional read-write disks, local SSDs, read-only disks.  
`SOURCE_IMAGE` | Use the same source image used for creation of the source instance's corresponding disk. The request will fail if the source VM's disk was created from a snapshot. Applicable to: boot disk, additional read-write disks.  
`SOURCE_IMAGE_FAMILY` | Use the same source image family used for creation of the source instance's corresponding disk. The request will fail if the source image of the source disk does not belong to any image family. Applicable to:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
