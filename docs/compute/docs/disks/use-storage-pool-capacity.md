---
url: https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity/
title: Add disks from a Hyperdisk pool to VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:31.066427+00:00
---

# Add disks from a Hyperdisk pool to VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add disks from a Hyperdisk pool to VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create disks in a pool. 

You can create a disk in a pool and then attach the disk to a virtual machine (VM) instance, or you can create disks in the pool when you create a VM instance.

You can't move an existing disk into or out of a pool. You must create a new disk from the existing disk. To do so, see [Change the type, placement, or location of a disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd). 

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

To get the permissions that you need to create a Hyperdisk Balanced or Hyperdisk Throughput disk in a pool, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM instance that can run as a service account: Service Account User (v1) (`roles/iam.serviceAccountUser` role) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a Hyperdisk Balanced or Hyperdisk Throughput disk in a pool. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Hyperdisk Balanced or Hyperdisk Throughput disk in a pool:

  * To create disks in a pool and attach the disks to a VM instance: 
    * `compute.disks.create` on the project
    * `compute.instances.attachDisk` on the VM
    * `compute.disks.use` on the volume that you want to attach to the VM
    * `compute.storagePools.use` on the pool you're creating disks in
  * To format and mount the attached volume: `compute.instances.setMetadata` on the VM 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For the permissions needed to create an instance, see [Required permissions](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#required-roles).

## Limitations

Limitations for adding disks to a pool:

  * You can create only Hyperdisk Balanced disks in a Hyperdisk Balanced pool, and you can create only Hyperdisk Throughput disks in a Hyperdisk Throughput pool.
  * Only new disks in the same project and zone can be created in a pool.
  * Pools don't support [regional disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).
  * You can't move disks in or out of a pool; you have to recreate the disk from a standard snapshot. For more information, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).
  * To create boot disks in a pool, you must use a Hyperdisk Balanced Storage Pool or Hyperdisk Balanced Exapool.



Limitations specific to Storage Pools:

  * You can create up to 10,000 disks in a Storage Pool.



Limitations specific to Exapools:

  * You can create up to 500,000 disks in an Exapool.



## Provisioning options

Depending on the provisioning type for the pool, you can choose how to provision both the capacity and the performance of each the disk that you create in the pool.

### Provisioning disk capacity

If you're using an Exapool or an advanced capacity Storage Pool, you can create disks in the pool with a cumulative size that exceeds the provisioned capacity of the pool. The used capacity of the pool is defined by the total data in use and not by the amount of disk space that you've provisioned. You can provision disks with an aggregate capacity of up to five or 50 times the provisioned capacity of an Advanced capacity pool or Hyperdisk Exapool, respectively.

If you are creating disks in a Standard capacity pool, then you create disks in the pool until the total size of all disks in the pool reaches the pool's provisioned capacity. The disks in a pool with Standard capacity behave similarly to non-pool disks, where capacity is consumed when you create the disks.

### Provisioning performance

**Note:** If you're using a Hyperdisk Exapool, the amount of performance you can provision for disks depends on the pool's provisioned write performance.

If you're using an Exapool or an advanced capacity Storage Pool, you can create disks in the pool with a cumulative amount of IOPS and throughput that exceeds the provisioned performance of the pool. The used performance of the pool is defined by the total performance used by the disks and not by the amount of performance provisioned to each disk.

  * For Storage Pools, you can provision disks with an aggregate performance of up to 500%% of the provisioned performance of an Advanced performance pool.

  * For Exapools, you can provision disks with an aggregate performance of up to 50x the pool's provisioned write performance.




If you're creating disks in a Standard performance pool, the IOPS or throughput that you provision for a disk must be less than the available IOPS or throughput in the Hyperdisk Storage Pool. The available IOPS or throughput is the provisioned amount for the pool minus the used amount for all the disks created in the pool.

If any of the conditions in the previous paragraph aren't true, then the request to create a disk in the pool fails and the disk isn't created.

**Example**

Assume that you have a Hyperdisk Balanced Storage Pool with 100,000 provisioned IOPS.

With Standard performance provisioning:

  * You can provision up to 100,000 of aggregate IOPS when creating Hyperdisk Balanced disks in the Storage Pool.
  * You are charged for the 100,000 IOPS of Hyperdisk Balanced Storage Pool provisioned performance.
  * Like disks created outside of a storage pool, Hyperdisk Balanced disks in Standard performance Storage Pools are automatically provisioned with up to 3,000 baseline IOPS and 140 MiB/s of baseline throughput. This baseline performance isn't counted against the provisioned performance for the Storage Pool. Only when you add disks to the Storage Pool with provisioned performance that's above the baseline does it count against the provisioned performance for the Storage Pool, for example:

    * A disk provisioned with 3,000 IOPS uses 0 pool IOPS and the pool still has 100,000 provisioned IOPS available for other disks.
    * A disk provisioned with 13,000 IOPS uses 10,000 pool IOPS and the pool has 90,000 provisioned IOPS remaining that you can allocate to other disks in the Storage Pool. 



With Advanced performance provisioning:

  * You can provision up to 500,000 IOPS of aggregate Hyperdisk performance when creating disks in the Storage Pool.
  * You are charged for 100,000 IOPS provisioned by the Storage Pool.
  * If you create a single disk (`Disk1`) in the Storage Pool that has 5,000 IOPS, you don't consume any IOPS from the Storage Pool provisioned IOPS. However, the amount of IOPS that you can provision to new disks created in the Storage Pool is now 495,000.
  * If `Disk1` starts to read and write data, and if it uses its maximum of 5,000 IOPS in a given minute, then 5,000 IOPS is consumed from the Storage Pool provisioned IOPS. Any other disks that you created in the same storage pool can use an aggregated maximum of 95,000 IOPS in that same minute without running into contention.



## Create disks in the pool

You can use the Google Cloud console, Google Cloud CLI, or REST to create a disk in a pool.

###  Console 

Using the Google Cloud console, you can create a new disk in a pool either through the **Storage pools** page or the **Disks** page.

On the **Storage pools** page:

  1. In the Google Cloud console, go to the **Storage pools** page.

[Go to the **Storage pools** page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

  3. Click the name of the pool that you would like to create a disk in.

  4. On the **Manage storage pool** page, click **+Create New Disk**.

  5. In the **Add new disk** panel, enter a **Name** for the disk.

  6. Specify or change any values for which you don't want to use the default value.

  7. When finished specifying the disk properties, click **Save**.

  8. On the **Manage storage pool** page, you should see the new disk listed in the **Storage pool disks** section.




On the **Create Disk** page:

  1. In the Google Cloud console, go to **Disks** > **Create a disk** page.

[Go to the Create a disk page](https://console.cloud.google.com/compute/disksAdd)

  2. Enter a **Name** for the disk.

  3. Select the zone that contains the pool you want to create the disk in.

  4. For the **Disk type** , choose the disk type that matches the pool, either Hyperdisk Throughput or Hyperdisk Balanced.

  5. Modify the values in the **Size** , **Provisioned IOPS** , and **Provisioned Throughput** fields, as necessary.

  6. In the **Storage pool** section, select **Enable storage pool** , then choose the name of the pool to create the disk in. Only pool that exist in the selected zone appear in the list.

  7. When finished specifying the disk information, click **Create**.




###  gcloud 

To create one or more disks in a pool, use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).
    
    
    gcloud compute disks create DISK_NAME \
        --zone=ZONE \
        --storage-pool=STORAGE_POOL_NAME \
        --size=SIZE \
        --type=DISK_TYPE \
        --provisioned-iops=PROVISIONED_IOPS \
        --provisioned-throughput=PROVISIONED_THROUGHPUT
    

Replace the following:

  * DISK_NAME: a unique name for the disk. You can provide a list of disk names specified by spaces to create multiple disks with the same attributes.
  * ZONE: the zone where the pool was created. Specify this value in region-zone format, for example `us-central1-a`.
  * STORAGE_POOL_NAME: the name of the pool to create the disk in
  * SIZE: Optional: the provisioned capacity of the new disk. The value must be a whole number followed by a size unit of GB for gibibyte, or TB for tebibyte. If no size is specified, 100 GB is used as the default value.
  * DISK_TYPE: the type of disk to create. This must match the type of the Hyperdisk Storage Pool, either `hyperdisk-balanced` or `hyperdisk-throughput`.
  * PROVISIONED_IOPS: Optional: the IOPS to provision for the disk. You can use this flag only with Hyperdisk Balanced disks.
  * PROVISIONED_THROUGHPUT: Optional: the throughput in MiB/s to provision for the disk.



###  REST 

To create one or more disks in a pool, construct a `POST` using the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). Include the `name`, `sizeGb`, `type`, `storagePool`, `provisionedIops`, and `provisionedThroughput` properties. To create this disk as an empty and unformatted non-boot disk, don't specify a source image or a source snapshot.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    
    {
        "name": "DISK_NAME",
        "description": "DESCRIPTION",
        "type": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE",
        "sizeGb": "DISK_SIZE",
        "storagePool": "STORAGE_POOL_NAME",
        "provisionedIops": "IOPS_LIMIT",
        "provisionedThroughput": "THROUGHPUT_LIMIT",
    }
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone in which the pool is located, for example, `us-central1-a`. This is the zone that the disk will be created in.
  * DISK_NAME: a unique name for the disk.
  * DESCRIPTION: Optional: a text string that describes the disk.
  * DISK_TYPE: the type of disk, which must match the pool type. Use either `hyperdisk-throughput` or `hyperdisk-balanced`.
  * DISK_SIZE: Optional: The size of the new disk. The value must be a whole number followed by a size unit of GB for gibibytes or TB for tebibytes. If no size is specified, 100 GB is used as the default value.
  * STORAGE_POOL_NAME: the name of the pool to create the disk in.
  * IOPS_LIMIT: Optional: the IOPS to provision for the disk. You can use this flag only with Hyperdisk Balanced disks.
  * THROUGHPUT_LIMIT: Optional: The throughput in MiB/s to provision for the disk.



###  Go 
    
    
    // createDiskInStoragePool creates a new Hyperdisk in the specified storage pool.
    func createDiskInStoragePool(w io.Writer, projectId, zone, diskName, storagePoolName, diskType string) error {
    	// Example usage:
    	//   projectID := "your_project_id"
    	//   zone := "europe-central2-b"
    	//   diskName := "your_disk_name"
    	//   storagePoolName := "https://www.googleapis.com/compute/v1/projects/your_project_id/zones/europe-central2-b/storagePools/your_storage_pool"
    	//   diskType := "zones/europe-central2-b/diskTypes/hyperdisk-balanced"
    
    	ctx := context.Background()
    	client, err := compute.NewDisksRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %v", err)
    	}
    	defer client.Close()
    
    	// Create the disk resource
    	disk := &computepb.Disk{
    		Name:                  proto.String(diskName),
    		Type:                  proto.String(diskType),
    		SizeGb:                proto.Int64(50),
    		Zone:                  proto.String(zone),
    		StoragePool:           proto.String(storagePoolName),
    		ProvisionedIops:       proto.Int64(10000),
    		ProvisionedThroughput: proto.Int64(1024),
    	}
    
    	// Create the insert disk request
    	req := &computepb.InsertDiskRequest{
    		Project:      projectId,
    		Zone:         zone,
    		DiskResource: disk,
    	}
    
    	// Send the insert disk request
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Insert disk request failed: %v", err)
    	}
    
    	// Wait for the insert disk operation to complete
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created in storage pool: %v\n", disk.Name)
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
    
    public class CreateDiskInStoragePool {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone in which you want to create the disk.
        String zone = "europe-central2-b";
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
        // Link to the storagePool you want to use. Use format :
        // https://www.googleapis.com/compute/v1/projects/%s/zones/%s/storagePools/%s"
        String storagePoolName = "YOUR_STORAGE_POOL_LINK";
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/(hyperdisk-balanced|hyperdisk-throughput)".
        // For example: "zones/us-west3-b/diskTypes/hyperdisk-balanced"
        String diskType = String.format("zones/%s/diskTypes/hyperdisk-balanced", zone);
        // Size of the new disk in gigabytes.
        long diskSizeGb = 10;
        // Optional: the IOPS to provision for the disk.
        // You can use this flag only with Hyperdisk Balanced disks.
        long provisionedIops = 3000;
        // Optional: the throughput in mebibyte (MB) per second to provision for the disk.
        long provisionedThroughput = 140;
    
        createDiskInStoragePool(projectId, zone, diskName, storagePoolName, diskType,
                diskSizeGb, provisionedIops, provisionedThroughput);
      }
    
      // Creates a hyperdisk in the storage pool
      public static [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) createDiskInStoragePool(String projectId, String zone, String diskName,
                                                 String storagePoolName, String diskType,
                                                 long diskSizeGb, long iops, long throughput)
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
                  .setStoragePool(storagePoolName)
                  .setProvisionedIops(iops)
                  .setProvisionedThroughput(throughput)
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
    // zone = 'us-central1-a';
    
    // The name of the new disk
    // diskName = 'disk-from-pool-name';
    
    // The name of the storage pool
    // storagePoolName = 'storage-pool-name';
    
    // Link to the storagePool you want to use. Use format:
    // https://www.googleapis.com/compute/v1/projects/{projectId}/zones/{zone}/storagePools/{storagePoolName}
    const storagePool = `https://www.googleapis.com/compute/v1/projects/${projectId}/zones/${zone}/storagePools/${storagePoolName}`;
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
    
    async function callCreateComputeHyperdiskFromPool() {
      // Create a disk
      const disk = new compute.Disk({
        sizeGb: diskSizeGb,
        name: diskName,
        type: diskType,
        zone,
        storagePool,
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
    
    await callCreateComputeHyperdiskFromPool();

Aftering creating the disk, you can [attach the disk to a VM](https://docs.cloud.google.com/compute/docs/disks/attach-disks).

## Create a VM that uses disks in the pool

When you create a VM, you configure a boot disk, and you can optionally create additional data (non-boot) disks, which are automatically attached to the VM. The following sections explain how to create each type of disk in a pool as part of the VM creation process.

### Create the boot disk for a VM in a pool

To create a VM that uses a boot disk in a pool, you must first create a Hyperdisk Balanced Storage Pool or Hyperdisk Balanced Exapool. You can then create an instance using a machine type that supports Hyperdisk Balanced disks. The machine type, disk type, and pool must all be available in the zone that you choose.

###  Console 

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create Instance**.

  3. Enter a name for the instance.

  4. Set the zone to the same zone where the pool is located.

  5. Choose a machine type that supports Hyperdisk Balanced, for example H3.

  6. In the **Boot disk** section, click **Change**.

  7. In the **Boot disk** panel, set the **Boot disk type** to Hyperdisk Balanced.

  8. Configure the properties for the disk.

  9. Expand **Show advanced configuration**.

  10. Under the heading **Storage pool** , select **Enable storage pool**.

  11. Choose the pool to create the disk in from the list.

  12. When finished with the disk configuration, click **Select**.

  13. Finish configuring the VM properties.

  14. Click **Create**.

The console creates the VM in the specified zone, and creates the boot disk in the selected pool.




###  gcloud 

You can create the boot disk for a new VM in the pool using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and including the `storage-pool` property for the boot disk.
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --create-disk=boot=yes,type=hyperdisk-balanced,size=DISK_SIZE,provisioned-throughput=THROUGHPUT, \
        provisioned-iops=IOPS,image=projects/IMAGE_PROJECT/global/images/IMAGE, \
        storage-pool=STORAGE_POOL_NAME
    

Replace the following:

  * VM_NAME: the name of the VM.
  * ZONE: the region and zone to create the VM in, using the format `us-central1-a`.
  * MACHINE_TYPE: the machine type of the VM, for example, `m3-ultramem-32`.
  * DISK_SIZE: the size, in GiB, of the boot disk
  * THROUGHPUT: the throughput to provision for the disk
  * IOPS: the IOPS to provision for the disk
  * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image
  * IMAGE: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v20240213`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates a VM using the latest version of the OS image in the `debian-12` image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * STORAGE_POOL_NAME: the name of the storage pool to create the new disk in.



###  REST 

You can create the boot disk for a new VM in the pool by constructing a `POST` request for the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and including the `storagePool` property for the boot disk.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "name": "VM_NAME",
       "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
       "disks": [
          {
             "deviceName": "BOOT_DISK_DEVICE_NAME",
             "initializeParams": {
                "diskSizeGb": "DISK_SIZE",
                "diskType": "DISK_TYPE",
                "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
                "boot": true,
                "provisionedIops": "IOPS_LIMIT",
                "provisionedThroughput": "THROUGHPUT_LIMIT",
                "storagePool": "POOL_URL"
             }
          }
       ]
    }
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone in which the pool is located, for example, `us-central1-a`. This is the zone that VM and boot disk are created in.
  * VM_NAME: the name of the VM.
  * MACHINE_TYPE: the machine type of the VM, for example, `m3-ultramem-32`.
  * BOOT_DISK_DEVICE_NAME: the device name for the boot disk
  * DISK_SIZE: the size, in GiB, of the boot disk
  * DISK_TYPE: the disk type, specified as a URI
  * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image
  * IMAGE: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v20240213`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates a VM using the latest version of the OS image in the `debian-12` image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * IOPS_LIMIT: the IOPS to provision for the disk
  * THROUGHPUT_LIMIT: the throughput to provision for the disk
  * POOL_URL: the storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 
    * `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`
    * `projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`
    * `zones/ZONE/storagePools/STORAGE_POOL_NAME`



### Create additional disks in a pool during VM creation

When creating disks in a pool during VM creation, the machine type, disk type, and pool must be available in the zone that you choose.

###  Console 

Use the following steps to use the console to create a new VM with additional, non-boot disks:

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create Instance**.

  3. Enter a name for the VM.

  4. Set the zone to the same zone where the pool is located.

  5. Choose a machine type that supports disk type used by the pool.

  6. Expand the **Advanced options** section.

  7. Expand **Disks**.

  8. Click add **Add new disk**.

  9. In the **Add new disk** panel, enter the information for the disk. Set the **Disk type** to match the pool type.

  10. In the **Storage Pool** section, select **Enable storage pool**.

  11. In the **Select a storage pool** field, select the pool to create the disk in.

  12. When finished with the disk configuration, click **Save**.

  13. Finish configuring the VM properties.

  14. Click **Create**.

The console creates the VM in the specified zone, and creates the non-boot disk in the selected pool.




###  gcloud 

You can create new disks in a pool during VM creation by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and including the `storage-pool` property for the disk.
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --create-disk=auto-delete=yes,boot=yes,device-name=BOOT_DISK_DEVICE_NAME,image=IMAGE_NAME, \
        size=BOOT_DISK_SIZE,type=BOOT_DISK_TYPE
        --create-disk=auto-delete=yes,boot=no,device-name=DATA_DISK_DEVICE_NAME,size=DATA_DISK_SIZE, \
        type=DATA_DISK_TYPE,provisioned-iops=IOPS,provisioned-throughput=THROUGHPUT, \
        storage_pool=STORAGE_POOL_NAME
    

Replace the following:

  * VM_NAME: the name of the VM
  * ZONE: the zone to create the VM in; for example, `us-central1-a`
  * MACHINE_TYPE: the machine type of the VM
  * BOOT_DISK_DEVICE_NAME: the device name for the boot disk
  * IMAGE_NAME: the name of the operating system image to install on the boot disk, for example, `debian-12-bookworm-v20240213`
  * BOOT_DISK_SIZE: the size, in GiB, of the boot disk
  * BOOT_DISK_TYPE: the disk type
  * DATA_DISK_DEVICE_NAME: the disk device name for the data disk
  * DATA_DISK_SIZE: the size of the data disk, in GiB
  * DATA_DISK_TYPE: the data disk type, either `hyperdisk-balanced` or `hyperdisk-throughput`
  * IOPS: the IOPS to provision for the disk
  * THROUGHPUT: the throughput to provision for the disk
  * STORAGE_POOL_NAME: the unique name for the pool in which you want to create the disk



###  REST 

You can create new disks in a pool during VM creation by constructing a `POST` request for the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and including the `storagePool` property for the additional disks.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "name": "VM_NAME",
       "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
       "disks": [
          {
            "initializeParams":{
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE"
            },
            "boot":true
          },
          {
            "deviceName": "DEVICE_NAME",
            "boot":false,
            "initializeParams": {
               "diskSizeGb": "DISK_SIZE",
               "diskType": "DISK_TYPE",
               "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
               "provisionedIops": "IOPS_LIMIT",
               "provisionedThroughput": "THROUGHPUT_LIMIT",
               "storagePool": "POOL_URL"
            }
          }
       ]
    }
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone in which the pool is located, for example, `us-central1-a`. This is the zone that VM and boot disk are created in.
  * VM_NAME: the name of the VM.
  * MACHINE_TYPE: the machine type of the VM, for example, `m3-ultramem-32`.
  * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image
  * IMAGE: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v20240213`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates a VM using the latest version of the OS image in the `debian-12` image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * DEVICE_NAME: the device name for the data disk
  * DISK_SIZE: the size, in GiB, of the data disk
  * DISK_TYPE: the disk type, specified as a URI
  * IOPS_LIMIT: the IOPS to provision for the disk
  * THROUGHPUT_LIMIT: the throughput to provision for the disk
  * POOL_URL: the storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 
    * `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`
    * `projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`
    * `zones/ZONE/storagePools/STORAGE_POOL_NAME`



## Use pool in an instance template

The instance templates used to create managed instance groups (MIGs) can contain the pool information. The disks created using the instance template are placed in the specified pool.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create Instance Template**.

  3. Enter a name for the instance template.

  4. Choose **Regional** for the location, and in the **Region** field, choose the region where the pool is located.

  5. Choose a machine type that supports Hyperdisk Balanced, for example C3.

  6. In the **Boot disk** section, click **Change**.

  7. In the **Boot disk** panel, set the **Boot disk type** to Hyperdisk Balanced.

  8. Configure the properties for the disk.

  9. Expand **Show advanced configuration**.

  10. Under the heading **Storage pool** , select **Enable storage pool**.

  11. Choose the pool to create the disk in from the list.

  12. When finished with the disk configuration, click **Select**.

  13. Finish configuring the VM properties.

  14. Click **Create**.

The template creates the VM in the specified zone, and creates the boot disk in the selected pool.




###  gcloud 

You can specify in an instance template that the book disk be created in a pool by using the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) and including the `storage-pool` property for the boot disk.
    
    
    gcloud compute instance-templates create TEMPLATE_NAME \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE \
        --create-disk=boot=yes,type=hyperdisk-balanced,size=DISK_SIZE,provisioned-throughput=THROUGHPUT, \
        provisioned-iops=IOPS,image=projects/IMAGE_PROJECT/global/images/IMAGE, \
        storage-pool=STORAGE_POOL_NAME
    

Replace the following:

  * TEMPLATE_NAME: the name of the instance template.
  * REGION: the region where you want to create the regional instance template. The region must contain the zone where the pool is located.
  * MACHINE_TYPE: the machine type to use when creating the VM, for example, `h3-standard-88`.
  * DISK_SIZE: the size, in GiB, of the disk
  * THROUGHPUT: the throughput to provision for the disk
  * IOPS: the IOPS to provision for the disk
  * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image
  * IMAGE: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v20240213`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates a VM using the latest version of the OS image in the `debian-12` image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * STORAGE_POOL_NAME: the name of the storage pool to create the new disk in.



###  REST 

You can create the boot disk for a new VM in the pool by constructing a `POST` request for the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and including the `storagePool` property for the boot disk.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    {
       "name": "VM_NAME",
       "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
       "disks": [
          {
             "deviceName": "BOOT_DISK_DEVICE_NAME",
             "initializeParams": {
                "diskSizeGb": "DISK_SIZE",
                "diskType": "DISK_TYPE",
                "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
                "boot": true,
                "provisionedIops": "IOPS_LIMIT",
                "provisionedThroughput": "THROUGHPUT_LIMIT",
                "storagePool": "POOL_URL"
             }
          }
       ]
    }
    

Replace the following:

  * PROJECT_ID: the project ID
  * VM_NAME: the name of the VM.
  * ZONE: the zone in which the pool is located, for example, `us-central1-a`. This is the zone that VM and boot disk are created in.
  * MACHINE_TYPE: the machine type of the VM, for example, `m3-ultramem-32`.
  * BOOT_DISK_DEVICE_NAME: the device name for the boot disk
  * DISK_SIZE: the size, in GiB, of the boot disk
  * DISK_TYPE: the disk type, specified as a URI
  * IMAGE_PROJECT: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that contains the image
  * IMAGE: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v20240213`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates an instance using the latest version of the OS image in the `debian-12` image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * IOPS_LIMIT: the IOPS to provision for the disk
  * THROUGHPUT_LIMIT: the throughput to provision for the disk
  * POOL_URL: the storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 
    * `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`
    * `projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME`
    * `zones/ZONE/storagePools/STORAGE_POOL_NAME`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
