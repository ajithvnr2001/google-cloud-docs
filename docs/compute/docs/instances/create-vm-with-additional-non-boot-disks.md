---
url: https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks/
title: Create an instance with additional non-boot disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:33.720879+00:00
---

# Create an instance with additional non-boot disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance with additional non-boot disks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create and attach additional non-boot disks to a Compute Engine instance when you create the instance.

The information in this document applies to creating a compute instance with zonal disks that aren't in a Hyperdisk pool. The following list describes related tasks and the relevant documentation.

  * To create an instance that uses disks in a Hyperdisk pool, see [Create a VM that uses disks in a Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity#create-vm).
  * To create a disk in multi-writer mode, you must [create the disk](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk) first, and then [attach the disk to the instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks). You can't create the disk at the same time that you create the instance.

  * To enable high availability, use regional disks for your boot and non-boot disks. For more information, see [Create an instance with a new regional boot disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#create-vm-repd-boot-disk) and [Create a new instance with additional regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_with_vm).

  * To attach existing disks to an instance, see [Attach a non-boot disk to an instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks).




## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create an instance with added non-boot disks, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create an instance with added non-boot disks. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an instance with added non-boot disks:

  * `compute.instances.create` on the project
  * To create a disk for the instance: `compute.disks.create` on the project 
  * To create a disk from an image: `compute.images.useReadOnly` on the source image 
  * To create a disk from a standard or archive snapshot: `compute.snapshots.useReadOnly` on the source snapshot 
  * To create a disk from an instant snapshot: `compute.instantSnapshots.useReadOnly` on the source instant snapshot 
  * To create a disk from an existing disk: `compute.disks.useReadOnly` on the source disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

The number, total combined size, and type of the disks that you can attach to an instance depends on the instance's machine type.

For example, C4 instances don't support Persistent Disk. Also, the combined size of all disks attached to a `c4-standard-2` instance can't exceed 257 TiB, but for a `c4-standard-192` instance, the limit is 512 TiB.

The detailed limits for each machine series are in the **Supported disk types** section within the machine series' documentation. To view the limits for your new instance's machine series, refer to the corresponding link in the following table.

General purpose  
machine types | Compute-optimized  
machine types | Memory-optimized  
machine types | Accelerator-optimized  
machine types | Storage-optimized  
machine types  
---|---|---|---|---  
  
  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_disks)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_disks)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4)
  * [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4a)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_c4d)
  * [E2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_disks)
  * [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_disks)
  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_disks)
  * [N2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_disks)
  * [N4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4)
  * [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4a)
  * [N4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#supported_disk_types_for_n4d)
  * [T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_disks)
  * [T2D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_disks)

| 

  * [C2](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_disks)
  * [C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_disks)
  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_disks)
  * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_disks)

| 

  * [M1](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_disks)
  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_disks)
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_disks)
  * [M4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_disks)
  * [X4](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x4_disks)
  * [X5](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#x5_disks)

| 

  * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-disks)
  * [A3+H100](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-disks)
  * [A3+H200](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-disks)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-disks)
  * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-disks)
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-disks)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-disks)
  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-disks)
  * [N1+GPU](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_disks)

| 

  * [Z3](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_disks)
  * [Z4D](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_disks)
  * [Z4M](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_disks)

  
  
## Disk size limits and reference names

The size you specify for a regional disk must be within the ranges listed in following table.

When you create a disk with the Google Cloud CLI, REST, or the Cloud Client Libraries for Compute Engine, you specify the type of disk to create with the corresponding value of the **Reference name** column in the following table.

