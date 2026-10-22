---
url: https://docs.cloud.google.com/compute/docs/samples/compute-windows-image-create/
title: Create a Windows Server image \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:27.537053+00:00
---

# Create a Windows Server image  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-windows-image-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a Windows Server image Stay organized with collections  Save and categorize content based on your preferences. 

Create a Windows Server image from the specified source disk.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create custom Windows Server images](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image)



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
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const sourceDiskName = 'YOUR_SOURCE_DISK_NAME';
    // const imageName = 'YOUR_IMAGE_NAME';
    // const storageLocation = 'eu';
    // const forceCreate = false;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    function parseInstanceName(name) {
      const parsedName = name.split('/');
      const l = parsedName.length;
    
      if (parsedName.legth < 5) {
        throw new Error(
          'Provide correct instance name in the following format: https://www.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances/INSTANCE_NAME'
        );
      }
    
      return [parsedName[l - 1], parsedName[l - 3], parsedName[l - 5]];
    }
    
    async function createWindowsOSImage() {
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Getting instances where source disk is attached
      const [sourceDisk] = await disksClient.get({
        project: projectId,
        zone,
        disk: sourceDiskName,
      });
    
      // Сhecking whether the instances is stopped
      for (const fullInstanceName of sourceDisk.users) {
        const [instanceName, instanceZone, instanceProjectId] =
          parseInstanceName(fullInstanceName);
        const [instance] = await instancesClient.get({
          project: instanceProjectId,
          zone: instanceZone,
          instance: instanceName,
        });
    
        if (
          !['TERMINATED', 'STOPPED'].includes(instance.status) &&
          !forceCreate
        ) {
          throw new Error(
            `Instance ${instanceName} should be stopped. Please stop the instance using GCESysprep command or set forceCreate parameter to true (not recommended). More information here: https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image#api.`
          );
        }
      }
    
      if (forceCreate) {
        console.warn(
          'Warning: forceCreate option compromise the integrity of your image. Stop the instance before you create the image if possible.'
        );
      }
    
      const [response] = await imagesClient.insert({
        project: projectId,
        forceCreate,
        imageResource: {
          name: imageName,
          sourceDisk: `/zones/${zone}/disks/${sourceDiskName}`,
          storageLocations: storageLocation ? [storageLocation] : [],
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new ccompute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html));
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Image created.');
    }
    
    createWindowsOSImage();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
