---
url: https://docs.cloud.google.com/compute/docs/disks/create-snapshots/
title: Create archive and standard disk snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:50.798000+00:00
---

# Create archive and standard disk snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/create-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create archive and standard disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Create [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) to periodically back up data from zonal and regional Persistent Disk and Google Cloud Hyperdisk volumes.

You can create snapshots from disks even while they are attached to running instances. Snapshots are, by default, [global resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#globalresources), so you can use them to [restore data](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot) to a new disk or VM within the same project. For additional data protection and cost management, you can control where you can use your snapshots to create new disks. To restrict the regions where your snapshots can restore data, you can create a [regionally scoped snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot-scopes) and [set allowed access locations](https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope) ([Preview](https://cloud.google.com/products/#product-launch-stages)). You can also [share snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#sharing_snapshots) across projects.

## Before you begin

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create regionally scoped snapshots, [set your default snapshot creation and restore locations](https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope) before you complete the steps on this page.
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

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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




## Required roles and permissions

To get the permissions that you need to create and manage snapshots, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage snapshots. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage snapshots:

  * `compute.snapshots.create` on the project
  * To create a snapshot of a zonal disk: `compute.disks.createSnapshot`
  * If the disk is a regional disk and you want a snapshot of the data on the disk: 
    * `compute.instances.useReadOnly`
    * `compute.disks.createSnapshot`
  * If the disk is a regional disk and you want a snapshot of a replica recovery checkpoint: `compute.disks.createSnapshot`
  * If you want to create a regionally scoped snapshot: 
    * `compute.regionSnapshots.create`
    * `compute.disks.useReadOnly`
  * To create a snapshot of a regional disk from a replica recovery checkpoint: `compute.disks.createSnapshot` on the disk 
  * To create a snapshot schedule: `compute.resourcePolicies.create` on the project or organization 
  * To attach a snapshot schedule to a disk: 
    * `compute.disks.addResourcePolicies` on the disk
    * `compute.resourcePolicies.use` on the resource policy
  * To delete a snapshot: 
    * `compute.snapshots.delete` on the snapshot
    * `compute.snapshots.list` on the project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare for creating snapshots

To prepare for creating snapshots of Persistent Disk or Hyperdisk volumes, complete the following steps:

  * Review [Best practices for Compute Engine disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) to prepare your disk for snapshotting.

  * If you want to customize the default storage location for all your new globally scoped snapshots, [update the snapshot settings for your project](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings#snapshot_settings_how_to_update). Google Cloud maintains a predefined default storage location value until you update the snapshot settings for the first time. This predefined location is the nearest multi-region to the source disk.

  * Read [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) to learn about creating a snapshot schedule and attaching it to your disks. Backing up your disks regularly with scheduled snapshots can reduce the risk of unexpected data loss.


**Important:** If you pause your applications before creating a snapshot, resume your workloads only after the snapshot resource reaches the `UPLOADING` status. For more information, see the table in [Manually creating application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

## Create a snapshot of a disk

The steps to create a snapshot of a disk depend on whether you're creating a snapshot of a zonal disk or regional disk.

**Caution:** If you try to create a snapshot from a disk and the snapshot creation process fails, you won't be able to delete the original disk until you capture a clean snapshot. This failsafe helps to prevent the accidental deletion of source data in the event of an unsuccessful backup. 

### Create a snapshot of a zonal disk

###  Console 

  1. Go to the **Create a Snapshot** page in the Google Cloud console.

[Go to the Create a Snapshot page](https://console.cloud.google.com/compute/snapshotsAdd)
  2. Enter a snapshot **Name**.
  3. Select a **Snapshot type**. The default is a `STANDARD` snapshot, which is the best option for long-term back up and disaster recovery.

Choose **Archive snapshot** for more cost-efficient data retention.

  4. Optional: Enter a **Description** of the snapshot.
  5. Under **Source disk** , select the existing disk that you want to create a snapshot of.
  6. In the **Location** section, [choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

The predefined or customized default location defined in your snapshot settings is automatically selected. Optionally, you can override the snapshot settings and store your snapshots in a custom storage location by doing the following:

     1. Choose the type of storage location that you want for your snapshot.

        * Choose [**Multi-regional**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) for higher availability at a higher cost.
        * Choose [**Regional snapshots**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) for more control over the physical location of your data at a lower cost.
     2. In the **Select location** field, select the specific region or multi-region that you want to use. To use the region or multi-region that is closest to your source disk, select **Based on disk's location**. 
  7. Click **Create** to create the snapshot.



###  gcloud 

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, use the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create).
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot.
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --storage-location=STORAGE_LOCATION
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, include the `--region` flag to indicate where to create your snapshot.
        
        gcloud beta compute snapshots create SNAPSHOT_NAME \
            --region=SNAPSHOT_SCOPE_REGION
            --source-disk=SOURCE_DISK_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --snapshot-type=SNAPSHOT_TYPE
        




Replace the following:

  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the Persistent Disk volume from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `--storage-location` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `gcloud compute snapshots create` command instead of the [`gcloud compute disks snapshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

###  Terraform 

To create a snapshot of the zonal Persistent Disk volume, use the [`google_compute_snapshot`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_snapshot) resource.
    
    
    resource "google_compute_snapshot" "snapdisk" {
      name        = "snapshot-name"
      source_disk = google_compute_disk.default.name
      zone        = "us-central1-a"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  Go 

### Go

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
    
    // createSnapshot creates a snapshot of a disk.
    func createSnapshot(
    	w io.Writer,
    	projectID, diskName, snapshotName, zone, region, location, diskProjectID string,
    ) error {
    	// projectID := "your_project_id"
    	// diskName := "your_disk_name"
    	// snapshotName := "your_snapshot_name"
    	// zone := "europe-central2-b"
    	// region := "eupore-central2"
    	// location = "eupore-central2"
    	// diskProjectID = "YOUR_DISK_PROJECT_ID"
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	if zone == "" && region == "" {
    		return fmt.Errorf("you need to specify `zone` or `region` for this function to work")
    	}
    
    	if zone != "" && region != "" {
    		return fmt.Errorf("you can't set both `zone` and `region` parameters")
    	}
    
    	if diskProjectID == "" {
    		diskProjectID = projectID
    	}
    
    	disk := &computepb.Disk{}
    	locations := []string{}
    	if location != "" {
    		locations = append(locations, location)
    	}
    
    	if zone != "" {
    		disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    		if err != nil {
    			return fmt.Errorf("NewDisksRESTClient: %w", err)
    		}
    		defer disksClient.Close()
    
    		getDiskReq := &computepb.GetDiskRequest{
    			Project: projectID,
    			Zone:    zone,
    			Disk:    diskName,
    		}
    
    		disk, err = disksClient.Get(ctx, getDiskReq)
    		if err != nil {
    			return fmt.Errorf("unable to get disk: %w", err)
    		}
    	} else {
    		regionDisksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    		if err != nil {
    			return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
    		}
    		defer regionDisksClient.Close()
    
    		getDiskReq := &computepb.GetRegionDiskRequest{
    			Project: projectID,
    			Region:  region,
    			Disk:    diskName,
    		}
    
    		disk, err = regionDisksClient.Get(ctx, getDiskReq)
    		if err != nil {
    			return fmt.Errorf("unable to get disk: %w", err)
    		}
    	}
    
    	req := &computepb.InsertSnapshotRequest{
    		Project: projectID,
    		SnapshotResource: &computepb.Snapshot{
    			Name:             proto.String(snapshotName),
    			SourceDisk:       proto.String(disk.GetSelfLink()),
    			StorageLocations: locations,
    		},
    	}
    
    	op, err := snapshotsClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create snapshot: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Snapshot created\n")
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
    import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
    import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateSnapshot {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // You need to pass `zone` or `region` parameter relevant to the disk you want to
        // snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
        // regional disks.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // Name of the snapshot that you want to create.
        String snapshotName = "YOUR_SNAPSHOT_NAME";
    
        // The zone of the source disk from which you create the snapshot (for zonal disks).
        String zone = "europe-central2-b";
    
        // The region of the source disk from which you create the snapshot (for regional disks).
        String region = "your-disk-region";
    
        // The Cloud Storage multi-region or the Cloud Storage region where you
        // want to store your snapshot.
        // You can specify only one storage location. Available locations:
        // https://cloud.google.com/storage/docs/locations#available-locations
        String location = "europe-central2";
    
        // Project ID or project number of the Cloud project that
        // hosts the disk you want to snapshot. If not provided, the value will be defaulted
        // to 'projectId' value.
        String diskProjectId = "YOUR_DISK_PROJECT_ID";
    
        createSnapshot(projectId, diskName, snapshotName, zone, region, location, diskProjectId);
      }
    
      // Creates a snapshot of a disk.
      public static void createSnapshot(String projectId, String diskName, String snapshotName,
          String zone, String region, String location, String diskProjectId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `snapshotsClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
    
          if (zone.isEmpty() && region.isEmpty()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You need to specify 'zone' or 'region' for this function to work");
          }
    
          if (!zone.isEmpty() && !region.isEmpty()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You can't set both 'zone' and 'region' parameters");
          }
    
          // If Disk's project id is not specified, then the projectId parameter will be used.
          if (diskProjectId.isEmpty()) {
            diskProjectId = projectId;
          }
    
          // If zone is not empty, use the DisksClient to create a disk.
          // Else, use the RegionDisksClient.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk;
          if (!zone.isEmpty()) {
            [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create();
            disk = disksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html#com_google_cloud_compute_v1_DisksClient_get_com_google_cloud_compute_v1_GetDiskRequest_)(projectId, zone, diskName);
          } else {
            [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) regionDisksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create();
            disk = regionDisksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html#com_google_cloud_compute_v1_RegionDisksClient_get_com_google_cloud_compute_v1_GetRegionDiskRequest_)(diskProjectId, region, diskName);
          }
    
          // Set the snapshot properties.
          [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshotResource;
          if (!location.isEmpty()) {
            snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                .setName(snapshotName)
                .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                .addStorageLocations(location)
                .build();
          } else {
            snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                .setName(snapshotName)
                .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                .build();
          }
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = snapshotsClient.insertAsync(projectId, snapshotResource)
              .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Snapshot creation failed!" + operation);
            return;
          }
    
          // Retrieve the created snapshot.
          [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshot = snapshotsClient.get(projectId, snapshotName);
          System.out.printf("Snapshot created: %s", snapshot.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html#com_google_cloud_compute_v1_Snapshot_getName__)());
    
        }
      }
    }

###  Node.js 

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const diskName = 'YOUR_DISK_NAME';
    // const snapshotName = 'YOUR_SNAPSHOT_NAME';
    // const zone = 'europe-central2-b';
    // const region = '';
    // const location = 'europe-central2';
    // let diskProjectId = 'YOUR_DISK_PROJECT_ID';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createSnapshot() {
      const snapshotsClient = new compute.[SnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      let disk;
    
      if (!zone && !region) {
        throw new Error(
          'You need to specify `zone` or `region` for this function to work.'
        );
      }
    
      if (zone && region) {
        throw new Error("You can't set both `zone` and `region` parameters");
      }
    
      if (!diskProjectId) {
        diskProjectId = projectId;
      }
    
      if (zone) {
        const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
        [disk] = await disksClient.get({
          project: diskProjectId,
          zone,
          disk: diskName,
        });
      } else {
        const regionDisksClient = new compute.[RegionDisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
        [disk] = await regionDisksClient.get({
          project: diskProjectId,
          region,
          disk: diskName,
        });
      }
    
      const snapshotResource = {
        name: snapshotName,
        sourceDisk: disk.selfLink,
      };
    
      if (location) {
        snapshotResource.storageLocations = [location];
      }
    
      const [response] = await snapshotsClient.insert({
        project: projectId,
        snapshotResource,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create snapshot operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Snapshot created.');
    }
    
    createSnapshot();

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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
    
    
    def create_snapshot(
        project_id: str,
        disk_name: str,
        snapshot_name: str,
        *,
        zone: str | None = None,
        region: str | None = None,
        location: str | None = None,
        disk_project_id: str | None = None,
    ) -> compute_v1.Snapshot:
        """
        Create a snapshot of a disk.
    
        You need to pass `zone` or `region` parameter relevant to the disk you want to
        snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
        regional disks.
    
        Args:
            project_id: project ID or project number of the Cloud project you want
                to use to store the snapshot.
            disk_name: name of the disk you want to snapshot.
            snapshot_name: name of the snapshot to be created.
            zone: name of the zone in which is the disk you want to snapshot (for zonal disks).
            region: name of the region in which is the disk you want to snapshot (for regional disks).
            location: The Cloud Storage multi-region or the Cloud Storage region where you
                want to store your snapshot.
                You can specify only one storage location. Available locations:
                https://cloud.google.com/storage/docs/locations#available-locations
            disk_project_id: project ID or project number of the Cloud project that
                hosts the disk you want to snapshot. If not provided, will look for
                the disk in the `project_id` project.
    
        Returns:
            The new snapshot instance.
        """
        if zone is None and region is None:
            raise RuntimeError(
                "You need to specify `zone` or `region` for this function to work."
            )
        if zone is not None and region is not None:
            raise RuntimeError("You can't set both `zone` and `region` parameters.")
    
        if disk_project_id is None:
            disk_project_id = project_id
    
        if zone is not None:
            disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
            disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=disk_project_id, zone=zone, disk=disk_name)
        else:
            regio_disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
            disk = regio_disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_get)(
                project=disk_project_id, region=region, disk=disk_name
            )
    
        snapshot = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Snapshot](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Snapshot.html)()
        snapshot.source_disk = disk.self_link
        snapshot.name = snapshot_name
        if location:
            snapshot.storage_locations = [location]
    
        snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
        operation = snapshot_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_insert)(project=project_id, snapshot_resource=snapshot)
    
        wait_for_extended_operation(operation, "snapshot creation")
    
        return snapshot_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_get)(project=project_id, snapshot=snapshot_name)
    
    

###  REST 

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotType": "SNAPSHOT_TYPE"
        }
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, make a `POST` request to the `snapshots.insert` method and include the `storageLocations` property in your request:
        
        POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotType": "SNAPSHOT_TYPE",
            "storageLocations": [
                "STORAGE_LOCATION"
            ],
        }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, make a `POST` request to the `snapshots.insert` method and define the creation region:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/regions/SNAPSHOT_SCOPE_REGION/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotType": "SNAPSHOT_TYPE"
        }
        




