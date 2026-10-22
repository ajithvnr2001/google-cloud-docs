---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication/
title: Manage Asynchronous Replication \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:52.322855+00:00
---

# Manage Asynchronous Replication  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage Asynchronous Replication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to start and stop Asynchronous Replication.

Asynchronous Replication is useful for low-RPO, low-RTO disaster recovery. To learn more about asynchronous replication, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).

## Limitations

  * A primary disk can only replicate to one secondary disk at a time.
  * After replication stops, you can't resume replication to the same disk. You must create a new secondary disk and restart replication.
  * Secondary disks can't be attached, deleted, or snapshotted while they are in the process of replication.
  * If you use a regional disk as a secondary disk and a zonal outage occurs in one of the secondary disk's zones, replication from the primary disk to the secondary disk fails.



## Before you begin

  * If you need to align replication across multiple disks, [create a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group).
  * [Create a primary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_primary_disk).
  * [Create a secondary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk).
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




## Required roles and permissions

To get the permissions that you need to start or stop replication, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to start or stop replication. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to start or stop replication:

  * To start replication: `compute.disks.startAsyncReplication`
  * To stop replication for a single disk: `compute.disks.stopAsyncReplication`
  * To stop replication for all the disks in a consistency group: `compute.disks.stopGroupAsyncReplication`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Start replication

Start replication using the Google Cloud console, Google Cloud CLI, REST, or Terraform.

###  Console 

**Note:** If you created a secondary disk using the Google Cloud console, replication started when you created the disk.

  1. In the Google Cloud console, go to the **Asynchronous replication** page.

