---
url: https://docs.cloud.google.com/compute/docs/images/create-custom/
title: Create custom images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:03.357788+00:00
---

# Create custom images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/create-custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create custom images Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

You can create custom images from source disks, images, snapshots, or images stored in Cloud Storage and use these images to create virtual machine (VM) instances. Custom images are ideal for situations where you have created and modified a persistent boot disk or specific image to a certain state and need to save that state for creating VMs.

Alternatively, you can use the [virtual disk import tool](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) to import boot disk images to Compute Engine from your existing systems and add them to your custom images list.

**Note:** If you want to create incremental backups of your persistent disk data, use [snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) instead.

## Before you begin

  * Read the [Images](https://docs.cloud.google.com/compute/docs/images) document.
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




## Required roles and permissions

To get the permissions that you need to create a custom image, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a custom image. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a custom image:

  * `compute.images.create`
  * To create a custom image from a disk: `compute.disks.useReadOnly` on the disk 
  * To create a custom image from an existing image: `compute.images.useReadOnly` on the source image 
  * To create a custom image from a standard or archive snapshot: `compute.snapshots.useReadOnly` on the source snapshot 
  * To add a label to the new image: `compute.images.setLabels` on the label 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a custom image

This section describes how to create a custom image on a Linux VM. For information about creating a Windows image, see [Creating a Windows image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image).

### Select an image storage location

When creating a custom image, you can specify the image's [Cloud Storage](https://docs.cloud.google.com/storage/docs/locations) location, excluding dual-region locations. By specifying the image storage location, you can meet your regulatory and compliance requirements for data locality as well as your high availability needs by providing redundancy across regions. To create, modify, and delete images stored in Cloud Storage, you must have [`roles/compute.storageAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.storageAdmin).

The storage location feature is optional. If you don't select a location, Compute Engine stores your image in the multi-region closest to the image source. For example, when you create an image from a source disk that is located in `us-central1` and if you don't specify a location for the custom image, then Compute Engine stores the image in the `us` multi-region.

If the image is not available in a region where you are creating a VM, Compute Engine caches the image in that region the first time you create a VM.

To see the location where an image is stored, use the [`images describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe) command from `gcloud compute`:
    
    
    gcloud compute images describe IMAGE_NAME \
        --project=PROJECT_ID

Replace the following:

  * IMAGE_NAME: the name of your image.

  * PROJECT_ID: the project ID to which the image belongs.




All of your existing images prior to this feature launch remain where they are, the only change is that you can view the image location of all your images. If you have an existing image you want to move, you must recreate it in the new location.

### Prepare your VM for an image

You can create an image from a disk even while it is attached to a running VM. However, your image is more reliable if you put the VM in a state that is easier for the image to capture. This section describes how to prepare your boot disk for the image.

#### Minimize writing data to the persistent disk

Use one of the following processes to reduce the disk writes:

  * [Stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance) so that it can shut down and stop writing any data to the persistent disk.

  * If you can't stop your VM before you create the image, minimize the amount of writes to the disk and sync your file system. To minimize writing to your persistent disk, follow these steps:

    1. Pause apps or operating system processes that write data to that persistent disk.
    2. Run an app flush to disk if necessary. For example, MySQL has a [`FLUSH`](http://dev.mysql.com/doc/refman/5.7/en/flush.html) statement. Other apps might have similar processes.
    3. Stop your apps from writing to your persistent disk.
    4. Run `sudo sync`.



#### Disable the auto-delete option for the disk

By default, the auto-delete option is enabled on the boot disks. Before creating an image from a disk, disable auto-delete to prevent the disk from being automatically deleted when you delete the VM. 

To disable auto-delete for the disk, use one of the following methods:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM that you're using as the source for creating an image.

The **VM instance details** page displays.

  3. Click **Edit**.

  4. In the **Boot disk** section, for the **Deletion rule** , check that the **Keep disk** option is selected.

  5. Click **Save**.




###  gcloud 

In the Google Cloud CLI, use the [`gcloud compute instances set-disk-auto-delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete) to disable the auto-delete option for the disk.
    
    
    gcloud compute instances set-disk-auto-delete VM_NAME \
        --no-auto-delete \
        --disk=SOURCE_DISK
    

Replace the following:

  * `VM_NAME`: the name of your VM instance.
  * `SOURCE_DISK`: the name of the disk from which you want to create the image.



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

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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

To set the auto-delete option of a disk, make a `POST` request to the [`instances.setDiskAutoDelete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setDiskAutoDelete).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setDiskAutoDelete?autoDelete=false&deviceName=SOURCE_DISK
    

Replace the following:

  * `PROJECT_ID`: the project ID to which the source VM belongs.
  * `ZONE`: the zone where the source VM is located.
  * `VM_NAME`: the name of the source VM.
  * `SOURCE_DISK`: the device name of the disk from which you want to create the image.



After you prepare the VM, create the image.

### Create the image

You can create disk images from the following sources: 

  * A persistent disk, even while that disk is attached to a VM
  * A snapshot of a persistent disk
  * Another image in your project
  * An image that is shared from another project
  * A [compressed RAW image](https://docs.cloud.google.com/compute/docs/import/import-existing-image#create_image_file) in Cloud Storage



You can create a disk image once every 10 minutes. If you want to issue a burst of requests to create a disk image, you can issue at most 6 requests in 60 minutes. For more information, see [Snapshot frequency limits](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#freq_limits).

###  Console 

  1. In the Google Cloud console, go to the **Create an image** page.

[Go to Create an image](https://console.cloud.google.com/compute/imagesAdd)

  2. Specify the **Name** of your image.

  3. Specify the **Source** from which you want to create an image. This can be a persistent disk, a snapshot, another image, or a disk.raw file in Cloud Storage.

  4. If you are creating an image from a disk attached to a running VM, select **Keep instance running** to confirm that you want to create the image while the VM is running. You can prepare your VM before creating the image.

  5. In the **Based on source disk location (default)** drop-down list, specify the location to store the image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.

  6. Optional: specify the properties for your image.

     * **Family** : the [image family](https://docs.cloud.google.com/compute/docs/images#image_families) this new image belongs to.
     * **Description** : a description for your custom image.
     * **Label** : a [label](https://docs.cloud.google.com/compute/docs/labeling-resources) to group together resources.
  7. Specify the encryption key. You can choose between a Google-owned and Google-managed encryption key, a [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) key or a [customer- supplied encryption key (CSEK)](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)) key. If no encryption key is specified, images are encrypted using a Google-owned and Google-managed encryption key.

  8. Click **Create** to create the image.




###  gcloud 

In the Google Cloud CLI, use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) to create a custom image.

**Create an image from a source disk:**

The `--force` flag is an optional flag that lets you create the image from a running instance. By default, you cannot create images from running instances. Specify this flag only if you are sure that you want to create the image while the instance is running.
    
    
    gcloud compute images create IMAGE_NAME \
        --source-disk=SOURCE_DISK \
        --source-disk-zone=ZONE \
        [--family=IMAGE_FAMILY] \
        [--storage-location=LOCATION] \
        [--force]
    

Replace the following:

  * `IMAGE_NAME`: a name for the new image
  * `SOURCE_DISK`: the disk from which you want to create the image
  * `ZONE`: the zone where the disk is located
  * `IMAGE_FAMILY`: Optional: a flag that specifies which [image family](https://docs.cloud.google.com/compute/docs/images#image_families) this image belongs to
  * `LOCATION`: Optional: a flag that lets you designate the region or multi-region where your image is stored. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



**Create an image from a source image:**
    
    
    gcloud compute images create IMAGE_NAME \
      --source-image=SOURCE_IMAGE \
      [--source-image-project=IMAGE_PROJECT] \
      [--family=IMAGE_FAMILY] \
      [--storage-location=LOCATION]
    

Replace the following:

  * `IMAGE_NAME`: a name for the new image.
  * `SOURCE_IMAGE`: the image from which you want to create the new image.
  * `IMAGE_PROJECT`: Optional: the project the source image is located in. Use this parameter if you want to copy an image from another project.
  * `IMAGE_FAMILY`: Optional: the [image family](https://docs.cloud.google.com/compute/docs/images#image_families) this new image belongs to.
  * `LOCATION`: Optional: lets you designate the region or multi-region where your image is stored. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



**Create an image from a snapshot:**
    
    
    gcloud compute images create IMAGE_NAME \
        --source-snapshot=SOURCE_SNAPSHOT \
        [--storage-location=LOCATION]
    

Replace the following:

  * `IMAGE_NAME`: a name for the new image
  * `SOURCE_SNAPSHOT`: the snapshot from which you want to create the image
  * `LOCATION`: Optional: a flag that lets you designate the region or multi-region where your image is stored. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



**View an image location:**

Use the [`gcloud compute images describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe) to view an image location. 
    
    
    gcloud compute images describe IMAGE_NAME

Replace `IMAGE_NAME` with the name of your image that you want to review.

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
    )
    
    // Creates a disk image from an existing disk
    func createImageFromDisk(
    	w io.Writer,
    	projectID, zone, sourceDiskName, imageName string,
    	storageLocations []string,
    	forceCreate bool,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-central1-a"
    	// sourceDiskName := "your_disk_name"
    	// imageName := "my_image"
    	// // If storageLocations empty, automatically selects the closest one to the source
    	// storageLocations = []string{}
    	// // If forceCreate is set to `true`, proceeds even if the disk is attached to
    	// // a running instance. This may compromise integrity of the image!
    	// forceCreate = false
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// Get the source disk
    	source_req := &computepb.GetDiskRequest{
    		Disk:    sourceDiskName,
    		Project: projectID,
    		Zone:    zone,
    	}
    
    	disk, err := disksClient.Get(ctx, source_req)
    	if err != nil {
    		return fmt.Errorf("unable to get source disk: %w", err)
    	}
    
    	// Create the image
    	req := computepb.InsertImageRequest{
    		ForceCreate: &forceCreate,
    		ImageResource: &computepb.Image{
    			Name:             &imageName,
    			SourceDisk:       disk.SelfLink,
    			StorageLocations: storageLocations,
    		},
    		Project: projectID,
    	}
    
    	op, err := imagesClient.Insert(ctx, &req)
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk image %s created\n", imageName)
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[InsertImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateImage {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Project ID or project number of the Cloud project you use.
        String project = "your-project-id";
        // Zone of the disk you copy from.
        String zone = "europe-central2-b";
        // Name of the source disk you copy from.
        String sourceDiskName = "source-disk-name";
        // Name of the image you want to create.
        String imageName = "your-image-name";
        // Storage location for the image. If the value is undefined,
        // function will store the image in the multi-region closest to your image's source location.
        String storageLocation = "eu";
        // Create the image even if the source disk is attached to a running instance.
        boolean forceCreate = false;
    
        createImage(project, zone, sourceDiskName, imageName, storageLocation, forceCreate);
      }
    
      // Creates a new disk image from the specified source disk.
      public static void createImage(String project, String zone, String sourceDiskName,
          String imageName, String storageLocation, boolean forceCreate)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create();
            [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create();
            [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = disksClient.get(project, zone, sourceDiskName);
    
          // Getting instances where source disk is attached.
          for (String fullInstanceName : disk.[getUsersList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getUsersList__)()) {
            Map<String, String> instanceInfo = parseInstanceName(fullInstanceName);
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(instanceInfo.get("instanceProjectId"),
                instanceInfo.get("instanceZone"), instanceInfo.get("instanceName"));
    
            // Сheck whether the instances are stopped.
            if (!Arrays.asList("TERMINATED", "STOPPED").contains(instance.getStatus())
                && !forceCreate) {
              throw new IllegalStateException(
                  String.format(
                      "Instance %s should be stopped. For Windows instances please stop the instance "
                          + "using GCESysprep command. For Linux instances just shut it down normally."
                          + " You can suppress this error and create an image of the disk by setting "
                          + "'forceCreate' parameter to true (not recommended). "
                          + "More information here: "
                          + "* https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image#api"
                          + "* https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#prepare_instance_for_image",
                      instanceInfo.get("instanceName")));
            }
          }
    
          if (forceCreate) {
            System.out.println(
                "Warning: forceCreate option compromise the integrity of your image. "
                    + "Stop the instance before you create the image if possible.");
          }
    
          // Create Image.
          I[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html)image = I[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html)newBuilder()
              .setName(imageName)
              .setSourceDisk(String.format("/zones/%s/disks/%s", zone, sourceDiskName))
              .addStorageLocations(storageLocation.isEmpty() ? "" : storageLocation)
              .build();
    
          I[InsertImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.html)insertImageRequest = I[InsertImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.html)newBuilder()
              .setProject(project)
              .s[setForceCreate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.Builder.html#com_google_cloud_compute_v1_InsertImageRequest_Builder_setForceCreate_boolean_)forceCreate)
              .setImageResource(image)
              .build();
    
          O[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html)response = imagesClient.insertAsync(insertImageRequest).get(5, TimeUnit.MINUTES);
    
          if (rresponse.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)() {
            System.out.println("Image creation failed ! ! " + response);
            return;
          }
    
          System.out.println("Image created.");
        }
      }
    
    
      public static Map<String, String> parseInstanceName(String name) {
        String[] parsedName = name.split("/");
        int splitLength = parsedName.length;
    
        if (splitLength < 5) {
          throw new IllegalArgumentException(
              "Provide correct instance name in the following format: "
                  + "https://www.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances/INSTANCE_NAME");
        }
    
        return new HashMap<>() {
          {
            put("instanceName", parsedName[splitLength - 1]);
            put("instanceZone", parsedName[splitLength - 3]);
            put("instanceProjectId", parsedName[splitLength - 5]);
          }
        };
      }
    
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    import warnings
    
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
    
    
    STOPPED_MACHINE_STATUS = (
        [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Instance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Instance.html).Status.TERMINATED.name,
        [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Instance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Instance.html).Status.STOPPED.name,
    )
    
    
    def create_image_from_disk(
        project_id: str,
        zone: str,
        source_disk_name: str,
        image_name: str,
        storage_location: str | None = None,
        force_create: bool = False,
    ) -> compute_v1.Image:
        """
        Creates a new disk image.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            zone: zone of the disk you copy from.
            source_disk_name: name of the source disk you copy from.
            image_name: name of the image you want to create.
            storage_location: storage location for the image. If the value is undefined,
                function will store the image in the multi-region closest to your image's
                source location.
            force_create: create the image even if the source disk is attached to a
                running instance.
    
        Returns:
            An Image object.
        """
        image_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ImagesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html)()
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        # Get source disk
        disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=project_id, zone=zone, disk=source_disk_name)
    
        for disk_user in disk.users:
            instance_name = disk_user.split("/")[-1]
            instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
                project=project_id, zone=zone, instance=instance_name
            )
            if instance.status in STOPPED_MACHINE_STATUS:
                continue
            if not force_create:
                raise RuntimeError(
                    f"Instance {disk_user} should be stopped. For Windows instances please "
                    f"stop the instance using `GCESysprep` command. For Linux instances just "
                    f"shut it down normally. You can supress this error and create an image of"
                    f"the disk by setting `force_create` parameter to true (not recommended). \n"
                    f"More information here: \n"
                    f" * https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image#api \n"
                    f" * https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#prepare_instance_for_image"
                )
            else:
                warnings.warn(
                    f"Warning: The `force_create` option may compromise the integrity of your image. "
                    f"Stop the {disk_user} instance before you create the image if possible."
                )
    
        # Create image
        image = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Image](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Image.html)()
        image.source_disk = disk.self_link
        image.name = image_name
        if storage_location:
            image.storage_locations = [storage_location]
    
        operation = image_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html#google_cloud_compute_v1_services_images_ImagesClient_insert)(project=project_id, image_resource=image)
    
        wait_for_extended_operation(operation, "image creation from disk")
    
        return image_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html#google_cloud_compute_v1_services_images_ImagesClient_get)(project=project_id, image=image_name)
    
    

