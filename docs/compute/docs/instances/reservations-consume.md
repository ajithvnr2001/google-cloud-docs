---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-consume/
title: Consume reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:06.432355+00:00
---

# Consume reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-consume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Consume reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to consume reservations in Compute Engine. To learn how to consume reservations in other Google Cloud products that support reservations, see the following documentation:

  * [Batch](https://docs.cloud.google.com/batch/docs/create-run-job-reservation)
  * [Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/compute-engine-reservations)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#auto_zone_and_resource_reservations)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations)
  * Vertex AI: 
    * [Use reservations with prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)
    * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute)



After you create a reservation, or Compute Engine automatically creates a reservation for you to fulfill a future reservation or future reservation in calendar mode, Compute Engine holds your reserved resources for your project, and any project you share the reservation with. When you create Compute Engine instances that match the reservation's properties, you _consume_ the reservation by using the reserved resources to create your compute instances instead of using the available resources in the compute instances' zone. You can consume your reservation for creating compute instances until the reservation is [fully consumed](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-reservation).

## Limitations

You can't consume a reservation to create the following Compute Engine resources:

  * Flex-start VMs

  * Spot VMs or preemptible instances

  * Sole-tenant nodes




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




### Required roles

To get the permissions that you need to consume reservations, ask your administrator to grant you the following IAM roles: 

  * To consume a reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project 
  * To consume a shared reservation from a consumer project: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the owner project and the consumer project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to consume reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to consume reservations:

  * To create reservations: `compute.reservations.create` on the project 
  * To create compute instances: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To create instance templates: `compute.instanceTemplates.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Consume a reservation

The examples in the following sections show how to consume a reservation by creating a single compute instance. You can also consume reservations by creating compute instances that match the reservations' properties by using a different [deployment option](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option), or by updating the properties of existing compute instances to match your automatically consumed reservations.

To consume a reservation, use one of the following methods:

  * To create a compute instance that consumes an automatic reservation that you created, or that Compute Engine automatically created to fulfill a future reservation, see Consume an automatically consumed reservation.

  * To create a compute instance that consumes a specific reservation that you created, or that Compute Engine automatically created to fulfill a future reservation, see Consume a specifically targeted reservation.

  * To create a compute instance to consume a specific reservation that Compute Engine automatically created to fulfill a future reservation in calendar mode, see Consume an auto-created reservation for a request in calendar mode.




### Consume an automatically consumed reservation

Automatically consumed reservations allow any compute instances that match the reservation's properties to automatically consume it. This consumption behavior applies to both new and existing, running compute instances. When you create on-demand reservations, or Compute Engine automatically creates a reservation to fulfill a future reservation, this reservation type is the default setting.

If the properties of a single-project, automatic reservation and a shared, automatic reservation match, then the compute instances in your project consume the single-project reservation first, and then they consume the shared reservation. For more information, see the [consumption order for reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-order).

To create and consume an example automatic reservation, select one of the following options:

###  Console 

The following example shows how to create an automatic reservation in zone `us-central1-a` for three N2 instances with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform. It also shows how to create a single compute instance to consume the reservation.

To create the example automatic reservation and consume it, do the following:

  1. To create an example reservation, complete the following steps:

     1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations?walkthrough_id=compute--reservations_automatic&start_index=2)

The remaining steps automatically appear in the Google Cloud console.

     2. On the **On-demand reservation** tab (default), click add_box **Create reservation**. The **Create a reservation** page appears.

     3. In the **Name** field, enter a name for the reservation. For example, enter `reservation-01`.

     4. Select the **Region** and **Zone** where to reserve resources. For example, select **us-central1** and **us-central1-a** respectively.

     5. In the **Share type** section, do one of the following:

        * To create a single-project reservation, select **Local**.

        * To create a shared reservation, select **Shared** , and then specify the projects that you want to share the reservation with.

     6. In the **Use with VM instance** section, select **Use reservation automatically** , if it isn't already selected.

     7. In the **Number of VM instances** field, enter `3`.

     8. On the **General purpose** tab, select **N2**.

     9. In the **Machine type** section, on the **Preset** tab (default), select **n2-standard-32**.

     10. Expand **CPU platform and GPU** , and then, in the **CPU platform** field, select **Intel Cascade Lake or later**.

     11. Click **Create**.

  2. To create a compute instance that consumes the example reservation, complete the following steps:

     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

The **Create an instance** page appears and displays the **Machine configuration** pane.

     2. In the Machine configuration pane, do the following:

        1. In the **Name** field, enter a name for the compute instance. For this example, enter `instance-01`.

        2. Specify the **Region** and **Zone** where to reserve resources. For this example, select **us-central1** and **us-central1-a** respectively.

        3. On the **General purpose** tab, select **N2**.

        4. In the **Machine type** section, on the **Preset** tab (default), select **n2-standard-32**.

        5. Expand the **Advanced options** section, and then, in the **CPU platform** field, select **Intel Cascade Lake or later**.

     3. Optional: Automatically consuming a matching reservation is the default setting. However, if you want to specify this setting, do the following:

        1. In the navigation menu, click **Advanced**. The **Advanced** pane appears.

        2. In the **Reservations** section, select **Use automatic selection**.

     4. Click **Create**.




###  gcloud 

The following example shows how to create an automatic reservation in zone `us-central1-a` for three N2 instances with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform. It also shows how to create a single compute instance to consume the reservation.

To create the example automatic reservation and consume it, do the following:

  1. To create the example reservation, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create):
         
         gcloud compute reservations create reservation-01 \
             --machine-type=n2-standard-32 \
             --min-cpu-platform="Intel Cascade Lake" \
             --vm-count=3 \
             --zone=us-central1-a
         

  2. To create a compute instance that consumes the example reservation, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--reservation-affinity` flag set to `any`. Because `any` is the default configuration, you can also omit this flag.
         
         gcloud compute instances create instance-01 \
             --machine-type=n2-standard-32 \
             --min-cpu-platform="Intel Cascade Lake" \
             **--reservation-affinity=any** \
             --zone=us-central1-a
         




###  Go 

To create the example automatic reservation using an instance template, and create an instance to consume the reservation using the same template, use the following code sample:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // consumeAnyReservation creates instance, consuming any available reservation
    func consumeAnyReservation(w io.Writer, projectID, zone, instanceName, sourceTemplate string) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-a"
    	// instanceName := "your_instance_name"
    	// sourceTemplate: existing template path. Following formats are allowed:
    	//  	- projects/{project_id}/global/instanceTemplates/{template_name}
    	//  	- projects/{project_id}/regions/{region}/instanceTemplates/{template_name}
    	//  	- https://www.googleapis.com/compute/v1/projects/{project_id}/global/instanceTemplates/instanceTemplate
    	//  	- https://www.googleapis.com/compute/v1/projects/{project_id}/regions/{region}/instanceTemplates/instanceTemplate
    
    	ctx := context.Background()
    
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project:                projectID,
    		Zone:                   zone,
    		SourceInstanceTemplate: proto.String(sourceTemplate),
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    			// specifies that any matching reservation should be consumed
    			ReservationAffinity: &computepb.ReservationAffinity{
    				ConsumeReservationType: proto.String("ANY_RESERVATION"),
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
    	fmt.Fprintf(w, "Instance created from reservation\n")
    
    	return nil
    }
    

###  Java 