[Go to Asynchronous replication](https://console.cloud.google.com/compute/asynchronousReplication)

  2. Click the name of the secondary disk that you want to start replication to.

  3. Click **Start replication**. The **Start replication** window opens.

  4. Click **Start replication**.




###  gcloud 

Start replication using the [`gcloud compute disks start-async-replication` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/start-async-replication):
    
    
    gcloud compute disks start-async-replication PRIMARY_DISK_NAME \
        --PRIMARY_LOCATION_FLAG=PRIMARY_LOCATION \
        --secondary-disk=SECONDARY_DISK_NAME \
        --SECONDARY_LOCATION_FLAG=SECONDARY_LOCATION \
        --secondary-disk-project=SECONDARY_PROJECT
    

Replace the following:

  * `PRIMARY_DISK_NAME`: the name of the primary disk.
  * `PRIMARY_LOCATION_FLAG`: the location flag for the primary disk. For regional disks, use `--region`. For zonal disks, use `--zone`.
  * `PRIMARY_LOCATION`: The primary disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.
  * `SECONDARY_DISK_NAME`: the name of the secondary disk.
  * `SECONDARY_LOCATION_FLAG`: the location flag for the secondary disk. For regional disks, use `--secondary-disk-region`. For zonal disks, use `--secondary-disk-zone`.
  * `SECONDARY_LOCATION`: the secondary disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.
  * `SECONDARY_PROJECT`: the project that contains the secondary disk.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // startReplication starts disk replication in a project for a given zone.
    func startReplication(
    	w io.Writer,
    	projectID, zone, diskName, primaryDiskName, primaryZone string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-west4-b"
    	// diskName := "your_disk_name"
    	// primaryDiskName := "your_disk_name2"
    	// primaryZone := "europe-west2-b"
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	secondaryFullDiskName := fmt.Sprintf("projects/%s/zones/%s/disks/%s", projectID, zone, diskName)
    
    	req := &computepb.StartAsyncReplicationDiskRequest{
    		Project: projectID,
    		Zone:    primaryZone,
    		Disk:    primaryDiskName,
    		DisksStartAsyncReplicationRequestResource: &computepb.DisksStartAsyncReplicationRequest{
    			AsyncSecondaryDisk: &secondaryFullDiskName,
    		},
    	}
    
    	op, err := disksClient.StartAsyncReplication(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Replication started\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[DisksStartAsyncReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksStartAsyncReplicationRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[StartAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationDiskRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class StartZonalDiskReplication {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The project that contains the primary disk.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the primary disk.
        String primaryDiskName = "PRIMARY_DISK_NAME";
        // Name of the secondary disk.
        String secondaryDiskName = "SECONDARY_DISK_NAME";
        // Name of the zone in which your primary disk is located.
        // Learn more about zones and regions:
        // https://cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs
        String primaryDiskLocation = "us-central1-a";
        // Name of the zone in which your secondary disk is located.
        String secondaryDiskLocation = "us-east1-b";
    
        startZonalDiskAsyncReplication(projectId, primaryDiskName, primaryDiskLocation,
                secondaryDiskName, secondaryDiskLocation);
      }
    
      // Starts asynchronous replication for the specified zonal disk.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) startZonalDiskAsyncReplication(String projectId, String primaryDiskName,
          String primaryDiskLocation, String secondaryDiskName, String secondaryDiskLocation)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        String secondaryDiskPath = String.format("projects/%s/zones/%s/disks/%s",
                projectId, secondaryDiskLocation, secondaryDiskName);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          [DisksStartAsyncReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksStartAsyncReplicationRequest.html) diskRequest =
                  [DisksStartAsyncReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksStartAsyncReplicationRequest.html).newBuilder()
                          .setAsyncSecondaryDisk(secondaryDiskPath)
                          .build();
    
          [StartAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationDiskRequest.html) request =
                  [StartAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationDiskRequest.html).newBuilder()
                          .setDisk(primaryDiskName)
                          .[setDisksStartAsyncReplicationRequestResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationDiskRequest.Builder.html#com_google_cloud_compute_v1_StartAsyncReplicationDiskRequest_Builder_setDisksStartAsyncReplicationRequestResource_com_google_cloud_compute_v1_DisksStartAsyncReplicationRequest_)(diskRequest)
                          .setProject(projectId)
                          .setZone(primaryDiskLocation)
                          .build();
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.startAsyncReplicationAsync(request).get(1, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error starting replication! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
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
    // The project of the secondary disk.
    const secondaryProjectId = await disksClient.getProjectId();
    
    // The zone of the secondary disk.
    // secondaryLocation = 'us-central1-a';
    
    // The name of the secondary disk.
    // secondaryDiskName = 'secondary-disk-name';
    
    // The project of the primary disk.
    const primaryProjectId = await disksClient.getProjectId();
    
    // The zone of the primary disk.
    // primaryLocation = 'us-central1-a';
    
    // The name of the primary disk.
    // primaryDiskName = 'primary-disk-name';
    
    // Start replication
    async function callStartReplication() {
      const [response] = await disksClient.startAsyncReplication({
        project: secondaryProjectId,
        zone: primaryLocation,
        disk: primaryDiskName,
        disksStartAsyncReplicationRequestResource:
          new compute.DisksStartAsyncReplicationRequest({
            asyncSecondaryDisk: `projects/${primaryProjectId}/zones/${secondaryLocation}/disks/${secondaryDiskName}`,
          }),
      });
    
      let operation = response.latestResponse;
    
      // Wait for the operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: secondaryProjectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(
        `Data replication from primary disk: ${primaryDiskName} to secondary disk: ${secondaryDiskName} started.`
      );
    }
    
    await callStartReplication();

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
    
    
    def start_disk_replication(
        project_id: str,
        primary_disk_location: str,
        primary_disk_name: str,
        secondary_disk_location: str,
        secondary_disk_name: str,
    ) -> bool:
        """Starts the asynchronous replication of a primary disk to a secondary disk.
        Args:
            project_id (str): The ID of the Google Cloud project.
            primary_disk_location (str): The location of the primary disk, either a zone or a region.
            primary_disk_name (str): The name of the primary disk.
            secondary_disk_location (str): The location of the secondary disk, either a zone or a region.
            secondary_disk_name (str): The name of the secondary disk.
        Returns:
            bool: True if the replication was successfully started.
        """
        # Check if the primary disk location is a region or a zone.
        if primary_disk_location[-1].isdigit():
            region_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
            request_resource = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksStartAsyncReplicationRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RegionDisksStartAsyncReplicationRequest.html)(
                async_secondary_disk=f"projects/{project_id}/regions/{secondary_disk_location}/disks/{secondary_disk_name}"
            )
            operation = region_client.[start_async_replication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_start_async_replication)(
                project=project_id,
                region=primary_disk_location,
                disk=primary_disk_name,
                region_disks_start_async_replication_request_resource=request_resource,
            )
        else:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
            request_resource = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksStartAsyncReplicationRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DisksStartAsyncReplicationRequest.html)(
                async_secondary_disk=f"zones/{secondary_disk_location}/disks/{secondary_disk_name}"
            )
            operation = client.[start_async_replication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_start_async_replication)(
                project=project_id,
                zone=primary_disk_location,
                disk=primary_disk_name,
                disks_start_async_replication_request_resource=request_resource,
            )
        wait_for_extended_operation(operation, verbose_name="replication operation")
        print(f"Replication for disk {primary_disk_name} started.")
        return True
    
    

###  REST 

Start replication using one of the following methods:

  * Start replication for zonal disks using the [`disks.startAsyncReplication` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/startAsyncReplication):
        
        POST https://compute.googleapis.com/compute/v1/projects/PRIMARY_DISK_PROJECT/zones/PRIMARY_LOCATION/disks/PRIMARY_DISK_NAME/startAsyncReplication
        
        {
        "asyncSecondaryDisk": "projects/SECONDARY_DISK_PROJECT/SECONDARY_LOCATION_PARAMETER/SECONDARY_LOCATION/disks/SECONDARY_DISK_NAME"
        }
        

  * Start replication for regional disks using the [`regionDisks.startAsyncReplication` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/startAsyncReplication):
        
        POST https://compute.googleapis.com/compute/v1/projects/PRIMARY_DISK_PROJECT/regions/PRIMARY_LOCATION/regionDisks/PRIMARY_DISK_NAME/startAsyncReplication
        
        {
        "asyncSecondaryDisk": "projects/SECONDARY_DISK_PROJECT/SECONDARY_LOCATION_PARAMETER/SECONDARY_LOCATION/disks/SECONDARY_DISK_NAME"
        }
        




Replace the following:

  * `PRIMARY_DISK_PROJECT`: the project that contains the primary disk.
  * `PRIMARY_LOCATION`: The primary disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.
  * `PRIMARY_DISK_NAME`: the name of the primary disk.
  * `SECONDARY_DISK_PROJECT`: the project that contains the secondary disk.
  * `SECONDARY_LOCATION_PARAMETER`: the location parameter for the secondary disk. For regional disks, use `regions`. For zonal disks, use `zones`.
  * `SECONDARY_LOCATION`: The secondary disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.
  * `SECONDARY_DISK_NAME`: the name of the secondary disk.



###  Terraform 

To start replication between primary and secondary disks, use the [`compute_disk_async_replication` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk_async_replication).
    
    
    resource "google_compute_disk_async_replication" "default" {
      primary_disk = google_compute_disk.primary_disk.id
      secondary_disk {
        disk = google_compute_disk.secondary_disk.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Stop replication

You can stop replication for a single primary or secondary disk, or for all disks in a consistency group. If you stop replication for a single disk in a consistency group, the replication time for that disk becomes out of sync with the other disks in the consistency group.

Stopping replication is performed in [failover and failback](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback) scenarios. If you stop replication, you can't restart replication to the same secondary disk. If you want to restart replication, you must create a new secondary disk and start again.

When you stop replication on a disk, the disk's replication state changes to `STOPPED`. The replication state of the other disk in the disk's replication pair (the corresponding primary or secondary disk) updates to `STOPPED` at a later time. If you want to avoid the time gap and update the replication state of the other disk to `STOPPED` immediately, you must manually stop replication on the other disk as well. Stopping replication on both disks doesn't affect the time at which replication stops, it only affects the disks' replication states.

### Stop replication for a single disk

Stop replication for a single disk using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

Stop replication by doing the following:

  1. In the Google Cloud console, go to the **Asynchronous replication** page.

[Go to Asynchronous replication](https://console.cloud.google.com/compute/asynchronousReplication)

  2. Click the name of primary or secondary disk for which you want to stop replication. The **Manage disk** page opens.

  3. Click **Terminate replication**. The **Terminate replication** window opens.

  4. Click **Terminate replication**.




###  gcloud 

Stop replication using the [`gcloud compute disks stop-async-replication` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/stop-async-replication):
    
    
    gcloud compute disks stop-async-replication DISK_NAME \
        --LOCATION_FLAG=LOCATION
    

Replace the following:

  * `DISK_NAME`: the name of the disk.
  * `LOCATION_FLAG`: the location flag for the disk. For a regional disk, use `--region`. For a zonal disk, use `--zone`.
  * `LOCATION`: the disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // stopReplication stops primary disk replication in a project for a given zone.
    func stopReplication(
    	w io.Writer,
    	projectID, primaryDiskName, primaryZone string,
    ) error {
    	// projectID := "your_project_id"
    	// primaryDiskName := "your_disk_name2"
    	// primaryZone := "europe-west2-b"
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.StopAsyncReplicationDiskRequest{
    		Project: projectID,
    		Zone:    primaryZone,
    		Disk:    primaryDiskName,
    	}
    
    	op, err := disksClient.StopAsyncReplication(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Replication stopped\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[StopAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopAsyncReplicationDiskRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class StopZonalDiskReplication {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The project that contains the primary disk.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region or zone in which your secondary disk is located.
        String secondaryDiskLocation = "us-east1-b";
        // Name of the secondary disk.
        String secondaryDiskName = "SECONDARY_DISK_NAME";
    
        stopZonalDiskAsyncReplication(projectId, secondaryDiskLocation, secondaryDiskName);
      }
    
      // Stops asynchronous replication for the specified disk.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) stopZonalDiskAsyncReplication(
              String project, String secondaryDiskLocation, String secondaryDiskName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          [StopAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopAsyncReplicationDiskRequest.html) stopReplicationDiskRequest =
                  [StopAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopAsyncReplicationDiskRequest.html).newBuilder()
                          .setProject(project)
                          .setDisk(secondaryDiskName)
                          .setZone(secondaryDiskLocation)
                          .build();
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.stopAsyncReplicationAsync(stopReplicationDiskRequest)
                  .get(1, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error stopping replication! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Instantiate a diskClient
    const disksClient = new computeLib.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the primary disk.
    const primaryProjectId = await disksClient.getProjectId();
    
    // The zone of the primary disk.
    // primaryLocation = 'us-central1-a';
    
    // The name of the primary disk.
    // primaryDiskName = 'primary-disk-name';
    
    // Stop replication
    async function callStopReplication() {
      const [response] = await disksClient.stopAsyncReplication({
        project: primaryProjectId,
        zone: primaryLocation,
        disk: primaryDiskName,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: primaryProjectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Replication for primary disk: ${primaryDiskName} stopped.`);
    }
    
    await callStopReplication();

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
    
    
    def stop_disk_replication(
        project_id: str, primary_disk_location: str, primary_disk_name: str
    ) -> bool:
        """
        Stops the asynchronous replication of a disk.
        Args:
            project_id (str): The ID of the Google Cloud project.
            primary_disk_location (str): The location of the primary disk, either a zone or a region.
            primary_disk_name (str): The name of the primary disk.
        Returns:
            bool: True if the replication was successfully stopped.
        """
        # Check if the primary disk is in a region or a zone
        if primary_disk_location[-1].isdigit():
            region_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
            operation = region_client.[stop_async_replication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_stop_async_replication)(
                project=project_id, region=primary_disk_location, disk=primary_disk_name
            )
        else:
            zone_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
            operation = zone_client.[stop_async_replication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_stop_async_replication)(
                project=project_id, zone=primary_disk_location, disk=primary_disk_name
            )
    
        wait_for_extended_operation(operation, verbose_name="replication operation")
        print(f"Replication for disk {primary_disk_name} stopped.")
        return True
    
    

###  REST 

Stop replication using one of the following methods:

  * Stop replication for zonal disks using the [`disks.stopAsyncReplication` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/stopAsyncReplication):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/LOCATION/disks/DISK_NAME/stopAsyncReplication
        {
        }
        

  * Stop replication for regional disks using the [`regionDisks.stopAsyncReplication` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/stopAsyncReplication):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/LOCATION/regionDisks/DISK_NAME/stopAsyncReplication
        {
        }
        




Replace the following:

  * `PROJECT`: the project that contains the disk.
  * `DISK_NAME`: the name of the disk.
  * `LOCATION`: the zone or region of the disk. For zonal disks, use the zone. For regional disks, use the region.



###  Terraform 

To stop the replication on primary and secondary disks, remove the `compute_disk_async_replication` resource.

### Stop replication for a consistency group

Stop replication for all disks in a consistency group using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

Stop replication for all disks in a consistency group by doing the following:

  1. In the Google Cloud console, go to the **Consistency Groups** page.

[Go to Consistency Groups](https://console.cloud.google.com/compute/consistencyGroups)

  2. In the **Disk consistency groups** tab, click the name of the consistency group for which you want to stop replication. The **Manage consistency group** page opens.

  3. Click **Terminate replication**. The **Terminate replication** window opens.

  4. Click **Terminate replication**.




###  gcloud 

Stop replication for all disks in a consistency group using the [`gcloud compute disks stop-group-async-replication` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication):
    
    
    gcloud compute disks stop-group-async-replication CONSISTENCY_GROUP \
    --LOCATION_FLAG=LOCATION
    

Replace the following:

  * `CONSISTENCY_GROUP`: the URL of the consistency group. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.
  * `LOCATION_FLAG`: the location flag for the disks in the consistency group. For regional disks, use `--region`. For zonal disks, use `--zone`.
  * `LOCATION`: the disk's region or zone. For regional disks, use the region. For zonal disks, use the zone.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // stopReplicationConsistencyGroup stop replication for a consistency group for a project in a given region.
    func stopReplicationConsistencyGroup(w io.Writer, projectID, region, groupName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-west4"
    	// groupName := "your_group_name"
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	consistencyGroupUrl := fmt.Sprintf("projects/%s/regions/%s/resourcePolicies/%s", projectID, region, groupName)
    
    	req := &computepb.StopGroupAsyncReplicationRegionDiskRequest{
    		Project: projectID,
    		DisksStopGroupAsyncReplicationResourceResource: &computepb.DisksStopGroupAsyncReplicationResource{
    			ResourcePolicy: proto.String(consistencyGroupUrl),
    		},
    		Region: region,
    	}
    
    	op, err := disksClient.StopGroupAsyncReplication(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to stop replication: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Group stopped replicating\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[DisksStopGroupAsyncReplicationResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksStopGroupAsyncReplicationResource.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[StopGroupAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopGroupAsyncReplicationDiskRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class StopZonalDiskReplicationConsistencyGroup {
      public static void main(String[] args)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project that contains the disk.
        String project = "YOUR_PROJECT_ID";
        // Zone of the disk.
        String zone = "us-central1-a";
        // Name of the consistency group.
        String consistencyGroupName = "CONSISTENCY_GROUP";
    
        stopZonalDiskReplicationConsistencyGroup(project, zone, consistencyGroupName);
      }
    
      // Stops replication of a consistency group for a project in a given zone.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) stopZonalDiskReplicationConsistencyGroup(
              String project, String zone, String consistencyGroupName)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
        String region = zone.substring(0, zone.lastIndexOf('-'));
    
        String resourcePolicy = String.format("projects/%s/regions/%s/resourcePolicies/%s",
                project, region, consistencyGroupName);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          [StopGroupAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopGroupAsyncReplicationDiskRequest.html) request =
                  [StopGroupAsyncReplicationDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopGroupAsyncReplicationDiskRequest.html).newBuilder()
                          .setProject(project)
                          .setZone(zone)
                          .setDisksStopGroupAsyncReplicationResourceResource(
                                  [DisksStopGroupAsyncReplicationResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksStopGroupAsyncReplicationResource.html).newBuilder()
                                          .setResourcePolicy(resourcePolicy).build())
                          .build();
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.stopGroupAsyncReplicationAsync(request)
                  .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error stopping disk replication! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // If disks are regional- use RegionDisksClient and RegionOperationsClient.
    // TODO(developer): Uncomment disksClient and zoneOperationsClient before running the sample.
    // Instantiate a disksClient
    // disksClient = new computeLib.DisksClient();
    // Instantiate a zoneOperationsClient
    // zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the consistency group.
    const projectId = await disksClient.getProjectId();
    
    // If you use RegionDisksClient- define region, if DisksClient- define zone.
    // The zone or region of the disks.
    const disksLocation = 'europe-central2-a';
    
    // The name of the consistency group.
    const consistencyGroupName = 'consistency-group-1';
    
    // The region of the consistency group.
    const consistencyGroupLocation = 'europe-central2';
    
    async function callStopReplication() {
      const [response] = await disksClient.stopGroupAsyncReplication({
        project: projectId,
        // If you use RegionDisksClient, pass region as an argument instead of zone.
        zone: disksLocation,
        disksStopGroupAsyncReplicationResourceResource:
          new compute.DisksStopGroupAsyncReplicationResource({
            resourcePolicy: [
              `https://www.googleapis.com/compute/v1/projects/${projectId}/regions/${consistencyGroupLocation}/resourcePolicies/${consistencyGroupName}`,
            ],
          }),
      });
    
      let operation = response.latestResponse;
    
      // Wait for the operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          // If you use RegionDisksClient, pass region as an argument instead of zone.
          zone: operation.zone.split('/').pop(),
        });
      }
    
      const message = `Replication stopped for consistency group: ${consistencyGroupName}.`;
      console.log(message);
      return message;
    }
    
    return await callStopReplication();

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
    
    
    def stop_replication_consistency_group(project_id, location, consistency_group_name):
        """
        Stops the asynchronous replication for a consistency group.
        Args:
            project_id (str): The ID of the Google Cloud project.
            location (str): The region where the consistency group is located.
            consistency_group_id (str): The ID of the consistency group.
        Returns:
            bool: True if the replication was successfully stopped.
        """
        consistency_group = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksStopGroupAsyncReplicationResource](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DisksStopGroupAsyncReplicationResource.html)(
            resource_policy=f"regions/{location}/resourcePolicies/{consistency_group_name}"
        )
        region_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
        operation = region_client.[stop_group_async_replication](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_stop_group_async_replication)(
            project=project_id,
            region=location,
            disks_stop_group_async_replication_resource_resource=consistency_group,
        )
        wait_for_extended_operation(operation, "Stopping replication for consistency group")
    
        return True
    
    

###  REST 

Stop replication for all disks in a consistency group using one of the following methods:

  * Stop replication for zonal disks using the [`disks.stopGroupAsyncReplication` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/stopGroupAsyncReplication):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/LOCATION/disks/stopGroupAsyncReplication
        {
        "resourcePolicy": "CONSISTENCY_GROUP"
        }
        

  * Stop replication for regional disks using the [`regionDisks.stopGroupAsyncReplication` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/stopGroupAsyncReplication):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/LOCATION/regionDisks/DISK_NAME/stopAsyncReplication
        {
        "resourcePolicy": "CONSISTENCY_GROUP"
        }
        




Replace the following:

  * `DISK_NAME`: the name of the disk
  * `LOCATION`: the zone or region of the disk. For zonal disks, use the zone. For regional disks, use the region.
  * `CONSISTENCY_GROUP`: the URL of the consistency group. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.



## What's next

  * Learn how to [failover and failback](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback).
  * Learn how to [monitor Asynchronous Replication performance](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
