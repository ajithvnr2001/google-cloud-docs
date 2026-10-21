---
url: https://docs.cloud.google.com/compute/docs/instances/create-vm-specific-subnet/
title: Create an instance in a specific subnet \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:57.578743+00:00
---

# Create an instance in a specific subnet  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-vm-specific-subnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance in a specific subnet Stay organized with collections  Save and categorize content based on your preferences. 

By default, every instance has a single network interface that determines the VPC network that the instance uses. You can [create an instance with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces), where each interface must connect to a different subnet. Each subnet defines the range of IPv4 or IPv6 addresses that can be assigned to the instance.

For more information, see the following:

  * [IP addresses](https://docs.cloud.google.com/compute/docs/networking/network-overview#ip-addresses)
  * [Create an instance that uses IPv6 addresses](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance)



By default, Google Cloud creates an [auto mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) called `default` for each project. To use a different network or a subnet that you manually created in an auto mode or custom mode VPC network, you must specify the subnet when you create the instance and configure the network interface.

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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create an instance with a specific subnet, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create an instance with a specific subnet. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an instance with a specific subnet:

  * compute.instances.create on the project
  * To specify a subnet for your instance: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To assign an external IP address to the instance when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Requirements

When you create an instance in a subnet, consider these rules:

  * If you don't specify a network or subnet, Compute Engine uses the default VPC network and the auto subnet that's in the same region as the instance.
  * If you don't specify a network, Compute Engine infers the network from the subnet specified.
  * If you specify a network, you must specify a subnet and it must belong to the same network. Otherwise, instance creation fails.



You must create the subnet that you want to use before you create the instance. For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

## Create an instance in a specific subnet

To create an instance in a specific subnet, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**.

The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Optional: In the **Zone** field, select a zone for this instance.

The default selection is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability. 

     3. Select the machine family for your instance. The Google Cloud console then displays the machine series that are available for your selected machine family. The following machine family options are available:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**
     4. In the **Series** column, select the machine series for your instance.

If you selected **GPUs** as the machine family in the previous step, then select the **GPU type** that you want. The machine series is then automatically selected for the selected GPU type.

     5. In the **Machine type** section, select the machine type for your instance.

  3. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. To permit HTTP or HTTPS traffic to the instance, go to the **Firewall** section and select **Allow HTTP traffic** or **Allow HTTPS traffic**.

The Compute Engine adds a network tag to your instance and creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS). The network tag associates the firewall rule with the instance. For more information, see [Firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls) in the Cloud Next Generation Firewall documentation.

     2. To specify the network interface details, go to the **Network interfaces** section and click **Add a network interface**.

In the **New network interface** section that appears, do the following:

        1. In the **Network** field, select the VPC network that contains the subnet you created.
        2. In the **Subnetwork** list, select the subnet for the instance to use.
        3. In the **IP stack type** field, select the IP stack type for the network interface.
        4. To confirm the network interface details, click **Done**.
  4. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  5. To create and start the instance, click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Using the Google Cloud CLI, follow the same instructions to [create an instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image) or a [snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot), and include the networking flags shown in this section when you run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
         
         gcloud compute instances create INSTANCE_NAME \
             --zone=ZONE \
             --machine-type=MACHINE_TYPE \
             --create-disk=boot=yes,image=projects/IMAGE_PROJECT/global/images/IMAGE,size=SIZE \
             --network=NETWORK_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=STACK_TYPE \
             --private-network-ip=INTERNAL_IPV4_ADDRESS \
             --address=EXTERNAL_IPV4_ADDRESS \
             --nic-type=GVNIC
         

Replace the following:

     * `INSTANCE_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the compute instance
     * `ZONE`: the zone where the instance is created, such as `europe-west1-b`. The instance's region is inferred from the zone.
     * `MACHINE_TYPE`: Optional: the machine type to use for the instance.
     * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image
     * `IMAGE`: Optional: specify one of the following: 
       * A specific version of the OS image—for example, `rocky-linux-9-optimized-gcp-v20240717`.
       * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/rocky-linux-9-optimized-gcp`, then Compute Engine creates an instance using the latest version of the OS image in the Rocky Linux 9 optimized for Google Cloud image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
     * `SIZE`: Optional: the size of the new disk. The value must be a whole number. The default unit of measurement is GiB.
     * `NETWORK_NAME`: Optional: name of the network
     * `SUBNET_NAME`: name of the subnet to use with the instance.