The following example shows how to create an N1 instance with four vCPUs, and Intel Skylake as the minimum CPU platform in zone `us-central1-a`. The instance automatically consumes a matching reservation.

To create the example instance, use the following code sample:
    
    
    import static com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.ANY_RESERVATION;
    
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.cloud.compute.v1.AttachedDisk;
    import com.google.cloud.compute.v1.AttachedDiskInitializeParams;
    import com.google.cloud.compute.v1.InsertInstanceRequest;
    import com.google.cloud.compute.v1.Instance;
    import com.google.cloud.compute.v1.InstancesClient;
    import com.google.cloud.compute.v1.NetworkInterface;
    import com.google.cloud.compute.v1.Operation;
    import com.google.cloud.compute.v1.ReservationAffinity;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ConsumeAnyMatchingReservation {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Zone where the VM instance will be created.
        String zone = "us-central1-a";
        // Name of the VM instance you want to query.
        String instanceName = "YOUR_INSTANCE_NAME";
        // machineType: machine type of the VM being created.
        // *   For a list of machine types, see https://cloud.google.com/compute/docs/machine-types
        String machineTypeName = "n1-standard-4";
        // sourceImage: path to the operating system image to mount.
        // *   For details about images you can mount, see https://cloud.google.com/compute/docs/images
        String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
        // diskSizeGb: storage size of the boot disk to attach to the instance.
        long diskSizeGb = 10L;
        // networkName: network interface to associate with the instance.
        String networkName = "default";
        // Minimum CPU platform of the instances.
        String minCpuPlatform = "Intel Skylake";
    
        createInstanceAsync(projectId, zone, instanceName, machineTypeName, sourceImage,
            diskSizeGb, networkName, minCpuPlatform);
      }
    
      // Create a virtual machine targeted with the reserveAffinity field.
      // In this consumption model, existing and new VMs automatically consume a reservation
      // if their properties match the VM properties specified in the reservation.
      public static Instance createInstanceAsync(String projectId, String zone,
          String instanceName, String machineTypeName, String sourceImage,
          long diskSizeGb, String networkName, String minCpuPlatform)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        String machineType = String.format("zones/%s/machineTypes/%s", zone, machineTypeName);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (InstancesClient instancesClient = InstancesClient.create()) {
          AttachedDisk disk =
              AttachedDisk.newBuilder()
                  .setBoot(true)
                  .setAutoDelete(true)
                  .setType(AttachedDisk.Type.PERSISTENT.toString())
                  .setDeviceName("disk-1")
                  .setInitializeParams(
                      AttachedDiskInitializeParams.newBuilder()
                          .setSourceImage(sourceImage)
                          .setDiskSizeGb(diskSizeGb)
                          .build())
                  .build();
    
          NetworkInterface networkInterface = NetworkInterface.newBuilder()
              .setName(networkName)
              .build();
    
          ReservationAffinity reservationAffinity =
              ReservationAffinity.newBuilder()
                  .setConsumeReservationType(ANY_RESERVATION.toString())
                  .build();
    
          Instance instanceResource =
              Instance.newBuilder()
                  .setName(instanceName)
                  .setMachineType(machineType)
                  .addDisks(disk)
                  .addNetworkInterfaces(networkInterface)
                  .setMinCpuPlatform(minCpuPlatform)
                  .setReservationAffinity(reservationAffinity)
                  .build();
    
          InsertInstanceRequest insertInstanceRequest = InsertInstanceRequest.newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(instanceResource)
              .build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
              insertInstanceRequest);
    
          Operation response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.hasError()) {
            return null;
          }
          return instancesClient.get(projectId, zone, instanceName);
        }
      }
    }

###  Node.js 

The following example shows how to create an N1 instance with four vCPUs, and Intel Skylake as the minimum CPU platform in zone `us-central1-a`. The instance automatically consumes a matching reservation.

