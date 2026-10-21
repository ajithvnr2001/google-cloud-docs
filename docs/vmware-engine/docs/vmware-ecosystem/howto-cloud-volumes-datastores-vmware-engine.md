---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-datastores-vmware-engine/
title: Use Google Cloud NetApp Volumes as a vSphere Datastore in VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:39.264900+00:00
---

# Use Google Cloud NetApp Volumes as a vSphere Datastore in VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-datastores-vmware-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Google Cloud NetApp Volumes as a vSphere Datastore in VMware Engine

This page describes how to use Google Cloud NetApp Volumes NFS storage with Standard, Premium, Extreme, and Flex Unified service levels as an external Datastore for ESXi hosts in Google Cloud VMware Engine. To use Google Cloud NetApp Volumes as a Datastore, create Google Cloud NetApp Volumes volumes in the same region as the vSphere cluster and then mount them as external Datastores to existing ESXi hosts in VMware Engine. This solution provides data protection through crash-consistent snapshots and cross-region replication.

For an overview of NFS Datastores, including prerequisites and benefits, see [NFS Datastores overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview).

The following diagram shows NetApp Volumes being used with VMware Engine and Compute Engine:

![NetApp Volumes in relation to VMware Engine and Compute Engine.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-netapp-volumes.png)

The preceding diagram illustrates using Google Cloud NetApp Volumes as an external Datastore for VMware Engine. A VPC Network Peering connection exists between your VPC network and the VMware Engine network (VEN). Another VPC Network Peering connection exists between the VEN and the Google Cloud NetApp Volumes service network where the NFS volume resides. The Google Cloud NetApp Volumes volume is mounted as an NFS Datastore on the ESXi hosts in the VMware Engine private cloud.

## Limitations

