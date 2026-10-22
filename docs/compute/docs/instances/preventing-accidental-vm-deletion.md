---
url: https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion/
title: Prevent accidental VM deletion \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:11.325702+00:00
---

# Prevent accidental VM deletion  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Prevent accidental VM deletion Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to protect specific VM instances from deletion by setting the `deletionProtection` property on an Instance resource. To learn more about VM instances, read the [Instances](https://docs.cloud.google.com/compute/docs/instances) documentation.

As part of your workload, there might be certain VM instances that are critical to running your application or services, such as an instance running a SQL server, a server used as a license manager, and so on. These VM instances might need to stay running indefinitely so you need a way to protect these VMs from being deleted.

By setting the `deletionProtection` flag, a VM instance can be protected from accidental deletion. If a user attempts to delete a VM instance for which you have set the `deletionProtection` flag, the request fails. Only a user that has been granted a role with `compute.instances.create` permission can reset the flag to allow the resource to be deleted.

## Before you begin

  * Read the [Instances](https://docs.cloud.google.com/compute/docs/instances) documentation.
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

### PHP

To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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




## Specifications

  * Deletion prevention does not prevent the following actions:

    * Terminating an instance from [within the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance_through_the_os) (such as running the `shutdown` command)
    * [Stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance)
    * [Resetting an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance)
    * [Suspending an instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)
    * Instances being removed due to fraud and abuse after being detected by Google
    * Instances being removed due to [project termination](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_deleting_projects)
  * Deletion protection can be applied to both regular VMs and preemptible VMs.

  * Deletion protection cannot be applied to VMs that are part of a managed instance group but can be applied to instances that are part of unmanaged instance groups.

  * Deletion prevention cannot be specified in instance templates.




## Permissions

To perform this task, you must have been granted the following [permissions](https://docs.cloud.google.com/compute/docs/access/iam-permissions) **OR** one of the following [IAM roles](https://docs.cloud.google.com/compute/docs/access/iam) on the resource.

**Permissions**

  * `compute.instances.create`



**Roles**

  * `compute.admin`
  * `compute.instanceAdmin.v1`



## Setting deletion protection during instance creation

By default, deletion protection is disabled for your instance. Enable deletion protection using the instructions below.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Expand the **Advanced options** section and do the following:

     1. Expand the **Management** section.
     2. Select the **Enable deletion protection** checkbox.
  3. Continue with the VM creation process.




###  gcloud 

When [creating a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), include either the `--deletion-protection` or `no-deletion-protection` flags. Deletion protection is disabled by default so to enable deletion protection:
    
    
    gcloud compute instances create [INSTANCE_NAME] --deletion-protection
    

where `[INSTANCE_NAME]` is the name of the desired instance.

To disable deletion protection during creation:
    
    
    gcloud compute instances create [INSTANCE_NAME] --no-deletion-protection
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createInstance sends an instance creation request to the Compute Engine API
    // and waits for it to complete.
    func createInstance(w io.Writer, projectID, zone, instanceName string, deleteProtection bool) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// deleteProtection := true
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    			// Set the delete protection bit.
    			DeletionProtection: proto.Bool(deleteProtection),
    			Disks: []*computepb.AttachedDisk{
    				{
    					// Describe the size and source image of the boot disk to attach to the instance.
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:  proto.Int64(10),
    						SourceImage: proto.String("projects/debian-cloud/global/images/family/debian-12"),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    			},
    			MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/e2-small", zone)),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					// Use the default VPC network.
    					Name: proto.String("default"),
    				},
    			},
    		},
    	}
    
    	op, err := instancesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstanceDeleteProtection {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // project: project ID or project number of the Cloud project you want to use.
        // zone: name of the zone you want to use. For example: “us-west3-b”
        // instanceName: name of the new virtual machine.
        // deleteProtection: boolean value indicating if the new virtual machine should be
        // protected against deletion or not.
        String projectId = "your-project-id-or-number";
        String zone = "zone-name";
        String instanceName = "instance-name";
        boolean deleteProtection = true;
        createInstanceDeleteProtection(projectId, zone, instanceName, deleteProtection);
      }
    
      // Send an instance creation request to the Compute Engine API and wait for it to complete.
      public static void createInstanceDeleteProtection(String projectId, String zone,
          String instanceName, boolean deleteProtection)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        String machineType = String.format("zones/%s/machineTypes/e2-small", zone);
        String sourceImage = String
            .format("projects/debian-cloud/global/images/family/%s", "debian-13");
        long diskSizeGb = 10L;
        String networkName = "default";
    
        // Instance creation requires at least one persistent disk and one network interface.
        try (Inst[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html)tancesClient = Inst[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html)ate()) {
    
          Atta[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html)k =
              Atta[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html)Builder()
                  .setBoot(true)
                  .setAutoDelete(true)
                  .setType(Atta[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html)e.PERSISTENT.toString())
                  .setI[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)                // Describe the size and source image of the boot disk to attach to the instance.
                      Atta[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html)Builder()
                          .setSourceImage(sourceImage)
                          .setDiskSizeGb(diskSizeGb)
                          .build())
                  .build();
    
          // Use the default VPC network.
          Netw[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html)workInterface = Netw[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html)Builder()
              .setName(networkName)
              .build();
    
          // Collect information into the Instance object.
          Inst[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html)tanceResource =
              Inst[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html)Builder()
                  .setName(instanceName)
                  .setMachineType(machineType)
                  .addDisks(disk)
                  .addNetworkInterfaces(networkInterface)
                  // Set the "Delete protection" bit.
                  .setDeletionProtection(deleteProtection)
                  .build();
    
          System.out.printf("Creating instance: %s at %s %n", instanceName, zone);
    
          // Prepare the request to insert an instance.
          Inse[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html)ertInstanceRequest = Inse[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html)Builder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(instanceResource)
              .build();
    
          // Wait for the create operation to complete.
          Oper[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html)ponse = instancesClient.insertAsync(insertInstanceRequest)
              .get(3, TimeUnit.MINUTES);
          ;
    
          if (respresponse.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()        System.out.println("Instance creation failed ! ! " + response);
            return;
          }
          System.out.printf("Instance created : %s", instanceName);
          System.out.println("Operation Status: " + respresponse.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)()   }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const deleteProtection = true;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Send an instance creation request to the Compute Engine API and wait for it to complete.
    async function createInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
          // Set the delete protection bit.
          deletionProtection: deleteProtection,
          disks: [
            {
              // Describe the size and source image of the boot disk to attach to the instance.
              initializeParams: {
                diskSizeGb: '10',
                sourceImage:
                  'projects/debian-cloud/global/images/family/debian-11',
              },
              autoDelete: true,
              boot: true,
              type: 'PERSISTENT',
            },
          ],
          machineType: `zones/${zone}/machineTypes/e2-small`,
          networkInterfaces: [
            {
              // Use the default VPC network.
              name: 'default',
            },
          ],
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance created.');
    }
    
    createInstance();

