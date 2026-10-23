---
url: https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses/
title: Bring your own licenses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:21.072327+00:00
---

# Bring your own licenses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Bring your own licenses Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how Google Cloud supports bringing your own licenses (BYOL) that have dedicated hardware requirements to Compute Engine. Before attempting to bring images with existing licenses to Google Cloud, review your licensing terms and conditions.

Bringing your existing physical-core or physical-processor licenses that have dedicated hardware requirements requires you to bring your own media and to run that media on hardware configurations, such as [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes), that are compliant with your licenses. You can bring images with existing licenses in any [region that supports sole-tenant nodes](https://docs.cloud.google.com/compute/docs/regions-zones), and although there is no additional charge for bringing images with existing licenses, you must still pay for your licenses according to your agreements.

Licensing scenarios such as licenses related to Linux BYOS with RHEL or SLES, as well as Microsoft applications don't require sole-tenant nodes. If you are considering bringing licenses from Microsoft applications such as SharePoint Server and SQL Server, use [Microsoft License Mobility](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing).

Sole-tenant nodes are physical servers dedicated to hosting virtual machine (VM) instances for only your project. You can configure sole-tenant nodes to support various workload requirements, such as requirements for minimizing the number of physical servers and cores. Consult your licensing agreements to determine which configuration options are most suitable for your workloads.

To support bringing your own licenses, and to help you manage compliance requirements related to your licenses, Google Cloud provides tools for importing images, managing VMs on dedicated hardware by using sole-tenant nodes, minimizing physical core usage, and tracking usage of physical cores for reporting purposes.

To bring images with existing licenses to Google Cloud, you must do the following:

  1. Prepare the images according to your license agreements.

  2. Activate your licenses.

  3. Import virtual disk files and create images from those disk files.

  4. Create sole-tenant node templates.

  5. Create sole-tenant node groups.

  6. Provision VMs on the node groups with the imported virtual disk files.

  7. Track the license usage of your VMs. To help you with reporting your license consumption, Google provides tools to help you [track both license usage and physical core and processor usage](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license/determining-server-usage).

  8. Report license consumption to your vendor.




If you need support or have questions regarding licensing, contact your licensing reseller. If you need support or have questions about bringing images with existing licenses to Google Cloud, [contact Google Cloud Support](https://docs.cloud.google.com/support).

## Before you begin

  * [ Review the node group host maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy): For BYOL there are two options for host maintenance policy that minimize the number of physical servers used for licensing purposes. These options are `restart-in-place` and `migrate-within-node-group`.
  * [Request additional CPU quota](https://console.cloud.google.com/iam-admin/quotas): New projects receive a CPU quota of 72. Make sure you have enough CPU quota to support your node group. For example, the `n1-node-96-624` node type contains 96 CPUs, and if your node group uses the minimum number of nodes (2), your CPU quota must be at least 192\. Depending on your setup and the needs of your workloads, you might also need to request a quota adjustment for VMs or IP addresses.
  * [ Enable the Cloud Build API](https://console.cloud.google.com/apis/api/cloudbuild.googleapis.com/overview): To import your OS image you must enable the Cloud Build API. When you enable this API, Compute Engine grants your project the appropriate [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) so that you can import images into your project. To list the roles granted to your project, use the [`gcloud projects get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy). For information about how to grant roles to your project, see [Managing access to Compute Engine resources](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources).
  * [ Enable the Cloud Logging API](https://console.cloud.google.com/apis/api/logging.googleapis.com/overview): Enable this API if your licensing agreements require you to track physical server usage. With this API enabled, you can import and view server usage information, such as physical core count, by using [BigQuery](https://docs.cloud.google.com/bigquery/docs), which Google strongly recommends. For information about how to determine the count of physical cores, see [Analyzing sole-tenant node usage](https://docs.cloud.google.com/compute/docs/nodes/determining-server-usage).
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




## Import and create an image from an offline virtual disk

To provision VMs with your existing licenses, you must bring your own media. Images based on a premium image are not eligible for BYOL because premium images require pay-as-you-go licenses from Google. For information about premium images, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

If you have virtual disks (_golden disks_ or _golden images_) in your on-premises environment with software configurations or licenses that you need, the [import virtual disk tool](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) can help you do the following:

  1. Import your customized virtual disks with a [supported operating system](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import#--os) and create images based on those disks.

**Note:** If you are importing Windows Server 2008 R2 SP1 or Windows 7 SP1 x64, the [image must support SHA2 signing](https://support.microsoft.com/en-us/help/4474419/sha-2-code-signing-support-update) because Compute Engine drivers are signed with SHA2.
  2. Set up the appropriate license configuration.

  3. Install the packages and drivers necessary for compatibility with Google Cloud.




Before you import the virtual disk file for your VM, verify that there are no [incompatibilities](https://googlecloudplatform.github.io/compute-image-import/image-import.html#compatibility-and-known-limitations) in the file by [downloading and running the precheck tool](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks#precheck) from inside your VM. Also, because software from third parties might interfere with the installation of Compute Engine drivers, Google recommends removing third-party software before importing your image.

To start a VM with your own license, import a virtual disk with the OS you want to use. You can import virtual disks from [Cloud Storage](https://docs.cloud.google.com/storage/docs) buckets and local workstations. When importing a virtual disk file from a local workstation, the image import tool uploads your image file to Cloud Storage, and, if necessary, creates a new Cloud Storage bucket. Then, the import tool copies the file to Compute Engine and creates a bootable image from the virtual disk file.

Files stored on Cloud Storage and images in Compute Engine incur charges. After verifying that the image imports and boots correctly as a VM, you can delete the virtual disk file from Cloud Storage.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `roles/compute.admin` on the Cloud Build service account
  * `roles/iam.serviceAccountUser` on the Cloud Build service account



###  Console 

  1. Go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Create image**.

  3. Specify a name for the image.

  4. Under **Source** , choose **Virtual disk (VMDK, VHD)**.

  5. Under **Cloud Storage file** , choose **Browse** and browse to the Cloud Storage location of the image to import.

  6. Under **Operating system on virtual disk** , choose the operating system of the image that you are importing.

  7. Make sure that **Install guest packages** is selected, so that the image you are importing is bootable.

  8. Expand **License key options**. Under **OS License** , choose **Use your own license key**.

  9. Click **Create** to import the image.




###  gcloud 

Run [`gcloud compute images import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import) to import a virtual disk file and to create a disk image from the virtual disk file:
    
    
    gcloud compute images import IMAGE_NAME \
        --source-file VMDK_NAME \
        --byol
    

Replace the following:

  * `IMAGE_NAME`: name to give the image created from the virtual disk file.
  * `VMDK_NAME`: name of the virtual disk to import and create an image from. You can import a VMDK file from the following:

    * **A local file** : If importing from a local file, use an absolute path or a relative path to the file. Depending on the size of the virtual disk and the speed of the network connection, the upload might take tens of minutes.
    * **Cloud Storage** : If importing from [Cloud Storage](https://docs.cloud.google.com/storage/docs), the Cloud Storage bucket must be in the same project that you are using to import the virtual disk, and you must specify the full path to the file as `gs://BUCKET_NAME/OBJECT_NAME`. Replace `BUCKET_NAME` with the name of the Cloud Storage bucket and `OBJECT_NAME` with the name of the Cloud Storage object.



## Activate licenses

After verifying that you are importing a [compatible OS](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import#--os), you are responsible for checking that your licensing agreements permit you to bring your own licenses and that you are permitted to use the guest OS image and license import environment provided by Google. You are also responsible for preparing your guest OS image for import according to your licensing agreements.

To activate a license, use [startup scripts](https://docs.cloud.google.com/compute/docs/startupscript) with your Multiple Activation Key (MAK), or configure access to your organization's Microsoft Key Management Service. You can't activate images with existing licenses against the Compute Engine license server.

After importing your image and activating the license, provision a VM based on the imported image onto a sole-tenant node.

## Create sole-tenant nodes

To run VMs with your existing licenses on dedicated hardware, you must do the following:

  1. Create sole-tenant node templates by following the instructions in [Creating sole-tenant node templates](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates).

  2. Create sole-tenant node groups by following the instructions in [Creating sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups). When creating your node group, consider the following for your host maintenance policy:

     * If your licenses are assigned per physical core, use the `restart-in-place` or `migrate-within-node-group` host maintenance policy to minimize the number of physical servers used.
     * If your licenses are assigned per user or device (such as for Virtual Desktop licenses), use the `default` host maintenance policy, as these models don't require limiting physical server usage.

For more information, see [Host maintenance policies](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy).




## Provision a sole-tenant VM

Provision a VM on the node group and specify its host maintenance policy. Be aware of the following requirements:

  * To provision in node groups with `restart-in-place` host maintenance policy, make sure that the VM has the value `TERMINATE` for the **on host maintenance** option.
  * To provision in node groups with `migrate-within-node-group` maintenance policy, make sure that the VM targets a single node group with the `node-group-name` affinity label, and that it does not target single nodes with the `node-name` affinity label. Any type of host maintenance option is valid, but the recommendation is to use `MIGRATE`.



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.create` on the project, and [other permissions related to creating an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#permissions-required-for-this-task) that are related to your scenario



###  Console 

If you used node affinity labels in the template, you can create multiple VMs by using managed instance groups (MIGs) and specifying the node affinity labels under **Sole-tenant nodes** settings, or, create individual VMs from the node group details page:

  1. Go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click the **Name** of the node group to provision a VM on.

  3. Create a VM on a sole-tenant node by doing one of the following:

     * To create a VM anywhere in the sole-tenant node group, click **Create instance**.
     * To create a VM on a specific sole-tenant node, click the **Name** of a sole-tenant node group, then click the **Name** of a sole-tenant node, then click **Create instance**.
  4. Configure the sole-tenant VM. Because you already selected your node group or a specific node, the **Region** , **Zone** , and **Node affinity labels** are already specified by the template.

  5. Select a **Machine configuration** by specifying the **Machine family** , **Series** , and **Machine type**. Choose the **Series** that corresponds to the [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types).

  6. Select the **Boot disk** for the sole-tenant VM, which is the previously imported virtual disk image.

  7. Select the **Management** tab:

     * Under **Availability policy > On host maintenance**, select the restart behavior of the VM.
     * Under **Automatic Restart** , select **On (recommended)** or **Off**.
  8. Click **Create**.




###  gcloud 

Provision a sole-tenant VM on a sole-tenant node group by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    
    gcloud compute instances create VM_NAME \
        --machine-type MACHINE_TYPE \
        --image IMAGE_NAME \
        --zone ZONE \
        --node-group GROUP_NAME \
        RESTART_BEHAVIOR \
        --maintenance-policy MAINTENANCE_POLICY
    

Replace the following:

  * `VM_NAME`: name of the VM to create.
  * `MACHINE_TYPE`: machine type for the new VM.
  * `IMAGE_NAME`: image to create a VM from. This is the image created during the import process.
  * `ZONE`: zone to create the VM in.
  * `GROUP_NAME`: name of the node group to provision the VM on.
  * `RESTART_BEHAVIOR`: restart behavior of this VM. Set the restart behavior to one of the following values:

    * `--restart-on-failure`
    * `--no-restart-on-failure`
  * `MAINTENANCE_POLICY`: VM behavior during maintenance events. Set the maintenance policy to one of the following values:

    * `MIGRATE`
    * `TERMINATE`



###  REST 

Provision a sole-tenant VM on a sole-tenant node group by using the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/VM_ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "/zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
      "scheduling": {
        "nodeAffinities": [
          {
            "key": "node-group",
            "operator": "IN",
            "values": [
            "GROUP_NAME"
            ]
          }
        ],
        "onHostMaintenance": "MAINTENANCE_POLICY",
        "automaticRestart": "AUTOMATIC_RESTART"
      },
      "networkInterfaces": [
        {
         "network": "/global/networks/NETWORK",
         "subnetwork": "/regions/region/subnetworks/SUBNETWORK"
        }
      ],
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "/projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
           }
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project to create the VM in.
  * `VM_ZONE`: zone to create the VM in.
  * `VM_NAME`: name of the new VM.
  * `MACHINE_TYPE_ZONE`: zone containing the machine type.
  * `MACHINE_TYPE`: machine type to provision the VM on.
  * `GROUP_NAME`: name of the node group to provision the VM on.
  * `MAINTENANCE_POLICY`: VM behavior during maintenance events, set to either `MIGRATE` or `TERMINATE`.
  * `AUTOMATIC_RESTART`: specifies whether the VM is automatically restarted if Compute Engine stops the VM. The default value is `true`.
  * `NETWORK`: name of the network to connect the VM to.
  * `SUBNETWORK`: name of the subnetwork to connect the VM to.
  * `IMAGE_PROJECT`: image project containing the source image.
  * `IMAGE_FAMILY`: image family of the source image.



## What's next

  * Consult the [FAQ](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license/frequently-asked-questions) for bringing your own licenses to Google Cloud.

  * Learn about [Windows on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
