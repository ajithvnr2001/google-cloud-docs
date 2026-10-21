---
url: https://docs.cloud.google.com/compute/docs/samples/compute-disk-create-from-snapshot/
title: Create a disk from a snapshot \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:16.036511+00:00
---

# Create a disk from a snapshot  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-disk-create-from-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a disk from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

Create a zonal disk from a snapshot.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Move a VM instance between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones)
  * [Restore from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot)



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
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
