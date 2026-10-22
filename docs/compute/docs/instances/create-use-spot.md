---
url: https://docs.cloud.google.com/compute/docs/instances/create-use-spot/
title: Create and use Spot VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:32.972217+00:00
---

# Create and use Spot VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-use-spot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create and use Spot VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create and manage [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), including the following:

  * How to create, start, and identify Spot VMs
  * How to detect, handle, and test preemption of Spot VMs
  * Best practices for Spot VMs



Spot VMs are virtual machine (VM) instances that use the [spot provisioning model](https://docs.cloud.google.com/compute/docs/instances/spot#provisioning-model). Spot VMs are available at a discount of up to 91% off of the on-demand price of standard VMs. For more information, see the [pricing page](https://cloud.google.com/spot-vms/pricing). However, Compute Engine might reclaim the resources by preempting Spot VMs at any time. Spot VMs are recommended only for fault-tolerant workloads that can withstand VM preemption.

**Caution:** Spot VMs are not covered by any Service Level Agreement and are excluded from the [Compute Engine SLA](https://cloud.google.com/compute/sla). For more information, see [limitations of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#limitations).

## Before you begin

  * Read about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), especially the [limitations](https://docs.cloud.google.com/compute/docs/instances/spot#limitations). 
  * Verify that you have sufficient quota for the resources that you want to request. For more information, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage). 
    * To prevent Spot VMs from consuming your quotas for standard VMs' CPUs, GPUs, and disks, consider requesting [preemptible quota](https://docs.cloud.google.com/compute/docs/instances/spot#quotas) for Spot VMs. 
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create a Spot VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a Spot VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Spot VM:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare to create Spot VMs

Before you create Spot VMs for a workload, complete the following steps:

  1. **Configure your workload to manage preemption.** Specifically, we recommend that you either prepare a script to handle preemption that runs as part of your workload or is a file that you can add in VM metadata to run during shutdown. For instructions, see [Manage preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#manage-preemption).

  2. **We strongly recommend that you view data for Spot VMs to help you choose a machine type and location.** By selecting a machine type and location with a higher availability of resources, you can help improve your chances of avoiding resource availability errors and of having a longer uptime before preemption.

     * For historical preemption and pricing data, which is especially helpful when planning long-term workloads, see [View the preemption rate and pricing data for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

     * For current availability data, which is especially helpful immediately before you create Spot VMs for short-term workloads, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

  3. **Select a method for creating Spot VMs.** We recommend that you select a method as follows:

     * If you haven't created Spot VMs before or have a small, short-term workload, then see [Create a Spot VM](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#create).

     * If you have created Spot VMs before and want to create multiple Spot VMs, such as for a large, long-term workload, then see [Create a managed instance group (MIG) that uses Spot VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-spot-vms).

     * If you want to create and manage Spot VMs with TPUs, then see [Request TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot-compute).

**Tip:** A Spot VM is any VM that is configured to use the spot provisioning model. For example, you can adapt any method of creating VMs to use the spot provisioning model as follows: 
     * In the Google Cloud console, select **Spot** in the **VM provisioning model** list.
     * In the gcloud CLI, include the `--provisioning-model=SPOT` flag.
     * In REST for the Compute Engine API, include the `"provisioningModel": "SPOT"` field.

For more information about recommendations for creating Spot VMs, see the [best practices](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#best-practices).




## Create a Spot VM

After you prepare to create Spot VMs, you can create a Spot VM by using one of the following methods.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In **Machine configuration** pane, which is open by default, complete the following steps:

     1. In the **Provisioning model** section, select **Spot** from the **VM provisioning model** list. The **VM provisioning model advanced settings** section expands.
     2. In the **Preemption notice duration** list, select an option based on how you want to handle preemption.

        * If you select **120 seconds** , ensure that you handle preemption within your workload before you create a Spot VM. For example, verify that your workload includes a script to save your progress that waits to run until preemption is detected.

        * If you select **0 seconds (default)** , ensure that you handle preemption using a shutdown script. Before creating a Spot VM, create a file that contains a shutdown script that saves your progress when shutdown is caused by preemption. Attach this shutdown script as explained in a later step.

     3. Optional: To choose the [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) that happens when Compute Engine preempts the VM, in the **On VM termination** list, select one of the following options:

        * To stop the VM during preemption, select **Stop** (default).
        * To delete the VM during preemption, select **Delete**.
  3. To add a shutdown script, complete the following steps. If you selected **0 seconds (default)** for the **Preemption notice duration** , then this step is required to handle preemption. Otherwise, if you selected **120 seconds** , then this step is optional.

     1. In the navigation menu, click **Advanced**.
     2. In the **Metadata** section, click add **Add item**.
     3. In the **Key** field, enter `shutdown-script` for the metadata key.
     4. In the **Value** field, add the contents of a shutdown script that handles preemption. For an example shutdown script, see Example of handling preemption in this document.
  4. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview).

  5. To create and start the VM, click **Create**.




###  gcloud 

To create a VM using the gcloud CLI, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). Whenever you create a VM, we recommend that you specify a machine type, location, and OS image.

To create a Spot VM, include the `--provisioning-model=SPOT` flag. To specify the preemption notice duration, include the `--preemption-notice-duration` flag and, if needed, a shutdown script. Optionally, you can specify a termination action for Spot VMs by also including the `--instance-termination-action` flag.
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --zone=ZONE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --preemption-notice-duration=PREEMPTION_NOTICE_DURATION \
        --metadata shutdown-script=SHUTDOWN_SCRIPT
    

Replace the following:

  * `VM_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.

  * `MACHINE_TYPE`: the [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the new VM.

  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) to create the VM in. The zone must also support the machine type to use for the new VM.

  * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `debian-13`, the latest version in the Debian 13 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

**Note:** If you want to use a specific version of the OS image, such as `debian-13-trixie-v20260902`, then replace the `--image-family` flag with the `--image` flag.
  * `IMAGE_PROJECT`: the [project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) containing the image. For example, if you specify `debian-13` as the image family, specify `debian-cloud` as the image project.

  * `TERMINATION_ACTION`: Optional: specify which [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) to take when Compute Engine preempts the VM, either `STOP` (default behavior) or `DELETE`.

  * `PREEMPTION_NOTICE_DURATION`: whether to enable a [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration). For gcloud CLI, the value must be either `120s` or `0s`.

    * If you specify `120s`, handle preemption within your workload. (Optionally, you can also specify a shutdown script.)

    * If you specify `0s` (default), handle preemption within a shutdown script.

  * `SHUTDOWN_SCRIPT`: a shutdown script.

    * If you set `PREEMPTION_NOTICE_DURATION` to `0s` (default), then, to handle preemption, you must specify a shutdown script. For more information about how to format and specify a shutdown script, see [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).

    * Otherwise, if you don't want to specify a shutdown script, then you can remove the `--metadata shutdown-script` flag.




###  Terraform 

**Important:** The following sample doesn't use a preemption notice duration. If you need a 120-second preemption notice duration, see [`preemption_notice_duration` block](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration) in the Terraform documentation.

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to create a Spot VM using the `scheduling` block as shown in the following example.

To add a shutdown script for handling preemption, also add a `metadata` block as shown in [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript). For an example shutdown script, see Handle preemption in this document.
    
    
    resource "google_compute_instance" "spot_vm_instance" {
      name         = "spot-instance-name"
      machine_type = "f1-micro"
      zone         = "us-central1-c"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
    
      scheduling {
        preemptible                 = true
        automatic_restart           = false
        provisioning_model          = "SPOT"
        instance_termination_action = "STOP"
      }
    
      network_interface {
        # A default network is created for all GCP projects
        network = "default"
        access_config {
        }
      }
    }
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a VM using the Compute Engine API, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Whenever you create a VM, we recommend that you specify a machine type, location, and OS image.

To create a Spot VM, you must include the `"provisioningModel": "SPOT"` field. To specify the preemption notice duration, include the `preemptionNoticeDuration` field. Optionally, you can also specify a termination action for Spot VMs by including the `instanceTerminationAction` field.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
     "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
     "name": "VM_NAME",
     "disks": [
       {
         "initializeParams": {
           "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
         },
         "boot": true
       }
     ],
     "scheduling":
     {
         "provisioningModel": "SPOT",
         "instanceTerminationAction": "TERMINATION_ACTION",
         "preemptionNoticeDuration": { "seconds": PREEMPTION_NOTICE_DURATION }
     },
    "metadata": {
        "items": [
          {
            "key": "shutdown-script",
            "value": "SHUTDOWN_SCRIPT"
          }
        ]
      }
    }

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers) of the project to create the VM in.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) to create the VM in. The zone must also support the machine type to use for the new VM.
  * `MACHINE_TYPE`: the [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type) machine type for the new VM.
  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM.
  * `IMAGE_PROJECT`: the [project](https://docs.cloud.google.com/compute/docs/images#os-compute-support) containing the image. For example, if you specify `family/debian-13` as the image family, specify `debian-cloud` as the image project.
  * `IMAGE`: specify one of the following:

    * A specific version of a public image. For example, a specific image is `"sourceImage": "projects/debian-cloud/global/images/debian-13-trixie-v20260908"` where `debian-cloud` is the `IMAGE_PROJECT`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-13"` where `debian-cloud` is the `IMAGE_PROJECT`, Compute Engine creates a VM from the latest version of the OS image in the Debian 13 image family.
  * `TERMINATION_ACTION`: Optional: specify which [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) to take when Compute Engine preempts the VM, either `STOP` (default behavior) or `DELETE`.

  * `PREEMPTION_NOTICE_DURATION`: whether to enable a [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration). For REST, the value must be either `120` or `0`.

    * If you specify `120`, handle preemption within your workload. (Optionally, you can also specify a shutdown script.)

    * If you specify `0` (default), handle preemption within a shutdown script.

  * `SHUTDOWN_SCRIPT`: a shutdown script.

    * If you set `PREEMPTION_NOTICE_DURATION` to `0` (default), then, to handle preemption, you must specify a shutdown script. For more information about how to format and specify a shutdown script, see [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript). For an example shutdown script, see Example of handling preemption in this document.

    * Otherwise, if you don't want to specify a shutdown script, then you can remove the `metadata` field and subfields.




For more information about the options you can specify when creating a VM, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview).

## Start Spot VMs

Like other VMs, Spot VMs start upon creation. Likewise, if Spot VMs are stopped, you can [restart the VMs](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart_a_stopped_vm_that_doesnt_have_an_encrypted_disk) to resume the `RUNNING` state. You can stop and restart preempted Spot VMs as many times as you would like, as long as there is capacity. For more information, see [VM instance life cycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

If Compute Engine stops one or more Spot VMs in an autoscaling managed instance group (MIG) or Google Kubernetes Engine (GKE) cluster, the group restarts the VMs when the resources become available again.

## Identify a VM's provisioning model and termination action

Identify a VM's [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) to see if it is a standard VM, Spot VM, or [preemptible VM](https://docs.cloud.google.com/compute/docs/instances/preemptible). For a Spot VM, you can also identify the [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action). You can identify a VM's provisioning model and termination action using the Google Cloud console, gcloud CLI, or the Compute Engine API.

###  Console 

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the VM you want to identify. The **VM instance details** page opens.

  3. Go to the **Management** section at the bottom of the page. In the **Availability policies** subsection, check the following options:

     * If the **VM provisioning model** is set to **Spot** , the VM is a Spot VM. 
       * **On VM termination** indicates which action to take when Compute Engine preempts the VM, either **Stop** or **Delete** the VM.
     * Otherwise, if the **VM provisioning model** is set to **Standard** or **—** : 
       * If the **Preemptibility** option is set to **On** , the VM is a preemptible VM.
       * Otherwise, the VM is a standard VM.



###  gcloud 

To describe a VM from the gcloud CLI, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
    
    
    gcloud compute instances describe VM_NAME
    

where `VM_NAME` is the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM that you want to check.

In the output, check the `scheduling` field to identify the VM:

  * If the output includes the `provisioningModel` field set to `SPOT`, similar to the following, the VM is a Spot VM.
        
        ...
        scheduling:
        ...
        provisioningModel: SPOT
        instanceTerminationAction: TERMINATION_ACTION
        ...
        

where `TERMINATION_ACTION` indicates which action to take when Compute Engine preempts the VM, either stop (`STOP`) or delete (`DELETE`) the VM. If the `instanceTerminationAction` field is missing, the default value is `STOP`.

  * Otherwise, if the output includes the `provisioningModel` field set to `standard` or if the output omits the `provisioningModel` field:

    * If the output includes the `preemptible` field set to `true`, the VM is a preemptible VM.
    * Otherwise, the VM is a standard VM.



###  REST 

To describe a VM from the Compute Engine API, use the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers) of the project that the VM is in.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where the VM is located.
  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM that you want to check.



In the output, check the `scheduling` field to identify the VM:

  * If the output includes the `provisioningModel` field set to `SPOT`, similar to the following, the VM is a Spot VM.
        
        {
          ...
          "scheduling":
          {
             ...
             "provisioningModel": "SPOT",
             "instanceTerminationAction": "TERMINATION_ACTION"
             ...
          },
          ...
        }
        

where `TERMINATION_ACTION` indicates which action to take when Compute Engine preempts the VM, either stop (`STOP`) or delete (`DELETE`) the VM. If the `instanceTerminationAction` field is missing, the default value is `STOP`.

  * Otherwise, if the output includes the `provisioningModel` field set to `standard` or if the output omits the `provisioningModel` field:

    * If the output includes the `preemptible` field set to `true`, the VM is a preemptible VM.
    * Otherwise, the VM is a standard VM.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // isSpotVM checks if a given instance is a Spot VM or not.
    func isSpotVM(w io.Writer, projectID, zone, instanceName string) (bool, error) {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	ctx := context.Background()
    	client, err := compute.NewInstancesRESTClient(ctx)
    	if err != nil {
    		return false, fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := client.Get(ctx, req)
    	if err != nil {
    		return false, fmt.Errorf("GetInstance: %w", err)
    	}
    
    	isSpot := instance.GetScheduling().GetProvisioningModel() == computepb.Scheduling_SPOT.String()
    
    	var isSpotMessage string
    	if !isSpot {
    		isSpotMessage = " not"
    	}
    	fmt.Fprintf(w, "Instance %s is%s spot\n", instanceName, isSpotMessage)
    
    	return instance.GetScheduling().GetProvisioningModel() == computepb.Scheduling_SPOT.String(), nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.Instance;
    import com.google.cloud.compute.v1.InstancesClient;
    import com.google.cloud.compute.v1.Scheduling;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class CheckIsSpotVm {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Name of the virtual machine to check.
        String instanceName = "your-route-name";
        // Name of the zone you want to use. For example: "us-west3-b"
        String zone = "your-zone";
    
        boolean isSpotVm = isSpotVm(projectId, instanceName, zone);
        System.out.printf("Is %s spot VM instance - %s", instanceName, isSpotVm);
      }
    
      // Check if a given instance is Spot VM or not.
      public static boolean isSpotVm(String projectId, String instanceName, String zone)
              throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (InstancesClient client = InstancesClient.create()) {
          Instance instance = client.get(projectId, zone, instanceName);
    
          return instance.getScheduling().getProvisioningModel()
                  .equals(Scheduling.ProvisioningModel.SPOT.name());
        }
      }
    }

###  Python 
    
    
    from google.cloud import compute_v1
    
    
    def is_spot_vm(project_id: str, zone: str, instance_name: str) -> bool:
        """
        Check if a given instance is Spot VM or not.
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: "us-west3-b"
            instance_name: name of the virtual machine to check.
        Returns:
            The Spot VM status of the instance.
        """
        instance_client = compute_v1.InstancesClient()
        instance = instance_client.get(
            project=project_id, zone=zone, instance=instance_name
        )
        return (
            instance.scheduling.provisioning_model
            == compute_v1.Scheduling.ProvisioningModel.SPOT.name
        )
    
    

## Manage preemption of Spot VMs

To learn how to manage the preemption of Spot VMs, review the following sections:

  * Handle preemption.
  * Detect preemption of Spot VMs.
  * Test preemption settings.



### Handle preemption

When Compute Engine begins preempting a Spot VM, you can try to perform cleanup actions before the VM finishes shutting down. Handling preemption can include gracefully stopping a running process and transferring the state of your workload.

You can use the following methods to handle preemption for a Spot VM. For more information about how to choose where to handle preemption for your workload, see the definition of [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration).

  * **Handle preemption within your workload.** We recommend this method for Spot VMs with a 120-second preemption notice duration. Specifically, within your workload, configure code for handling preemption to wait to run until preemption starts as explained in Detect preemption within a VM. Then, your code for handling preemption runs during the [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration). (Optionally, these VMs can also specify a shutdown script, which runs during a shutdown period.)
  * **Handle preemption within a shutdown script.** We recommend this method for Spot VMs without a preemption notice duration, which is the default configuration. Specifically, configure your code for handling preemption within a [shutdown script](https://docs.cloud.google.com/compute/docs/shutdownscript) as shown in the following example. The shutdown script automatically runs for up to 30 seconds during the best-effort [shutdown period](https://docs.cloud.google.com/compute/docs/instances/spot#shutdown-period) for any type of shutdown. Consequently, you might want to configure the code for handling preemption to only run if the VM is being preempted as explained in Detect preemption within a VM.



#### Example of handling preemption

The following example script demonstrates how to handle preemption by uploading a checkpoint file to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets). You can either execute this script within your workload or configure it as a shutdown script. After gracefully stopping a specified program, the script performs a parallel upload of a checkpoint file to a Cloud Storage bucket. After the script finishes or times out, the operating system's normal `kill` command stops all remaining processes.
    
    
    #!/bin/bash
    
    MY_PROGRAM="PROGRAM_NAME" # For example, "apache2" or "nginx"
    MY_USER="LOCAL_USER"
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
    

This script assumes the following:

  * The VM was created with at least read or write access to Cloud Storage. For instructions about how to create a VM with the appropriate scopes, see the [authentication documentation](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using).

  * You have an existing Cloud Storage bucket and permission to write to it.




To add this script to a VM, configure the script to work with the workload on your VM and then add the script to your workload or the VM's metadata.

  1. Copy or download the example script:

     * Copy the preceding script after replacing the following:

       * `PROGRAM_NAME`: the name of the process or program that you want to shut down. For example, `apache2` or `nginx`.
       * `LOCAL_USER`: the username that you are logged into the virtual machine as.
       * `BUCKET_NAME`: the name of the Cloud Storage bucket where you want to save the program's checkpoint file. Note the bucket name does not start with `gs://` in this case.
     * [Download the example script](https://docs.cloud.google.com/static/compute/docs/instances/downloads/shutdown-script-pvm.sh) to your local workstation. Then, replace the following variables in the file:

       * `PROGRAM_NAME`: the name of the process or program that you want to shut down. For example, `apache2` or `nginx`.
       * `LOCAL_USER`: the username that you are logged into the virtual machine as.
       * `BUCKET_NAME`: the name of the Cloud Storage bucket where you want to save the program's checkpoint file. Note the bucket name does not start with `gs://` in this case.
  2. Configure preemption detection and add the script based on where you plan to handle preemption, either within your workload or within a shutdown script. For more information about how to choose where to handle preemption for your workload, see the definition of [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration).

     * **Handle preemption within your workload:** Complete the following steps.

       1. Configure the script to wait until preemption starts as explained in Detect preemption within a VM.

       2. Add the script to your workload.

     * **Handle preemption within a shutdown script:** Complete the following steps.

       1. We recommend that you configure the script to run only when shutdown is caused by preemption as explained in Detect preemption within a VM. For example, you don't need to upload a checkpoint file when your VM shuts down because your workload is finished.

       2. Add the shutdown script to a [new VM](https://docs.cloud.google.com/compute/docs/shutdownscript#use_a_local_shutdown_script) or an [existing VM](https://docs.cloud.google.com/compute/docs/shutdownscript#apply_a_shutdown_script_to_running_instances).




### Detect preemption of Spot VMs

The following sections explain the methods you can use to detect preemption of Spot VMs.

  * Detect preemption within a VM: For example, use this method to check for preemption within a shutdown script or to trigger preemption handling for Spot VMs with a 120-second preemption notice duration.
  * View preemption operations: For example, use this method when you want to determine why Spot VMs shut down.



#### Detect preemption within a VM

To detect if a VM is being preempted from inside the VM itself, check the metadata server for the `preempted` value in your VM's [default metadata](https://docs.cloud.google.com/compute/docs/metadata#default). For example, use one or more of the following methods based on where you plan to handle preemption.

  * **If you handle preemption in a shutdown script, check the current value of`preempted`.** You can run the following `curl` command from within your VM to obtain the current value for `preempted`:
        
        curl "http://metadata.google.internal/computeMetadata/v1/instance/preempted" -H "Metadata-Flavor: Google"
        TRUE
        

If this value is `TRUE`, the VM was preempted by Compute Engine, otherwise it is `FALSE`. For example, use this command within a shutdown script to perform different actions based on whether the shutdown was caused by preemption or not.

  * **If you handle preemption within your workload, wait until`preempted` is `TRUE`.** To wait until `preempted` is `TRUE`, you can append the [`?wait_for_change=true` query parameter](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#waitforchange) to the URL of the previous command. With this query parameter, the command performs a hanging HTTP GET request that only returns when the metadata has changed and the VM has been preempted.
        
        curl "http://metadata.google.internal/computeMetadata/v1/instance/preempted?wait_for_change=true" -H "Metadata-Flavor: Google"
        TRUE
        

This command is useful when you want to trigger preemption handling outside of a shutdown script. For example, use this method to trigger preemption handling for Spot VMs with a 120-second preemption notice duration.




#### View preemption operations

You can view preemption operations from Compute Engine by using the [Google Cloud console](https://console.cloud.google.com/), [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/latest/instances).

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

Use the [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) with a [filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) parameter to get a list of preemption events in your project.
    
    
    gcloud compute operations list \
        --filter="operationType=compute.instances.preempted"
    

Optionally, you can use additional filter parameters to further scope the results. For example, to see preemption events only for instances within a managed instance group, use the following command:
    
    
    gcloud compute operations list \
        --filter="operationType=compute.instances.preempted AND targetLink:instances/BASE_INSTANCE_NAME"
    

where `BASE_INSTANCE_NAME` is the base name specified as a prefix for the names of all the VMs in this managed instance group.

The output is similar to the following:
    
    
    NAME                  TYPE                         TARGET                                        HTTP_STATUS STATUS TIMESTAMP
    systemevent-yyyyyyyy  compute.instances.preempted  us-central1-f/instances/example-instance-yyy  200         DONE   2015-04-02T12:12:10.881-07:00
    

An operation type of `compute.instances.preempted` indicates that the VM instance was preempted. You can use the [`gcloud compute operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe) to get more information about a specific preemption operation.
    
    
    gcloud compute operations describe SYSTEM_EVENT \
        --zone=ZONE
    

Replace the following:

  * `SYSTEM_EVENT`: the system event from the output of the `gcloud compute operations list` command—for example, `systemevent-yyyyyyyy`.
  * `ZONE`: the zone of the system event—for example, `us-central1-f`.



The output is similar to the following:
    
    
    ...
    operationType: compute.instances.preempted
    progress: 100
    selfLink: https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/operations/systemevent-yyyyyyyy
    startTime: '2015-04-02T12:12:10.881-07:00'
    status: DONE
    statusMessage: Instance was preempted.
    ...

###  REST 

To get a list of recent system operations for a specific project and zone, use the [`zoneOperations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations
    

Replace the following:

  * `PROJECT_ID`: a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `ZONE`: a [zone](https://docs.cloud.google.com/compute/docs/regions-zones).



Optionally, to scope the response to show only preemption operations, you can add a filter to your API request:
    
    
    operationType="compute.instances.preempted"
    

Alternatively, to see preemption operations for a specific VM, add a `targetLink` parameter to the filter:
    
    
    operationType="compute.instances.preempted" AND
    targetLink="https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
    

Replace the following: \+ `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers). \+ `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones). \+ `VM_NAME`: the name of a specific VM in this zone and project.

The response contains a list of recent operations. For example, a preemption looks similar to the following:
    
    
    {
      "kind": "compute#operation",
      "id": "15041793718812375371",
      "name": "systemevent-yyyyyyyy",
      "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f",
      "operationType": "compute.instances.preempted",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/instances/example-instance",
      "targetId": "12820389800990687210",
      "status": "DONE",
      "statusMessage": "Instance was preempted.",
      ...
    }
    

### Test preemption settings

You can run simulated maintenance events on your Spot VMs to force them to preempt. Use this feature to test how your workloads detect and handle preemption. To learn how to test maintenance events on your instances, see [Simulate a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance).

## Best practices

Here are some best practices to help you get the most out of Spot VMs.

  * **View resource availability**. Before you create Spot VMs, or if you attempt to create Spot VMs but keep encountering resource availability errors, you can view the availability of a machine type in a specific region or zone. Checking the availability of resources helps increase your chances of successfully creating Spot VMs. For instructions, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

  * **View historical data**. Before you create Spot VMs, you can view the historical preemption rate and historical pricing for the machine types that you want your Spot VMs to use. This information helps you compare and choose the machine type that best fits your workload and cost needs. For instructions, see [View the preemption rate and pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

  * **Use instance templates**. Rather than creating Spot VMs one at a time, you can use [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates) to create multiple Spot VMs with the same properties. Instance templates are required for using MIGs. Alternatively, you can also create multiple Spot VMs [using the bulk instance API](https://docs.cloud.google.com/compute/docs/instances/using-bulk-api).

  * **Use MIGs to improve resource availability and automatically recreate Spot VMs**. Use [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) to make workloads on Spot VMs more flexible and resilient. For example, to prevent resource-availability errors, you can increase the flexibility of your workload by allowing the following:

    * Allow multiple locations by using [regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
    * Allow multiple machine types by using [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

Additionally, MIGs can [repair](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) preempted Spot VMs by automatically recreating them.

  * **Pick smaller machine types**. Resources for Spot VMs come out of excess and backup Google Cloud capacity. Capacity for Spot VMs is often easier to get for _smaller machine types_ , meaning machine types with less resources like vCPUs and memory. You might find more capacity for Spot VMs by selecting a smaller custom machine type, but capacity is even more likely for smaller predefined machine types. For example, compared to capacity for the `n2-standard-32` predefined machine type, capacity for the `n2-custom-24-96` custom machine type is more likely, but capacity for the `n2-standard-16` predefined machine type is even more likely.

  * **Run large clusters of Spot VMs during off peak times**. The load on Google Cloud data centers varies with location and time of day, but generally lowest on nights and weekends. As such, nights and weekends are the best times to run large clusters of Spot VMs.

  * **Design your workloads to be fault and preemption tolerant**. It's important to be prepared for the fact that there are changes in preemption patterns at different points in time. For example, if a zone suffers a partial outage, large numbers of Spot VMs could be preempted to make room for standard VMs that need to be moved as part of the recovery. In that small window of time, the preemption rate would look very different than on any other day. If your workload assumes that preemptions are always done in small groups, you might not be prepared for such an event.

  * **Retry creating Spot VMs that have been preempted**. If your Spot VMs have been preempted, try creating new Spot VMs once or twice before falling back to standard VMs. Depending on your requirements, it might be a good idea to combine standard VMs and Spot VMs in your clusters to ensure that work proceeds at an adequate pace.

  * **Save progress to mitigate preemption**. Manage shutdown and preemption notices by saving your workload's progress so that it can pick up where it left off, rather than start over from scratch. For example, save progress whenever preemption is detected as explained in Manage preemption of Spot VMs. For further resilience, also consider saving progress at regular intervals, not just when preemption is detected.




## What's next?

  * [Connect to your VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  * Learn about [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).
  * Learn about [limiting the runtime of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime).
  * Learn about [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates).
  * Learn about [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
