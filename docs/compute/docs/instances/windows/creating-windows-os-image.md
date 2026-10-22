---
url: https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image/
title: Create custom Windows Server images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:12.644096+00:00
---

# Create custom Windows Server images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create custom Windows Server images Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

You can create customized Windows Server images from existing Compute Engine Windows Server images. Use these custom images to create instances with boot disks that are the same as your existing instances.

These custom images are useful for saving the operating system configuration of your existing instances and reusing the same configuration to create other instances.

The following tasks are not covered in this section:

  * Create an instance from a public image or a custom image; instead see [Creating a new Windows instance](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances).
  * Schedule a backup of your disks; instead see [About snapshot schedules for disks](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).
  * Import Windows Server or SQL Server systems; instead use the [VM migration service](https://docs.cloud.google.com/compute/docs/tutorials/migrating-vms-compute-engine).



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




To get the permissions that you need to create a custom Windows Server image, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a custom Windows Server image. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a custom Windows Server image:

  * `compute.images.create`
  * To create a custom image from a disk: `compute.disks.useReadOnly` on the disk 
  * To create a custom image from an existing image: `compute.images.useReadOnly` on on the source image 
  * To create a custom image from a standard or archive snapshot: `compute.snapshots.useReadOnly` on the source snapshot 
  * To add a label to the new image: `compute.images.setLabels` on the label 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare to create a Windows Server image

Before you create the image, run `GCESysprep` on the instance to prepare it for the image creation process.

`GCESysprep` prepares an instance for becoming a Compute Engine image by completing the following steps:

  1. Disables the `GCEStartup` scheduled task.
  2. Deletes all files from temp folder location.
  3. Clears all Windows event logs.
  4. Runs sysprep.exe /generalize /oobe /quit /unattend
  5. Configures `instance_setup.ps1` to run on the first boot of the VM instance.
  6. Deletes the RDP Certificate.
  7. Removes the stored list of persistent disks.
  8. Enables RDP and WinRM firewall rules.
  9. Disables the Google OS Config service.
  10. Shuts down the instance.



`GCESysprep` operations are logged to the Windows event log and serial port 1. Sysprep writes to multiple [log files](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep-process-overview#sysprep-log-files).

**Note:** Sysprep only [clears the built-in Administrator account's password](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/enable-and-disable-the-built-in-administrator-account?view=windows-11#configuring-the-built-in-administrator-password) for Windows server editions. We encourage users to review and update all local accounts prior to running `GCESysprep` as any enabled accounts and credentials will be present in the new image.

How to create a Compute Engine image using `GCESysprep`:

  1. Run `GCESysprep` with administrative rights.
         
         GCESysprep
         

  2. Create the image.




## Specify an image location

When creating a custom image, you can specify the image's [Cloud Storage](https://docs.cloud.google.com/storage/docs/locations) location, excluding dual-region locations. By specifying the image storage location, you can meet your regulatory and compliance requirements for data locality as well as your high availability needs by ensuring redundancy across regions.

The storage location feature is optional. If you don't select a location, Compute Engine will store your image in the multi-region closest to the image source. You can create custom images from source disks, images, snapshots, or images stored in Cloud Storage. You can use these images to create new VM instances.

All of your existing images prior to this feature launch remain where they are. The only change is that you can view the image location of all your images. If you have an existing image you want to move, you must recreate it in the selected location.

## Create a Windows image

You can create disk images from the following sources:

  * A persistent disk, even while that disk is attached to an instance
  * A snapshot of a persistent disk
  * Another image in your project
  * An image that is shared from another project
  * An [imported image](https://docs.cloud.google.com/compute/docs/images/import-existing-image) stored in Cloud Storage




###  Console 

  1. In the Google Cloud console, go to the **Create a new image** page. 

[Create a new image](https://console.cloud.google.com/compute/imagesAdd)

  2. Specify the image **Name**.
  3. Choose a **Source** disk with a Windows operating system from which you want to create an image.
  4. Specify the **Location** to store the image. Choose an image location from the **Based on source disk location (default)** drop-down menu. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine will store the image in the multi-region closest to your image's source location.
  5. Specify the properties for your image. For example, you can specify an image family name for your image to organize this image as part of an [image family](https://docs.cloud.google.com/compute/docs/images#image_families).
  6. Click **Create**.



###  Google Cloud CLI 

Use the `gcloud compute` with [`images create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create), and provide the source persistent disk from which you want to create an image. Optionally, include the `--force` flag to create the image even if it is attached to a running instance.
    
    
    gcloud compute images create example-image --source-disk DISK_NAME \
        --source-disk-zone ZONE \
        --storage-location LOCATION \
       [--force]
    

Replace the following:

  * `DISK_NAME`: the name of the source disk to create the image from.
  * `ZONE`: the zone of the disk.
  * `LOCATION`: an optional flag that lets you designate the region or multi-region where your image is going to be stored. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.
  * `--force`: an optional flag that creates the image even if the disk is attached to a running instance. This option might compromise the integrity of your image. Stop the instance before you create the image if possible.



When you run this command, `gcloud compute` creates a new image based on the persistent disk you provided and adds it to your collection. You can confirm that your image was successfully created by running:
    
    
    gcloud compute images list
    

###  Go 

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createWindowsOSImage creates a new Windows image from the specified source disk.
    func createWindowsOSImage(
    	w io.Writer,
    	projectID, zone, sourceDiskName, imageName, storageLocation string,
    	forceCreate bool,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// sourceDiskName := "your_source_disk_name"
    	// imageName := "your_image_name"
    	// storageLocation := "eu"
    	// forceCreate := false
    
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
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	// Getting instances where source disk is attached
    	diskRequest := &computepb.GetDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		Disk:    sourceDiskName,
    	}
    
    	sourceDisk, err := disksClient.Get(ctx, diskRequest)
    	if err != nil {
    		return fmt.Errorf("unable to get disk: %w", err)
    	}
    
    	// Сhecking whether the instances is stopped
    	for _, fullInstanceName := range sourceDisk.GetUsers() {
    		parsedName := strings.Split(fullInstanceName, "/")
    		l := len(parsedName)
    		if l < 5 {
    			return fmt.Errorf(
    				"API returned instance name with unexpected format",
    			)
    		}
    		instanceReq := &computepb.GetInstanceRequest{
    			Project:  parsedName[l-5],
    			Zone:     parsedName[l-3],
    			Instance: parsedName[l-1],
    		}
    		instance, err := instancesClient.Get(ctx, instanceReq)
    		if err != nil {
    			return fmt.Errorf("unable to get instance: %w", err)
    		}
    
    		if instance.GetStatus() != "TERMINATED" && instance.GetStatus() != "STOPPED" {
    			if !forceCreate {
    				return fmt.Errorf("instance %s should be stopped. "+
    					"Please stop the instance using "+
    					"GCESysprep command or set forceCreate parameter to true "+
    					"(not recommended). More information here: "+
    					"https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image#api",
    					parsedName[l-1],
    				)
    			}
    		}
    	}
    
    	if forceCreate {
    		fmt.Fprintf(w, "Warning: ForceCreate option compromise the integrity of your image. "+
    			"Stop the instance before you create the image if possible.",
    		)
    	}
    
    	req := &computepb.InsertImageRequest{
    		Project:     projectID,
    		ForceCreate: &forceCreate,
    		ImageResource: &computepb.Image{
    			Name:             proto.String(imageName),
    			SourceDisk:       proto.String(fmt.Sprintf("zones/%s/disks/%s", zone, sourceDiskName)),
    			StorageLocations: []string{storageLocation},
    		},
    	}
    
    	op, err := imagesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create image: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Image created\n")
    
    	return nil
    }
    

###  Java 

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

###  Node.js 

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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

Make a `POST` request to the [`images().insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert) method, with a `sourceDisk` URL in the request body.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images?FORCE_OPTION
    
    {
      "name": "IMAGE_NAME",
      "sourceDisk": "zones/ZONE/disks/DISK_NAME",
      "storageLocations": "LOCATION",
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `FORCE_OPTION`: an optional flag to create the image even if the source disk is attached to a running instance. Specify `forceCreate=true` at the end of your POST line to set this option. This option might compromise the integrity of your image. Stop the instance before you create the image if possible.
  * `IMAGE_NAME`: the name to give this image.
  * `ZONE`: the zone of the source disk to create an image from.
  * `DISK_NAME`: the name of the source disk.
  * `LOCATION`: an optional parameter that lets you select the multi-region or a region storage location of your image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.



For more information about adding images, see the [images reference](https://docs.cloud.google.com/compute/docs/reference/latest/images/insert).

## Update Windows agents and scripts

Compute Engine occasionally releases new Windows images with the latest agents and scripts. These items assist Windows instances with startup and shutdown processes, account management, and address management.

Since Windows image version `v20160112`, the Windows agent updates itself with upstream releases. You can disable these agent updates by setting the `disable-agent-updates` instance metadata key to `true`. If you have instances that are based on older image releases, you can [manually update the Windows agent](https://github.com/GoogleCloudPlatform/compute-image-windows/blob/master/README.md) of those instances.

## What's next

  * [Automating Windows password generation](https://docs.cloud.google.com/compute/docs/instances/windows/automate-pw-generation)
  * [Using existing Microsoft application licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
