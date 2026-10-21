---
url: https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk/
title: Create a new Hyperdisk volume \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:30.646827+00:00
---

# Create a new Hyperdisk volume  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a new Hyperdisk volume Stay organized with collections  Save and categorize content based on your preferences. 

You can use a Hyperdisk Balanced, Hyperdisk Extreme or Hyperdisk Throughput volume with your Compute Engine instance by completing the following tasks:

  * Create a blank, non-boot, and zonal Hyperdisk volume and attach it to your instance either during or after instance creation.
  * Format and mount the volume to provide access to a data or file system.



For Hyperdisk Balanced volumes, you can also create boot disks as well as data disks.

To add a new Hyperdisk Balanced High Availability disk to your instance, use the following procedures:

  * [Create a regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk)
  * [Create a new instance with regional boot disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#create-vm-repd-boot-disk)



To add an existing disk that contains data to an instance, see [Attach a non-boot disk to a VM](https://docs.cloud.google.com/compute/docs/disks/attach-disks).

For general information about Hyperdisk, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

## Before you begin

  * Review the [Hyperdisk limitations](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limitations) before adding a Hyperdisk volume to your compute instance. 
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

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to add a Hyperdisk volume to your instance, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to add a Hyperdisk volume to your instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to add a Hyperdisk volume to your instance:

  * To create and attach a Hyperdisk volume: 
    * `compute.disks.create` on the project
    * `compute.instances.attachDisk` on the instance
    * `compute.disks.use` on the volume that you want to attach to the instance
  * To format and mount the attached volume: `compute.instances.setMetadata` on the instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Supported values for Hyperdisk volumes

### Size limits and reference names for Hyperdisk

To create a Hyperdisk volume using the Google Cloud CLI, REST, or the Cloud Client Libraries for Compute Engine, you must indicate the Hyperdisk type to create by providing the value in the **Reference name** column in the following table.

The size you specify for a Hyperdisk volume must be within the ranges listed in following table.

Disk type | Reference name | Minimum size | Maximum size | Default size  
---|---|---|---|---  
Hyperdisk Balanced | `hyperdisk-balanced` | 4 GiB | 64 TiB1 | 100 GiB  
Hyperdisk Balanced High Availability | `hyperdisk-balanced-high-availability` | 4 GiB | 64 TiB | 100 GiB  
Hyperdisk Extreme | `hyperdisk-extreme` | 64 GiB | 64 TiB | 1 TiB  
Hyperdisk Throughput | `hyperdisk-throughput` | 2 TiB | 32 TiB | 2 TiB  
Hyperdisk ML | `hyperdisk-ml` | 4 GiB | 64 TiB | 100 GiB  
1**[Preview](https://cloud.google.com/products#product-launch-stages)** : C4 supports a maximum disk size of 128 TiB. For access to this feature, contact [hyperdisk-questions@google.com](https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=hyperdisk-questions@google.com). 

However, the total size of all the Hyperdisk volumes that's attached to an instance can't exceed the [ instance's Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

### Performance limits

The following table lists the limits for the performance that you can specify for each Hyperdisk type. However, the IOPS and throughput levels you can specify also depend on the volume's size. For a detailed summary of each limit, see the **Size and performance limits** section for [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits), [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#size_limits), [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits), [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#size_limits), and [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits).

Hyperdisk type | IOPS limit | Throughput limit (MiB/s)  
---|---|---  
Hyperdisk Balanced | 160,000 | 2,400  
Hyperdisk Balanced High Availability | 100,000 | 2,400  
Hyperdisk Extreme | 350,000 |  You can't provision a throughput level for Hyperdisk Extreme volumes. Each volume gets 250 MiB/s of throughput with every 1,000 IOPS, up to 5,000 MiB/s.  
Hyperdisk ML | You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 16 IOPS, up to 33,554,432 IOPS. | 2,097,152  
Hyperdisk Throughput | You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 4 IOPS, up to 9,600 IOPS. | 2,400  
  
## Add a Hyperdisk volume to your instance

You can create and attach a Hyperdisk volume by using any of the methods listed in this section.

The size, throughput, and IOPS that you specify when creating a Hyperdisk volume must be in the range of supported values.

When you create a Hyperdisk Balanced volume, you can optionally allow multiple instances to access the disk concurrently by creating the disk in multi-writer mode.

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance where you want to add a disk.

  3. On the **VM instance details** page, click **edit Edit**.

  4. In the **Storage** section, under **Additional disks** , click **Add new disk**.

  5. Specify a name for the disk, and optionally add a description.

  6. Under **Disk source type** , choose the data source for the disk:

     * To create a blank disk, select **Blank disk**.
     * To create the disk from an image: 
       1. Select **Image**.
       2. Under **Source image** , choose the source image for the disk.
     * To create the disk from an existing snapshot: 
       1. Select **Snapshot** , **Instant snapshot** or **Archive snapshot** , depending on whether the source snapshot is a standard snapshot, an instant snapshot, or an archive snapshot, respectively.
       2. Under **Source snapshot** , select the source snapshot or instant snapshot from the list. Only snapshots that are in the location you selected are listed.
     * To create the disk from a specific disk that's within a machine image (Preview): 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

       1. Select **Machine Image**.
       2. In the **Source machine image** drop-down menu, select the machine image you want to use.
       3. In the **Source disk** drop-down menu, select the device name of the specific disk within the chosen machine image that you want to use as the source for the new disk.
       4. If the selected machine image is protected by a Customer-supplied encryption key (CSEK) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine)), an **Encryption** section appears. Enter the required decryption key in the provided field.
       5. Configure other disk properties such as **Name** , **Type** , **Size** , and **Deletion** rule as needed.
  7. Under **Disk settings** , choose a disk type from the following list. The values that you specify must be in the range of supported values.

     1. **Hyperdisk Balanced**. You can also change the default disk **Size** , **Provisioned IOPS** , and **Provisioned Throughput** settings.
     2. **Hyperdisk Extreme**. You can also change the default disk **Size** and **Provisioned IOPS** settings.
     3. **Hyperdisk ML**. You can also change the default disk **Size** and **Provisioned Throughput** settings.
     4. **Hyperdisk Throughput**. You can also change the default disk **Size** and **Provisioned Throughput** settings.
  8. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section. 

     * Select the disk attachment mode in the **Mode** field.
     * Choose to keep or delete the disk when the instance is deleted by selecting the option in the **Deletion rule** field.
     * To make identifying the disk easier from within the guest OS, specify a custom device name. Under the heading **Device name** , select the option **Use a custom device name**. In the **Device name** field, enter a string to use as a symlink for the disk. 
  9. Click **Done**.

  10. To apply your changes to the instance, click **Save**.




###  gcloud 

  1. Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create the Hyperdisk volume.
         
         gcloud compute disks create DISK_NAME \
             --zone=ZONE \
             --size=DISK_SIZE \
             --type=DISK_TYPE \
             --provisioned-iops=IOPS_LIMIT \
             --provisioned-throughput=THROUGHPUT_LIMIT \
             --access-mode=DISK_ACCESS_MODE
         

Replace the following:

     * `DISK_NAME`: the name of the new disk.
     * `ZONE`: the name of zone where the new disk is being created. 
     * `DISK_SIZE`: Optional: The size of the new disk. The value must be a whole number followed by a size unit of GB for gibibyte, or TB for tebibyte. If no size unit is specified, 100 GB is used as the default value. The accepted values for the disk size are: 
       * Hyperdisk Balanced: From 4 GiB to 64 TiB, inclusive, in 1 GiB increments.
       * Hyperdisk Extreme: From 64 GiB to 64 TiB, inclusive, in 1 GiB increments.
       * Hyperdisk ML: From 4 GiB to 64 TiB, inclusive, in 1 GiB increments.
       * Hyperdisk Throughput: From 2 TiB to 32 TiB, inclusive, in 1 GiB increments.
     * `DISK_TYPE`: the type of disk. Use one of the following values: `hyperdisk-balanced`, `hyperdisk-extreme`, `hyperdisk-ml`, or `hyperdisk-throughput`
     * `IOPS_LIMIT`: Optional: For Hyperdisk Balanced or Hyperdisk Extreme disks, this is the number of I/O operations per second (IOPS) that the disk can handle.
     * `THROUGHPUT_LIMIT`: Optional: For Hyperdisk Balanced, Hyperdisk ML, or Hyperdisk Throughput volumes, this is an integer that represents the maximum throughput, measured in MiB per second, that the disk can provide.
     * `DISK_ACCESS_MODE`: Optional: How compute instances can access the data on the disk. Supported values are:

       * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default.
       * `READ_WRITE_MANY`, (Hyperdisk Balanced and Hyperdisk Balanced High Availability only) for concurrent read-write access from multiple instances.
       * `READ_ONLY_MANY`, (Hyperdisk ML only) for concurrent read-only access from multiple instances.

To set the access mode for Hyperdisk Balanced High Availability disks, see [Create a regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk).

  2. Optional: Use the [`gcloud compute disks describe DISK_NAME` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe) to see a description of your disk.

  3. After you create the disk, you can [attach the disk to an instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks).




###  REST 

  1. Construct a `POST` request to create a zonal Hyperdisk by using the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). Include the `name`, `sizeGb`, `type`, `provisionedIops`, and `provisionedThroughput` properties. To create this disk as an empty and unformatted non-boot disk, don't specify a source image or a source snapshot.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
         {
            "name": "DISK_NAME",
            "sizeGb": "DISK_SIZE",
            "type": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE",
            "provisionedIops": "IOPS_LIMIT",
            "provisionedThroughput": "THROUGHPUT_LIMIT",
            "accessMode": "DISK_ACCESS_MODE"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where your instance and new disk are located
     * `DISK_NAME`: the name of the new disk
     * `DISK_SIZE`: Optional: The size of the new disk. The value must be a whole number followed by a size unit of GB for gibibytes or TB for tebibytes.
     * `DISK_TYPE`: the type of disk. To create a Hyperdisk volume, use one of the following values: `hyperdisk-balanced`, `hyperdisk-extreme`, `hyperdisk-ml`, or `hyperdisk-throughput`.
     * `IOPS_LIMIT`: Optional: For Hyperdisk Balanced and Hyperdisk Extreme, this is the number of I/O operations per second that the disk can handle.
     * `THROUGHPUT_LIMIT`: Optional: For Hyperdisk Balanced, Hyperdisk ML, or Hyperdisk Throughput volumes, this is an integer that represents the maximum throughput, measured in MiB per second, that the disk can provide.
     * `DISK_ACCESS_MODE`: Optional: How compute instances can access the data on the disk. Supported values are:

       * `READ_WRITE_SINGLE`, for read-write access from one instance. This is the default.
       * `READ_WRITE_MANY`, (Hyperdisk Balanced and Hyperdisk Balanced High Availability only) for concurrent read-write access from multiple instances.
       * `READ_ONLY_MANY`, (Hyperdisk ML only) for concurrent read-only access from multiple instances.

To set the access mode for Hyperdisk Balanced High Availability disks, see [Create a regional disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_create_disk).

  2. Optional: Use the [`compute.disks.get` method](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe) to see a description of your disk.

  3. After you create the disk, you can [attach the disk](https://docs.cloud.google.com/compute/docs/disks/attach-disks) to any running or stopped instance.




###  Go 
    
    
    // createHyperdisk creates a new Hyperdisk in the specified project and zone.
    func createHyperdisk(w io.Writer, projectId, zone, diskName string) error {
    	//   projectID := "your_project_id"
    	//   zone := "europe-central2-b"
    	//   diskName := "your_disk_name"
    
    	ctx := context.Background()
    	client, err := compute.NewDisksRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %v", err)
    	}
    	defer client.Close()
    
    	// use format "zones/{zone}/diskTypes/(hyperdisk-balanced|hyperdisk-throughput)".
    	diskType := fmt.Sprintf("zones/%s/diskTypes/hyperdisk-balanced", zone)
    
    	// Create the disk
    	disk := &computepb.Disk{
    		Name:   proto.String(diskName),
    		Type:   proto.String(diskType),
    		SizeGb: proto.Int64(10),
    		Zone:   proto.String(zone),
    	}
    
    	req := &computepb.InsertDiskRequest{
    		Project:      projectId,
    		Zone:         zone,
    		DiskResource: disk,
    	}
    
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Insert disk request failed: %v", err)
    	}
    
    	// Wait for the insert disk operation to complete
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Hyperdisk created: %v\n", diskName)
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateHyperdisk {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone in which you want to create the disk.
        String zone = "europe-central2-b";
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/{disktype}".
        // disktype is one of hyperdisk-balanced, hyperdisk-extreme, hyperdisk-throughput
        // hyperdisk-ml, hyperdisk-balanced-high-availability
        // For example: "zones/us-west3-b/diskTypes/hyperdisk-balanced"
        String diskType = String.format("zones/%s/diskTypes/hyperdisk-balanced", zone);
        // Size of the new disk in gigabytes.
        long diskSizeGb = 10;
        // Optional: For Hyperdisk Balanced or Hyperdisk Extreme disks,
        // this is the number of I/O operations per second (IOPS) that the disk can handle
        long provisionedIops = 3000;
        // Optional: For Hyperdisk Balanced or Hyperdisk Throughput volumes,
        // this is an integer that represents the throughput,
        // measured in MiB per second, that the disk can handle.
        long provisionedThroughput = 140;
    
        createHyperdisk(projectId, zone, diskName, diskType, diskSizeGb,
                provisionedIops, provisionedThroughput);
      }
    
      // Creates a hyperdisk in a project
      public static [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) createHyperdisk(String projectId, String zone, String diskName,
                                         String diskType, long diskSizeGb, long provisionedIops,
                                         long provisionedThroughput)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) client = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          // Create a disk.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
                  .setZone(zone)
                  .setName(diskName)
                  .setType(diskType)
                  .setSizeGb(diskSizeGb)
                  .setProvisionedIops(provisionedIops)
                  .setProvisionedThroughput(provisionedThroughput)
                  .build();
    
          [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html) request = [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html).newBuilder()
                  .setProject(projectId)
                  .setZone(zone)
                  .setDiskResource(disk)
                  .build();
    
          // Wait for the insert disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = client.insertAsync(request).get(1, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
    
          // Wait for server update
          TimeUnit.SECONDS.sleep(10);
    
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) hyperdisk = client.get(projectId, zone, diskName);
    
          System.out.printf("Hyperdisk '%s' has been created successfully", hyperdisk.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getName__)());
    
          return hyperdisk;
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a diskClient
    const disksClient = new computeLib.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await disksClient.getProjectId();
    
    // The zone where your VM and new disk are located.
    // zone = 'europe-central2-b';
    
    // The name of the new disk
    // diskName = 'disk-name';
    
    // The type of disk. This value uses the following format:
    // "zones/{zone}/diskTypes/(hyperdisk-balanced|hyperdisk-extreme|hyperdisk-ml|hyperdisk-throughput)".
    // For example: "zones/us-west3-b/diskTypes/hyperdisk-balanced"
    const diskType = `zones/${zone}/diskTypes/hyperdisk-balanced`;
    // Size of the new disk in gigabytes.
    const diskSizeGb = 10;
    // Optional: For Hyperdisk Balanced or Hyperdisk Extreme disks,
    // this is the number of I/O operations per second (IOPS) that the disk can handle.
    const provisionedIops = 3000;
    // Optional: For Hyperdisk Balanced or Hyperdisk Throughput volumes,
    // this is an integer that represents the throughput,
    // measured in MiB per second, that the disk can handle.
    const provisionedThroughput = 140;
    
    async function callCreateComputeHyperdisk() {
      // Create a disk
      const disk = new compute.Disk({
        sizeGb: diskSizeGb,
        name: diskName,
        zone,
        type: diskType,
        provisionedIops,
        provisionedThroughput,
      });
    
      const [response] = await disksClient.insert({
        project: projectId,
        zone,
        diskResource: disk,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Disk: ${diskName} created.`);
    }
    
    await callCreateComputeHyperdisk();

After you create the disk, you can [attach the disk](https://docs.cloud.google.com/compute/docs/disks/attach-disks) to any running or stopped instance.

## Format and mount the disk

After you create and [attach the new disk to an instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks), you must format and mount the disk, so that the operating system can use the available storage space.

  * Linux: See [Formatting and mounting a non-boot disk on a Linux compute instance](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux)
  * Windows: See [Formatting and mounting a non-boot disk on a Windows compute instance](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows)



## What's next

  * Learn how to [customize the IOPS and throughput on your Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks).
  * Learn how to regularly [back up your disks using snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_hyperdisk_snapshots) to prevent unintended data loss.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