Replace the following:

  * DESTINATION_PROJECT_ID: The ID of project in which you want to create the snapshot.
  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_PROJECT_ID: The ID of the source disk project.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the Persistent Disk volume from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `storageLocations` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `storageLocations` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `snapshots.insert` method instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

### Create a snapshot of a regional disk

You can create snapshots of your regional disk in one of the following ways:

  * By using the data on the source disk. To use this snapshot creation method, you must have a synced zonal replica available.
  * By using the replica recovery checkpoint of a degraded disk. You can create snapshots from a checkpoint only by using the Google Cloud CLI or REST.

**Important:** Google recommends that you use the checkpoint to create standard snapshots only when your degraded replicated disk doesn't have a synced replica available. To avoid data loss, if your degraded disk has a synced replica available, always use the data on the disk to create your snapshot. 

After you [prepare the disk](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency), you can create a snapshot. When creating a snapshot of a regional disk, you must indicate the region where the source disk is located.

###  Console 

  1. Go to the **Create a Snapshot** page in the Google Cloud console.

[Go to the Create a Snapshot page](https://console.cloud.google.com/compute/snapshotsAdd)
  2. Enter a snapshot **Name**.
  3. Select a **Snapshot type**. The default is a `STANDARD` snapshot, which is the best option for long-term back up and disaster recovery.

Choose **Archive snapshot** for more cost-efficient data retention.

  4. Optional: Enter a **Description** of the snapshot.
  5. Under **Source disk** , select the existing disk that you want to create a snapshot of.
  6. In the **Location** section, [choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

The predefined or customized default location defined in your snapshot settings is automatically selected. Optionally, you can override the snapshot settings and store your snapshots in a custom storage location by doing the following:

     1. Choose the type of storage location that you want for your snapshot.

        * Choose [**Multi-regional**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) for higher availability at a higher cost.
        * Choose [**Regional snapshots**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) for more control over the physical location of your data at a lower cost.
     2. In the **Select location** field, select the specific region or multi-region that you want to use. To use the region or multi-region that is closest to your source disk, select **Based on disk's location**. 
  7. Click **Create** to create the snapshot.



###  gcloud 

You can create a snapshot either by using the source disk's data or its replica recovery checkpoint.

###  From disk data 

You can create a snapshot from your disk's data using the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, use the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create).
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-region=SOURCE_REGION \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot.
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-region=SOURCE_REGION \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --storage-location=STORAGE_LOCATION
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, include the `--region` flag to indicate where to create your snapshot.
        
        gcloud beta compute snapshots create SNAPSHOT_NAME \
            --region=SNAPSHOT_SCOPE_REGION \
            --source-disk=SOURCE_DISK_NAME \
            --source-disk-region=SOURCE_REGION \
            --snapshot-type=SNAPSHOT_TYPE
        




Replace the following:

  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_REGION: The region of the source disk. 
  * SOURCE_DISK_NAME: The name of the Regional Persistent Disk or Hyperdisk Balanced High Availability volume from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `--storage-location` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `gcloud compute snapshots create` command instead of the [`gcloud compute disks snapshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

###  From checkpoint 

You can create your snapshot using the [replica recovery checkpoint](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-replica-recovery-checkpoint) of a degraded disk. Your snapshot gets created as long as your incomplete replica is available.

To create a snapshot using the replica recovery checkpoint, use the [ `gcloud compute snapshots create` command ](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create). Include the `--source-disk-for-recovery-checkpoint` flag to specify that you want to create the snapshot using a replica recovery checkpoint. Exclude the `--source-disk` and `--source-disk-region` parameters. 
    
    
    gcloud compute snapshots create SNAPSHOT_NAME \
        --source-disk-for-recovery-checkpoint=SOURCE_DISK \
        --source-disk-for-recovery-checkpoint-region=SOURCE_REGION \
        --storage-location=STORAGE_LOCATION \
        --snapshot-type=SNAPSHOT_TYPE
    

Replace the following: 

  * `DESTINATION_PROJECT_ID`: The ID of project in which you want to create the snapshot.
  * `SNAPSHOT_NAME`: A name for the snapshot.
  * `SOURCE_PROJECT_ID`: The project ID of the source disk whose checkpoint you want to use to create the snapshot.
  * `SOURCE_REGION`: The region of the source disk whose checkpoint you want to use to create the snapshot. 
  * `SOURCE_DISK_NAME`: The name of the source disk whose checkpoint you want to use to create the snapshot. 
  * `STORAGE_LOCATION`: Optional: The [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.  
Use the only if you want to override the predefined or customized default storage location configured in your snapshot settings.
  * `SNAPSHOT_TYPE`: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a **STANDARD** snapshot is created.



You can use replica recovery checkpoint to create a snapshot only on [degraded disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd_replication_state). If you try to create a snapshot from a replica recovery checkpoint when the device is fully replicated, you see the following error message:
    
    
    The device is fully replicated and should not create snapshots out of a recovery checkpoint. Please
    create regular snapshots instead.
    

The Google Cloud CLI waits until the operation returns a status of `READY`, `FAILED`, or reaches the maximum timeout and returns the last known details of the snapshot.

###  Terraform 

The Terraform provider for Google Cloud doesn't support creating a snapshot of a regional disk. To track this limitation, see the [issue on GitHub](https://github.com/hashicorp/terraform-provider-google/issues/9053)

###  Go 

### Go

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
    
    // createSnapshot creates a snapshot of a disk.
    func createSnapshot(
    	w io.Writer,
    	projectID, diskName, snapshotName, zone, region, location, diskProjectID string,
    ) error {
    	// projectID := "your_project_id"
    	// diskName := "your_disk_name"
    	// snapshotName := "your_snapshot_name"
    	// zone := "europe-central2-b"
    	// region := "eupore-central2"
    	// location = "eupore-central2"
    	// diskProjectID = "YOUR_DISK_PROJECT_ID"
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	if zone == "" && region == "" {
    		return fmt.Errorf("you need to specify `zone` or `region` for this function to work")
    	}
    
    	if zone != "" && region != "" {
    		return fmt.Errorf("you can't set both `zone` and `region` parameters")
    	}
    
    	if diskProjectID == "" {
    		diskProjectID = projectID
    	}
    
    	disk := &computepb.Disk{}
    	locations := []string{}
    	if location != "" {
    		locations = append(locations, location)
    	}
    
    	if zone != "" {
    		disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    		if err != nil {
    			return fmt.Errorf("NewDisksRESTClient: %w", err)
    		}
    		defer disksClient.Close()
    
    		getDiskReq := &computepb.GetDiskRequest{
    			Project: projectID,
    			Zone:    zone,
    			Disk:    diskName,
    		}
    
    		disk, err = disksClient.Get(ctx, getDiskReq)
    		if err != nil {
    			return fmt.Errorf("unable to get disk: %w", err)
    		}
    	} else {
    		regionDisksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    		if err != nil {
    			return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
    		}
    		defer regionDisksClient.Close()
    
    		getDiskReq := &computepb.GetRegionDiskRequest{
    			Project: projectID,
    			Region:  region,
    			Disk:    diskName,
    		}
    
    		disk, err = regionDisksClient.Get(ctx, getDiskReq)
    		if err != nil {
    			return fmt.Errorf("unable to get disk: %w", err)
    		}
    	}
    
    	req := &computepb.InsertSnapshotRequest{
    		Project: projectID,
    		SnapshotResource: &computepb.Snapshot{
    			Name:             proto.String(snapshotName),
    			SourceDisk:       proto.String(disk.GetSelfLink()),
    			StorageLocations: locations,
    		},
    	}
    
    	op, err := snapshotsClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create snapshot: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Snapshot created\n")
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
    import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
    import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateSnapshot {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // You need to pass `zone` or `region` parameter relevant to the disk you want to
        // snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
        // regional disks.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // Name of the snapshot that you want to create.
        String snapshotName = "YOUR_SNAPSHOT_NAME";
    
        // The zone of the source disk from which you create the snapshot (for zonal disks).
        String zone = "europe-central2-b";
    
        // The region of the source disk from which you create the snapshot (for regional disks).
        String region = "your-disk-region";
    
        // The Cloud Storage multi-region or the Cloud Storage region where you
        // want to store your snapshot.
        // You can specify only one storage location. Available locations:
        // https://cloud.google.com/storage/docs/locations#available-locations
        String location = "europe-central2";
    
        // Project ID or project number of the Cloud project that
        // hosts the disk you want to snapshot. If not provided, the value will be defaulted
        // to 'projectId' value.
        String diskProjectId = "YOUR_DISK_PROJECT_ID";
    
        createSnapshot(projectId, diskName, snapshotName, zone, region, location, diskProjectId);
      }
    
      // Creates a snapshot of a disk.
      public static void createSnapshot(String projectId, String diskName, String snapshotName,
          String zone, String region, String location, String diskProjectId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `snapshotsClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
    
          if (zone.isEmpty() && region.isEmpty()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You need to specify 'zone' or 'region' for this function to work");
          }
    
          if (!zone.isEmpty() && !region.isEmpty()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You can't set both 'zone' and 'region' parameters");
          }
    
          // If Disk's project id is not specified, then the projectId parameter will be used.
          if (diskProjectId.isEmpty()) {
            diskProjectId = projectId;
          }
    
          // If zone is not empty, use the DisksClient to create a disk.
          // Else, use the RegionDisksClient.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk;
          if (!zone.isEmpty()) {
            [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create();
            disk = disksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html#com_google_cloud_compute_v1_DisksClient_get_com_google_cloud_compute_v1_GetDiskRequest_)(projectId, zone, diskName);
          } else {
            [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) regionDisksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create();
            disk = regionDisksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html#com_google_cloud_compute_v1_RegionDisksClient_get_com_google_cloud_compute_v1_GetRegionDiskRequest_)(diskProjectId, region, diskName);
          }
    
          // Set the snapshot properties.
          [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshotResource;
          if (!location.isEmpty()) {
            snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                .setName(snapshotName)
                .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                .addStorageLocations(location)
                .build();
          } else {
            snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                .setName(snapshotName)
                .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                .build();
          }
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = snapshotsClient.insertAsync(projectId, snapshotResource)
              .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Snapshot creation failed!" + operation);
            return;
          }
    
          // Retrieve the created snapshot.
          [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshot = snapshotsClient.get(projectId, snapshotName);
          System.out.printf("Snapshot created: %s", snapshot.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html#com_google_cloud_compute_v1_Snapshot_getName__)());
    
        }
      }
    }

###  Node.js 

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const diskName = 'YOUR_DISK_NAME';
    // const snapshotName = 'YOUR_SNAPSHOT_NAME';
    // const zone = 'europe-central2-b';
    // const region = '';
    // const location = 'europe-central2';
    // let diskProjectId = 'YOUR_DISK_PROJECT_ID';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createSnapshot() {
      const snapshotsClient = new compute.[SnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      let disk;
    
      if (!zone && !region) {
        throw new Error(
          'You need to specify `zone` or `region` for this function to work.'
        );
      }
    
      if (zone && region) {
        throw new Error("You can't set both `zone` and `region` parameters");
      }
    
      if (!diskProjectId) {
        diskProjectId = projectId;
      }
    
      if (zone) {
        const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
        [disk] = await disksClient.get({
          project: diskProjectId,
          zone,
          disk: diskName,
        });
      } else {
        const regionDisksClient = new compute.[RegionDisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
        [disk] = await regionDisksClient.get({
          project: diskProjectId,
          region,
          disk: diskName,
        });
      }
    
      const snapshotResource = {
        name: snapshotName,
        sourceDisk: disk.selfLink,
      };
    
      if (location) {
        snapshotResource.storageLocations = [location];
      }
    
      const [response] = await snapshotsClient.insert({
        project: projectId,
        snapshotResource,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create snapshot operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Snapshot created.');
    }
    
    createSnapshot();

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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
    
    
    def create_snapshot(
        project_id: str,
        disk_name: str,
        snapshot_name: str,
        *,
        zone: str | None = None,
        region: str | None = None,
        location: str | None = None,
        disk_project_id: str | None = None,
    ) -> compute_v1.Snapshot:
        """
        Create a snapshot of a disk.
    
        You need to pass `zone` or `region` parameter relevant to the disk you want to
        snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
        regional disks.
    
        Args:
            project_id: project ID or project number of the Cloud project you want
                to use to store the snapshot.
            disk_name: name of the disk you want to snapshot.
            snapshot_name: name of the snapshot to be created.
            zone: name of the zone in which is the disk you want to snapshot (for zonal disks).
            region: name of the region in which is the disk you want to snapshot (for regional disks).
            location: The Cloud Storage multi-region or the Cloud Storage region where you
                want to store your snapshot.
                You can specify only one storage location. Available locations:
                https://cloud.google.com/storage/docs/locations#available-locations
            disk_project_id: project ID or project number of the Cloud project that
                hosts the disk you want to snapshot. If not provided, will look for
                the disk in the `project_id` project.
    
        Returns:
            The new snapshot instance.
        """
        if zone is None and region is None:
            raise RuntimeError(
                "You need to specify `zone` or `region` for this function to work."
            )
        if zone is not None and region is not None:
            raise RuntimeError("You can't set both `zone` and `region` parameters.")
    
        if disk_project_id is None:
            disk_project_id = project_id
    
        if zone is not None:
            disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
            disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=disk_project_id, zone=zone, disk=disk_name)
        else:
            regio_disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
            disk = regio_disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_get)(
                project=disk_project_id, region=region, disk=disk_name
            )
    
        snapshot = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Snapshot](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Snapshot.html)()
        snapshot.source_disk = disk.self_link
        snapshot.name = snapshot_name
        if location:
            snapshot.storage_locations = [location]
    
        snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
        operation = snapshot_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_insert)(project=project_id, snapshot_resource=snapshot)
    
        wait_for_extended_operation(operation, "snapshot creation")
    
        return snapshot_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_get)(project=project_id, snapshot=snapshot_name)
    
    

###  REST 

You can create a snapshot either by using the source disk's data or its replica recovery checkpoint.

###  From disk data 

You can create a snapshot from your disk's data using the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE"
        }
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, make a `POST` request to the `snapshots.insert` method and include the `storageLocations` property in your request:
        
        POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
          "storageLocations": [
              "STORAGE_LOCATION"
          ],
        }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, make a `POST` request to the `snapshots.insert` method and define the creation region:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/regions/SNAPSHOT_SCOPE_REGION/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
        }
        




