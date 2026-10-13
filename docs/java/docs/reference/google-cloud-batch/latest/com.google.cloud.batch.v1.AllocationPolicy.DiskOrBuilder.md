---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.DiskOrBuilder
title: Interface AllocationPolicy.DiskOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:09.114172+00:00
---

# Interface AllocationPolicy.DiskOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.DiskOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AllocationPolicy.DiskOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static interface AllocationPolicy.DiskOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDataSourceCase()
    
    
    public abstract AllocationPolicy.Disk.DataSourceCase getDataSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.Disk.DataSourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.DataSourceCase)` |   
  
### getDiskInterface()
    
    
    public abstract String getDiskInterface()

Local SSDs are available through both "SCSI" and "NVMe" interfaces. If not indicated, "NVMe" will be the default one for local ssds. This field is ignored for persistent disks as the interface is chosen automatically. See <https://cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface>.

`string disk_interface = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskInterface.  
  
### getDiskInterfaceBytes()
    
    
    public abstract ByteString getDiskInterfaceBytes()

Local SSDs are available through both "SCSI" and "NVMe" interfaces. If not indicated, "NVMe" will be the default one for local ssds. This field is ignored for persistent disks as the interface is chosen automatically. See <https://cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface>.

`string disk_interface = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskInterface.  
  
### getImage()
    
    
    public abstract String getImage()

URL for a VM image to use as the data source for this disk. For example, the following are all valid URLs:

  * Specify the image by its family name: projects/{project}/global/images/family/{image_family}
  * Specify the image version: projects/{project}/global/images/{image_version}

You can also use Batch customized image in short names. The following image values are supported for a boot disk:

  * `batch-debian`: use Batch Debian images.

  * `batch-cos`: use Batch Container-Optimized images.
  * `batch-hpc-rocky`: use Batch HPC Rocky Linux images.



`string image = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The image.  
  
### getImageBytes()
    
    
    public abstract ByteString getImageBytes()

URL for a VM image to use as the data source for this disk. For example, the following are all valid URLs:

  * Specify the image by its family name: projects/{project}/global/images/family/{image_family}
  * Specify the image version: projects/{project}/global/images/{image_version}

You can also use Batch customized image in short names. The following image values are supported for a boot disk:

  * `batch-debian`: use Batch Debian images.

  * `batch-cos`: use Batch Container-Optimized images.
  * `batch-hpc-rocky`: use Batch HPC Rocky Linux images.



`string image = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for image.  
  
### getSizeGb()
    
    
    public abstract long getSizeGb()

Disk size in GB.

**Non-Boot Disk** : If the `type` specifies a persistent disk, this field is ignored if `data_source` is set as `image` or `snapshot`. If the `type` specifies a local SSD, this field should be a multiple of 375 GB, otherwise, the final size will be the next greater multiple of 375 GB.

**Boot Disk** : Batch will calculate the boot disk size based on source image and task requirements if you do not speicify the size. If both this field and the `boot_disk_mib` field in task spec's `compute_resource` are defined, Batch will only honor this field. Also, this field should be no smaller than the source disk's size when the `data_source` is set as `snapshot` or `image`. For example, if you set an image as the `data_source` field and the image's default disk size 30 GB, you can only use this field to make the disk larger or equal to 30 GB.

`int64 size_gb = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sizeGb.  
  
### getSnapshot()
    
    
    public abstract String getSnapshot()

Name of a snapshot used as the data source. Snapshot is not supported as boot disk now.

`string snapshot = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The snapshot.  
  
### getSnapshotBytes()
    
    
    public abstract ByteString getSnapshotBytes()

Name of a snapshot used as the data source. Snapshot is not supported as boot disk now.

`string snapshot = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for snapshot.  
  
### getType()
    
    
    public abstract String getType()

Disk type as shown in `gcloud compute disk-types list`. For example, local SSD uses type "local-ssd". Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd" or "pd-standard". If not specified, "pd-standard" will be used as the default type for non-boot disks, "pd-balanced" will be used as the default type for boot disks.

`string type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

Disk type as shown in `gcloud compute disk-types list`. For example, local SSD uses type "local-ssd". Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd" or "pd-standard". If not specified, "pd-standard" will be used as the default type for non-boot disks, "pd-balanced" will be used as the default type for boot disks.

`string type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### hasImage()
    
    
    public abstract boolean hasImage()

URL for a VM image to use as the data source for this disk. For example, the following are all valid URLs:

  * Specify the image by its family name: projects/{project}/global/images/family/{image_family}
  * Specify the image version: projects/{project}/global/images/{image_version}

You can also use Batch customized image in short names. The following image values are supported for a boot disk:

  * `batch-debian`: use Batch Debian images.

  * `batch-cos`: use Batch Container-Optimized images.
  * `batch-hpc-rocky`: use Batch HPC Rocky Linux images.



`string image = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the image field is set.  
  
### hasSnapshot()
    
    
    public abstract boolean hasSnapshot()

Name of a snapshot used as the data source. Snapshot is not supported as boot disk now.

`string snapshot = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the snapshot field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