Disk type | Reference name | Minimum size | Maximum size | Default size  
---|---|---|---|---  
Hyperdisk Balanced | `hyperdisk-balanced` | 4 GiB | 64 TiB1 | 100 GiB  
Hyperdisk Balanced High Availability | `hyperdisk-balanced-high-availability` | 4 GiB | 64 TiB | 100 GiB  
Hyperdisk Extreme | `hyperdisk-extreme` | 64 GiB | 64 TiB | 1 TiB  
Hyperdisk Throughput | `hyperdisk-throughput` | 2 TiB | 32 TiB | 2 TiB  
Hyperdisk ML | `hyperdisk-ml` | 4 GiB | 64 TiB | 100 GiB  
Balanced Persistent Disk | `pd-balanced` | Zonal: 10 GiB  
Regional: 10 GiB | 64 TiB | 100 GiB  
Performance (SSD) Persistent Disk | `pd-ssd` | Zonal: 10 GiB  
Regional: 10 GiB | 64 TiB | 100 GiB  
Standard Persistent Disk | `pd-standard` | Zonal: 10 GiB  
Regional: 200 GiB | 64 TiB | 500 GiB  
Extreme Persistent Disk | `pd-extreme` | 500 GiB | 64 TiB | 1 TiB  
1**[Preview](https://cloud.google.com/products#product-launch-stages)** : C4 supports a maximum disk size of 128 TiB. For access to this feature, contact [hyperdisk-questions@google.com](https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=hyperdisk-questions@google.com). 

## Create an instance with new additional non-boot disks

To create an instance that has additional non-boot disks created and attached, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**.

The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. In the **Region** field, specify the region where you want your instance.
     3. Optional: In the **Zone** field, select a zone for this instance.

The default selection is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability. 

     4. Select the machine family for your instance. The Google Cloud console then displays the machine series that are available for your selected machine family. The following machine family options are available:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**
     5. In the **Series** column, select the machine series for your instance.

If you selected **GPUs** as the machine family in the previous step, then select the **GPU type** that you want. The machine series is then automatically selected for the selected GPU type.

     6. In the **Machine type** section, select the machine type for your instance.

  3. In the navigation menu, click **OS and storage**. The **Operating system and storage** pane appears.

  4. To configure your boot disk, click **Change**. The **Boot disk** pane appears and displays the **Public images** tab.

  5. Configure the data source for the boot disk in one of the following ways:

**Note:** Unless you explicitly choose a different boot disk, if the name of the new instance matches the name of an existing disk, then the existing disk automatically attaches to the new instance as the boot disk.

     * To choose a public image as the data source for your boot disk, in the **Public images** tab, specify the following: 
       1. In the **Operating system** list, select the OS type.
       2. In the **Version** list, select the OS version.
       3. In the **Boot disk type** list, select the type of the boot disk.
       4. In the **Size (GB)** field, specify the size of the boot disk.
     * To choose a custom image as the data source for your boot disk, click **Custom images** and then, in the **Custom images** tab that appears, specify the following: 
       1. To select the image project, click **Change** , and then select the project that contains the image.
       2. In the **Image** list, select the image that you want to import.
       3. In the **Boot disk type** list, select the type of the boot disk.
       4. In the **Size (GB)** field, specify the size of the boot disk.
     * To choose a standard snapshot as the data source for your boot disk, click **Snapshots** and then, in the **Snapshots** tab that appears, specify the following: 
       1. In the **Snapshot** list, select the snapshot.
       2. In the **Boot disk type** list, select the type of the boot disk.
       3. In the **Size (GB)** field, specify the size of the boot disk.
     * To choose an archive snapshot as the data source for your boot disk, click **Archive snapshots** and then, in the **Archive snapshots** tab that appears, specify the following: 
       1. In the **Archive snapshot** list, select the archive snapshot.
       2. In the **Boot disk type** list, select the type of the boot disk.
       3. In the **Size (GB)** field, specify the size of the boot disk.
     * To choose an existing disk as your boot disk, click **Existing disks**. Then, in the **Existing disks** tab that appears, select an existing disk in the **Disk** list. _This option uses the existing disk as the boot disk and doesn't create a new disk._
  6. Optional: If the boot disk is a Hyperdisk Balanced volume, you can set performance limits for the new disk. The values that you specify must be in the range of supported values.

  7. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section. 

     * Select the disk attachment mode in the **Mode** field.
     * Choose to keep or delete the disk when the instance is deleted by selecting the option in the **Deletion rule** field.
     * To make identifying the disk easier from within the guest OS, specify a custom device name. Under the heading **Device name** , select the option **Use a custom device name**. In the **Device name** field, enter a string to use as a symlink for the disk. 
  8. To confirm your boot disk options and return to the **OS and storage** pane, click **Select**.

  9. To create a new non-boot disk and attach it to your instance, follow the following steps for each disk that you want to add.

     1. In the **Additional disks** section, click **Add new disk**. The **Add new disk** pane appears.

     2. In the **Disk configuration** section, in the **Name** field, specify a name for the non-boot disk.

     3. Optional: in the **Description** field, specify a description for the disk.

     4. Select the data source for the new disk:

        * To create an empty, unformatted disk, in the **Disk source type** list, select **Blank disk**.
        * To create a copy of existing data, select the source type for the non-boot disk.
     5. In the **Disk type** list, select a type for the non-boot disk. The machine type must support the disk type.

     6. In the **Size** field, specify the size of the non-boot disk.

     7. Optional: If the new disk is a Hyperdisk volume, you can set performance limits for the new disk. The values that you specify must be in the range of supported values, and depend on the Hyperdisk type, as follows:

        * **Hyperdisk Balanced**. You can change the disk's **Size** , **Provisioned IOPS** , and **Provisioned Throughput**
        * **Hyperdisk Extreme**. You can change the disk's **Size** and **Provisioned IOPS**.
        * **Hyperdisk ML**. You can change the disk's **Size** and **Provisioned Throughput**.
        * **Hyperdisk Throughput**.You can change the disk's **Size** and **Provisioned Throughput**.
     8. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section. 

        * Select the disk attachment mode in the **Mode** field.
        * Choose to keep or delete the disk when the instance is deleted by selecting the option in the **Deletion rule** field.
        * To make identifying the disk easier from within the guest OS, specify a custom device name. Under the heading **Device name** , select the option **Use a custom device name**. In the **Device name** field, enter a string to use as a symlink for the disk. 
     9. To confirm your options and return to the **OS and storage** pane, click **Save**.

Repeat this step for each non-boot disk that you want to create and attach to your instance.

  10. Optional: specify back up and replication options for your compute instance. In the navigation menu, click **Data protection**. In the **Data protection** pane that appears, specify how you want to back up and replicate the data for your compute instance by doing the following.

**Caution:** The data backup and replication settings that you specify while creating an instance using the Google Cloud console are applied only when your selected instance and disk configurations support those options. You must verify that your configuration for the compute instance and each disk meets the requirements for each data protection option that you specify. For more information, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).
     1. To specify how you want to back up data, select an option for **Back up your data**.
     2. To specify how you want to replicate data, do the following:

        1. If you want new disks for the instance to be synchronously replicated in a second zone by using [regional disks types](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk), select the **Regional disks** checkbox.