Replace the following:

  * DESTINATION_PROJECT_ID: The ID of project in which you want to create the snapshot.
  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_PROJECT_ID: The ID of the source disk project.
  * SOURCE_REGION: The region of the source disk. 
  * SOURCE_DISK_NAME: The name of the Regional Persistent Disk or Hyperdisk Balanced High Availability volume from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `storageLocations` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `storageLocations` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `snapshots.insert` method instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

###  From checkpoint 

Alternatively, you can create your snapshot using the [replica recovery checkpoint](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-replica-recovery-checkpoint) of a degraded disk. Your snapshot gets created as long as your incomplete replica is available.

To create a snapshot using the replica recovery checkpoint, make a `POST` request to the [ `snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert). Exclude the `sourceDisk` parameter and instead include the `sourceDiskForRecoveryCheckpoint` parameter to specify that you want to create the snapshot using the checkpoint. 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
    
    {
      "name": "SNAPSHOT_NAME",
      "sourceDiskForRecoveryCheckpoint": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
      "storageLocations": "STORAGE_LOCATION",
      "snapshotType": "SNAPSHOT_TYPE"
    }
    

Replace the following: 

  * `DESTINATION_PROJECT_ID`: The ID of project in which you want to create the snapshot.
  * `SNAPSHOT_NAME`: A name for the snapshot.
  * `SOURCE_PROJECT_ID`: The project ID of the source disk whose checkpoint you want to use to create the snapshot.
  * `SOURCE_REGION`: The region of the source disk whose checkpoint you want to use to create the snapshot. 
  * `SOURCE_DISK_NAME`: The name of the source disk whose checkpoint you want to use to create the snapshot. 
  * `STORAGE_LOCATION`: Optional: The [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.  
Use the `storageLocations` parameter only if you want to override the predefined or customized default storage location configured in your snapshot settings.
  * `SNAPSHOT_TYPE`: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a **STANDARD** snapshot is created.



You can use replica recovery checkpoint to create a snapshot only on [degraded disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd_replication_state). If you try to create a snapshot from a replica recovery checkpoint when the device is fully replicated, you see the following error message:
    
    
    The device is fully replicated and should not create snapshots out of a recovery checkpoint. Please
    create regular snapshots instead.
    

## What's next

  * Learn how to [create scheduled snapshots for disks](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).
  * Learn how to [view, delete, and share disk snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots).
  * Learn how to [create a disk image from your snapshot](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