To create the example instance, use the following code sample:
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a reservationsClient
    const instancesClient = new computeLib.InstancesClient();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where you want to create instance.
    const projectId = await instancesClient.getProjectId();
    // The zone in which to create instance.
    const zone = 'us-central1-a';
    // The name of the instance to create.
    // const instanceName = 'instance-01';
    // Machine type to use for VM.
    const machineType = 'n1-standard-4';
    
    // Create instance to consume reservation if their properties match the VM properties
    async function callCreateInstanceToConsumeAnyReservation() {
      // Describe the size and source image of the boot disk to attach to the instance.
      const disk = new compute.Disk({
        boot: true,
        autoDelete: true,
        type: 'PERSISTENT',
        initializeParams: {
          diskSizeGb: '10',
          sourceImage: 'projects/debian-cloud/global/images/family/debian-12',
        },
      });
    
      //  Define networkInterface
      const networkInterface = new compute.NetworkInterface({
        name: 'global/networks/default',
      });
    
      // Define reservationAffinity
      const reservationAffinity = new compute.ReservationAffinity({
        consumeReservationType: 'ANY_RESERVATION',
      });
    
      // Create an instance
      const instance = new compute.Instance({
        name: instanceName,
        machineType: `zones/${zone}/machineTypes/${machineType}`,
        minCpuPlatform: 'Intel Skylake',
        disks: [disk],
        networkInterfaces: [networkInterface],
        reservationAffinity,
      });
    
      const [response] = await instancesClient.insert({
        project: projectId,
        instanceResource: instance,
        zone,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create instance operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Instance ${instanceName} created.`);
    }
    
    await callCreateInstanceToConsumeAnyReservation();

###  Python 

The following example shows how to create an automatic reservation in zone `us-central1-a` for three N1 instances with one vCPU, and Intel Ivy as the minimum CPU platform. It also shows how to create a single instance to consume the reservation.

To create the example automatic reservation and consume it, do the following:
    
    
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
    
    
    def consume_any_project_reservation(
        project_id: str,
        zone: str,
        reservation_name: str,
        instance_name: str,
        machine_type: str = "n1-standard-1",
        min_cpu_platform: str = "Intel Ivy Bridge",
    ) -> compute_v1.Instance:
        """
        Creates a specific reservation in a single project and launches a VM
        that consumes the newly created reservation.
        Args:
            project_id (str): The ID of the Google Cloud project.
            zone (str): The zone to create the reservation.
            reservation_name (str): The name of the reservation to create.
            instance_name (str): The name of the instance to create.
            machine_type (str): The machine type for the instance.
            min_cpu_platform (str): The minimum CPU platform for the instance.
        """
        instance_properties = (
            compute_v1.AllocationSpecificSKUAllocationReservedInstanceProperties(
                machine_type=machine_type,
                min_cpu_platform=min_cpu_platform,
            )
        )
    
        reservation = compute_v1.Reservation(
            name=reservation_name,
            specific_reservation=compute_v1.AllocationSpecificSKUReservation(
                count=3,
                instance_properties=instance_properties,
            ),
        )
    
        # Create a reservation client
        client = compute_v1.ReservationsClient()
        operation = client.insert(
            project=project_id,
            zone=zone,
            reservation_resource=reservation,
        )
        wait_for_extended_operation(operation, "Reservation creation")
    
        instance = compute_v1.Instance()
        instance.name = instance_name
        instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
        instance.min_cpu_platform = min_cpu_platform
        instance.zone = zone
    
        # Set the reservation affinity to target any matching reservation
        instance.reservation_affinity = compute_v1.ReservationAffinity(
            consume_reservation_type="ANY_RESERVATION",  # Type of reservation to consume
        )
        # Define the disks for the instance
        instance.disks = [
            compute_v1.AttachedDisk(
                boot=True,  # Indicates that this is a boot disk
                auto_delete=True,  # The disk will be deleted when the instance is deleted
                initialize_params=compute_v1.AttachedDiskInitializeParams(
                    source_image="projects/debian-cloud/global/images/family/debian-13",
                    disk_size_gb=10,
                ),
            )
        ]
        instance.network_interfaces = [
            compute_v1.NetworkInterface(
                network="global/networks/default",  # The network to use
                access_configs=[
                    compute_v1.AccessConfig(
                        name="External NAT",  # Name of the access configuration
                        type="ONE_TO_ONE_NAT",  # Type of access configuration
                    )
                ],
            )
        ]
        # Create a request to insert the instance
        request = compute_v1.InsertInstanceRequest()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        vm_client = compute_v1.InstancesClient()
        operation = vm_client.insert(request)
        wait_for_extended_operation(operation, "instance creation")
        print(f"Instance {instance_name} that targets any open reservation created.")
    
        return vm_client.get(project=project_id, zone=zone, instance=instance_name)
    
    

###  REST 

The following example shows how to create an automatic reservation in zone `us-central1-a` for three N2 instances with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform. It also shows how to create a single instance to consume the reservation.

To create the example automatic reservation and consume it, do the following:

  1. To create the example reservation, make a `POST` request to [`reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations
         
         {
           "name": "reservation-01",
           "specificReservation": {
             "count": "3",
             "instanceProperties": {
               "machineType": "n2-standard-32",
               "minCpuPlatform": "Intel Cascade Lake",
             }
           }
         }
         

  2. To create an instance that consumes the example reservation, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `consumeReservationType` field set to `ANY_RESERVATION`. However, because `ANY_RESERVATION` is the default configuration, you can also omit the field.
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances
         
         {
           "name": "instance-01",
           "machineType": "zones/us-central1-a/machineTypes/n2-standard-32",
           "minCpuPlatform": "Intel Cascade Lake",
           "disks": [
             {
               "boot": true,
               "initializeParams": {
                 "sourceImage": "projects/debian-cloud/global/images/family/debian-12"
               }
             }
           ],
           "networkInterfaces": [
             {
               "network": "global/networks/default"
             }
           ],
           **"reservationAffinity": {
             "consumeReservationType": "ANY_RESERVATION"
           }**
         }
         




### Consume a specifically targeted reservation

Specifically targeted reservations allow new compute instances that match the reservation's properties and target the reservation to consume it. You can successfully create compute instances only if their properties match the reservation properties. Otherwise, your creation request fails.

Based on the creation method that you want to use, create specific reservations and compute instances that target them as follows:

Creation method | [When you create a reservation](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) | When you create compute instances to consume the reservation  
---|---|---  
Google Cloud console | In the **Use with VM instance** section, select **Select specific reservation**. | In the **Advanced** pane, in the **Reservations** section, select **Choose a reservation**. Then, follow the prompts to select a reservation.  
Google Cloud CLI | Include the `--require-specific-reservation` flag. | Include the following flags:   


  * The `--reservation-affinity` flag set to `specific`.
  * The `--reservation` flag set to the resource path to the reservation, formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`. 

  
Go | Include the `SpecificReservationRequired` field set to `true`. | In the `ReservationAffinity` field, include the following fields: 

  * The `ConsumeReservationType` field set to `SPECIFIC_RESERVATION`.
  * The `Key` field set to `compute.googleapis.com/reservation-name`.
  * The `Values` field set to the resource path to the reservation, formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`. 

  
Java | Include the `setSpecificReservationRequired` field set to `true`. | In the `ReservationAffinity` field, include the following fields: 

  * The `setConsumeReservationType` field set to `SPECIFIC_RESERVATION`.
  * The `setKey` field set to `compute.googleapis.com/reservation-name`.
  * The `addValues` field set to the resource path to the reservation, formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`. 

  
Node.js and REST API | Include the `specificReservationRequired` field set to `true`. | In the `reservationAffinity` field, include the following fields: 

  * The `consumeReservationType` field set to `SPECIFIC_RESERVATION`.
  * The `key` field set to `compute.googleapis.com/reservation-name`.
  * The `values` field set to a list that contains a single item with the resource path to the reservation, formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`. 

  
Python | Include the `specific_reservation_required` field set to `true`. | In the `reservation_affinity` field, include the following fields: 

  * The `consume_reservation_type` field set to `SPECIFIC_RESERVATION`.
  * The `key` field set to `compute.googleapis.com/reservation-name`.
  * The `values` field set to the resource path to the reservation, formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`. 

  
Terraform | Include the `specific_reservation_required` field set to `true`. | In the `reservation_affinity` field, include the following fields: 

  * The `type` field set to `SPECIFIC_RESERVATION`.
  * The `specific_reservation` field, which includes the following fields:
    * The `key` field set to `compute.googleapis.com/reservation-name`.
    * The `values` field set to a list that contains a single item with the resource path to the reservation, formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`. 

  
**Note:** To enable a regional managed instance group (MIG) to consume specific reservations in multiple zones, create reservations with matching names and properties in each zone. Then, target the reservations in the group's instance template.

To create an example specific reservation and a compute instance to consume it, select one of the following options:

###  Console 

The following example shows how to create a specific reservation in zone `us-central1-a` for three N2 instances with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform. It also shows how to create a single compute instance to consume the reservation.

To create the example specific reservation and consume it, do the following:

  1. To create an example reservation, complete the following steps:

     1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations?walkthrough_id=compute--reservations_specific&start_index=2)

The remaining steps automatically appear in the Google Cloud console.

     2. On the **On-demand reservation** tab (default), click add_box **Create reservation**. The **Create a reservation** page appears.

     3. In the **Name** field, enter a name for the reservation. For example, enter `reservation-02`.

     4. Specify the **Region** and **Zone** where to reserve resources. For this example, select **us-central1** and **us-central1-a** respectively.

     5. In the **Share type** section, do one of the following:

        * To create a single-project reservation, select **Local**.

        * To create a shared reservation, select **Shared** , and then specify the projects that you want to share the reservation with.

     6. In the **Use with VM instance** section, select **Select specific reservation**.

     7. In the **Number of VM instances** field, enter `3`.

     8. On the **General purpose** tab, select **N2**.

     9. In the **Machine type** section, on the **Preset** tab (default), select **n2-standard-32**.

     10. Expand **CPU platform and GPU** , and then, in the **CPU platform** field, select **Intel Cascade Lake or later**.

     11. Click **Create**.

  2. To create a compute instance that consumes the example reservation, complete the following steps:

     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

The **Create an instance** page appears and displays the **Machine configuration** pane.

     2. In the Machine configuration pane, do the following:

        1. In the **Name** field, enter a name for the compute instance. For this example, enter `instance-02`.

        2. Specify the **Region** and **Zone** where to reserve resources. For this example, select **us-central1** and **us-central1-a** respectively.

        3. On the **General purpose** tab, select **N2**.

        4. In the **Machine type** section, on the **Preset** tab (default), select **n2-standard-32**.

        5. Expand the **Advanced options** section, and then, in the **CPU platform** field, select **Intel Cascade Lake or later**.

     3. In the navigation menu, click **Advanced**. The **Advanced** pane appears.

     4. In the **Reservations** section, select **Choose a reservation** , and then click **Choose reservation**.

     5. On the **Choose a reservation** pane that appears, do the following:

        1. Select the specific reservation that you created in the previous steps. If you want to consume a shared reservation that exists in a different project, then, in the **Project** list, select the project in which the reservation exists.

        2. Click **Choose**.

     6. Click **Create**.




###  gcloud 

The following example shows how to create a specific reservation in zone `us-central1-a` for three N2 instances with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform. It also shows how to create a single compute instance to consume the reservation.

To create the example specific reservation and consume it, do the following:

  1. To create the example reservation, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) with the `--require-specific-reservation` flag:
         
         gcloud compute reservations create reservation-02 \
             --machine-type=n2-standard-32 \
             --min-cpu-platform="Intel Cascade Lake" \
             **--require-specific-reservation** \
             --vm-count=3 \
             --zone=us-central1-a
         

  2. To create a compute instance that consumes the example reservation, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--reservation` and `--reservation-affinity=specific` flags:
         
         gcloud compute instances create instance-02 \
             --machine-type=n2-standard-32 \
             --min-cpu-platform="Intel Cascade Lake" \
             **--reservation-affinity=specific** \
             **--reservation= RESERVATION_URL** \
             --zone=us-central1-a
         

Replace `RESERVATION_URL` with the URL of the reservation. Specify one of the following values:

     * If you created the reservation in the same project: `reservation-02`

     * If the reservation is in a different project: `projects/PROJECT_ID/reservations/reservation-02`




###  Go 

The following examples show how to create an N2 instance with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform, in zone `us-central1-a` to consume a specific, matching reservation:

  * To create the example compute instance to consume a single-project, specific reservation, use the following code sample:
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	compute "cloud.google.com/go/compute/apiv1"
        	computepb "cloud.google.com/go/compute/apiv1/computepb"
        	"google.golang.org/protobuf/proto"
        )
        
        // consumeSpecificReservation creates instance, consuming specific reservation
        // Note: respective reservation should have SpecificReservationRequired: true
        func consumeSpecificReservation(w io.Writer, projectID, zone, instanceName, reservationName string) error {
        	// projectID := "your_project_id"
        	// zone := "us-west3-a"
        	// reservationName := "your_reservation_name"
        	// instanceName := "your_instance_name"
        
        	ctx := context.Background()
        	machineType := fmt.Sprintf("zones/%s/machineTypes/%s", zone, "n2-standard-32")
        	sourceImage := "projects/debian-cloud/global/images/family/debian-12"
        
        	instancesClient, err := compute.NewInstancesRESTClient(ctx)
        	if err != nil {
        		return fmt.Errorf("NewInstancesRESTClient: %w", err)
        	}
        	defer instancesClient.Close()
        
        	req := &computepb.InsertInstanceRequest{
        		Project: projectID,
        		Zone:    zone,
        		InstanceResource: &computepb.Instance{
        			Disks: []*computepb.AttachedDisk{
        				{
        					InitializeParams: &computepb.AttachedDiskInitializeParams{
        						DiskSizeGb:  proto.Int64(10),
        						SourceImage: proto.String(sourceImage),
        					},
        					AutoDelete: proto.Bool(true),
        					Boot:       proto.Bool(true),
        					Type:       proto.String(computepb.AttachedDisk_PERSISTENT.String()),
        				},
        			},
        			MachineType:    proto.String(machineType),
        			MinCpuPlatform: proto.String("Intel Cascade Lake"),
        			Name:           proto.String(instanceName),
        			NetworkInterfaces: []*computepb.NetworkInterface{
        				{
        					Network: proto.String("global/networks/default"),
        				},
        			},
        			// specifies particular reservation, which should be consumed
        			ReservationAffinity: &computepb.ReservationAffinity{
        				ConsumeReservationType: proto.String("SPECIFIC_RESERVATION"),
        				Key:                    proto.String("compute.googleapis.com/reservation-name"),
        				Values:                 []string{reservationName},
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
        	fmt.Fprintf(w, "Instance created from reservation\n")
        
        	return nil
        }
        

  * To create the example compute instance to consume a shared, specific reservation, use the following code sample:
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	computepb "cloud.google.com/go/compute/apiv1/computepb"
        	"google.golang.org/protobuf/proto"
        )
        
        // consumeSpecificSharedReservation consumes specific shared reservation in particular zone
        func consumeSpecificSharedReservation(w io.Writer, client InstanceClientInterface, projectID, baseProjectId, zone, instanceName, reservationName string) error {
        	// client, err := compute.NewInstancesRESTClient(ctx)
        	// projectID := "your_project_id". Project where reservation is created.
        	// baseProjectId := "shared_project_id". Project where instance will be consumed and created.
        	// zone := "us-west3-a"
        	// reservationName := "your_reservation_name"
        	// instanceName := "your_instance_name"
        
        	ctx := context.Background()
        	machineType := fmt.Sprintf("zones/%s/machineTypes/%s", zone, "n2-standard-32")
        	sourceImage := "projects/debian-cloud/global/images/family/debian-12"
        	sharedReservation := fmt.Sprintf("projects/%s/reservations/%s", baseProjectId, reservationName)
        
        	req := &computepb.InsertInstanceRequest{
        		Project: projectID,
        		Zone:    zone,
        		InstanceResource: &computepb.Instance{
        			Disks: []*computepb.AttachedDisk{
        				{
        					InitializeParams: &computepb.AttachedDiskInitializeParams{
        						DiskSizeGb:  proto.Int64(10),
        						SourceImage: proto.String(sourceImage),
        					},
        					AutoDelete: proto.Bool(true),
        					Boot:       proto.Bool(true),
        					Type:       proto.String(computepb.AttachedDisk_PERSISTENT.String()),
        				},
        			},
        			MachineType:    proto.String(machineType),
        			MinCpuPlatform: proto.String("Intel Cascade Lake"),
        			Name:           proto.String(instanceName),
        			NetworkInterfaces: []*computepb.NetworkInterface{
        				{
        					Network: proto.String("global/networks/default"),
        				},
        			},
        			// specifies particular reservation, which should be consumed
        			ReservationAffinity: &computepb.ReservationAffinity{
        				ConsumeReservationType: proto.String("SPECIFIC_RESERVATION"),
        				Key:                    proto.String("compute.googleapis.com/reservation-name"),
        				Values:                 []string{sharedReservation},
        			},
        		},
        	}
        
        	op, err := client.Insert(ctx, req)
        	if err != nil {
        		return fmt.Errorf("unable to create instance: %w", err)
        	}
        
        	if op != nil {
        		if err = op.Wait(ctx); err != nil {
        			return fmt.Errorf("unable to wait for the operation: %w", err)
        		}
        	}
        	fmt.Fprintf(w, "Instance created from shared reservation\n")
        
        	return nil
        }
        




###  Java 

The following examples show how to create an N1 instance with four vCPUs, and Intel Skylake as the minimum CPU platform, in zone `us-central1-a` to consume a specific, matching reservation:

  * To create an example reservation as a single-project reservation, and create a compute instance to consume it, use the following code sample:
        
        import static com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.SPECIFIC_RESERVATION;
        
        import com.google.api.gax.longrunning.OperationFuture;
        import com.google.cloud.compute.v1.AttachedDisk;
        import com.google.cloud.compute.v1.AttachedDiskInitializeParams;
        import com.google.cloud.compute.v1.InsertInstanceRequest;
        import com.google.cloud.compute.v1.Instance;
        import com.google.cloud.compute.v1.InstancesClient;
        import com.google.cloud.compute.v1.NetworkInterface;
        import com.google.cloud.compute.v1.Operation;
        import com.google.cloud.compute.v1.ReservationAffinity;
        import java.io.IOException;
        import java.util.concurrent.ExecutionException;
        import java.util.concurrent.TimeUnit;
        import java.util.concurrent.TimeoutException;
        
        public class ConsumeSingleProjectReservation {
          public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
            // TODO(developer): Replace these variables before running the sample.
            // Project ID or project number of the Cloud project you want to use.
            String projectId = "YOUR_PROJECT_ID";
            // Name of the zone where the reservation is located.
            String zone = "us-central1-a";
            // Name of the reservation you want to query.
            String reservationName = "YOUR_RESERVATION_NAME";
            // Name of the VM instance you want to query.
            String instanceName = "YOUR_INSTANCE_NAME";
            // machineType: machine type of the VM being created.
            // *   For a list of machine types, see https://cloud.google.com/compute/docs/machine-types
            String machineTypeName = "n1-standard-4";
            // sourceImage: path to the operating system image to mount.
            // *   For details about images you can mount, see https://cloud.google.com/compute/docs/images
            String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
            // diskSizeGb: storage size of the boot disk to attach to the instance.
            long diskSizeGb = 10L;
            // networkName: network interface to associate with the instance.
            String networkName = "default";
            // Minimum CPU platform of the instances.
            String minCpuPlatform = "Intel Skylake";
        
            createInstanceAsync(projectId, zone, instanceName, reservationName, machineTypeName,
                sourceImage, diskSizeGb, networkName, minCpuPlatform);
          }
        
          // Create a virtual machine targeted with the reserveAffinity field.
          // Ensure that the VM's properties match the reservation's VM properties.
          public static Instance createInstanceAsync(String projectId, String zone, String instanceName,
              String reservationName, String machineTypeName, String sourceImage, long diskSizeGb,
              String networkName, String minCpuPlatform)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
            String machineType = String.format("zones/%s/machineTypes/%s", zone, machineTypeName);
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            try (InstancesClient instancesClient = InstancesClient.create()) {
              AttachedDisk disk =
                  AttachedDisk.newBuilder()
                      .setBoot(true)
                      .setAutoDelete(true)
                      .setType(AttachedDisk.Type.PERSISTENT.toString())
                      .setDeviceName("disk-1")
                      .setInitializeParams(
                          AttachedDiskInitializeParams.newBuilder()
                              .setSourceImage(sourceImage)
                              .setDiskSizeGb(diskSizeGb)
                              .build())
                      .build();
        
              NetworkInterface networkInterface = NetworkInterface.newBuilder()
                  .setName(networkName)
                  .build();
        
              ReservationAffinity reservationAffinity =
                  ReservationAffinity.newBuilder()
                      .setConsumeReservationType(SPECIFIC_RESERVATION.toString())
                      .setKey("compute.googleapis.com/reservation-name")
                      // Set specific reservation
                      .addValues(reservationName)
                      .build();
        
              Instance instanceResource =
                  Instance.newBuilder()
                      .setName(instanceName)
                      .setMachineType(machineType)
                      .addDisks(disk)
                      .addNetworkInterfaces(networkInterface)
                      .setMinCpuPlatform(minCpuPlatform)
                      .setReservationAffinity(reservationAffinity)
                      .build();
        
              InsertInstanceRequest insertInstanceRequest = InsertInstanceRequest.newBuilder()
                  .setProject(projectId)
                  .setZone(zone)
                  .setInstanceResource(instanceResource)
                  .build();
        
              OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
                  insertInstanceRequest);
              Operation response = operation.get(3, TimeUnit.MINUTES);
        
              if (response.hasError()) {
                return null;
              }
              return instancesClient.get(projectId, zone, instanceName);
            }
          }
        }

  * To create an example reservation as a shared reservation, and create a compute instance to consume it, use the following code sample:
        
        import static com.google.cloud.compute.v1.ReservationAffinity.ConsumeReservationType.SPECIFIC_RESERVATION;
        
        import com.google.api.gax.longrunning.OperationFuture;
        import com.google.cloud.compute.v1.AttachedDisk;
        import com.google.cloud.compute.v1.AttachedDiskInitializeParams;
        import com.google.cloud.compute.v1.InsertInstanceRequest;
        import com.google.cloud.compute.v1.Instance;
        import com.google.cloud.compute.v1.InstancesClient;
        import com.google.cloud.compute.v1.NetworkInterface;
        import com.google.cloud.compute.v1.Operation;
        import com.google.cloud.compute.v1.ReservationAffinity;
        import java.io.IOException;
        import java.util.concurrent.ExecutionException;
        import java.util.concurrent.TimeUnit;
        import java.util.concurrent.TimeoutException;
        
        public class ConsumeSpecificSharedReservation {
          public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
            // TODO(developer): Replace these variables before running the sample.
            // Project ID or project number of the Cloud project you want to use.
            String projectId = "YOUR_PROJECT_ID";
            // Name of the zone the reservation is located.
            String zone = "us-central1-a";
            // Name of the reservation you want to query.
            String reservationName = "YOUR_RESERVATION_NAME";
            // Name of the VM instance you want to query.
            String instanceName = "YOUR_INSTANCE_NAME";
            // machineType: machine type of the VM being created.
            // *   For a list of machine types, see https://cloud.google.com/compute/docs/machine-types
            String machineTypeName = "n1-standard-4";
            // sourceImage: path to the operating system image to mount.
            // *   For details about images you can mount, see https://cloud.google.com/compute/docs/images
            String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
            // diskSizeGb: storage size of the boot disk to attach to the instance.
            long diskSizeGb = 10L;
            // networkName: network interface to associate with the instance.
            String networkName = "default";
            // Minimum CPU platform of the instances.
            String minCpuPlatform = "Intel Skylake";
        
            createInstanceAsync(projectId, zone, instanceName, reservationName, machineTypeName,
                sourceImage, diskSizeGb, networkName, minCpuPlatform);
          }
        
          // Create a virtual machine targeted with the reserveAffinity field.
          // Ensure that the VM's properties match the reservation's VM properties.
          public static Instance createInstanceAsync(String projectId, String zone, String instanceName,
              String reservationName, String machineTypeName, String sourceImage, long diskSizeGb,
              String networkName, String minCpuPlatform)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
            String machineType = String.format("zones/%s/machineTypes/%s", zone, machineTypeName);
            // To consume this reservation from any consumer projects that this reservation is shared with,
            // you must also specify the owner project of the reservation - the path to the reservation.
            String reservationPath =
                String.format("projects/%s/reservations/%s", projectId, reservationName);
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            try (InstancesClient instancesClient = InstancesClient.create()) {
              AttachedDisk disk =
                  AttachedDisk.newBuilder()
                      .setBoot(true)
                      .setAutoDelete(true)
                      .setType(AttachedDisk.Type.PERSISTENT.toString())
                      .setDeviceName("disk-1")
                      .setInitializeParams(
                          AttachedDiskInitializeParams.newBuilder()
                              .setSourceImage(sourceImage)
                              .setDiskSizeGb(diskSizeGb)
                              .build())
                      .build();
        
              NetworkInterface networkInterface = NetworkInterface.newBuilder()
                  .setName(networkName)
                  .build();
        
              ReservationAffinity reservationAffinity =
                  ReservationAffinity.newBuilder()
                      .setConsumeReservationType(SPECIFIC_RESERVATION.toString())
                      .setKey("compute.googleapis.com/reservation-name")
                      // Set specific reservation
                      .addValues(reservationPath)
                      .build();
        
              Instance instanceResource =
                  Instance.newBuilder()
                      .setName(instanceName)
                      .setMachineType(machineType)
                      .addDisks(disk)
                      .addNetworkInterfaces(networkInterface)
                      .setMinCpuPlatform(minCpuPlatform)
                      .setReservationAffinity(reservationAffinity)
                      .build();
        
              InsertInstanceRequest insertInstanceRequest = InsertInstanceRequest.newBuilder()
                  .setProject(projectId)
                  .setZone(zone)
                  .setInstanceResource(instanceResource)
                  .build();
        
              OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
                  insertInstanceRequest);
              Operation response = operation.get(3, TimeUnit.MINUTES);
        
              if (response.hasError()) {
                return null;
              }
              return instancesClient.get(projectId, zone, instanceName);
            }
          }
        }




###  Node.js 

The following examples show how to create an N1 instance with 4 vCPUs, and Intel Skylake as the minimum CPU platform, in zone `us-central1-a` to consume a specific, matching reservation:
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a reservationsClient
    const instancesClient = new computeLib.InstancesClient();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where you want to create instance.
    const projectId = await instancesClient.getProjectId();
    // The zone in which to create instance.
    const zone = 'us-central1-a';
    // The name of the instance to create.
    // const instanceName = 'instance-01';
    // The name of the reservation to consume.
    // Ensure that the specificReservationRequired field in reservation properties is set to true.
    // const reservationName = 'reservation-01';
    // Machine type to use for VM.
    const machineType = 'n1-standard-4';
    
    // Create instance to consume a specific single-project reservation
    async function callCreateInstanceToConsumeSingleProjectReservation() {
      // Describe the size and source image of the boot disk to attach to the instance.
      // Ensure that the VM's properties match the reservation's VM properties,
      // including the zone, machine type (machine family, vCPUs, and memory),
      // minimum CPU platform, GPU amount and type, and local SSD interface and size
      const disk = new compute.Disk({
        boot: true,
        autoDelete: true,
        type: 'PERSISTENT',
        initializeParams: {
          diskSizeGb: '10',
          sourceImage: 'projects/debian-cloud/global/images/family/debian-12',
        },
      });
    
      //  Define networkInterface
      const networkInterface = new compute.NetworkInterface({
        name: 'global/networks/default',
      });
    
      // Define reservationAffinity
      const reservationAffinity = new compute.ReservationAffinity({
        consumeReservationType: 'SPECIFIC_RESERVATION',
        key: 'compute.googleapis.com/reservation-name',
        values: [reservationName],
      });
    
      // Create an instance
      const instance = new compute.Instance({
        name: instanceName,
        machineType: `zones/${zone}/machineTypes/${machineType}`,
        minCpuPlatform: 'Intel Skylake',
        disks: [disk],
        networkInterfaces: [networkInterface],
        reservationAffinity,
      });
    
      const [response] = await instancesClient.insert({
        project: projectId,
        instanceResource: instance,
        zone,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create instance operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Instance ${instanceName} created.`);
    }
    
    await callCreateInstanceToConsumeSingleProjectReservation();

