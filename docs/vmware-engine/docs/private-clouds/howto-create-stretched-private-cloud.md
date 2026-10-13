---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-stretched-private-cloud/
title: Creating a VMware Engine stretched private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:55.702349+00:00
---

# Creating a VMware Engine stretched private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-stretched-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating a VMware Engine stretched private cloud

A Google Cloud VMware Engine stretched private cloud is a private cloud that is stretched across two data zones and a witness zone, all within the same Google Cloud region. Stretched private clouds provide compute, storage and network infrastructure that is fault tolerant to zone level failures in a given region.

Stretched private clouds use vSphere and vSAN stretched clusters to provide compute and storage high availability against zone-level failures. All clusters of a stretched private cloud are considered VMware Engine stretched clusters, including the primary cluster.

**Note:** Once a stretched private cloud is created, it cannot be converted back to a standard private cloud. Additionally, you cannot convert an existing private cloud to a stretched private cloud.

## Before you begin

The steps in this document assume that you first do the following:

  * Allocate a unique IP address range for vSphere/vSAN subnets of the private cloud you want to create. 
    * **Minimum CIDR range prefix:** _/24_
    * **Maximum CIDR range prefix:** _/20_
  * If you want [global address resolution using Cloud DNS](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises#global-address-resolution-cloud-dns), then [enable the Cloud DNS API](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name#before-you-begin) and complete Cloud DNS setup before you create your private cloud.



The vSphere/vSAN subnet address space must not overlap with any network that will communicate with the private cloud, such as on-premises networks and Google Cloud Virtual Private Cloud (VPC) networks. For more information about vSphere or vSAN subnets, see [VLANs and subnets on VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets).

## Create a stretched private cloud

###  Console 

To create a stretched private cloud using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the stretched private cloud.

  3. Click **Create**.

  4. Click **Stretched private cloud**.

  5. Enter your primary hosting location and select your secondary zone.

  6. Select the node type for your primary cluster.

  7. Select the number of nodes per zone for the stretched private cloud. Create your stretched private cloud with a minimum of 3 nodes per zone.

  8. Optional: Click the **Customize Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  9. Enter a CIDR range for the VMware management network. Make sure that the CIDR range doesn't overlap with any of your on-premises or cloud subnets.

  10. Click **Review and create**.

  11. Review the settings. To change any settings, click **Back**.

  12. Click **Create** to begin creating the stretched private cloud.

  13. Optional: If you want to list stretched private cloud details and cluster data to confirm the creation of the new stretched private cloud, start on the **Private clouds** details page. This page contains private cloud details. Clicking the **Clusters** tab displays cluster data in the table.




The following list describes each field during private cloud creation in more detail:

  * **Name:** Permanent unique identifier of the private cloud.
  * **Description:** Additional information that's visible on the details page of the private cloud.
  * **Region:** Geographical region where VMware Engine hosts your private cloud.
  * **Preferred Zone:** Subset of a region physically isolated from other zones in the same region. The preferred zone is the preferred single failure domain within a region.
  * **Secondary Zone:** Subset of a region physically isolated from other zones in the same region. The secondary zone is the secondary single failure domain within a region.
  * **Primary cluster name:** Name given to the initial vSphere cluster in your private cloud. VMware management appliances of your private cloud run on this cluster.
  * **Node type:** Hardware configuration of nodes in your primary cluster.
  * **Nodes:** Number of nodes in your primary cluster, minimum of 6 nodes.



  * **VMware Engine network:** Network resource that handles private cloud connections according to a network policy. You and resources connected to this VMware Engine network can access the private cloud from within Google Cloud.
  * **Management IP address range:** IP address range used for vCenter Server, NSX Manager, ESXi hosts, and other parts of the private cloud's infrastructure. This range is not used for workload VMs and must not overlap with any part of your VPC network or any other network which you plan to connect your private cloud to.



###  gcloud 

To create a stretched private cloud using the Google Cloud CLI, do the following:

  1. Create a stretched private cloud by entering the [`gcloud vmware private-clouds create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create):
         
         gcloud vmware private-clouds create PRIVATE_CLOUD_ID \
           --description="DESCRIPTION" \
           --location="REGION" \
           --cluster="CLUSTER_ID" \
           --node-type-config=type=standard-72,count="NODE_COUNT" \
           --management-range="MANAGEMENT_RANGE" \
           --vmware-engine-network="NETWORK_ID" \
           --preferred-zone=projects/PROJECT_ID/locations/PREFERRED_ZONE \
           --secondary-zone=projects/PROJECT_ID/locations/SECONDARY_ZONE \
           --type=STRETCHED

Replace the following:

     * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
     * `DESCRIPTION`: a description for this stretched private cloud.
     * `REGION`: the region for this request.
     * `CLUSTER_ID`: the cluster ID for this request.
     * `NODE_COUNT`: the total number of nodes in the cluster, an even number, for this request.
     * `MANAGEMENT_RANGE`: the IP address and range, for example, `192.168.1.0/23`, for this request.
     * `NETWORK_ID`: the network ID for this request.
     * `PROJECT_ID`: the project ID for this request.
     * `PREFERRED_ZONE`: the preferred zone for this request.
     * `SECONDARY_ZONE`: the secondary zone for this request.
  2. Optional: If you want to list stretched private cloud details and cluster data to confirm the creation of the new stretched private cloud, use the [`gcloud vmware private-clouds list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/list):
         
         gcloud vmware private-clouds list \
           --location=REGION

Replace the following:

     * `REGION`: the region for this request.



### API

To create a stretched private cloud using the VMware Engine API, do the following:

  1. Create a stretched private cloud by making a `POST` request:
         
         POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds?private_cloud_id=PRIVATE_CLOUD_ID"
           -d '{
             "network_config": {
               "vmware_engine_network": "projects//locations/REGION/vmwareEngineNetworks/NETWORK_ID",
                 "management_cidr": "MANAGEMENT_CIDR"
             },
             "management_cluster": {
               "cluster_id": "CLUSTER_ID",
               "node_type_configs": {
                 "standard-72": {
                   "node_count": "NODE_COUNT"
                 }
               },
               "stretched_cluster_config": {
                 "preferred_location": "projects/PROJECT_ID/locations/PREFERRED_ZONE",
                 "secondary_location": "projects/PROJECT_ID/locations/SECONDARY_ZONE"
               }
             },
             "type": "STRETCHED"
           }'
         

