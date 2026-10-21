---
url: https://docs.cloud.google.com/compute/docs/disks/manage-snapshots/
title: Manage disk snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:27.747684+00:00
---

# Manage disk snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/manage-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[Standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) help you to periodically back up data from your Persistent Disk and Google Cloud Hyperdisk.

You can view, list, and delete disk snapshots. You can also share snapshots across projects.

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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required roles and permissions

To get the permissions that you need to manage standard snapshots, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage standard snapshots. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage standard snapshots:

  * To list snapshots in a project or location: `compute.snapshots.list` on the project 
  * To view information about a snapshot: `compute.snapshots.get` on the snapshot 
  * To delete a snapshot: `compute.snapshots.delete` on the snapshot 
  * To delete snapshots based on a filter: 
    * `compute.snapshots.delete` on the snapshot
    * `compute.snapshots.list` on the project
  * To share snapshot data across projects: 
    * `compute.storageAdmin` on the project (for accessing all standard snapshots)
    * `compute.disks.create` on the project to share with
    * `compute.snapshots.create` on the source project
    * `compute.disks.createSnapshot` on the source disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View standard snapshots

You can view a list of all standard snapshots by project, location, or disk.

### View the standard snapshots in a project or location

You can view or list the standard snapshots in a project or location by using the gcloud CLI, Google Cloud console, or the REST.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. On the **Snapshots** tab, you can see the standard snapshots for the current project.

  3. Optional. Narrow your results with the filter_list **Filter** field. Enter a property name or value in the **Filter** field, or choose from the available properties.




###  gcloud 

  * To see a list of all snapshots available to you in a particular project, use the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list).
        
        gcloud compute snapshots list --project=PROJECT_ID
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To see a list of regionally scoped snapshots available to you in a particular project, use the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list) and specify the region.
        
        gcloud compute snapshots list --region=REGION_NAME
        

  * To see a list of globally scoped snapshots available to you in a particular project, use the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list) and include the `--global` flag.
        
        gcloud compute snapshots list --global
        




Replace the following:

  * `PROJECT_ID`: Optional. Replace with the project ID. If you omit this flag, then the current project is used. You can set the default project for your session by using the gcloud CLI command `gcloud config set project PROJECT_ID`.
  * `REGION_NAME`: The name of the region that you want to view snapshots for.



###  REST 

  * To see a list of all snapshots available to you in a particular project, make a `GET` request to the [`snapshots.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/list) and specify "aggregated".
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/snapshots
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To see a list of regionally scoped snapshots available to you in a particular project, make a `GET` request to the [`snapshots.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/list) and specify the region.
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/snapshots
        

  * To see a list of globally scoped snapshots available to you in a particular project, make a `GET` request to the [`snapshots.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/list) and specify "global".
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots
        




Replace the following:

  * `PROJECT_ID`: The project ID.
  * `REGION_NAME`: The name of the region that you want to view snapshots for.



### View the standard snapshots for a disk

You can view the list of standard snapshots for a disk by using the Google Cloud console, gcloud CLI,or REST.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. On the **Snapshots** tab, a list of all the standard snapshots in the project appears.

  3. Narrow the results by source disk:

     1. Enter `Source disk:` in the filter_list **Filter** field, or click the **Filter** field and then choose the value `Source disk` from the **Properties** list.

     2. Select the name of the disk from the **Values** list that appears next to `Source disk:` in the **Filter** field.

The snapshots displayed in the console now shows all standard snapshots for the specified disk.

If you don't see the name of a disk in the **Values** list, then in the **Filter** field next to `Source disk:`, type in the first few letters of the source disk's name to change the list of values that you see.




###  gcloud 

List the standard snapshots for a disk with the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list) and the [`--filter` argument](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list#--filter).

  * List the standard snapshots for a zonal disk:
        
        gcloud compute snapshots list --filter="sourceDisk:projects/PROJECT_ID/zones/SOURCE_ZONE/disks/DISK_NAME
        

  * List the standard snapshots for a regional disk:
        
        gcloud compute snapshots list --filter=sourceDisk:projects/PROJECT_ID/regions/SOURCE_REGION/disks/DISK_NAME
        




Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `SOURCE_ZONE`: (Zonal disks only) the name of the zone for the disk, for example, `us-west1-a`.
  * `SOURCE_REGION`: (Regional disks only) the name of the region for the disk, for example, `us-west1`.
  * `DISK_NAME`: the name of the disk, for example, `disk-1`.



###  REST 

List the standard snapshots for a zonal or regional disk with a `GET` request to the [`snapshots.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/list).

