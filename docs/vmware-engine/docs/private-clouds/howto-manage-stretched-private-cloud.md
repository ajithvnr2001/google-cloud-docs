---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-stretched-private-cloud/
title: Managing stretched private cloud resources and activity \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:01.146172+00:00
---

# Managing stretched private cloud resources and activity  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-stretched-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing stretched private cloud resources and activity

After you create a stretched private cloud, you can view detailed information about it, manage its resources and activity, and access its VMware management appliances.

Each stretched private cloud contains one or more clusters that are stretched across two Google Cloud zones. Each cluster contains nodes that correspond to ESXi hosts.

**Important:** Adjustments to clusters assign VMware Engine node quota corresponding to your Google Cloud project. To increase your quota, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/quotas).

To manage a stretched private cloud, start by accessing its resource summary page:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the stretched private cloud.

  3. Select the stretched private cloud you want to manage from the list of private clouds.




## Viewing a private cloud summary

The summary provides information about your stretched private cloud including its name, number of vSphere clusters, number of nodes, location, operational state, and more. The summary page also includes the DNS servers deployed on the private cloud.

From the private cloud summary page, you can perform the following actions:

  * [**Launch vSphere Client.**](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client) Access the vCenter for this stretched private cloud.

  * **Expand.** Expand this stretched private cloud by adding a minimum of two nodes.

  * **Shrink nodes.** Shrink this stretched private cloud by removing nodes.

  * [**Delete the private cloud.**](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud) Delete a stretched private cloud, including all of the VMs, vCenter configuration, and data. _Before deleting, back up all systems and data._

  * [**Change vSphere privileges.**](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege) Elevate your privileges to perform a particular task on this stretched private cloud.

  * **Copy IP addresses of DNS servers.** Get a list of DNS servers on your private cloud. You can set up DNS forwarding from on-premises DNS servers to your private Cloud DNS servers. For more information about DNS forwarding, see [Configuring DNS for name resolution for private cloud vCenter access from on-premises workstations](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises).




## Expanding a stretched private cloud

A stretched private cloud consists of one or more vSphere clusters, each containing multiple nodes. When adding nodes to a stretched private cloud, you add a minimum of two nodes (or in multiples of two nodes) to the existing cluster or create a new cluster. A stretched private cloud can be expanded multiple times as long as you stay within the overall [node limits](https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud#limits).

If a stretched cluster is expanded by two nodes, one node is added to the primary site, and the other node is added to the secondary site.

As part of the new cluster configuration, Google configures the VMware infrastructure. The settings include storage settings for vSAN disk groups, VMware High Availability, and Distributed Resource Scheduler (DRS).

You can expand a stretched cluster by adding nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following. This action adds the specified number of nodes to each zone in the stretched cluster.

## Expand a stretched cluster using a node

You can expand a stretched cluster by adding nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following.

###  Console 

To expand a stretched cluster by adding nodes using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click the name of the cluster you want to expand.

  3. Under cluster details, click **Adjust nodes**.

  4. Choose a higher number of nodes per zone for your cluster.




###  gcloud 

To expand a stretched cluster by adding nodes using the Google Cloud CLI, do the following:

Increase your node count by entering the [`gcloud vmware private-clouds clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update):
    
    
    gcloud vmware private-clouds clusters update CLUSTER_ID \
      --location="REGION" \
      --project="PROJECT_ID" \
      --private-cloud=PRIVATE_CLOUD_ID \
      --update-nodes-config=type=standard-72,count="NODE_COUNT"

Replace the following:

  * `CLUSTER_ID`: the cluster ID for this request.
  * `REGION`: the region for this request.
  * `PROJECT_ID`: the project ID for this request.
  * `NODE_COUNT`: the new total number of nodes in the cluster, an even number, for this request.



### API

To expand a stretched cluster by adding nodes using the VMware Engine API, do the following:

Increase your node count by making a `PATCH` request:
    
    
      PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/PRIVATE_CLOUD_ID/clusters/CLUSTER_ID"
      -d '{
        "node_type_configs": {
            "standard-72": {
              "node_count": "NODE_COUNT"
            }
        }
      }'
    

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `REGION`: the region for this request.
  * `CLUSTER_ID`: the cluster ID for this request.
  * `NODE_COUNT`: the new total number of nodes in the cluster, an even number, for this request.



## Add a cluster

To add a cluster to a stretched private cloud using the Google Cloud console, Google Cloud CLI, or VMware Engine API by do the following. The added cluster is stretched across the same two data zones as specified during the stretched private cloud creation:

###  Console 

To add a cluster using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click the **Clusters** tab.

  3. Click **Add Cluster**.

  4. Add the cluster details and submit.




###  gcloud 

To add a cluster using the Google Cloud CLI, do the following:

Add a cluster by running the [`gcloud vmware private-clouds clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/create):
    
    
    gcloud vmware private-clouds clusters create CLUSTER_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --node-type-config=type=standard-72,count="NODE_COUNT"

Replace the following:

  * `CLUSTER_ID`: the cluster ID for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `NODE_COUNT`: the total number of nodes in the cluster, an even number, for this request.



### API

To expand a stretched cluster by adding nodes using the VMware Engine API, do the following:

Increase your node count by making a `POST` request:
    
    
      POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/PRIVATE_CLOUD_ID/clusters/CLUSTER_ID"
        -d '{
          "node_type_configs": {
              "standard-72": {
                "node_count": "NODE_COUNT"
              }
          }
        }'
    

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `REGION`: the region for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `CLUSTER_ID`: the cluster ID for this request.
  * `NODE_COUNT`: the total number of nodes in the cluster, an even number, for this request.



