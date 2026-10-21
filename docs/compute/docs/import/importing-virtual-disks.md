---
url: https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks/
title: Import virtual disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:13.913845+00:00
---

# Import virtual disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Import virtual disks Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

If you have virtual disks in your on-premises environment with software and configurations that you need (sometimes referred to as _golden disks_ or _golden images_), you can save time by importing those virtual disks into Compute Engine and using the resulting image to [create virtual machines](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). The Migrate to Virtual Machines import tool supports most virtual disk file formats, including VMDK and VHD.

## Before you begin

  * Enable the VM Migration API on your project. For more information about enabling the VM Migration API, see [Enable Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).
  * Verify that the operating system on the disk is supported by Migrate to Virtual Machines. For more information, see [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).
  * Verify that the virtual disk image files that you want to import are supported.



## Supported formats

You can import virtual disk image files in the following formats using Migrate to Virtual Machines:

  * A single virtual machine disk (VMDK) - Recommended option, VMDK files are imported faster **Note:** Only monolithic VMDK files are supported. If you have a _-flat.vmdk_ file and a _.vmdk_ descriptor file, you can import these files by renaming the _-flat.vmdk_ file to _disk.raw_ , and compressing it as a _.tar.gz_ file.
  * QEMU copy-on-write (QCOW)
  * QEMU copy-on-write 2 (QCOW2)
  * QEMU enhanced disk format (QED)
  * VPC
  * Virtual disk image (VDI)
  * Virtual hard disk v2 (VHDX)
  * Virtual hard disk (VHD)



In addition to these formats, you can also import raw images from a RAW file (_.raw_), or from a compressed tar file (_.tar.gz_). When you use a compressed tar file, ensure that it contains a single file named _disk.raw_.

## Limitations

