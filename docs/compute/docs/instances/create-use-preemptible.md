---
url: https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible/
title: Create and use preemptible VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:01.469279+00:00
---

# Create and use preemptible VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create and use preemptible VMs Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Spot VMs are the latest version of preemptible VMs, and we recommend using Spot VMs instead of preemptible VMs. New and existing preemptible VMs continue to be available, and preemptible VMs use the same pricing model as Spot VMs. However, Spot VMs provide new features that preemptible VMs don't support. For example, preemptible VMs can only run for up to 24 hours at a time, but Spot VMs don't have a maximum runtime unless you [limit the runtime](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime). Learn more about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) and how to [create Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot).

This page explains how to create and use a preemptible virtual machine (VM) instance. Preemptible VMs are available at a discount of up to 91% off of the default price of standard VMs. However, Compute Engine might stop (preempt) these VMs if it needs to reclaim those resources for other tasks. Preemptible VMs always stop after 24 hours. Preemptible VMs are recommended only for fault-tolerant applications that can withstand VM preemption. Make sure your application can handle preemptions before you decide to create a preemptible VM. To understand the risks and value of preemptible VMs, read the [preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) documentation.

**Caution:** Preemptible VMs are not covered by any Service Level Agreement and are excluded from the [Compute Engine SLA](https://cloud.google.com/compute/sla). For more information, see [limitations of preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible#limitations).

## Before you begin

  * Read the [Preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) documentation.
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




## Create a preemptible VM

Create a preemptible VM using the gcloud CLI or the Compute Engine API. To use the Google Cloud console, [create a Spot VM](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#create) instead.

**Note:** You cannot change the [automatic restart and host maintenance options](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#limitations) for a preemptible VM.

###  gcloud 

With `gcloud compute`, use the same `instances create` command that you would use to create a normal VM, but add the `--preemptible` flag.
    
    
    gcloud compute instances create VM_NAME --preemptible
    

where `VM_NAME` is the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM.

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createPreemtibleInstance creates a new preemptible VM instance
    // with Debian 10 operating system.
    func createPreemtibleInstance(
    	w io.Writer, projectID, zone, instanceName string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// preemptible := true
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// List of public operating system (OS) images:
    	// https://cloud.google.com/compute/docs/images/os-details.
    	newestDebianReq := &computepb.GetFromFamilyImageRequest{
    		Project: "debian-cloud",
    		Family:  "debian-12",
    	}
    	newestDebian, err := imagesClient.GetFromFamily(ctx, newestDebianReq)
    	if err != nil {
    		return fmt.Errorf("unable to get image from family: %w", err)
    	}
    
    	inst := &computepb.Instance{
    		Name: proto.String(instanceName),
    		Disks: []*computepb.AttachedDisk{
    			{
    				InitializeParams: &computepb.AttachedDiskInitializeParams{
    					DiskSizeGb:  proto.Int64(10),
    					SourceImage: newestDebian.SelfLink,
    					DiskType:    proto.String(fmt.Sprintf("zones/%s/diskTypes/pd-standard", zone)),
    				},
    				AutoDelete: proto.Bool(true),
    				Boot:       proto.Bool(true),
    			},
    		},
    		Scheduling: &computepb.Scheduling{
    			// Set the preemptible setting
    			Preemptible: proto.Bool(true),
    		},
    		MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
    		NetworkInterfaces: []*computepb.NetworkInterface{
    			{
    				Name: proto.String("global/networks/default"),
    			},
    		},
    	}
    
    	req := &computepb.InsertInstanceRequest{
    		Project:          projectID,
    		Zone:             zone,
    		InstanceResource: inst,
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
    import com.google.cloud.compute.v1.[Scheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Scheduling.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreatePreemptibleInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you want to use.
        // zone: name of the zone you want to use. For example: “us-west3-b”
        // instanceName: name of the new virtual machine.
        String projectId = "your-project-id-or-number";
        String zone = "zone-name";
        String instanceName = "instance-name";
    
        createPremptibleInstance(projectId, zone, instanceName);
      }
    
      // Send an instance creation request with preemptible settings to the Compute Engine API
      // and wait for it to complete.
      public static void createPremptibleInstance(String projectId, String zone, String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        String machineType = String.format("zones/%s/machineTypes/e2-small", zone);
        String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
        long diskSizeGb = 10L;
        String networkName = "default";
    
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
                  // Set the preemptible setting.
                  .setScheduling(Sche[Scheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Scheduling.html)Builder()
                      .setP[setPreemptible](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Scheduling.Builder.html#com_google_cloud_compute_v1_Scheduling_Builder_setPreemptible_boolean_)e)
                      .build())
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
    
          System.out.printf("Instance created : %s\n", instanceName);
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
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createPreemptible() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.insert({
        instanceResource: {
          name: instanceName,
          disks: [
            {
              initializeParams: {
                diskSizeGb: '64',
                sourceImage:
                  'projects/debian-cloud/global/images/family/debian-11/',
              },
              autoDelete: true,
              boot: true,
            },
          ],
          scheduling: {
            // Set the preemptible setting
            preemptible: true,
          },
          machineType: `zones/${zone}/machineTypes/e2-small`,
          networkInterfaces: [
            {
              name: 'global/networks/default',
            },
          ],
        },
        project: projectId,
        zone,
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
    
    createPreemptible();

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
    
    
    def create_preemptible_instance(
        project_id: str, zone: str, instance_name: str
    ) -> compute_v1.Instance:
        """
        Create a new preemptible VM instance with Debian 10 operating system.
    
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
        instance = create_instance(project_id, zone, instance_name, disks, preemptible=True)
        return instance
    
    

###  REST 

In the API, construct a normal request to [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinginstancewithimage), but include the `preemptible` property under `scheduling` and set it to `true`. For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      'machineType': 'zones/ZONE/machineTypes/MACHINE_TYPE',
      'name': 'INSTANCE_NAME',
      'scheduling':
      {
        'preemptible': true
      },
      ...
    }
    

## Preemptible CPU quotas

Preemptible VMs require available [CPU quotas](https://docs.cloud.google.com/compute/docs/resource-quotas) like standard VMs. To avoid preemptible VMs consuming the CPU quotas for your standard VMs, you can request a special "Preemptible CPU" quota. After Compute Engine grants you preemptible CPU quota in that region, all preemptible VMs count against that quota, and all standard VMs continue to count against the standard CPU quota.

In regions where you don't have preemptible CPU quota, you can use standard CPU quota to launch preemptible VMs. You also need sufficient IP and disk quota, as usual. Preemptible CPU quota is not visible in the gcloud CLI or Google Cloud console quota pages unless Compute Engine has granted the quota.

For more information about quotas, visit the [Resource Quotas page](https://docs.cloud.google.com/compute/docs/resource-quotas).

## Start a preempted VM

Like any other VM, if a preemptible VM is stopped or preempted, you can [start the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart_a_stopped_vm_that_doesnt_have_an_encrypted_disk) again and bring it back to the `RUNNING` state. Starting a preemptible VM resets the 24-hour counter but as it is still a preemptible VM, Compute Engine can preempt before 24 hours. It isn't possible to convert a preemptible VM to a standard VM while it's running.

If Compute Engine stops a preemptible VM in an autoscaling managed instance group (MIG) or Google Kubernetes Engine cluster, the group restarts the VM when the resources become available again.

## Handle preemption with a shutdown script

When Compute Engine preempts a VM, you can use a [shutdown script](https://docs.cloud.google.com/compute/docs/shutdownscript) to try to perform cleanup actions before the VM is preempted. For example, you can gracefully stop a running process and copy a checkpoint file to [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction). Notably, the maximum length of the shutdown period is shorter for a preemption notice than for a user-initiated shutdown. For more information about the shutdown period for a preemption notice, see [Preemption process](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption-process) in the conceptual documentation.

The following is a shutdown script that you can add to a running preemptible VM or add to a new preemptible VM when you create it. This script runs when the VM starts to shut down, before the operating system's normal `kill` command stops all remaining processes. After gracefully stopping the chosen program, the script performs a parallel upload of a checkpoint file to a Cloud Storage bucket.
    
    
    #!/bin/bash
    
    MY_PROGRAM="PROGRAM_NAME" # For example, "apache2" or "nginx"
    MY_USER="LOCAL_USERNAME"
    CHECKPOINT="/home/$MY_USER/checkpoint.out"
    BUCKET_NAME="BUCKET_NAME" # For example, "my-checkpoint-files" (without gs://)
    
    echo "Shutting down!  Seeing if ${MY_PROGRAM} is running."
    
    # Find the newest copy of $MY_PROGRAM
    PID="$(pgrep -n "$MY_PROGRAM")"
    
    if [[ "$?" -ne 0 ]]; then
      echo "${MY_PROGRAM} not running, shutting down immediately."
      exit 0
    fi
    
    echo "Sending SIGINT to $PID"
    kill -2 "$PID"
    
    # Portable waitpid equivalent
    while kill -0 "$PID"; do
       sleep 1
    done
    
    echo "$PID is done, copying ${CHECKPOINT} to gs://${BUCKET_NAME} as ${MY_USER}"
    
    su "${MY_USER}" -c "gcloud storage cp $CHECKPOINT gs://${BUCKET_NAME}/"
    
    echo "Done uploading, shutting down."
    

To add this script to a VM, configure the script to work with an application on your VM and add it to the VM's metadata.

  1. Copy or download the [shutdown script](https://docs.cloud.google.com/static/compute/docs/instances/downloads/shutdown-script-pvm.sh) to your local workstation.
  2. Open the file for edit and change the following variables: 
     * `PROGRAM_NAME` is the name of the process or program you want to shut down. For example, `apache2` or `nginx`.
     * `LOCAL_USERNAME` is the username you are logged into the virtual machine as.
     * `BUCKET_NAME` is the name of the Cloud Storage bucket where you want to save the program's checkpoint file. Note the bucket name does not start with `gs://` in this case.
  3. Save your changes.
  4. Add the shutdown script to a [new VM](https://docs.cloud.google.com/compute/docs/shutdownscript#use_a_local_shutdown_script) or an [existing VM](https://docs.cloud.google.com/compute/docs/shutdownscript#apply_a_shutdown_script_to_running_instances).



This script assumes the following:

  * The VM was created with at least read/write access to Cloud Storage. See the [authentication documentation](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) for instructions about how to create a VM with the appropriate scopes.

  * You have an existing Cloud Storage bucket and permission to write to it.




## Identify preemptible VMs

To check if a VM is a preemptible VM, follow the steps to [Identify a VM's provisioning model and termination action](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#identify).

## Determine if a VM was preempted

Determine if a VM was preempted with the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or the [API](https://docs.cloud.google.com/compute/docs/reference/latest/globalOperations/aggregatedList).

###  Console 

You can check if a VM was preempted by checking the system activity logs.

  1. In the Google Cloud console, go to the **Logs** page.

[Go to Logs](https://console.cloud.google.com/logs)

  2. Select your project and click **Continue**.

  3. Add `compute.instances.preempted` to the **filter by label or text search** field.

  4. Optionally, you can also enter a VM name if you want to see preemption operations for a specific VM.

  5. Press enter to apply the specified filters. The Google Cloud console updates the list of logs to show only the operations where a VM was preempted.

  6. Select an operation in the list to see details about the VM that was preempted.




###  gcloud 

  
Use the [`gcloud compute operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) command with a [filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) parameter to get a list of preemption events in your project.
    
    
    gcloud compute operations list \
        --filter="operationType=compute.instances.preempted"
    

You can use the filter param to further scope the results. For example, to see preemption events only for VMs within a managed instance group:
    
    
    gcloud compute operations list \
        --filter="operationType=compute.instances.preempted AND targetLink:instances/BASE_VM_NAME"
    

`gcloud` returns a response similar to:
    
    
    NAME                  TYPE                         TARGET                                   HTTP_STATUS STATUS TIMESTAMP
    systemevent-yyyyyyyy  compute.instances.preempted  us-central1-f/instances/example-vm-yyy  200         DONE   2015-04-02T12:12:10.881-07:00

An operation type of `compute.instances.preempted` indicates that the VM was preempted. You can use the `operations describe` command to get more information about a specific preemption operation.
    
    
    gcloud compute operations describe \
        systemevent-yyyyyyyy
    

`gcloud` returns a response similar to:
    
    
    ...
    operationType: compute.instances.preempted
    progress: 100
    selfLink: https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-f/operations/systemevent-yyyyyyyy
    startTime: '2015-04-02T12:12:10.881-07:00'
    status: DONE
    statusMessage: Instance was preempted.
    ...

###  REST 

  
To get a list of recent system operations, send a `GET` request to the URI of zone operations.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations
    

The response contains a list of recent operations.
    
    
    {
      "kind": "compute#operation",
      "id": "15041793718812375371",
      "name": "systemevent-yyyyyyyy",
      "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-f",
      "operationType": "compute.instances.preempted",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-f/instances/EXAMPLE_VM",
      "targetId": "12820389800990687210",
      "status": "DONE",
      "statusMessage": "Instance was preempted.",
      ...
    }

To scope the response to show only preemption operations, you can add a filter to your API request: `operationType="compute.instances.preempted"`. To see preemption operations for a specific VM, add a `targetLink` param to the filter: `operationType="compute.instances.preempted" AND targetLink="https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME"`.

Alternatively, you can determine if a VM was preempted from inside the VM itself. This is useful if you want to handle a shutdown due to a Compute Engine preemption differently from a normal shutdown in a shutdown script. To do this, check the metadata server for the `preempted` value in your VM's [default instance metadata](https://docs.cloud.google.com/compute/docs/metadata#default).

For example, use `curl` from within your VM to obtain the value for `preempted`:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/preempted" -H "Metadata-Flavor: Google"
    TRUE
    

If this value is `TRUE`, the VM was preempted by Compute Engine, otherwise it is `FALSE`.

If you want to use this outside of a shutdown script, you can append [?wait_for_change=true](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#waitforchange) to the URL. This performs a hanging HTTP GET request that only returns when the metadata has changed and the VM has been preempted.
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/preempted?wait_for_change=true" -H "Metadata-Flavor: Google"
    TRUE
    

## Test preemption settings

You can run simulated maintenance events on your VMs to force them to preempt. Use this feature to test how your apps handle preemptible VMs. Read [testing your availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies) to learn how to test maintenance events on your VMs.

You can also simulate a VM's preemption by [stopping the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance), which can be used instead of simulating a maintenance event and which avoids quota limits.

## Best practices

Here are some best practices to help you get the most out of preemptible VM instances.

**Using the bulk instance API**

Rather than creating single VMs, you can [use the bulk instance API](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api).

**Pick smaller machine shapes**

Resources for preemptible VMs come out of excess and backup Google Cloud capacity. Capacity is often easier to get for _smaller machine types_ , meaning machine types with less resources like vCPUs and memory. You might find more capacity for preemptible VMs by selecting a smaller custom machine type, but capacity is even more likely for smaller predefined machine types. For example, compared to capacity for the `n2-standard-32` predefined machine type, capacity for the `n2-custom-24-96` custom machine type is more likely, but capacity for the `n2-standard-16` predefined machine type is even more likely.

**Run large preemptible VM clusters during off peak times**

The load on Google Cloud data centers varies with location and time of day, but generally lowest on nights and weekends. As such, nights and weekends are the best times to run large preemptible VM clusters.

**Design your applications to be fault and preemption tolerant**

It's important to be prepared for the fact that there are changes in preemption patterns at different points in time. For example, if a zone suffers a partial outage, large numbers of preemptible VMs could be preempted to make room for standard VMs that need to be moved as part of the recovery. In that small window of time, the preemption rate would look very different than on any other day. If your application assumes that preemptions are always done in small groups, you might not be prepared for such an event. You can test your application's behavior under a preemption event by stopping the VM instance.

**Retry creating VMs that have been preempted**

If your VM instance has been preempted, try creating new preemptible VMs once or twice before falling back to standard VMs. Depending on your requirements, it might be a good idea to combine standard and preemptible VMs in your clusters to ensure that work proceeds at an adequate pace.

**Use shutdown scripts**

Manage shutdown and preemption notices with a shutdown script that can save a job's progress so that it can pick up where it left off, rather than start over from scratch.

## What's next?

  * Read the [Preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) documentation.
  * Read about [Shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).
  * [Connect to your VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
