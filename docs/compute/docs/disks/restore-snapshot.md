---
url: https://docs.cloud.google.com/compute/docs/disks/restore-snapshot/
title: Restore from a snapshot \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:01:02.900797+00:00
---

# Restore from a snapshot  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/restore-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Restore from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

If you use a standard or archive snapshot to back up a disk, then you can access the backed-up data by using the snapshot to create a new disk. The new disk can immediately achieve its maximum performance and doesn't require pre-warming. Creating a new disk from a snapshot is called _restoring a snapshot_.

You can use snapshots to backup and restore disk data in the following ways:

  * Create a disk from a snapshot of a disk.

  * Create an instance from a snapshot of a boot disk.

  * Create an instance and attach a new disk restored from a snapshot.




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




### Required roles

To get the permissions that you need to restore from a snapshot, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to restore from a snapshot. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore from a snapshot:

  * To create a disk from a globally scoped snapshot (default): 
    * `compute.disks.create` on the project
    * `compute.instances.attachDisk` on the instance
    * `compute.disks.use` on the disk to attach
    * `compute.snapshots.useReadOnly`, `compute.snapshots.create`, or `compute.disks.createSnapshot` on the project
  * To create a disk from a regionally scoped snapshot: 
    * `compute.disks.create` on the project
    * `compute.instances.attachDisk` on the instance
    * `compute.disks.use` on the disk to attach
    * `compute.snapshots.useReadOnly` on the project
  * To create an instance from a boot disk and non-boot disk snapshot, at a minimum, you need the following permissions: 
    * `compute.instances.create` on the project
    * `compute.snapshots.useReadOnly` on the snapshot
    * `compute.disks.create` on the project
    * `compute.disks.use` on the disk
    * `compute.instances.attachDisk` on the instance



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * The new disk must be at least the same size as the original source disk for the snapshot. If you create a disk that is larger than the original source disk for the snapshot, you must [resize the file system on that disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) to include the additional disk space. Depending on your operating system and file system type, you might need to use a different file system resizing tool. For more information, see your operating system documentation.

  * You can create a new zonal or regional disks from a given snapshot at most once every ten minutes. If you want to issue a burst of requests to snapshot your disks, you can issue at most 6 requests in 60 minutes. This limit does not apply when creating regional disks from a snapshot. For more information, see [Snapshot frequency limits](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#freq_limits).




## Create a disk from a snapshot and optionally attach it to an instance

If you backed up a boot or non-boot disk with a snapshot, you can create a new disk based on the snapshot.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to Snapshots](https://console.cloud.google.com/compute/snapshots)

  2. Find the name of the snapshot that you want to restore.

  3. Go to the **Disks** page.

[Go to the Disks page](https://console.cloud.google.com/compute/disks)

  4. Click **Create new disk**.

  5. Specify the following configuration parameters:

     * A name for the disk.
     * A type for the disk.
     * Optionally, you can override the default region and zone selection. You can select any region and zone, regardless of the storage location of the source snapshot.
  6. Under **Source type** , click **Snapshot**.

  7. Select the name of the snapshot to restore.

  8. Select the size of the new disk, in gigabytes. This number must be equal to or larger than the original source disk for the snapshot.

  9. Click **Create** to create the disk.




Optionally, you can then [attach a non-boot disk to an instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks).

###  gcloud 

  1. Use the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list) to find the name of the snapshot you want to restore:
         
         gcloud compute snapshots list
         

  2. Use the [`gcloud compute snapshots describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe) to find the size of the snapshot you want to restore:
         
         gcloud compute snapshots describe SNAPSHOT_NAME
         

Replace SNAPSHOT_NAME with the name of the snapshot being restored.

  3. Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create a new regional or zonal disk from your snapshot. You can include the `--type` flag to specify the type of disk to create.

     * To create a zonal disk from a globally scoped snapshot:
    
    gcloud compute disks create DISK_NAME \
        --zone=ZONE \
        --size=DISK_SIZE \
        --source-snapshot=SNAPSHOT_NAME \
        --type=DISK_TYPE
    

     * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a zonal disk from a regionally scoped snapshot:
    
    gcloud beta compute disks create DISK_NAME \
        --zone=ZONE \
        --source-snapshot=SNAPSHOT_NAME \
        --source-snapshot-region=SOURCE_REGION \
        --type=DISK_TYPE
    

     * To create a regional disk from a globally scoped snapshot:
    
    gcloud beta compute disks create DISK_NAME \
        --size=DISK_SIZE \
        --source-snapshot=SNAPSHOT_NAME \
        --type=DISK_TYPE \
        --region=REGION \
        --replica-zones=ZONE1,ZONE2
    

     * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regional disk from a regionally scoped snapshot:
    
    gcloud beta compute disks create DISK_NAME \
        --size=DISK_SIZE \
        --source-snapshot=SNAPSHOT_NAME \
        --source-snapshot-region=SOURCE_REGION \
        --type=DISK_TYPE \
        --region=REGION \
        --replica-zones=ZONE1,ZONE2
    

Replace the following:

     * DISK_NAME: the name of the new disk
     * DISK_SIZE: the size of the new disk, in gibibytes (GiB). This number must be equal to or larger than the original source disk for the snapshot.
     * SNAPSHOT_NAME: the name of the snapshot being restored
     * DISK_TYPE: the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the disk, for example, `pd-ssd`, `hyperdisk-throughput` or `hyperdisk-balanced-high-availability`
     * REGION: the region for the regional disk to reside in, for example: `europe-west1`
     * SOURCE_REGION: the region that the source snapshot is scoped to
     * ZONE: the zone where the new disk will reside
     * ZONE1,ZONE2: the zones within the region where the two disk replicas are located, for example: `europe-west1-b` and `europe-west1-c`
  4. Optional: Attach the new disk to an existing instance by using the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk):
         
         gcloud compute instances attach-disk INSTANCE_NAME \
             --disk DISK_NAME
         

Replace the following:

     * INSTANCE_NAME: the name of the instance
     * DISK_NAME: the name of the disk made from your snapshot



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
    
    // createDiskFromSnapshot creates a new disk in a project in given zone.
    func createDiskFromSnapshot(
    	w io.Writer,
    	projectID, zone, diskName, diskType, snapshotLink string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "zones/us-west3-b/diskTypes/pd-ssd"
    	// snapshotLink := "projects/your_project_id/global/snapshots/snapshot_name"
    	// diskSizeGb := 120
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.InsertDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		DiskResource: &computepb.Disk{
    			Name:           proto.String(diskName),
    			Zone:           proto.String(zone),
    			Type:           proto.String(diskType),
    			SourceSnapshot: proto.String(snapshotLink),
    			SizeGb:         proto.Int64(diskSizeGb),
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

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDiskFromSnapshot {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the zone in which you want to create the disk.
        String zone = "europe-central2-b";
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        // For example: "zones/us-west3-b/diskTypes/pd-ssd"
        String diskType = String.format("zones/%s/diskTypes/pd-ssd", zone);
    
        // Size of the new disk in gigabytes.
        long diskSizeGb = 10;
    
        // The full path and name of the snapshot that you want to use as the source for the new disk.
        // This value uses the following format:
        // "projects/{projectName}/global/snapshots/{snapshotName}"
        String snapshotLink = String.format("projects/%s/global/snapshots/%s", projectId,
            "SNAPSHOT_NAME");
    
        createDiskFromSnapshot(projectId, zone, diskName, diskType, diskSizeGb, snapshotLink);
      }
    
      // Creates a new disk in a project in given zone, using a snapshot.
      public static void createDiskFromSnapshot(String projectId, String zone, String diskName,
          String diskType, long diskSizeGb, String snapshotLink)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          // Set the disk properties and the source snapshot.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setName(diskName)
              .setZone(zone)
              .setSizeGb(diskSizeGb)
              .setType(diskType)
              .setSourceSnapshot(snapshotLink)
              .build();
    
          // Create the insert disk request.
          [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html) insertDiskRequest = [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setDiskResource(disk)
              .build();
    
          // Wait for the create disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.insertAsync(insertDiskRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!" + response);
            return;
          }
          System.out.println("Disk created. Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
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
    // const zone = 'europe-central2-b';
    // const diskName = 'YOUR_DISK_NAME';
    // const diskType = 'zones/us-west3-b/diskTypes/pd-ssd';
    // const diskSizeGb = 10;
    // const snapshotLink = 'projects/project_name/global/snapshots/snapshot_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createDiskFromSnapshot() {
      const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await disksClient.insert({
        project: projectId,
        zone,
        diskResource: {
          sizeGb: diskSizeGb,
          name: diskName,
          zone,
          type: diskType,
          sourceSnapshot: snapshotLink,
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Disk created.');
    }
    
    createDiskFromSnapshot();

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
    
    
    def create_disk_from_snapshot(
        project_id: str,
        zone: str,
        disk_name: str,
        disk_type: str,
        disk_size_gb: int,
        snapshot_link: str,
    ) -> compute_v1.Disk:
        """
        Creates a new disk in a project in given zone.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone in which you want to create the disk.
            disk_name: name of the disk you want to create.
            disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            snapshot_link: a link to the snapshot you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/global/snapshots/{snapshot_name}"
    
        Returns:
            An unattached Disk instance.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.zone = zone
        disk.size_gb = disk_size_gb
        disk.source_snapshot = snapshot_link
        disk.type_ = disk_type
        disk.name = disk_name
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(project=project_id, zone=zone, disk_resource=disk)
    
        wait_for_extended_operation(operation, "disk creation")
    
        return disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=project_id, zone=zone, disk=disk_name)
    
    

###  REST 

  1. Construct a `GET` request to [`snapshots.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/list) to display the list of snapshots in your project.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots
         

Replace PROJECT_ID with your project ID.

  2. Construct a `POST` request to create a zonal disk or a [regional](https://docs.cloud.google.com/compute/docs/disks#repds) disk using the respective `disks.insert` method:

     * For zonal disks: [`disks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert)
     * For regional disks: [`regionDisks.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/insert)

Include the `name`, `sizeGb`, and `type` properties. To restore a disk using a snapshot, you must include the `sourceSnapshot` property.

     * To create a zonal disk from a globally scoped snapshot:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    {
      "name": "DISK_NAME",
      "sourceSnapshot": "SNAPSHOT_NAME",
      "sizeGb": "DISK_SIZE",
      "type": "zones/ZONE/diskTypes/DISK_TYPE"
    }
    

     * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a zonal disk from a regionally scoped snapshot:
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/disks
    {
      "name": "DISK_NAME",
      "sourceSnapshot": "projects/PROJECT_ID/regions/SOURCE_REGION/snapshots/SNAPSHOT_NAME",
      "sizeGb": "DISK_SIZE",
      "type": "projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE",
      "zone": "projects/PROJECT_ID/zones/ZONE"
    }
    

     * To create a regional disk from a globally scoped snapshot:
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/disks
    {
      "name": "DISK_NAME",
      "sourceSnapshot": "SNAPSHOT_NAME",
      "region": "projects/PROJECT_ID/regions/REGION",
      "replicaZones": [
         "projects/PROJECT_ID/zones/ZONE1",
         "projects/PROJECT_ID/zones/ZONE2"
      ],
      "sizeGb": "DISK_SIZE",
      "type": "zones/ZONE/diskTypes/DISK_TYPE"
    }
    

     * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regional disk from a regionally scoped snapshot:
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/disks
    {
      "name": "DISK_NAME",
      "sourceSnapshot": "projects/PROJECT_ID/regions/SOURCE_REGION/snapshots/SNAPSHOT_NAME",
      "replicaZones": [
         "projects/PROJECT_ID/zones/ZONE1",
         "projects/PROJECT_ID/zones/ZONE2"
      ],
      "sizeGb": "DISK_SIZE",
      "type": "projects/PROJECT_ID/regions/REGION/diskTypes/DISK_TYPE"
    }
    

Replace the following:

     * PROJECT_ID: your project ID
     * ZONE: the zone where your instance and new disk are located
     * DISK_NAME: the name of the new disk
     * SNAPSHOT_NAME: the source snapshot for the disk that you're restoring
     * REGION: the region for the regional disk to reside in, for example: `europe-west1`
     * SOURCE_REGION: the region that the source snapshot is scoped to
     * ZONE1, ZONE2: the zones where replicas of the new disk should be located
     * DISK_SIZE: the size of the new disk, in gibibytes (GiB). This number must be equal to or larger than the original source disk for the snapshot.
     * DISK_TYPE: full or partial URL for the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the disk, for example, `PROJECT_ID/zones/ZONE/diskTypes/pd-ssd`, `PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced` or `PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced-high-availability`
  3. Optional. Attach the new disk to an existing instance.

Construct a `POST` request to the [`instances.attachDisk` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/attachDisk), and include the URL to the disk that you just created from your snapshot.

For zonal disks:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/attachDisk
         {
           "source": "/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME"
         }
         

For regional disks:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/attachDisk
         {
           "source": "/compute/v1/projects/PROJECT_ID/regions/REGION/disks/DISK_NAME"
         }
         

Replace the following:

     * PROJECT_ID: your project ID
     * ZONE: the zone where your instance and new disk are located
     * REGION: the region where the regional disk is located. This must be the same region that the compute instance is located in.
     * INSTANCE_NAME: the name of the instance where you're adding the new disk
     * DISK_NAME: the name of the new disk



After you create and attach a new disk to an instance, you must [mount the disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#format_linux) so that the operating system can use the available storage space.

**Important:** If you create a compute instance from a disk snapshot based on a [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) image, the original [integrity policy baseline](https://docs.cloud.google.com/compute/docs/instances/integrity-monitoring#updating-baseline) is lost and the first set of boot sequence measurements on the new instance is used as the new baseline. Because this new set of measurements is not verified, validate the instance's boot integrity after restoring from a snapshot. You can do this by manually examining the boot log and verifying that the proper keys are loaded into the SecureBoot database, and that the expected kernel version is running. Also, secrets saved in the vTPM on the originating instance are not accessible on any instances restored from a snapshot of that instance.

### Create an instance from existing disks

You can create boot disks and data disks from snapshots and then attach these disks to a new compute instance.

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
    
    // createWithExistingDisks create a new VM instance using selected disks.
    // The first disk in diskNames will be used as boot disk.
    func createWithExistingDisks(
    	w io.Writer,
    	projectID, zone, instanceName string,
    	diskNames []string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// diskNames := []string{"boot_disk", "disk1", "disk2"}
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	disks := [](*computepb.Disk){}
    
    	for _, diskName := range diskNames {
    		reqDisk := &computepb.GetDiskRequest{
    			Project: projectID,
    			Zone:    zone,
    			Disk:    diskName,
    		}
    
    		disk, err := disksClient.Get(ctx, reqDisk)
    		if err != nil {
    			return fmt.Errorf("unable to get disk: %w", err)
    		}
    
    		disks = append(disks, disk)
    	}
    
    	attachedDisks := [](*computepb.AttachedDisk){}
    
    	for _, disk := range disks {
    		attachedDisk := &computepb.AttachedDisk{
    			Source: proto.String(disk.GetSelfLink()),
    		}
    		attachedDisks = append(attachedDisks, attachedDisk)
    	}
    
    	attachedDisks[0].Boot = proto.Bool(true)
    
    	instanceResource := &computepb.Instance{
    		Name:        proto.String(instanceName),
    		Disks:       attachedDisks,
    		MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
    		NetworkInterfaces: []*computepb.NetworkInterface{
    			{
    				Name: proto.String("global/networks/default"),
    			},
    		},
    	}
    
    	req := &computepb.InsertInstanceRequest{
    		Project:          projectID,
    		Zone:             zone,
    		InstanceResource: instanceResource,
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

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstanceWithExistingDisks {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the zone to create the instance in. For example: "us-west3-b"
        String zone = "europe-central2-b";
    
        // Name of the new virtual machine (VM) instance.
        String instanceName = "YOUR_INSTANCE_NAME";
    
        // Array of disk names to be attached to the new virtual machine.
        // First disk in this list will be used as the boot disk.
        List<String> diskNames = List.of("your-boot-disk", "another-disk1", "another-disk2");
    
        createInstanceWithExistingDisks(projectId, zone, instanceName, diskNames);
      }
    
      // Create a new VM instance using the selected disks.
      // The first disk in diskNames will be used as the boot disk.
      public static void createInstanceWithExistingDisks(String projectId, String zone,
          String instanceName, List<String> diskNames)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create();
            [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          if (diskNames.size() == 0) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("At least one disk should be provided");
          }
    
          // Create the list of attached disks to be used in instance creation.
          List<AttachedDisk> attachedDisks = new ArrayList<>();
          for (int i = 0; i < diskNames.size(); i++) {
            String diskName = diskNames.get(i);
            [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = disksClient.get(projectId, zone, diskName);
            [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attDisk = null;
    
            if (i == 0) {
              // Make the first disk in the list as the boot disk.
              attDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                  .setSource(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                  .setBoot(true)
                  .build();
            } else {
              attDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                  .setSource(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                  .build();
            }
            attachedDisks.add(attDisk);
          }
    
          // Create the instance.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
              .setName(instanceName)
              // Add the attached disks to the instance.
              .addAllDisks(attachedDisks)
              .setMachineType(String.format("zones/%s/machineTypes/n1-standard-1", zone))
              .addNetworkInterfaces(
                  [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder().setName("global/networks/default").build())
              .build();
    
          // Create the insert instance request.
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(instance)
              .build();
    
          // Wait for the create operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.insertAsync(insertInstanceRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance creation failed!" + response);
            return;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
    
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
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const diskNames = ['boot_disk', 'disk1', 'disk2'];
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createWithExistingDisks() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      if (diskNames.length < 1) {
        throw new Error('At least one disk should be provided');
      }
    
      const disks = [];
      for (const diskName of diskNames) {
        const [disk] = await disksClient.get({
          project: projectId,
          zone,
          disk: diskName,
        });
        disks.push(disk);
      }
    
      const attachedDisks = [];
    
      for (const disk of disks) {
        attachedDisks.push({
          source: disk.selfLink,
        });
      }
    
      attachedDisks[0].boot = true;
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
          disks: attachedDisks,
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
    
    createWithExistingDisks();

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def get_disk(project_id: str, zone: str, disk_name: str) -> compute_v1.Disk:
        """
        Gets a disk from a project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone where the disk exists.
            disk_name: name of the disk you want to retrieve.
        """
        disk_client = compute_v1.DisksClient()
        return disk_client.get(project=project_id, zone=zone, disk=disk_name)
    
    
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
    
    
    def create_with_existing_disks(
        project_id: str, zone: str, instance_name: str, disk_names: list[str]
    ) -> compute_v1.Instance:
        """
        Create a new VM instance using selected disks. The first disk in disk_names will
        be used as boot disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            disk_names: list of disk names to be attached to the new virtual machine.
                First disk in this list will be used as the boot device.
    
        Returns:
            Instance object.
        """
        assert len(disk_names) >= 1
        disks = [get_disk(project_id, zone, disk_name) for disk_name in disk_names]
        attached_disks = []
        for disk in disks:
            adisk = compute_v1.AttachedDisk()
            adisk.source = disk.self_link
            attached_disks.append(adisk)
        attached_disks[0].boot = True
        instance = create_instance(project_id, zone, instance_name, attached_disks)
        return instance
    
    

## Create an instance from a boot disk snapshot

If you created a snapshot of the boot disk of a compute instance,you can use that snapshot to create a new instance.

To quickly create more than one instance with the same boot disk, [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), then [create instances from that image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image) instead of using a snapshot.

To create a compute instance with a regional boot disk that was created from a snapshot, use the Google Cloud CLI or REST.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Optional: In the **Zone** field, select a zone for this instance.

The default selection is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability. 

     3. Select the machine family for your instance. The Google Cloud console then displays the machine series that are available for your selected machine family. The following machine family options are available:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**
     4. In the **Series** column, select the machine series for your instance.

If you selected **GPUs** as the machine family in the previous step, then select the **GPU type** that you want. The machine series is then automatically selected for the selected GPU type.

     5. In the **Machine type** section, select the machine type for your instance.

  3. In the navigation menu, click **OS and storage**. In the **Operating system and storage** pane that appears, configure your boot disk by doing the following: 

     1. Click **Change**. The **Boot disk** pane appears and displays the **Public images** tab.
     2. Click **Snapshots**. The **Snapshot** tab appears.
     3. In the **Snapshot** list, select the snapshot to use.
     4. In the **Boot disk type** list, select the type of the boot disk.
     5. In the **Size (GB)** field, specify the size of the boot disk.
     6. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section.
     7. To confirm your boot disk options and return to the **Operating system and storage** pane, click **Select**.
  4. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. Go to the **Firewall** section.
     2. To permit HTTP or HTTPS traffic to the instance, select **Allow HTTP traffic** or **Allow HTTPS traffic**.

The Google Cloud console adds a network tag to your instance and creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS). The network tag associates the firewall rule with the instance. For more information, see [Firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls) in the Virtual Private Cloud documentation.

  5. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the instance, click **Create**.




###  gcloud 

### Zonal boot disk

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and include the `--source-snapshot` flag.
    
    
       gcloud compute instances create INSTANCE_NAME    
    
           --source-snapshot=BOOT_SNAPSHOT_NAME    
    
           --boot-disk-size=BOOT_DISK_SIZE    
    
           --boot-disk-type=BOOT_DISK_TYPE    
    
           --boot-disk-device-name=BOOT_DISK_NAME
       

Replace the following:

  * `INSTANCE_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance
  * `BOOT_SNAPSHOT_NAME`: name of the boot disk snapshot that you want to restore to the boot disk of the new instance
  * `BOOT_DISK_SIZE`: Optional: size, in GiB, of the new boot disk

The size must be equal to or larger than the size of the source disk from which the snapshot was made.

  * `BOOT_DISK_TYPE`: Optional: [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk, for example `PROJECT_ID/zones/ZONE/diskTypes/pd-ssd` or `PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced`

  * `BOOT_DISK_NAME`: name of the new boot disk for this instance 




### Regional boot disk

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and include the `--create-disk` flag with the `source-snapshot`, `replica-zones`, and `boot` properties.
    
    
      gcloud compute instances create INSTANCE_NAME   
    
          --zone=ZONE   
    
          --create-disk=^:^name=DISK_NAME:source-snapshot=BOOT_SNAPSHOT_NAME:boot=true:type=BOOT_DISK_TYPE:replica-zones=ZONE,REMOTE_ZONE
      

The characters `^:^` specify that a colon `:` is used as the separator between each of the disk properties. This is required so that you can use a comma `,` when specifying the zones for `replica-zones`.

Replace the following:

  * `INSTANCE_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance
  * `ZONE`: To zone to create the instance in
  * `DISK_NAME`: Optional: a name for the disk
  * `BOOT_SNAPSHOT_NAME`: name of the boot disk snapshot that you want to restore to the boot disk of the new instance.
  * `BOOT_DISK_TYPE`: Optional: [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk, for example `pd-ssd` or `hyperdisk-balanced-high-availability`
  * `REMOTE_ZONE`: The region that the boot disk is replicated to. The `replica-zones` property requires two zones separated by comma, and one of the zones must the same as the zone for the instance. 



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
    
    // createInstanceFromSnapshot creates a new VM instance with boot disk created from a snapshot.
    func createInstanceFromSnapshot(w io.Writer, projectID, zone, instanceName, snapshotLink string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// snapshotLink := "projects/project_name/global/snapshots/snapshot_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    			Disks: []*computepb.AttachedDisk{
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:     proto.Int64(11),
    						SourceSnapshot: proto.String(snapshotLink),
    						DiskType:       proto.String(fmt.Sprintf("zones/%s/diskTypes/pd-standard", zone)),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
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

### Java

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
       * @param diskType the type of disk you want to create. This value uses the following format:
       * "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)". For example:
       * "zones/us-west3-b/diskTypes/pd-ssd"
       * @param diskSizeGb size of the new disk in gigabytes
       * @param boot boolean flag indicating whether this disk should be used as a boot disk of an
       * instance
       * @param diskSnapshot disk snapshot to use when creating this disk. You must have read access to
       * this disk. This value uses the following format:
       * "projects/{project_name}/global/snapshots/{snapshot_name}"
       * @return AttachedDisk object configured to be created using the specified snapshot.
       */
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) diskFromSnapshot(String diskType, int diskSizeGb, boolean boot,
          String diskSnapshot) {
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk =
            [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                .setBoot(boot)
                // Remember to set auto_delete to True if you want the disk to be deleted when
                // you delete your VM instance.
                .setAutoDelete(true)
                .setType(Type.PERSISTENT.toString())
                .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                    [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                        .setSourceSnapshot(diskSnapshot)
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
       * Create a new VM instance with boot disk created from a snapshot.
       *
       * @param project project ID or project number of the Cloud project you want to use.
       * @param zone name of the zone to create the instance in. For example: "us-west3-b"
       * @param instanceName name of the new virtual machine (VM) instance.
       * @param snapshotName link to the snapshot you want to use as the source of your boot disk in the
       * form of: "projects/{project_name}/global/snapshots/{snapshot_name}"
       * @return Instance object.
       */
      public static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createFromSnapshot(String project, String zone, String instanceName,
          String snapshotName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        String diskType = String.format("zones/%s/diskTypes/pd-standard", zone);
        Vector<AttachedDisk> disks = new Vector<>();
        disks.add(diskFromSnapshot(diskType, 11, true, snapshotName));
        return createWithDisks(project, zone, instanceName, disks, "n1-standard-1",
            "global/networks/default", null);
      }

###  Node.js 

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const snapshotLink = 'projects/YOUR_PROJECT/global/snapshots/YOUR_SNAPSHOT_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Creates a new VM instance with boot disk created from a snapshot.
    async function createInstanceFromSnapshot() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
          disks: [
            {
              initializeParams: {
                diskSizeGb: '11',
                sourceSnapshot: snapshotLink,
                diskType: `zones/${zone}/diskTypes/pd-standard`,
              },
              autoDelete: true,
              boot: true,
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
    
    createInstanceFromSnapshot();

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def disk_from_snapshot(
        disk_type: str,
        disk_size_gb: int,
        boot: bool,
        source_snapshot: str,
        auto_delete: bool = True,
    ) -> compute_v1.AttachedDisk():
        """
        Create an AttachedDisk object to be used in VM instance creation. Uses a disk snapshot as the
        source for the new disk.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            source_snapshot: disk snapshot to use when creating this disk. You must have read access to this disk.
                This value uses the following format: "projects/{project_name}/global/snapshots/{snapshot_name}"
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created using the specified snapshot.
        """
        disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_snapshot = source_snapshot
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
    
    
    def create_from_snapshot(
        project_id: str, zone: str, instance_name: str, snapshot_link: str
    ):
        """
        Create a new VM instance with boot disk created from a snapshot. The
        new boot disk will have 20 gigabytes.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            snapshot_link: link to the snapshot you want to use as the source of your
                boot disk in the form of: "projects/{project_name}/global/snapshots/{snapshot_name}"
    
        Returns:
            Instance object.
        """
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_snapshot(disk_type, 20, True, snapshot_link)]
        instance = create_instance(project_id, zone, instance_name, disks)
        return instance
    
    

###  REST 

When you use the API to create an instance from a snapshot, the following restrictions apply:

  * Only one disk can be used as the boot disk.
  * You must attach the boot disk as the first disk for that instance.
  * If you specify the `source` property, you cannot also specify the `initializeParams` property. Providing a `source` indicates that the boot disk exists already, but the `initializeParams` property indicates that Compute Engine should create a new boot disk.



### Zonal boot disk

To create an instance from a boot disk snapshot, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and specify the `sourceSnapshot` field under the `disks` property. You can optionally specify the `diskSizeGb` and `diskType` properties for the new boot disk. 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "name": "INSTANCE_NAME",
      "machineType": "machineTypes/MACHINE_TYPE",
      "disks": [{
         "boot": true,
         "initializeParams": {
           "sourceSnapshot": "global/snapshots/BOOT_SNAPSHOT_NAME",
           "diskSizeGb": "BOOT_DISK_SIZE",
           "diskType": "BOOT_DISK_TYPE"
          }
       }],
      "networkInterfaces": [
        {
           "nicType": "GVNIC"
        }
      ]
    }
    

Replace the following: 

  * `PROJECT_ID`: your project ID
  * `ZONE`: zone where you want to create the new instance
  * `INSTANCE_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the instance that you want to restore a snapshot to
  * `MACHINE_TYPE`: [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of the instance
  * `BOOT_SNAPSHOT_NAME`: name of the snapshot that you want to use to create the boot disk of the new instance
  * `BOOT_DISK_SIZE`: Optional: size, in gibibytes (GiB), for the new boot disk

The size must be equal to or larger than the size of the source disk from which the snapshot was made.

  * `BOOT_DISK_TYPE`: Optional: [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk, for example `PROJECT_ID/zones/ZONE/diskTypes/pd-ssd` or `PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced`




### Regional boot disk

To create a compute instance with a regional boot disk using a boot disk snapshot as the source, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and specify the `sourceSnapshot` and `replicaZones` fields in the `disks` property. 
    
    
       POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
       {
         "name": "INSTANCE_NAME",
         "disks": [
           {
             "boot": true,
             "initializeParams": {
                "sourceSnapshot": "global/snapshots/BOOT_SNAPSHOT_NAME",
                "replicaZones": [
                    "projects/PROJECT_ID/zones/ZONE",
                    "projects/PROJECT_ID/zones/REMOTE_ZONE"
                  ],
                "diskType": "BOOT_DISK_TYPE"
             }
           }
         ],
         "networkInterfaces": [
           {
             "nicType": "GVNIC"
           }
         ]
       }
       

Replace the following: 

  * `PROJECT_ID`: your project ID
  * `ZONE`: the name of the zone where you want to create the instance
  * `INSTANCE_NAME`: a name for the instance
  * `BOOT_SNAPSHOT_NAME`: the name of the boot disk snapshot
  * `REMOTE_ZONE`: the remote zone for the regional disk
  * `BOOT_DISK_TYPE`: Optional: [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk, for example `PROJECT_ID/zones/ZONE/diskTypes/pd-ssd` or `PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced-high-availability`




## Create a compute instance from a non-boot disk snapshot

If you backed up a non-boot disk with a snapshot, you can create an instance with an additional non-boot disk based on the snapshot.

###  Console 

When restoring non-boot snapshots to a new instance from the console, first create a disk from each snapshot. Then, attach the new disks when you create the instance.

  1. Restore each non-boot snapshot to a new disk.

     1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

     2. Click **Create disk**.

     3. Specify a **Name** for your disk. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

     4. Select the **Region** and **Zone** for this disk. The disk and instance must be in the same zone for zonal disks, or region for regional disks.

     5. Select a disk **Type**.

     6. Under **Source type** , select **Snapshot**.

     7. Under the new **Source snapshot** field, select a non-boot snapshot that you want to restore to the new disk.

     8. To create the disk, click **Create**.

Repeat these steps to create a disk from each snapshot that you want to restore.

  2. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Select your project and click **Continue**.

  4. Click **Create instance**.

  5. Specify a **Name** for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  6. Select the **Region** and **Zone** for this instance. The disk and instance must be in the same zone for zonal disks, or region for regional disks.

  7. Select a **Machine type** for your instance.

  8. If you want to allow incoming external traffic, change the **Firewall** rules for the instance.

  9. To attach disks to the instance, expand the **Advanced options** section, and then do the following:

     1. Expand the **Disks** section.
     2. Click **Attach existing disk**.
     3. In the **Disk** list, select a disk to attach to this instance.
     4. In the **Attachment Setting** section, select disk's attachment **Mode** and the **Deletion rule**. For more information about adding new disks, see [Add a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) or [Add Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).
     5. Click **Save**.

Repeat these steps for each disk that you want to attach.

  10. To create and start the instance, click **Create**.




###  gcloud 

Create an instance by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). For each non-boot snapshot that you want to restore, include the `--create-disk` flag, and specify a `source-snapshot`.

For example, to restore two snapshots of non-boot disks to a new instance, use the following command:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --create-disk source-snapshot=SNAPSHOT_1_NAME,name=DISK_1_NAME,size=DISK_1_SIZE,type=DISK_1_TYPE \
        --create-disk source-snapshot=SNAPSHOT_2_NAME,name=DISK_2_NAME,size=DISK_2_SIZE,type=DISK_2_TYPE

Replace the following:

  * `INSTANCE_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance
  * `SNAPSHOT_1_NAME` and `SNAPSHOT_2_NAME`: names of the non-boot disk snapshots that you want to restore
  * `DISK_1_NAME` and `DISK_2_NAME`: names of the new non-boot disks to create for this instance
  * `DISK_1_SIZE` and `DISK_2_SIZE`: Optional: sizes, in gibibytes (GiB), of each new non-boot disk

The sizes must be equal to or larger than the sizes of the source disks from which the snapshot was made.

  * `DISK_1_TYPE` and `DISK_2_TYPE`: Optional: the disk [types](https://docs.cloud.google.com/compute/docs/disks#disk-types) to create, for example `pd-ssd` or `hyperdisk-balanced`




###  REST 

When using REST to restore a non-boot snapshot to a new instance, the following restrictions apply:

  * Only one disk can be the boot disk.
  * You must attach the boot disk as the first disk for that instance.
  * If you specify the `source` property, you can't also specify the `initializeParams` property. Providing a `source` indicates that the boot disk exists already, but the `initializeParams` property indicates that Compute Engine should create a new boot disk.



Create a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and specify the `sourceSnapshot` field under the `initializeParams` property. You can add multiple non-boot disks by repeating the `initializeParams` property for every non-boot disk that you want to create. You can optionally specify the `diskSizeGb` and `diskType` properties for any of the disks that you create.

For example, to restore two non-boot disk snapshots to a new instance, make the following request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "name": "INSTANCE_NAME",
      "machineType": "machineTypes/MACHINE_TYPE",
      "networkInterfaces": [
        {
          "nicType": "GVNIC"
        }
      ],
      "disks": [
        {
          "autoDelete": "true",
          "boot": "true",
          "diskSizeGb": "BOOT_DISK_SIZE",
          "diskType": "BOOT_DISK_TYPE",
          "initializeParams": {
             "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
          }
        },
        {
          "deviceName": "DEVICE_1_NAME",
          "initializeParams": {
             "sourceSnapshot": "global/snapshots/SNAPSHOT_1_NAME",
             "diskSizeGb": "DISK_1_SIZE",
             "diskType": "DISK_1_TYPE"
          }
        },
        {
          "deviceName": "DEVICE_2_NAME",
          "initializeParams": {
             "sourceSnapshot": "global/snapshots/SNAPSHOT_2_NAME",
             "diskSizeGb": "DISK_2_SIZE",
             "diskType": "DISK_2_TYPE"
          }
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: zone where you want to create the instance
  * `INSTANCE_NAME`: a [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance
  * `MACHINE_TYPE`: [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of the instance
  * `DISK_SIZE`: Optional: size, in gibibytes (GiB), of the corresponding disk

When provided, this property must be equal to or larger than the size of the source disk from which the snapshot was made.

  * `DISK_TYPE`: Optional: full or partial URL for the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the corresponding disk, for example, `PROJECT_ID/zones/ZONE/diskTypes/pd-ssd` or `PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced`

  * `IMAGE_PROJECT`: the project containing the image. For example, `debian-cloud`

  * `IMAGE_FAMILY`: an image family. This creates the instance from the most recent, non-deprecated OS image in that family. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-13"`, the Compute Engine creates an instance using the latest version of the OS image in the Debian 13 image family.

  * `DEVICE_NAME`: Optional: the [device name](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks) displayed in the guest OS of the instance

  * `SNAPSHOT_NAME`: the names of corresponding non-boot disk snapshots that you want to restore to new disks on the instance




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
