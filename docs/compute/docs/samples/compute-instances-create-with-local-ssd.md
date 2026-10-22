---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-create-with-local-ssd/
title: Create a VM with a local SSD \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:06.205118+00:00
---

# Create a VM with a local SSD  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-create-with-local-ssd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a VM with a local SSD Stay organized with collections  Save and categorize content based on your preferences. 

Attach a local SSD to a VM during VM creation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Add a Local SSD disk to your compute instance](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd)



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
    	"google.golang.org/protobuf/proto"
    )
    
    // createWithLocalSSD creates a new VM instance with Debian 10 operating system and a local SSD attached.
    func createWithLocalSSD(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
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
    
    	// List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details.
    	newestDebianReq := &computepb.GetFromFamilyImageRequest{
    		Project: "debian-cloud",
    		Family:  "debian-12",
    	}
    	newestDebian, err := imagesClient.GetFromFamily(ctx, newestDebianReq)
    	if err != nil {
    		return fmt.Errorf("unable to get image from family: %w", err)
    	}
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
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
    					Type:       proto.String(computepb.[AttachedDisk_PERSISTENT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskType: proto.String(fmt.Sprintf("zones/%s/diskTypes/local-ssd", zone)),
    					},
    					AutoDelete: proto.Bool(true),
    					Type:       proto.String(computepb.[AttachedDisk_SCRATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AttachedDisk_UNDEFINED_TYPE_AttachedDisk_PERSISTENT_AttachedDisk_SCRATCH).String()),
    				},
    			},
    			MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					Name: proto.String("global/networks/default"),
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

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWithLocalSsd {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you want to use.
        String projectId = "your-project-id";
        // zone: name of the zone to create the instance in. For example: "us-west3-b"
        String zone = "zone-name";
        // instanceName: name of the new virtual machine (VM) instance.
        String instanceName = "instance-name";
    
        createWithLocalSsd(projectId, zone, instanceName);
      }
    
      // Create a new VM instance with Debian 13 operating system and SSD local disk.
      public static void createWithLocalSsd(String projectId, String zone, String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        int diskSizeGb = 10;
        boolean boot = true;
        boolean autoDelete = true;
        String diskType = String.format("zones/%s/diskTypes/pd-standard", zone);
        // Get the latest debian image.
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) newestDebian = getImageFromFamily("debian-cloud", "debian-13");
        List<AttachedDisk> disks = new ArrayList<>();
    
        // Create the disks to be included in the instance.
        disks.add(
            createDiskFromImage(diskType, diskSizeGb, boot, newestDebian.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html#com_google_cloud_compute_v1_Image_getSelfLink__)(), autoDelete));
        disks.add(createLocalSsdDisk(zone));
    
        // Create the instance.
        [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = createInstance(projectId, zone, instanceName, disks);
    
        if (instance != null) {
          System.out.printf("Instance created with local SSD: %s", instance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getName__)());
        }
    
      }
    
      // Retrieve the newest image that is part of a given family in a project.
      // Args:
      //    projectId: project ID or project number of the Cloud project you want to get image from.
      //    family: name of the image family you want to get image from.
      private static [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) getImageFromFamily(String projectId, String family) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `imagesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
          // List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
          return imagesClient.[getFromFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html#com_google_cloud_compute_v1_ImagesClient_getFromFamily_com_google_cloud_compute_v1_GetFromFamilyImageRequest_)(projectId, family);
        }
      }
    
      // Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
      // source for the new disk.
      //
      // Args:
      //    diskType: the type of disk you want to create. This value uses the following format:
      //        "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
      //        For example: "zones/us-west3-b/diskTypes/pd-ssd"
      //
      //    diskSizeGb: size of the new disk in gigabytes.
      //
      //    boot: boolean flag indicating whether this disk should be used as a
      //    boot disk of an instance.
      //
      //    sourceImage: source image to use when creating this disk.
      //    You must have read access to this disk. This can be one of the publicly available images
      //    or an image from one of your projects.
      //    This value uses the following format: "projects/{project_name}/global/images/{image_name}"
      //
      //    autoDelete: boolean flag indicating whether this disk should be deleted
      //    with the VM that uses it.
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) createDiskFromImage(String diskType, int diskSizeGb, boolean boot,
          String sourceImage, boolean autoDelete) {
    
        [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html) attachedDiskInitializeParams =
            [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                .setSourceImage(sourceImage)
                .setDiskSizeGb(diskSizeGb)
                .setDiskType(diskType)
                .build();
    
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) bootDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
            .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(attachedDiskInitializeParams)
            // Remember to set auto_delete to True if you want the disk to be deleted when you delete
            // your VM instance.
            .setAutoDelete(autoDelete)
            .setBoot(boot)
            .build();
    
        return bootDisk;
      }
    
      // Create an AttachedDisk object to be used in VM instance creation. The created disk contains
      // no data and requires formatting before it can be used.
      // Args:
      //    zone: The zone in which the local SSD drive will be attached.
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) createLocalSsdDisk(String zone) {
    
        [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html) attachedDiskInitializeParams =
            [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                .setDiskType(String.format("zones/%s/diskTypes/local-ssd", zone))
                .build();
    
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
            .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.SCRATCH.name())
            .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(attachedDiskInitializeParams)
            .setAutoDelete(true)
            .build();
    
        return disk;
      }
    
      // Send an instance creation request to the Compute Engine API and wait for it to complete.
      // Args:
      //    projectId: project ID or project number of the Cloud project you want to use.
      //    zone: name of the zone to create the instance in. For example: "us-west3-b"
      //    instanceName: name of the new virtual machine (VM) instance.
      //    disks: a list of compute.v1.AttachedDisk objects describing the disks
      //           you want to attach to your new instance.
      private static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createInstance(String projectId, String zone, String instanceName,
          List<AttachedDisk> disks)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          // machineType: machine type of the VM being created. This value uses the
          // following format: "zones/{zone}/machineTypes/{type_name}".
          // For example: "zones/europe-west3-c/machineTypes/f1-micro"
          String typeName = "n1-standard-1";
          String machineType = String.format("zones/%s/machineTypes/%s", zone, typeName);
    
          // networkLink: name of the network you want the new instance to use.
          // For example: "global/networks/default" represents the network
          // named "default", which is created automatically for each project.
          String networkLink = "global/networks/default";
    
          // Collect information into the Instance object.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
              .setName(instanceName)
              .setMachineType(machineType)
              .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder().setName(networkLink).build())
              .addAllDisks(disks)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.insertAsync(projectId, zone, instance)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Instance creation failed ! ! " + response);
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
          return instancesClient.get(projectId, zone, instanceName);
        }
    
      }
    
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO(developer): Uncomment and replace these variables before running the sample.
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new VM instance with Debian 10 operating system and SSD local disk.
    async function createInstanceWithLocalSSD() {
      const diskSizeGb = 10;
      const boot = true;
      const autoDelete = true;
      const diskType = `zones/${zone}/diskTypes/pd-standard}`;
      const disks = [];
    
      // Get the latest debian image.
      // Retrieve the newest image that is part of a given family in a project.
      // Args:
      //    project: project ID or project number of the Cloud project you want to get image from.
      //    family: name of the image family you want to get image from.
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const [newestDebian] = await imagesClient.getFromFamily({
        project: 'debian-cloud',
        family: 'debian-11',
      });
    
      // Create the disks to be included in the instance.
      disks.push(
        createDiskFromImage(
          diskType,
          diskSizeGb,
          boot,
          newestDebian.selfLink,
          autoDelete
        )
      );
      disks.push(createLocalSsdDisk(zone));
    
      // Create the instance.
      const [instance] = await createInstance(
        projectId,
        zone,
        instanceName,
        disks
      );
    
      if (instance !== null) {
        console.log(`Instance created with local SSD: ${instance.name}`);
      }
    }
    
    // Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
    // source for the new disk.
    //
    // Args:
    //    diskType: the type of disk you want to create. This value uses the following format:
    //        "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
    //        For example: "zones/us-west3-b/diskTypes/pd-ssd"
    //
    //    diskSizeGb: size of the new disk in gigabytes.
    //
    //    boot: boolean flag indicating whether this disk should be used as a
    //    boot disk of an instance.
    //
    //    sourceImage: source image to use when creating this disk.
    //    You must have read access to this disk. This can be one of the publicly available images
    //    or an image from one of your projects.
    //    This value uses the following format: "projects/{project_name}/global/images/{image_name}"
    //
    //    autoDelete: boolean flag indicating whether this disk should be deleted
    //    with the VM that uses it.
    function createDiskFromImage(
      diskType,
      diskSizeGb,
      boot,
      sourceImage,
      autoDelete
    ) {
      return {
        initializeParams: {
          sourceImage: sourceImage,
          diskSizeGb: diskSizeGb,
        },
        // Remember to set autoDelete to True if you want the disk to be deleted when you delete
        // your VM instance.
        autoDelete: autoDelete,
        boot: boot,
        diskType: diskType,
      };
    }
    
    // Create an AttachedDisk object to be used in VM instance creation. The created disk contains
    // no data and requires formatting before it can be used.
    // Args:
    //    zone: The zone in which the local SSD drive will be attached.
    function createLocalSsdDisk(zone) {
      return {
        type: 'SCRATCH',
        autoDelete: true,
        initializeParams: {
          diskType: `zones/${zone}/diskTypes/local-ssd`,
        },
      };
    }
    
    // Send an instance creation request to the Compute Engine API and wait for it to complete.
    // Args:
    //    projectId: project ID or project number of the Cloud project you want to use.
    //    zone: name of the zone to create the instance in. For example: "us-west3-b"
    //    instanceName: name of the new virtual machine (VM) instance.
    //    disks: a list of compute.v1.AttachedDisk objects describing the disks
    //           you want to attach to your new instance.
    async function createInstance(projectId, zone, instanceName, disks) {
      // Instantiates a reusable client object.
      // (Node.js will automatically clean it up.)
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // machineType: machine type of the VM being created. This value uses the
      // following format: "zones/{zone}/machineTypes/{type_name}".
      // For example: "zones/europe-west3-c/machineTypes/f1-micro"
      const typeName = 'n1-standard-1';
      const machineType = `zones/${zone}/machineTypes/${typeName}`;
      // networkLink: name of the network you want the new instance to use.
      // For example: "global/networks/default" represents the network
      // named "default", which is created automatically for each project.
      const networkLink = 'global/networks/default';
    
      // Collect information into the Instance object.
      const [response] = await instancesClient.insert({
        project: projectId,
        zone: zone,
        instanceResource: {
          name: instanceName,
          machineType: machineType,
          networkInterfaces: [
            {
              name: networkLink,
            },
          ],
          disks: disks,
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
    
      return instancesClient.get({
        project: projectId,
        zone: zone,
        instance: instanceName,
      });
    }
    
    createInstanceWithLocalSSD();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    
    def local_ssd_disk(zone: str) -> compute_v1.AttachedDisk():
        """
        Create an AttachedDisk object to be used in VM instance creation. The created disk contains
        no data and requires formatting before it can be used.
    
        Args:
            zone: The zone in which the local SSD drive will be attached.
    
        Returns:
            AttachedDisk object configured as a local SSD disk.
        """
        disk = compute_v1.AttachedDisk()
        disk.type_ = compute_v1.AttachedDisk.Type.SCRATCH.name
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.disk_type = f"zones/{zone}/diskTypes/local-ssd"
        disk.initialize_params = initialize_params
        disk.auto_delete = True
        return disk
    
    
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
    
    
    def create_with_ssd(
        project_id: str, zone: str, instance_name: str
    ) -> compute_v1.Instance:
        """
        Create a new VM instance with Debian 10 operating system and SSD local disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
    
        Returns:
            Instance object.
        """
        newest_debian = get_image_from_family(project="debian-cloud", family="debian-12")
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [
            disk_from_image(disk_type, 10, True, newest_debian.self_link, True),
            local_ssd_disk(zone),
        ]
        instance = create_instance(project_id, zone, instance_name, disks)
        return instance
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Create a VM with a local SSD for temporary storage use cases
    
    resource "google_compute_instance" "default" {
      name         = "my-vm-instance-with-scratch"
      machine_type = "n2-standard-8"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      # Local SSD interface type; NVME for image with optimized NVMe drivers or SCSI
      # Local SSD are 375 GiB in size
      scratch_disk {
        interface = "SCSI"
      }
    
      network_interface {
        network = "default"
        access_config {}
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