To view a list of subnets in the network, use the [`gcloud compute networks subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list).

     * `STACK_TYPE`: Optional: the stack type for the network interface. `STACK_TYPE` must be one of: `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY`. The default value is `IPV4_ONLY`.

     * `INTERNAL_IPV4_ADDRESS`: Optional: the internal IPv4 address that you want the compute instance to use in the target subnet. Omit this flag if you don't need a specific IP address.

To specify an internal IPv6 address, use the flag `--internal-ipv6-address` instead.

     * `EXTERNAL_IPV4_ADDRESS`: Optional: the static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following:

       * Specify a valid IPv4 address from the subnet.
       * Use the flag `--network-interface=no-address` instead if you don't want the network interface to have an external IP address.
       * Specify `address=''` if you want the interface to receive an ephemeral external IP address.

To specify an external IPv6 address, use the flag `--external-ipv6-address` instead.




###  Terraform 

To create an instance in a specific subnet, you can use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).
    
    
    # Create a VM in a custom VPC network and subnet
    
    resource "google_compute_instance" "custom_subnet" {
      name         = "my-vm-instance"
      tags         = ["allow-ssh"]
      zone         = "europe-west1-b"
      machine_type = "e2-small"
      network_interface {
        network    = google_compute_network.custom.id
        subnetwork = google_compute_subnetwork.custom.id
      }
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-12"
        }
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
    
    // createInstanceWithSubnet creates a new VM instance with Debian 10 operating system in specified network and subnetwork.
    func createInstanceWithSubnet(w io.Writer, projectID, zone, instanceName, networkLink, subnetworkLink string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// networkLink := "global/networks/default"
    	// subnetworkLink := "regions/region/subnetworks/subnetwork_name"
    
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
    			},
    			MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					Name:       proto.String(networkLink),
    					Subnetwork: proto.String(subnetworkLink),
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

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type;
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.Vector;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstancesAdvanced {
    
      /**
       * Create an AttachedDisk object to be used in VM instance creation. Uses an image as the source
       * for the new disk.
       *
       * @param diskType the type of disk you want to create. This value uses the following format:
       * "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)". For example:
       * "zones/us-west3-b/diskTypes/pd-ssd"
       * @param diskSizeGb size of the new disk in gigabytes
       * @param boot boolean flag indicating whether this disk should be used as a boot disk of an
       * instance
       * @param sourceImage source image to use when creating this disk. You must have read access to
       * this disk. This can be one of the publicly available images or an image from one of your
       * projects. This value uses the following format:
       * "projects/{project_name}/global/images/{image_name}"
       * @return AttachedDisk object configured to be created using the specified image.
       */
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) diskFromImage(String diskType, int diskSizeGb, boolean boot,
          String sourceImage) {
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk =
            [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                .setBoot(boot)
                // Remember to set auto_delete to True if you want the disk to be deleted when
                // you delete your VM instance.
                .setAutoDelete(true)
                .setType(Type.PERSISTENT.toString())
                .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                    [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                        .setSourceImage(sourceImage)
                        .setDiskSizeGb(diskSizeGb)
                        .setDiskType(diskType)
                        .build())
                .build();
        return disk;
      }
    
    
      /**
       * Send an instance creation request to the Compute Engine API and wait for it to complete.
       *
       * @param project project ID or project number of the Cloud project you want to use.
       * @param zone name of the zone to create the instance in. For example: "us-west3-b"
       * @param instanceName name of the new virtual machine (VM) instance.
       * @param disks a list of compute_v1.AttachedDisk objects describing the disks you want to attach
       * to your new instance.
       * @param machineType machine type of the VM being created. This value uses the following format:
       * "zones/{zone}/machineTypes/{type_name}".
       * For example: "zones/europe-west3-c/machineTypes/f1-micro"
       * @param network name of the network you want the new instance to use. For example:
       * "global/networks/default" represents the network named "default", which is created
       * automatically for each project.
       * @param subnetwork name of the subnetwork you want the new instance to use. This value uses the
       * following format: "regions/{region}/subnetworks/{subnetwork_name}"
       * @return Instance object.
       */
      private static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createWithDisks(String project, String zone, String instanceName,
          Vector<AttachedDisk> disks, String machineType, String network, String subnetwork)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          // Use the network interface provided in the networkName argument.
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface;
          if (subnetwork != null) {
            networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                .setName(network).setSubnetwork(subnetwork)
                .build();
          } else {
            networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                .setName(network).build();
          }
    
          machineType = String.format("zones/%s/machineTypes/%s", zone, machineType);
    
          // Bind `instanceName`, `machineType`, `disk`, and `networkInterface` to an instance.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instanceResource =
              [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
                  .setName(instanceName)
                  .setMachineType(machineType)
                  .addAllDisks(disks)
                  .addNetworkInterfaces(networkInterface)
                  .build();
    
          System.out.printf("Creating instance: %s at %s ", instanceName, zone);
    
          // Insert the instance in the specified project and zone.
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstanceResource(instanceResource).build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.insertAsync(
              insertInstanceRequest);
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance creation failed ! ! " + response);
            return null;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
    
          return instancesClient.get(project, zone, instanceName);
        }
      }

###  Node.js 

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const networkLink = 'global/networks/default';
    // const subnetworkLink = 'regions/europe-central2/subnetworks/default';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Creates a new VM instance with Debian 10 operating system in specified network and subnetwork.
    async function createInstanceWithSubnet() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
      const imagesClient = new compute.[ImagesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details.
      const [newestDebian] = await imagesClient.getFromFamily({
        project: 'debian-cloud',
        family: 'debian-11',
      });
    
      const [response] = await instancesClient.insert({
        project: projectId,
        zone,
        instanceResource: {
          name: instanceName,
          disks: [
            {
              initializeParams: {
                diskSizeGb: '10',
                sourceImage: newestDebian.selfLink,
                diskType: `zones/${zone}/diskTypes/pd-standard`,
              },
              autoDelete: true,
              boot: true,
              type: 'PERSISTENT',
            },
          ],
          machineType: `zones/${zone}/machineTypes/n1-standard-1`,
          networkInterfaces: [
            {
              name: networkLink,
              subnetwork: subnetworkLink,
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
    
    createInstanceWithSubnet();

###  Python 

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
    
    
    def create_with_subnet(
        project_id: str, zone: str, instance_name: str, network_link: str, subnet_link: str
    ) -> compute_v1.Instance:
        """
        Create a new VM instance with Debian 10 operating system in specified network and subnetwork.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
                "regions/{region}/subnetworks/{subnetwork_name}"
    
        Returns:
            Instance object.
        """
        newest_debian = get_image_from_family(project="debian-cloud", family="debian-12")
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_image(disk_type, 10, True, newest_debian.self_link)]
        instance = create_instance(
            project_id,
            zone,
            instance_name,
            disks,
            network_link=network_link,
            subnetwork_link=subnet_link,
        )
        return instance
    
    

###  REST 

Follow the `REST` instructions to [create an instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image) or a [snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot), but specify the `subnet` field in the request body.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "machineType":"zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
       "name":"VM_NAME",
       
       "disks":[
          {
             "initializeParams":{
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE"
             },
             "boot":true
          }
       ],
       
       
       "networkInterfaces":[
          {
             "network":"global/networks/NETWORK_NAME",
             "subnetwork":"regions/REGION/subnetworks/SUBNET_NAME",
             "stackType":"STACK_TYPE"
          }
       ],
       
      
       "shieldedInstanceConfig":{
          "enableSecureBoot":"ENABLE_SECURE_BOOT"
       }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project to create the VM in
  * `ZONE`: zone to create the VM in
  * `MACHINE_TYPE_ZONE`: zone containing the machine type to use for the new VM
  * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types), for the new VM
  * `VM_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM
  * `IMAGE_PROJECT`: [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) containing the image  
For example, if you specify `debian-10` as the image family, specify `debian-cloud` as the image project.
  * `IMAGE`: specify one of the following: 
    * `IMAGE`: a specific version of a public image

For example, `"sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200309"`

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images#image_families)

This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-10"`, Compute Engine creates a VM from the latest version of the OS image in the `Debian 10` image family.

  * `NETWORK_NAME`: Optional: the VPC network that you want to use for the VM. You can specify `default` to use your default network.
  * `REGION`: region where the specified subnet exists. This must be the same region as the VM.
  * `SUBNET_NAME`: name of the subnet to use
  * `STACK_TYPE`: Optional: the stack type for the network interface. You can specify one of `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY`. The default value is `IPV4_ONLY`.
  * `ENABLE_SECURE_BOOT`: Optional: If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features, Compute Engine, by default, enables the [virtual trusted platform module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) and [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring). Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default.

If you specify `true` for `enableSecureBoot`, Compute Engine creates a VM with all three Shielded VM features enabled. After Compute Engine starts your VM, to [modify Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm) options, you must stop the VM.




**Note:** A network interface can have only one IPv6 address, either internal or external, but not both.

## What's next?

  * Learn how to [check the status of an instance](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) to see when it is ready to use.
  * Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
