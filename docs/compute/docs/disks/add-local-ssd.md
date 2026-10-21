---
url: https://docs.cloud.google.com/compute/docs/disks/add-local-ssd/
title: Add a Local SSD disk to your compute instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:09.298722+00:00
---

# Add a Local SSD disk to your compute instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/add-local-ssd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add a Local SSD disk to your compute instance Stay organized with collections  Save and categorize content based on your preferences. 

Local SSD disks are designed for temporary storage use cases such as caches or scratch processing space. Because Local SSD disks are located on the physical machine where your Compute Engine instance is running, they can be created only during the instance creation process. Local SSD disks can't be used as boot devices.

For [third generation machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) and later that support Local SSD disks (excluding G4 and M3), Compute Engine automatically attaches a specific number of Local SSD disks when you create your instance. These machine series offer Local SSD storage in the following ways:

  * **H4D, C4, C4A, C4D, C4N, C3, and C3D** : For these machine series, Local SSD storage is available only with the machine types that end in `-lssd`, such as `c3-standard-88-lssd`.
  * **Z4D, Z4M, Z3, A4X Max, A4X, A4, A3, and A2 Ultra machine series** : For these machine series, every machine type comes with Local SSD storage.



For G4, M3, first generation, and second generation machine types that support Local SSD disks, you must specify the number of Local SSD disks to attach when you create the compute instance.

After creating a Local SSD disk, you must format and mount the device before you can use it.

For information about the amount of Local SSD storage available with various machine types, and the number of Local SSD disks you can attach to a compute instance, see [Choosing a valid number of Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds).

## Before you begin

  * Review the [Local SSD limitations](https://docs.cloud.google.com/compute/docs/disks/local-ssd#limitations) before using Local SSD disks.
  * Review the [data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence) scenarios for Local SSD disks.
  * If you are adding Local SSD disks to compute instances that have attached GPUs, see [ Local SSD disk availability](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#local-ssd-gpu). 
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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

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




## Create a compute instance with Local SSD disks

You can create a compute instance with Local SSD storage using the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/latest/instances).

###  Console 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the name, region, and zone for your compute instance. Optionally, add tags or labels.

  3. In the **Machine configuration** section, choose the machine family that contains your target machine type.

  4. Select a series from the **Series** list, then choose the machine type.

     * For H4D, C4, C4A, C4D, C4N, C3, and C3D, choose a machine type that ends in `-lssd`.
     * For Z4D, Z4M, Z3, A4X Max, A4X, A4, A3, and A2 Ultra, every machine type comes with Local SSD storage.
     * For G4, M3, or first and second generation machine series, after selecting the machine type, do the following: 
       1. Expand the **Advanced options** section.
       2. Expand **Disks** , click **Add Local SSD** , and do the following: 
          1. On the **Configure Local SSD** page, choose the disk interface type.
          2. Select the number of disks you want from the **Disk capacity** list.
          3. Click **Save**.
  5. Continue with the compute instance creation process.

  6. After creating the instance with Local SSD disks, you must format and mount each device before you can use the disks.




###  gcloud 

  * For the Z4D, Z4M, Z3, A4X Max, A4X, A4, A3, and A2 Ultra machine series, to create a compute instance with attached Local SSD disks, create an instance that uses any of the available machine types for that series by following the instructions to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  * For the H4D, C4, C4A, C4D, C4N, C3, and C3D machine series, to create a compute instance with attached Local SSD disks, follow the instructions to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), and specify a machine type that ends in `-lssd`.

For example, you can create a C3 instance with two Local SSD disks that use the NVMe disk interface as follows:
        
        gcloud compute instances create example-c3-instance \
           --zone ZONE \
           --machine-type c3-standard-8-lssd \
           --image-project IMAGE_PROJECT \
           --image-family IMAGE_FAMILY
        

  * For G4, M3, and first and second generation machine series, to create a compute instance with attached Local SSD disks, follow the instructions to [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), but use the `--local-ssd` flag to create and attach a Local SSD disk. To create multiple Local SSD disks, add more `--local-ssd` flags. Optionally, you can also set values for the interface and the device name for each `--local-ssd` flag.

