---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import/
title: Import machine images \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:13.463881+00:00
---

# Import machine images  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Import machine images Stay organized with collections  Save and categorize content based on your preferences. 

A machine image lets you store the configuration, metadata, permissions, and data from one or more disks for a virtual machine (VM) instance running on Compute Engine. For information about when and how to use machine images, see [Machine images](https://docs.cloud.google.com/compute/docs/machine-images).

This page describes the steps that you can use to import a machine image from a [virtual appliance](https://wikipedia.org/wiki/Virtual_appliance) using Migrate to Virtual Machines.

## Before you begin

  * [Enable the VM Migration API](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services) on your project.
  * Verify that the boot disk is configured with a [supported operating system](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).



## Supported file formats

You can import machine image files in the following formats using Migrate to Virtual Machines:

  * **Open Virtualization Format (OVF):** One OVF file and virtual machine disk (VMDK) files in the same bucket.

**Note:** Migrate to Virtual Machines only supports importing VMDK disk files in the OVF format. To import any other type of disk file, you must first convert the disk file to an OVA file and then import it.
  * **Open Virtual Appliance (OVA):** One OVA file containing an OVF file and disk files. Migrate to Virtual Machines supports importing OVA machine image files in the following disk file formats:

    * Virtual machine disk (VMDK)
    * QEMU copy-on-write (QCOW)
    * QEMU copy-on-write 2 (QCOW2)
    * QEMU enhanced disk format (QED)
    * VPC
    * Virtual disk image (VDI)
    * Virtual hard disk v2 (VHDX)



## Limitations

When you import machine images, the following limitations apply:

  * You can only import machine images to [regions that support N2 instance families](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * You can't import machine images to [4th generation machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). For more information, see [machine image import limitations and restrictions](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images#limitations_and_restrictions)
  * You can't import Arm architecture-based machine images.
  * You can't create machine images from source VMs with any of the following: 
    * Attached disks greater than 200 TB
    * A4, A3, C3D, H3, or Z3 machine types



## Machine image import process

To import a machine image to Compute Engine machine image using Migrate to Virtual Machines, use the following steps:

  1. Prepare a machine image file for import
  2. Choose a target project
  3. Import a machine image to Compute Engine



## Prepare a machine file for import

To import a machine image to a Compute Engine image, you must first prepare the machine image file for import. The following sections discuss these tasks in detail.

### Add the machine image file to Cloud Storage

To import a machine image to a Compute Engine machine image, you must first add the machine image file to Cloud Storage. For more information, see [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects). For better performance, we recommend that you upload the machine image file to a bucket in the same Google Cloud in which you want to create the machine image.

### Grant the required permissions

To import a machine image to a Compute Engine machine image, grant permissions as described in the following table.

Role | Permissions required | Description  
---|---|---  
[Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) | `roles/storage.objectViewer` | Grant the default Migrate to Virtual Machines service account in the host project (`service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`) the `roles/storage.objectViewer` role on the bucket where the image you want to import resides. This permission lets Migrate to Virtual Machines access the source image.  
[VM Migration Administrator](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference) | `roles/vmmigration.admin` | In the host project, grant the user account that you want to use to import the source image the `roles/vmmigration.admin` role.  
[VM Migration Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/vmmigration#vmmigration.serviceAgent) | `roles/vmmigration.serviceAgent` | Grant the default Migrate to Virtual Machines service account in the host project (`service-HOST_PROJECT_NUMBER@gcp-sa-vmmigration.iam.gserviceaccount.com`) the `roles/vmmigration.serviceAgent` role on the target project. For example, if `service-1234567890@gcp-sa-vmmigration.iam.gserviceaccount.com` is the Migrate to Virtual Machines service account in the host project, you must grant this service account the `roles/vmmigration.serviceAgent` role to be able to create the image in the target project.  
  
## Choose a target project

To host the machine image, you must create or choose a target project. A target project defines the destination project for a machine image. For more information on creating or choosing a target project, see [Adding a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

## Import a machine image to Compute Engine

You can import a machine image to Compute Engine using the Google Cloud console, Google Cloud CLI, or REST API commands.

When you import a machine image, Migrate to Virtual Machines creates some temporary resources, such as VMs or disks, in the target project. These temporary resources are deleted when the machine image import process is complete.

###  Console 

To import a machine image to Compute Engine using the Google Cloud console, use the following steps.

  1. Open the Migrate to Virtual Machines page in the Google Cloud console.

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Machine Image Imports** tab.

  3. Click **Create a machine image**.

  4. Define the characteristics of the image. The following table lists the parameters that you can set for your machine image.

Section title | Field name | Description  
---|---|---  
**General** | Name | The name of the machine image that you want to create. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).  
| Machine image import ID | An ID that represents the machine image import resource. When you import a machine image to Compute Engine, Migrate to Virtual Machines first creates a machine image import resource. The machine image import resource represents the machine image import job. You can use the Machine Image import ID to get the link to the machine image that was imported as part of the machine image import process.  
| Source file input | The file from which you want to import the machine image. Click **Browse** to view the list of buckets in your current project, and select the file from which you want to import the machine image.   
If you want to import a machine image from a bucket from another project, you must enter the path in the format _bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view). When you copy the path, make sure that you don't copy the `gs://` prefix.   
Note that you can only import machine images from `.ova` and `.ovf` files.   
| Region | The region in which you want to create the machine image. For a list of supported regions, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
| Target project | The target project in which you want to create the machine image. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).   
| Auto-select Compute Engine machine type | Automatically selects the machine type from the source file. This option is enabled by default. If you want to manually select the machine type series and machine type, click this field to the off position.   
| Machine type series | Select the machine type series for the machine image. This field is visible only when the **Auto-select GCE machine type** option is disabled. Note that the machine type series available for selection is dependent on the region you've selected. For more information, see [Predefined machine types](https://docs.cloud.google.com/compute/docs/machine-resource#predefined-types).   
| Machine type | Select the machine type.   
| Description | (Optional) Add a description for the machine image.  
| Skip OS adaptation | To skip OS adaptation, click the **Skip OS adaptation** toggle to the on position.   
To function properly on Google Cloud, VMs created from imported machine images require changes to be made to their configuration. These changes are referred to as _OS adaptations_. Migrate to Virtual Machines performs OS adaptations automatically in the machine image import process. For more information, see [Adapt VM instances to run on Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations).  
| Generalize | To generalize the machine image, click the **Generalize** toggle to the on position. When you create an instance from a machine image, Windows adds some unique information to the instance. Generalize is a process that removes this information so that you can create multiple instances from the same machine image.  
**Licenses** | License type | Compute Engine supports pay as you go (PAYG) licenses and bring your own licenses (BYOL) for your deployed VMs. The default license type for a migrated VM is assigned by Migrate to Virtual Machines based on the migrated operating system, as described in [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).   
If your operating system supports multiple license types, you can override the default license type to explicitly specify a license type of PAYG or BYOL.   
**Note:** Some operating system types, such as CentOS and Debian, don't support a license. Other operating systems only support one type of license. Attempting to set an unsupported license type causes an error when you attempt to import the machine image.  
**Additional licenses** | Additional licenses | You can add up to 10 additional licenses to the VM instance created from the imported machine image using a valid URL format. For example, you can add additional licenses using the following URL format:   

         
         https://www.googleapis.com/compute/beta/projects/windows-sql-cloud/global/licenses/sql-server-2012-enterprise  
  
| Labels | To organize your project, add labels as key-value pairs to your resources. See [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).   
**Encryption** | Google-managed encryption key | Choose this option to use Google-owned and Google-managed encryption key to encrypt your data during the import process. For more information, see [encrypts data when it is at rest](https://cloud.google.com/docs/security/encryption/default-encryption/).   
| Customer managed encryption key | Choose this option to use customer-managed encryption keys (CMEK) to encrypt your data during the import process, and the data of the image created by the import process. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [CMEK](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data. These encryption keys are created, managed, and owned by you. For more information, see [ Protect resources by using Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin).   
When you add a CMEK, you must grant permissions as described in the following table. | Role | Permissions required | Description  
---|---|---  
[Cloud VM Migration Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-vm-migration-service-account) | `roles/vmmigration.serviceAgent` | Grant this permission to the Compute Engine service account to encrypt data of the machine image created during the import process.  
[Compute Engine Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent) | `roles/compute.serviceAgent` | Grant this permission to the Migrate to Virtual Machines service agent to encrypt the data during the import process.  
  5. Select **Create**.




###  gcloud 

To import a machine image to Compute Engine using the Google Cloud CLI, use the following request.
    
    
    gcloud compute migration machine-image-imports create IMAGE_NAME \
    --source-file=SOURCE_FILE \
    --location=REGION_ID \
    --target-project=projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT
    

Replace the following:

  * `IMAGE_NAME`: the name of the machine image that you want to create. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
  * `SOURCE_FILE`: the file from which you want to import the machine image. Enter the path in the format _gs://bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view). Note that you can only import images from `.ovf` and `.ova` files.
  * `REGION_ID`: the region in which you want the machine image import process to run. The machine image is created in the closest multi-region. If you want the machine image to be created in a region, verify that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `HOST_PROJECT_ID`: the name of the host project from which you want to migrate the machine image.
  * `TARGET_PROJECT`: the target project in which you want to create the machine image. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).



For more information, see [`gcloud migration vms machine-image-imports`](https://docs.cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports)

###  REST API 

To import a machine image to Compute Engine using the REST API, use the following steps.

  1. Create a machine image import resource using the following request.
         
         POST https://vmmigration.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/REGION_ID/imageImports?imageImportId=IMPORT_NAME
         {
         "cloudStorageUri": "SOURCE_FILE",
         "machineImageTargetDefaults": {
         "imageName": "IMAGE_NAME",
         "targetProject": "projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT",
         ...
         }
         }
         

Replace the following:

     * `HOST_PROJECT_ID`: the name of the host project from which you want to migrate the machine image.
     * `REGION_ID`: the region in which you want the machine image import process to run. The machine image is created in the closest multi-region. If you want the machine image to be created in a region, verify that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `SOURCE_FILE`: the file from which you want to import the machine image. Enter the path in the format _gs://bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view). Note that you can only import machine images from `.ova` and `.ovf` files.
     * `IMAGE_NAME`: the name of the machine image that you want to create. For more information on the naming rules, see [Naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     * `TARGET_PROJECT`: the target project in which you want to create the machine image. If you've not already added a target project, do so using the instructions given in [Add a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

In this example, `IMPORT_NAME` is an ID that represents the machine image import resource. When you import an machine image to Compute Engine, Migrate to Virtual Machines creates an first creates an machine image import resource. The machine image import resource represents the machine image import process. You can use the `IMPORT_NAME` to get the link to the machine image that was imported as part of the machine image import process.

See the following table for the full list of machine image import create request fields supported fields.

Field name | Description  
---|---  
`cloudStorageUri` |  The path of the file from which you want to import the machine image. Enter the path in the format _gs://bucket/folder/file_. To get the path of an object inside a bucket, see [View object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).   
Note that you can only import machine images from `.ovf` and `.ova` files.   
`machineImageTargetDefaults.targetProject` |  The target project in which you want to create the machine image. For more information, see [target project API reference](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.targetProjects/list). For example,   
`projects/HOST_PROJECT_ID/locations/global/targetProjects/TARGET_PROJECT`   
In the example, replace the following: 
     * `HOST_PROJECT_ID`: the name of the host project from which you want to migrate the machine image.
     * `TARGET_PROJECT`: the target project in which you want to create the image.   
`machineImageTargetDefaults.machine_image_name` |  The name of the machine image to be created. For more information on the naming rules, see [resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).   
`machineImageTargetDefaults.description` |  (Optional) A description of the machine image.   
`machineImageTargetDefaults.machine_type` |  (Optional) The machine to create the machine image with. If you don't specify the machine type, Migrate to Virtual Machines chooses a relevant machine type based on the information from the source machine image.   
`machineImageTargetDefaults.labels` |  To organize your project, add labels as key-value pairs to your resources. See [Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).   
`machineImageTargetDefaults.tags` |  Add any tags that you want to attach to the machine image. See [Manage tags for resources](https://docs.cloud.google.com/compute/docs/tag-resources).   
`machineImageTargetDefaults.additionalLicenses` |  You can add up to 10 additional licenses to the VM instance created from the imported machine image using a valid URL format. For example, you can add additional licenses using the following URL format:   

    
    https://www.googleapis.com/compute/beta/projects/windows-sql-cloud/global/licenses/sql-server-2012-enterprise  
  
`machineImageTargetDefaults.service_account` | Specify the service account on the target project used by the machine image. By default, no service account is assigned to the machine image.  
If you create a Compute Engine instance from a machine image and plan to run an application on it, the instance might need access to other gcloud CLI services and APIs. [Create a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount) in the target project with the necessary permissions to access these services and APIs before creating the Compute Engine instance. Then, specify that service account here. For more information, see [set up a VM to run as a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using).  
To attach the service account to the Compute Engine instance, your user account on the Migrate to Virtual Machines host project requires the necessary permissions. For more information, see [Configuring permissions on target project service account](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine).   
`machineImageTargetDefaults.shielded_instance_config` | (Optional) Enable Shielded VM on this instance. Shielded VMs are hardened by a set of security controls that help defend against rootkits and bootkits. See [What is Shielded VM?](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)  
`machineImageTargetDefaults.singleRegionStorage` |  Set this flag to true if you want the machine image `storageLocations` to be a region. If you set this flag to false, the closest multi-region is selected.  
`machineImageTargetDefaults.skip_os_adaptation` |  Set this flag to true if you want to skip OS adaptation.   
To function properly on Google Cloud, VMs created from imported machine images require changes to be made to their configuration. These changes are referred to as _OS adaptations_. Migrate to Virtual Machines performs OS adaptations automatically in the machine image import process. For more information, see [Adapt VM instances to run on Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations).  
`machineImageTargetDefaults.osAdaptationParameters.licenseType` |  The license type you want to use for your machine image. Compute Engine supports pay as you go (PAYG) licenses and bring your own licenses (BYOL) for your deployed VMs. The default license type for a migrated VM is assigned by Migrate to Virtual Machines based on the migrated operating system, as described in [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).   
If your operating system supports multiple license types, you can override the default license type to explicitly specify a license type of PAYG or BYOL.   
**Note:** Some operating system types, such as CentOS and Debian, don't support a license. Other operating systems only support one type of license. Attempting to set an unsupported license type causes an error when you attempt to import the machine image.  
`machineImageTargetDefaults.osAdaptationParameters.network_interfaces` | Migrate to Virtual Machines lets you optionally create a machine images with multiple network interfaces (NICs). Each interface is attached to a different VPC network, giving that machine image access to different VPC networks in gcloud CLI.  
Before you add additional network interfaces, be aware of the following considerations:  

     * Attaching multiple network interfaces to the same VPC network is not supported. While the configuration might get save, the instantiation of the VM will fail.
     * After a Compute Engine instance is instantiated from a machine image, you cannot add or remove a network interface on the created instance.   
To add or remove a network interface: 
       * Select **Add network interface** to add an additional network interface to the Compute Engine instance. You can set all of the same options as you do with the initial network interface.  

For more information, see [Creating instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).   
`machineImageTargetDefaults.osAdaptationParameters.generalize` |  Set this flag to true if you want to generalize the machine image.   
When you create an instance from an machine image, Windows adds some unique information to the instance. Generalization is a process that removes this information so that you can create multiple instances from the same machine image.  
`machineImageTargetDefaults.encryption` |  The Google-owned and Google-managed encryption key that you want to use to encrypt your data during the import process. For more information, see [Default encryption at rest](https://cloud.google.com/docs/security/encryption/default-encryption/).   
  
Use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) to encrypt the data of the machine image. These encryption keys are created, managed, and owned by you. For more information, see [Protect resources by using Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin).   
  
**Note:** The encryption key that you select for use during the import process will also be used for the output image.   
  
When you add a CMEK, you must grant permissions as described in the following table. | Role | Permissions required | Description  
---|---|---  
[Cloud VM Migration Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-vm-migration-service-account) | roles/vmmigration.serviceAgent | Grant this permission to the Compute Engine service account to encrypt data of the machine image created during the import process.  
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
    

  2. Check if the machine image import job is complete by polling the operation using the following command.
         
         GET https://vmmigration.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID
         

Replace the following:

     * `HOST_PROJECT_ID`: the name of the host project from which you are migrating the machine image.
     * `REGION_ID`: the region in which you want the machine image import process to run. The machine image is created in the closest multi-region. If you want the machine image to be created in a region, verify that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `OPERATION_ID`: the operation ID of the migrate job.

You should see an operation completion response similar to the following sample response.
    
    {
        "done": true,
        "name": "projects/HOST_PROJECT_ID/locations/REGION_ID/operations/OPERATION_ID",
        "response": {
          "@type": "type.googleapis.com/google.cloud.vmmigration.v1.ImageImport",
          "name": "projects/HOST_PROJECT_ID/locations/us-central1/imageImports/IMPORT_NAME",
          "cloudStorageUri": "SOURCE_FILE",
          "createTime": "2023-10-31T09:04:04.413664947Z",
          "machineImageTargetDefaults": {
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
    

  3. Monitor the machine image import job for completion using the following command.
         
         GET https://vmmigration.googleapis.com/v1/projects/HOST_PROJECT_ID/locations/REGION_ID/imageImports/IMPORT_NAME/imageImportJobs/image-import-job
         

Replace the following:

     * `HOST_PROJECT_ID`: the name of the host project from which you are migrating the machine image.
     * `REGION_ID`: the region in which you want the machine image import process to run. The machine image is created in the closest multi-region. If you want the machine image to be created in a region, verify that `singleRegionStorage` is set to true. For a list of supported regions, see [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).
     * `IMPORT_NAME`: the ID that represents the machine image import resource. When you import an machine image to Compute Engine, Migrate to Virtual Machines creates an first creates an machine image import resource. The machine image import resource represents the machine image import process. You can use the `IMPORT_NAME` to get the link to the machine image that was imported as part of the machine image import process.

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