**Important:** The **Regional disks** checkbox doesn't affect existing disks. If you want to change an existing zonal disk to a regional disk, see [Change a zonal disk to a regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#migrate-repd) instead.
        1. If you want disks for the instance to be replicated in a second region using [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about), select the **Asynchronous replication** checkbox.
     3. To use the specified data protection options on only non-boot disks, select the **Exclude boot disks** checkbox.

**Important:** This option doesn't affect backup plans, which can't exclude boot disks.
  11. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. Go to the **Firewall** section.
     2. To permit HTTP or HTTPS traffic to the instance, select **Allow HTTP traffic** or **Allow HTTPS traffic**.

The Compute Engine adds a network tag to your instance and creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS). The network tag associates the firewall rule with the instance. For more information, see [Firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls) in the Cloud Next Generation Firewall documentation.

  12. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  13. To create and start the instance, click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance with additional non-boot disks.

You can add up to 127 non-boot disks while you're creating your instance. Specify the `--create-disk` flag for each non-boot disk you create.

To create non-boot disks from a public or stock image, specify the `image` or `image-family` and `image-project` properties with the `--create-disk` flag. To create a blank disk, don't include these properties.

You can optionally include values for the following properties:

     * Disk size: use the `--size` property.
     * Disk type: use the `--type` property.
     * Regional disks: include the `replica-zones` property.
    
    gcloud compute instances create INSTANCE_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --image-project=BOOT_DISK_IMAGE_PROJECT \
        BOOT_DISK_IMAGE_FLAG \
        --create-disk name=DISK_NAME,device-name=DISK_DEVICE_NAME,size=SIZE_GB,type=DISK_TYPE,image=DISK_IMAGE,image-project=DISK_IMAGE_PROJECT,replica-zones=^:^ZONE:REMOTE_ZONE,boot=false
    