For example, you can create a M3 instance with four Local SSD disks and specify the disk interface type as follows:
        
        gcloud compute instances create INSTANCE_NAME \
           --machine-type m3-ultramem-64 \
           --zone ZONE \
           --local-ssd interface=INTERFACE_TYPE,device-name=DEVICE-NAME \
           --local-ssd interface=INTERFACE_TYPE,device-name=DEVICE-NAME \
           --local-ssd interface=INTERFACE_TYPE,device-name=DEVICE-NAME \
           --local-ssd interface=INTERFACE_TYPE \
           --image-project IMAGE_PROJECT \
           --image-family IMAGE_FAMILY
        




Replace the following:

  * INSTANCE_NAME: the name for the new compute instance
  * ZONE: the zone to create the instance in. This flag is optional if you have configured the gcloud CLI `compute/zone` property or the environment variable `CLOUDSDK_COMPUTE_ZONE`.
  * INTERFACE_TYPE: the disk interface type that you want to use for the Local SSD disk. If you're creating a G4 or M3 instance, or if your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `nvme`. Specify `scsi` for other images.
  * DEVICE-NAME: Optional: A name that indicates the disk name to use in the guest operating system [symbolic link](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks) (symlink).
  * IMAGE_FAMILY: one of the [available image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that you want installed on the boot disk
  * IMAGE_PROJECT: the [image project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that the image family belongs to



You can attach Local SSD disks to a compute instance created using a first or second generation machine type using a combination of `nvme` and `scsi` for different partitions. Performance for the `nvme` device depends on the boot disk image for your instance. Third generation and later compute instances support only the NVMe disk interface.

After creating a compute instance with Local SSD disks, you must format and mount each device before you can use it.

###  Terraform 

To create a compute instance with attached Local SSD disks, you can use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).
    
    
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

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To generate the Terraform code, you can use the **Equivalent code** component in the Google Cloud console. 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.
  3. Specify the parameters you want.
  4. At the top or bottom of the page, click **Equivalent code** , and then click the **Terraform** tab to view the Terraform code.



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
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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
    
    

###  REST 

Use the [`instances.insert method`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create a compute instance from an image family or from a specific version of an operating system image.

  * For the Z4D, Z4M, Z3, A4X Max, A4X, A4, A3, and A2 Ultra machine series, to create a compute instance that has attached Local SSD disks, create an instance that uses any of the available machine types for that series.
  * For the H4D, C4, C4A, C4D, C4N, C3, and C3D machine series, to create a compute instance that has attached Local SSD disks, specify an instance type that ends in `-lssd`.

Here is a sample request payload that creates a C3 instance with an Ubuntu boot disk and two Local SSD disks:
        
        {
         "machineType":"zones/us-central1-c/machineTypes/c3-standard-8-lssd",
         "name":"c3-with-local-ssd",
         "disks":[
            {
               "type":"PERSISTENT",
               "initializeParams":{
                  "sourceImage":"projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts"
               },
               "boot":true
            }
         ],
         "networkInterfaces":[
            {
               "network":"global/networks/default"
        }
         ]
        }
        

  * For G4, M3, and first and second generation machine series, to create a compute instance with attached Local SSD disks, you can add Local SSD disks during instance creation by using the `initializeParams` property. You must also provide the following properties:

    * `diskType`: Set to Local SSD
    * `autoDelete`: Set to true
    * `type`: Set to `SCRATCH`

The following properties can't be used with Local SSD disks:

    * `diskName`
    * `sourceImage` property
    * `diskSizeGb`

Here is a sample request payload that creates a M3 instance with a boot disk and four Local SSD disks:
    
    {
     "machineType":"zones/us-central1-f/machineTypes/m3-ultramem-64",
     "name":"local-ssd-instance",
     "disks":[
        {
         "type":"PERSISTENT",
         "initializeParams":{
            "sourceImage":"projects/ubuntu-os-cloud/global/images/family/ubuntu-2204-lts"
         },
         "boot":true
        },
        {
           "type":"SCRATCH",
           "initializeParams":{
              "diskType":"zones/us-central1-f/diskTypes/local-ssd"
           },
           "autoDelete":true,
           "interface": "NVME"
        },
        {
           "type":"SCRATCH",
           "initializeParams":{
              "diskType":"zones/us-central1-f/diskTypes/local-ssd"
           },
           "autoDelete":true,
           "interface": "NVME"
        },
        {
           "type":"SCRATCH",
           "initializeParams":{
              "diskType":"zones/us-central1-f/diskTypes/local-ssd"
           },
           "autoDelete":true,
           "interface": "NVME"
        },
        {
           "type":"SCRATCH",
           "initializeParams":{
              "diskType":"zones/us-central1-f/diskTypes/local-ssd"
           },
           "autoDelete":true,
           "interface": "NVME"
        },
     ],
     "networkInterfaces":[
        {
           "network":"global/networks/default"
        }
     ]
    }
    




After creating a Local SSD disk, you must format and mount each device before you can use it.

For more information on creating an instance using REST, see the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/latest/instances).

## Formatting and mounting a Local SSD disk

You can format and mount each Local SSD disk individually, or you can combine multiple Local SSD disks into a single logical volume.

### Format and mount individual Local SSD disks

The easiest way to connect Local SSD disks to your compute instance is to format and mount each device with a single partition. Alternatively, you can combine multiple partitions into a single logical volume.

###  Linux instances 

Format and mount the new Local SSD disk on your Linux instance. You can use any partition format and configuration that you need. This example creates a single `ext4` partition.

  1. Go to the VM instances page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **SSH** button next to the compute instance that has the new attached Local SSD. The browser opens a terminal connection to the instance.

  3. In the terminal, use the `find` command to identify the Local SSD disk that you want to mount.
         
         $ find /dev/ | grep google-local-nvme-ssd
         

Local SSD disks in SCSI mode have standard names like `google-local-ssd-0`. Local SSD disks in NVMe mode have names like `google-local-nvme-ssd-0`, as shown in the following output:
         
         $ find /dev/ | grep google-local-nvme-ssd
         
          /dev/disk/by-id/google-local-nvme-ssd-0
         

  4. Format the Local SSD disk with an `ext4` file system. This command _deletes_ all existing data from the Local SSD disk.
         
         $ sudo mkfs.ext4 -F /dev/disk/by-id/[SSD_NAME]
         

Replace `[SSD_NAME]` with the ID of the Local SSD disk that you want to format. For example, specify `google-local-nvme-ssd-0` to format the first NVMe Local SSD disk on the instance.

  5. Use the `mkdir` command to create a directory where you can mount the device.
         
         $ sudo mkdir -p /mnt/disks/[MNT_DIR]
         

Replace `[MNT_DIR]` with the directory path where you want to mount your Local SSD disk.

  6. Mount the Local SSD disk to the compute instance.
         
         $ sudo mount /dev/disk/by-id/[SSD_NAME] /mnt/disks/[MNT_DIR]
         

Replace the following:

     * `[SSD_NAME]`: the ID of the Local SSD disk that you want to mount.
     * `[MNT_DIR]`: the directory where you want to mount your Local SSD disk.
  7. Configure read and write access to the device. For this example, grant write access to the device for all users.
         
         $ sudo chmod a+w /mnt/disks/[MNT_DIR]
         

Replace `[MNT_DIR]` with the directory where you mounted your Local SSD disk.




Optionally, you can add the Local SSD disk to the `/etc/fstab` file so that the device automatically mounts again when the instance restarts. This entry does not preserve data on your Local SSD disk if the instance stops. See [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence) for complete details.

When you specify the entry `/etc/fstab` file, be sure to include the `nofail` option so that the instance can continue to boot even if the Local SSD is not present. For example, if you take a snapshot of the boot disk and create a new instance without any Local SSD disks attached, the instance can continue through the startup process and not pause indefinitely.

  1. Create the `/etc/fstab` entry. Use the `blkid` command to find the UUID for the file system on the device and edit the `/etc/fstab` file to include that UUID with the mount options. You can complete this step with a single command.

For example, for a Local SSD in NVMe mode, use the following command:
         
         $ echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-local-nvme-ssd-0` /mnt/disks/[MNT_DIR] ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
         

For a Local SSD in a non-NVMe mode such as SCSI, use the following command:
         
         $ echo UUID=`sudo blkid -s UUID -o value /dev/disk/by-id/google-local-ssd-0` /mnt/disks/[MNT_DIR] ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
         

Replace `[MNT_DIR]` with the directory where you mounted your Local SSD.

  2. Use the `cat` command to verify that your `/etc/fstab` entries are correct:
         
         $ cat /etc/fstab
         




If you create a snapshot from the boot disk of this instance and use it to create a separate instance that does not have Local SSD disks, edit the `/etc/fstab` file and remove the entry for this Local SSD disk. Even with the `nofail` option in place, keep the `/etc/fstab` file in sync with the partitions that are attached to your instance and remove these entries before you create your boot disk snapshot.

###  Windows instances 

Use the Windows [Disk Management tool](https://technet.microsoft.com/en-us/library/dd163549.aspx) to format and mount a Local SSD disk on a Windows instance.

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) through RDP. For this example, go to the [VM instances page](https://console.cloud.google.com/compute/instances) and click the **RDP** button next the instance that has the Local SSD disks attached. After you enter your username and password, a window opens with the desktop interface for your server.

  2. Right-click the Windows Start button and select **Disk Management**.

![Selecting the Windows Disk Manager tool from the right-click menu on the Windows Start button.](https://docs.cloud.google.com/static/compute/images/start_disk_manager_windows.png)

  3. If you have not initialized the Local SSD disk before, the tool prompts you to select a partitioning scheme for the new partitions. Select **GPT** and click **OK**.

![Selecting a partition scheme in the disk initialization window.](https://docs.cloud.google.com/static/compute/images/initialize_disk_windows.png)

  4. After the Local SSD disk initializes, right-click the unallocated disk space and select **New Simple Volume**.

![Creating a new simple volume from the attached disk.](https://docs.cloud.google.com/static/compute/images/local_ssd_new_volume_windows.png)

  5. Follow the instructions in the **New Simple Volume Wizard** to configure the new volume. You can use any partition format that you like, but for this example select `NTFS`. Also, select **Perform a quick format** to speed up the formatting process.

![Selecting the partition format type in the New Simple Volume Wizard.](https://docs.cloud.google.com/static/compute/images/configure_new_volume_windows.png)

  6. After you complete the wizard and the volume finishes formatting, check the new Local SSD disk to ensure it has a `Healthy` status.

![Viewing the list of disks that are recognized by Windows, verify that the Local SSD has a Healthy status.](https://docs.cloud.google.com/static/compute/images/local_ssd_healthy_windows.png)




That's it! You can now write files to the Local SSD disk.

### Format and mount multiple Local SSD disks into a single logical volume

Unlike Google Cloud Hyperdisk and Persistent Disk volumes, Local SSD disks have a [fixed capacity for each disk](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds) that you attach to the instance. If you want to combine multiple Local SSD disks into a single logical volume, then you must define volume management across these partitions yourself.

**Note:** Due to the underlying hardware configuration, using parity or mirroring RAID levels across Local SSD disks does not provide any actual reliability or redundancy benefit. Use RAID 0 to get the best performance and the greatest capacity from your Local SSD arrays.

###  Linux instances 

Use `mdadm` to create a RAID 0 array. This example formats the array with a single `ext4` file system, but you can apply any file system that you prefer.

**Note:** Although you can create an `/etc/fstab` entry to automatically mount the Local SSD disk during an instance reboot, it does not allow data on the Local SSD disk to persist through stopping or preemption.

  1. Go to the VM instances page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **SSH** button next to the instance that has the new attached Local SSD disk. The browser opens a terminal connection to the instance.

  3. In the terminal, install the `mdadm` tool. The install process for `mdadm` includes a user prompt that halts scripts, so run this process manually.

Debian and Ubuntu: 
         
         $ sudo apt update && sudo apt install mdadm --no-install-recommends
         

CentOS and RHEL: 
         
         $ sudo yum install mdadm -y
         

SLES and openSUSE: 
         
         $ sudo zypper install -y mdadm
         

  4. Use the `find` command to identify all of the Local SSD disks that you want to mount together.

For this example, the instance has eight Local SSD partitions in NVMe mode:
         
         $  find /dev/ | grep google-local-nvme-ssd
         
          /dev/disk/by-id/google-local-nvme-ssd-7
          /dev/disk/by-id/google-local-nvme-ssd-6
          /dev/disk/by-id/google-local-nvme-ssd-5
          /dev/disk/by-id/google-local-nvme-ssd-4
          /dev/disk/by-id/google-local-nvme-ssd-3
          /dev/disk/by-id/google-local-nvme-ssd-2
          /dev/disk/by-id/google-local-nvme-ssd-1
          /dev/disk/by-id/google-local-nvme-ssd-0
         

`find` does not guarantee an ordering. It's alright if the devices are listed in a different order as long as number of output lines match the expected number of SSD disks. Local SSD disks in SCSI mode have standard names like `google-local-ssd`. Local SSD disks in NVMe mode have names like `google-local-nvme-ssd`.

  5. Use `mdadm` to combine multiple Local SSD disk into a single array named `/dev/md0`. This example merges eight Local SSD disk in NVMe mode. For Local SSD disks in SCSI mode, specify the names that you obtained from the `find` command:
         
         $ sudo mdadm --create /dev/md0 --level=0 --raid-devices=8 \
          /dev/disk/by-id/google-local-nvme-ssd-0 \
          /dev/disk/by-id/google-local-nvme-ssd-1 \
          /dev/disk/by-id/google-local-nvme-ssd-2 \
          /dev/disk/by-id/google-local-nvme-ssd-3 \
          /dev/disk/by-id/google-local-nvme-ssd-4 \
          /dev/disk/by-id/google-local-nvme-ssd-5 \
          /dev/disk/by-id/google-local-nvme-ssd-6 \
          /dev/disk/by-id/google-local-nvme-ssd-7
         
         mdadm: Defaulting to version 1.2 metadata
         mdadm: array /dev/md0 started.
         
         

You can confirm the details of the array with `mdadm --detail`. Adding the `--prefer=by-id` flag will list the devices using the `/dev/disk/by-id` paths.
         
         sudo mdadm --detail --prefer=by-id /dev/md0
          

The output should look similar to the following for each device in the array. 
         
         ...
          Number   Major   Minor   RaidDevice State
             0      259      0         0      active sync   /dev/disk/by-id/google-local-nvme-ssd-0
          ...
          

  6. Format the full `/dev/md0` array with an ext4 file system.

**Caution:** This command **deletes** all existing data from the Local SSD disks.
         
         $ sudo mkfs.ext4 -F /dev/md0
         

  7. Create a directory to where you can mount `/dev/md0`. For this example, create the `/mnt/disks/ssd-array` directory:
         
         $ sudo mkdir -p /mnt/disks/[MNT_DIR]
         

Replace `[MNT_DIR]` with the directory where you want to mount your Local SSD array.

  8. Mount the `/dev/md0` array to the `/mnt/disks/ssd-array` directory:
         
         $ sudo mount /dev/md0 /mnt/disks/[MNT_DIR]
         

Replace `[MNT_DIR]` with the directory where you want to mount your Local SSD array.

  9. Configure read and write access to the device. For this example, grant write access to the device for all users.
         
         $ sudo chmod a+w /mnt/disks/[MNT_DIR]
         

Replace `[MNT_DIR]` with the directory where you mounted your Local SSD array.




Optionally, you can add the Local SSD disk to the `/etc/fstab` file so that the device automatically mounts again when the instance restarts. This entry does not preserve data on your Local SSD disk if the instance stops. See [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence) for details.

When you specify the entry `/etc/fstab` file, be sure to include the `nofail` option so that the instance can continue to boot even if the Local SSD disk is not present. For example, if you take a snapshot of the boot disk and create a new instance without any Local SSD disks attached, the instance can continue through the startup process and not pause indefinitely.

  1. Create the `/etc/fstab` entry. Use the `blkid` command to find the UUID for the file system on the device and edit the `/etc/fstab` file to include that UUID with the mount options. Specify the `nofail` option to allow the system to boot even if the Local SSD disk is unavailable.You can complete this step with a single command. For example:
         
         $ echo UUID=`sudo blkid -s UUID -o value /dev/md0` /mnt/disks/[MNT_DIR] ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
         

Replace `[MNT_DIR]` with the directory where you mounted your Local SSD array.

  2. If you use a device name like `/dev/md0` in the `/etc/fstab` file instead of the UUID, you need to edit the file `/etc/mdadm/mdadm.conf` to make sure the array is reassembled automatically at boot. To do this, complete the following two steps:

     1. Make sure the disk array is scanned and reassembled automatically when the compute instance boots. 
            
            $ sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
            

     2. Update `initramfs` so that the array is available during the early boot process. 
            
            $ sudo update-initramfs -u
            

  3. Use the `cat` command to verify that your `/etc/fstab` entries are correct:
         
         $ cat /etc/fstab
         




If you create a snapshot from the boot disk of this instance and use it to create a separate instance that does not have Local SSD disks, edit the `/etc/fstab` file and remove the entry for this Local SSD disk array. Even with the `nofail` option in place, keep the `/etc/fstab` file in sync with the partitions that are attached to your instance and remove these entries before you create your boot disk snapshot.

###  Windows instances 

Use the Windows [Disk Management tool](https://technet.microsoft.com/en-us/library/dd163549.aspx) to format and mount an array of Local SSD disks on a Windows instance.

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) through RDP. For this example, go to the [VM instances page](https://console.cloud.google.com/compute/instances) and click the **RDP** button next the instance that has the Local SSD disks attached. After you enter your username and password, a window opens with the desktop interface for your server.

  2. Right-click the Windows Start button and select **Disk Management**.

![Selecting the Windows Disk Manager tool from the right-click menu on the Windows Start button.](https://docs.cloud.google.com/static/compute/images/start_disk_manager_windows.png)

  3. If you have not initialized the Local SSD disks before, the tool prompts you to select a partitioning scheme for the new partitions. Select **GPT** and click **OK**.

![Selecting a partition scheme in the disk initialization window.](https://docs.cloud.google.com/static/compute/images/initialize_multiple_disks_windows.png)

  4. After the Local SSD disk initializes, right-click the unallocated disk space and select **New Striped Volume**.

![Creating a new striped volume from the attached disk.](https://docs.cloud.google.com/static/compute/images/local_ssd_new_striped_volume_windows.png)

  5. Select the Local SSD disks that you want to include in the striped array. For this example, select all of the partitions to combine them into a single Local SSD disk.

![Selecting the Local SSD partitions to include in the array.](https://docs.cloud.google.com/static/compute/images/configure_new_striped_volumes_windows.png)

  6. Follow the instructions in the **New Striped Volume Wizard** to configure the new volume. You can use any partition format that you like, but for this example select `NTFS`. Also, select **Perform a quick format** to speed up the formatting process.

![Selecting the partition format type in the New Striped Volume Wizard.](https://docs.cloud.google.com/static/compute/images/configure_new_volume_windows.png)

  7. After you complete the wizard and the volume finishes formatting, check the new Local SSD disk to ensure it has a `Healthy` status.

![Viewing the list of disks that are recognized by Windows, verify that the Local SSD has a Healthy status.](https://docs.cloud.google.com/static/compute/images/local_ssd_array_healthy_windows.png)




You can now write files to the Local SSD disk.

## What's next

  * Learn more about [device names](https://docs.cloud.google.com/compute/docs/disks/local-ssd#device_names) for your compute instances.
  * Learn how to [benchmark performance for Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/benchmarking-local-ssd-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
