---
url: https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates/
title: Create instance templates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:26:53.087101+00:00
---

# Create instance templates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create instance templates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates). Instance templates let you specify the machine type, boot disk image, network, and other VM properties that you want to use when creating virtual machine (VM) instances.

You can use instance templates to do the following:

  * Create [individual VMs](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).
  * Create VMs in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups).
  * Create [ reservations for VMs](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).



## Before you begin

  * Read when and why to create [deterministic instance templates.](https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates)
  * Read about [regional and global instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#global_and_regional_instance_templates).
  * If you include Dynamic Network Interfaces (NICs) in the instance template, review the properties and limitations of Dynamic NICs as described in [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics). For more information about creating instances with multiple network interfaces, see [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).
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




## Limitations

  * Shared VPC on interfaces other than `nic0` for instance templates is supported in gcloud CLI and REST, but not in Google Cloud console.
  * You can't update an existing instance template or change an instance template after it has been created. If an instance template goes out of date, or you need to make changes to the configuration, create a new instance template.
  * If you want to specify an image family in an instance template, you can't use the Google Cloud console. You can use the Google Cloud CLI or REST instead.
  * If you want to specify regional disks instead of zonal disks in an instance template, you can't use the Google Cloud console. You can use the Google Cloud CLI or REST instead.
  * You can use an instance template to create VMs with a Hyperdisk Balanced boot disk that is in a [storage pool](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity#create-template), if the storage pool exists in the same zone that the VM is created in. You can't use global instance templates to create VMs with non-boot disks that are in a storage pool.



## Create an instance template

Most of the VM properties that you can specify in a request to create an individual VM instance can also be specified for an instance template, including any VM metadata, startup scripts, persistent disks, and service accounts. You must specify the machine type, boot disk, and network.

Create a regional or global instance template through the [Google Cloud console](https://console.cloud.google.com/), [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or the [API](https://docs.cloud.google.com/compute/docs/reference/latest/instanceTemplates). To create a global instance template, you can also use the Terraform or the [Cloud Client Libraries](https://docs.cloud.google.com/compute/docs/api/libraries).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).



###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates?walkthrough_id=compute--create-new-instance-template&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create instance template**.
  3. Select the **Location** as follows:
     1. If you want to use the instance template across regions, choose **Global**.
     2. If you want to reduce cross-region dependency, choose **Regional**.
  4. If you chose regional, then select the **Region** where you want to create your instance template.
  5. For the following fields, either accept the default values or modify them as required. The default values change based on the machine family that you select.

     * Select a **Machine type**.
     * To update the boot disk type or image, in the Boot disk section, click **Change**.
     * To update the network interface or IP address settings, click **Advanced options** , then click **Networking** , and then click the network interface you want to edit.
  6. Optional: If you chose an image that supports Shielded VM, change the VM's [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) settings:

     1. Click **Advanced options** , and then click the **Security** tab.
     2. If you want to disable Secure Boot, clear the **Turn on Secure Boot** checkbox. Secure Boot helps protect your VM instances against boot-level and kernel-level malware and rootkits. For more information, see [Secure boot](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm#secure-boot).
     3. If you want to disable the virtual trusted platform module (vTPM), clear the **Turn on vTPM** checkbox. The vTPM enables Measured boot, which validates the VM pre-boot and boot integrity. For more information, see [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm#vtpm).

**Important** : Disabling the vTPM also disables integrity monitoring because integrity monitoring relies on data gathered by Measured boot.
     4. If you want to disable integrity monitoring, uncheck the **Turn on Integrity Monitoring** checkbox. Integrity monitoring lets youn monitor the boot integrity of your Shielded VM instances by using Cloud Monitoring. For more information, see [Integrity monitoring](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm#integrity-monitoring).

  7. Optional: Under **Advanced options** , click the tabs to further customize your template. For example, you can add up to 15 secondary non-boot disks.

  8. Optional: Click **Equivalent REST** to view the REST request body, which includes the [JSON representation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates) of your instance template.

  9. Click **Create** to create the template.




###  gcloud 

To create a regional or global instance template, use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create). For a regional instance template, you must use the `--instance-template-region` flag to set the region of the template.

Create a regional instance template using the following command.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --instance-template-region=REGION
    

Replace `REGION` with the region where you want to create the regional instance template.

Create a global instance template using the following command:
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME
    

If you don't provide explicit template settings, `gcloud compute` uses the following default values:

  * Machine type: the machine type—for example, `n1-standard-1`
  * Image: the latest Debian image
  * Boot disk: a new standard boot disk named after the VM
  * Network: the default VPC network
  * IP address: an ephemeral external IPv4 address
  * Stack type: `IPV4_ONLY`



You can also explicitly provide these configuration settings. For example:
    
    
    gcloud compute instance-templates create my-instance-template \
        --machine-type=e2-standard-4 \
        --image-family=debian-13 \
        --image-project=debian-cloud \
        --boot-disk-size=250GB

You can add up to 15 secondary non-boot disks. Specify the `--create-disk` flag for each secondary disk you create. To create secondary disks from a public or custom image, specify the `image` and `image-project` properties for each disk in the `--create-disk` flag. To create a blank disk, don't include these properties. Optionally, include properties for the disk `size` and `type`. To specify regional disks, use the `replica-zones` property.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --create-disk=image-family=DISK_IMAGE_FAMILY,image-project=DISK_IMAGE_PROJECT,size=SIZE_GB_DISK1 \
        --create-disk=device-name=DISK_NAME,type=DISK_TYPE,size=SIZE_GB_DISK2,replica-zones=^:^ZONE:REMOTE_ZONE,boot=false
    

Tip: When specifying the disk `replica-zones` parameter, the characters `^:^` specify that the separation character between values is a colon (`:`) instead of the expected comma (`,`).

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name for the template
  * `MACHINE_TYPE`: the machine type of the VMs
  * `DISK_IMAGE_FAMILY`: an image family to use as a non-boot disk

For more information about image families, see [best practices when using image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices) on Compute Engine.

You can use instead the flag `--image=IMAGE` to specify a specific version of an image.

For blank disks, don't specify the `image-family` or `image` property.

  * `DISK_IMAGE_PROJECT`: the image project that contains the image

For blank disks, don't specify the `image-project` property. For more information on public images, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `SIZE_GB_DISK1` and `SIZE_GB_DISK2`: the size of each secondary disk

  * `DISK_NAME`: Optional: the disk name displayed to the guest OS after the VM is created.

  * `DISK_TYPE`: Optional: the type of disk to create. If not specified, the default disk type that is used depends on the value of the `--machine-type` flag.

  * `ZONE` and `REMOTE_ZONE`: the zone to create the [regional disk](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) in and the zone to replicate it to.

For zonal disks, don't include the `replica-zones` property.




If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm), you can optionally change the instance's Shielded VM settings using one of the following flags:

  * `--no-shielded-secure-boot`: turns off Secure Boot

Secure Boot helps protect your VM instances against boot-level and kernel-level malware and rootkits. For more information, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).

  * `--no-shielded-vtpm`: turns off the virtual trusted platform module (vTPM)

The vTPM enables Measured Boot, which validates the VM pre-boot and boot integrity. For more information, see [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).

**Important:** Disabling the vTPM also disables integrity monitoring because integrity monitoring relies on data gathered by Measured Boot.
  * `--no-shielded-integrity-monitoring`: turns off integrity monitoring

Integrity monitoring lets you monitor the boot integrity of your Shielded VM instances using Cloud Monitoring. For more information, see [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).




For a list of all available subcommands and flags, see the [`instance-templates` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates).

### Terraform

To create an instance template, use one of the following resources:

  * For a regional instance template, use the [`google_compute_region_instance_template` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_template).
  * For a global instance template, use the [`google_compute_instance_template` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template).



The following example creates a global instance template:
    
    
    resource "google_compute_instance_template" "foobar" {
      name         = "my-instance-template"
      machine_type = "e2-standard-4"
    
      disk {
        source_image = "debian-cloud/debian-13"
        disk_size_gb = 250
      }
    
      network_interface {
        network = "default"
    
        # default access config, defining external IP configuration
        access_config {
          network_tier = "PREMIUM"
        }
      }
    
      # To avoid embedding secret keys or user credentials in the instances, Google recommends that you use custom service accounts with the following access scopes.
      service_account {
        scopes = [
          "https://www.googleapis.com/auth/cloud-platform"
        ]
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createTemplate creates a new instance template with the provided name and a specific instance configuration.
    func createTemplate(w io.Writer, projectID, templateName string) error {
    	// projectID := "your_project_id"
    	// templateName := "your_template_name"
    
    	ctx := context.Background()
    	instanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer instanceTemplatesClient.Close()
    
    	req := &computepb.InsertInstanceTemplateRequest{
    		Project: projectID,
    		InstanceTemplateResource: &computepb.InstanceTemplate{
    			Name: proto.String(templateName),
    			Properties: &computepb.InstanceProperties{
    				// The template describes the size and source image of the boot disk
    				// to attach to the instance.
    				Disks: []*computepb.AttachedDisk{
    					{
    						InitializeParams: &computepb.AttachedDiskInitializeParams{
    							DiskSizeGb:  proto.Int64(250),
    							SourceImage: proto.String("projects/debian-cloud/global/images/family/debian-12"),
    						},
    						AutoDelete: proto.Bool(true),
    						Boot:       proto.Bool(true),
    					},
    				},
    				MachineType: proto.String("e2-standard-4"),
    				// The template connects the instance to the `default` network,
    				// without specifying a subnetwork.
    				NetworkInterfaces: []*computepb.NetworkInterface{
    					{
    						Name: proto.String("global/networks/default"),
    						// The template lets the instance use an external IP address.
    						AccessConfigs: []*computepb.AccessConfig{
    							{
    								Name:        proto.String("External NAT"),
    								Type:        proto.String(computepb.[AccessConfig_ONE_TO_ONE_NAT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_TYPE_AccessConfig_DIRECT_IPV6_AccessConfig_ONE_TO_ONE_NAT).String()),
    								NetworkTier: proto.String(computepb.[AccessConfig_PREMIUM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_NETWORK_TIER_AccessConfig_FIXED_STANDARD_AccessConfig_PREMIUM_AccessConfig_STANDARD_AccessConfig_STANDARD_OVERRIDES_FIXED_STANDARD).String()),
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    
    	op, err := instanceTemplatesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance template: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance template created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).NetworkTier;
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateInstanceTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you use.
        // templateName: name of the new template to create.
        String projectId = "your-project-id";
        String templateName = "template-name";
        createInstanceTemplate(projectId, templateName);
      }
    
      /*
        Create a new instance template with the provided name and a specific
        instance configuration.
       */
      public static void createInstanceTemplate(String projectId, String templateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
    
          String machineType = "e2-standard-4";
          String sourceImage = "projects/debian-cloud/global/images/family/debian-13";
    
          // The template describes the size and source image of the boot disk
          // to attach to the instance.
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setSourceImage(sourceImage)
                  .setDiskType("pd-balanced")
                  .setDiskSizeGb(250).build())
              .setAutoDelete(true)
              .setBoot(true).build();
    
          // The template connects the instance to the `default` network,
          // without specifying a subnetwork.
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
              .setName("global/networks/default")
              // The template lets the instance use an external IP address.
              .[addAccessConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.Builder.html#com_google_cloud_compute_v1_NetworkInterface_Builder_addAccessConfigs_com_google_cloud_compute_v1_AccessConfig_)([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).newBuilder()
                  .setName("External NAT")
                  .setType([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type.ONE_TO_ONE_NAT.toString())
                  .setNetworkTier(NetworkTier.PREMIUM.toString()).build()).build();
    
          [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html) instanceProperties = [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
              .addDisks(attachedDisk)
              .setMachineType(machineType)
              .addNetworkInterfaces(networkInterface).build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource([InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
                  .setName(templateName)
                  .setProperties(instanceProperties).build()).build();
    
          // Create the Instance Template.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instanceTemplatesClient.insertAsync(insertInstanceTemplateRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance Template creation failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance Template Operation Status %s: %s", templateName, response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    
      public static void createInstanceTemplateWithDiskType(String projectId, String templateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create();
            [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html) globalOperationsClient = [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setDiskSizeGb(10)
                  .setDiskType("pd-balanced")
                  .setSourceImage("projects/debian-cloud/global/images/family/debian-13").build())
              .setAutoDelete(true)
              .setBoot(true)
              .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.PERSISTENT.toString()).build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
              .setName(templateName)
              .setProperties([InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
                  .setMachineType("n1-standard-1")
                  .addDisks(disk)
                  .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                      .setName("global/networks/default").build()).build()).build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource(instanceTemplate).build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instanceTemplatesClient.insertAsync(insertInstanceTemplateRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance Template creation failed ! ! " + response);
            return;
          }
          System.out
              .printf("Instance Template Operation Status %s: %s", templateName, response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new instance template with the provided name and a specific instance configuration.
    async function createTemplate() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: {
          name: templateName,
          properties: {
            disks: [
              {
                // The template describes the size and source image of the boot disk
                // to attach to the instance.
                initializeParams: {
                  diskSizeGb: '250',
                  sourceImage:
                    'projects/debian-cloud/global/images/family/debian-11',
                },
                autoDelete: true,
                boot: true,
              },
            ],
            machineType: 'e2-standard-4',
            // The template connects the instance to the `default` network,
            // without specifying a subnetwork.
            networkInterfaces: [
              {
                // Use the network interface provided in the networkName argument.
                name: 'global/networks/default',
                // The template lets the instance use an external IP address.
                accessConfigs: [
                  {
                    name: 'External NAT',
                    type: 'ONE_TO_ONE_NAT',
                    networkTier: 'PREMIUM',
                  },
                ],
              },
            ],
          },
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Instance template created.');
    }
    
    createTemplate();

###  Python 
    
    
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
    
    
    def create_template(project_id: str, template_name: str) -> compute_v1.InstanceTemplate:
        """
        Create a new instance template with the provided name and a specific
        instance configuration.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            template_name: name of the new template to create.
    
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
        # The template describes the size and source image of the boot disk
        # to attach to the instance.
        disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = (
            "projects/debian-cloud/global/images/family/debian-13"
        )
        initialize_params.disk_size_gb = 250
        disk.initialize_params = initialize_params
        disk.auto_delete = True
        disk.boot = True
    
        # The template connects the instance to the `default` network,
        # without specifying a subnetwork.
        network_interface = compute_v1.NetworkInterface()
        network_interface.name = "global/networks/default"
    
        # The template lets the instance use an external IP address.
        access_config = compute_v1.AccessConfig()
        access_config.name = "External NAT"
        access_config.type_ = "ONE_TO_ONE_NAT"
        access_config.network_tier = "PREMIUM"
        network_interface.access_configs = [access_config]
    
        template = compute_v1.InstanceTemplate()
        template.name = template_name
        template.properties.disks = [disk]
        template.properties.machine_type = "e2-standard-4"
        template.properties.network_interfaces = [network_interface]
    
        template_client = compute_v1.InstanceTemplatesClient()
        operation = template_client.insert(
            project=project_id, instance_template_resource=template
        )
    
        wait_for_extended_operation(operation, "instance template creation")
    
        return template_client.get(project=project_id, instance_template=template_name)
    
    

###  REST 

To create a regional instance template, make a `POST` request to the [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert) as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    

To create a global instance template, make a `POST` request to the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/instanceTemplates/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    

You can add up to 15 secondary non-boot disks by using the `disks` property, with a field for each additional disk. For each additional disk, you can do the following:

  * Create additional disks with a public or custom image.
  * To add a blank disk, define the `initializeParams` entry with no `sourceImage` value.
  * To create regional disks, define the `initializeParams` entry with the property `replicaZones`.



In the body of the request, provide the template properties:
    
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default",
            "accessConfigs":
            [
              {
                "name": "external-IP",
                "type": "ONE_TO_ONE_NAT"
              }
            ]
          }
        ],
        "disks":
        [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "initializeParams":
            {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          },
          {
            "type": "PERSISTENT",
            "boot": false,
            "deviceName": "DISK_NAME",
            "initializeParams":
            {
              "replicaZones": [
                  "projects/PROJECT_NAME/zones/ZONE",
                  "projects/PROJECT_NAME/zones/REMOTE_ZONE"
              ]
            }
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `REGION`: the region where you want to create your regional instance template
  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template
  * `ZONE`: the zone where VMs are located
  * `MACHINE_TYPE`: the machine type of the VMs

  * `IMAGE_PROJECT`: the image project that contains the image 

For more information on public images, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support). 

  * `IMAGE` or `IMAGE_FAMILY`: specify one of the following: 
    * `IMAGE`: a specific version of the image 

For example, `"sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200309"`

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details)

This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-10"`, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family. 

For more information on image families, see [ best practices when using image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices) on Compute Engine.

  * `DISK_NAME`: Optional: the disk name displayed to the guest OS after the VM is created.

  * `PROJECT_NAME`: the project associated with the VM

  * `REMOTE_ZONE`: the zone where the regional disk should be replicated to




You can specify one of the following options for the `disks` property:

  * Specify `initializeParams` to create boot disks for each instance. You can create disks by using public or custom images (or [image families](https://docs.cloud.google.com/compute/docs/images#image_families)) using the `sourceImage` property, as shown in the preceding example. To add blank disks, don't specify a `sourceImage`. You can also add up to 15 secondary non-boot disks by using the `initializeParams` property for each additional disk.

  * Specify `source` to attach an existing boot disk. If you attach an existing boot disk, you can only create one instance from your template.




Optionally, you can specify the `diskSizeGb`, `diskType`, and [`labels`](https://docs.cloud.google.com/compute/docs/labeling-resources) properties for `initializeParams` and the `diskSizeGb` property for `source`.

If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm), you can optionally change the VM's Shielded VM settings by using the following Boolean request body items:

  * `enableSecureBoot`: turns on or off Secure Boot

Secure Boot helps protect your VM instances against boot-level and kernel-level malware and rootkits. For more information, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).

  * `enableVtpm`: turns on or off the virtual trusted platform module (vTPM)

The vTPM enables Measured Boot, which validates the VM pre-boot and boot integrity. For more information, see [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm). **Important:** Disabling the vTPM also disables integrity monitoring because integrity monitoring relies on data gathered by Measured Boot.

  * `enableIntegrityMonitoring`: turns on or off integrity monitoring

Integrity monitoring lets you monitor and verify the runtime boot integrity of your Shielded VM instances by using Cloud Monitoring reports. For more information, see [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).




To learn more about request parameters, see the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

## Create an instance template based on an existing instance

You can use REST or gcloud CLI to save the configuration of an existing VM instance as an instance template. You can optionally override how the source disks are defined in the template.

If you need to override other properties, first create an instance template based on an existing instance, then create a similar template with additional overrides.

**Warning:** If the existing instance contains a static external IP address, that address is copied into the instance template and might limit the use of the template.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).



###  gcloud 

Use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--source-instance` and `--source-instance-zone` flags. If you want to create a regional instance template, then you must also use the `--instance-template-region` flag to specify the region of the instance template.

To create a regional instance template, use the following command:
    
    
     gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
         --source-instance=SOURCE_INSTANCE \
         --source-instance-zone=SOURCE_INSTANCE_ZONE \
         --instance-template-region=REGION
    

To create a global instance template, use the following command:
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --source-instance=SOURCE_INSTANCE \
        --source-instance-zone=SOURCE_INSTANCE_ZONE
    

To override how the source instance's disks are defined, add one or more `--configure-disk` flags.

The following example creates a global instance template from an existing instance and overrides the source instance's disk with the specifications that you provide.
    
    
      gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
          --source-instance=SOURCE_INSTANCE \
          --source-instance-zone=SOURCE_INSTANCE_ZONE \
          --configure-disk= \
          device-name=SOURCE_DISK, \
          instantiate-from=INSTANTIATE_OPTIONS, \
          auto-delete=AUTO_DELETE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME` is the name of the template to create.
  * `SOURCE_INSTANCE` is the name of the instance to use as a model for the new template.
  * `SOURCE_INSTANCE_ZONE` is the zone that contains the source instance.
  * `SOURCE_DISK` is the name of a source-instance disk that you want to override within the template.
  * `INSTANTIATE_OPTIONS` specifies whether to include the disk and which image to use. Valid values depend on the type of disk:

    * `source-image` or `source-image-family` (valid only for boot and other persistent read-write disks). Specify this option if you want to use the same source image or source image family that was used to create the disk in the source VM instance.
    * `custom-image` (valid only for boot and other persistent read-write disks). If you want to retain applications and settings from the source VMs in your instance template, you can [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) and then specify it when you create the template. If specified, then provide the path or URL for the custom image, as shown in the following example. Alternatively, you can specify an image family using the following format:
          
          --configure-disk=device-name=DATA_DISK_NAME,instantiate-from=custom-image, \
          custom-image=projects/PROJECT_ID/global/images/family/IMAGE_FAMILY_NAME
          

    * `attach-read-only` (valid only for read-only disks).

    * `blank` (valid only for non-boot persistent disks and local SSDs). If specified, then, when the template is used to create a new instance, the disk is created unformatted. You must [format and mount](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#format_linux) the disk in a startup script before you can use it in a scalable setup.

    * `do-not-include` (valid only for non-boot persistent disks and read-only disks).

  * `AUTO_DELETE` specifies whether the disk is auto-deleted when the instance is deleted. Valid values are: `false`, `no`, `true`, and `yes`.




For example, the following command creates an instance template based on `my-source-instance`, with the option to use the original image from `data-disk-a`, but set auto-delete to `true` and replace `data-disk-b` with a custom image.
    
    
     gcloud compute instance-templates create my-instance-template  \
         --source-instance=my-source-instance \
         --configure-disk=device-name=data-disk-a,instantiate-from=source-image,auto-delete=true \
         --configure-disk=device-name=data-disk-b,instantiate-from=custom-image,custom-image=projects/cps-cloud/global/images/cos-89-16108-403-15
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createTemplateFromInstance creates a new instance template based on an existing instance.
    // This new template specifies a different boot disk.
    func createTemplateFromInstance(w io.Writer, projectID, instance, templateName string) error {
    	// projectID := "your_project_id"
    	// instance := "projects/project/zones/zone/instances/instance"
    	// templateName := "your_template_name"
    
    	ctx := context.Background()
    	instanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer instanceTemplatesClient.Close()
    
    	req := &computepb.InsertInstanceTemplateRequest{
    		Project: projectID,
    		InstanceTemplateResource: &computepb.InstanceTemplate{
    			Name:           proto.String(templateName),
    			SourceInstance: proto.String(instance),
    			SourceInstanceParams: &computepb.SourceInstanceParams{
    				DiskConfigs: []*computepb.DiskInstantiationConfig{
    					{
    						// Device name must match the name of a disk attached to the instance
    						// your template is based on.
    						DeviceName: proto.String("disk-1"),
    						// Replace the original boot disk image used in your instance with a Rocky Linux image.
    						InstantiateFrom: proto.String(computepb.[DiskInstantiationConfig_CUSTOM_IMAGE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_DiskInstantiationConfig_UNDEFINED_INSTANTIATE_FROM_DiskInstantiationConfig_ATTACH_READ_ONLY_DiskInstantiationConfig_BLANK_DiskInstantiationConfig_CUSTOM_IMAGE_DiskInstantiationConfig_DEFAULT_DiskInstantiationConfig_DO_NOT_INCLUDE_DiskInstantiationConfig_SOURCE_IMAGE_DiskInstantiationConfig_SOURCE_IMAGE_FAMILY).String()),
    						CustomImage:     proto.String("projects/rocky-linux-cloud/global/images/family/rocky-linux-8"),
    						// Override the auto_delete setting.
    						AutoDelete: proto.Bool(true),
    					},
    				},
    			},
    		},
    	}
    
    	op, err := instanceTemplatesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance template: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance template created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DiskInstantiationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.html);
    import com.google.cloud.compute.v1.[DiskInstantiationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.html).[InstantiateFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.InstantiateFrom.html);
    import com.google.cloud.compute.v1.[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[SourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateTemplateFromInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you use.
        // instance: the instance to base the new template on. This value uses the following format:
        // **NOTE**: "projects/{project}/zones/{zone}/instances/{instance_name}"
        // templateName: name of the new template to create.
        String projectId = "your-project-id";
        String templateName = "template-name";
        String instance = String.format("projects/%s/zones/%s/instances/%s", projectId, "zone",
            "instanceName");
        createTemplateFromInstance(projectId, templateName, instance);
      }
    
      // Create a new instance template based on an existing instance.
      // This new template specifies a different boot disk.
      public static void createTemplateFromInstance(String projectId, String templateName,
          String instance)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create();
            [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html) globalOperationsClient = [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html).create()) {
    
          [SourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.html) sourceInstanceParams = [SourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.html).newBuilder()
              .[addDiskConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SourceInstanceParams.Builder.html#com_google_cloud_compute_v1_SourceInstanceParams_Builder_addDiskConfigs_com_google_cloud_compute_v1_DiskInstantiationConfig_)([DiskInstantiationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.html).newBuilder()
                  // Device name must match the name of a disk attached to the instance you are
                  // basing your template on.
                  .setDeviceName("disk-1")
                  // Replace the original boot disk image used in your instance
                  // with a Rocky Linux image.
                  .[setInstantiateFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.Builder.html#com_google_cloud_compute_v1_DiskInstantiationConfig_Builder_setInstantiateFrom_java_lang_String_)([InstantiateFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.InstantiateFrom.html).CUSTOM_IMAGE.toString())
                  .[setCustomImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskInstantiationConfig.Builder.html#com_google_cloud_compute_v1_DiskInstantiationConfig_Builder_setCustomImage_java_lang_String_)(
                      String.format("projects/%s/global/images/family/%s", "rocky-linux-cloud",
                          "rocky-linux-8"))
                  // Override the AutoDelete setting.
                  .setAutoDelete(true).build())
              .build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
              .setName(templateName)
              .setSourceInstance(instance)
              .[setSourceInstanceParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.Builder.html#com_google_cloud_compute_v1_InstanceTemplate_Builder_setSourceInstanceParams_com_google_cloud_compute_v1_SourceInstanceParams_)(sourceInstanceParams)
              .build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource(instanceTemplate)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instanceTemplatesClient.insertCallable()
              .futureCall(insertInstanceTemplateRequest).get(3, TimeUnit.MINUTES);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = globalOperationsClient.wait(projectId, operation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getName__)());
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance Template creation failed ! ! " + response);
            return;
          }
          System.out.printf("Instance Template creation operation status %s: %s", templateName,
              response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const instance = 'projects/project/zones/zone/instances/instance';
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create a new instance template based on an existing instance.
    // This new template specifies a different boot disk.
    async function createTemplateFromInstance() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: {
          name: templateName,
          sourceInstance: instance,
          sourceInstanceParams: {
            diskConfigs: [
              {
                // Device name must match the name of a disk attached to the instance
                // your template is based on.
                deviceName: 'disk-1',
                // Replace the original boot disk image used in your instance with a Rocky Linux image.
                instantiateFrom: 'CUSTOM_IMAGE',
                customImage:
                  'projects/rocky-linux-cloud/global/images/family/rocky-linux-8',
                // Override the auto_delete setting.
                autoDelete: true,
              },
            ],
          },
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Instance template created.');
    }
    
    createTemplateFromInstance();

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
    
    
    def create_template_from_instance(
        project_id: str, instance: str, template_name: str
    ) -> compute_v1.InstanceTemplate:
        """
        Create a new instance template based on an existing instance.
        This new template specifies a different boot disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            instance: the instance to base the new template on. This value uses
                the following format: "projects/{project}/zones/{zone}/instances/{instance_name}"
            template_name: name of the new template to create.
    
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DiskInstantiationConfig](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DiskInstantiationConfig.html)()
        # Device name must match the name of a disk attached to the instance you are
        # basing your template on.
        disk.device_name = "disk-1"
        # Replace the original boot disk image used in your instance with a Rocky Linux image.
        disk.instantiate_from = "CUSTOM_IMAGE"
        disk.custom_image = "projects/rocky-linux-cloud/global/images/family/rocky-linux-8"
        # Override the auto_delete setting.
        disk.auto_delete = True
    
        template = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplate](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceTemplate.html)()
        template.name = template_name
        template.source_instance = instance
        template.source_instance_params = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SourceInstanceParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.SourceInstanceParams.html)()
        template.source_instance_params.disk_configs = [disk]
    
        template_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplatesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html)()
        operation = template_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_insert)(
            project=project_id, instance_template_resource=template
        )
    
        wait_for_extended_operation(operation, "instance template creation")
    
        return template_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_get)(project=project_id, instance_template=template_name)
    
    

###  REST 

To create a regional instance template, use the [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert), or, to create a global instance template, use the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

In your request, you must specify the `sourceInstance` field. To override how the source instance's disks are defined, add one or more `diskConfigs` fields.

For example, make the following call to create a global instance template from an existing instance.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "sourceInstance": "zones/SOURCE_INSTANCE_ZONE/instances/SOURCE_INSTANCE",
      "sourceInstanceParams": {
        "diskConfigs": [
          {
            "deviceName": "SOURCE_DISK",
            "instantiateFrom": "INSTANTIATE_OPTIONS",
            "autoDelete": false
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project id](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `INSTANCE_TEMPLATE_NAME`: the name for the new template
  * `SOURCE_INSTANCE_ZONE`: the zone of the source instance
  * `SOURCE_INSTANCE`: the name of the source instance to use as a model for this instance template
  * `SOURCE_DISK`: the name of a source-instance disk that you want to override within the template
  * `INSTANTIATE_OPTIONS`: specifies whether to include the disk and which image to use

Valid values depend on the type of disk:

    * `source-image` or `source-image-family` (valid only for boot and other persistent read-write disks).
    * `custom-image` (valid only for boot and other persistent read-write disks). If you want to retain applications and settings from the source VMs in your instance template, you can [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) and then specify it when you create the template. If specified, then provide the path or URL for the custom image, as shown in the following example. Alternatively, you can specify an image family using the following format:
          
          "diskConfigs": [
              {
                "deviceName": DATA_DISK_NAME,
                "instantiateFrom": custom-image,
                "customImage": "projects/PROJECT_ID/global/images/family/IMAGE_FAMILY_NAME"
              }
            ]
          

    * `attach-read-only` (valid only for read-only disks).

    * `blank` (valid only for non-boot persistent disks and local SSDs). If specified, then, when the template is used to create a new instance, the disk is created unformatted. You must [format and mount](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#format_linux) the disk in a startup script before you can use it in a scalable setup.

    * `do-not-include` (valid only for non-boot persistent disks and read-only disks).




The following example creates a new instance template based on `my-source-instance`. In the instance template, the image for `data-disk-a` is replaced with `projects/cos-cloud/global/images/cos-89-16108-403-15`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my_project/global/instanceTemplates
    
    {
      "name": "my-instance-template",
      "sourceInstance": "zones/us-central1-a/instances/my-source-instance",
      "sourceInstanceParams":
      {
        "diskConfigs":
        [
          {
            "deviceName": "data-disk-a",
            "instantiateFrom": "custom-image",
            "customImage": "projects/cos-cloud/global/images/cos-89-16108-403-15"
          }
        ]
      }
    }

The following table shows how the options for overriding disks are defined in the template.

Disk type | Options  
---|---  
Boot disk | 

  * **[Default]** Use the same source image or image family that was used to create the boot disk in the source instance.
  * Use the URL of any image (custom or public) as described in the preceding example or specify an image family using the following format:
`projects/exampleproject/global/images/family/IMAGE_FAMILY_NAME` 
  
Other read/write persistent disks | 

  * **[Default]** Use the same source image/source image family that was used to create the disk in the source instance. Note: If the source instance's disk doesn't have a source image/source image family property, then it is included in the template as a blank disk.
  * Use the URL of any image (custom or public) as described in the preceding example or specify an image family using the following format:  `projects/exampleproject/global/images/family/IMAGE_FAMILY_NAME`
  * Use a blank disk in the template instead. When the template is used to create a new instance, this disk is created unformatted. You must [format and mount](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#format_linux) the disk in a startup script before you can use it in a scalable setup.
  * Don't include the disk.

  
Read-only disk(s) | 

  * **[Default]** Include the disk in read-only mode.
  * Don't include the disk.

  
Local SSD(s) | 

  * **[Default]** Include a blank local SSD. When the template is used to create a new instance, this disk is created unformatted. You must [format and mount](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#formatandmount) the disk in a startup script before you can use it in a scalable setup.

  
  
For each disk, you can also override the `auto-delete` attribute to specify whether the disk should be deleted when its associated instance is deleted.

By default, if no override options are specified, the disk configuration in the template matches the source instance.

## Create an instance template based on an existing template

You can't update an existing instance template. But, if an instance template goes out of date or if you need to make changes, you can create another one with similar properties by using the console.

  1. Go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click the instance template that you want to copy and update.

  3. Click **Create similar**.

  4. Update the configuration in the new template.

  5. Click **Create**.




## Create an instance template for GPU VMs

When creating an instance template, you can configure it for creating VMs that have attached GPUs by specifying the following:

  * A machine type that [supports the GPU type you want](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types). If you want to create a regional instance template, the GPU type that you specify in the template must be [available in at least one zone in the region](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  * A maintenance policy that stops VMs during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).




**Note:** If you want to run data science or machine learning workloads, consider using a Deep Learning VM image when you create an instance template. Deep Learning VM Images is a set of prepackaged VM images that comes with machine learning frameworks and essential tools. For more information about these images, see [Choose an image](https://docs.cloud.google.com/deep-learning-vm/docs/images) in the Deep Learning VM Images documentation.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).



###  Console 

To create an instance template for GPU VMs, do the following:

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select one of the following options:

     * To create a global instance template, select **Global** (default).

     * To create a regional instance template, select **Regional** , and then select the region where you want to create the instance template.

  5. In the **Machine configuration** section, do the following:

     1. Click the **GPUs** tab.

     2. In the **GPU type** menu, select the GPU type.

     3. In the **Number of GPUs** menu, select the number of GPUs.

     4. Optional: If your GPU model supports [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), and you plan to run graphics-intensive workloads, select **Enable Virtual Workstation (NVIDIA GRID)**.

     5. In the **Machine type** section, select a machine type.

  6. Optional: To change the default value boot disk type or image, in the **Boot disk** section, click **Change**. Then, follow the prompts to change the boot disk.

  7. Click **Create**.




###  gcloud 

To create an instance template for GPU VMs, use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--maintenance-policy` flag set to `TERMINATE`.

For example, to create a global instance template for GPU VMs, use the following command:
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE_FAMILY` or `IMAGE`: specify one of the following:

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `debian-13`, the latest version in the Debian 13 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

    * `IMAGE`: a specific version of the OS image; for example, `debian-13-trixie-v20260902`. If you choose to specify a specific version of the OS image, then you must replace the `--image-family` flag with the `--image` flag.

  * `MACHINE_TYPE`: the machine type of the VMs. If you specify an N1 machine type, then include the [`--accelerator` flag](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-templates/create#--accelerator) to specify the number and type of GPUs to attach to your VMs.




For example, assume that you want to create a global instance template for GPU VMs that specifies the following properties:

  * An N1 predefined machine type with 2 vCPUs.

  * One NVIDIA T4 GPU to attach to the VMs.

  * Debian as the image project.

  * Debian 13 as the image family.




To create the example instance template, use the following command:
    
    
    gcloud compute instance-templates create instance-template-gpu \
        --accelerator=count=1,type=nvidia-tesla-t4 \
        --machine-type=n1-standard-2 \
        --image-family=debian-13 \
        --image-project=debian-cloud \
        --maintenance-policy=TERMINATE
    

###  Terraform 

To create an instance template, use one of the following resources:

  * For a regional instance template, use the [`google_compute_region_instance_template` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_template).
  * For a global instance template, use the [`google_compute_instance_template` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template).



The following example creates a global instance template that specifies an N1 predefined machine type with 2 vCPUs and one NVIDIA T4 GPU attached:
    
    
    resource "google_compute_instance_template" "default" {
      name         = "gpu-template"
      machine_type = "n1-standard-2"
    
      disk {
        source_image = "debian-cloud/debian-13"
      }
    
      network_interface {
        network = "default"
      }
    
      guest_accelerator {
        type  = "nvidia-tesla-t4"
        count = 1
      }
    
      scheduling {
        on_host_maintenance = "TERMINATE"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create an instance template for GPU VMs, make a `POST` request to the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/latest/instanceTemplates/insert). In the request body, include the `onHostMaintenance` field and set it to `TERMINATE`.

For example, to create a global instance template for GPU VMs, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "accessConfigs": [
              {
                "name": "external-IP",
                "type": "ONE_TO_ONE_NAT"
              }
            ],
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "onHostMaintenance": "TERMINATE"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which you want to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE` or `IMAGE_FAMILY`: specify one of the following:

    * `IMAGE`: a specific version of the OS image; for example, `debian-13-trixie-v20260902`.

    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-13`, the latest version in the Debian 13 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type of the VMs. If you specify an N1 machine type, then include the [`guestAccelerators` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert#request-body) to specify the number and type of GPUs to attach to your VMs.




For example, assume that you want to create a global instance template for GPU VMs that specifies the following properties:

  * An N1 predefined machine type with 2 vCPUs.

  * One NVIDIA T4 GPU to attach to the VMs.

  * Debian as the image project.

  * Debian 13 as the image family.




To create the example instance template, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates
    
    {
      "name": "instance-template-gpu",
      "properties": {
        "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/family/debian-13"
            }
          }
        ],
        "guestAccelerators": [
          {
            "acceleratorType": "nvidia-tesla-t4",
            "acceleratorCount": 1
          }
        ],
        "machineType": "n1-standard-2",
        "networkInterfaces": [
          {
            "accessConfigs": [
              {
                "name": "external-IP",
                "type": "ONE_TO_ONE_NAT"
              }
            ],
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "onHostMaintenance": "TERMINATE"
        }
      }
    }
    

For more configuration options when creating an instance template, see Create an instance template in this document.

## Create an instance template with a container image

**Caution:** The container startup agent (konlet) that deploys containers on VMs during VM creation is deprecated. Use the `docker run` commands in a startup script or use the `cloud-init` tool to configure and to run containers on your VMs and MIGs. For more information, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers). 

You can specify a container image in an instance template. By default, Compute Engine also includes in the template a [Container-Optimized OS image](https://docs.cloud.google.com/container-optimized-os/docs) with Docker installed. When you use the template to create a new instance, the container is launched automatically as the instance starts up.

###  Console 

**Note:** The **Deploy container** option in the Google Cloud console is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

  1. Go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. In the **Container** section, click **Deploy Container**.

  4. In the **Configure container** dialog, specify the **Container image** to use.

     * You can specify an image from [Container Registry](https://docs.cloud.google.com/container-registry/docs/overview#versions_of_images_within_a_registry) or [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/names). For example: 
       * `gcr.io/cloud-marketplace/google/nginx1:TAG`, where TAG is the tag defined for a specific version of NGINX container image available on Google Cloud Marketplace.
       * `us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0` selects a sample `hello-app` image stored in Artifact Registry.
     * If you use a container image from Docker Hub, always specify the full Docker image name. For example, specify the following image name to deploy an Apache container image: `docker.io/httpd:2.4`.
  5. Optionally, click **Advanced container options**. For more information, see [Configuring options to run your Container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).

  6. Click **Create**.




###  gcloud 

**Note:** The `create-with-container` gcloud CLI command is deprecated. Use the equivalent `docker run` command to configure and to run the container. 

Use the [`gcloud compute instance-templates create-with-container` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create-with-container):
    
    
     gcloud compute instance-templates create-with-container INSTANCE_TEMPLATE_NAME \
         --container-image=CONTAINER_IMAGE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: The name of the template to create.
  * `CONTAINER_IMAGE`: The full name of the container image to use.



For example, the following command creates a new instance template named `nginx-vm`. A VM instance created from this template launches and runs the container image, `gcr.io/cloud-marketplace/google/nginx1:TAG`, when the VM starts.
    
    
     gcloud compute instance-templates create-with-container nginx-vm \
         --container-image=gcr.io/cloud-marketplace/google/nginx1:TAG
    

Replace `TAG` with the tag defined for a specific version of NGINX container image available on Google Cloud Marketplace.

You can also configure [options to run your container](https://docs.cloud.google.com/compute/docs/containers/configuring-options-to-run-containers).

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

## Create an instance template that specifies a subnet

###  gcloud 

To create a regional or global instance template, use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create). Use the `--subnet` flag to place instances that are created from the template into the subnet of your choice. The `--subnet` flag requires the `--region` flag.

If you want to create a regional instance template, you must use the `--instance-template-region` flag to set the region of the template. Make sure that you use a subnet from the same region as where you want to create the regional instance template.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --region=REGION \
        --subnet=SUBNET_NAME_OR_URL \
        --stack-type=STACK_TYPE \
        --instance-template-region=INSTANCE_TEMPLATE_REGION
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name for the instance template
  * `REGION`: the region of the subnet
  * `SUBNET_NAME_OR_URL`: either the name of the subnet or its URL

**Note:** If you use the subnet name, Google finds that subnet in the target region (provided that it exists there). However, if you use the subnet URL, the instance template can only be used to create instances in the specific region that is associated with the subnet URL.
  * `STACK_TYPE`: Optional: whether IPv6 is enabled on the default network interface. The following values can be used: `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY`. If you don't include this flag, the default value is `IPV4_ONLY`.

  * `INSTANCE_TEMPLATE_REGION`: the region where you want to create the instance template. This region must be same as `REGION`.




The following example creates a template called `template-qa` that only creates instances in the `subnet-us-qa` subnet.
    
    
    gcloud compute instance-templates create template-qa \
        --region=us-central1 \
        --subnet=subnet-us-qa
    

The output is similar to the following:
    
    
    Created [https://compute.googleapis.com/compute/latest/projects/PROJECT_ID/global/instanceTemplates/template-qa].
    NAME        MACHINE_TYPE        PREEMPTIBLE CREATION_TIMESTAMP
    template-qa e2-standard-2       2019-12-23T20:34:00.791-07:00
    
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createTemplateWithSubnet creates an instance template that uses a provided subnet.
    func createTemplateWithSubnet(w io.Writer, projectID, network, subnetwork, templateName string) error {
    	// projectID := "your_project_id"
    	// network := "projects/project/global/networks/network"
    	// subnetwork := "projects/project/regions/region/subnetworks/subnetwork"
    	// templateName := "your_template_name"
    
    	ctx := context.Background()
    	instanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer instanceTemplatesClient.Close()
    
    	req := &computepb.InsertInstanceTemplateRequest{
    		Project: projectID,
    		InstanceTemplateResource: &computepb.InstanceTemplate{
    			Name: proto.String(templateName),
    			Properties: &computepb.InstanceProperties{
    				// The template describes the size and source image of the boot disk
    				// to attach to the instance.
    				Disks: []*computepb.AttachedDisk{
    					{
    						InitializeParams: &computepb.AttachedDiskInitializeParams{
    							DiskSizeGb:  proto.Int64(250),
    							SourceImage: proto.String("projects/debian-cloud/global/images/family/debian-12"),
    						},
    						AutoDelete: proto.Bool(true),
    						Boot:       proto.Bool(true),
    					},
    				},
    				MachineType: proto.String("e2-standard-4"),
    				// The template connects the instance to the specified network and subnetwork.
    				NetworkInterfaces: []*computepb.NetworkInterface{
    					{
    						Network:    proto.String(network),
    						Subnetwork: proto.String(subnetwork),
    					},
    				},
    			},
    		},
    	}
    
    	op, err := instanceTemplatesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance template: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance template created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateTemplateWithSubnet {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /*
        TODO(developer): Replace these variables before running the sample.
        projectId: project ID or project number of the Cloud project you use.
        network: the network to be used in the new template. This value uses
            the following format: "projects/{project}/global/networks/{network}"
        subnetwork: the subnetwork to be used in the new template. This value
            uses the following format: "projects/{project}/regions/{region}/subnetworks/{subnetwork}"
        templateName: name of the new template to create.
        */
        String projectId = "your-project-id";
        String network = String.format("projects/%s/global/networks/%s", projectId, "network");
        String subnetwork = String.format("projects/%s/regions/%s/subnetworks/%s", projectId, "region",
            "subnetwork");
        String templateName = "template-name";
        createTemplateWithSubnet(projectId, network, subnetwork, templateName);
      }
    
      // Create an instance template that uses a provided subnet.
      public static void createTemplateWithSubnet(String projectId, String network, String subnetwork,
          String templateName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create();
            [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html) globalOperationsClient = [GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setSourceImage(
                      String.format("projects/%s/global/images/family/%s", "debian-cloud", "debian-13"))
                  .setDiskSizeGb(250).build())
              .setAutoDelete(true)
              .setBoot(true)
              .build();
    
          [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html) instanceProperties = [InstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceProperties.html).newBuilder()
              .addDisks(disk)
              .setMachineType("e2-standard-4")
              .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                  .setNetwork(network)
                  .setSubnetwork(subnetwork).build())
              .build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html).newBuilder()
              .setName(templateName)
              .setProperties(instanceProperties)
              .build();
    
          [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html) insertInstanceTemplateRequest = [InsertInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplateResource(instanceTemplate)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instanceTemplatesClient.insertCallable()
              .futureCall(insertInstanceTemplateRequest).get(3, TimeUnit.MINUTES);
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = globalOperationsClient.wait(projectId, operation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getName__)());
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Template creation from subnet failed ! ! " + response);
            return;
          }
          System.out.printf("Template creation from subnet operation status %s: %s", templateName,
              response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const network = 'projects/project/global/networks/network';
    // const subnetwork = 'projects/project/regions/region/subnetworks/subnetwork';
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Create an instance template that uses a provided subnet.
    async function createTemplateWithSubnet() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instanceTemplatesClient.insert({
        project: projectId,
        instanceTemplateResource: {
          name: templateName,
          properties: {
            // The template describes the size and source image of the boot disk
            // to attach to the instance.
            disks: [
              {
                // The template describes the size and source image of the boot disk
                // to attach to the instance.
                initializeParams: {
                  diskSizeGb: '250',
                  sourceImage:
                    'projects/debian-cloud/global/images/family/debian-11',
                },
                autoDelete: true,
                boot: true,
              },
            ],
            machineType: 'e2-standard-4',
            // The template connects the instance to the specified network and subnetwork.
            networkInterfaces: [
              {
                network,
                subnetwork,
              },
            ],
          },
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
        });
      }
    
      console.log('Instance template created.');
    }
    
    createTemplateWithSubnet();

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
    
    
    def create_template_with_subnet(
        project_id: str, network: str, subnetwork: str, template_name: str
    ) -> compute_v1.InstanceTemplate:
        """
        Create an instance template that uses a provided subnet.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            network: the network to be used in the new template. This value uses
                the following format: "projects/{project}/global/networks/{network}"
            subnetwork: the subnetwork to be used in the new template. This value
                uses the following format: "projects/{project}/regions/{region}/subnetworks/{subnetwork}"
            template_name: name of the new template to create.
    
        Returns:
            InstanceTemplate object that represents the new instance template.
        """
        # The template describes the size and source image of the book disk to
        # attach to the instance.
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDisk.html)()
        initialize_params = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AttachedDiskInitializeParams](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AttachedDiskInitializeParams.html)()
        initialize_params.source_image = (
            "projects/debian-cloud/global/images/family/debian-13"
        )
        initialize_params.disk_size_gb = 250
        disk.initialize_params = initialize_params
        disk.auto_delete = True
        disk.boot = True
    
        template = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplate](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceTemplate.html)()
        template.name = template_name
        template.properties = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceProperties](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstanceProperties.html)()
        template.properties.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html) = [disk]
        template.properties.machine_type = "e2-standard-4"
    
        # The template connects the instance to the specified network and subnetwork.
        network_interface = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[NetworkInterface](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.NetworkInterface.html)()
        network_interface.network = network
        network_interface.subnetwork = subnetwork
        template.properties.network_interfaces = [network_interface]
    
        template_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstanceTemplatesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html)()
        operation = template_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_insert)(
            project=project_id, instance_template_resource=template
        )
        wait_for_extended_operation(operation, "instance template creation")
    
        return template_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instance_templates.InstanceTemplatesClient.html#google_cloud_compute_v1_services_instance_templates_InstanceTemplatesClient_get)(project=project_id, instance_template=template_name)
    
    

Using this template to create instances for a [MIG](https://docs.cloud.google.com/compute/docs/instance-groups) (with or without [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler)) automatically creates the instance in the specified region and subnet. This lets you control the subnet of new instances created for load balancing.

## Use custom or public images in your instance templates

You can either use a custom image or a public image for your instance templates:

  * **Custom images.** As MIGs are designed to add and remove instances frequently, it is useful to [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) and specify it in the instance template. You can prepare your image with the applications and settings that your VMs need, so you don't have to manually configure those items on individual VMs in the MIG.

  * **Public images.** You can create an instance template that uses a [public image](https://docs.cloud.google.com/compute/docs/images) and a [startup script](https://docs.cloud.google.com/compute/docs/startupscript) to prepare the instance after it starts running.




Custom images are more [deterministic](https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates) and start more quickly than VMs with startup scripts. However, startup scripts are more flexible, which helps you update the apps and settings in your instances.

If you're managing images using [image families](https://docs.cloud.google.com/compute/docs/images#image_families), you can specify the name of your custom or public image family in the instance template. For more information on image families, see [best practices when using image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#how-to-use) on Compute Engine.

**Note:** If the image you want to use belongs to a different project, you can still use that image in your instance template, provided that the owner of that project grants the MIG access to the images. For more information, see [Granting a MIG access to images](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects#granting_a_managed_instance_group_access_to_images).

## What's next

  * [View an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to see its ID and instance properties.
  * Create a [VM from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).
  * Create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
  * Update the [VMs in an existing MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) to use the properties from a different instance template.
  * Create a [reservation for VMs](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).
  * Learn how to use [managed workload identities](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls) with MIGs to communicate with Google Cloud services and enable mTLS communication between instances. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
