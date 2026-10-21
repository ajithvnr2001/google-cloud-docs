---
url: https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk/
title: Modify a Persistent Disk or Google Cloud Hyperdisk's settings \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:35:04.243033+00:00
---

# Modify a Persistent Disk or Google Cloud Hyperdisk's settings  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Modify a Persistent Disk or Google Cloud Hyperdisk's settings Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You can use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) and [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) volumes as boot disks and data disks for Compute Engine instances.

This document explains how to complete the following tasks:

  * Convert a disk to a different Persistent Disk or Hyperdisk type by creating a new disk that contains the original disk's data. Depending on the new disk type you choose, you can gain the following benefits:

    * Reach higher performance levels if you choose a faster disk type
    * Reduce costs if you choose a more cost-efficient disk type
  * Configure whether Compute Engine deletes a compute instance's boot or data disks when you delete the instance. You incur costs for a disk until you delete it, even if the disk isn't attached to any instances. You can reduce costs by enabling automatic deletion of disks that you won't need after the attached instance is deleted.

  * Update the access mode of a Hyperdisk volume to enable or disable access to the volume from multiple Compute Engine instances.




To change the size of a Hyperdisk or Persistent Disk volume, see [Modify the size or provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks) and [Modify the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk), respectively.

## Change the type of a Persistent Disk volume

At times, you need to change the type of a particular Persistent Disk volume to meet your performance or pricing requirements. For example, you might want to change a workload's data disk from a Standard Persistent Disk to a Balanced Persistent Disk.

You can't directly change the type of an existing Persistent Disk volume. You must create a snapshot of the existing disk and then use that snapshot to create a disk of the new type.