Use the `filter=sourceDisk` query parameter to specify the name of the disk.

  * List the standard snapshots for a zonal disk:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots?filter=sourceDisk:'https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/SOURCE_ZONE/disks/DISK_NAME'
        

  * List the standard snapshots for a regional disk:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots?filter=sourceDisk:'https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/SOURCE_REGION/disks/DISK_NAME'
        




Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `SOURCE_ZONE`: (Zonal disks only) the name of the zone for the disk, for example, `us-west1-a`.
  * `SOURCE_REGION`: (Regional disks only) the name of the region for the disk, for example, `us-west1`.
  * `DISK_NAME`: the name of the source disk, for example `disk-1`.



## View information about a standard snapshot

Retrieve detailed information about a standard snapshot, such as its creation time, source disk, and size by using the Google Cloud console, Google Cloud CLI, or REST.

To determine if the recycle bin is enabled for a specific standard snapshot, see [Check the recycle bin retention period for a specific snapshot](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin#view-retention-period-snapshot).

**Note:** A snapshot's size is zero if no data on the disk has changed since the previous snapshot was created. So, if a snapshot's size is zero, this doesn't mean that the disk is empty or that there was a problem backing up the disk.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. On the **Snapshots** tab, view the list of snapshots in the project.

  3. In the **Name** column, click the name of the standard snapshot. The **Snapshot details** page for the selected snapshot appears, showing its properties.




###  gcloud 

  * To view information about a globally scoped standard snapshot, use the [`gcloud compute snapshots describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe).
        
        gcloud compute snapshots describe SNAPSHOT_NAME
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To view information about a regionally scoped standard snapshot, use the [`gcloud compute snapshots describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe) and specify the region.
        
        gcloud compute snapshots describe SNAPSHOT_NAME --regions=REGION_NAME
        




Replace the following:

  * `SNAPSHOT_NAME`: The name of the standard snapshot.
  * `REGION_NAME`: The name of the region that your snapshot is scoped to.



###  REST 

  * To view information about a globally scoped standard snapshot, make a `GET` request to the [`snapshots.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To view information about a regionally scoped standard snapshot, make a `GET` request to the [`snapshots.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/get) and specify the region.
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/snapshots/SNAPSHOT_NAME
        




Replace the following:

  * `PROJECT_ID`: The name of the project containing the standard snapshot.
  * `SNAPSHOT_NAME`: The name of the standard snapshot.
  * `REGION_NAME`: The name of the region that your snapshot is scoped to.



## Delete snapshots

To reduce your storage costs, you can delete a single standard or archive snapshot or multiple snapshots based on a filter.

Deleting an image, instant snapshot, image, or archive snapshot is irreversible.

Deleting a standard snapshot might be irreversible if the recycle bin ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) is disabled for the standard snapshot. 