###  Python 
    
    
    from __future__ import annotations
    
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def get_image_from_family(project: str, family: str) -> compute_v1.Image:
        """
        Retrieve the newest image that is part of a given family in a project.
    
        Args:
            project: project ID or project number of the Cloud project you want to get image from.
            family: name of the image family you want to get image from.
    
        Returns:
            An Image object.
        """
        image_client = compute_v1.ImagesClient()
        # List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
        newest_image = image_client.get_from_family(project=project, family=family)
        return newest_image
    
    
    def disk_from_image(
        disk_type: str,
        disk_size_gb: int,
        boot: bool,
        source_image: str,
        auto_delete: bool = True,
    ) -> compute_v1.AttachedDisk:
        """
        Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
        source for the new disk.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            source_image: source image to use when creating this disk. You must have read access to this disk. This can be one
                of the publicly available images or an image from one of your projects.
                This value uses the following format: "projects/{project_name}/global/images/{image_name}"
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created using the specified image.
        """
        boot_disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = source_image
        initialize_params.disk_size_gb = disk_size_gb
        initialize_params.disk_type = disk_type
        boot_disk.initialize_params = initialize_params
        # Remember to set auto_delete to True if you want the disk to be deleted when you delete
        # your VM instance.
        boot_disk.auto_delete = auto_delete
        boot_disk.boot = boot
        return boot_disk
    
    
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
    
    
    def create_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        disks: list[compute_v1.AttachedDisk],
        machine_type: str = "n1-standard-1",
        network_link: str = "global/networks/default",
        subnetwork_link: str = None,
        internal_ip: str = None,
        external_access: bool = False,
        external_ipv4: str = None,
        accelerators: list[compute_v1.AcceleratorConfig] = None,
        preemptible: bool = False,
        spot: bool = False,
        instance_termination_action: str = "STOP",
        custom_hostname: str = None,
        delete_protection: bool = False,
    ) -> compute_v1.Instance:
        """
        Send an instance creation request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            disks: a list of compute_v1.AttachedDisk objects describing the disks
                you want to attach to your new instance.
            machine_type: machine type of the VM being created. This value uses the
                following format: "zones/{zone}/machineTypes/{type_name}".
                For example: "zones/europe-west3-c/machineTypes/f1-micro"
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
                "regions/{region}/subnetworks/{subnetwork_name}"
            internal_ip: internal IP address you want to assign to the new instance.
                By default, a free address from the pool of available internal IP addresses of
                used subnet will be used.
            external_access: boolean flag indicating if the instance should have an external IPv4
                address assigned.
            external_ipv4: external IPv4 address to be assigned to this instance. If you specify
                an external IP address, it must live in the same region as the zone of the instance.
                This setting requires `external_access` to be set to True to work.
            accelerators: a list of AcceleratorConfig objects describing the accelerators that will
                be attached to the new instance.
            preemptible: boolean value indicating if the new instance should be preemptible
                or not. Preemptible VMs have been deprecated and you should now use Spot VMs.
            spot: boolean value indicating if the new instance should be a Spot VM or not.
            instance_termination_action: What action should be taken once a Spot VM is terminated.
                Possible values: "STOP", "DELETE"
            custom_hostname: Custom hostname of the new VM instance.
                Custom hostnames must conform to RFC 1035 requirements for valid hostnames.
            delete_protection: boolean value indicating if the new virtual machine should be
                protected against deletion or not.
        Returns:
            Instance object.
        """
        instance_client = compute_v1.InstancesClient()
    
        # Use the network interface provided in the network_link argument.
        network_interface = compute_v1.NetworkInterface()
        network_interface.network = network_link
        if subnetwork_link:
            network_interface.subnetwork = subnetwork_link
    
        if internal_ip:
            network_interface.network_i_p = internal_ip
    
        if external_access:
            access = compute_v1.AccessConfig()
            access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
            access.name = "External NAT"
            access.network_tier = access.NetworkTier.PREMIUM.name
            if external_ipv4:
                access.nat_i_p = external_ipv4
            network_interface.access_configs = [access]
    
        # Collect information into the Instance object.
        instance = compute_v1.Instance()
        instance.network_interfaces = [network_interface]
        instance.name = instance_name
        instance.disks = disks
        if re.match(r"^zones/[a-z\d\-]+/machineTypes/[a-z\d\-]+$", machine_type):
            instance.machine_type = machine_type
        else:
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
    
        instance.scheduling = compute_v1.Scheduling()
        if accelerators:
            instance.guest_accelerators = accelerators
            instance.scheduling.on_host_maintenance = (
                compute_v1.Scheduling.OnHostMaintenance.TERMINATE.name
            )
    
        if preemptible:
            # Set the preemptible setting
            warnings.warn(
                "Preemptible VMs are being replaced by Spot VMs.", DeprecationWarning
            )
            instance.scheduling = compute_v1.Scheduling()
            instance.scheduling.preemptible = True
    
        if spot:
            # Set the Spot VM setting
            instance.scheduling.provisioning_model = (
                compute_v1.Scheduling.ProvisioningModel.SPOT.name
            )
            instance.scheduling.instance_termination_action = instance_termination_action
    
        if custom_hostname is not None:
            # Set the custom hostname for the instance
            instance.hostname = custom_hostname
    
        if delete_protection:
            # Set the delete protection bit
            instance.deletion_protection = True
    
        # Prepare the request to insert an instance.
        request = compute_v1.InsertInstanceRequest()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        # Wait for the create operation to complete.
        print(f"Creating the {instance_name} instance in {zone}...")
    
        operation = instance_client.insert(request=request)
    
        wait_for_extended_operation(operation, "instance creation")
    
        print(f"Instance {instance_name} created.")
        return instance_client.get(project=project_id, zone=zone, instance=instance_name)
    
    
    def create_protected_instance(
        project_id: str, zone: str, instance_name: str
    ) -> compute_v1.Instance:
        """
        Create a new VM instance with Debian 10 operating system and delete protection
        turned on.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
    
        Returns:
            Instance object.
        """
        newest_debian = get_image_from_family(project="debian-cloud", family="debian-13")
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_image(disk_type, 10, True, newest_debian.self_link)]
        instance = create_instance(
            project_id, zone, instance_name, disks, delete_protection=True
        )
        return instance
    
    

