---
url: https://docs.cloud.google.com/compute/docs/samples/compute-disk-list/
title: List disks in a zone \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:16.940220+00:00
---

# List disks in a zone  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-disk-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List disks in a zone Stay organized with collections  Save and categorize content based on your preferences. 

This sample lists all the disks in a given zone.

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
    
    // listDisks lists disks in a project zone.
    func listDisks(w io.Writer, projectID, zone, filter string) error {
    	// projectID := "your_project_id"
    	// zone := "us-central1-a"
    	// filter := ""
    
    	// Formatting for filters:
    	// https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListDisksRequest
    
    	ctx := context.Background()
    	client, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &computepb.ListDisksRequest{
    		Project: projectID,
    		Zone:    zone,
    		Filter:  &filter,
    	}
    
    	it := client.List(ctx, req)
    	fmt.Fprintf(w, "Disks in zone %s:\n", zone)
    	for {
    		disk, err := it.Next()
    		if err == context.Canceled || err == context.DeadlineExceeded {
    			return err
    		}
    		if err != nil {
    			break
    		}
    		fmt.Fprintf(w, "- %s\n", *disk.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name))
    	}
    
    	if err != nil {
    		return fmt.Errorf("ListDisks: %w", err)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[ListDisksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListDisksRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class ListDisks {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // The zone where the disks are located.
        String zone = "europe-central2-b";
    
        // Filter to be applied when listing disks. Learn more about filters here:
        // https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListDisksRequest
        String filter = "FILTER_CONDITION";
    
        listDisks(projectId, zone, filter);
      }
    
      // Lists disks from a project.
      public static void listDisks(String projectId, String zone, String filter)
          throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          // Create the request object.
          [ListDisksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListDisksRequest.html) listDisksRequest = [ListDisksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListDisksRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setFilter(filter)
              .build();
    
          System.out.println("List of disks:");
          for ([Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk : disksClient.list(listDisksRequest).iterateAll()) {
            System.out.println(disk.getName());
          }
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_disks(
        project_id: str, zone: str, filter_: str = ""
    ) -> Iterable[compute_v1.Disk]:
        """
        Lists disks in a project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone
            filter_: filter to be applied when listing disks. Learn more about filters here:
                https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListDisksRequest
        """
        disk_client = compute_v1.DisksClient()
        request = compute_v1.ListDisksRequest()
        request.project = project_id
        request.zone = zone
        request.filter = filter_
        return disk_client.list(request)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