Replace the following:

     * `INSTANCE_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new instance.
     * `ZONE`: the zone to create the instance in.
     * `MACHINE_TYPE`: the machine type for the instance. For example, `c3-standard-4`.
     * `BOOT_DISK_IMAGE_PROJECT`: the project containing the image. For example, for Debian, `debian-cloud`. To find the image project for public images, go to the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page. In the **GA versions** section for your OS, the image project is listed in the **Image project** column of the **General information** tab.
     * `BOOT_DISK_IMAGE_FLAG`: specify one of the following:

       * Use the `--image IMAGE_NAME` flag to specify a specific version of a public or custom image. For example, `--image debian-12-bookworm-v20241112`.

       * Use the `--image-family IMAGE_FAMILY_NAME` flag to specify an [image family](https://docs.cloud.google.com/compute/docs/images#image_families). This creates the instance that uses the most recent, non-deprecated OS image in the image family. For example, if you specify `--image-family debian-12`, then Compute Engine uses the latest version of the OS image in the Debian 12 image family when creating the instance.

     * For additional disks, replace the following:

       * `DISK_NAME`: optional: the name of the non-boot disk.
       * `SIZE_GB`: optional: the size of the non-boot disk.
       * `DISK_TYPE`: the type of the disk. For example, `hyperdisk-balanced`. The machine type must support the disk type.
       * `DISK_DEVICE_NAME`: optional: the name for the disk that is displayed to the guest OS after the instance is created.
       * `DISK_IMAGE`: optional: To create a disk from an existing image, specify one of the following: 
         * `image=DISK_IMAGE_NAME`: name of the image that you want to use to create the non-boot disk, for example, `debian-12-bookworm-v20260210`.
         * `image-family=DISK_IMAGE_FAMILY`: an image family to use when creating a non-boot disk, for example, `debian-12`.
       * `DISK_IMAGE_PROJECT`: optional: to create a non-boot disk from an existing image, specify the image project that contains the image.
       * `REMOTE_ZONE`: optional: if creating a regional disk, specify the zone where the disk should be replicated to, for example, `us-central1-b`.

For blank disks, don't specify the `image`, `image-project`, or `image-family` parameters.

For zonal disks, don't specify the disk property `replica-zones`.




###  Terraform 

To generate the Terraform code, you can use the **Equivalent code** component in the Google Cloud console. 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.
  3. Specify the parameters you want.
  4. At the top or bottom of the page, click **Equivalent code** , and then click the **Terraform** tab to view the Terraform code.



###  Go 

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createWithAdditionalDisk create a new VM instance with Debian 10 operating system and a 11 GB additional empty disk.
    func createWithAdditionalDisk(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details.
    	newestDebianReq := &computepb.GetFromFamilyImageRequest{
    		Project: "debian-cloud",
    		Family:  "debian-12",
    	}
    	newestDebian, err := imagesClient.GetFromFamily(ctx, newestDebianReq)
    	if err != nil {
    		return fmt.Errorf("unable to get image from family: %w", err)
    	}
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    			Disks: []*computepb.AttachedDisk{
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:  proto.Int64(10),
    						SourceImage: newestDebian.SelfLink,
    						DiskType:    proto.String(fmt.Sprintf("zones/%s/diskTypes/pd-standard", zone)),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb: proto.Int64(11),
    						DiskType:   proto.String(fmt.Sprintf("zones/%s/diskTypes/pd-standard", zone)),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(false),
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    			},
    			MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					Name: proto.String("global/networks/default"),
    				},
    			},
    		},
    	}
    
    	op, err := instancesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance created\n")
    
    	return nil
    }
    

###  Java 

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type;
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.Vector;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstancesAdvanced {
    
      /**
       * Create an AttachedDisk object to be used in VM instance creation. Uses an image as the source
       * for the new disk.
       *
       * @param diskType the type of disk you want to create. This value uses the following format:
       * "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)". For example:
       * "zones/us-west3-b/diskTypes/pd-ssd"
       * @param diskSizeGb size of the new disk in gigabytes
       * @param boot boolean flag indicating whether this disk should be used as a boot disk of an
       * instance
       * @param sourceImage source image to use when creating this disk. You must have read access to
       * this disk. This can be one of the publicly available images or an image from one of your
       * projects. This value uses the following format:
       * "projects/{project_name}/global/images/{image_name}"
       * @return AttachedDisk object configured to be created using the specified image.
       */
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) diskFromImage(String diskType, int diskSizeGb, boolean boot,
          String sourceImage) {
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk =
            [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                .setBoot(boot)
                // Remember to set auto_delete to True if you want the disk to be deleted when
                // you delete your VM instance.
                .setAutoDelete(true)
                .setType(Type.PERSISTENT.toString())
                .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                    [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                        .setSourceImage(sourceImage)
                        .setDiskSizeGb(diskSizeGb)
                        .setDiskType(diskType)
                        .build())
                .build();
        return disk;
      }
    
    
      /**
       * Create an AttachedDisk object to be used in VM instance creation. The created disk contains no
       * data and requires formatting before it can be used.
       *
       * @param diskType the type of disk you want to create. This value uses the following format:
       * "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)". For example:
       * "zones/us-west3-b/diskTypes/pd-ssd"
       * @param diskSizeGb size of the new disk in gigabytes
       * @return AttachedDisk object configured to be created as an empty disk.
       */
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) emptyDisk(String diskType, int diskSizeGb) {
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk =
            [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                .setBoot(false)
                // Remember to set auto_delete to True if you want the disk to be deleted when
                // you delete your VM instance.
                .setAutoDelete(true)
                .setType(Type.PERSISTENT.toString())
                .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                    [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                        .setDiskSizeGb(diskSizeGb)
                        .setDiskType(diskType)
                        .build())
                .build();
        return disk;
      }
    
      /**
       * Send an instance creation request to the Compute Engine API and wait for it to complete.
       *
       * @param project project ID or project number of the Cloud project you want to use.
       * @param zone name of the zone to create the instance in. For example: "us-west3-b"
       * @param instanceName name of the new virtual machine (VM) instance.
       * @param disks a list of compute_v1.AttachedDisk objects describing the disks you want to attach
       * to your new instance.
       * @param machineType machine type of the VM being created. This value uses the following format:
       * "zones/{zone}/machineTypes/{type_name}".
       * For example: "zones/europe-west3-c/machineTypes/f1-micro"
       * @param network name of the network you want the new instance to use. For example:
       * "global/networks/default" represents the network named "default", which is created
       * automatically for each project.
       * @param subnetwork name of the subnetwork you want the new instance to use. This value uses the
       * following format: "regions/{region}/subnetworks/{subnetwork_name}"
       * @return Instance object.
       */
      private static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createWithDisks(String project, String zone, String instanceName,
          Vector<AttachedDisk> disks, String machineType, String network, String subnetwork)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          // Use the network interface provided in the networkName argument.
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface;
          if (subnetwork != null) {
            networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                .setName(network).setSubnetwork(subnetwork)
                .build();
          } else {
            networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                .setName(network).build();
          }
    
          machineType = String.format("zones/%s/machineTypes/%s", zone, machineType);
    
          // Bind `instanceName`, `machineType`, `disk`, and `networkInterface` to an instance.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instanceResource =
              [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
                  .setName(instanceName)
                  .setMachineType(machineType)
                  .addAllDisks(disks)
                  .addNetworkInterfaces(networkInterface)
                  .build();
    
          System.out.printf("Creating instance: %s at %s ", instanceName, zone);
    
          // Insert the instance in the specified project and zone.
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstanceResource(instanceResource).build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
              insertInstanceRequest);
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance creation failed ! ! " + response);
            return null;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
    
          return instancesClient.get(project, zone, instanceName);
        }
      }
    
      /**
       * Create a new VM instance with Debian 13 operating system and a 11 GB additional empty disk.
       *
       * @param project project ID or project number of the Cloud project you want to use.
       * @param zone name of the zone to create the instance in. For example: "us-west3-b"
       * @param instanceName name of the new virtual machine (VM) instance.
       * @return Instance object.
       */
      public static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createWithAdditionalDisk(String project, String zone, String instanceName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
          // List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) image = imagesClient.[getFromFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html#com_google_cloud_compute_v1_ImagesClient_getFromFamily_com_google_cloud_compute_v1_GetFromFamilyImageRequest_)("debian-cloud", "debian-13");
          String diskType = String.format("zones/%s/diskTypes/pd-standard", zone);
          Vector<AttachedDisk> disks = new Vector<>();
          disks.add(diskFromImage(diskType, 10, true, image.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html#com_google_cloud_compute_v1_Image_getSelfLink__)()));
          disks.add(emptyDisk(diskType, 11));
          return createWithDisks(project, zone, instanceName, disks, "n1-standard-1",
              "global/networks/default", null);
        }
      }

###  Node.js 

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new VM instance with Debian 10 operating system and a 11 GB additional empty disk.
    async function createWithAdditionalDisk() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details.
      const [newestDebian] = await imagesClient.getFromFamily({
        project: 'debian-cloud',
        family: 'debian-11',
      });
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
          disks: [
            {
              initializeParams: {
                diskSizeGb: '10',
                sourceImage: newestDebian.selfLink,
                diskType: `zones/${zone}/diskTypes/pd-standard`,
              },
              autoDelete: true,
              boot: true,
              type: 'PERSISTENT',
            },
            {
              initializeParams: {
                diskSizeGb: '11',
                diskType: `zones/${zone}/diskTypes/pd-standard`,
              },
              autoDelete: true,
              boot: false,
              type: 'PERSISTENT',
            },
          ],
          machineType: `zones/${zone}/machineTypes/n1-standard-1`,
          networkInterfaces: [
            {
              name: 'global/networks/default',
            },
          ],
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance created.');
    }
    
    createWithAdditionalDisk();

###  Python 

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def get_image_from_family(project: str, family: str) -> compute_v1.Image:
        """
        Retrieve the newest image that is part of a given family in a project.
    
        Args:
            project: project ID or project number of the Cloud project you want to get image from.
            family: name of the image family you want to get image from.
    
        Returns:
            An Image object.
        """
        image_client = compute_v1.ImagesClient()
        # List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
        newest_image = image_client.get_from_family(project=project, family=family)
        return newest_image
    
    
    def disk_from_image(
        disk_type: str,
        disk_size_gb: int,
        boot: bool,
        source_image: str,
        auto_delete: bool = True,
    ) -> compute_v1.AttachedDisk:
        """
        Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
        source for the new disk.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            source_image: source image to use when creating this disk. You must have read access to this disk. This can be one
                of the publicly available images or an image from one of your projects.
                This value uses the following format: "projects/{project_name}/global/images/{image_name}"
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created using the specified image.
        """
        boot_disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = source_image
        initialize_params.disk_size_gb = disk_size_gb
        initialize_params.disk_type = disk_type
        boot_disk.initialize_params = initialize_params
        # Remember to set auto_delete to True if you want the disk to be deleted when you delete
        # your VM instance.
        boot_disk.auto_delete = auto_delete
        boot_disk.boot = boot
        return boot_disk
    
    
    def empty_disk(
        disk_type: str, disk_size_gb: int, boot: bool = False, auto_delete: bool = True
    ) -> compute_v1.AttachedDisk():
        """
        Create an AttachedDisk object to be used in VM instance creation. The created disk contains
        no data and requires formatting before it can be used.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created as an empty disk.
        """
        disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.disk_type = disk_type
        initialize_params.disk_size_gb = disk_size_gb
        disk.initialize_params = initialize_params
        # Remember to set auto_delete to True if you want the disk to be deleted when you delete
        # your VM instance.
        disk.auto_delete = auto_delete
        disk.boot = boot
        return disk
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        disks: list[compute_v1.AttachedDisk],
        machine_type: str = "n1-standard-1",
        network_link: str = "global/networks/default",
        subnetwork_link: str = None,
        internal_ip: str = None,
        external_access: bool = False,
        external_ipv4: str = None,
        accelerators: list[compute_v1.AcceleratorConfig] = None,
        preemptible: bool = False,
        spot: bool = False,
        instance_termination_action: str = "STOP",
        custom_hostname: str = None,
        delete_protection: bool = False,
    ) -> compute_v1.Instance:
        """
        Send an instance creation request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            disks: a list of compute_v1.AttachedDisk objects describing the disks
                you want to attach to your new instance.
            machine_type: machine type of the VM being created. This value uses the
                following format: "zones/{zone}/machineTypes/{type_name}".
                For example: "zones/europe-west3-c/machineTypes/f1-micro"
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
                "regions/{region}/subnetworks/{subnetwork_name}"
            internal_ip: internal IP address you want to assign to the new instance.
                By default, a free address from the pool of available internal IP addresses of
                used subnet will be used.
            external_access: boolean flag indicating if the instance should have an external IPv4
                address assigned.
            external_ipv4: external IPv4 address to be assigned to this instance. If you specify
                an external IP address, it must live in the same region as the zone of the instance.
                This setting requires `external_access` to be set to True to work.
            accelerators: a list of AcceleratorConfig objects describing the accelerators that will
                be attached to the new instance.
            preemptible: boolean value indicating if the new instance should be preemptible
                or not. Preemptible VMs have been deprecated and you should now use Spot VMs.
            spot: boolean value indicating if the new instance should be a Spot VM or not.
            instance_termination_action: What action should be taken once a Spot VM is terminated.
                Possible values: "STOP", "DELETE"
            custom_hostname: Custom hostname of the new VM instance.
                Custom hostnames must conform to RFC 1035 requirements for valid hostnames.
            delete_protection: boolean value indicating if the new virtual machine should be
                protected against deletion or not.
        Returns:
            Instance object.
        """
        instance_client = compute_v1.InstancesClient()
    
        # Use the network interface provided in the network_link argument.
        network_interface = compute_v1.NetworkInterface()
        network_interface.network = network_link
        if subnetwork_link:
            network_interface.subnetwork = subnetwork_link
    
        if internal_ip:
            network_interface.network_i_p = internal_ip
    
        if external_access:
            access = compute_v1.AccessConfig()
            access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
            access.name = "External NAT"
            access.network_tier = access.NetworkTier.PREMIUM.name
            if external_ipv4:
                access.nat_i_p = external_ipv4
            network_interface.access_configs = [access]
    
        # Collect information into the Instance object.
        instance = compute_v1.Instance()
        instance.network_interfaces = [network_interface]
        instance.name = instance_name
        instance.disks = disks
        if re.match(r"^zones/[a-z\d\-]+/machineTypes/[a-z\d\-]+$", machine_type):
            instance.machine_type = machine_type
        else:
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
    
        instance.scheduling = compute_v1.Scheduling()
        if accelerators:
            instance.guest_accelerators = accelerators
            instance.scheduling.on_host_maintenance = (
                compute_v1.Scheduling.OnHostMaintenance.TERMINATE.name
            )
    
        if preemptible:
            # Set the preemptible setting
            warnings.warn(
                "Preemptible VMs are being replaced by Spot VMs.", DeprecationWarning
            )
            instance.scheduling = compute_v1.Scheduling()
            instance.scheduling.preemptible = True
    
        if spot:
            # Set the Spot VM setting
            instance.scheduling.provisioning_model = (
                compute_v1.Scheduling.ProvisioningModel.SPOT.name
            )
            instance.scheduling.instance_termination_action = instance_termination_action
    
        if custom_hostname is not None:
            # Set the custom hostname for the instance
            instance.hostname = custom_hostname
    
        if delete_protection:
            # Set the delete protection bit
            instance.deletion_protection = True
    
        # Prepare the request to insert an instance.
        request = compute_v1.InsertInstanceRequest()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        # Wait for the create operation to complete.
        print(f"Creating the {instance_name} instance in {zone}...")
    
        operation = instance_client.insert(request=request)
    
        wait_for_extended_operation(operation, "instance creation")
    
        print(f"Instance {instance_name} created.")
        return instance_client.get(project=project_id, zone=zone, instance=instance_name)
    
    
    def create_with_additional_disk(
        project_id: str, zone: str, instance_name: str
    ) -> compute_v1.Instance:
        """
        Create a new VM instance with Debian 10 operating system on a 20 GB disk
        and a 25 GB additional empty disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
    
        Returns:
            Instance object.
        """
        newest_debian = get_image_from_family(project="debian-cloud", family="debian-12")
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [
            disk_from_image(disk_type, 20, True, newest_debian.self_link),
            empty_disk(disk_type, 25),
        ]
        instance = create_instance(project_id, zone, instance_name, disks)
        return instance
    
    

###  REST 

You can create up to 127 non-boot disks at the time you create an instance by using the `initializeParams` property for each additional disk. Create additional disks with a public or private image. To add a blank disk, define the `initializeParams` entry with no `sourceImage` value. Include the disk property `replicaZones` to create regional disks instead of zonal disks.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "machineType":"zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
       "name":"VM_NAME",
       
       "disks":[
          {
             "initializeParams":{
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE"
             },
             "boot":true
          },
          {
             "initializeParams":{
                "diskSizeGb":"SIZE_GB",
                "sourceImage":"projects/DISK_IMAGE_PROJECT/global/images/DISK_IMAGE",
                "diskType":"DISK_TYPE"
             }
          },
          {
             "initializeParams":{
                "diskSizeGb":"SIZE_GB",
                "diskType":"DISK_TYPE"
             },
          },
          {
             "boot": false,
             "deviceName":"DISK_NAME",
             "initializeParams": {
                "diskType": "DISK_TYPE",
                "replicaZones": [
                   "projects/PROJECT_ID/zones/ZONE",
                   "projects/PROJECT_ID/zones/REMOTE_ZONE"
                ]
             }
          }
       ],
       
       
       "networkInterfaces":[
          {
             "network":"global/networks/NETWORK_NAME"
          }
       ],
       
      
       "shieldedInstanceConfig":{
          "enableSecureBoot":"ENABLE_SECURE_BOOT"
       }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project to create the VM in
  * `ZONE`: zone to create the VM in
  * `MACHINE_TYPE_ZONE`: zone containing the machine type to use for the new VM
  * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types), for the new VM
  * `VM_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM
  * `IMAGE_PROJECT`: [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) containing the image  