Before you delete a standard snapshot that contains critical data, you can [ check if the recycle bin is enabled for the snapshot](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin#view-retention-period-snapshot). If you accidentally delete a standard snapshot, you might be able recover it if Compute Engine retained the snapshot in the recycle bin. For more information, see [Recover a deleted snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin#recover-snapshot). 

### Delete a snapshot

Compute Engine uses differential snapshots so that each snapshot contains only the data that has changed since the previous snapshot. Because subsequent snapshots might require information stored in a previous snapshot, keep in mind that deleting a snapshot does not necessarily delete all the data on the snapshot.

To learn more about snapshot deletion, see [Snapshot deletion](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot_deletion).

###  Console 

  1. Go to the **Snapshots** page in the Google Cloud console.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Select one or more snapshots that you want to delete.

  3. At the top of the **Snapshots** page, click **Delete**.




###  gcloud 

  * To delete a globally scoped snapshot, use the [`gcloud compute snapshots delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete).
        
        gcloud compute snapshots delete SNAPSHOT_NAME
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To delete a regionally scoped snapshot, use the [`gcloud compute snapshots delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete) and specify the region name.
        
        gcloud compute snapshots delete SNAPSHOT_NAME --regions=REGION_NAME
        




Replace the following:

  * SNAPSHOT_NAME: The name of the snapshot that you want to delete.
  * REGION_NAME: The region that the snapshot is scoped to.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // deleteSnapshot deletes a snapshot of a disk.
    func deleteSnapshot(w io.Writer, projectID, snapshotName string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    
    	ctx := context.Background()
    	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.DeleteSnapshotRequest{
    		Project:  projectID,
    		Snapshot: snapshotName,
    	}
    
    	op, err := snapshotsClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete snapshot: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Snapshot deleted\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteSnapshot {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // Name of the snapshot to be deleted.
        String snapshotName = "YOUR_SNAPSHOT_NAME";
    
        deleteSnapshot(projectId, snapshotName);
      }
    
      // Delete a snapshot of a disk.
      public static void deleteSnapshot(String projectId, String snapshotName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `snapshotsClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = snapshotsClient.deleteAsync(projectId, snapshotName)
              .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Snapshot deletion failed!" + operation);
            return;
          }
    
          System.out.println("Snapshot deleted!");
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const snapshotName = 'YOUR_SNAPSHOT_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function deleteSnapshot() {
      const snapshotsClient = new compute.[SnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await snapshotsClient.delete({
        project: projectId,
        snapshot: snapshotName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Snapshot deleted.');
    }
    
    deleteSnapshot();

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
    
    
    def delete_snapshot(project_id: str, snapshot_name: str) -> None:
        """
        Delete a snapshot of a disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            snapshot_name: name of the snapshot to delete.
        """
    
        snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
        operation = snapshot_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_delete)(project=project_id, snapshot=snapshot_name)
    
        wait_for_extended_operation(operation, "snapshot deletion")
    
    

###  REST 

  * To delete a globally scoped snapshot, make a `DELETE` request to the [`snapshots.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/delete).
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To delete a regionally scoped snapshot, make a `DELETE` request to the [`snapshots.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/delete) and specify the region.
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/snapshots/SNAPSHOT_NAME
        




Replace the following:

  * PROJECT_ID: The name of your project.
  * SNAPSHOT_NAME: The name of the snapshot to delete.
  * REGION_NAME: The region that the snapshot is scoped to.



### Delete multiple snapshots based on a filter

**Warning:** Deleting a snapshot is irreversible. You can't recover a deleted snapshot.

Compute Engine uses differential snapshots so that each snapshot contains only the data that has changed since the previous snapshot. Because subsequent snapshots might require information stored in a previous snapshot, deleting a snapshot does not necessarily delete all the data on the snapshot.

To learn more about snapshot deletion, see [Snapshot deletion](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot_deletion).

You can delete a number of snapshots based on a given filter. For more information on how to use filters with the gcloud CLI, see [gcloud CLI topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

To delete the snapshots, use a combination of the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list) with a given filter, and the [`gcloud compute snapshots delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete) with `xargs`.
    
    
      gcloud compute snapshots list --filter="EXPRESSION" --uri |
      xargs gcloud compute snapshots delete
      

Replace `EXPRESSION` with a gcloud CLI topic filter.

For example, `--filter="creationTimestamp<'2023-12-31'"` deletes all snapshots created before December 31, 2023.

## Share snapshot data across projects in the same organization

You can use this procedure to move data from a disk in one project to a disk in a different project within the same organization.

###  gcloud 

  1. Create a standard snapshot in the destination project by using the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create). For example, to create a snapshot of a zonal Persistent Disk or Hyperdisk, use the following command:
         
         gcloud compute snapshots create SNAPSHOT_NAME \
          --source-disk https://www.googleapis.com/compute/v1/projects/SOURCE_PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME \
          --project DESTINATION_PROJECT_ID
         

Replace the following:

     * SNAPSHOT_NAME: A name for the new snapshot.
     * SOURCE_PROJECT_ID: The ID of the project for the source disk.
     * ZONE: The zone of the source disk.
     * SOURCE_DISK_NAME: The name of the source disk.
     * DESTINATION_PROJECT_ID: The ID of the destination project for the new snapshot.
  2. In the destination project, create a zonal or regional disk that's based on the snapshot by using the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create):
         
         gcloud compute disks create DISK_NAME \
          --source-snapshot SNAPSHOT_NAME \
          --project DESTINATION_PROJECT_ID
         

Replace the following:

     * DISK_NAME: A name for the new disk.
     * SNAPSHOT_NAME: The name of the snapshot.
     * DESTINATION_PROJECT_ID: The ID of the destination project for the new disk.



###  REST 

  1. Create a standard snapshot in the destination project by calling the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert). For example, to take a snapshot of a zonal Persistent Disk or Hyperdisk, make the following request:
         
         POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
         {
          "name": SNAPSHOT_NAME
          "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME
         }
         

Replace the following:

     * DESTINATION_PROJECT_ID: The ID of the destination project for the new snapshot.
     * SNAPSHOT_NAME: A name for the snapshot.
     * SOURCE_PROJECT_ID: The ID of the source disk project.
     * SOURCE_ZONE: The zone of the source disk.
     * SOURCE_DISK_NAME: The name of the source disk.
  2. In the destination project, create a zonal or regional disk that's based on the snapshot by using the zonal [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) or the regional [`regionDisks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/insert).