###  Python 

The following examples show how to create an N2 instance with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform, in zone `us-central1-a` to consume a specific, matching reservation:

To create the example specific reservation and consume it, do the following:

  * To create and consume the example reservation as a single-project reservation, use the following code sample:
        
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
        
        
        def consume_specific_single_project_reservation(
            project_id: str,
            zone: str,
            reservation_name: str,
            instance_name: str,
            machine_type: str = "n1-standard-1",
            min_cpu_platform: str = "Intel Ivy Bridge",
        ) -> compute_v1.Instance:
            """
            Creates a specific reservation in a single project and launches a VM
            that consumes the newly created reservation.
            Args:
                project_id (str): The ID of the Google Cloud project.
                zone (str): The zone to create the reservation.
                reservation_name (str): The name of the reservation to create.
                instance_name (str): The name of the instance to create.
                machine_type (str): The machine type for the instance.
                min_cpu_platform (str): The minimum CPU platform for the instance.
            """
            instance_properties = (
                compute_v1.AllocationSpecificSKUAllocationReservedInstanceProperties(
                    machine_type=machine_type,
                    min_cpu_platform=min_cpu_platform,
                )
            )
        
            reservation = compute_v1.Reservation(
                name=reservation_name,
                specific_reservation=compute_v1.AllocationSpecificSKUReservation(
                    count=3,
                    instance_properties=instance_properties,
                ),
                # Only VMs that target the reservation by name can consume from this reservation
                specific_reservation_required=True,
            )
        
            # Create a reservation client
            client = compute_v1.ReservationsClient()
            operation = client.insert(
                project=project_id,
                zone=zone,
                reservation_resource=reservation,
            )
            wait_for_extended_operation(operation, "Reservation creation")
        
            instance = compute_v1.Instance()
            instance.name = instance_name
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
            instance.min_cpu_platform = min_cpu_platform
            instance.zone = zone
        
            # Set the reservation affinity to target the specific reservation
            instance.reservation_affinity = compute_v1.ReservationAffinity(
                consume_reservation_type="SPECIFIC_RESERVATION",  # Type of reservation to consume
                key="compute.googleapis.com/reservation-name",  # Key for the reservation
                values=[reservation_name],  # Reservation name to consume
            )
            # Define the disks for the instance
            instance.disks = [
                compute_v1.AttachedDisk(
                    boot=True,  # Indicates that this is a boot disk
                    auto_delete=True,  # The disk will be deleted when the instance is deleted
                    initialize_params=compute_v1.AttachedDiskInitializeParams(
                        source_image="projects/debian-cloud/global/images/family/debian-13",
                        disk_size_gb=10,
                    ),
                )
            ]
            instance.network_interfaces = [
                compute_v1.NetworkInterface(
                    network="global/networks/default",  # The network to use
                    access_configs=[
                        compute_v1.AccessConfig(
                            name="External NAT",  # Name of the access configuration
                            type="ONE_TO_ONE_NAT",  # Type of access configuration
                        )
                    ],
                )
            ]
            # Create a request to insert the instance
            request = compute_v1.InsertInstanceRequest()
            request.zone = zone
            request.project = project_id
            request.instance_resource = instance
        
            vm_client = compute_v1.InstancesClient()
            operation = vm_client.insert(request)
            wait_for_extended_operation(operation, "instance creation")
            print(f"Instance {instance_name} with specific reservation created successfully.")
        
            return vm_client.get(project=project_id, zone=zone, instance=instance_name)
        
        

  * To create and consume the example reservation as a shared reservation, use the following code sample:
        
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
        
        
        def consume_specific_shared_project_reservation(
            owner_project_id: str,
            shared_project_id: str,
            zone: str,
            reservation_name: str,
            instance_name: str,
            machine_type: str = "n1-standard-1",
            min_cpu_platform: str = "Intel Ivy Bridge",
        ) -> compute_v1.Instance:
            """
            Creates a specific reservation in a single project and launches a VM
            that consumes the newly created reservation.
            Args:
                owner_project_id (str): The ID of the Google Cloud project.
                shared_project_id: The ID of the owner project of the reservation in the same zone.
                zone (str): The zone to create the reservation.
                reservation_name (str): The name of the reservation to create.
                instance_name (str): The name of the instance to create.
                machine_type (str): The machine type for the instance.
                min_cpu_platform (str): The minimum CPU platform for the instance.
            """
            instance_properties = (
                compute_v1.AllocationSpecificSKUAllocationReservedInstanceProperties(
                    machine_type=machine_type,
                    min_cpu_platform=min_cpu_platform,
                )
            )
        
            reservation = compute_v1.Reservation(
                name=reservation_name,
                specific_reservation=compute_v1.AllocationSpecificSKUReservation(
                    count=3,
                    instance_properties=instance_properties,
                ),
                # Only VMs that target the reservation by name can consume from this reservation
                specific_reservation_required=True,
                share_settings=compute_v1.ShareSettings(
                    share_type="SPECIFIC_PROJECTS",
                    project_map={
                        shared_project_id: compute_v1.ShareSettingsProjectConfig(
                            project_id=shared_project_id
                        )
                    },
                ),
            )
        
            # Create a reservation client
            client = compute_v1.ReservationsClient()
            operation = client.insert(
                project=owner_project_id,
                zone=zone,
                reservation_resource=reservation,
            )
            wait_for_extended_operation(operation, "Reservation creation")
        
            instance = compute_v1.Instance()
            instance.name = instance_name
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
            instance.min_cpu_platform = min_cpu_platform
            instance.zone = zone
        
            # Set the reservation affinity to target the specific reservation
            instance.reservation_affinity = compute_v1.ReservationAffinity(
                consume_reservation_type="SPECIFIC_RESERVATION",  # Type of reservation to consume
                key="compute.googleapis.com/reservation-name",
                # To consume this reservation from any consumer projects, specify the owner project of the reservation
                values=[f"projects/{owner_project_id}/reservations/{reservation_name}"],
            )
            # Define the disks for the instance
            instance.disks = [
                compute_v1.AttachedDisk(
                    boot=True,  # Indicates that this is a boot disk
                    auto_delete=True,  # The disk will be deleted when the instance is deleted
                    initialize_params=compute_v1.AttachedDiskInitializeParams(
                        source_image="projects/debian-cloud/global/images/family/debian-13",
                        disk_size_gb=10,
                    ),
                )
            ]
            instance.network_interfaces = [
                compute_v1.NetworkInterface(
                    network="global/networks/default",  # The network to use
                    access_configs=[
                        compute_v1.AccessConfig(
                            name="External NAT",  # Name of the access configuration
                            type="ONE_TO_ONE_NAT",  # Type of access configuration
                        )
                    ],
                )
            ]
            # Create a request to insert the instance
            request = compute_v1.InsertInstanceRequest()
            request.zone = zone
            # The instance will be created in the shared project
            request.project = shared_project_id
            request.instance_resource = instance
        
            vm_client = compute_v1.InstancesClient()
            operation = vm_client.insert(request)
            wait_for_extended_operation(operation, "instance creation")
            print(f"Instance {instance_name} from project {owner_project_id} created.")
            # The instance is created in the shared project, so we return it from there.
            return vm_client.get(project=shared_project_id, zone=zone, instance=instance_name)
        
        




