---
url: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-list/
title: List snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:06.946660+00:00
---

# List snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-snapshot-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This sample lists all snapshots in a project. You can filter the results by specifying a filter expression.

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
    	"google.golang.org/api/iterator"
    )
    
    // listSnapshots prints a list of disk snapshots in the given project
    func listSnapshots(w io.Writer, projectID, filter string) error {
    	// projectID := "your_project_id"
    	// filter := ""
    	// Learn more about filters:
    	// https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListSnapshotsRequest
    	ctx := context.Background()
    	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.ListSnapshotsRequest{
    		Project: projectID,
    		Filter:  &filter,
    	}
    
    	it := snapshotsClient.List(ctx, req)
    	fmt.Fprintf(w, "Found snapshots:\n")
    	for {
    		snapshot, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s\n", snapshot.GetName())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest.html);
    import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
    import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
    import java.io.IOException;
    
    public class ListSnapshots {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Filter to be applied when listing snapshots. Learn more about filters here:
        // https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListSnapshotsRequest
        String filter = "FILTER_CONDITION";
    
        listSnapshots(projectId, filter);
      }
    
      // List snapshots from a project.
      public static void listSnapshots(String projectId, String filter) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `snapshotsClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
    
          // Create the List Snapshot request.
          [ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest.html) listSnapshotsRequest = [ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest.html).newBuilder()
              .setProject(projectId)
              .setFilter(filter)
              .build();
    
          System.out.println("List of snapshots:");
          for ([Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshot : snapshotsClient.list(listSnapshotsRequest).iterateAll()) {
            System.out.println(snapshot.getName());
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
    
    
    def list_snapshots(project_id: str, filter_: str = "") -> Iterable[compute_v1.Snapshot]:
        """
        List snapshots from a project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            filter_: filter to be applied when listing snapshots. Learn more about filters here:
                https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListSnapshotsRequest
    
        Returns:
            An iterable containing all Snapshots that match the provided filter.
        """
    
        snapshot_client = compute_v1.SnapshotsClient()
        request = compute_v1.ListSnapshotsRequest()
        request.project = project_id
        request.filter = filter_
    
        return snapshot_client.list(request)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
