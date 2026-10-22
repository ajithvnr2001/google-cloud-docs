---
url: https://docs.cloud.google.com/compute/docs/api/using-libraries/
title: Using client libraries \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:59.996515+00:00
---

# Using client libraries  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/api/using-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Using client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This document demonstrates how to use Cloud Client Libraries for Compute Engine. It describes how to list, create, and delete virtual machine (VM) instances. It also describes how to check the status of a long-running operation. You can run code samples from your local machine or on a VM instance, provided that you have authorized the sample correctly.

For a full list of available client libraries, including other client libraries and third-party open source libraries, see [Compute Engine Client Libraries](https://docs.cloud.google.com/compute/docs/api/libraries).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * Compute Engine



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Before you begin, follow the installation and authentication setup steps on [Compute Engine Client Libraries](https://docs.cloud.google.com/compute/docs/api/libraries) for the client library you want to use.

The examples in this document require you to provide information about the VM you want to create, like its location, machine type, and source image. For details on those values, see the following documents:

  * [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones)
  * [Machine types](https://docs.cloud.google.com/compute/docs/machine-resource)
  * [Images](https://docs.cloud.google.com/compute/docs/images)



## Creating an instance

The following example defines an instance that uses a specified name, machine type, network, source image, and disk. Then, it creates (inserts) the instance in a project and zone that you provide. In this example, the instance connects to the `default` network, which is created automatically for every project. You receive a message back when the API successfully creates the instance.

When you create a virtual machine (VM) instance, you must also attach a boot disk to the VM. The boot disk contains all of the necessary files required for starting a VM, including a public or custom OS image.

### C#
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System.Threading.Tasks;
    
    public class CreateInstanceAsyncSample
    {
        public async Task CreateInstanceAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string zone = "us-central1-a",
            string machineName = "test-machine",
            string machineType = "n1-standard-1",
            string diskImage = "projects/debian-cloud/global/images/family/debian-12",
            long diskSizeGb = 10,
            string networkName = "default")
        {
            [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instance.html) instance = new [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instance.html)
            {
                Name = machineName,
                // See https://cloud.google.com/compute/docs/machine-types for more information on machine types.
                MachineType = $"zones/{zone}/machineTypes/{machineType}",
                // Instance creation requires at least one persistent disk.
                Disks =
                {
                    new [AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk.html)
                    {
                        AutoDelete = true,
                        Boot = true,
                        Type = [ComputeEnumConstants](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.html).[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.html).[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.Type.html).[Persistent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.Type.html#Google_Cloud_Compute_V1_ComputeEnumConstants_AttachedDisk_Type_Persistent),
                        InitializeParams = new [AttachedDiskInitializeParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDiskInitializeParams.html) 
                        {
                            // See https://cloud.google.com/compute/docs/images for more information on available images.
                            SourceImage = diskImage,
                            DiskSizeGb = diskSizeGb
                        }
                    }
                },
                NetworkInterfaces = { new [NetworkInterface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkInterface.html) { Name = networkName } }
            };
    
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Insert the instance in the specified project and zone.
            var instanceCreation = await client.[InsertAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_InsertAsync_Google_Cloud_Compute_V1_InsertInstanceRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone, instance);
    
            // Wait for the operation to complete using client-side polling.
            // The server-side operation is not affected by polling,
            // and might finish successfully even if polling times out.
            await instanceCreation.PollUntilCompletedAsync();
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createInstance sends an instance creation request to the Compute Engine API and waits for it to complete.
    func createInstance(w io.Writer, projectID, zone, instanceName, machineType, sourceImage, networkName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// machineType := "n1-standard-1"
    	// sourceImage := "projects/debian-cloud/global/images/family/debian-12"
    	// networkName := "global/networks/default"
    
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
    			Disks: []*computepb.AttachedDisk{
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:  proto.Int64(10),
    						SourceImage: proto.String(sourceImage),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    			},
    			MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/%s", zone, machineType)),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					Name: proto.String(networkName),
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
    

### Java
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type;
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
    
    public class CreateInstance {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        createInstance(project, zone, instanceName);
      }
    
    
      // Create a new instance with the provided "instanceName" value in the specified project and zone.
      public static void createInstance(String project, String zone, String instanceName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // Below are sample values that can be replaced.
        // machineType: machine type of the VM being created.
        // *   This value uses the format zones/{zone}/machineTypes/{type_name}.
        // *   For a list of machine types, see https://cloud.google.com/compute/docs/machine-types
        // sourceImage: path to the operating system image to mount.
        // *   For details about images you can mount, see https://cloud.google.com/compute/docs/images
        // diskSizeGb: storage size of the boot disk to attach to the instance.
        // networkName: network interface to associate with the instance.
        String machineType = String.format("zones/%s/machineTypes/n1-standard-1", zone);
        String sourceImage = String
            .format("projects/debian-cloud/global/images/family/%s", "debian-13");
        long diskSizeGb = 10L;
        String networkName = "default";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          // Instance creation requires at least one persistent disk and one network interface.
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk =
              [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                  .setBoot(true)
                  .setAutoDelete(true)
                  .setType(Type.PERSISTENT.toString())
                  .setDeviceName("disk-1")
                  .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                      [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                          .setSourceImage(sourceImage)
                          .setDiskSizeGb(diskSizeGb)
                          .build())
                  .build();
    
          // Use the network interface provided in the networkName argument.
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
              .setName(networkName)
              .build();
    
          // Bind `instanceName`, `machineType`, `disk`, and `networkInterface` to an instance.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instanceResource =
              [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
                  .setName(instanceName)
                  .setMachineType(machineType)
                  .addDisks(disk)
                  .addNetworkInterfaces(networkInterface)
                  .build();
    
          System.out.printf("Creating instance: %s at %s %n", instanceName, zone);
    
          // Insert the instance in the specified project and zone.
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstanceResource(instanceResource)
              .build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
              insertInstanceRequest);
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance creation failed ! ! " + response);
            return;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME'
    // const machineType = 'n1-standard-1';
    // const sourceImage = 'projects/debian-cloud/global/images/family/debian-11';
    // const networkName = 'global/networks/default';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new instance with the values provided above in the specified project and zone.
    async function createInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      console.log(`Creating the ${instanceName} instance in ${zone}...`);
    
      const [response] = await instancesClient.insert({
        instanceResource: {
          name: instanceName,
          disks: [
            {
              // Describe the size and source image of the boot disk to attach to the instance.
              initializeParams: {
                diskSizeGb: '10',
                sourceImage,
              },
              autoDelete: true,
              boot: true,
              type: 'PERSISTENT',
            },
          ],
          machineType: `zones/${zone}/machineTypes/${machineType}`,
          networkInterfaces: [
            {
              // Use the network interface provided in the networkName argument.
              name: networkName,
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
    
    createInstance();

### PHP
    
    
    use Google\Cloud\Compute\V1\AttachedDisk;
    use Google\Cloud\Compute\V1\AttachedDisk\Type;
    use Google\Cloud\Compute\V1\AttachedDiskInitializeParams;
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\InsertInstanceRequest;
    
    /**
     * To correctly handle string enums in Cloud Compute library
     * use constants defined in the Enums subfolder.
     */
    use Google\Cloud\Compute\V1\Instance;
    use Google\Cloud\Compute\V1\NetworkInterface;
    
    /**
     * Creates an instance in the specified project and zone.
     *
     * @param string $projectId Project ID of the Cloud project to create the instance in.
     * @param string $zone Zone to create the instance in (like "us-central1-a").
     * @param string $instanceName Unique name for this Compute Engine instance.
     * @param string $machineType Machine type of the instance being created.
     * @param string $sourceImage Boot disk image name or family.
     * @param string $networkName Network interface to associate with the instance.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function create_instance(
        string $projectId,
        string $zone,
        string $instanceName,
        string $machineType = 'n1-standard-1',
        string $sourceImage = 'projects/debian-cloud/global/images/family/debian-11',
        string $networkName = 'global/networks/default'
    ) {
        // Set the machine type using the specified zone.
        $machineTypeFullName = sprintf('zones/%s/machineTypes/%s', $zone, $machineType);
    
        // Describe the source image of the boot disk to attach to the instance.
        $diskInitializeParams = (new AttachedDiskInitializeParams())
            ->setSourceImage($sourceImage);
        $disk = (new AttachedDisk())
            ->setBoot(true)
            ->setAutoDelete(true)
            ->setType(Type::name(Type::PERSISTENT))
            ->setInitializeParams($diskInitializeParams);
    
        // Use the network interface provided in the $networkName argument.
        $network = (new NetworkInterface())
            ->setName($networkName);
    
        // Create the Instance object.
        $instance = (new Instance())
            ->setName($instanceName)
            ->setDisks([$disk])
            ->setMachineType($machineTypeFullName)
            ->setNetworkInterfaces([$network]);
    
        // Insert the new Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new InsertInstanceRequest())
            ->setInstanceResource($instance)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->insert($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Created instance %s' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Instance creation failed: %s' . PHP_EOL, $error?->getMessage());
        }
    }

### Python
    
    
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
    
    

### Ruby
    
    
    require "google/cloud/compute/v1"
    
    # Sends an instance creation request to the Compute Engine API and waits for it to complete.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @param [String] zone name of the zone you want to use. For example: "us-west3-b"
    # @param [String] instance_name name of the new virtual machine.
    # @param [String] machine_type machine type of the VM being created. For example: "e2-standard-2"
    #         See https://cloud.google.com/compute/docs/machine-types for more information
    #         on machine types.
    # @param [String] source_image path to the operating system image to mount on your boot
    #         disk. This can be one of the public images
    #         (like "projects/debian-cloud/global/images/family/debian-12")
    #         or a private image you have access to.
    #         See https://cloud.google.com/compute/docs/images for more information on available images.
    # @param [String] network_name name of the network you want the new instance to use.
    #         For example: "global/networks/default" represents the `default`
    #         network interface, which is created automatically for each project.
    def create_instance project:, zone:, instance_name:,
                        machine_type: "n2-standard-2",
                        source_image: "projects/debian-cloud/global/images/family/debian-12",
                        network_name: "global/networks/default"
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      # Construct the instance object.
      # It can be either a hash or ::Google::Cloud::Compute::V1::Instance instance.
      instance = {
        name: instance_name,
        machine_type: "zones/#{zone}/machineTypes/#{machine_type}",
        # Instance creation requires at least one persistent disk.
        disks: [{
          auto_delete: true,
          boot: true,
          type: :PERSISTENT,
          initialize_params: {
            source_image: source_image,
            disk_size_gb: 10
          }
        }],
        network_interfaces: [{ name: network_name }]
      }
    
      # Prepare a request to create the instance in the specified project and zone.
      request = { project: project, zone: zone, instance_resource: instance }
    
      puts "Creating the #{instance_name} instance in #{zone}..."
      begin
        # Send the insert request.
        operation = client.insert request
        # Wait for the create operation to complete.
        operation = wait_until_done operation: operation
    
        compute_operation = operation.operation
        if operation.error?
          warn "Error during creation:", compute_operation.error.errors.map { |e| "#{e.code}: #{e.message}" }
        else
          warn "Warning during creation:", compute_operation.warnings unless compute_operation.warnings.empty?
          puts "Instance #{instance_name} created."
        end
      rescue ::Google::Cloud::Error => e
        warn "Exception during creation:", e
      end
    end

### Rust
    
    
    use google_cloud_compute_v1::client::Instances;
    use google_cloud_compute_v1::model::{
        AttachedDisk, AttachedDiskInitializeParams, Instance, NetworkInterface,
    };
    use google_cloud_lro::Poller;
    
    pub async fn sample(client: &Instances, project_id: &str, name: &str) -> anyhow::Result<()> {
        const ZONE: &str = "us-central1-a";
    
        let instance = Instance::new()
            .set_machine_type(format!("zones/{ZONE}/machineTypes/f1-micro"))
            .set_name(name)
            .set_description("A test VM created by the Rust client library.")
            .set_labels([("source", "compute_instances_create")])
            .set_disks([AttachedDisk::new()
                .set_initialize_params(
                    AttachedDiskInitializeParams::new()
                        .set_source_image("projects/cos-cloud/global/images/family/cos-stable"),
                )
                .set_boot(true)
                .set_auto_delete(true)])
            .set_network_interfaces([NetworkInterface::new().set_network("global/networks/default")]);
    
        let operation = client
            .insert()
            .set_project(project_id)
            .set_zone(ZONE)
            .set_body(instance)
            .poller()
            .until_done()
            .await?
            .to_result()?;
        println!("Instance successfully created: {operation:?}");
    
        Ok(())
    }

## Listing instances

The following examples list instances in a project, either in one zone or across all zones:

### C#
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class ListZoneInstancesAsyncSample
    {
        public async Task<IList<Instance>> ListZoneInstancesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id", 
            string zone = "us-central1-a")
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
            IList<Instance> allInstances = new List<Instance>();
    
            // Make the request to list all VM instances in the given zone in the specified project.
            await foreach(var instance in client.[ListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_ListAsync_Google_Cloud_Compute_V1_ListInstancesRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone))
            {
                // The result is an Instance collection.
                Console.WriteLine($"Instance: {instance.Name}");
                allInstances.Add(instance);
            }
    
            return allInstances;
        }
    }
    

You can also get a list of instances across all zones in your project:
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class ListAllInstancesAsyncSample
    {
        public async Task<IList<Instance>> ListAllInstancesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id") 
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
            IList<Instance> allInstances = new List<Instance>();
    
            // Make the request to list all VM instances in a project.
            await foreach (var instancesByZone in client.[AggregatedListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_AggregatedListAsync_Google_Cloud_Compute_V1_AggregatedListInstancesRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId))
            {
                // The result contains a KeyValuePair collection, where the key is a zone and the value
                // is a collection of instances in that zone.
                Console.WriteLine($"Instances for zone: {instancesByZone.Key}");
                foreach (var instance in instancesByZone.Value.[Instances](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instances.html))
                {
                    Console.WriteLine($"-- Name: {instance.Name}");
                    allInstances.Add(instance);
                }
            }
    
            return allInstances;
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    )
    
    // listInstances prints a list of instances created in given project in given zone.
    func listInstances(w io.Writer, projectID, zone string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.ListInstancesRequest{
    		Project: projectID,
    		Zone:    zone,
    	}
    
    	it := instancesClient.List(ctx, req)
    	fmt.Fprintf(w, "Instances found in zone %s:\n", zone)
    	for {
    		instance, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s %s\n", instance.GetName(), instance.GetMachineType())
    	}
    	return nil
    }
    

You can also get a list of instances across all zones in your project:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/protobuf/proto"
    )
    
    // listAllInstances prints all instances present in a project, grouped by their zone.
    func listAllInstances(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	// Use the `MaxResults` parameter to limit the number of results that the API returns per response page.
    	req := &computepb.AggregatedListInstancesRequest{
    		Project:    projectID,
    		MaxResults: proto.Uint32(3),
    	}
    
    	it := instancesClient.AggregatedList(ctx, req)
    	fmt.Fprintf(w, "Instances found:\n")
    	// Despite using the `MaxResults` parameter, you don't need to handle the pagination
    	// yourself. The returned iterator object handles pagination
    	// automatically, returning separated pages as you iterate over the results.
    	for {
    		pair, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		instances := pair.Value.Instances
    		if len(instances) > 0 {
    			fmt.Fprintf(w, "%s\n", pair.Key)
    			for _, instance := range instances {
    				fmt.Fprintf(w, "- %s %s\n", instance.GetName(), instance.GetMachineType())
    			}
    		}
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import java.io.IOException;
    
    public class ListInstance {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample
        String project = "your-project-id";
        String zone = "zone-name";
        listInstances(project, zone);
      }
    
      // List all instances in the given zone in the specified project ID.
      public static void listInstances(String project, String zone) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to 
        // safely clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          // Set the project and zone to retrieve instances present in the zone.
          System.out.printf("Listing instances from %s in %s:", project, zone);
          for ([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) zoneInstance : instancesClient.list(project, zone).iterateAll()) {
            System.out.println(zoneInstance.getName());
          }
          System.out.println("####### Listing instances complete #######");
        }
      }
    }

You can also get a list of instances across all zones in your project:
    
    
    import com.google.cloud.compute.v1.[AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).AggregatedListPagedResponse;
    import com.google.cloud.compute.v1.[InstancesScopedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesScopedList.html);
    import java.io.IOException;
    import java.util.Map;
    
    public class ListAllInstances {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample
        String project = "your-project-id";
        listAllInstances(project);
      }
    
      // List all instances in the specified project ID.
      public static AggregatedListPagedResponse listAllInstances(String project) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to
        // safely clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          // Use the `setMaxResults` parameter to limit the number of results
          // that the API returns per response page.
          [AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest.html) aggregatedListInstancesRequest = [AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest.html)
              .newBuilder()
              .setProject(project)
              .setMaxResults(5)
              .build();
    
          [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).AggregatedListPagedResponse response = instancesClient
              .aggregatedList(aggregatedListInstancesRequest);
    
          // Despite using the `setMaxResults` parameter, you don't need to handle the pagination
          // yourself. The returned `AggregatedListPager` object handles pagination
          // automatically, requesting next pages as you iterate over the results.
          for (Map.Entry<String, InstancesScopedList> zoneInstances : response.iterateAll()) {
            // Instances scoped by each zone
            String zone = zoneInstances.getKey();
            if (!zoneInstances.getValue().getInstancesList().isEmpty()) {
              // zoneInstances.getKey() returns the fully qualified address.
              // Hence, strip it to get the zone name only
              System.out.printf("Instances at %s: ", zone.substring(zone.lastIndexOf('/') + 1));
              for (Instance instance : zoneInstances.getValue().getInstancesList()) {
                System.out.println(instance.getName());
              }
            }
          }
          System.out.println("####### Listing all instances complete #######");
          return response;
        }
      }
    
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // List all instances in the given zone in the specified project.
    async function listInstances() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instanceList] = await instancesClient.list({
        project: projectId,
        zone,
      });
    
      console.log(`Instances found in zone ${zone}:`);
    
      for (const instance of instanceList) {
        console.log(` - ${instance.name} (${instance.machineType})`);
      }
    }
    
    listInstances();

You can also get a list of instances across all zones in your project:
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // List all instances in the specified project.
    async function listAllInstances() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      //Use the `maxResults` parameter to limit the number of results that the API returns per response page.
      const aggListRequest = instancesClient.aggregatedListAsync({
        project: projectId,
        maxResults: 5,
      });
    
      console.log('Instances found:');
    
      // Despite using the `maxResults` parameter, you don't need to handle the pagination
      // yourself. The returned object handles pagination automatically,
      // requesting next pages as you iterate over the results.
      for await (const [zone, instancesObject] of aggListRequest) {
        const instances = instancesObject.instances;
    
        if (instances && instances.length > 0) {
          console.log(` ${zone}`);
          for (const instance of instances) {
            console.log(` - ${instance.name} (${instance.machineType})`);
          }
        }
      }
    }
    
    listAllInstances();

### PHP
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\ListInstancesRequest;
    
    /**
     * List all instances for a particular Cloud project and zone.
     *
     * @param string $projectId Your Google Cloud project ID.
     * @param string $zone Zone to list instances for (like "us-central1-a").
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_instances(string $projectId, string $zone)
    {
        // List Compute Engine instances using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new ListInstancesRequest())
            ->setProject($projectId)
            ->setZone($zone);
        $instancesList = $instancesClient->list($request);
    
        printf('Instances for %s (%s)' . PHP_EOL, $projectId, $zone);
        foreach ($instancesList as $instance) {
            printf(' - %s' . PHP_EOL, $instance->getName());
        }
    }

You can also get a list of instances across all zones in your project:
    
    
    use Google\Cloud\Compute\V1\AggregatedListInstancesRequest;
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    
    /**
     * List all instances for a particular Cloud project.
     *
     * @param string $projectId Your Google Cloud project ID.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_all_instances(string $projectId)
    {
        // List Compute Engine instances using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new AggregatedListInstancesRequest())
            ->setProject($projectId);
        $allInstances = $instancesClient->aggregatedList($request);
    
        printf('All instances for %s' . PHP_EOL, $projectId);
        foreach ($allInstances as $zone => $zoneInstances) {
            $instances = $zoneInstances->getInstances();
            if (count($instances) > 0) {
                printf('Zone - %s' . PHP_EOL, $zone);
                foreach ($instances as $instance) {
                    printf(' - %s' . PHP_EOL, $instance->getName());
                }
            }
        }
    }

### Python
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_instances(project_id: str, zone: str) -> Iterable[compute_v1.Instance]:
        """
        List all instances in the given zone in the specified project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
        Returns:
            An iterable collection of Instance objects.
        """
        instance_client = compute_v1.InstancesClient()
        instance_list = instance_client.list(project=project_id, zone=zone)
    
        print(f"Instances found in zone {zone}:")
        for instance in instance_list:
            print(f" - {instance.name} ({instance.machine_type})")
    
        return instance_list
    
    

You can also get a list of instances across all zones in your project:
    
    
    from __future__ import annotations
    
    from collections import defaultdict
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_all_instances(
        project_id: str,
    ) -> dict[str, Iterable[compute_v1.Instance]]:
        """
        Returns a dictionary of all instances present in a project, grouped by their zone.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
        Returns:
            A dictionary with zone names as keys (in form of "zones/{zone_name}") and
            iterable collections of Instance objects as values.
        """
        instance_client = compute_v1.InstancesClient()
        request = compute_v1.AggregatedListInstancesRequest()
        request.project = project_id
        # Use the `max_results` parameter to limit the number of results that the API returns per response page.
        request.max_results = 50
    
        agg_list = instance_client.aggregated_list(request=request)
    
        all_instances = defaultdict(list)
        print("Instances found:")
        # Despite using the `max_results` parameter, you don't need to handle the pagination
        # yourself. The returned `AggregatedListPager` object handles pagination
        # automatically, returning separated pages as you iterate over the results.
        for zone, response in agg_list:
            if response.instances:
                all_instances[zone].extend(response.instances)
                print(f" {zone}:")
                for instance in response.instances:
                    print(f" - {instance.name} ({instance.machine_type})")
        return all_instances
    
    

### Ruby
    
    
    require "google/cloud/compute/v1"
    
    # Lists all instances in the given zone in the specified project.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @param [String] zone name of the zone you want to use. For example: "us-west3-b"
    # @return [Array<::Google::Cloud::Compute::V1::Instance>] Array of instances.
    def list_instances project:, zone:
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      # Send the request to list all VM instances in the given zone in the specified project.
      instance_list = client.list project: project, zone: zone
    
      puts "Instances found in zone #{zone}:"
      instances = []
      instance_list.each do |instance|
        puts " - #{instance.name} (#{instance.machine_type})"
        instances << instance
      end
      instances
    end

You can also get a list of instances across all zones in your project:
    
    
    require "google/cloud/compute/v1"
    
    # Returns a dictionary of all instances present in a project, grouped by their zone.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @return [Hash<String, Array<::Google::Cloud::Compute::V1::Instance>>] A hash with zone names
    #   as keys (in form of "zones/{zone_name}") and arrays of instances as values.
    def list_all_instances project:
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      # Send the request to list all VM instances in a project.
      agg_list = client.aggregated_list project: project
      all_instances = {}
      puts "Instances found:"
      # The result contains a Map collection, where the key is a zone and the value
      # is a collection of instances in that zone.
      agg_list.each do |zone, list|
        next if list.instances.empty?
        all_instances[zone] = list.instances
        puts " #{zone}:"
        list.instances.each do |instance|
          puts " - #{instance.name} (#{instance.machine_type})"
        end
      end
      all_instances
    end

### Rust
    
    
    use google_cloud_compute_v1::client::Instances;
    use google_cloud_gax::paginator::ItemPaginator;
    
    pub async fn sample(client: &Instances, project_id: &str) -> anyhow::Result<()> {
        let mut items = client.aggregated_list().set_project(project_id).by_item();
        while let Some((zone, scoped_list)) = items.next().await.transpose()? {
            for instance in scoped_list.instances {
                println!(
                    "Instance {} found in zone: {zone}",
                    instance.name.expect("name should be Some()")
                );
            }
        }
    
        Ok(())
    }

## Deleting an instance

The following example deletes an instance based on the project, zone, and instance name that you provide. You receive a message back when the API successfully deletes the instance.

The delete operation is _irreversible_. When you only want to turn off an instance temporarily, consider [stopping](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) or [suspending](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) the instance instead.

If the `autoDelete` parameter is `true` for the instance, you also delete the boot disk when you delete the instance. This setting is set to `true` by default during instance creation, and you can [adjust it](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete) when your use case calls for disks and instances to be deleted separately.

### C#
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System.Threading.Tasks;
    
    public class DeleteInstanceAsyncSample
    {
        public async Task DeleteInstanceAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string zone = "us-central1-a",
            string machineName = "test-machine")
        {
    
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Make the request to delete a VM instance.
            var instanceDeletion = await client.[DeleteAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_DeleteAsync_Google_Cloud_Compute_V1_DeleteInstanceRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone, machineName);
    
            // Wait for the operation to complete using client-side polling.
            await instanceDeletion.PollUntilCompletedAsync();
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // deleteInstance sends a delete request to the Compute Engine API and waits for it to complete.
    func deleteInstance(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.DeleteInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	op, err := instancesClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance deleted\n")
    
    	return nil
    }
    

### Java
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteInstance {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        deleteInstance(project, zone, instanceName);
      }
    
      // Delete the instance specified by `instanceName`
      // if it's present in the given project and zone.
      public static void deleteInstance(String project, String zone, String instanceName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          System.out.printf("Deleting instance: %s ", instanceName);
    
          // Describe which instance is to be deleted.
          [DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html) deleteInstanceRequest = [DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName).build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.deleteAsync(
              deleteInstanceRequest);
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance deletion failed ! ! " + response);
            return;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Delete the instance specified by `instanceName` if it's present in the given project and zone.
    async function deleteInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      console.log(`Deleting ${instanceName} from ${zone}...`);
    
      const [response] = await instancesClient.delete({
        project: projectId,
        zone,
        instance: instanceName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the delete operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance deleted.');
    }
    
    deleteInstance();

### PHP
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\DeleteInstanceRequest;
    
    /**
     * Delete an instance.
     *
     * @param string $projectId Your Google Cloud project ID.
     * @param string $zone Zone where the instance you want to delete is (like "us-central1-a").
     * @param string $instanceName Unique name for the Compute instance to delete.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function delete_instance(
        string $projectId,
        string $zone,
        string $instanceName
    ) {
        // Delete the Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new DeleteInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->delete($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Deleted instance %s' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Failed to delete instance: %s' . PHP_EOL, $error?->getMessage());
        }
    }

### Python
    
    
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
    
    
    def delete_instance(project_id: str, zone: str, machine_name: str) -> None:
        """
        Send an instance deletion request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            machine_name: name of the machine you want to delete.
        """
        instance_client = comp[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)t[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)    print(f"Deleting {machine_name} from {zone}...")
        operation = instinstance_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_delete)      project=project_id, zone=zone, instance=machine_name
        )
        wait_for_extended_operation(operation, "instance deletion")
        print(f"Instance {machine_name} deleted.")
    
    

### Ruby
    
    
    require "google/cloud/compute/v1"
    
    # Sends an instance deletion request to the Compute Engine API and waits for it to complete.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @param [String] zone name of the zone you want to use. For example: "us-west3-b"
    # @param [String] instance_name name of the instance you want to delete.
    def delete_instance project:, zone:, instance_name:
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      puts "Deleting #{instance_name} from #{zone}..."
      begin
        # Make the request to delete a VM instance.
        operation = client.delete project: project, zone: zone, instance: instance_name
        # Wait for the delete operation to complete.
        operation = wait_until_done operation: operation
    
        compute_operation = operation.operation
        if operation.error?
          warn "Error during deletion:", compute_operation.error.errors.map { |e| "#{e.code}: #{e.message}" }
        else
          warn "Warning during deletion:", compute_operation.warnings unless compute_operation.warnings.empty?
          puts "Instance #{instance_name} deleted."
        end
      rescue ::Google::Cloud::Error => e
        warn "Exception during deletion:", e
      end
    end

### Rust
    
    
    use google_cloud_compute_v1::client::Instances;
    use google_cloud_lro::Poller;
    
    pub async fn sample(client: &Instances, project_id: &str, name: &str) -> anyhow::Result<()> {
        const ZONE: &str = "us-central1-a";
    
        let operation = client
            .delete()
            .set_project(project_id)
            .set_zone(ZONE)
            .set_instance(name)
            .poller()
            .until_done()
            .await?
            .to_result()?;
        println!("Instance successfully deleted: {operation:?}");
    
        Ok(())
    }

## Checking operation status

Requests to the Compute Engine API that modify resources such as instances immediately return a response acknowledging your request. The acknowledgement includes information about the status of the requested operation.

Depending on the nature of the operation, it can take some time to complete. The following example waits until an operation completes before continuing code execution:

### C#
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System.Threading.Tasks;
    
    public class CreateInstanceAsyncSample
    {
        public async Task CreateInstanceAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string zone = "us-central1-a",
            string machineName = "test-machine",
            string machineType = "n1-standard-1",
            string diskImage = "projects/debian-cloud/global/images/family/debian-12",
            long diskSizeGb = 10,
            string networkName = "default")
        {
            [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instance.html) instance = new [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instance.html)
            {
                Name = machineName,
                // See https://cloud.google.com/compute/docs/machine-types for more information on machine types.
                MachineType = $"zones/{zone}/machineTypes/{machineType}",
                // Instance creation requires at least one persistent disk.
                Disks =
                {
                    new [AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk.html)
                    {
                        AutoDelete = true,
                        Boot = true,
                        Type = [ComputeEnumConstants](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.html).[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.html).[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.Type.html).[Persistent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.Type.html#Google_Cloud_Compute_V1_ComputeEnumConstants_AttachedDisk_Type_Persistent),
                        InitializeParams = new [AttachedDiskInitializeParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDiskInitializeParams.html) 
                        {
                            // See https://cloud.google.com/compute/docs/images for more information on available images.
                            SourceImage = diskImage,
                            DiskSizeGb = diskSizeGb
                        }
                    }
                },
                NetworkInterfaces = { new [NetworkInterface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkInterface.html) { Name = networkName } }
            };
    
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Insert the instance in the specified project and zone.
            var instanceCreation = await client.[InsertAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_InsertAsync_Google_Cloud_Compute_V1_InsertInstanceRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone, instance);
    
            // Wait for the operation to complete using client-side polling.
            // The server-side operation is not affected by polling,
            // and might finish successfully even if polling times out.
            await instanceCreation.PollUntilCompletedAsync();
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    )
    
    // waitForOperation waits for an operation to be completed. Calling this function will block until the operation is finished.
    func waitForOperation(w io.Writer, projectID string, operation *compute.Operation) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// opName := "your_operation_name"
    
    	ctx := context.Background()
    
    	if err := operation.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Operation finished\n")
    
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html);
    import java.io.IOException;
    
    public class WaitForOperation {
    
      public static void main(String[] args) throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // operation: Specify the operation to wait.
        String project = "your-project-id";
        [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).newBuilder().build();
    
        waitForOperation(project, operation);
      }
    
      // Waits for the specified operation to complete.
      public static void waitForOperation(String project, [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation)
          throws IOException {
        try ([ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html) zoneOperationsClient = [ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html).create()) {
    
          // Check if the operation hasn't been completed already.
          if (operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() != [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).DONE) {
            String zone = operation.[getZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getZone__)();
            zone = zone.substring(zone.lastIndexOf("/") + 1);
    
            // Wait for the operation to complete.
            [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = zoneOperationsClient.wait(project, zone, operation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getName__)());
    
            // Check if the operation has errors.
            if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
              System.out.println("Error in executing the operation ! ! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
              return;
            }
            System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
            return;
          }
          System.out.println("Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const operationString = 'YOUR_OPERATION_STRING'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Parse stringified operation to the object instance.
    let operation = JSON.parse(operationString);
    
    async function waitForOperation() {
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Operation finished.');
    }
    
    waitForOperation();

### PHP
    
    
    // Wait for the operation to complete.
    $operation->pollUntilComplete();
    if ($operation->operationSucceeded()) {
        printf('Created instance %s' . PHP_EOL, $instanceName);
    } else {
        $error = $operation->getError();
        printf('Instance creation failed: %s' . PHP_EOL, $error?->getMessage());
    }

### Python
    
    
    import time
    
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_operation(
        operation: [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Operation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Operation.html), project_id: str
    ) -> compute_v1.Operation:
        """
        This method waits for an operation to be completed. Calling this function
        will block until the operation is finished.
    
        Args:
            operation: The Operation object representing the operation you want to
                wait on.
            project_id: project ID or project number of the Cloud project you want to use.
    
        Returns:
            Finished Operation object.
        """
        kwargs = {"project": project_id, "operation": operation.name}
        if operation.zone:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ZoneOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.zone_operations.ZoneOperationsClient.html)()
            # Operation.zone is a full URL address of a zone, so we need to extract just the name
            kwargs["zone"] = operation.zone.rsplit("/", maxsplit=1)[1]
        elif operation.region:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_operations.RegionOperationsClient.html)()
            # Operation.region is a full URL address of a region, so we need to extract just the name
            kwargs["region"] = operation.region.rsplit("/", maxsplit=1)[1]
        else:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_operations.GlobalOperationsClient.html)()
    
        while True:
            result = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_operations.GlobalOperationsClient.html#google_cloud_compute_v1_services_global_operations_GlobalOperationsClient_get)(**kwargs)
    
            if result.status == [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Operation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Operation.html).Status.DONE:
                print("Operation finished.")
                if result.error:
                    print(f"Error during operation: {result.error}")
                return result
    
            print("Waiting for operation to complete...")
            time.sleep(2)
    
    

### Ruby
    
    
    require "google/cloud/compute/v1"
    
    require "time"
    
    # Waits for an operation to be completed. Calling this method
    # will block until the operation is finished or timed out.
    #
    # @param [::Gapic::GenericLRO::Operation] operation The operation to wait for.
    # @param [Numeric] timeout seconds until timeout (default is 3 minutes)
    # @return [::Gapic::GenericLRO::Operation] Finished Operation object.
    def wait_until_done operation:, timeout: 3 * 60
      retry_policy = ::Gapic::Operation::RetryPolicy.new initial_delay: 0.2, multiplier: 2, max_delay: 1, timeout: timeout
      operation.wait_until_done! retry_policy: retry_policy
    end

### Rust
    
    
    use google_cloud_compute_v1::client::{Instances, ZoneOperations};
    use google_cloud_compute_v1::model::{
        AttachedDisk, AttachedDiskInitializeParams, Instance, NetworkInterface,
    };
    use google_cloud_compute_v1::model::{Operation, operation::Status};
    
    pub async fn sample(client: &Instances, project_id: &str, name: &str) -> anyhow::Result<()> {
        const ZONE: &str = "us-central1-a";
        let operations_client = ZoneOperations::builder().build().await?;
    
        // Start an operation, in this example we use a VM creation.
        let mut op = start_instance_insert(client, project_id, ZONE, name).await?;
    
        // Manually wait for the operation.
        let operation = loop {
            if op.status.as_ref().is_some_and(|s| s == &Status::Done) {
                break op;
            }
            let Some(name) = op.name.clone() else {
                return Err(anyhow::Error::msg(format!(
                    "the operation name should be set, operation={op:?}"
                )));
            };
            println!("polling operation {op:?}");
            op = operations_client
                .wait()
                .set_project(project_id)
                .set_zone(ZONE)
                .set_operation(name)
                .send()
                .await?;
        };
    
        println!("Instance creation finished: {operation:?}");
        // Check if there was an error.
        if let Err(error) = operation.to_result() {
            println!("Instance creation failed: {error:?}");
            return Err(anyhow::Error::msg(format!(
                "instance creation failed with: {error:?}"
            )));
        }
    
        Ok(())
    }
    
    async fn start_instance_insert(
        client: &Instances,
        project_id: &str,
        zone: &str,
        name: &str,
    ) -> anyhow::Result<Operation> {
        let instance = Instance::new()
            .set_machine_type(format!("zones/{zone}/machineTypes/f1-micro"))
            .set_name(name)
            .set_description("A test VM created by the Rust client library.")
            .set_labels([("source", "compute_instances_create")])
            .set_disks([AttachedDisk::new()
                .set_initialize_params(
                    AttachedDiskInitializeParams::new()
                        .set_source_image("projects/cos-cloud/global/images/family/cos-stable"),
                )
                .set_boot(true)
                .set_auto_delete(true)])
            .set_network_interfaces([NetworkInterface::new().set_network("global/networks/default")]);
    
        // Start the operation without waiting for it to complete. This will require
        // manually waiting for the operation. In most cases we recommend you use
        // `.poller().until_done()` instead of `.send()`:
        let op = client
            .insert()
            .set_project(project_id)
            .set_zone(zone)
            .set_body(instance)
            .send()
            .await?;
        Ok(op)
    }
    

## Handling default values

For _some_ fields that you choose not to send in requests or don't receive in responses, the Compute Engine API assumes non-zero default values. Google specifies these default values in [API reference](https://docs.cloud.google.com/compute/docs/reference/latest) field descriptions and in the comments of the protocol buffers that the client libraries are built on.

These protocol buffers are in [protocol buffers v3](https://docs.cloud.google.com/apis/design/proto3) format and report a zero value for fields that aren't present, even when the Compute Engine API server uses a different default. Zero values for fields that aren't present are as follows: `0` for numbers, `false` for booleans, empty for strings.

In the protocol buffers that the Compute Engine Cloud Client Libraries are built on, all non-required fields are marked as proto3 `optional`. Consider a field named `name` marked as `optional` in a hypothetical protocol buffer message named `MyRecord`. For that field, do the following:

  * **When sending a request:** If you intend to send an explicit zero value to the server for the field, you must set it in the request message: `MyRecord.name=""`. Otherwise, the server uses its default value. Before you make the request to the server, you can confirm based on field presence that you set the zero value in your code. A field is present when something like the hypothetical `MyRecord.hasName()` method returns `true`.

  * **When handling a response:** If a field marked as `optional` is absent or has an explicit zero value, check the API reference to see what value you should assume for the field. For some fields, a zero value in the response is a valid non-default value and represents the intended value of the field.




In general, check the API reference documentation to see how the server interprets an absent value or zero value for a field, as it varies by method.

For example, consider changing the prefix of the name of the usage report (`reportNamePrefix`) for your project. When the server receives an empty string value or doesn't receive the field at all, it uses a certain default value (`usage_gce`, as described in the reference for [`projects.setUsageExportBucket`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/setUsageExportBucket)) to generate the report.

Although the server explicitly returns an empty string for `reportNamePrefix`, the reference for [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get) correctly indicates that the report is generated with the default value `usage_gce` for `reportNamePrefix`.

### C#
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class SetUsageExportBucketAsyncSample
    {
        public async Task SetUsageExportBucketAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string bucketName = "usage-export-bucket",
            string reportNamePrefix = "usage-report")
        {
            if (string.IsNullOrEmpty(reportNamePrefix))
            {
                Console.WriteLine(
                    $"Setting {nameof([UsageExportLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html).[ReportNamePrefix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html#Google_Cloud_Compute_V1_UsageExportLocation_ReportNamePrefix))} " +
                    $"to null or empty values causes the report to have the default prefix of `usage_gce`.");
            }
    
            [UsageExportLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html) exportLocation = new [UsageExportLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html)
            {
                BucketName = bucketName,
                ReportNamePrefix = reportNamePrefix,
            };
    
            // Initialize the client that will be used to send project-related requests.
            // You should reuse the same client for multiple requests.
            [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html) client = await [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html#Google_Cloud_Compute_V1_ProjectsClient_CreateAsync_System_Threading_CancellationToken_)();
    
            var operation = await client.[SetUsageExportBucketAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html#Google_Cloud_Compute_V1_ProjectsClient_SetUsageExportBucketAsync_Google_Cloud_Compute_V1_SetUsageExportBucketProjectRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, exportLocation);
            // Wait for the operation to complete using client-side polling.
            await operation.PollUntilCompletedAsync();
        }
    }
    

Verify that the server used the default prefix value `usage_gce`:
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class GetUsageExportBucketAsyncSample
    {
        public async Task<Project> GetUsageExportBucketAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id")
        {
            // Initialize the client that will be used to send project-related requests.
            // You should reuse the same client for multiple requests.
            [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html) client = await [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html#Google_Cloud_Compute_V1_ProjectsClient_CreateAsync_System_Threading_CancellationToken_)();
    
            [Project](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Project.html) project = await client.[GetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient.html#Google_Cloud_Compute_V1_ProjectsClient_GetAsync_Google_Cloud_Compute_V1_GetProjectRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId);
    
            if (project.[UsageExportLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Project.html#Google_Cloud_Compute_V1_Project_UsageExportLocation) is null)
            {
                Console.WriteLine("This project has no usage report export location configured.");
            }
            else if (string.IsNullOrEmpty(project.[UsageExportLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Project.html#Google_Cloud_Compute_V1_Project_UsageExportLocation).[ReportNamePrefix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html#Google_Cloud_Compute_V1_UsageExportLocation_ReportNamePrefix)))
            {
                Console.WriteLine(
                    $"Setting {nameof([UsageExportLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html).[ReportNamePrefix](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UsageExportLocation.html#Google_Cloud_Compute_V1_UsageExportLocation_ReportNamePrefix))} " +
                    $"to null or empty values causes the report to have the default prefix of `usage_gce`.");
            }
    
            return project;
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // setUsageExportBucket sets the Compute Engine usage export bucket for the Cloud project.
    // This sample presents how to interpret the default value for the report name prefix parameter.
    func setUsageExportBucket(w io.Writer, projectID, bucketName, reportNamePrefix string) error {
    	// projectID := "your_project_id"
    	// bucketName := "your_bucket_name"
    	// reportNamePrefix := ""
    	ctx := context.Background()
    	projectsClient, err := compute.[NewProjectsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ProjectsClient_NewProjectsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProjectsRESTClient: %w", err)
    	}
    	defer projectsClient.Close()
    
    	// Updating the setting with an empty UsageExportLocationResource value disables the usage report generation.
    	req := &computepb.SetUsageExportBucketProjectRequest{
    		Project: projectID,
    		UsageExportLocationResource: &computepb.UsageExportLocation{
    			BucketName:       proto.String(bucketName),
    			ReportNamePrefix: proto.String(reportNamePrefix),
    		},
    	}
    
    	if reportNamePrefix == "" {
    		// Sending an empty value for reportNamePrefix results in the next usage report being generated
    		// with the default prefix value "usage_gce". (see: https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
    		fmt.Fprintf(w, "Setting reportNamePrefix to empty value causes the report to have the default prefix value `usage_gce`.\n")
    	}
    
    	op, err := projectsClient.SetUsageExportBucket(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to set usage export bucket %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Usage export bucket has been set\n")
    
    	return nil
    }
    

Verify that the server used the default prefix value `usage_gce`:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // getUsageExportBucket retrieves the Compute Engine usage export bucket for the Cloud project. Replaces the empty value returned by the API with the default value used to generate report file names.
    func getUsageExportBucket(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    	ctx := context.Background()
    	projectsClient, err := compute.[NewProjectsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ProjectsClient_NewProjectsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProjectsRESTClient: %w", err)
    	}
    	defer projectsClient.Close()
    
    	// Updating the setting with an empty UsageExportLocationResource value disables the usage report generation.
    	req := &computepb.GetProjectRequest{
    		Project: projectID,
    	}
    
    	project, err := projectsClient.Get(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get project: %w", err)
    	}
    
    	usageExportLocation := project.GetUsageExportLocation()
    
    	if usageExportLocation == nil || usageExportLocation.GetBucketName() == "" {
    		// The usage reports are disabled.
    		return nil
    	}
    
    	if usageExportLocation.ReportNamePrefix != nil {
    		// Although the server explicitly sent the empty string value,
    		// the next usage report generated with these settings still has the default prefix value `usage_gce`.
    		// (see https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
    		fmt.Fprintf(w, "Report name prefix not set, replacing with default value of `usage_gce`.\n")
    		usageExportLocation.ReportNamePrefix = proto.String("usage_gce")
    	}
    
    	fmt.Fprintf(w, "Returned ReportNamePrefix: %s\n", usageExportLocation.GetReportNamePrefix())
    
    	return nil
    }
    

### Java
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project.html);
    import com.google.cloud.compute.v1.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html);
    import com.google.cloud.compute.v1.[SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest.html);
    import com.google.cloud.compute.v1.[UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    
      // Set Compute Engine usage export bucket for the Cloud project.
      // This sample presents how to interpret the default value for the report name prefix parameter.
      public static void setUsageExportBucket(String project, String bucketName,
          String reportNamePrefix)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
    
        // bucketName: Cloud Storage Bucket used to store Compute Engine usage reports.
        // An existing Google Cloud Storage bucket is required.
        // reportNamePrefix: Prefix of the name of the usage report that would
        // store Google Compute Engine data.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html).create()) {
    
          // Initialize UsageExportLocation object with provided bucket name and report name prefix.
          [UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html) usageExportLocation = [UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html).newBuilder()
              .setBucketName(bucketName)
              .[setReportNamePrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.Builder.html#com_google_cloud_compute_v1_UsageExportLocation_Builder_setReportNamePrefix_java_lang_String_)(reportNamePrefix).build();
    
          if (reportNamePrefix.length() == 0) {
            // Sending an empty value for reportNamePrefix results in the
            // next usage report being generated with the default prefix value "usage_gce".
            // (see,
            // https://cloud.google.com/compute/docs/reference/rest/v1/projects/setUsageExportBucket)
            System.out.println("Setting reportNamePrefix to empty value causes the "
                + "report to have the default value of `usage_gce`.");
          }
    
          // Set the usage export location.
          OperationFuture<Operation, Operation> operation = projectsClient
              .[setUsageExportBucketAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html#com_google_cloud_compute_v1_ProjectsClient_setUsageExportBucketAsync_com_google_cloud_compute_v1_SetUsageExportBucketProjectRequest_)([SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest.html).newBuilder()
                  .setProject(project)
                  .[setUsageExportLocationResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest.Builder.html#com_google_cloud_compute_v1_SetUsageExportBucketProjectRequest_Builder_setUsageExportLocationResource_com_google_cloud_compute_v1_UsageExportLocation_)(usageExportLocation)
                  .build());
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Setting usage export bucket failed ! ! " + response);
            return;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }

Verify that the server used the default prefix value `usage_gce`:
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project.html);
    import com.google.cloud.compute.v1.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html);
    import com.google.cloud.compute.v1.[SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest.html);
    import com.google.cloud.compute.v1.[UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    
      // Retrieve Compute Engine usage export bucket for the Cloud project.
      // Replaces the empty value returned by the API with the default value used
      // to generate report file names.
      public static [UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html) getUsageExportBucket(String project) throws IOException {
    
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.html).create()) {
          // Get the usage export location for the project from the server.
          [Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project.html) projectResponse = projectsClient.get(project);
    
          // Replace the empty value returned by the API with the default value
          // used to generate report file names.
          if (projectResponse.[hasUsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project.html#com_google_cloud_compute_v1_Project_hasUsageExportLocation__)()) {
            [UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html) usageExportLocation = projectResponse.[getUsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project.html#com_google_cloud_compute_v1_Project_getUsageExportLocation__)();
    
            // Verify that the server explicitly sent the optional field.
            if (usageExportLocation.[hasReportNamePrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html#com_google_cloud_compute_v1_UsageExportLocation_hasReportNamePrefix__)()) {
              String reportNamePrefix = usageExportLocation.[getReportNamePrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation.html#com_google_cloud_compute_v1_UsageExportLocation_getReportNamePrefix__)();
    
              if (reportNamePrefix.length() == 0) {
                // Although the server explicitly sent the empty string value,
                // the next usage report generated with these settings still has the default
                // prefix value "usage_gce".
                // (see, https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
                reportNamePrefix = "usage_gce";
                System.out.println(
                    "Report name prefix not set, replacing with default value of `usage_gce`.");
              }
            }
            return usageExportLocation;
          } else {
            // The usage reports are disabled.
            return null;
          }
        }
      }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const bucketName = 'YOUR_BUCKET_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const computeProtos = compute.protos.google.cloud.compute.v1;
    
    async function setUsageExportBucket() {
      const usageExportLocationResource = new computeProtos.UsageExportLocation();
      usageExportLocationResource.bucketName = bucketName;
      usageExportLocationResource.reportNamePrefix = reportNamePrefix;
    
      if (!reportNamePrefix) {
        // Sending an empty value for reportNamePrefix results in the next usage report being generated with the default prefix value "usage_gce".
        // (see: https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
        console.log(
          'Setting reportNamePrefix to empty value causes the report to have the default prefix value `usage_gce`.'
        );
      }
    
      // Set the usage export location.
      const projectsClient = new compute.[ProjectsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      let [operation] = await projectsClient.setUsageExportBucket({
        project: projectId,
        usageExportLocationResource,
      });
    
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    }
    
    setUsageExportBucket();

Verify that the server used the default prefix value `usage_gce`:
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function getUsageExportBucket() {
      // Get the usage export location for the project from the server.
      const projectsClient = new compute.[ProjectsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const [project] = await projectsClient.get({
        project: projectId,
      });
    
      const usageExportLocation = project.usageExportLocation;
    
      if (!usageExportLocation || !usageExportLocation.bucketName) {
        // The usage reports are disabled.
        return;
      }
    
      if (!usageExportLocation.reportNamePrefix) {
        // Although the server explicitly sent the empty string value,
        // the next usage report generated with these settings still has the default prefix value `usage_gce`.
        // (see https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
        console.log(
          'Report name prefix not set, replacing with default value of `usage_gce`.'
        );
        usageExportLocation.reportNamePrefix = 'usage_gce';
      }
    
      console.log(
        'Returned reportNamePrefix:',
        usageExportLocation.reportNamePrefix
      );
    }
    
    getUsageExportBucket();

### PHP
    
    
    use Google\Cloud\Compute\V1\Client\ProjectsClient;
    use Google\Cloud\Compute\V1\Operation;
    use Google\Cloud\Compute\V1\SetUsageExportBucketProjectRequest;
    use Google\Cloud\Compute\V1\UsageExportLocation;
    
    /**
     * Set Compute Engine usage export bucket for the Cloud project.
     * This sample presents how to interpret the default value for the report name prefix parameter.
     *
     * @param string $projectId Your Google Cloud project ID.
     * @param string $bucketName Google Cloud Storage bucket used to store Compute Engine usage reports.
     * An existing Google Cloud Storage bucket is required.
     * @param string $reportNamePrefix Prefix of the usage report name which defaults to an empty string
     * to showcase default values behavior.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function set_usage_export_bucket(
        string $projectId,
        string $bucketName,
        string $reportNamePrefix = ''
    ) {
        // Initialize UsageExportLocation object with provided bucket name and no report name prefix.
        $usageExportLocation = new UsageExportLocation(array(
            'bucket_name' => $bucketName,
            'report_name_prefix' => $reportNamePrefix
        ));
    
        if (strlen($reportNamePrefix) == 0) {
            // Sending empty value for report_name_prefix results in the next usage report
            // being generated with the default prefix value "usage_gce".
            // See https://cloud.google.com/compute/docs/reference/rest/v1/projects/setUsageExportBucket
            print('Setting report_name_prefix to empty value causes the ' .
                'report to have the default value of `usage_gce`.' . PHP_EOL);
        }
    
        // Set the usage export location.
        $projectsClient = new ProjectsClient();
        $request = (new SetUsageExportBucketProjectRequest())
            ->setProject($projectId)
            ->setUsageExportLocationResource($usageExportLocation);
        $operation = $projectsClient->setUsageExportBucket($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf(
                'Compute Engine usage export bucket for project `%s` set to bucket_name = `%s` with ' .
                'report_name_prefix = `%s`.' . PHP_EOL,
                $projectId,
                $usageExportLocation->getBucketName(),
                (strlen($reportNamePrefix) == 0) ? 'usage_gce' : $usageExportLocation->getReportNamePrefix()
            );
        } else {
            $error = $operation->getError();
            printf('Setting usage export bucket failed: %s' . PHP_EOL, $error?->getMessage());
        }
    }

Verify that the server used the default prefix value `usage_gce`:
    
    
    use Google\Cloud\Compute\V1\Client\ProjectsClient;
    use Google\Cloud\Compute\V1\GetProjectRequest;
    
    /**
     * Retrieve Compute Engine usage export bucket for the Cloud project.
     * Replaces the empty value returned by the API with the default value used
     * to generate report file names.
     *
     * @param string $projectId Your Google Cloud project ID.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function get_usage_export_bucket(string $projectId)
    {
        // Get the usage export location for the project from the server.
        $projectsClient = new ProjectsClient();
        $request = (new GetProjectRequest())
            ->setProject($projectId);
        $projectResponse = $projectsClient->get($request);
    
        // Replace the empty value returned by the API with the default value used to generate report file names.
        if ($projectResponse->hasUsageExportLocation()) {
            $responseUsageExportLocation = $projectResponse->getUsageExportLocation();
    
            // Verify that the server explicitly sent the optional field.
            if ($responseUsageExportLocation->hasReportNamePrefix()) {
                if ($responseUsageExportLocation->getReportNamePrefix() == '') {
                    // Although the server explicitly sent the empty string value, the next usage
                    // report generated with these settings still has the default prefix value "usage_gce".
                    // See https://cloud.google.com/compute/docs/reference/rest/v1/projects/get
                    print('Report name prefix not set, replacing with default value of `usage_gce`.' . PHP_EOL);
                    $responseUsageExportLocation->setReportNamePrefix('usage_gce');
                }
            }
    
            printf(
                'Compute Engine usage export bucket for project `%s` is bucket_name = `%s` with ' .
                'report_name_prefix = `%s`.' . PHP_EOL,
                $projectId,
                $responseUsageExportLocation->getBucketName(),
                $responseUsageExportLocation->getReportNamePrefix()
            );
        } else {
            // The usage reports are disabled.
            printf('Compute Engine usage export bucket for project `%s` is disabled.', $projectId);
        }
    }

### Python
    
    
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
    
    
    def set_usage_export_bucket(
        project_id: str, bucket_name: str, report_name_prefix: str = ""
    ) -> None:
        """
        Set Compute Engine usage export bucket for the Cloud project.
        This sample presents how to interpret the default value for the
        report name prefix parameter.
    
        Args:
            project_id: project ID or project number of the project to update.
            bucket_name: Google Cloud Storage bucket used to store Compute Engine
                usage reports. An existing Google Cloud Storage bucket is required.
            report_name_prefix: Prefix of the usage report name which defaults to an empty string
                to showcase default values behaviour.
        """
        usage_export_location = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[UsageExportLocation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UsageExportLocation.html)()
        usage_export_location.bucket_name = bucket_name
        usage_export_location.report_name_prefix = report_name_prefix
    
        if not report_name_prefix:
            # Sending an empty value for report_name_prefix results in the
            # next usage report being generated with the default prefix value
            # "usage_gce". (ref: https://cloud.google.com/compute/docs/reference/rest/v1/projects/setUsageExportBucket)
            print(
                "Setting report_name_prefix to empty value causes the report "
                "to have the default prefix of `usage_gce`."
            )
    
        projects_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.projects.ProjectsClient.html)()
        operation = projects_client.[set_usage_export_bucket](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.projects.ProjectsClient.html#google_cloud_compute_v1_services_projects_ProjectsClient_set_usage_export_bucket)(
            project=project_id, usage_export_location_resource=usage_export_location
        )
    
        wait_for_extended_operation(operation, "setting GCE usage bucket")
    
    

Verify that the server used the default prefix value `usage_gce`:
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    def get_usage_export_bucket(project_id: str) -> compute_v1.UsageExportLocation:
        """
        Retrieve Compute Engine usage export bucket for the Cloud project.
        Replaces the empty value returned by the API with the default value used
        to generate report file names.
    
        Args:
            project_id: project ID or project number of the project to update.
        Returns:
            UsageExportLocation object describing the current usage export settings
            for project project_id.
        """
        projects_client = compute_v1.ProjectsClient()
        project_data = projects_client.get(project=project_id)
    
        uel = project_data.usage_export_location
    
        if not uel.bucket_name:
            # The usage reports are disabled.
            return uel
    
        if not uel.report_name_prefix:
            # Although the server sent the empty string value, the next usage report
            # generated with these settings still has the default prefix value
            # "usage_gce". (see https://cloud.google.com/compute/docs/reference/rest/v1/projects/get)
            print(
                "Report name prefix not set, replacing with default value of "
                "`usage_gce`."
            )
            uel.report_name_prefix = "usage_gce"
        return uel
    
    

### Ruby
    
    
    require "google/cloud/compute/v1"
    
    
    # Sets Compute Engine usage export bucket for the Cloud project.
    # This sample presents how to interpret the default value for the
    # report name prefix parameter.
    #
    # @param [String] project project ID or project number of the project to update.
    # @param [String] bucket_name Google Cloud Storage bucket used to store Compute Engine
    #            usage reports. An existing Google Cloud Storage bucket is required.
    # @param [String] report_name_prefix Prefix of the usage report name which defaults to an empty string
    #            to showcase default values behaviour.
    def set_usage_export_bucket project:, bucket_name:, report_name_prefix: ""
      export_location = { bucket_name: bucket_name, report_name_prefix: report_name_prefix }
      if report_name_prefix.empty?
        # Sending an empty value for report_name_prefix results in the
        # next usage report being generated with the default prefix value
        # "usage_gce". (ref: https://cloud.google.com/compute/docs/reference/rest/v1/projects/setUsageExportBucket)
        puts "Setting report_name_prefix to empty value causes the report " \
             "to have the default prefix of `usage_gce`."
      end
      projects_client = ::Google::Cloud::Compute::V1::Projects::Rest::Client.new
      operation = projects_client.set_usage_export_bucket project: project,
                                                          usage_export_location_resource: export_location
      wait_until_done operation: operation
    end

Verify that the server used the default prefix value `usage_gce`:
    
    
    require "google/cloud/compute/v1"
    
    # Retrieves Compute Engine usage export bucket for the Cloud project.
    # Replaces the empty value returned by the API with the default value used
    # to generate report file names.
    #
    # @param [String] project project ID or project number of the project to get from.
    # @return [::Google::Cloud::Compute::V1::UsageExportLocation] object describing the current usage
    #   export settings for project.
    def get_usage_export_bucket project:
      projects_client = ::Google::Cloud::Compute::V1::Projects::Rest::Client.new
      project_data = projects_client.get project: project
      export_location = project_data.usage_export_location
    
      if !export_location.nil? && export_location.report_name_prefix.empty?
        puts "Report name prefix not set, replacing with default value of `usage_gce`."
        export_location.report_name_prefix = "usage_gce"
      end
      export_location
    end

### Rust
    
    
    use google_cloud_compute_v1::client::Projects;
    use google_cloud_compute_v1::model::UsageExportLocation;
    use google_cloud_lro::Poller;
    
    pub async fn sample(client: &Projects, project_id: &str, bucket_name: &str) -> anyhow::Result<()> {
        let operation = client
            .set_usage_export_bucket()
            .set_project(project_id)
            .set_body(UsageExportLocation::new().set_bucket_name(bucket_name))
            .poller()
            .until_done()
            .await?;
        println!(
            "Setting the usage export bucket with the default prefix (`usage_gce`) completed successfully: {operation:?}"
        );
    
        let operation = client
            .set_usage_export_bucket()
            .set_project(project_id)
            .set_body(
                UsageExportLocation::new()
                    .set_bucket_name(bucket_name)
                    .set_report_name_prefix("report-prefix"),
            )
            .poller()
            .until_done()
            .await?
            .to_result()?;
        println!("Setting the usage export bucket completed successfully: {operation:?}");
    
        Ok(())
    }

Verify that the server used the default prefix value `usage_gce`:
    
    
    use google_cloud_compute_v1::client::Projects;
    
    pub async fn sample(client: &Projects, project_id: &str) -> anyhow::Result<()> {
        let response = client.get().set_project(project_id).send().await?;
        let Some(bucket) = response
            .usage_export_location
            .as_ref()
            .and_then(|l| l.bucket_name.as_ref())
        else {
            println!("usage reports are disabled for {project_id}");
            return Ok(());
        };
        let prefix = response
            .usage_export_location
            .as_ref()
            .and_then(|l| l.report_name_prefix.as_deref())
            .unwrap_or("usage_gce");
        println!("usage reports are enabled and go to bucket {bucket} with prefix {prefix}");
    
        Ok(())
    }

For more information on setting up usage exports, see [Viewing usage reports](https://docs.cloud.google.com/compute/docs/logging/usage-export#api).

## Handling pagination

Some requests to the Compute Engine API return long lists of results, which the server provides to you as smaller "pages" of results with each call. When interacting with the API directly, you make multiple API requests to get responses for successive pages.

When you use Cloud Client Libraries, those requests simply return an iterator. You can then use the iterator to obtain all the individual results corresponding to your initial request. This process happens as though the results were returned in one long list. The client library silently issues any necessary API requests for additional pages to ensure your iterator automatically traverses the full set of results.

### C#
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class ListImagesAsyncSample
    {
        public async Task ListImagesAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id")
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html) client = await [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html#Google_Cloud_Compute_V1_ImagesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Make the request to list all non-deprecated images in a project.
            [ListImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListImagesRequest.html) request = new [ListImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListImagesRequest.html)
            {
                Project = projectId,
                // Listing only non-deprecated images to reduce the size of the reply.
                Filter = "deprecated.state != DEPRECATED",
                // MaxResults indicates the maximum number of items that will be returned per page.
                MaxResults = 100
            };
    
            // Although the MaxResults parameter is specified in the request, the sequence returned
            // by the ListAsync() method hides the pagination mechanic. The library makes multiple
            // requests to the API for you, so you can simply iterate over all the images.
            await foreach (var image in client.[ListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html#Google_Cloud_Compute_V1_ImagesClient_ListAsync_Google_Cloud_Compute_V1_ListImagesRequest_Google_Api_Gax_Grpc_CallSettings_)(request))
            {
                // The result is an Image collection.
                Console.WriteLine($"Image: {image.Name}");
            }
        }
    }
    

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class ListImagesPerPageAsyncSample
    {
        public async Task ListImagesPerPageAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id")
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html) client = await [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html#Google_Cloud_Compute_V1_ImagesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Make the request to list all non-deprecated images in a project.
            [ListImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListImagesRequest.html) request = new [ListImagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListImagesRequest.html)
            {
                Project = projectId,
                // Listing only non-deprecated images to reduce the size of the reply.
                Filter = "deprecated.state != DEPRECATED",
                // MaxResults indicates the maximum number of items that will be returned per page.
                MaxResults = 10
            };
    
            // Call the AsRawResponses() method of the returned image sequence to access the page sequece instead
            // This allows you to have more granular control of iteration over paginated results from the API.
            // Each time you access the next page, the library retrieves that page from the API.
            int pageIndex = 0;
            await foreach (var page in client.[ListAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient.html#Google_Cloud_Compute_V1_ImagesClient_ListAsync_Google_Cloud_Compute_V1_ListImagesRequest_Google_Api_Gax_Grpc_CallSettings_)(request).AsRawResponses())
            {
                Console.WriteLine($"Page index: {pageIndex}");
                pageIndex++;
                foreach (var image in page)
                {
                    // The result is an Image collection.
                    Console.WriteLine($"Image: {image.Name}");
                }
            }
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/protobuf/proto"
    )
    
    // printImagesList prints a list of all non-deprecated image names available in given project.
    func printImagesList(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    	ctx := context.Background()
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// Listing only non-deprecated images to reduce the size of the reply.
    	req := &computepb.ListImagesRequest{
    		Project:    projectID,
    		MaxResults: proto.Uint32(3),
    		Filter:     proto.String("deprecated.state != DEPRECATED"),
    	}
    
    	// Although the `MaxResults` parameter is specified in the request, the iterator returned
    	// by the `list()` method hides the pagination mechanic. The library makes multiple
    	// requests to the API for you, so you can simply iterate over all the images.
    	it := imagesClient.List(ctx, req)
    	for {
    		image, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s\n", image.GetName())
    	}
    	return nil
    }
    

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/protobuf/proto"
    )
    
    // printImagesListByPage prints a list of all non-deprecated image names available in a given project,
    // divided into pages as returned by the Compute Engine API.
    func printImagesListByPage(w io.Writer, projectID string, pageSize uint32) error {
    	// projectID := "your_project_id"
    	// pageSize := 10
    	ctx := context.Background()
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// Listing only non-deprecated images to reduce the size of the reply.
    	req := &computepb.ListImagesRequest{
    		Project:    projectID,
    		MaxResults: proto.Uint32(pageSize),
    		Filter:     proto.String("deprecated.state != DEPRECATED"),
    	}
    
    	// Use the `iterator.NewPage` to have more granular control of iteration over
    	// paginated results from the API. Each time you want to access the
    	// next page, the library retrieves that page from the API.
    	it := imagesClient.List(ctx, req)
    	p := iterator.NewPager(it, int(pageSize), "" /* start from the beginning */)
    	for page := 0; ; page++ {
    		var items []*computepb.Image
    		pageToken, err := p.NextPage(&items)
    		if err != nil {
    			return fmt.Errorf("iterator paging failed: %w", err)
    		}
    		fmt.Fprintf(w, "Page %d: %v\n", page, items)
    		if pageToken == "" {
    			break
    		}
    	}
    
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).ListPage;
    import com.google.cloud.compute.v1.[ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html);
    import java.io.IOException;
      // Prints a list of all non-deprecated image names available in given project.
      public static void listImages(String project) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to
        // safely clean up any remaining background resources.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
    
          // Listing only non-deprecated images to reduce the size of the reply.
          [ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html) imagesRequest = [ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html).newBuilder()
              .setProject(project)
              .setMaxResults(100)
              .setFilter("deprecated.state != DEPRECATED")
              .build();
    
          // Although the `setMaxResults` parameter is specified in the request, the iterable returned
          // by the `list()` method hides the pagination mechanic. The library makes multiple
          // requests to the API for you, so you can simply iterate over all the images.
          int imageCount = 0;
          for ([Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) image : imagesClient.list(imagesRequest).iterateAll()) {
            imageCount++;
            System.out.println(image.getName());
          }
          System.out.printf("Image count in %s is: %s", project, imageCount);
        }
      }

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).ListPage;
    import com.google.cloud.compute.v1.[ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html);
    import java.io.IOException;
      //  Prints a list of all non-deprecated image names available in a given project,
      //  divided into pages as returned by the Compute Engine API.
      public static void listImagesByPage(String project, int pageSize) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to
        // safely clean up any remaining background resources.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
    
          // Listing only non-deprecated images to reduce the size of the reply.
          [ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html) imagesRequest = [ListImagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListImagesRequest.html).newBuilder()
              .setProject(project)
              .setMaxResults(pageSize)
              .setFilter("deprecated.state != DEPRECATED")
              .build();
    
          // Use the `iteratePages` attribute of returned iterable to have more granular control of
          // iteration over paginated results from the API. Each time you want to access the
          // next page, the library retrieves that page from the API.
          int pageNumber = 1;
          for (ListPage page : imagesClient.list(imagesRequest).iteratePages()) {
            System.out.println("Page Number: " + pageNumber++);
            for ([Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) image : page.getValues()) {
              System.out.println(image.getName());
            }
          }
        }
      }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function listImages() {
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Listing only non-deprecated images to reduce the size of the reply.
      const images = imagesClient.listAsync({
        project: projectId,
        maxResults: 3,
        filter: 'deprecated.state != DEPRECATED',
      });
    
      // Although the `maxResults` parameter is specified in the request, the iterable returned
      // by the `listAsync()` method hides the pagination mechanic. The library makes multiple
      // requests to the API for you, so you can simply iterate over all the images.
      for await (const image of images) {
        console.log(` - ${image.name}`);
      }
    }
    
    listImages();

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const pageSize = 10;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function listImagesByPage() {
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Listing only non-deprecated images to reduce the size of the reply.
      const listRequest = {
        project: projectId,
        maxResults: pageSize,
        filter: 'deprecated.state != DEPRECATED',
      };
    
      const options = {
        autoPaginate: false,
      };
    
      let pageNum = 1;
    
      // Set autoPaginate option to `false` to have more granular control of
      // iteration over paginated results from the API. Each time you want to access the
      // next page, the library retrieves that page from the API.
      const listCallback = (err, resources, nextPageRequest, response) => {
        if (err) {
          console.error(err);
          return;
        }
    
        console.log(`Page ${pageNum}:`);
        pageNum += 1;
    
        for (let i = 0; i < resources.length; i++) {
          console.log(resources[i].name);
        }
    
        if (response.nextPageToken) {
          imagesClient.list(nextPageRequest, options, listCallback);
        }
      };
    
      imagesClient.list(listRequest, options, listCallback);
    }
    
    listImagesByPage();

### PHP
    
    
    use Google\Cloud\Compute\V1\Client\ImagesClient;
    use Google\Cloud\Compute\V1\ListImagesRequest;
    
    /**
     * Prints a list of all non-deprecated image names available in given project.
     *
     * @param string $projectId Project ID or project number of the Cloud project you want to list images from.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_all_images(string $projectId)
    {
        $imagesClient = new ImagesClient();
        // Listing only non-deprecated images to reduce the size of the reply.
        $optionalArgs = ['maxResults' => 100, 'filter' => 'deprecated.state != DEPRECATED'];
    
        /**
         * Although the maxResults parameter is specified in the request, the iterateAllElements() method
         * hides the pagination mechanic. The library makes multiple requests to the API for you,
         * so you can simply iterate over all the images.
         */
        $request = (new ListImagesRequest())
            ->setProject($projectId)
            ->setMaxResults($optionalArgs['maxResults'])
            ->setFilter($optionalArgs['filter']);
        $pagedResponse = $imagesClient->list($request);
        print('=================== Flat list of images ===================' . PHP_EOL);
        foreach ($pagedResponse->iterateAllElements() as $element) {
            printf(' - %s' . PHP_EOL, $element->getName());
        }
    }

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    use Google\Cloud\Compute\V1\Client\ImagesClient;
    use Google\Cloud\Compute\V1\ListImagesRequest;
    
    /**
     * Prints a list of all non-deprecated image names available in a given project,
     * divided into pages as returned by the Compute Engine API.
     *
     * @param string $projectId Project ID or project number of the Cloud project you want to list images from.
     * @param int $pageSize Size of the pages you want the API to return on each call.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     */
    function list_images_by_page(string $projectId, int $pageSize = 10)
    {
        $imagesClient = new ImagesClient();
        $pageNum = 1;
        // Listing only non-deprecated images to reduce the size of the reply.
        $optionalArgs = ['maxResults' => $pageSize, 'filter' => 'deprecated.state != DEPRECATED'];
    
        /**
         * Use the 'iteratePages()' method of returned response to have more granular control of iteration over
         * paginated results from the API. Each time you want to access the next page, the library retrieves
         * that page from the API.
         */
        $request = (new ListImagesRequest())
            ->setProject($projectId)
            ->setMaxResults($optionalArgs['maxResults'])
            ->setFilter($optionalArgs['filter']);
        $pagedResponse = $imagesClient->list($request);
        print('=================== Paginated list of images ===================' . PHP_EOL);
        foreach ($pagedResponse->iteratePages() as $page) {
            printf('Page %s:' . PHP_EOL, $pageNum);
            foreach ($page as $element) {
                printf(' - %s' . PHP_EOL, $element->getName());
            }
            $pageNum++;
        }
    }

### Python
    
    
    import google.cloud.compute_v1 as compute_v1
    
    def print_images_list(project: str) -> str:
        """
        Prints a list of all non-deprecated image names available in given project.
    
        Args:
            project: project ID or project number of the Cloud project you want to list images from.
    
        Returns:
            The output as a string.
        """
        images_client = compute_v1.ImagesClient()
        # Listing only non-deprecated images to reduce the size of the reply.
        images_list_request = compute_v1.ListImagesRequest(
            project=project, max_results=100, filter="deprecated.state != DEPRECATED"
        )
        output = []
    
        # Although the `max_results` parameter is specified in the request, the iterable returned
        # by the `list()` method hides the pagination mechanic. The library makes multiple
        # requests to the API for you, so you can simply iterate over all the images.
        for img in images_client.list(request=images_list_request):
            print(f" -  {img.name}")
            output.append(f" -  {img.name}")
        return "\n".join(output)
    
    

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    import google.cloud.compute_v1 as compute_v1
    
    def print_images_list_by_page(project: str, page_size: int = 10) -> str:
        """
        Prints a list of all non-deprecated image names available in a given project,
        divided into pages as returned by the Compute Engine API.
    
        Args:
            project: project ID or project number of the Cloud project you want to list images from.
            page_size: size of the pages you want the API to return on each call.
    
        Returns:
            Output as a string.
        """
        images_client = compute_v1.ImagesClient()
        # Listing only non-deprecated images to reduce the size of the reply.
        images_list_request = compute_v1.ListImagesRequest(
            project=project, max_results=page_size, filter="deprecated.state != DEPRECATED"
        )
        output = []
    
        # Use the `pages` attribute of returned iterable to have more granular control of
        # iteration over paginated results from the API. Each time you want to access the
        # next page, the library retrieves that page from the API.
        for page_num, page in enumerate(
            images_client.list(request=images_list_request).pages, start=1
        ):
            print(f"Page {page_num}: ")
            output.append(f"Page {page_num}: ")
            for img in page.items:
                print(f" - {img.name}")
                output.append(f" - {img.name}")
        return "\n".join(output)
    
    

### Ruby
    
    
    require "google/cloud/compute/v1"
    
    # Prints a list of all non-deprecated image names available in given project.
    #
    # @param [String] project project ID or project number of the Cloud project you want to list images from.
    def print_images_list project:
      client = ::Google::Cloud::Compute::V1::Images::Rest::Client.new
    
      # Make the request to list all non-deprecated images in a project.
      request = {
        project: project,
        # max_results indicates the maximum number of items that will be returned per page.
        max_results: 100,
        # Listing only non-deprecated images to reduce the size of the reply.
        filter: "deprecated.state != DEPRECATED"
      }
    
      # Although the `max_results` parameter is specified in the request, the iterable returned
      # by the `list` method hides the pagination mechanic. The library makes multiple
      # requests to the API for you, so you can simply iterate over all the images.
      client.list(request).each do |image|
        puts " - #{image.name}"
      end
    end

You can also use the `pages` attribute of the returned object to have more granular control of iteration over paginated results from the API.
    
    
    require "google/cloud/compute/v1"
    
    # Prints a list of all non-deprecated image names available in a given project,
    # divided into pages as returned by the Compute Engine API.
    #
    # @param [String] project ID or project number of the Cloud project you want to list images from.
    # @param [Number] size of the pages you want the API to return on each call.
    def print_images_list_by_page project:, page_size: 10
      client = ::Google::Cloud::Compute::V1::Images::Rest::Client.new
    
      # Make the request to list all non-deprecated images in a project.
      request = {
        project: project,
        # max_results indicates the maximum number of items that will be returned per page.
        max_results: page_size,
        # Listing only non-deprecated images to reduce the size of the reply.
        filter: "deprecated.state != DEPRECATED"
      }
    
      # Call the each_page method of the returned enumerable to have more granular control
      # of iteration over paginated results from the API. Each time you access the next
      # page, the library retrieves that page from the API.
      page_index = 0
      client.list(request).each_page do |page|
        puts "Page index: #{page_index}"
        page_index += 1
        page.each do |image|
          puts " - #{image.name}"
        end
      end
    end

### Rust
    
    
    pub use google_cloud_compute_v1::client::Images;
    pub use google_cloud_gax::paginator::ItemPaginator;
    
    pub async fn sample(client: &Images, project_id: &str) -> anyhow::Result<()> {
        let mut items = client
            .list()
            .set_project(project_id)
            // Maximum number of results per page. Higher values reduce the number
            // of RPCs, but increase memory usage.
            .set_max_results(100_u32)
            // Skip deprecated images.
            .set_filter("deprecated.state != DEPRECATED")
            .by_item();
        println!("iterating by item:");
        while let Some(image) = items.next().await.transpose()? {
            println!("item = {:?}", image);
        }
        Ok(())
    }

You can use the `by_page()` method to have more granular control of iteration over paginated results from the API.
    
    
    pub use google_cloud_compute_v1::client::Images;
    pub use google_cloud_gax::paginator::Paginator;
    
    pub async fn sample(client: &Images, project_id: &str) -> anyhow::Result<()> {
        let mut pages = client
            .list()
            .set_project(project_id)
            // Limit the number of images in each page.
            .set_max_results(10_u32)
            // Skip deprecated images.
            .set_filter("deprecated.state != DEPRECATED")
            .by_page();
        println!("iterating by page:");
        while let Some(page) = pages.next().await.transpose()? {
            println!("items = {:?}", page.items);
        }
        Ok(())
    }

Compute Engine in particular also offers `aggregatedList` methods like [`instances.aggregatedList`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/aggregatedList). Pagination for those methods function similarly, but instead iterate over key-list pairs. For an example, see Listing instances.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

When you're done experimenting, follow these cleanup instructions to avoid incurring charges for the virtual machine instance.

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



## What's next

  * Review the [API reference](https://docs.cloud.google.com/compute/docs/reference/latest) to learn how to perform other tasks with the API.



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
