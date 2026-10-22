---
url: https://docs.cloud.google.com/compute/docs/samples/compute-disk-delete/
title: Delete a disk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:14.656325+00:00
---

# Delete a disk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-disk-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Delete a disk Stay organized with collections  Save and categorize content based on your preferences. 

Delete a persistent disk from the specified zone.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Move a VM instance between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace compute_disks = ::google::cloud::compute_disks_v1;
    [](std::string const& project_id, std::string const& zone,
       std::string const& disk_name) {
      auto client =
          compute_disks::DisksClient(compute_disks::MakeDisksConnectionRest());
      auto delete_result = client.DeleteDisk(project_id, zone, disk_name).get();
      if (!delete_result) throw std::move(delete_result).status();
      std::cout << "Deleted disk: " << disk_name << "\n";
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // deleteDisk deletes a disk from a project.
    func deleteDisk(w io.Writer, projectID, zone, diskName string) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b"
    	// diskName := "your_disk_name"
    
    	ctx := context.Background()
    	disksClient, err := compute.NewDisksRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.DeleteDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		Disk:    diskName,
    	}
    
    	op, err := disksClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk deleted\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.DeleteDiskRequest;
    import com.google.cloud.compute.v1.DisksClient;
    import com.google.cloud.compute.v1.Operation;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteDisk {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // The zone from where you want to delete the disk.
        String zone = "europe-central2-b";
    
        // Name of the disk you want to delete.
        String diskName = "YOUR_DISK_NAME";
    
        deleteDisk(projectId, zone, diskName);
      }
    
      // Deletes a disk from a project.
      public static void deleteDisk(String projectId, String zone, String diskName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try (DisksClient disksClient = DisksClient.create()) {
    
          // Create the request object.
          DeleteDiskRequest deleteDiskRequest = DeleteDiskRequest.newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setDisk(diskName)
              .build();
    
          // Wait for the delete disk operation to complete.
          Operation response = disksClient.deleteAsync(deleteDiskRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.hasError()) {
            System.out.println("Disk deletion failed!" + response);
            return;
          }
          System.out.println("Operation Status: " + response.getStatus());
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
    
    const compute = require('@google-cloud/compute');
    
    async function deleteDisk() {
      const disksClient = new compute.DisksClient();
    
      const [response] = await disksClient.delete({
        project: projectId,
        zone,
        disk: diskName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.ZoneOperationsClient();
    
      // Wait for the create disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Disk deleted.');
    }
    
    deleteDisk();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
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
    
    
    def delete_disk(project_id: str, zone: str, disk_name: str) -> None:
        """
        Deletes a disk from a project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone in which is the disk you want to delete.
            disk_name: name of the disk you want to delete.
        """
        disk_client = compute_v1.DisksClient()
        operation = disk_client.delete(project=project_id, zone=zone, disk=disk_name)
        wait_for_extended_operation(operation, "disk deletion")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