###  REST 

In the API, when [creating a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), include the `deletionProtection` property in your request body. For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances
    
    {
      "name": "[INSTANCE_NAME]",
      "deletionProtection": "true",
      ...
    }
    

To disable deletion protection, set `deletionProtection` to `false`.

## Determining if an instance has deletion protection enabled

You can determine if an instance has deletion protection enabled in the `gcloud tool` or in the API.

###  Console 

  1. Go to the VM instances page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.

  3. On the **VM instances** page, pull down the **Columns** menu and enable **Deletion protection**.

![VM deletion option.](https://docs.cloud.google.com/static/compute/images/deletion-protection-column.png)

  4. A new column appears with the deletion protection icon. If a VM has deletion protection enabled, the icon appears next to the instance name.




###  gcloud 

In the gcloud CLI, run the `instances describe` command and search for the deletion protection field. For example:
    
    
    gcloud compute instances describe example-instance | grep "deletionProtection"
    

The tool returns the value of the `deletionProtection` property, either set to `true` or `false`:
    
    
    deletionProtection: false
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // getDeleteProtection prints the state of delete protection flag of given instance.
    func getDeleteProtection(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get instance: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance %s has DeleteProtection value: %v", instanceName, instance.GetDeletionProtection())
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import java.io.IOException;
    
    public class GetDeleteProtection {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // project: project ID or project number of the Cloud project you want to use.
        // zone: name of the zone you want to use. For example: “us-west3-b”
        // instanceName: name of the new virtual machine.
        String projectId = "your-project-id-or-number";
        String zone = "zone-name";
        String instanceName = "instance-name";
        getDeleteProtection(projectId, zone, instanceName);
      }
    
      // Returns the state of delete protection flag of given instance.
      public static boolean getDeleteProtection(String projectId, String zone,
          String instanceName) throws IOException {
    
        try (Inst[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html)tancesClient = Inst[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html)ate()) {
          Inst[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html)tance = instancesClient.get(projectId, zone, instanceName);
          boolean deleteProtection = instinstance.[getDeletionProtection](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getDeletionProtection__)()    System.out.printf("Retrieved Delete Protection setting for instance: %s : %s", instanceName,
              deleteProtection);
    
          return deleteProtection;
        }
      }
    }
    

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Print the state of delete protection flag of given instance.
    async function getDeleteProtection() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instance] = await instancesClient.get({
        project: projectId,
        zone,
        instance: instanceName,
      });
    
      console.log(
        `Instance ${instanceName} has deletionProtection value: ${instance.deletionProtection}`
      );
    }
    
    getDeleteProtection();