###  REST 

Make a `POST` request to the [`images().insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert), a URL in the request body that points to the source object from which you want to create the image. Specify URLs to your resources using your own project ID and resource names.

**Create an image from a persistent disk:**
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    
    {
      "name": "IMAGE_NAME",
      "sourceDisk": "/zones/ZONE/disks/SOURCE_DISK",
      ("storageLocations": "LOCATION",)
      ("forceCreate": "TRUE")
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID to which the image belongs.
  * `IMAGE_NAME`: a name for the new image that you want to create.
  * `ZONE`: the zone where the source disk is located.
  * `SOURCE_DISK`: the disk from which you want to create the image.
  * `LOCATION`: Optional: the storage location of your image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



The optional `forceCreate` parameter lets you create the image from a running VM. Specify `TRUE` only if you are sure that you want to create the image from a running VM. The `forceCreate` default setting is `FALSE`.

**Create an image from another image:**
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    
    {
      "name": "IMAGE_NAME",
      "sourceImage": "/global/images/SOURCE_IMAGE",
      ("storageLocations": "LOCATION")
    }
    

Replace the following:

  * `PROJECT_ID`: the project to which the image belongs.
  * `IMAGE_NAME`: a name for the new image that you want to create.
  * `SOURCE_IMAGE`: the image from which you want to create the image.
  * `LOCATION`: Optional: the storage location of your image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



**Create an image from a snapshot:**
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    {
      "name": "IMAGE_NAME",
      "sourceSnapshot": "(/SOURCE_PROJECT_ID)/global/snapshots/SOURCE_SNAPSHOT",
      ("storageLocations": "LOCATION")
    }
    

Replace the following:

  * `PROJECT_ID`: the project to which the image belongs.
  * `IMAGE_NAME`: a name for the new image that you want to create.
  * `SOURCE_PROJECT_ID`: Optional: the project the snapshot is located in. You must have permission to access the snapshot resource in that project.
  * `SOURCE_SNAPSHOT`: the snapshot from which you want to create the image.
  * `LOCATION`: Optional: the storage location of your image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



For more information about adding images, see the [images reference](https://docs.cloud.google.com/compute/docs/reference/latest/images/insert).

### Share the image

After creating a custom image, you can [share it across projects](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images#share-images-%0Awithin-organization). If you allow users from another project to use your custom images, then they can [access these images by specifying the image project](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images#accessing_images) in their request.

## Enable guest operating system features

Use guest operating system (OS) features to configure the following networking, security, storage, and OS options on custom images. Custom images with these configured features are used as boot disks.

###  gcloud 

Use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) with the `--guest-os-features` flag to create a new custom image from an existing custom image.
    
    
    gcloud compute images create IMAGE_NAME \
        --source-image=SOURCE_IMAGE \
        [--source-image-project=IMAGE_PROJECT] \
        --guest-os-features="FEATURES,..." \
        [--storage-location=LOCATION]
    

Replace the following:

  * `IMAGE_NAME`: the name for the new image
  * `SOURCE_IMAGE`: an image to base the new image on
  * `IMAGE_PROJECT`: Optional: the project containing the source image

Use this parameter to copy an image from another project.

  * `FEATURES`: guest OS tags to enable features for VMs that you create from images

To add multiple values, use commas to separate values. Set to one or more of the following values:

    * **`VIRTIO_SCSI_MULTIQUEUE`.** Use on local SSD devices as an alternative to NVMe. For more information about images that support SCSI, see [Choosing an interface.](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface)

For Linux images, you can enable multi-queue SCSI on local SSD devices on images with kernel versions 3.17 or later. For Windows images, you can enable multi-queue SCSI on local SSD devices on images with Compute Engine Windows driver [ version 1.2](https://github.com/GoogleCloudPlatform/compute-windows-drivers/releases/tag/1.2.0.1621). 

    * **`WINDOWS`.** Tag Windows Server custom boot images as Windows images. 
    * **`MULTI_IP_SUBNET`.** Configure interfaces with a netmask other than `/32`. For more information about configuring netmasks, see [ Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks). 
    * **`UEFI_COMPATIBLE`.** Boot with [ UEFI firmware](https://wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#UEFI_booting) and the following [ Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features: 
      * [ Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot): disabled by default 
      * [ Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm): enabled by default 
      * [ Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring): enabled by default 
    * **`GVNIC`.** Support higher network bandwidths of up to [ 50 Gbps to 100 Gbps speeds](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus#high-bandwidth). For more information, see [ Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
    * **`IDPF`.** Support Intel Infrastructure Data Path Function (IDPF) network interfaces. 
    * **`SEV_CAPABLE` or `SEV_SNP_CAPABLE`.** Use these tags if you want to use your image on a [ Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance with AMD Secure Encrypted Virtualization (SEV) or AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP) support. To check if your kernel supports AMD SEV or AMD SEV-SNP, see [ Linux kernel details](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images#kernel-details). 
    * **`SEV_LIVE_MIGRATABLE_V2`.** Use this tag if you want to use your image on a [ Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance that supports [ live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration) on AMD SEV. To check if your kernel supports live migration, see [ Linux kernel details](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images#kernel-details). 
    * **`TDX_CAPABLE`.** Use this tag if you want to use your image on a [ Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance with Intel Trust Domain Extensions (TDX) support. To check if your kernel supports Intel TDX, see [ Linux kernel details](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images#kernel-details). 


* `LOCATION`: Optional: region or multi-region in which to store the image

For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.

###  REST 

Use the [`images().insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/images/insert) with the `guestOsFeatures` flag to create a new custom image from an existing custom image.
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    
    {
     "name": "IMAGE_NAME",
     "sourceImage": "(projects/IMAGE_PROJECT)/global/images/SOURCE_IMAGE",
     ("storageLocations": "LOCATION",)
     "guestOsFeatures": [
      {
       "type": "FEATURES"
      }
     ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the new image
  * `IMAGE_NAME`: a name for the new image
  * `IMAGE_PROJECT`: Optional: the project containing the source image

Use this parameter to copy an image from another project.

  * `SOURCE_IMAGE`: the image to base the new image on

  * `LOCATION`: Optional: a region or multi-region in which to store the image

For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.

  * `FEATURES`: guest OS tags to enable features for VMs that you create from images

To add multiple values, use commas to separate values. Set to one or more of the following values:

    * **`VIRTIO_SCSI_MULTIQUEUE`.** Use on local SSD devices as an alternative to NVMe. For more information about images that support SCSI, see [Choosing an interface.](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface)

For Linux images, you can enable multi-queue SCSI on local SSD devices on images with kernel versions 3.17 or later. For Windows images, you can enable multi-queue SCSI on local SSD devices on images with Compute Engine Windows driver [ version 1.2](https://github.com/GoogleCloudPlatform/compute-windows-drivers/releases/tag/1.2.0.1621). 

    * **`WINDOWS`.** Tag Windows Server custom boot images as Windows images. 
    * **`MULTI_IP_SUBNET`.** Configure interfaces with a netmask other than `/32`. For more information about configuring netmasks, see [ Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks). 
    * **`UEFI_COMPATIBLE`.** Boot with [ UEFI firmware](https://wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#UEFI_booting) and the following [ Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features: 
      * [ Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot): disabled by default 
      * [ Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm): enabled by default 
      * [ Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring): enabled by default 
    * **`GVNIC`.** Support higher network bandwidths of up to [ 50 Gbps to 100 Gbps speeds](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus#high-bandwidth). For more information, see [ Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). 
    * **`IDPF`.** Support Intel Infrastructure Data Path Function (IDPF) network interfaces. 
    * **`SEV_CAPABLE` or `SEV_SNP_CAPABLE`.** Use these tags if you want to use your image on a [ Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance with AMD Secure Encrypted Virtualization (SEV) or AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP) support. To check if your kernel supports AMD SEV or AMD SEV-SNP, see [ Linux kernel details](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images#kernel-details). 
    * **`SEV_LIVE_MIGRATABLE_V2`.** Use this tag if you want to use your image on a [ Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance that supports [ live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration) on AMD SEV. To check if your kernel supports live migration, see [ Linux kernel details](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images#kernel-details). 
    * **`TDX_CAPABLE`.** Use this tag if you want to use your image on a [ Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) instance with Intel Trust Domain Extensions (TDX) support. To check if your kernel supports Intel TDX, see [ Linux kernel details](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images#kernel-details). 



### Avoid sensitive information in UEFI variables

Unified Extensible Firmware Interface (UEFI) variables are key-value pair variables used by the UEFI firmware during boot time to boot the operating system of a VM. Unlike physical machines, where the variables are stored on a hardware chip, Compute Engine virtualizes storage of these variables. As such, in many operating systems, all applications and users can reach these variables and access this information.

Because of this reason, Google strongly recommends that you don't write or store sensitive or personal identifiable information such as passwords or private keys to UEFI variables.

## Considerations for Arm images

Google offers the [A4X, C4A, and Tau T2A](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute) machine series, which run on Arm CPU platforms. You can start a VM with one of these machine series and then use that source VM to create an Arm image. The process for creating a custom Arm image is identical to creating an x86 image.

To help your users differentiate between Arm and x86 images, Arm images will have an `architecture` field set to `ARM64`. Possible values for this field are:

  * `ARCHITECTURE_UNSPECIFIED`
  * `X86_64`
  * `ARM64`



Image users can then filter on this field to find x86 or Arm-based images.

## What's next

  * [Share your private image](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects) with other projects.
  * Learn how to [import disks, images, and VM instances](https://docs.cloud.google.com/compute/docs/import).
  * Learn how to [export an image to Cloud Storage](https://docs.cloud.google.com/compute/docs/images/export-image).
  * Learn how to [start a VM from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#creating_an_instance_from_a_custom_image).
  * Learn how to [set the image version in an image family](https://docs.cloud.google.com/compute/docs/images/set-version-custom).
  * Learn how to [deprecate a custom image](https://docs.cloud.google.com/compute/docs/images/deprecate-custom).
  * Learn how to [delete a custom image](https://docs.cloud.google.com/compute/docs/images/delete-custom).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