Arm is supported in [regions where Arm machines are available](https://docs.cloud.google.com/compute/docs/regions-zones). Migrate to Virtual Machines doesn't support importing disk images with Arm architecture in the following regions:

Region description | Region name  
---|---  
Berlin, Germany | `europe-west10`  
Turin, Italy | `europe-west12`  
Warsaw, Poland | `europe-central2`  
  
## Image import process

To import a virtual disk image to a Compute Engine image using Migrate to Virtual Machines, use the following steps:

  1. Prepare a virtual disk image file for import
  2. Choose a target project
  3. Import a virtual disk image to Compute Engine



## Prepare a virtual disk file for import

To import a virtual disk image to a Compute Engine image, you must first prepare the virtual disk image file for import. The following sections discuss these tasks in detail.

### Add the virtual disk image file to Cloud Storage

To import a virtual disk image to a Compute Engine image, you must first add the virtual disk image file to Cloud Storage. For more information, see [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects). For better performance, we recommend that you upload the virtual disk image file to a bucket in the same cloud region in which you want to create the image.

### Grant the required permissions

To import a virtual disk image to a Compute Engine image, grant permissions as described in the following table.

Role | Permissions required | Description  
---|---|---  
[Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) | `roles/storage.objectViewer` | Grant the default Migrate to Virtual Machines service account in the host project (`service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`) the `roles/storage.objectViewer` role on the bucket where the image you want to import resides. This permission lets Migrate to Virtual Machines access the source image.  
[VM Migration Administrator](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference) | `roles/vmmigration.admin` | In the host project, grant the user account that you want to use to import the source image the `roles/vmmigration.admin` role.  
[VM Migration Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/vmmigration#vmmigration.serviceAgent) | `roles/vmmigration.serviceAgent` | Grant the default Migrate to Virtual Machines service account in the host project (`service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`) the `roles/vmmigration.serviceAgent` role on the target project. For example, if `service-1234567890@gcp-sa-vmmigration.iam.gserviceaccount.com` is the Migrate to Virtual Machines service account in the host project, you must grant this service account the `roles/vmmigration.serviceAgent` role to be able to create the image in the target project.  
  
## Choose a target project

To host the Compute Engine image, you must create or choose a target project. A target project defines the destination project for a Compute Engine image. For more information on creating or choosing a target project, see [Adding a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

## Import a virtual disk image to Compute Engine

You can import a virtual disk image to Compute Engine using the Google Cloud console, Google Cloud CLI, or REST API commands.

###  Console 

To import a virtual disk image to Compute Engine using the Google Cloud console, use the following steps.

  1. Open the **Images** page in the Google Cloud console.   
[Go to the **Images** page](https://console.cloud.google.com/compute/images)
  2. Click **Import image**.
  3. Define the characteristics of the image. The following table lists the parameters that you can set for your image. Section title | Field name | Description  
---|---|---  
**General** | Name | The name of the image that you want to create. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).  
| Image import ID | An ID that represents the image import resource. When you import an image to Compute Engine, Migrate to Virtual Machines first creates an image import resource. The image import resource represents the image import process. You can use the Image import ID to get the link to the image that was imported as part of the image import process.  
| Source Cloud Storage file | The file from which you want to import the image. Click **Browse** to view the list of buckets in your current project, and select the file from which you want to import the image.   
If you want to import an image from a bucket from another project, you must enter the path in the format _bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view). When you copy the path, make sure that you don't copy the `gs://` prefix.   
Note that you can only import images from `.vmdk` and `.tar.gz` files.   
| Region | The region in which you want to create the image. For a list of supported regions, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
| Target project | The target project in which you want to create the image. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).   
| Family | (Optional) Select the image family. Compute Engine provides image families to help you make sure that your automation systems can reference the latest images. As an administrator, you can group a set of images as an image family. For more information, see [Public image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#public-families).   
| Description | (Optional) Add a description for the image.  
| Skip OS adaptation | To skip OS adaptation, click the **Skip OS adaptation** toggle to the on position.   
To function properly on Google Cloud, VMs created from imported images require changes to be made to their configuration. These changes are referred to as _OS adaptations_. Migrate to Virtual Machines performs OS adaptations automatically in the image import process. For more information, see [Adapt VM instances to run on Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations).  
| Generalize | To generalize the image, click the **Generalize** toggle to the on position. When you create an instance from an image, Windows adds some unique information to the instance. Generalize is a process that removes this information so that you can create multiple instances from the same image.  
**Licenses** | License type | Compute Engine supports pay as you go (PAYG) licenses and bring your own licenses (BYOL) for your deployed VMs. The default license type for a migrated VM is assigned by Migrate to Virtual Machines based on the migrated operating system, as described in [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).   
If your operating system supports multiple license types, you can override the default license type to explicitly specify a license type of PAYG or BYOL.   
**Note:** Some operating system types, such as CentOS and Debian, don't support a license. Other operating systems only support one type of license. Attempting to set an unsupported license type causes an error when you attempt to import the image.  
**Additional licenses** | Additional licenses | You can add up to 10 additional licenses to the VM instance created from the imported image using a valid URL format. For example, you can add additional licenses using the following URL format:   

         
         https://www.googleapis.com/compute/beta/projects/windows-sql-cloud/global/licenses/sql-server-2012-enterprise  
  
| Labels | To organize your project, add labels as key-value pairs to your resources. See [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).   
**Encryption** | Google-managed encryption key | Choose this option to use Google-owned and Google-managed encryption keys to encrypt your data during the import process. For more information, see [encrypts data when it is at rest](https://cloud.google.com/security/encryption-at-rest/default-encryption).   
| Customer managed encryption key | Choose this option to use customer-managed encryption keys (CMEK) to encrypt your data during the import process, and the data of the image created by the import process. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [CMEK](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data. These encryption keys are created, managed, and owned by you. For more information, see [ Protect resources by using Cloud KMS keys](https://cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin).   
When you add a CMEK, you must grant permissions as described in the following table. | Role | Permissions required | Description  
---|---|---  
[Cloud VM Migration Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-vm-migration-service-account) | `roles/vmmigration.serviceAgen` | Grant this permission to the Compute Engine service account to encrypt data of the image created during the import process.  
[Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent) | `roles/compute.serviceAgent` | Grant this permission to the Migrate to Virtual Machines service agent to encrypt the data during the import process.  
  4. Select **Import**.



###  gcloud 

To import a virtual disk image to Compute Engine using the Google Cloud CLI, use the following request.
    
    
    gcloud compute migration image-imports create IMAGE_NAME \
    --source-file=SOURCE_FILE \
    --location=REGION_ID \
    --target-project=projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT
    

Replace the following:

  * `IMAGE_NAME`: the name of the image that you want to create. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
  * `SOURCE_FILE`: the file from which you want to import the image. Enter the path in the format `gs://bucket/folder/file`. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view). Note that you can only import images from `.vmdk` and `.tar.gz` files.
  * `REGION_ID`: the region in which you want the image import process to run. The image is created in the closest multi-region. If you want the image to be created in a region, make sure that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `HOST_PROJECT_ID`: the name of the host project from which you want to migrate the virtual disk image.
  * `TARGET_PROJECT`: the target project in which you want to create the image. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).



For more information, see [`gcloud compute migration image-imports`](https://docs.cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports).

###  REST 

To import a virtual disk image to Compute Engine using the REST API, use the following steps.

  1. Create an image import resource using the following request.
         
         POST https://vmmigration.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/REGION_ID/imageImports?imageImportId=IMPORT_NAME
         {
         "cloudStorageUri": "SOURCE_FILE",
         "diskImageTargetDefaults": {
         "imageName": "IMAGE_NAME",
         "targetProject": "projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT",
         ...
         }
         }
         

Replace the following:

     * `HOST_PROJECT_ID`: the name of the host project from which you want to migrate the virtual disk image.
     * `REGION_ID`: the region in which you want the image import process to run. The image is created in the closest multi-region. If you want the image to be created in a region, make sure that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `SOURCE_FILE`: the file from which you want to import the image. Enter the path in the format _gs://bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view). Note that you can only import images from `.vmdk` and `.tar.gz` files.
     * `IMAGE_NAME`: the name of the image that you want to create. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     * `TARGET_PROJECT`: the target project in which you want to create the image. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

In this example, `IMPORT_NAME` is an ID that represents the image import resource. When you import an image to Compute Engine, Migrate to Virtual Machines creates an first creates an image import resource. The image import resource represents the image import process. You can use the `IMPORT_NAME` to get the link to the image that was imported as part of the image import process.

See the following table for the full list of image import create request fields supported fields.

Field name | Description  
---|---  
`cloudStorageUri` | string   
The path of the file from which you want to import the image. Enter the path in the format _gs://bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).   
Note that you can only import images from `.vmdk` and `.tar.gz` files.   
`diskImageTargetDefaults.targetProject` | string   
The path of the `TargetProject`. The target project in which you want to create the image. For more information, see [target project API reference](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.targetProjects/list). For example,   
`projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT`   
In the example, replace the following: 
     * `HOST_PROJECT_ID`: the name of the host project from which you want to migrate the virtual disk image.
     * `TARGET_PROJECT`: the target project in which you want to create the image.   
`diskImageTargetDefaults.imageName` | string   
The name of the image to be created. For more information on the naming rules, see [resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).   
`diskImageTargetDefaults.description` | string   
(Optional) A description of the image.   
`diskImageTargetDefaults.familyName` | string   
(Optional) Select the image family. Compute Engine provides image families to help you make sure that your automation systems can reference the latest images. As an administrator, you can group a set of images as an image family. For more information, see [Public image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#public-families). For more information, see [Public image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#public-families).  
`diskImageTargetDefaults.labels` | map (key: string, value: string)   
To organize your project, add labels as key-value pairs to your resources. See [Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).   
`diskImageTargetDefaults.additionalLicenses` | string[]   
You can add up to 10 additional licenses to the VM instance created from the imported image using a valid URL format. For example, you can add additional licenses using the following URL format:   

    
    https://www.googleapis.com/compute/beta/projects/windows-sql-cloud/global/licenses/sql-server-2012-enterprise  
  
`diskImageTargetDefaults.singleRegionStorage` | boolean   
Set this flag to true if you want the image `storageLocations` to be a region. If you set this flag to false, the closest multi-region is selected.  
`diskImageTargetDefaults.dataDiskImageImport` | boolean   
Set this flag to true if you want to skip OS adaptation.   
To function properly on Google Cloud, VMs created from imported images require changes to be made to their configuration. These changes are referred to as _OS adaptations_. Migrate to Virtual Machines performs OS adaptations automatically in the image import process. For more information, see [Adapt VM instances to run on Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations).  
`diskImageTargetDefaults.dataDiskImageImport.guestOsFeatures` | string[]   
Use these flags to enable capabilities on your Compute Engine VM instances created from the image.   
These flags don't affect the OS of the image; it only marks the image with the specified features. For a list of available flags, see [Guest OS features](https://cloud.google.com/compute/docs/images/create-custom#guest-os-features).   
`diskImageTargetDefaults.osAdaptationParameters.licenseType` | string   
The license type you want to use for your image. Compute Engine supports pay as you go (PAYG) licenses and bring your own licenses (BYOL) for your deployed VMs. The default license type for a migrated VM is assigned by Migrate to Virtual Machines based on the migrated operating system, as described in [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).   
If your operating system supports multiple license types, you can override the default license type to explicitly specify a license type of PAYG or BYOL.   
**Note:** Some operating system types, such as CentOS and Debian, don't support a license. Other operating systems only support one type of license. Attempting to set an unsupported license type causes an error when you attempt to import the image.  
`diskImageTargetDefaults.osAdaptationParameters.generalize` | boolean   
Set this flag to true if you want to generalize the image.   
When you create an instance from an image, Windows adds some unique information to the instance. Generalize is a process that removes this information so that you can create multiple instances from the same image.  
`diskImageTargetDefaults.encryption` | string   
The Google-owned and Google-managed encryption key that you want to use to encrypt your data during the import process. For more information, see [encrypts data when it is at rest](https://cloud.google.com/security/encryption-at-rest/default-encryption).   
`encryption` | string   
Choose this option to use customer-managed encryption keys (CMEK) to encrypt your data during the import process, and the data of the image created during the import process. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [CMEK](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data. These encryption keys are created, managed, and owned by you. For more information, see [ Protect resources by using Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin).   
When you add a CMEK, you must grant permissions as described in the following table. | Role | Permissions required | Description  
---|---|---  
[Cloud VM Migration Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-vm-migration-service-account) | roles/vmmigration.serviceAgent | Grant this permission to the Compute Engine service account to encrypt data of the image created during the import process.  
[Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent) | roles/compute.serviceAgent | Grant this permission to the Migrate to Virtual Machines service agent to encrypt the data during the import process.  
  
You should see a response similar to the following sample response.
    
    {
      "name": "projects/HOST_PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID",
      "metadata": {
        "createTime": "2023-10-31T09:12:26.94928636Z",
        "target": "projects/HOST_PROJECT_ID/locations/us-central1/imageImports/IMPORT_NAME",
        "verb": "create",
        "apiVersion": "v1",
        "@type": "type.googleapis.com/google.cloud.vmmigration.v1.OperationMetadata"
      }
    }
    

  2. Check if the image import job is complete by polling the operation using the following command.
         
         GET https://vmmigration.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID
         

Replace the following:

     * `HOST_PROJECT_ID`: the name of the host project from which you are migrating the virtual disk image.
     * `REGION_ID`: the region in which you want the image import process to run. The image is created in the closest multi-region. If you want the image to be created in a region, make sure that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `OPERATION_ID`: the operation ID of the migrate job.

You should see an operation completion response similar to the following sample response.
    
    {
        "done": true,
        "name": "projects/HOST_PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID",
        "response": {
          "@type": "type.googleapis.com/google.cloud.vmmigration.v1.ImageImport",
          "name": "projects/<HOST_PROJECT_ID>/locations/us-central1/imageImports/IMPORT_NAME",
          "cloudStorageUri": "SOURCE_FILE",
          "createTime": "2023-10-31T09:04:04.413664947Z",
          "diskImageTargetDefaults": {
            "imageName": "IMAGE_NAME",
            "targetProject": "projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT"
          },
          "recentImageImportJobs": [
            {
              "name": "projects/HOST_PROJECT_ID/locations/us-central1/imageImports/IMPORT_NAME/imageImportJobs/image-import-job",
              "diskImageTargetDetails": {
               "imageName": "IMAGE_NAME",
               "targetProject": "projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT"
            },
             "state": "PENDING"
           }
          ]
        },
        "metadata": {
          "createTime": "2023-10-31T09:04:04.416740716Z",
          "endTime": "2023-10-31T09:05:36.79987142Z",
          "target": "projects/HOST_PROJECT_ID/locations/us-central1/imageImports/IMPORT_NAME",
          "verb": "create",
          "apiVersion": "v1",
          "@type": "type.googleapis.com/google.cloud.vmmigration.v1.OperationMetadata"
        }
      }
    

  3. Monitor the image import job for completion using the following command.
         
         GET https://vmmigration.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/REGION_ID/imageImports/IMPORT_NAME/imageImportJobs/image-import-job
         

Replace the following:

     * `HOST_PROJECT_ID`: the name of the host project from which you are migrating the virtual disk image.
     * `REGION_ID`: the region in which you want the image import process to run. The image is created in the closest multi-region. If you want the image to be created in a region, make sure that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `IMPORT_NAME`: the ID that represents the image import resource. When you import an image to Compute Engine, Migrate to Virtual Machines creates an first creates an image import resource. The image import resource represents the image import process. You can use the `IMPORT_NAME` to get the link to the image that was imported as part of the image import process.

You should see a job completion response similar to the following sample response.
    
    {
      "createTime":"2023-10-31T09:12:27.053788394Z",
      "createdResources":[
        "https://www.googleapis.com/compute/v1/projects/USER_PROJECT/global/images/IMAGE_NAME"
      ],
      "diskImageTargetDetails": {
        "imageName":"IMAGE_NAME",
        "targetProject":"projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT"
      },
      "endTime":"2023-10-31T09:16:50.224865783Z",
      "name":"projects/HOST_PROJECT_ID/locations/us-central1/imageImports/IMPORT_NAME/imageImportJobs/image-import-job",
      "state":"SUCCEEDED"
    }
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
