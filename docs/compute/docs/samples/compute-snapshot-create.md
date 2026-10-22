---
url: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-create/
title: Create a disk snapshot \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:04.184624+00:00
---

# Create a disk snapshot  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a disk snapshot Stay organized with collections  Save and categorize content based on your preferences. 

Create a zonal or a regional snapshot of a disk in the specified Cloud Storage location.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)
  * [Move a VM instance between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    resource "google_compute_snapshot" "snapdisk" {
      name        = "snapshot-name"
      source_disk = google_compute_disk.default.name
      zone        = "us-central1-a"
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
