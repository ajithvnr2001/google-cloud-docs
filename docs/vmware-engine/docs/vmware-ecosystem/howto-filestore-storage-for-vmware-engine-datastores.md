---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-filestore-storage-for-vmware-engine-datastores/
title: Use Google Cloud Filestore Volumes as vSphere Datastore in VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:32.960173+00:00
---

# Use Google Cloud Filestore Volumes as vSphere Datastore in VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-filestore-storage-for-vmware-engine-datastores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Google Cloud Filestore Volumes as vSphere Datastore in VMware Engine

This page describes how to use Filestore as an external Datastore for ESXi hosts in Google Cloud VMware Engine. Filestore Zonal and Regional tier instances with capacities of 10 TiB or greater are VMware certified for use with VMware Engine Datastores. These tiers are available in all [VMware Engine regions](https://cloud.google.com/about/locations#regions).

For an overview of NFS Datastores, including benefits and prerequisites, see [NFS Datastores overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview).

## Limitations

In addition to the limitations described in the [NFS Datastores overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview), the following limitations apply to Filestore Datastores:

  * **Supported tiers:** VMware Engine supports Zonal and Regional tier instances with capacities of 10 TiB or greater. Basic SSD and Basic HDD tier instances are not supported.
  * **Connection mode:** VMware Engine supports only instances that are connected by using Private Service Access (PSA). You can't mount instances connected with direct peering or Private Service Connect (PSC) as Datastores. For more information, see [Network configuration and IP resource requirements](https://docs.cloud.google.com/filestore/docs/network-ip-requirements).
  * **VAAI:** Copy offload ([VAAI](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/techpaper/vmware-vsphere-storage-api-array-integration-white-paper.pdf)) is not available.



## Before you begin

Meet the following prerequisites before you mount an external NFS volume as a Datastore:

  * **Filestore instance:** Create a Filestore instance. For instructions, see [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances). Select the Zonal or Regional tier when you create the instance.
  * **Delete protection:** [Enable delete protection](https://docs.cloud.google.com/filestore/docs/deletion-protection) on the volume to prevent accidental deletion and data loss.
  * **VPC Peering:** Establish an active VPC Network Peering connection between the Filestore tenant project VPC and the VMware Engine network (VEN) of the private cloud where you plan to mount the Datastore.



### Get VPC network details

When you create a peering connection between VMware Engine and Filestore, you need some details about the VPC network used by Filestore. To get these details, do the following:

  1. In the Google Cloud console, go to the **Filestore Instances** page.

[Go to Filestore Instances](https://console.cloud.google.com/filestore/instances)

  2. Click the name of your Filestore instance.

  3. On the **Instance details** page, note the VPC network name listed in **VPC network**.

  4. Go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  5. Click the name of the VPC network you noted in step 3.

  6. Click the **VPC network peering** tab.

  7. Select the peering connection named `servicenetworking-googleapis-com`.

  8. Copy the **Peered project ID** and the **Peered VPC network** name. You will need these values when creating a peering connection.




### Create a private connection for legacy networks

If you created your VMware Engine project and private clouds before Nov 12, 2023, you are using an earlier version of the VMware Engine network (legacy VEN). For environments using a legacy VMware Engine network, a private connection is used to connect with Filestore. If your Filestore instance and private cloud are in different projects, you must create this private connection manually. If they are in the same project, the private connection likely already exists.

To create a private connection for legacy networks:

  1. In the Google Cloud console, go to the **Private connections** page.

[Go to Private connections](https://console.cloud.google.com/vmwareengine/private-connections)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the peering connection.

  3. Click **Create**.

  4. In **Private connection name** , provide a name for your peering, for example, `peering-2-filestore`.

  5. In **VMware Engine network** , specify the VMware Engine network you want to peer, for example, `us-central1-default`.

  6. For **Private connection type** , select **Private services access**.

  7. In **Peered project ID** , enter the peered project ID of Filestore that you retrieved in the previous step.

  8. For **Routing mode** , select **Global**.

  9. Click **Create**.




Expect the VPC peering status of your new private connection to stay in the _Inactive_ state for up to 72 hours while VMware Engine services and validates the peering request.

For legacy networks, ensure that the private connection to the Filestore tenant project is active before you attempt to mount a Datastore. A missing or inactive connection will cause the mount operation to fail. Also, avoid deleting a private connection that is in use by a mounted Datastore, as this can disrupt access to the Datastore. 

### Create a peering connection

If your VMware Engine project and private clouds were created after Nov 12, 2023, do the following. For more information on how to create VPC peerings for such environments, see [Peer a VPC network](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network).

  1. In the Google Cloud console, go to the **VPC Network peerings** page.

[Go to VPC Network peerings](https://console.cloud.google.com/vmwareengine/network-peerings)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the peering connection.

  3. Click **Create**.

  4. In the **Name** field, provide a name for your networking peering. For example, `peering-2-filestore`.

  5. In the **VMware Engine network** section, keep the default **In current project** selected and specify the VMware Engine network you want to peer, for example `ven1`.

  6. For **Peering** , select **Private services access**.

  7. In the **Service networking tenant project ID** field, enter the **Peered project ID** that you retrieved in the previous section.

  8. In the **Service networking tenant VPC name** field, enter the **Peered VPC network** name that you retrieved in the previous section.

  9. In the **Route exchange** section, keep the default settings.

  10. Click **Create**.




After the VPC peering is established, route propagation to the vSphere nodes can take up to 20 minutes.

Peering connects two networks. Avoid overlapping routes between the two networks; peering does not prevent overlaps in dynamic routes.

  * **Service subnet:** You must configure an IP CIDR range on a service subnet to use for NFS traffic. This subnet must be used exclusively for NFS Datastores.
  * **NFS volume access control:** You must add the reserved CIDR allocation for the service subnet to the allowed clients list of your NFS volume. For Filestore, in the [**Access control**](https://docs.cloud.google.com/filestore/docs/access-control) section of the instance, add a rule that grants access to the service subnet CIDR range.
  * **Required roles:** To mount Filestore volumes as external Datastores, the VMware Engine service agent requires specific IAM roles. Grant the following roles to the service agent:

    * **`roles/file.viewer`:** To allow VMware Engine to access Filestore instances.
    * **`roles/compute.networkViewer`:** To allow VMware Engine to view network peerings.

Use the following gcloud CLI commands to grant these roles:
    
    gcloud projects add-iam-policy-binding FILESTORE_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/file.viewer
    
    gcloud projects add-iam-policy-binding FILESTORE_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/compute.networkViewer
    

Replace the following:

    * `FILESTORE_PROJECT_ID`: The project ID where your Filestore instance resides.
    * `PROJECT_NUMBER`: The project number where VMware Engine is enabled.



## Mount the Filestore instance as a Datastore

After you create your Filestore instance and configure prerequisites, you can mount the volume as a Datastore using the VMware Engine API.

After VMware Engine mounts the NFS Datastore to all hosts in a given cluster and it becomes available, you can use the vCenter console to provision VMs against the external Datastore, view metrics, and view logs related to I/O operations performed against the external Datastore.

## API, gcloud CLI, and Terraform workflow

For details on using the API, the gcloud CLI, or Terraform to manage Datastores, see [Manage NFS volumes as vSphere Datastores in VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores).

For information on reference Terraform configurations, see the following resources:

  * [Terraform for creating a datastore](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_datastore)
  * [Terraform example for mounting Filestore](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_cluster#example-usage---vmware-engine-cluster-nfs-datastore-filestore)
  * [Terraform example for mounting NetApp Volumes](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_cluster#example-usage---vmware-engine-cluster-nfs-datastore-netapp)



## What's next

  * Learn more about [Filestore](https://docs.cloud.google.com/filestore/docs/overview).
  * [Compare the relative advantages of block, file, and object storage](https://docs.cloud.google.com/architecture/storage-advisor#review_the_storage_options).
  * [Review the storage options for High Performance Computing (HPC) workloads in Google Cloud](https://docs.cloud.google.com/architecture/parallel-file-systems-for-hpc#storage-options-for-hpc-workloads-in-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