For example, to create a zonal disk, make the following request:
         
         POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/zones/DESTINATION_ZONE/disks
         {
          "name": DISK_NAME
          "sourceSnapshot": SNAPSHOT_NAME
         }
         

Replace the following:

     * DESTINATION_PROJECT_ID: The ID of the destination project for the new disk.
     * DESTINATION_ZONE: The zone in the destination project for the new disk.
     * DISK_NAME: A name for the new disk.
     * SNAPSHOT_NAME: The name of the snapshot.



To get a list of snapshots available to you, see View the standard snapshots in a project or location.

## Share a snapshot across projects in different organizations

You can use this procedure to share a standard snapshot in a project in one organization with a different project in another organization.

###  gcloud 

  1. In the source project, create a disk that's based on the snapshot by using the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).
         
         gcloud compute disks create DISK_NAME \
          --source-snapshot SNAPSHOT_NAME \
          --project SOURCE_PROJECT_ID \
          --zone ZONE
         

Replace the following:

     * DISK_NAME: A name for the new disk.
     * SNAPSHOT_NAME: The name of the snapshot.
     * SOURCE_PROJECT_ID: The ID of the source project.
     * ZONE: The zone to create the new disk in.

This disk is a temporary disk that is created only to copy the snapshot across organizations.

  2. In the destination project, create a snapshot by using the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create).

For example, to create a snapshot using the zonal disk created in the first step, use the following command:
         
         gcloud compute snapshots create SNAPSHOT_NAME \
          --source-disk https://www.googleapis.com/compute/v1/projects/SOURCE_PROJECT_ID/zones/ZONE/disks/DISK_NAME \
          --project DESTINATION_PROJECT_ID
         

Replace the following:

     * SNAPSHOT_NAME: A name for the snapshot.
     * SOURCE_PROJECT_ID: The ID of the project that contains the source disk.
     * ZONE: The zone of the source disk.
     * DISK_NAME: The name of the disk created in step 1.
     * DESTINATION_PROJECT_ID: The ID of the destination project for the new snapshot.

To get a list of snapshots available to you, see View the standard snapshots in a project or location.

  3. Delete the temporary disk created in the first step using the [`gcloud compute disks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete).
         
         gcloud compute disks delete DISK_NAME \
          --project SOURCE_PROJECT_ID --zone ZONE
         

Replace the following:

     * DISK_NAME: The name of the disk created in step 1.
     * SOURCE_PROJECT_ID: The ID of the project that contains the source disk.
     * ZONE: The zone of the disk.



###  REST 

  1. In the source project, create a zonal or regional disk that's based on the snapshot by using the zonal [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert).

For example, to create a zonal disk, make the following request:
         
         POST https://compute.googleapis.com/compute/v1/projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks
         {
          "name": DISK_NAME
          "sourceSnapshot": SNAPSHOT_NAME
         }
         

Replace the following:

     * SOURCE_PROJECT_ID: The ID of the source project for the new disk.
     * SOURCE_ZONE: The zone for new disk.
     * DISK_NAME: A name for the new disk.
     * SNAPSHOT_NAME: The name of the snapshot.

This disk is a temporary disk that is created only to copy the snapshot across organizations.

  2. Create a snapshot in the destination project by calling the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert).

For example, to create a snapshot using the zonal disk created in the first step, use the following command:
         
         POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
         {
            "name": SNAPSHOT_NAME
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/DISK_NAME
         }
         

Replace the following:

     * DESTINATION_PROJECT_ID: The ID of the destination project for the new snapshot.
     * SNAPSHOT_NAME: A name for the snapshot.
     * SOURCE_PROJECT_ID: The ID of the project that contains the source disk.
     * SOURCE_ZONE: The zone of the source disk.
     * DISK_NAME: The name of the source disk.
  3. Delete the temporary disk created in the first step using the [`disks.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/delete).
         
         DELETE https://compute.googleapis.com/compute/v1/projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/DISK_NAME
         

Replace the following:

     * SOURCE_PROJECT_ID: The ID of the project that contains the temporary disk.
     * SOURCE_ZONE: The zone of the disk.
     * DISK_NAME: The name of the temporary disk created in step 1.



## What's next

  * Learn how to [create scheduled snapshots for disks](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).
  * Learn how to [create a disk image from your snapshot](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
