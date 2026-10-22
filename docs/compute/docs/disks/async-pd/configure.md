---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/configure/
title: Configure Asynchronous Replication \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:33.086425+00:00
---

# Configure Asynchronous Replication  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure Asynchronous Replication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about). Asynchronous Replication is useful for low-RPO, low-RTO disaster recovery.

To enable asynchronous disk replication, complete the following steps:

  1. Set up a disk replication pair to configure Asynchronous Replication.
  2. [Manually start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication) to begin replicating data between the primary and secondary disk.



## Limitations

  * Secondary disks must be blank when created. They can't be created from images, snapshots, or other disks.
  * Asynchronous Replication isn't supported for Hyperdisk ML or Hyperdisk Throughput.



## Before you begin

  * [Choose a region pair ](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).
  * [ Optionally create a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group).
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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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




## Set up a disk replication pair

Before you can replicate data between disks, you need to configure replication by completing the following tasks:

  1. [Choose a region pair](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs) and your primary and secondary regions.
  2. Optional: If you need to coordinate replication across a group of disks, [create a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group) in the primary region. You must add primary disks to a consistency group before you start replication.
  3. Create or select the primary disks. You can optionally add these disks to the consistency group.
  4. Create new, blank secondary disks.



### Disk requirements

Disks must meet the following requirements to be used as primary or secondary disks for Asynchronous Replication:

  * **Disk type** : you must use one of the following [disk types](https://docs.cloud.google.com/compute/docs/disks): 
    * Balanced Persistent Disk
    * Performance (SSD) Persistent Disk
    * Hyperdisk Balanced
    * Hyperdisk Balanced High Availability
    * Hyperdisk Extreme
  * **Size** : less than or equal to 64 TiB.
  * **Encryption type** : Google-owned and Google-managed encryption keys or [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption).
  * **Multi-writer mode** : you can enable Asynchronous Replication for Hyperdisk Balanced and Hyperdisk Balanced High Availability disks that are in multi-writer mode. For all other disk types, the disk must be in read-write mode.
  * **Location** : located in a [supported region](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs) (or a zone within a supported region).



### Create or select a primary disk

The primary disk is the boot or data disk that is attached to the VM where the workload runs. You can use any pre-existing disk that meets the disk requirements as a primary disk, or you can create a new disk. If you want to use an existing disk as a primary disk, you don't need to perform any additional configuration on the disk. Proceed to create a secondary disk to complete Asynchronous Replication configuration.

#### Create a primary disk

Create a primary disk using the methods described in one of the following documents.

  * [Create a primary boot disk while creating a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage). Optionally add the disk to a consistency group by creating the VM using the gcloud CLI or REST and specifying one of the following:

    * If you create the VM using the gcloud CLI, specify the [`--create-disk` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--create-disk):
          
          --create-disk=disk-resource-policy=projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME
          

    * If you create the VM using REST, specify the `resourcePolicies` property:
          
          "disks":
          {
          …
          "resourcePolicies": "projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME"
          }
          

  * [Create a primary data disk while creating a VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks). Optionally add the disk to a consistency group by creating the VM using the gcloud CLI or REST and specifying one of the following:

    * If you create the VM using the gcloud CLI, specify the [`--create-disk` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--create-disk):
          
          --create-disk=disk-resource-policy=projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME
          

    * If you create the VM using REST, specify the `resourcePolicies` property:
          
          "disks":
          {
          …
          "resourcePolicies": "projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME"
          }
          

  * [Create a primary data disk without creating a VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk). Optionally add the disk to a consistency group by creating the VM using the Google Cloud console, gcloud CLI, or REST and specifying one of the following:

    * If you create the disk using the Google Cloud console, select the consistency group from the **Consistency group** dropdown.

    * If you create the disk using the gcloud CLI, specify the [`--resource-policies` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create#--resource-policies):
          
          --resource-policies=projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME
          

    * If you create the disk using REST, specify the `resourcePolicies` property:
          
          "disks":
          {
          …
          "resourcePolicies": "projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME"
          }
          

Replace the following:

    * `PROJECT`: the project that contains the consistency group
    * `REGION`: the region that the consistency group is location in
    * `CONSISTENCY_GROUP_NAME`: the name of the consistency group to add the disk to



### Create a secondary disk

The secondary disk is a data disk in a separate region from the primary disk, that receives and writes replicated data from the primary disk. When configuring Asynchronous Replication, you must create a new, blank secondary disk that references the primary disk.

To create a secondary disk with the same properties as the primary disk, follow the steps in Create a secondary disk identical to the primary disk.

**Note:** Compute Engine copies some properties from the primary disk to the secondary disk only once, when the secondary disk is created. For more information on which properties are monitored and automatically updated, see [Secondary disk customization](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#change_secondary_disk).

To create a secondary disk that differs from the primary disk, see Create a custom secondary disk.

#### Create a secondary disk identical to the primary disk

This section describes how to create a secondary disk identical to the primary disk.

  * For Persistent Disk Asynchronous Replication, you can create a secondary disk with the Google Cloud console, the gcloud CLI, or REST.
  * For Hyperdisk Asynchronous Replication, you can use the Google Cloud console, the gcloud CLI, Terraform, or REST.




###  Console 

**Note:** When you create a secondary disk using the Google Cloud console, replication starts immediately. If you want to [add the secondary disk's corresponding primary disk to a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#add_a_disk_to_a_consistency_group), you must do so before you create the secondary disk.

Create a secondary disk and start replication by doing the following:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click the name of the primary disk. The **Manage disk** page opens.

  3. Click **Create secondary disk**.

  4. In the **Name** field, enter a name for the disk.

  5. In the **Location** section, do one of the following:

     * To create a regional disk:

       1. Select **Regional**.
       2. In the **Region** field, select a [region that corresponds with the primary disk's region](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).
       3. In the **Zone** field, select the primary zone.
       4. In the **Replica zone** field, select the replica zone.
     * To create a zonal disk:

       1. Select **Single zone**.
       2. In the **Region** field, select a [region that corresponds with the primary disk's region](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).
       3. In the **Zone** field, select a zone.
  6. Click **Create**. Compute Engine creates the disk and starts replication.




###  gcloud 

Create a secondary disk using the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create):
    
    
    gcloud compute disks create SECONDARY_DISK_NAME \
        --SECONDARY_LOCATION_FLAG=SECONDARY_LOCATION \
        --size=SIZE \
        --primary-disk=PRIMARY_DISK_NAME \
        --PRIMARY_DISK_LOCATION_FLAG=PRIMARY_LOCATION \
        --primary-disk-project=PRIMARY_DISK_PROJECT
    

To create a regional secondary disk, additionally specify the `--replica-zones` flag:
    
    
    --replica-zones=ZONE_1,ZONE_2
    

Replace the following:

  * `SECONDARY_DISK_NAME`: the name for the secondary disk.
  * `SECONDARY_LOCATION_FLAG`: the location flag for the secondary disk. To create a regional secondary disk, use `--region`. To create a zonal secondary disk, use `--zone`.
  * `SECONDARY_LOCATION`: the region or zone for the secondary disk. 
    * To create a regional disk, use [the region that corresponds with the primary disk's region](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).
    * To create a zonal disk, use a zone within the region that corresponds with the primary disk's region.
  * `SIZE`: the size, in GB, of the new disk. The size must be the same as the size of the primary disk. Acceptable sizes range, in 1 GB increments, from 10 GB to 2000 GB.
  * `PRIMARY_DISK_NAME`: the name of the primary disk that the secondary disk receives data from.
  * `PRIMARY_LOCATION_FLAG`: the location flag for the primary disk. 
    * For a regional primary disk, use `--primary-disk-region`.
    * For a zonal primary disk, use `--primary-disk-zone`.
  * `PRIMARY_LOCATION`: the primary disk's region or zone. 
    * For a regional disk, use the region.
    * For a zonal disks use the zone.
  * `PRIMARY_PROJECT`: the project that contains the primary disk.
  * `ZONE_1`: one of the zones that the regional disk is replicated to. Must be a zone within the specified region and must be different than `ZONE_2`.
  * `ZONE_2`: one of the zones that the regional disk is replicated to. Must be a zone within the specified region and must be different than `ZONE_1`.



###  Go 

Create a zonal or regional secondary disk using one of the following code samples:

##### Create a zonal secondary disk
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createSecondaryDisk creates a new secondary disk in a project in given zone.
    // Note: secondary disk should be located in a different region, but within the same continent.
    // More details: https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
    func createSecondaryDisk(
    	w io.Writer,
    	projectID, zone, diskName, primaryDiskName, primaryZone string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-west4-b"
    	// diskName := "your_disk_name"
    	// primaryDiskName := "your_disk_name2"
    	// primaryDiskZone := "europe-west2-b"
    	// diskSizeGb := 20
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	primaryFullDiskName := fmt.Sprintf("projects/%s/zones/%s/disks/%s", projectID, primaryZone, primaryDiskName)
    
    	req := &computepb.InsertDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		DiskResource: &computepb.Disk{
    			Name:   proto.String(diskName),
    			Zone:   proto.String(zone),
    			SizeGb: proto.Int64(diskSizeGb),
    			AsyncPrimaryDisk: &computepb.DiskAsyncReplication{
    				Disk: proto.String(primaryFullDiskName),
    			},
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

##### Create a regional secondary disk
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createRegionalSecondaryDisk creates a new secondary disk in a project in given region.
    // Note: secondary disk should be located in a different region, but within the same continent.
    // More details: https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
    func createRegionalSecondaryDisk(
    	w io.Writer,
    	projectID, region, diskName, primaryDiskName, primaryRegion string,
    	replicaZones []string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// region := "europe-west1"
    	// diskName := "your_disk_name"
    	// primaryDiskName := "your_disk_name2"
    	// primaryDiskRegion := "europe-west4"
    	// replicaZones := []string{"europe-west1-a", "europe-west1-b"}
    	// diskSizeGb := 200
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	primaryFullDiskName := fmt.Sprintf("projects/%s/regions/%s/disks/%s", projectID, primaryRegion, primaryDiskName)
    
    	// Exactly two replica zones must be specified
    	replicaZoneURLs := []string{
    		fmt.Sprintf("projects/%s/zones/%s", projectID, replicaZones[0]),
    		fmt.Sprintf("projects/%s/zones/%s", projectID, replicaZones[1]),
    	}
    
    	req := &computepb.InsertRegionDiskRequest{
    		Project: projectID,
    		Region:  region,
    		DiskResource: &computepb.Disk{
    			Name:   proto.String(diskName),
    			Region: proto.String(region),
    			// The size must be at least 200 GB
    			SizeGb: proto.Int64(diskSizeGb),
    			AsyncPrimaryDisk: &computepb.DiskAsyncReplication{
    				Disk: proto.String(primaryFullDiskName),
    			},
    			ReplicaZones: replicaZoneURLs,
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

###  Java 

Create a zonal or regional secondary disk using one of the following code samples:

##### Create a zonal secondary disk
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDiskSecondaryZonal {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The project that contains the primary disk.
        String primaryProjectId = "PRIMARY_PROJECT_ID";
        // The project that contains the secondary disk.
        String secondaryProjectId = "SECONDARY_PROJECT_ID";
        // Name of the primary disk you want to use.
        String primaryDiskName = "PRIMARY_DISK_NAME";
        // Name of the zone in which your primary disk is located.
        // Learn more about zones and regions:
        // https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
        String primaryDiskZone = "us-central1-a";
        // Name of the disk you want to create.
        String secondaryDiskName = "SECONDARY_DISK_NAME";
        // Name of the zone in which you want to create the secondary disk.
        String secondaryDiskZone = "us-east1-c";
        // Size of the new disk in gigabytes.
        long diskSizeGb = 30L;
        // The type of the disk you want to create. This value uses the following format:
        // "projects/{projectId}/zones/{zone}/diskTypes/
        // (pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        String diskType = String.format(
            "projects/%s/zones/%s/diskTypes/pd-balanced", secondaryProjectId, secondaryDiskZone);
    
        createDiskSecondaryZonal(primaryProjectId, secondaryProjectId, primaryDiskName,
            secondaryDiskName, primaryDiskZone, secondaryDiskZone, diskSizeGb,  diskType);
      }
    
      // Creates a secondary disk in a specified zone.
      public static [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createDiskSecondaryZonal(String primaryProjectId,
           String secondaryProjectId, String primaryDiskName, String secondaryDiskName,
           String primaryDiskZone, String secondaryDiskZone, long diskSizeGb, String diskType)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          String primaryDiskSource = String.format("projects/%s/zones/%s/disks/%s",
              primaryProjectId, primaryDiskZone, primaryDiskName);
    
          [DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html) asyncReplication = [DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html).newBuilder()
              .setDisk(primaryDiskSource)
              .build();
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setName(secondaryDiskName)
              .setZone(secondaryDiskZone)
              .setSizeGb(diskSizeGb)
              .setType(diskType)
              .setAsyncPrimaryDisk(asyncReplication)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.insertAsync(secondaryProjectId, secondaryDiskZone, disk)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error creating secondary disks! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

##### Create a regional secondary disk
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDiskSecondaryRegional {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The project that contains the primary disk.
        String primaryProjectId = "PRIMARY_PROJECT_ID";
        // The project that contains the secondary disk.
        String secondaryProjectId = "SECONDARY_PROJECT_ID";
        // Name of the primary disk you want to use.
        String primaryDiskName = "PRIMARY_DISK_NAME";
        // Name of the disk you want to create.
        String secondaryDiskName = "SECONDARY_DISK_NAME";
        // Name of the region in which your primary disk is located.
        // Learn more about zones and regions:
        // https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
        String primaryDiskRegion = "us-central1";
        // Name of the region in which you want to create the secondary disk.
        String secondaryDiskRegion = "us-east1";
        // Size of the new disk in gigabytes.
        // Learn more about disk requirements:
        // https://cloud.google.com/compute/docs/disks/async-pd/configure?authuser=0#disk_requirements
        long diskSizeGb = 30L;
        // The type of the disk you want to create. This value uses the following format:
        // "projects/{projectId}/zones/{zone}/diskTypes/
        // (pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        String diskType = String.format(
            "projects/%s/regions/%s/diskTypes/pd-balanced", secondaryProjectId, secondaryDiskRegion);
    
        createDiskSecondaryRegional(primaryProjectId, secondaryProjectId, primaryDiskName,
            secondaryDiskName, primaryDiskRegion, secondaryDiskRegion, diskSizeGb, diskType);
      }
    
      // Creates a secondary disk in a specified region.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createDiskSecondaryRegional(String projectId,
           String secondaryProjectId, String primaryDiskName, String secondaryDiskName,
           String primaryDiskRegion, String secondaryDiskRegion, long diskSizeGb, String diskType)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        List<String> replicaZones = Arrays.asList(
            String.format("projects/%s/zones/%s-c", secondaryProjectId, secondaryDiskRegion),
            String.format("projects/%s/zones/%s-b", secondaryProjectId, secondaryDiskRegion));
    
        String primaryDiskSource = String.format("projects/%s/regions/%s/disks/%s",
            projectId, primaryDiskRegion, primaryDiskName);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) disksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create()) {
          [DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html) asyncReplication = [DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html).newBuilder()
              .setDisk(primaryDiskSource)
              .build();
    
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .addAllReplicaZones(replicaZones)
              .setName(secondaryDiskName)
              .setSizeGb(diskSizeGb)
              .setType(diskType)
              .setRegion(secondaryDiskRegion)
              .setAsyncPrimaryDisk(asyncReplication)
              .build();
    
          // Wait for the create disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.insertAsync(secondaryProjectId, secondaryDiskRegion, disk)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error creating secondary disks! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 

Create a zonal or regional secondary disk using one of the following code samples:

##### Create a zonal secondary disk
    
    
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
    // The project for the secondary disk.
    const secondaryProjectId = await disksClient.getProjectId();
    
    // The zone for the secondary disk. The primary and secondary disks must be in different regions.
    // secondaryLocation = 'us-central1-a';
    
    // The name of the secondary disk.
    // secondaryDiskName = 'secondary-disk-name';
    
    // The project that contains the primary disk.
    const primaryProjectId = await disksClient.getProjectId();
    
    // The zone for the primary disk.
    // primaryLocation = 'us-central1-b';
    
    // The name of the primary disk that the secondary disk receives data from.
    // primaryDiskName = 'primary-disk-name';
    
    // The disk type. Must be one of `pd-ssd` or `pd-balanced`.
    const diskType = `zones/${secondaryLocation}/diskTypes/pd-balanced`;
    
    // The size of the secondary disk in gigabytes.
    const diskSizeGb = 10;
    
    // Create a secondary disk identical to the primary disk.
    async function callCreateComputeSecondaryDisk() {
      // Create a secondary disk
      const disk = new compute.Disk({
        sizeGb: diskSizeGb,
        name: secondaryDiskName,
        zone: secondaryLocation,
        type: diskType,
        asyncPrimaryDisk: new compute.DiskAsyncReplication({
          // Make sure that the primary disk supports asynchronous replication.
          // Only certain persistent disk types, like `pd-balanced` and `pd-ssd`, are eligible.
          disk: `projects/${primaryProjectId}/zones/${primaryLocation}/disks/${primaryDiskName}`,
        }),
      });
    
      const [response] = await disksClient.insert({
        project: secondaryProjectId,
        zone: secondaryLocation,
        diskResource: disk,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create secondary disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: secondaryProjectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Secondary disk: ${secondaryDiskName} created.`);
    }
    
    await callCreateComputeSecondaryDisk();

##### Create a regional secondary disk
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a regionDisksClient
    const regionDisksClient = new computeLib.[RegionDisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a regionOperationsClient
    const regionOperationsClient = new computeLib.[RegionOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project for the secondary disk.
    const secondaryProjectId = await regionDisksClient.getProjectId();
    
    // The region for the secondary disk.
    // secondaryLocation = 'us-central1';
    
    // The name of the secondary disk.
    // secondaryDiskName = 'secondary-disk-name';
    
    // The project that contains the primary disk.
    const primaryProjectId = await regionDisksClient.getProjectId();
    
    // The region for the primary disk.
    // primaryLocation = 'us-central2';
    
    // The name of the primary disk that the secondary disk receives data from.
    // primaryDiskName = 'primary-disk-name';
    
    // The disk type. Must be one of `pd-ssd` or `pd-balanced`.
    const diskType = `regions/${secondaryLocation}/diskTypes/pd-balanced`;
    
    // The size of the secondary disk in gigabytes.
    const diskSizeGb = 10;
    
    // Create a secondary disk identical to the primary disk.
    async function callCreateComputeRegionalSecondaryDisk() {
      // Create a secondary disk
      const disk = new compute.Disk({
        sizeGb: diskSizeGb,
        name: secondaryDiskName,
        region: secondaryLocation,
        type: diskType,
        replicaZones: [
          `zones/${secondaryLocation}-a`,
          `zones/${secondaryLocation}-b`,
        ],
        asyncPrimaryDisk: new compute.DiskAsyncReplication({
          // Make sure that the primary disk supports asynchronous replication.
          // Only certain persistent disk types, like `pd-balanced` and `pd-ssd`, are eligible.
          disk: `projects/${primaryProjectId}/regions/${primaryLocation}/disks/${primaryDiskName}`,
        }),
      });
    
      const [response] = await regionDisksClient.insert({
        project: secondaryProjectId,
        diskResource: disk,
        region: secondaryLocation,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create secondary disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await regionOperationsClient.wait({
          operation: operation.name,
          project: secondaryProjectId,
          region: secondaryLocation,
        });
      }
    
      console.log(`Secondary disk: ${secondaryDiskName} created.`);
    }
    
    await callCreateComputeRegionalSecondaryDisk();

###  Python 

Create a zonal or regional secondary disk using one of the following code samples:

##### Create a zonal secondary disk
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
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
    
    
    def create_secondary_disk(
        primary_disk_name: str,
        primary_disk_project: str,
        primary_disk_zone: str,
        secondary_disk_name: str,
        secondary_disk_project: str,
        secondary_disk_zone: str,
        disk_size_gb: int,
        disk_type: str = "pd-ssd",
    ) -> compute_v1.Disk:
        """Create a secondary disk with a primary disk as a source.
        Args:
            primary_disk_name (str): The name of the primary disk.
            primary_disk_project (str): The project of the primary disk.
            primary_disk_zone (str): The location of the primary disk.
            secondary_disk_name (str): The name of the secondary disk.
            secondary_disk_project (str): The project of the secondary disk.
            secondary_disk_zone (str): The location of the secondary disk.
            disk_size_gb (int): The size of the disk in GB. Should be the same as the primary disk.
            disk_type (str): The type of the disk. Must be one of pd-ssd or pd-balanced.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.name = secondary_disk_name
        disk.size_gb = disk_size_gb
        disk.type = f"zones/{primary_disk_zone}/diskTypes/{disk_type}"
        disk.async_primary_disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DiskAsyncReplication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskAsyncReplication.html)(
            disk=f"projects/{primary_disk_project}/zones/{primary_disk_zone}/disks/{primary_disk_name}"
        )
    
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(
            project=secondary_disk_project, zone=secondary_disk_zone, disk_resource=disk
        )
        wait_for_extended_operation(operation, "create_secondary_disk")
    
        secondary_disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(
            project=secondary_disk_project,
            zone=secondary_disk_zone,
            disk=secondary_disk_name,
        )
        return secondary_disk
    
    

##### Create a regional secondary disk
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
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
    
    
    def create_secondary_region_disk(
        primary_disk_name: str,
        primary_disk_project: str,
        primary_disk_region: str,
        secondary_disk_name: str,
        secondary_disk_project: str,
        secondary_disk_region: str,
        disk_size_gb: int,
        disk_type: str = "pd-ssd",
    ) -> compute_v1.Disk:
        """Create a secondary disk in replica zones with a primary region disk as a source .
        Args:
            primary_disk_name (str): The name of the primary disk.
            primary_disk_project (str): The project of the primary disk.
            primary_disk_region (str): The location of the primary disk.
            secondary_disk_name (str): The name of the secondary disk.
            secondary_disk_project (str): The project of the secondary disk.
            secondary_disk_region (str): The location of the secondary disk.
            disk_size_gb (int): The size of the disk in GB. Should be the same as the primary disk.
            disk_type (str): The type of the disk. Must be one of pd-ssd or pd-balanced.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.name = secondary_disk_name
        disk.size_gb = disk_size_gb
        disk.type = f"regions/{primary_disk_region}/diskTypes/{disk_type}"
        disk.async_primary_disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DiskAsyncReplication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskAsyncReplication.html)(
            disk=f"projects/{primary_disk_project}/regions/{primary_disk_region}/disks/{primary_disk_name}"
        )
    
        # Set the replica zones for the secondary disk. By default, in b and c zones.
        disk.replica_zones = [
            f"zones/{secondary_disk_region}-b",
            f"zones/{secondary_disk_region}-c",
        ]
    
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_insert)(
            project=secondary_disk_project,
            region=secondary_disk_region,
            disk_resource=disk,
        )
        wait_for_extended_operation(operation, "create_secondary_region_disk")
        secondary_disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_get)(
            project=secondary_disk_project,
            region=secondary_disk_region,
            disk=secondary_disk_name,
        )
        return secondary_disk
    
    

###  REST 

Create a zonal or regional secondary disk using one of the following methods:

  * To create a zonal secondary disk, use the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/SECONDARY_DISK_PROJECT/zones/SECONDARY_DISK_LOCATION/disks
        
        {
        "name": "SECONDARY_DISK_NAME",
        "sizeGb": "DISK_SIZE",
        "type": "DISK_TYPE"
        "asyncPrimaryDisk": {
          "disk": "projects/PRIMARY_DISK_PROJECT/PRIMARY_DISK_LOCATION_PARAMETER/PRIMARY_DISK_LOCATION/disks/PRIMARY_DISK_NAME"
          }
        }
        

  * To create a regional secondary disk, use the [`regionDisks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/SECONDARY_DISK_PROJECT/regions/SECONDARY_DISK_LOCATION/disks
        
        {
        "name": "SECONDARY_DISK_NAME",
        "sizeGb": "DISK_SIZE",
        "type": "DISK_TYPE"
        "asyncPrimaryDisk": {
          "disk": "projects/PRIMARY_DISK_PROJECT/PRIMARY_DISK_LOCATION_PARAMETER/PRIMARY_DISK_LOCATION/disks/PRIMARY_DISK_NAME"
          }
        }
        




Replace the following:

  * `SECONDARY_DISK_PROJECT`: the project for the secondary disk.
  * `SECONDARY_DISK_LOCATION`: the region or zone for the secondary disk. 
    * For a regional disk, use the region.
    * For a zonal disk, use the zone.
  * `SECONDARY_DISK_NAME`: the name for the secondary disk.
  * `DISK_SIZE`: the size of the secondary disk. Must be the same as the size of the primary disk.
  * `PRIMARY_DISK_PROJECT`: the project that contains the primary disk.
  * `PRIMARY_DISK_LOCATION_PARAMETER`: the location parameter for the primary disk. 
    * For a regional primary disk, use `regions`.
    * For a zonal primary disk, use `zones`.
  * `PRIMARY_DISK_LOCATION`: the primary disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.
  * `PRIMARY_DISK_NAME`: the name of the primary disk that the secondary disk receives data from.

**Note:** You can't create a secondary disk from a snapshot, image or disk. Don't add the `sourceSnapshot`, `sourceImage`, or `sourceDisk` fields to your request.

###  Terraform 

To create a secondary disk identical to the primary disk, use the [`compute_disk` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk).
    
    
    resource "google_compute_disk" "secondary_disk" {
      name = "secondary-disk"
      type = "pd-ssd"
      zone = "europe-west3-a"
    
      async_primary_disk {
        disk = google_compute_disk.primary_disk.id
      }
    
      physical_block_size_bytes = 4096
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

#### Create a custom secondary disk

This section discusses how to create a custom secondary disk, that is, a secondary disk whose properties differ from the primary disk.

If the primary disk is a boot disk, you can't change or remove any of the primary disk's guest OS features. You can only add more guest OS features. For more information, see [Secondary disk customization](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#change_secondary_disk).

You can create a custom secondary disk with the gcloud CLI, REST, or Terraform. You can't customize the secondary disk from the Google Cloud console.

###  gcloud 

To create a custom secondary disk, use the `gcloud compute disks create` command as described in Create a secondary disk identical to the primary disk. Use additional flags to customize the secondary disk's properties.

The following are examples of how to customize the secondary disk: 

  * To specify additional guest OS features, use the `--guest-os-features` parameter. 
        
        --guest-os-features=UEFI_COMPATIBLE,GVNIC,MULTI_IP_SUBNET
         

  * To assign additional labels to the secondary disk, use the `--labels` parameter. 
        
        --labels=secondary-disk-for-replication=yes
          




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createCustomSecondaryDisk creates a new secondary disk in a project in given zone.
    // Note: secondary disk should be located in a different region, but within the same continent.
    // More details: https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
    func createCustomSecondaryDisk(
    	w io.Writer,
    	projectID, zone, diskName, primaryDiskName, primaryZone string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-central1-a"
    	// diskName := "your_disk_name"
    	// primaryDiskName := "your_disk_name2"
    	// primaryDiskZone := "us-east1-b"
    	// diskSizeGb := 20
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	primaryFullDiskName := fmt.Sprintf("projects/%s/zones/%s/disks/%s", projectID, primaryZone, primaryDiskName)
    
    	req := &computepb.InsertDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		DiskResource: &computepb.Disk{
    			Name:   proto.String(diskName),
    			Zone:   proto.String(zone),
    			SizeGb: proto.Int64(diskSizeGb),
    			AsyncPrimaryDisk: &computepb.DiskAsyncReplication{
    				Disk: proto.String(primaryFullDiskName),
    			},
    			// More about guest features: https://cloud.google.com/compute/docs/images/create-custom#guest-os-features
    			GuestOsFeatures: []*computepb.GuestOsFeature{
    				{Type: proto.String("UEFI_COMPATIBLE")},
    				{Type: proto.String("GVNIC")},
    				{Type: proto.String("MULTI_IP_SUBNET")},
    			},
    			// The secondary disk automatically inherits the labels of the primary disk.
    			Labels: map[string]string{
    				"secondary-disk-for-replication": "yes",
    			},
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateSecondaryCustomDisk {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The project that contains the primary disk.
        String primaryProjectId = "PRIMARY_PROJECT_ID";
        // The project that contains the secondary disk.
        String secondaryProjectId = "SECONDARY_PROJECT_ID";
        // Name of the primary disk you want to use.
        String primaryDiskName = "PRIMARY_DISK_NAME";
        // Name of the zone in which your primary disk is located.
        // Learn more about zones and regions:
        // https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
        String primaryDiskZone = "us-central1-a";
        // Name of the disk you want to create.
        String secondaryDiskName = "SECONDARY_DISK_NAME";
        // Name of the zone in which you want to create the secondary disk.
        String secondaryDiskZone = "us-east1-c";
        // Size of the new disk in gigabytes.
        long diskSizeGb = 30L;
        // The type of the disk you want to create. This value uses the following format:
        // "projects/{projectId}/zones/{zone}/diskTypes/
        // (pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        String diskType = String.format(
            "projects/%s/zones/%s/diskTypes/pd-balanced", secondaryProjectId, secondaryDiskZone);
    
        createSecondaryCustomDisk(primaryProjectId, secondaryProjectId, primaryDiskName,
            secondaryDiskName, primaryDiskZone, secondaryDiskZone, diskSizeGb,  diskType);
      }
    
      // Creates a secondary disk with specified custom parameters.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createSecondaryCustomDisk(String primaryProjectId, String secondaryProjectId,
          String primaryDiskName, String secondaryDiskName, String primaryDiskZone,
          String secondaryDiskZone, long diskSizeGb, String diskType)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          String primaryDiskSource = String.format("projects/%s/zones/%s/disks/%s",
              primaryProjectId, primaryDiskZone, primaryDiskName);
    
          [DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html) asyncReplication = [DiskAsyncReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplication.html).newBuilder()
              .setDisk(primaryDiskSource)
              .build();
    
          // Define the guest OS features.
          List<GuestOsFeature> guestOsFeatures = Arrays.asList(
              [GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html).newBuilder().setType("UEFI_COMPATIBLE").build(),
              [GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html).newBuilder().setType("GVNIC").build(),
              [GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html).newBuilder().setType("MULTI_IP_SUBNET").build());
    
          // Define the labels.
          Map<String, String> labels = new HashMap<>();
          labels.put("secondary-disk-for-replication", "yes");
    
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setName(secondaryDiskName)
              .setSizeGb(diskSizeGb)
              .setType(diskType)
              .setZone(secondaryDiskZone)
              .addAllGuestOsFeatures(guestOsFeatures)
              .putAllLabels(labels)
              .setAsyncPrimaryDisk(asyncReplication)
              .build();
    
          // Wait for the create disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.insertAsync(secondaryProjectId, secondaryDiskZone, disk)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error creating secondary custom disks! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // If you want to create regional disk, you should use: RegionDisksClient and RegionOperationsClient.
    // Instantiate a diskClient
    const disksClient = new computeLib.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project for the secondary disk.
    const secondaryProjectId = await disksClient.getProjectId();
    
    // The zone or region for the secondary disk. The primary and secondary disks must be in different regions.
    // If you use RegionDisksClient- define region, if DisksClient- define zone.
    // secondaryLocation = 'us-central1-a';
    
    // The name of the secondary disk.
    // secondaryDiskName = 'secondary-disk-name';
    
    // The project that contains the primary disk.
    const primaryProjectId = await disksClient.getProjectId();
    
    // The zone or region for the primary disk.
    // If you use RegionDisksClient- define region, if DisksClient- define zone.
    // primaryLocation = 'us-central1-b';
    
    // The name of the primary disk that the secondary disk receives data from.
    // primaryDiskName = 'primary-disk-name';
    
    // The disk type. Must be one of `pd-ssd` or `pd-balanced`.
    const diskType = `zones/${secondaryLocation}/diskTypes/pd-balanced`;
    
    // The size of the secondary disk in gigabytes.
    const diskSizeGb = 10;
    
    // Create a secondary disk identical to the primary disk.
    async function callCreateComputeSecondaryDisk() {
      // Create a secondary disk
      const disk = new compute.Disk({
        sizeGb: diskSizeGb,
        name: secondaryDiskName,
        // If you use RegionDisksClient, pass region as an argument instead of zone
        zone: secondaryLocation,
        type: diskType,
        asyncPrimaryDisk: new compute.DiskAsyncReplication({
          // Make sure that the primary disk supports asynchronous replication.
          // Only certain persistent disk types, like `pd-balanced` and `pd-ssd`, are eligible.
          disk: `projects/${primaryProjectId}/zones/${primaryLocation}/disks/${primaryDiskName}`,
        }),
        // Specify additional guest OS features.
        // To learn more about OS features, open: `https://cloud.google.com/compute/docs/disks/async-pd/configure?authuser=0#secondary2`.
        // You don't need to include the guest OS features of the primary disk.
        // The secondary disk automatically inherits the guest OS features of the primary disk.
        guestOsFeatures: [
          new compute.GuestOsFeature({
            type: 'NEW_FEATURE_ID_1',
          }),
        ],
        // Assign additional labels to the secondary disk.
        // You don't need to include the labels of the primary disk.
        // The secondary disk automatically inherits the labels from the primary disk
        labels: {
          key: 'value',
        },
      });
    
      const [response] = await disksClient.insert({
        project: secondaryProjectId,
        // If you use RegionDisksClient, pass region as an argument instead of zone
        zone: secondaryLocation,
        diskResource: disk,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create secondary disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: secondaryProjectId,
          // If you use RegionOperationsClient, pass region as an argument instead of zone
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Custom secondary disk: ${secondaryDiskName} created.`);
    }
    
    await callCreateComputeSecondaryDisk();

###  Python 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
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
    
    
    def create_secondary_custom_disk(
        primary_disk_name: str,
        primary_disk_project: str,
        primary_disk_zone: str,
        secondary_disk_name: str,
        secondary_disk_project: str,
        secondary_disk_zone: str,
        disk_size_gb: int,
        disk_type: str = "pd-ssd",
    ) -> compute_v1.Disk:
        """Creates a custom secondary disk whose properties differ from the primary disk.
        Args:
            primary_disk_name (str): The name of the primary disk.
            primary_disk_project (str): The project of the primary disk.
            primary_disk_zone (str): The location of the primary disk.
            secondary_disk_name (str): The name of the secondary disk.
            secondary_disk_project (str): The project of the secondary disk.
            secondary_disk_zone (str): The location of the secondary disk.
            disk_size_gb (int): The size of the disk in GB. Should be the same as the primary disk.
            disk_type (str): The type of the disk. Must be one of pd-ssd or pd-balanced.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.name = secondary_disk_name
        disk.size_gb = disk_size_gb
        disk.type = f"zones/{primary_disk_zone}/diskTypes/{disk_type}"
        disk.async_primary_disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DiskAsyncReplication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskAsyncReplication.html)(
            disk=f"projects/{primary_disk_project}/zones/{primary_disk_zone}/disks/{primary_disk_name}"
        )
    
        # Add guest OS features to the secondary dis
        # For possible values, visit:
        # https://cloud.google.com/compute/docs/images/create-custom#guest-os-features
        disk.guest_os_features = [[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GuestOsFeature.html)(type="MULTI_IP_SUBNET")]
    
        # Assign additional labels to the secondary disk
        disk.labels = {
            "source-disk": primary_disk_name,
            "secondary-disk-for-replication": "true",
        }
    
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(
            project=secondary_disk_project, zone=secondary_disk_zone, disk_resource=disk
        )
        wait_for_extended_operation(operation, "create_secondary_disk")
    
        secondary_disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(
            project=secondary_disk_project,
            zone=secondary_disk_zone,
            disk=secondary_disk_name,
        )
        return secondary_disk
    
    

###  REST 

To create a custom secondary disk, use the same method described in Create a secondary disk identical to the primary disk. Specify additional fields to customize the secondary disk's properties.

The following are examples of how to customize the secondary disk: 

  * To specify additional guest OS features, use the `guestOsFeatures` field. You can only specify additional guest OS features; you can't change or remove any of the guest OS features that were copied from the primary disk. 
        
        "guestOsFeatures": [
          {
            "type": "NEW_FEATURE_ID_1"
          },
          {
            "type": "NEW_FEATURE_ID_1"
          }
        ]
        

  * To assign additional labels to the secondary disk, use the `labels` field. 
        
        "labels": [
            {
              "key": "value"
            },
          ]
        




###  Terraform 

To create a custom secondary disk, use the same method described in Create a secondary disk identical to the primary disk. You can specify additional fields to customize the secondary disk's properties.

The following are examples of how to customize the secondary disk: 

  * To specify additional guest OS features, use the `guest_os_features` field. You can only specify additional guest OS features; you can't change or remove any of the guest OS features that were copied from the primary disk. 
        
        guest_os_features {
          type = "SECURE_BOOT"
        }
        guest_os_features {
          type = "MULTI_IP_SUBNET"
        }
        guest_os_features {
          type = "WINDOWS"
        }
        

  * To assign additional labels to the secondary disk, use the `labels` field. 
        
        labels = {
            environment = "dev"
          }
        




## Start replication

After you create a primary and secondary disk, you must [start replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication) to begin replicating data from the primary disk to the secondary disk.

## What's next

  * Learn how to [manage disks that use Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-async-disks).
  * Learn how to [manage replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication).
  * Learn how to [manage consistency groups](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups).
  * Learn how to [monitor Asynchronous Replication performance](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