Replace the following:

     * `PROJECT_ID`: the project for this request.
     * `PREFERRED_ZONE`: the preferred zone for this request.
     * `SECONDARY_ZONE`: the secondary zone for this request.
     * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
     * `REGION`: the region for this request.

     * `MANAGEMENT_CIDR`: the IP address and range, for example, `192.168.1.0/23`, for this request.

     * `CLUSTER_ID`: the cluster ID for this request.

     * `NODE_COUNT`: the total number of nodes in the cluster, an even number, for this request.

  2. Optional: If you want to list stretched private cloud details and cluster data to confirm the creation of the new stretched private cloud, make a `GET` request:
         
         GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/PRIVATE_CLOUD_ID"
         

Replace the following:

     * `PROJECT_ID`: the project for this request.
     * `REGION`: the region for this request.
     * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  3. Optional: If you want to list stretched private cloud details and cluster data to confirm the creation of the new stretched private cloud, make a `GET` request:
         
         GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/PRIVATE_CLOUD_ID"
         

Replace the following:

     * `PROJECT_ID`: the project for this request.
     * `REGION`: the region for this request.
     * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.



As VMware Engine creates your new stretched private cloud, it deploys a number of [VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) and divides the provided IP address range into subnets. Stretched private cloud creation can take 30 minutes to 2 hours. After the provisioning is complete, you receive an email.

**Note:** If the stretched cluster creation fails and you see the message `error Stretched private cloud creation is not allowed in projects without the gcp.requiresPhysicalZoneSeparation organizational policy constraint`, reach out to your account or support team before creating the stretched cluster for a new organization.

## What's next

  * [Get sign-in credentials for management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client).
  * [Manage your stretched private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