For example, if you specify `debian-10` as the image family, specify `debian-cloud` as the image project.
  * `IMAGE`: specify one of the following: 
    * `IMAGE`: a specific version of a public image

For example, `"sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200309"`

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images#image_families)

This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-10"`, Compute Engine creates a VM from the latest version of the OS image in the `Debian 10` image family.

  * For additional disks, replace the following:

    * `SIZE_GB`: disk size
    * `DISK_IMAGE` or
    * `DISK_IMAGE_FAMILY`: Specify either a source image or image family for the non-boot disk: 
      * `DISK_IMAGE`: name of the image that you want to use as a non-boot disk. For example, `"sourceImage": "projects/DISK_IMAGE_PROJECT/global/images/DISK_IMAGE"`. 
      * `DISK_IMAGE_FAMILY`: an image family to use as a non-boot disk. For example, `"sourceImage": "projects/DISK_IMAGE_PROJECT/global/images/family/DISK_IMAGE_FAMILY"`. 
    * `DISK_TYPE`: full or partial URL for the type of the disk type. For example, `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced`. The machine type must support the disk type. 
    * `DISK_NAME`: Optional. The disk name displayed to the guest OS after the VM is created.
    * `REMOTE_ZONE`: the zone to replicate the regional disk to

For blank disks, don't specify the `sourceImage` property.

For zonal disks, don't specify the `replicaZones` property.

  * `NETWORK_NAME`: the VPC network that you want to use for the VM. You can specify `default` to use your default network.
  * `ENABLE_SECURE_BOOT`: Optional: If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features, Compute Engine, by default, enables the [virtual trusted platform module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) and [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring). Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default.

If you specify `true` for `enableSecureBoot`, Compute Engine creates a VM with all three Shielded VM features enabled. After Compute Engine starts your VM, to [modify Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm) options, you must stop the VM.




After you create the instance, you must [format any blank disks and mount all the disks](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux). before you can use them.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