###  REST 

The following example shows how to create a specific reservation in zone `us-central1-a` for three N2 instances with 32 vCPUs, and Intel Cascade Lake as the minimum CPU platform. It also shows how to create a single instance to consume the reservation.

To create the example specific reservation and consume it, do the following:

  1. To create the example reservation, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `specificReservationRequired` field set to `true`:
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations
         
         {
           "name": "reservation-02",
           "specificReservation": {
             "count": "3",
             "instanceProperties": {
               "machineType": "n2-standard-32",
               "minCpuPlatform": "Intel Cascade Lake",
             }
           },
           **"specificReservationRequired": true**
         }
         

  2. To create a compute instance that consumes the example reservation, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, in the `reservationAffinity` field, include the following:

     * The `consumeReservationType` field set to `SPECIFIC_RESERVATION`.

     * The `key` field set to `compute.googleapis.com/reservation-name`.

     * The `values` field set to the URL of the reservation.

The request is similar to the following:
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances
    
    {
      "name": "instance-02",
      "machineType": "zones/us-central1-a/machineTypes/n2-standard-32",
      "minCpuPlatform": "Intel Cascade Lake",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/debian-cloud/global/images/family/debian-12"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      **"reservationAffinity": {
        "consumeReservationType": "SPECIFIC_RESERVATION",
        "key": "compute.googleapis.com/reservation-name",
        "values": [
          " RESERVATION_URL"
        ]
      }**
    }
    