###  Python 
    
    
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def get_delete_protection(project_id: str, zone: str, instance_name: str) -> bool:
        """
        Returns the state of delete protection flag of given instance.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            instance_name: name of the virtual machine to check.
        Returns:
            The boolean value of the delete protection setting.
        """
        instance_client = comp[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)t[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)   instance = instinstance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)      project=project_id, zone=zone, instance=instance_name
        )
        return instance.deletion_protection
    
    

###  REST 

In the API, make a `GET` request and look for the `deletionProtection` field:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]
    

## Toggling deletion protection for existing instances

You can toggle deletion protection for an existing instance, irrespective of the instance's current [status](https://docs.cloud.google.com/compute/docs/instances/checking-instance-status). Specifically, you do not have to stop the instance before you can enable or disable deletion protection.

###  Console 

  1. Go to the VM instances page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.

  3. Click the name of the instance for which you want to toggle deletion protection. The instance details page displays.

  4. From the instance details page, complete the following steps:

     1. Click the **Edit** button at the top of the page.
     2. Under **Deletion Protection** , check the box to enable or uncheck the box to disable deletion protection.

![VM deletion check box.](https://docs.cloud.google.com/static/compute/images/vm-deletion-new-vm.png)

     3. Save your changes.




###  gcloud 

Using the gcloud CLI, run the `update` command with either the `--deletion-protection` or `--no-deletion-protection` flag:
    
    
    gcloud compute instances update [INSTANCE_NAME] \
        [--deletion-protection | --no-deletion-protection]
    

For example, to enable deletion protection for an instance named `example-vm`:
    
    
    gcloud compute instances update example-vm --deletion-protection
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // setDeleteProtection updates the delete protection setting of given instance.
    func setDeleteProtection(w io.Writer, projectID, zone, instanceName string, deleteProtection bool) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// deleteProtection := true
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.SetDeletionProtectionInstanceRequest{
    		Project:            projectID,
    		Zone:               zone,
    		Resource:           instanceName,
    		DeletionProtection: proto.Bool(deleteProtection),
    	}
    
    	op, err := instancesClient.SetDeletionProtection(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to set deletion protection: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance updated\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SetDeleteProtection {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // project: project ID or project number of the Cloud project you want to use.
        // zone: name of the zone you want to use. For example: “us-west3-b”
        // instanceName: name of the new virtual machine.
        // deleteProtection: boolean value indicating if the new virtual machine should be
        // protected against deletion or not.
        String projectId = "your-project-id-or-number";
        String zone = "zone-name";
        String instanceName = "instance-name";
        boolean deleteProtection = true;
        setDeleteProtection(projectId, zone, instanceName, deleteProtection);
      }
    
      // Updates the "Delete Protection" setting of given instance.
      public static void setDeleteProtection(String projectId, String zone,
          String instanceName, boolean deleteProtection)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        try (Inst[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html)tancesClient = Inst[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html)ate()) {
    
          SetD[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest.html)uest =
              SetD[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest.html)Builder()
                  .setProject(projectId)
                  .setZone(zone)
                  .setResource(instanceName)
                  .setDeletionProtection(deleteProtection)
                  .build();
    
          instancesClient.setD[setDeletionProtectionAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_setDeletionProtectionAsync_com_google_cloud_compute_v1_SetDeletionProtectionInstanceRequest_)uest).get(3, TimeUnit.MINUTES);
          ;
          // Retrieve the updated setting from the instance.
          System.out.printf("Updated Delete Protection setting: %s",
              instancesClient.get(projectId, zone, instanceName).getDeletionProtection());
        }
      }
    }
    

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const deleteProtection = True;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Update the delete protection setting of given instance.
    async function setDeleteProtection() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.setDeletionProtection({
        project: projectId,
        zone,
        // Set the delete protection bit.
        deletionProtection: deleteProtection,
        resource: instanceName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance updated.');
    }
    
    setDeleteProtection();

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
    
    
    def set_delete_protection(
        project_id: str, zone: str, instance_name: str, delete_protection: bool
    ) -> None:
        """
        Updates the delete protection setting of given instance.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            instance_name: name of the instance to update.
            delete_protection: boolean value indicating if the virtual machine should be
                protected against deletion or not.
        """
        instance_client = comp[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)t[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)    request = comp[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)D[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.SetDeletionProtectionInstanceRequest.html)   request.project = project_id
        request.zone = zone
        request.resource = instance_name
        request.deletion_protection = delete_protection
    
        operation = instinstance_client.[set_deletion_protection](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_set_deletion_protection)uest)
        wait_for_extended_operation(operation, "changing delete protection setting")
    
    

###  REST 

In the API, make a `POST` request to the `setDeletionProtection` method with the `deletionProtection` query parameter. For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]/setDeletionProtection?deletionProtection=true
    

To disable deletion protection, set `deletionProtection` to `false`. Do not provide a request body with the request.

## What's next

  * Learn how to [stop an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance).
  * [Delete your instances](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) if you no longer need them.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