## Shrink a stretched cluster

You can shrink a stretched cluster by removing nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following.

###  Console 

To shrink a stretched cluster by removing nodes using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click the name of the cluster you want to expand.

  3. Under cluster details, click **Adjust nodes**.

  4. Choose a lower number of nodes for your cluster.




###  gcloud 

To shrink a stretched cluster by removing nodes using the Google Cloud CLI, do the following:

Decrease your node count by running the [`gcloud vmware private-clouds clusters update command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update):
    
    
    gcloud vmware private-clouds clusters update CLUSTER_ID \
      --location="REGION" \
      --project="PROJECT_ID" \
      --private-cloud=PRIVATE_CLOUD_ID \
      --update-nodes-config=type=standard-72,count="NODE_COUNT"

Replace the following:

  * `CLUSTER_ID`: the cluster ID for this request.
  * `REGION`: the region for this request.
  * `PROJECT_ID`: the project for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `NODE_COUNT`: the new total number of nodes in the cluster, an even number, for this request. Shrinking must be done in increments of two.



### API

To shrink a stretched cluster by removing nodes using the VMware Engine API, do the following:

Decrease your node count by making a `PATCH` request:
    
    
        PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/PRIVATE_CLOUD_ID/clusters/CLUSTER_ID"
        -d '{
          "node_type_configs": {
              "standard-72": {
                "node_count": "NODE_COUNT"
              }
          }
        }'
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `REGION`: the region for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud ID for this request.
  * `CLUSTER_ID`: the cluster ID for this request.
  * `NODE_COUNT`: the new total number of nodes in the cluster, an even number, for this request. Shrinking must be done in increments of two.



This process requires resynchronization in vSAN and can take a few hours, depending on the data.

## Shrink a stretched private cloud

When removing nodes from a stretched private cloud, you remove nodes from the existing cluster or delete the entire cluster.

To shrink a stretched private cloud, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. On the private clouds summary page, click **Remove nodes**.

  3. Select the cluster that you want to shrink or delete.

  4. Select **Remove one node per zone** or **Delete the whole cluster**.

  5. Verify the cluster capacity.

  6. Click **Submit** to begin the process of removing nodes.




### Restrictions

The process of removing nodes from your stretched private cloud has the following restrictions:

  * You can't remove nodes from a cluster with six (6) nodes (three (3) per zone).
  * The total storage consumed can't exceed the total capacity after removing nodes from a cluster.
  * You can't delete the first cluster that was created when the private cloud was created.



## Viewing subnets

To view the list of defined management subnets for your private cloud, select the **Subnets** tab. The list includes the HCX subnets created when the private cloud was created.

## Viewing activity information

To view the activity information for your private cloud, click **Go to Logs Viewer**. For a full list of activities and associated actions, see [Monitoring VMware Engine activity](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-monitor-activity).

## Viewing vSphere management network

To view the list of VMware management resources and virtual machines that are configured on your private cloud, select the **vSphere Management Network** tab. Information includes the software version, fully qualified domain name (FQDN), and IP address of the resources.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
