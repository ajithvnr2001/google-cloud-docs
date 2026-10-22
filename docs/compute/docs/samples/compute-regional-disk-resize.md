---
url: https://docs.cloud.google.com/compute/docs/samples/compute-regional-disk-resize/
title: Resize a regional persistent disk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:50.075890+00:00
---

# Resize a regional persistent disk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-regional-disk-resize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Resize a regional persistent disk Stay organized with collections  Save and categorize content based on your preferences. 

This sample resizes a regional persistent disk to a specified size in GB. After you resize the disk, you must also resize the file system so that the operating system can access the additional space.

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
    )
    
    // resizeRegionalDisk changes the size of a regional disk.
    // After you resize the disk, you must also resize the file system
    // so that the operating system can access the additional space.
    func resizeRegionalDisk(w io.Writer, projectID, region, diskName string, newSizeGb int64) error {
    	// projectID := "your_project_id"
    	// region := "us-west3"
    	// diskName := "your_disk_name"
    	// newSizeGb := 20
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.ResizeRegionDiskRequest{
    		Disk:    diskName,
    		Project: projectID,
    		Region:  region,
    		RegionDisksResizeRequestResource: &computepb.RegionDisksResizeRequest{
    			SizeGb: &newSizeGb,
    		},
    	}
    
    	op, err := disksClient.Resize(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to resize disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk resized\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
    import com.google.cloud.compute.v1.[RegionDisksResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksResizeRequest.html);
    import com.google.cloud.compute.v1.[ResizeRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ResizeRegionalDisk {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "your-project-id";
    
        // Region of the disk to be resized.
        String diskRegion = "us-central1";
    
        // Name of the disk that you want to resize.
        String diskName = "DISK_NAME";
    
        // The new size you want to set for the disk in gigabytes.
        int newSizeGb = 23;
    
        resizeRegionalDisk(projectId, diskRegion, diskName, newSizeGb);
      }
    
      // Resizes a regional persistent disk to a specified size in GB. After you resize the disk, you
      // must also resize the file system so that the operating system can access the additional space.
      public static void resizeRegionalDisk(String projectId, String diskRegion, String diskName,
          int newSizeGb)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `regionDisksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) regionDisksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create()) {
    
          [ResizeRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest.html) resizeRegionDiskRequest = [ResizeRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest.html).newBuilder()
              .setRegion(diskRegion)
              .[setRegionDisksResizeRequestResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest.Builder.html#com_google_cloud_compute_v1_ResizeRegionDiskRequest_Builder_setRegionDisksResizeRequestResource_com_google_cloud_compute_v1_RegionDisksResizeRequest_)([RegionDisksResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksResizeRequest.html).newBuilder()
                  .setSizeGb(newSizeGb)
                  .build())
              .setDisk(diskName)
              .setProject(projectId)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = regionDisksClient.resizeAsync(resizeRegionDiskRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Resize region disk failed! " + response);
            return;
          }
          System.out.println("Resize region disk - operation status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import re
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
    
    
    def resize_disk(project_id: str, disk_link: str, new_size_gb: int) -> None:
        """
        Resizes a persistent disk to a specified size in GB. After you resize the disk, you must
        also resize the file system so that the operating system can access the additional space.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            disk_link: a link to the disk you want to resize.
                This value uses the following format:
                    * https://www.googleapis.com/compute/v1/projects/{project_name}/zones/{zone}/disks/{disk_name}
                    * projects/{project_name}/zones/{zone}/disks/{disk_name}
                    * projects/{project_name}/regions/{region}/disks/{disk_name}
            new_size_gb: the new size you want to set for the disk in gigabytes.
        """
        search_results = re.search(
            r"/projects/[\w_-]+/(?P<area_type>zones|regions)/"
            r"(?P<area_name>[\w_-]+)/disks/(?P<disk_name>[\w_-]+)",
            disk_link,
        )
    
        if search_results["area_type"] == "regions":
            disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
            request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResizeRegionDiskRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResizeRegionDiskRequest.html)()
            request.region = search_results["area_name"]
            request.region_disks_resize_request_resource = (
                [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksResizeRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RegionDisksResizeRequest.html)()
            )
            request.region_disks_resize_request_resource.size_gb = new_size_gb
        else:
            disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
            request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResizeDiskRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResizeDiskRequest.html)()
            request.zone = search_results["area_name"]
            request.disks_resize_request_resource = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksResizeRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DisksResizeRequest.html)()
            request.disks_resize_request_resource.size_gb = new_size_gb
    
        request.disk = search_results["disk_name"]
        request.project = project_id
    
        operation = disk_client.[resize](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_resize)(request)
        wait_for_extended_operation(operation, "disk resize")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
