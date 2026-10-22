---
url: https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances/
title: Create and manage Windows Server VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:51.155877+00:00
---

# Create and manage Windows Server VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create and manage Windows Server VMs Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

Compute Engine provides [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) with Windows Server that you can use to create instances. For instructions on how to create a Windows Server instance with SQL Server preinstalled, see [Creating SQL Server instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances).

For more general information about Windows Server instances and Windows applications that you can run on Compute Engine, see [Windows on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows).

## Pricing

  * Windows Server images are premium images, and using them results in [additional charges](https://docs.cloud.google.com/compute/disks-image-pricing#windows_server_pricing).

  * Windows Server VMs are not included with the [Google Cloud Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial).




## Before you begin

  * [Enabling billing for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project). 
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




## Create a Windows Server instance

To create an instance with Windows Server, specify the image family for the specific version of Windows that you need. Compute Engine offers several versions of Windows Server, most of which are available as [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) images. Shielded VM images offer security features like UEFI-compliant firmware, Secure Boot, and vTPM-protected Measured Boot. For a list of the available image families, see [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

If you need more than two concurrent remote desktop sessions, you will need to purchase Remote Desktop Session (RDS) Client Access Licenses (CALs). For more information, see [License your RDS deployment with client access licenses (CALs)](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license).

**Note:** All Windows Server instances must be able to communicate with `kms.windows.googlecloud.com` (`35.190.247.13/32` or `2001:4860:4802:32::86/128`) to activate its license. Review configuring access to kms.windows.googlecloud.com to ensure your VPC network allows access to the activation server before you create your first Windows instance. To receive updates from Microsoft's Windows Update service, your Windows instances also need access to the internet because Google Cloud doesn't provide an internal Windows Update server.

### Work with Microsoft Active Directory

If you plan on using Microsoft Active Directory (AD) with your new instance, make sure the instance name is no longer than 15 characters, to meet the stated [maximum name length restrictions](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/naming-conventions-for-computer-domain-site-ou) of the system.

AD uses the NetBIOS names of machines, which are generated as the instance name truncated to 15 characters. As a result, you might encounter the following error when trying to sign in as a domain user: `The Security Database on the Server does not have a Computer Account for this Workstation Trust Relationship`.

### Create a Windows Server instance that uses an external IP to activate

This section describes how to create a Windows Server instance that has an external IP address. Your VPC network must be configured to allow access to `kms.windows.googlecloud.com`.

###  Console 

To create a basic Windows VM:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. For **Boot disk** , select **Change** , and do the following:

     1. On the **Public images** tab, choose a Windows Server operating system.
     2. Click **Select**.
  3. To create the VM, click **Create**.




To create a [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) Windows instance, do the following:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. For **Boot disk** , select **Change** , and do the following:

     1. On the **Public images** tab, choose a Windows Server operating system.
     2. To save your boot disk configuration, click **Select**.
  3. Optionally, to change the VM's Shielded VM settings, expand the **Advanced options** section. Then, do the following:

     1. Expand the **Security** section.
     2. If you want to turn off Secure Boot, clear the **Turn on Secure Boot** checkbox. Secure Boot helps protect your VM instances against boot-level and kernel-level malware and rootkits. For more information, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).
     3. If you want to turn off the virtual trusted platform module (vTPM), clear the **Turn on vTPM** checkbox. The vTPM enables Measured Boot, which validates the VM pre-boot and boot integrity. For more information, see [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).

**Important:** Disabling the vTPM also disables integrity monitoring, because integrity monitoring relies on data gathered by Measured Boot.
     4. If you want to turn off integrity monitoring, clear the **Turn on Integrity Monitoring** checkbox. Integrity monitoring lets you monitor the boot integrity of your Shielded VM VMs using Cloud Monitoring. For more information, see [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).

  4. To create the VM, click **Create**.




###  gcloud 

Use the [`compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) to see a list of available Windows Server images:
    
    
    gcloud compute images list --project windows-cloud --no-standard-images
    

To determine whether an image supports Shielded VM features, run the following command, and check for `UEFI_COMPATIBLE` in the output:
    
    
    gcloud compute images describe IMAGE_NAME --project windows-cloud
    

Replace `IMAGE_NAME` with the name of the image to check for support of Shielded VM features.

Use the [`compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create a new instance and specify the image family for one of the Windows Server [public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).
    
    
    gcloud compute instances create INSTANCE_NAME \
        --image-project windows-cloud \
        --image-family IMAGE_FAMILY \
        --machine-type MACHINE_TYPE \
        --boot-disk-size BOOT_DISK_SIZE \
        --boot-disk-type BOOT_DISK_TYPE
    

Replace the following:

  * `INSTANCE_NAME`: a [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
  * `IMAGE_FAMILY`: one of the [public image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) for Windows Server images.
  * `MACHINE_TYPE`: one of the available [machine types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GiB. Larger disks have [higher throughput](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).
  * `BOOT_DISK_TYPE`: the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk for your instance, for example, `hyperdisk-balanced` or `pd-ssd`.



If you chose an image that supports Shielded VM, you can optionally change the instance's Shielded VM settings using one of the following flags:

  * `--no-shielded-secure-boot`: Disable Secure Boot. Secure Boot helps protect your VM instances against boot-level and kernel-level malware and rootkits. For more information, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).
  * `--no-shielded-vtpm`: Disable the virtual trusted platform module (vTPM). The vTPM enables Measured Boot, which validates the VM pre-boot and boot integrity. For more information, see [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).

**Important:** Disabling the vTPM also disables integrity monitoring, because integrity monitoring relies on data gathered by Measured Boot.

  * `--no-shielded-integrity-monitoring`: Disable integrity monitoring. Integrity monitoring lets you monitor the boot integrity of your Shielded VM instances using Cloud Monitoring. For more information, see [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).




The following example creates a Windows 2022 Shielded VM instance with Secure Boot disabled:
    
    
    gcloud compute instances create my-instance \
        --image-family windows-2022 --image-project windows-cloud \
        --no-shielded-secure-boot
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createWndowsServerInstanceExternalIP creates a new Windows Server instance
    // that has an external IP address.
    func createWndowsServerInstanceExternalIP(
    	w io.Writer,
    	projectID, zone, instanceName, machineType, sourceImageFamily string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// machineType := "n1-standard-1"
    	// sourceImageFamily := "windows-2022"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	disk := &computepb.AttachedDisk{
    		// Describe the size and source image of the boot disk to attach to the instance.
    		InitializeParams: &computepb.AttachedDiskInitializeParams{
    			DiskSizeGb: proto.Int64(64),
    			SourceImage: proto.String(
    				fmt.Sprintf(
    					"projects/windows-cloud/global/images/family/%s",
    					sourceImageFamily,
    				),
    			),
    		},
    		AutoDelete: proto.Bool(true),
    		Boot:       proto.Bool(true),
    	}
    
    	network := &computepb.NetworkInterface{
    		// If you are using a custom VPC network it must be configured
    		// to allow access to kms.windows.googlecloud.com.
    		// https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server.
    		Name: proto.String("global/networks/default"),
    		AccessConfigs: []*computepb.AccessConfig{
    			{
    				Type: proto.String("ONE_TO_ONE_NAT"),
    				Name: proto.String("External NAT"),
    			},
    		},
    	}
    
    	inst := &computepb.Instance{
    		Name: proto.String(instanceName),
    		Disks: []*computepb.AttachedDisk{
    			disk,
    		},
    		MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/%s", zone, machineType)),
    		NetworkInterfaces: []*computepb.NetworkInterface{
    			network,
    		},
    		// If you chose an image that supports Shielded VM,
    		// you can optionally change the instance's Shielded VM settings.
    		// ShieldedInstanceConfig: &computepb.ShieldedInstanceConfig{
    		// 	EnableSecureBoot: proto.Bool(true),
    		// 	EnableVtpm: proto.Bool(true),
    		// 	EnableIntegrityMonitoring: proto.Bool(true),
    		// },
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
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
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
    
    public class CreateWindowsServerInstanceExternalIp {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId - ID or number of the project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // zone - Name of the zone you want to use, for example: us-west3-b
        String zone = "europe-central2-b";
    
        // instanceName - Name of the new machine.
        String instanceName = "instance-name";
    
        createWindowsServerInstanceExternalIp(projectId, zone, instanceName);
      }
    
      // Creates a new Windows Server instance that has an external IP address.
      public static void createWindowsServerInstanceExternalIp(String projectId, String zone,
          String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // machineType - Machine type you want to create in following format:
        //  *    "zones/{zone}/machineTypes/{type_name}". For example:
        //  *    "zones/europe-west3-c/machineTypes/f1-micro"
        //  *    You can find the list of available machine types using:
        //  *    https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
        String machineType = "n1-standard-1";
        // sourceImageFamily - Name of the public image family for Windows Server or SQL Server images.
        //  *    https://cloud.google.com/compute/docs/images#os-compute-support
        String sourceImageFamily = "windows-2022";
    
        // Instantiates a client.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              // Describe the size and source image of the boot disk to attach to the instance.
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setDiskSizeGb(64)
                  .setSourceImage(
                      String.format("projects/windows-cloud/global/images/family/%s",
                          sourceImageFamily))
                  .build())
              .setAutoDelete(true)
              .setBoot(true)
              .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.PERSISTENT.toString())
              .build();
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
              .setName(instanceName)
              .setMachineType(String.format("zones/%s/machineTypes/%s", zone, machineType))
              .addDisks(attachedDisk)
              .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                  .[addAccessConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.Builder.html#com_google_cloud_compute_v1_NetworkInterface_Builder_addAccessConfigs_com_google_cloud_compute_v1_AccessConfig_)([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).newBuilder()
                      .setType("ONE_TO_ONE_NAT")
                      .setName("External NAT")
                      .build())
                  // If you're going to use a custom VPC network, it must be configured
                  // to allow access to kms.windows.googlecloud.com.
                  // https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server.
                  .setName("global/networks/default")
                  .build())
              // If you chose an image that supports Shielded VM, you can optionally change the
              // instance's Shielded VM settings.
              // .setShieldedInstanceConfig(ShieldedInstanceConfig.newBuilder()
              //    .setEnableSecureBoot(true)
              //    .setEnableVtpm(true)
              //    .setEnableIntegrityMonitoring(true)
              //    .build())
              .build();
    
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) request = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(instance)
              .build();
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instancesClient.insertAsync(request).get(5, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.printf("Error in creating instance %s", operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
            return;
          }
    
          System.out.printf("Instance created %s", instanceName);
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
    // const machineType = 'n1-standard-1';
    // const sourceImageFamily = 'windows-2022';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createWindowsServerInstanceExpernalIP() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.insert({
        instanceResource: {
          name: instanceName,
          disks: [
            {
              // Describe the size and source image of the boot disk to attach to the instance.
              initializeParams: {
                diskSizeGb: '64',
                sourceImage: `projects/windows-cloud/global/images/family/${sourceImageFamily}/`,
              },
              autoDelete: true,
              boot: true,
              type: 'PERSISTENT',
            },
          ],
          machineType: `zones/${zone}/machineTypes/${machineType}`,
          networkInterfaces: [
            {
              accessConfigs: [
                {
                  type: 'ONE_TO_ONE_NAT',
                  name: 'External NAT',
                },
              ],
              // If you are using a custom VPC network it must be configured to allow access to kms.windows.googlecloud.com.
              // https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server.
              name: 'global/networks/default',
            },
          ],
          // If you chose an image that supports Shielded VM, you can optionally change the instance's Shielded VM settings.
          // "shieldedInstanceConfig": {
          //   "enableSecureBoot": true,
          //   "enableVtpm": true,
          //   "enableIntegrityMonitoring": true
          // },
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
    
    createWindowsServerInstanceExpernalIP();

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
    
    
    def create_windows_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        machine_type: str,
        source_image_family: str = "windows-2022",
        network_link: str = "global/networks/default",
        subnetwork_link: str | None = None,
    ) -> compute_v1.Instance:
        """
        Creates a new Windows Server instance that has only an internal IP address.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            machine_type: machine type you want to create in following format:
                "zones/{zone}/machineTypes/{type_name}". For example:
                "zones/europe-west3-c/machineTypes/f1-micro"
                You can find the list of available machine types using:
                https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
            source_image_family: name of the public image family for Windows Server or SQL Server images.
                https://cloud.google.com/compute/docs/images#os-compute-support
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
               "regions/{region}/subnetworks/{subnetwork_name}"
    
        Returns:
            Instance object.
        """
        if subnetwork_link is None:
            subnetwork_link = f"regions/{zone}/subnetworks/default"
    
        base_image = get_image_from_family(
            project="windows-cloud", family=source_image_family
        )
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_image(disk_type, 100, True, base_image.self_link, True)]
    
        # You must verify or configure routes and firewall rules in your VPC network
        # to allow access to kms.windows.googlecloud.com.
        # More information about access to kms.windows.googlecloud.com: https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server
    
        # Additionally, you must enable Private Google Access for subnets in your VPC network
        # that contain Windows instances with only internal IP addresses.
        # More information about Private Google Access: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
    
        instance = create_instance(
            project_id,
            zone,
            instance_name,
            disks,
            machine_type=machine_type,
            network_link=network_link,
            subnetwork_link=subnetwork_link,
            external_access=True,  # Set this to False to disable external IP for your instance
        )
        return instance
    
    

###  REST 

To create an instance with the API, include the [`initializeParams` property](https://docs.cloud.google.com/compute/docs/reference/latest/instances#disks.initializeParams) in your instance creation request and specify a Windows image. For example, your request body might look like the following:
    
    
    instance = {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [{
          "boot": "true",
          "type": "PERSISTENT",
          "initializeParams": {
             "diskName": "DISK_NAME",
             "sourceImage": "https://www.googleapis.com/compute/v1/projects/windows-cloud/global/images/family/IMAGE_FAMILY",
             "diskSizeGb": "BOOT_DISK_SIZE",
             "diskType": "BOOT_DISK_TYPE",
           }
        }],
      "networkInterfaces": [{
        "accessConfigs": [{
          "type": "ONE_TO_ONE_NAT",
          "name": "External NAT"
         }],
        "network": "global/networks/default"
      }],
      "serviceAccounts": [{
           "email": DEFAULT_SERVICE_EMAIL,
           "scopes": DEFAULT_SCOPES
      }]
    }

Replace the following placeholders with valid values:

  * `INSTANCE_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
  * `IMAGE_FAMILY`: one of the [public image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) for Windows Server or SQL Server images.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
  * `MACHINE_TYPE`: one of the available [machine types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GiB. Larger disks have [higher throughput](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).
  * `BOOT_DISK_TYPE`: the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk for your instance, for example, `hyperdisk-balanced` or `pd-ssd`.



If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm), you can optionally change the instance's Shielded VM settings by using the following boolean request body items:

  * `enableSecureBoot`: Enable or disable Secure Boot. Secure Boot helps protect your VM instances against boot-level and kernel-level malware and rootkits. For more information, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).
  * `enableVtpm`: Enable or disable the virtual trusted platform module (vTPM). The vTPM enables Measured Boot, which validates the VM pre-boot and boot integrity. For more information, see [Virtual Trusted Platform Module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).

**Important:** Disabling the vTPM also disables integrity monitoring, because integrity monitoring relies on data gathered by Measured Boot.

  * `enableIntegrityMonitoring`: Enable or disable integrity monitoring. Integrity monitoring lets you monitor and verify the runtime boot integrity of your Shielded VM instances using Cloud Monitoring reports. For more information, see [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).




For more information about creating an instance, read the [`instances.insert()` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/insert) documentation.

After you create your Windows or SQL Server instance, [set the initial password for the instance](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials) so that you can [connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) through RDP.

Additionally, you can join the VM to a [Managed Microsoft AD](https://docs.cloud.google.com/security/products/managed-microsoft-ad/docs/overview) domain either while creating the VM or after creating the VM. For more information, see [Join a Windows VM automatically to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce)).

### Create a Windows Server instance that uses an internal IP address to activate

Before you can create a Windows Server instance that has only an internal IP address, you must verify or configure routes and firewall rules in your VPC network to allow access to `kms.windows.googlecloud.com`. Additionally, you must [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) for subnets in your VPC network that contain Windows instances with only internal IP addresses.

###  gcloud 

When you create a new instance by using the gcloud CLI, you can use the `--no-address` flag to ensure that it is not assigned an external IP address:
    
    
    gcloud compute instances create INSTANCE_NAME --network NETWORK_NAME \
     --subnet SUBNET_NAME \
     --no-address \
     --zone ZONE \
     --image-project windows-cloud \
     --image-family IMAGE_FAMILY \
     --machine-type MACHINE_TYPE \
     --boot-disk-size BOOT_DISK_SIZE \
     --boot-disk-type BOOT_DISK_TYPE
    

Replace the following placeholders with valid values:

  * `INSTANCE_NAME`: a [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
  * `SUBNET_NAME`: the name of the subnet in the VPC network that the instance will use. The subnet must be in the same region as the zone that you choose for the instance.
  * `IMAGE_FAMILY`: one of the [public image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support) for Windows Server images.
  * `MACHINE_TYPE`: one of the available [machine types](https://docs.cloud.google.com/compute/docs/machine-resource).
  * `BOOT_DISK_SIZE`: the size of the boot disk in GiB. Larger disks have [higher throughput](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).
  * `BOOT_DISK_TYPE`: the [type](https://docs.cloud.google.com/compute/docs/disks#disk-types) of the boot disk for your instance. For example, `hyperdisk-balanced` or `pd-ssd`.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createWndowsServerInstanceInternalIP creates a new Windows Server instance
    // that has only an internal IP address.
    func createWndowsServerInstanceInternalIP(
    	w io.Writer,
    	projectID, zone, instanceName, machineType, sourceImageFamily, networkLink, subnetworkLink string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// machineType := "n1-standard-1"
    	// sourceImageFamily := "windows-2022"
    	// networkLink := "global/networks/default"
    	// subnetworkLink := "regions/europe-central2/subnetworks/default"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	disk := &computepb.AttachedDisk{
    		// Describe the size and source image of the boot disk to attach to the instance.
    		InitializeParams: &computepb.AttachedDiskInitializeParams{
    			DiskSizeGb: proto.Int64(64),
    			SourceImage: proto.String(
    				fmt.Sprintf(
    					"projects/windows-cloud/global/images/family/%s",
    					sourceImageFamily,
    				),
    			),
    		},
    		AutoDelete: proto.Bool(true),
    		Boot:       proto.Bool(true),
    	}
    
    	network := &computepb.NetworkInterface{
    		// You must verify or configure routes and firewall rules in your VPC network
    		// to allow access to kms.windows.googlecloud.com.
    		// More information about access to kms.windows.googlecloud.com:
    		// https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server
    
    		// Additionally, you must enable Private Google Access for subnets in your VPC network
    		// that contain Windows instances with only internal IP addresses.
    		// More information about Private Google Access:
    		// https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
    		Name:       proto.String(networkLink),
    		Subnetwork: proto.String(subnetworkLink),
    	}
    
    	inst := &computepb.Instance{
    		Name: proto.String(instanceName),
    		Disks: []*computepb.AttachedDisk{
    			disk,
    		},
    		MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/%s", zone, machineType)),
    		NetworkInterfaces: []*computepb.NetworkInterface{
    			network,
    		},
    		// If you chose an image that supports Shielded VM,
    		// you can optionally change the instance's Shielded VM settings.
    		// ShieldedInstanceConfig: &computepb.ShieldedInstanceConfig{
    		// 	EnableSecureBoot: proto.Bool(true),
    		// 	EnableVtpm: proto.Bool(true),
    		// 	EnableIntegrityMonitoring: proto.Bool(true),
    		// },
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
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateWindowsServerInstanceInternalIp {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId - ID or number of the project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // zone - Name of the zone you want to use, for example: us-west3-b
        String zone = "europe-central2-b";
    
        // instanceName - Name of the new machine.
        String instanceName = "instance-name";
    
        // networkLink - Name of the network you want the new instance to use.
        //  *   For example: "global/networks/default" represents the network
        //  *   named "default", which is created automatically for each project.
        String networkLink = "global/networks/default";
    
        // subnetworkLink - Name of the subnetwork you want the new instance to use.
        //  *   This value uses the following format:
        //  *   "regions/{region}/subnetworks/{subnetwork_name}"
        String subnetworkLink = "regions/europe-central2/subnetworks/default";
    
        createWindowsServerInstanceInternalIp(projectId, zone, instanceName, networkLink,
            subnetworkLink);
      }
    
      // Creates a new Windows Server instance that has only an internal IP address.
      public static void createWindowsServerInstanceInternalIp(String projectId, String zone,
          String instanceName, String networkLink, String subnetworkLink)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // machineType - Machine type you want to create in following format:
        //  *    "zones/{zone}/machineTypes/{type_name}". For example:
        //  *    "zones/europe-west3-c/machineTypes/f1-micro"
        //  *    You can find the list of available machine types using:
        //  *    https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
        String machineType = "n1-standard-1";
        // sourceImageFamily - Name of the public image family for Windows Server or SQL Server images.
        //  *    https://cloud.google.com/compute/docs/images#os-compute-support
        String sourceImageFamily = "windows-2022";
    
        // Instantiates a client.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              // Describe the size and source image of the boot disk to attach to the instance.
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)([AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                  .setDiskSizeGb(64)
                  .setSourceImage(
                      String.format("projects/windows-cloud/global/images/family/%s",
                          sourceImageFamily))
                  .build())
              .setAutoDelete(true)
              .setBoot(true)
              .setType([AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).Type.PERSISTENT.toString())
              .build();
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
              .setName(instanceName)
              .setMachineType(String.format("zones/%s/machineTypes/%s", zone, machineType))
              .addDisks(attachedDisk)
              .addNetworkInterfaces([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                  // You must verify or configure routes and firewall rules in your VPC network
                  // to allow access to kms.windows.googlecloud.com.
                  // More information about access to kms.windows.googlecloud.com: https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server
    
                  // Additionally, you must enable Private Google Access for subnets in your VPC network
                  // that contain Windows instances with only internal IP addresses.
                  // More information about Private Google Access: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
                  .setName(networkLink)
                  .setSubnetwork(subnetworkLink)
                  .build())
              // If you chose an image that supports Shielded VM, you can optionally change the
              // instance's Shielded VM settings.
              // .setShieldedInstanceConfig(ShieldedInstanceConfig.newBuilder()
              //    .setEnableSecureBoot(true)
              //    .setEnableVtpm(true)
              //    .setEnableIntegrityMonitoring(true)
              //    .build())
              .build();
    
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) request = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setInstanceResource(instance)
              .build();
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instancesClient.insertAsync(request).get(5, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.printf("Error in creating instance %s", operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
            return;
          }
    
          System.out.printf("Instance created %s", instanceName);
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
    // const machineType = 'n1-standard-1';
    // const sourceImageFamily = 'windows-2022';
    // const networkLink = 'global/networks/default';
    // const subnetworkLink = 'regions/europe-central2/subnetworks/default';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function createWindowsServerInstanceInternalIP() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.insert({
        instanceResource: {
          name: instanceName,
          disks: [
            {
              // Describe the size and source image of the boot disk to attach to the instance.
              initializeParams: {
                diskSizeGb: '64',
                sourceImage: `projects/windows-cloud/global/images/family/${sourceImageFamily}/`,
              },
              autoDelete: true,
              boot: true,
              type: 'PERSISTENT',
            },
          ],
          machineType: `zones/${zone}/machineTypes/${machineType}`,
          networkInterfaces: [
            {
              // You must verify or configure routes and firewall rules in your VPC network
              // to allow access to kms.windows.googlecloud.com.
              // More information about access to kms.windows.googlecloud.com: https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server
    
              // Additionally, you must enable Private Google Access for subnets in your VPC network
              // that contain Windows instances with only internal IP addresses.
              // More information about Private Google Access: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
              name: networkLink,
              subnetwork: subnetworkLink,
            },
          ],
          // If you chose an image that supports Shielded VM, you can optionally change the instance's Shielded VM settings.
          // "shieldedInstanceConfig": {
          //   "enableSecureBoot": true,
          //   "enableVtpm": true,
          //   "enableIntegrityMonitoring": true
          // },
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
    
    createWindowsServerInstanceInternalIP();

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
    
    
    def create_windows_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        machine_type: str,
        source_image_family: str = "windows-2022",
        network_link: str = "global/networks/default",
        subnetwork_link: str | None = None,
    ) -> compute_v1.Instance:
        """
        Creates a new Windows Server instance that has only an internal IP address.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            machine_type: machine type you want to create in following format:
                "zones/{zone}/machineTypes/{type_name}". For example:
                "zones/europe-west3-c/machineTypes/f1-micro"
                You can find the list of available machine types using:
                https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list
            source_image_family: name of the public image family for Windows Server or SQL Server images.
                https://cloud.google.com/compute/docs/images#os-compute-support
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
               "regions/{region}/subnetworks/{subnetwork_name}"
    
        Returns:
            Instance object.
        """
        if subnetwork_link is None:
            subnetwork_link = f"regions/{zone}/subnetworks/default"
    
        base_image = get_image_from_family(
            project="windows-cloud", family=source_image_family
        )
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_image(disk_type, 100, True, base_image.self_link, True)]
    
        # You must verify or configure routes and firewall rules in your VPC network
        # to allow access to kms.windows.googlecloud.com.
        # More information about access to kms.windows.googlecloud.com: https://cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server
    
        # Additionally, you must enable Private Google Access for subnets in your VPC network
        # that contain Windows instances with only internal IP addresses.
        # More information about Private Google Access: https://cloud.google.com/vpc/docs/configure-private-google-access#enabling
    
        instance = create_instance(
            project_id,
            zone,
            instance_name,
            disks,
            machine_type=machine_type,
            network_link=network_link,
            subnetwork_link=subnetwork_link,
            external_access=True,  # Set this to False to disable external IP for your instance
        )
        return instance
    
    

Because this instance does not have an external IP address, you cannot connect to it directly over the Internet. You can connect from another network connected to your VPC network by using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-vpn), or you can first connect to a bastion instance over RDP and then connect to the instance that has only an internal IP address.

Additionally, you can join the VM to a [Managed Microsoft AD](https://docs.cloud.google.com/security/products/managed-microsoft-ad/docs/overview) domain either while creating the VM or after creating the VM. For more information, see [Join a Windows VM automatically to a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce).

## Configure access to kms.windows.googlecloud.com

For Windows activation and renewal, your VPC network must meet the following routing and firewall rule requirements.

### Routing requirements

Your Windows instances must be able to reach `kms.windows.googlecloud.com` (`35.190.247.13` or `2001:4860:4802:32::86`) through a route whose next hop is the _default Internet gateway_. You cannot activate Windows instances using an instance based NAT gateway or Cloud NAT because `kms.windows.googlecloud.com` rejects activation requests from IP addresses that are not confirmed to be Compute Engine instances.

You can use the [default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) in your VPC network to route traffic directly to `kms.windows.googlecloud.com`. If you remove this route, or if you plan to do so in the future, [create a custom static route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute) with destination `35.190.247.13` or `2001:4860:4802:32::86`, and next hop set to _default Internet gateway_ , as follows:

### IPv4 only
    
    
    gcloud compute routes create mskms-ipv4-route-ipv4-network \
        --destination-range=35.190.247.13/32 \
        --network=ipv4-network \
        --next-hop-gateway=default-internet-gateway
    

### Dual stack
    
    
    gcloud compute routes create mskms-ipv4-route-ipv4-network \
        --destination-range=35.190.247.13/32 \
        --network=ipv4-network \
        --next-hop-gateway=default-internet-gateway
    
    
    
    gcloud compute routes create mskms-ipv6-route-ipv6-network \
        --destination-range=2001:4860:4802:32::86/128 \
        --network=ipv6-network \
        --next-hop-gateway=default-internet-gateway
    

### IPv6 only
    
    
    gcloud compute routes create mskms-ipv6-route-ipv6-network \
        --destination-range=2001:4860:4802:32::86/128 \
        --network=ipv6-network \
        --next-hop-gateway=default-internet-gateway
    

Replace `ipv4-network` or `ipv6-network` with the name of your VPC network.

Either the default route or a custom static route permit instances with external IP addresses to reach `kms.windows.googlecloud.com`. If you have Windows instances without external IP addresses or using Cloud NAT, you must also [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) so that instances with only internal IP addresses can send traffic to the external IP address for `kms.windows.googlecloud.com` (`35.190.247.13` or `2001:4860:4802:32::86`).

### Firewall rule requirements

The [implied allow egress](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules) firewall rule allows instances to make requests and receive established responses. Unless you have created custom firewall rules that deny egress, your Windows instances can communicate with `kms.windows.googlecloud.com`.

If you customize firewall rules, it's a good practice to create a high priority egress allow rule that explicitly permits communication with `35.190.247.13` or `2001:4860:4802:32::86`. This way, as you modify your firewall rules, you won't accidentally disable Windows activation.

The following `gcloud` examples creates the recommended allow egress rule with the highest priority:

### IPv4 only
    
    
    gcloud compute firewall-rules create mskms-ipv4-firewall-rule-ipv4-network \
        --direction=EGRESS \
        --network=ipv4-network \
        --action=ALLOW \
        --rules=tcp:1688 \
        --destination-ranges=35.190.247.13/32 \
        --priority=0
    

### Dual stack
    
    
    gcloud compute firewall-rules create mskms-ipv4-firewall-rule-ipv4-network \
        --direction=EGRESS \
        --network=ipv4-network \
        --action=ALLOW \
        --rules=tcp:1688 \
        --destination-ranges=35.190.247.13/32 \
        --priority=0
    
    
    
    gcloud compute firewall-rules create mskms-ipv6-firewall-rule-ipv6-network \
        --direction=EGRESS \
        --network=ipv6-network \
        --action=ALLOW \
        --rules=tcp:1688 \
        --destination-ranges=2001:4860:4802:32::86/128 \
        --priority=0
    

### IPv6 only
    
    
    gcloud compute firewall-rules create mskms-ipv6-firewall-rule-ipv6-network \
        --direction=EGRESS \
        --network=ipv6-network \
        --action=ALLOW \
        --rules=tcp:1688 \
        --destination-ranges=2001:4860:4802:32::86/128 \
        --priority=0
    

Replace `ipv4-network` or `ipv6-network` with the name of your VPC network.

## Verifying that an instance has successfully started

Windows instances experience a longer startup time because of the sysprep process. The Google Cloud console might show that the instance is running even if the sysprep process is not yet complete. To check if your instance has successfully started and is ready to be used, check the serial port output with the following command:
    
    
    gcloud compute instances get-serial-port-output INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of the instance that you want to verify.
    
    
    ...[snip]...
    Running schtasks with arguments /run /tn GCEStartup
    -->  SUCCESS: Attempted to run the scheduled task "GCEStartup".
    -------------------------------------------------------------
    Instance setup finished. INSTANCE_NAME is ready to use.
    -------------------------------------------------------------
    

## Enabling and disabling Windows instance features

If you have Windows instances with image versions `v20170509` and later or with agent version `4.1.0` and later, you can set instance configuration in a config file or in [project or instance custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata). The config file is in [INI](https://en.wikipedia.org/wiki/INI_file) format, and is located at the following path:
    
    
    C:\Program Files\Google\Compute Engine\instance_configs.cfg
    

The system overrides configuration settings in the following order of priority from the highest priority to the lowest priority:

  1. Configuration parameters that you set in the config file
  2. Configuration parameters set in instance-level custom metadata
  3. Configuration parameters set in project-level custom metadata



For example, if you can enable the `accountManager` feature in a config file, your instance ignores parameters that you set in custom metadata to disable that feature.

One benefit of setting these parameters in the config file is that those settings persist when you create a custom image for a Windows Server instance. Instance-level custom metadata does not persist beyond the life of the instance.

You can disable different Windows instance features using the following examples.

### Disable the account manager

Disabling the account manager also disables [resetting passwords with the Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password) or the Google Cloud console:

  * Config file:
        
        [accountManager]
        disable=true
        

  * In custom metadata, set `disable-account-manager` to `true` in metadata.




### Disable the address manager

  * Config file entry:
        
        [addressManager]
        disable=true
        

  * In custom metadata, set `disable-address-manager` to `true` in metadata.




### Windows Server Failover Clustering

Enable the Windows Server Failover Clustering agent:

  * Config file entry:
        
        [wsfc]
        enable=true
        

  * In custom metadata, set `enable-wsfc` to `true` in metadata.




#### Using multiple internal load balancers

Specify the IP address of the internal load balancing instance for failover clustering. This is an advanced configuration that you don't need to set for a dedicated failover cluster.

Normally you use an instance of internal load balancing to direct network traffic to one VM instance at a time. If you add a second instance of internal load balancing that uses the failover clustering VM instances as part of a load-balanced website backend, you would have two internal load balancing IP addresses. If failover clustering uses `10.0.0.10` and the website's load balancer uses `10.0.0.11`, you must specify the IP address of the load balancer that you use for failover clustering. This disambiguates which address is in use for the cluster.

  * Config file entry:
        
        [wsfc]
        addresses=10.0.0.10
        

  * In custom metadata, set `wsfc-addrs` to a `10.0.0.10`.




#### Changing the clustering agent port

Set the failover clustering agent port. The default port is `59998`. You need to specify a port only when you want to use a different port:

  * Config file entry:
        
        [wsfc]
        port=12345
        

  * In custom metadata, set `wsfc-agent-port` to the port number.




### Image version notes

Older images don't use a config file and only have a subset of features. Image versions between version `v20160112` and version `v20170509`, or Windows agent version between `3.2.1.0` and `4.0.0` require you to use the following custom metadata values:

  * Set `disable-account-manager` to `true` in instance metadata to disable the account manager.
  * Set `disable-address-manager` to `true` in instance metadata to disable the address manager.



## What's next

  * [Generate credentials for Windows VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials)
  * [Add a persistent disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)
  * [Connect to Windows VMs using SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh)
  * [Connect to Windows VMs using PowerShell](https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