Replace `RESERVATION_URL` with the URL of the reservation. Specify one of the following values:

     * If you created the reservation in the same project: `reservation-02`

     * If the reservation is in a different project: `projects/PROJECT_ID/reservations/reservation-02`




### Consume an auto-created reservation for a request in calendar mode

This reservation type allows new compute instances to consume a reservation that Compute Engine automatically creates (auto-creates) to fulfill a [future reservation in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

To consume this type of reservation, you must create a compute instance as follows:

  * The compute instance must [specifically target the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * The compute instance must be [stopped or deleted at the reservation end time](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm).

  * The compute instance must use the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). When you create a compute instance, you can specify this model as follows:

    * In the Google Cloud console, if you specify a supported machine type for future reservations in calendar mode, then the reservation-bound model is automatically selected.

    * In the gcloud CLI, include the `--provisioning-model` flag set to `reservation-bound`.

    * In the REST API, include the `provisioningModel` field set to `RESERVATION_BOUND`.




The following example creates a future reservation request in calendar mode for A3 Ultra instances. The example also shows the fields to specify when you create a standalone A3 Ultra instance to consume the auto-created reservation for the request.

To consume the example auto-created reservation, select one of the following options:

###  Console 

  1. Create an example request for five A3 Ultra instances and submit it for review:

     1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

     2. Click the **Future reservations** tab.

     3. Click add_box **Create future reservation**. The **Create a future reservation** page appears.

     4. Click the **GPUs** tab, and then, in the **GPU type** list, select **NVIDIA H200 141GB**. This action specifies an A3 Ultra instance.

     5. In the **Total capacity needed** field, enter `5`.

     6. In the **Reservation period** section, specify the start time and duration for your reservation period.

     7. Click **Search for capacity** , and then, in the **Available capacity** section, select one of the available machines.

     8. Click **Create**.

  2. At the request start time, to create an A3 Ultra instance to consume the example auto-created reservation, do the following:

**Important:** The following steps show how to create a single-NIC A3 Ultra instance, which is useful for quick tests. To create a multi-NIC A3 Ultra instance, see [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-instance-overview).
     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

     2. In the **Name** field, enter a name for the compute instance. For this example, enter `example-instance`.

     3. Specify the **Region** and **Zone** where the auto-created reservation exists. For this example, select **us-central1** and **us-central1-b** respectively.

     4. Click the **GPUs** tab, and then, in the **GPU type** list, select **NVIDIA H200 141GB**. This action specifies an A3 Ultra instance and sets the provisioning model to **Reservation-bound**.

     5. In the navigation menu, click **Advanced**.

     6. In the **Reservations** section, select **Choose a reservation** , and then click **Choose a reservation**.

     7. On the **Choose a reservation** pane, do the following:

        1. Select the example auto-created reservation.

        2. Click **Choose**.

     8. In the **Provisioning model** section, expand the **VM provisioning model advanced settings** section.

     9. In the **On VM termination** list, select **Stop** (default) or **Delete**.

     10. Click **Create**.




###  gcloud 

  1. To create an example request for five A3 Ultra VMs and submit it for review, use the [`gcloud compute future-reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/create):
         
         gcloud compute future-reservations create example-fr \
             --auto-delete-auto-created-reservations \
             --deployment-type=DENSE \
             --planning-status=SUBMITTED \
             --require-specific-reservation \
             --reservation-mode=CALENDAR \
             --reservation-name=example-reservation \
             --share-setting=local \
             --start-time=2026-03-05T00:00:00Z \
             --end-time=2026-03-19T00:00:00Z \
             --machine-type=a3-ultragpu-8g \
             --total-count=5 \
             --zone=us-central1-b
         

Assume that Google Cloud approves the request and Compute Engine automatically creates an empty reservation. At the request start time, on March 5, 2026, Compute Engine increases the number of reserved GPU VMs in the reservation. You can then consume the reservation.

  2. At the request start time, to create an A3 Ultra instance to consume the example auto-created reservation, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the following flags:

     * The `--instance-termination-action` flag.

     * The `--provisioning-model` flag set to `RESERVATION_BOUND`.

     * The `--reservation` flag.

     * The `--reservation-affinity` flag set to `specific`.

The command is similar to the following. For the full requirements to create an A3 Ultra instance, see [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-instance-overview).
    
    gcloud compute instance create example-a3ultra-instance  \
        --machine-type=a3-ultragpu-8g \
        **--instance-termination-action= TERMINATION_ACTION** \
        **--provisioning-model=RESERVATION_BOUND** \
        **--reservation-affinity=specific** \
        **--reservation= RESERVATION_URL** \
        --zone=us-central1-b \
        ...
    

The command includes the following values:

     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the VM at the end of the reservation period.

     * `RESERVATION_URL`: the URL of the reservation, which is formatted as follows:

       * If the auto-created reservation exists in your project: `example-reservation`.

       * If the auto-created reservation exists in a different project: `projects/PROJECT_ID/reservations/example-reservation`.




###  REST 

  1. To create an example request for five A3 Ultra instances and submit it for review, make a `POST` request to the [`futureReservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-b/futureReservations
         
         {
           "name": "example-request-calendar-mode",
           "autoDeleteAutoCreatedReservations": true,
           "deploymentType": "DENSE",
           "planningStatus": "SUBMITTED",
           "reservationMode": "CALENDAR",
           "reservationName": "example-reservation",
           "shareSettings": {
             "shareType": "LOCAL"
           },
           "specificReservationRequired": true,
           "specificSkuProperties": {
             "machineType": "a3-ultragpu-8g",
             "totalCount": 5
           },
           "timeWindow": {
             "startTime": "2026-03-05T00:00:00Z",
             "endTime": "2026-03-19T00:00:00Z"
           }
         }
         

Assume that Google Cloud approves the request and Compute Engine automatically creates an empty reservation. At the request start time, on March 5, 2026, Compute Engine increases the number of reserved GPU VMs in the reservation. You can then consume the reservation.

  2. At the request start time, to create an A3 Ultra instance to consume the example auto-created reservation, make a `POST` request to [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the following fields:

     * The `reservationAffinity.consumeReservationType` field set to `SPECIFIC_RESERVATION`.

     * The `reservationAffinity.key` field set to `compute.googleapis.com/reservation-name`.

     * The `reservationAffinity.values` field set to the URL of the reservation.

     * The `scheduling.instanceTerminationAction` field.

     * The `scheduling.provisioningModel` field set to `RESERVATION_BOUND`.

The request is similar to the following. For the full requirements to create an A3 Ultra instance, see [Create an A3 Ultra or A4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-instance-overview).
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-b/
    
    {
      {
        "machineType": "projects/example-project/zones/us-central1-b/machineTypes/a3-ultragpu-8g",
        "name": "example-a3ultra-instance",
        "reservationAffinity": {
          **"consumeReservationType": "SPECIFIC_RESERVATION"** ,
          **"key": "compute.googleapis.com/reservation-name"** ,
          **"values":[
            " RESERVATION_URL"
          ]**,
        },
        "scheduling": {
          **"instanceTerminationAction": " TERMINATION_ACTION"**,
          **"provisioningModel": "RESERVATION_BOUND"**
        },
        ...
      }
    }
    

The request body includes the following values:

     * `RESERVATION_URL`: the URL of the reservation, which is formatted as follows:

       * If the auto-created reservation exists in your project: `example-reservation`.

       * If the auto-created reservation exists in a different project: `projects/PROJECT_ID/reservations/example-reservation`.

     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the VM at the end of the reservation period.




## Test if compute instance properties match an automatically consumed reservation

Unlike specifically targeted reservations, automatically consumed reservations don't return an error when compute instance properties don't match. Instead, Compute Engine attempts to create a compute instance by using on-demand capacity. To verify that your compute instance properties match an automatically consumed reservation before you launch your workloads, test the properties against a test specifically targeted reservation that has the same properties.

To test if a compute instance's properties match an automatically consumed reservation, complete the following steps:

  1. **Create a test reservation** : create a specifically targeted reservation with the same compute instance properties as the automatically consumed reservation that you want to test. Set the number of reserved compute instances to `1`.

  2. **Create a test compute instance** : attempt to create a compute instance by targeting your test reservation. The outcome of this step is one of the following:

     * If you successfully create the compute instance, then the properties of the compute instance and the test reservation match.

     * If you can't create the compute instance and receive an error, then the properties might not match. To troubleshoot the error, see [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption).

  3. **Clean up resources** : if you successfully created a compute instance by targeting the test reservation, then delete the test resources to avoid unnecessary charges:

     * [Delete the test compute instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)

     * [Delete the test reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete)




## Verify reservations consumption

To verify reservations consumption, use one of the following methods:

  * To check which reservation a compute instance is consuming, [view the reservation that a compute instance is consuming](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view_the_reservation_that_an_instance_is_consuming).

  * To check which compute instances are consuming a specific reservation, [view a list of compute instances that are consuming a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view_a_list_of_instances_that_are_consuming_a_reservation).

  * To check the current reservation usage and see the number of compute instances that are consuming a reservation, and how many more compute instances can consume it, [view reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances).

  * To monitor reservations consumption data, which updates every 30 minutes, and receive alerts when reservations are consumed, [monitor reservations consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-monitor).

  * To analyze reservation consumption by using Cloud Billing data exported to BigQuery, see the following examples:

    * [View consumption for a given compute instance](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#view_consumption_for_a_given_instance)

    * [Analyze usage distribution for a given reservation](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#analyze_usage_distribution_for_a_given_reservation)

    * [List all the compute instances consuming a reservation](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#list_all_the_instances_consuming_a_reservation)

  * To view reservations consumption data, which updates every 24 hours, do one of the following:

    * To receive consumption reports in a Cloud Storage bucket to analyze consumption trends and identify unconsumed reservations, [view reservations usage report](https://docs.cloud.google.com/compute/docs/logging/usage-export).
    * To analyze consumption trends and plan for future capacity needs by viewing past and forecasted reservation consumption, [use Capacity Planner](https://docs.cloud.google.com/capacity-planner/docs/view-data).



## What's next

  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)


  * [Modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify)

  * [Delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