To change a Persistent Disk volume (the source disk) to another Persistent Disk type (the new disk), use the following process:

  1. If the source disk is attached to a compute instance, [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) of the source disk.

  3. Create the new disk [from the snapshot of the source disk](https://docs.cloud.google.com/compute/docs/disks/restore-and-delete-snapshots).

  4. To start using the new disk, detach the source disk from the instance and attach the new disk that you just created.

     * If the source disk is a boot disk:

       1. [Detach the source disk from the instance](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk).
       2. [Use the new disk as the instance's boot disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#attach_disk).
     * If the source disk is a non-boot disk:

       1. [Detach the source disk from the instance](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_non_boot_disk).
       2. [Attach the new disk to the instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks).
  5. [Start the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm).

  6. Verify that new disk works as expected.

  7. After you test the new disk, you can [delete the snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot) and [delete the source disk](https://docs.cloud.google.com/compute/docs/samples/compute-disk-delete). You continue to incur charges for the source disk and snapshot until you delete them.




## Modify a disk's auto-delete setting

To prevent accidental data loss, you can control whether or not Compute Engine automatically deletes any of the Google Cloud Hyperdisk or Persistent Disk volumes that are attached to an instance when you delete the instance. Local SSD disks are always deleted with the instance.

The `autoDelete` property for each Google Cloud Hyperdisk or Persistent Disk volume that is attached to the instance controls this behavior.

To keep a specific volume when you delete the instance, set the `autoDelete` property for the volume to `false`. Conversely, to delete a volume when you delete the instance, set the `autoDelete` property to `true`.

**Important:** If you opt to keep a disk after the instance is deleted, then you must [manually delete the disk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete) when you no longer need the disk. You incur costs for the disk until you delete it, even if the disk isn't attached to any instances.

You can't automatically delete a disk if the disk is attached to the instance in read-only mode.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.setDiskAutoDelete` on the instance
  * `compute.disks.update` on the disk



###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instance that has the disks associated with it.

  3. Click the instance name. The **VM instance details** page appears.

  4. Click mode_edit **Edit**.

  5. To update the auto-delete setting for your disks, in the **Storage** section, follow these steps:

     * For the boot disk, under the heading **Boot disk** , select the boot disk's **Deletion Rule**.
     * For each additional disk attached to the instance, find the disk in the **Additional disks** section, then follow these steps: 
       1. Click mode_edit **Edit disk**. The **Existing disk** pane opens.
       2. Under **Attachment mode** set the disk's **Deletion Rule**. To save the setting for the disk and close the pane, click **Save**.
  6. To save your changes, click **Save**.




###  gcloud 

Set the auto-delete state of a disk with the [`gcloud compute instances set-disk-auto-delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete).

To keep the disk when you delete the instance, specify the `--no-auto-delete` flag. To delete the disk, specify the `--auto-delete` flag.

If the instance has multiple disks attached, then you must run the command for each disk attached to the instance.
    
    
    gcloud compute instances set-disk-auto-delete INSTANCE_NAME \
      AUTO_DELETE_SETTING \
      --disk DISK_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `AUTO_DELETE_SETTING`: whether or not to automatically delete the disk. Specify `--no-auto-delete` to keep the disk after deleting the compute instance, and `--auto-delete` to delete the disk at the same time as the instance.
  * `DISK_NAME`: the name of the disk.



###  Go 

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // setDiskAutodelete sets the autodelete flag of a disk to given value.
    func setDiskAutoDelete(
    	w io.Writer,
    	projectID, zone, instanceName, diskName string, autoDelete bool,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b"
    	// instanceName := "your_instance_name"
    	// diskName := "your_disk_name"
    	// autoDelete := true
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	getInstanceReq := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, getInstanceReq)
    	if err != nil {
    		return fmt.Errorf("unable to get instance: %w", err)
    	}
    
    	diskExists := false
    
    	for _, disk := range instance.GetDisks() {
    		if disk.GetDeviceName() == diskName {
    			diskExists = true
    			break
    		}
    	}
    
    	if !diskExists {
    		return fmt.Errorf(
    			"instance %s doesn't have a disk named %s attached",
    			instanceName,
    			diskName,
    		)
    	}
    
    	req := &computepb.SetDiskAutoDeleteInstanceRequest{
    		Project:    projectID,
    		Zone:       zone,
    		Instance:   instanceName,
    		DeviceName: diskName,
    		AutoDelete: autoDelete,
    	}
    
    	op, err := instancesClient.SetDiskAutoDelete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to set disk autodelete field: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "disk autoDelete field updated.\n")
    
    	return nil
    }
    

###  Java 

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SetDiskAutodelete {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
    
        // The zone of the disk that you want to modify.
        String zone = "europe-central2-b";
    
        // Name of the instance the disk is attached to.
        String instanceName = "YOUR_INSTANCE_NAME";
    
        // The name of the disk for which you want to modify the autodelete flag.
        String diskName = "YOUR_DISK_NAME";
    
        // The new value of the autodelete flag.
        boolean autoDelete = true;
    
        setDiskAutodelete(projectId, zone, instanceName, diskName, autoDelete);
      }
    
      // Sets the autodelete flag of a disk to given value.
      public static void setDiskAutodelete(String projectId, String zone, String instanceName,
          String diskName, boolean autoDelete)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          // Retrieve the instance given by the instanceName.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(projectId, zone, instanceName);
    
          // Check if the instance contains a disk that matches the given diskName.
          boolean diskNameMatch = instance.[getDisksList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getDisksList__)()
              .stream()
              .anyMatch(disk -> disk.getDeviceName().equals(diskName));
    
          if (!diskNameMatch) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(
                String.format("Instance %s doesn't have a disk named %s attached", instanceName,
                    diskName));
          }
    
          // Create the request object.
          [SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest.html) request = [SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstance(instanceName)
              .setDeviceName(diskName)
              // Update the autodelete property.
              .setAutoDelete(autoDelete)
              .build();
    
          // Wait for the update instance operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.[setDiskAutoDeleteAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_setDiskAutoDeleteAsync_com_google_cloud_compute_v1_SetDiskAutoDeleteInstanceRequest_)(request)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Failed to update Disk autodelete field!" + response);
            return;
          }
          System.out.println(
              "Disk autodelete field updated. Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Node.js 

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const diskName = 'YOUR_DISK_NAME';
    // const autoDelete = true;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function setDiskAutodelete() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instance] = await instancesClient.get({
        project: projectId,
        zone,
        instance: instanceName,
      });
    
      if (!instance.disks.some(disk => disk.deviceName === diskName)) {
        throw new Error(
          `Instance ${instanceName} doesn't have a disk named ${diskName} attached.`
        );
      }
    
      const [response] = await instancesClient.setDiskAutoDelete({
        project: projectId,
        zone,
        instance: instanceName,
        deviceName: diskName,
        autoDelete,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the update instance operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Disk autoDelete field updated.');
    }
    
    setDiskAutodelete();

###  Python 

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
    
    
    def set_disk_autodelete(
        project_id: str, zone: str, instance_name: str, disk_name: str, autodelete: bool
    ) -> None:
        """
        Set the autodelete flag of a disk to given value.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone in which is the disk you want to modify.
            instance_name: name of the instance the disk is attached to.
            disk_name: the name of the disk which flag you want to modify.
            autodelete: the new value of the autodelete flag.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
        instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
            project=project_id, zone=zone, instance=instance_name
        )
    
        for disk in instance.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html):
            if disk.device_name == disk_name:
                break
        else:
            raise RuntimeError(
                f"Instance {instance_name} doesn't have a disk named {disk_name} attached."
            )
    
        disk.auto_delete = autodelete
    
        operation = instance_client.[update](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_update)(
            project=project_id,
            zone=zone,
            instance=instance_name,
            instance_resource=instance,
        )
    
        wait_for_extended_operation(operation, "disk update")
    
    

###  REST 

To set the auto-delete state using the API, make a `POST` request to the [instances.setDiskAutoDelete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setDiskAutoDelete) method. Use the `autoDelete` parameter to indicate whether to delete the disk.

If the instance has multiple disks attached, then you must make a request for each disk that's attached to the instance.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/setDiskAutoDelete?deviceName=DISK_NAME,autoDelete=AUTO_DELETE_OPTION
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your instance and disk are located.
  * `INSTANCE_NAME`: the name of your instance
  * `DISK_NAME`: the name of the disk attached to the instance.
  * `AUTO_DELETE_OPTION`: whether or not to automatically delete the disk when you delete the instance. To delete the disk, set to `true`. Set to `false` to keep the disk after deleting the instance.



## Access mode for Hyperdisk volumes

To share a Hyperdisk volume between multiple instances and grant each instance concurrent read-only or read-write access to the volume, you must set the volume's access mode to read-only or multi-writer mode, respectively.

On the other hand, to perform certain actions, like creating an image, on a Hyperdisk volume that's in read-only or multi-writer mode, you must set its access mode to single-writer.

This section describes how to set a disk's access mode.

To learn more about disk sharing, see [Share disks between instances](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

### Limitations for access mode changes

  * You can't set a disk's access mode unless you [detach the disk from all instances](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk).

  * Hyperdisk Throughput volumes only support single-writer mode and you can't set the access mode for a Hyperdisk Throughput volume.

  * For Hyperdisk Balanced, Hyperdisk Extreme, and Hyperdisk Balanced High Availability volumes, you can only enable or disable multi-writer mode. You can't set the access mode to read-only.

  * For Hyperdisk ML volumes, you can only set the access mode to read-only. Hyperdisk ML volumes don't support multi-writer mode.

  * You can't modify a Hyperdisk ML volume's access mode after you set it to read-only.




### Required roles and permissions

To get the permission that you need to set a disk's access mode, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.disks.update` permission, which is required to set a disk's access mode. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set the access mode of a Hyperdisk volume

Before you set a disk's access mode, you must [detach the disk from all instances](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk).

You can set the access mode with the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the list of disks in your project, click the name of the Hyperdisk volume that you want to modify.

  3. On the disk details page, click edit**Edit**.

  4. In the **Access mode** field, select the access mode that you want:

     * To enable read-only mode, select **Multiple VMs read only**.
     * To enable multi-writer mode, select **Multiple VMs read-write**.
     * (Default) To enable single-writer mode, select **Single VM read-write**.
  5. To apply your changes, click **Save**.




###  gcloud 

Run the [`disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update) and specify the access mode by using `--access-mode` flag.
    
    
    gcloud compute disks update DISK_NAME  \
       --access-mode=DISK_ACCESS_MODE
    

Replace the following:

  * DISK_NAME: the name of the Hyperdisk volume that you are modifying.
  * DISK_ACCESS_MODE: how instances can access the data on the disk. Supported values are: 
    * `READ_ONLY_MANY`, for read-only access from multiple instances.
    * `READ_WRITE_MANY`, for read-write access from multiple instances.
    * (Default) `READ_WRITE_SINGLE`, for read-write access from one instance.



###  REST 

Construct a `PATCH` request to the [`compute.disks.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/update). In the request body, set the access mode by including the `accessMode` parameter.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/update
    {
       "accessMode": "DISK_ACCESS_MODE"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your Hyperdisk volume is located.
  * `DISK_NAME`: the name of the Hyperdisk volume to modify.
  * `DISK_ACCESS_MODE`: how instances can access the data on the disk. Supported values are: 
    * `READ_ONLY_MANY`, for read-only access from multiple instances.
    * `READ_WRITE_MANY`, for read-write access from multiple instances.
    * `READ_WRITE_SINGLE`, for single-writer mode, that is, read-write access from one instance.



## Troubleshooting

To find methods for diagnosing and resolving issues related to full disks and disk resizing, see [Troubleshooting full disks and disk resizing](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-full-resize).

## What's next

  * Learn how to regularly [back up your disks using snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) to prevent unintended data loss.
  * Use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) for synchronous replication between two zones.
  * [Mount a RAM disk on your instance](https://docs.cloud.google.com/compute/docs/disks/mount-ram-disks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