In addition to the limitations described in [NFS Datastores overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview), the following limitations apply to Google Cloud NetApp Volumes Datastores:

  * **VAAI:** Copy offload ([VAAI](https://core.vmware.com/resource/vmware-vsphere-apis-array-integration-vaai)) is not supported.



## Before you begin

Meet the following prerequisites before you mount an external NFS volume as a Datastore:

  * **VPC Peering:** Establish an active VPC Network Peering connection between the NFS volume's VPC network and the VMware Engine network (VEN) of the private cloud where you plan to mount the Datastore.
  * **Service subnet:** Reserve a dedicated service subnet with a unique CIDR range allocated for NFS traffic. Configure at least a `/26` CIDR for the VMware Engine service network for external NFS storage. This subnet must be used exclusively for NFS Datastores, but the same service subnet can be used for multiple NFS Datastores.
  * **Delete protection:** Enable delete protection on the volume to prevent accidental deletion and data loss.



## Permissions

To mount Google Cloud NetApp Volumes volumes as external Datastores, the VMware Engine service agent requires specific IAM roles for `service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com`. Grant the following roles to the service agent:

  * **`roles/netapp.viewer`:** Grant this role on the project where Google Cloud NetApp Volumes resides. This role lets VMware Engine access Google Cloud NetApp Volumes volumes.
  * **`roles/compute.networkViewer`:** Grant this role on the project where Google Cloud NetApp Volumes resides. If you are using Shared VPC and Google Cloud NetApp Volumes is deployed in a service project, grant this role on the host project instead. This role lets VMware Engine view network peerings.



Use the following gcloud CLI commands to grant these roles:
    
    
    gcloud projects add-iam-policy-binding NETAPP_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/netapp.viewer
    
    gcloud projects add-iam-policy-binding VPC_HOST_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/compute.networkViewer
    

Replace the following:

  * `NETAPP_PROJECT_ID`: The project ID where your Google Cloud NetApp Volumes volume resides.
  * `PROJECT_NUMBER`: The project number where VMware Engine is enabled.
  * `VPC_HOST_PROJECT_ID`: The project ID that holds the VPC network used by Google Cloud NetApp Volumes. If Google Cloud NetApp Volumes is deployed in a Shared VPC service project, this is the ID of the host project. Otherwise, this value is the same as `NETAPP_PROJECT_ID`.



## Get VPC network details

When you create a peering connection between VMware Engine and NetApp Volumes, you need some details about the VPC network used by NetApp Volumes. To get these details, do the following:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the VPC network that is peered with NetApp Volumes.

  3. Click the **VPC network peering** tab.

  4. Select the peering connection to the NetApp Volumes tenant project. The connection name is typically `sn-netapp-prod`.

  5. Copy the **Peered project ID** (e.g., `netapp-tenant-project-tp`) and the **Peered VPC network** name.




## Create a peering connection for legacy networks

To establish a connection between VMware Engine and NetApp Volumes or Filestore services, make a one-time peering between tenant host projects. If you created your VMware Engine project and private clouds before Nov 12, 2023, you are using an earlier version of the VMware Engine network. For environments using an earlier version of VMware Engine network, do the following:

  1. In the Google Cloud console, go to the **Private connections** page.

[Go to Private connections](https://console.cloud.google.com/vmwareengine/private-connections)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the peering connection.

  3. Click **Create**.

  4. In **Private connection name** , provide a name for your peering, for example, `peering-2-netapp-volumes`.

  5. In **VMware Engine network** , specify the VMware Engine network you want to peer, for example, `us-central1-default`.

  6. For **Private connection type** , select **Third party service**.

  7. In **Peered project ID** , enter the peered project ID of the NetApp Volumes that contains your volume.

  8. In **Peered VPC network** , enter the name of the peered VPC network that volume is in.

  9. Click **Create**.




Expect the VPC peering status of your new private connection to stay in the _Inactive_ state for up to 72 hours while VMware Engine services and validates the peering request.

For legacy networks, ensure that the private connection to the NetApp Volumes tenant project is active before you attempt to mount a Datastore. A missing or inactive connection will cause the mount operation to fail. Also, avoid deleting a private connection that is in use by a mounted Datastore, as this can disrupt access to the Datastore. 

## Create a peering connection

If your VMware Engine project and private clouds were created after Nov 12, 2023, do the following. For more information on how to create VPC peerings for such environments, see [Peer a VPC network](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network).

  1. In the Google Cloud console, go to the **VPC Network peerings** page.

[Go to VPC Network peerings](https://console.cloud.google.com/vmwareengine/network-peerings)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the peering connection.

  3. Click **Create**.

  4. In the **Name** field, provide a name for your networking peering. For example, `peering-2-netapp-volumes`.

  5. In the **VMware Engine network** section, keep the default **"In current project"** selected. Specify the VMware Engine network you want to peer, for example `ven1`.

  6. For **Peering** , select **Google Cloud NetApp Volumes**.

  7. In the **Service tenant project ID** field, enter the _peered project ID_ of the Google Cloud project containing your volume.

  8. In the **Route exchange** section, keep the default settings.

  9. Click **Create**.




After the VPC Peering is established, route propagation to the vSphere nodes can take up to 20 minutes.

Peering connects two networks. Avoid overlapping routes between the two networks; peering does not prevent overlaps in dynamic routes.

## Create Google Cloud NetApp Volumes volumes

When you [create a Google Cloud NetApp Volumes volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume) for use as a VMware Engine Datastore, ensure that the volume export rule allows the following:

  * Access from the service subnet range you created earlier under Authorized applications.
  * Read and write access
  * Root access



## Mark a volume as non-deletable

Enable delete protection on your volume before mounting it as an external NFS Datastore. When delete protection is enabled, it prevents accidental deletion by any user.

To enable delete protection, use the gcloud CLI to restrict the `delete` action on the volume:
    
    
    gcloud netapp volumes update $VOLUME_NAME --restricted-actions=DELETE --project=$PROJECT --location=$LOCATION
    

For more information, see [Prevent volume deletion](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#block-volume-deletion).

After creating the volume, you can perform various volume management functions by using the NetApp Volumes UI/API/CLI. For more information, see [Volumes overview](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview).

## Mount the volume as a Datastore

Mount the volume as a Datastore using the VMware Engine API after creating your Google Cloud NetApp Volumes volume and completing the prerequisites.

After VMware Engine mounts the Datastore, it becomes available, and you can use the vCenter UI to provision VMs against the external Datastore, view metrics, and view logs related to I/O operations performed against the external Datastore.

For more information about NetApp Volumes, see [What is Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).

## REST, gcloud CLI, and Terraform workflow

For details on using the API, the gcloud CLI, or Terraform to manage Datastores, see [Manage NFS volumes as vSphere Datastores in VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
