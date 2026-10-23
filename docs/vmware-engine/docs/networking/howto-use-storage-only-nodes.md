---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-use-storage-only-nodes/
title: Manage storage-only nodes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:30.964630+00:00
---

# Manage storage-only nodes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-use-storage-only-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage storage-only nodes

This document describes how to use storage-only nodes in VMware Engine. Storage-only nodes, also known as storage nodes, can be used to scale the storage capacity of a vSAN cluster without adding cores or memory to the cluster. You can create clusters that contain both standard and storage-only nodes, and then expand or shrink them using the Google Cloud CLI or VMware Engine API.

### Google Cloud CLI and API requirements

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

## Before you begin

Before you create a private cloud with storage-only nodes, confirm that a VMware Engine network exists. If a VMware Engine network doesn't exist, create one using the Google Cloud CLI by entering the [`gcloud vmware networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/create):
    
    
       gcloud vmware networks create NETWORK_NAME \
          --type=STANDARD \
          --project=PROJECT_ID

Replace the following:

  * `NETWORK_NAME`: the name for the network.
  * `PROJECT_ID`: the project ID for the request.



## List available node types

To verify that a storage-only node is available for your project and region, list available node types using the Google Cloud CLI or VMware Engine API.

###  gcloud 

List available node types using the [`gcloud vmware node-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/node-types/list) :
    
    
      gcloud vmware node-types list \
         --location=ZONE \
         --project=PROJECT_ID

Replace the following:

  * `ZONE`: the zone for this request.
  * `PROJECT_ID`: the project ID for this request.



###  API 

To list available node types using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/nodeTypes"

Replace the following:

  * `PROJECT_ID`: the project name for this request.
  * `ZONE`: the zone for the private cloud.



## Create a private cloud with storage-only nodes

You can create a VMware Engine private cloud that contains storage-only nodes in addition to standard nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API.

**Note:** A cluster with standard and storage-only nodes must be made up of a minimum of 2 standard nodes and 1 storage-only node.

###  Console 

To create a private cloud with storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the private cloud with storage-only nodes.

  3. Click **Create**.

  4. Enter a name for your private cloud.

  5. Choose **Standard** for the private cloud type.

  6. Select the location where you want the private cloud deployed.

  7. Enter a name for the primary cluster.

  8. Select the node type for your primary cluster.

  9. Select the number of nodes for the private cloud. For production workloads, create your private cloud with at least 3 nodes. VMware Engine deletes private clouds that contain only 1 node after 60 days.

  10. Optional: Click the **Customize Node Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  11. Select the storage node model and node count.

  12. Enter a CIDR range for the VMware management network. Make sure that the CIDR range doesn't overlap with any of your on-premises or cloud subnets.

  13. Select **Create new network** to create a new VMware Engine network or select from an existing network, if applicable.

  14. Click **Create** to begin creating the private cloud.




###  gcloud 

To create private cloud with storage-only nodes using the Google Cloud CLI, do the following:

  1. Create a private cloud PC_STORAGE_NODE_NAME with n `standard-72` nodes and m `storage-only-standard-72` by entering the [`gcloud private-clouds create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create):
         
         gcloud vmware private-clouds create PC_STORAGE_NODE_NAME \
          --location=ZONE \
          --project=PROJECT_ID \
          --description=DESCRIPTION \
          --management-range=IP_ADDRESS \
          --cluster=CLUSTER_NAME \
          --node-type-config=type=standard-72,count=n \
          --node-type-config=type=storage-only-standard-72,count=m \
          --vmware-engine-network=NETWORK_NAME

Replace the following:

     * `PC_STORAGE_NODE_NAME`: the name for the private cloud with storage-only node.
     * `ZONE`: the zone for this private cloud.
     * `PROJECT_ID`: the project ID for the request.
     * `DESCRIPTION`: the description for this private cloud.
     * `IP_ADDRESS`: the IP address and range for this private cloud, for example `192.168.0.0/22`.
     * `CLUSTER_NAME`: the name for the new cluster in this private cloud.
     * `n`: the number of standard nodes in the primary cluster of this private cloud.
     * `m`: the number of storage-only nodes in the primary cluster of this private cloud.
     * `NETWORK_NAME`: the name for the network.
  2. Optional: To confirm creation of the private cloud with storage-only nodes, enter the [`gcloud vmware private-clouds clusters describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/describe):
         
         gcloud vmware private-clouds clusters describe CLUSTER_NAME \
          --location=ZONE \
          --project=PROJECT_ID \
          --private-cloud=PC_STORAGE_NODE_NAME

Replace the following:

     * `CLUSTER_NAME`: the name for the new cluster in this private cloud.
     * `ZONE`: the zone for this private cloud.
     * `PROJECT_ID`: the project ID for the request.
     * `PC_STORAGE_NODE_NAME`: the name for the private cloud with storage-only node.



###  API 

To create private cloud with storage-only nodes using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds?alt=json&privateCloudId=PC_STORAGE_NODE_NAME" -d '{
      "description": "DESCRIPTION",
      "managementCluster": {
         "clusterId": "CLUSTER_NAME",
         "nodeTypeConfigs": {
            "standard-72": {
               "nodeCount": n
            },
            "storage-only-standard-72": {
               "nodeCount": m
            }
         }
         },
         "networkConfig": {
            "managementCidr": "IP_ADDRESS",
            "vmwareEngineNetwork": "projects/PROJECT_ID/locations/ZONE/vmwareEngineNetworks/NETWORK_NAME"
          }
         }'

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the zone for this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name for the private cloud with storage-only node.
  * `DESCRIPTION`: the description for this private cloud.
  * `CLUSTER_NAME`: the name for the new cluster in this private cloud.
  * `n`: the number of standard nodes in the primary cluster of this private cloud.
  * `m`: the number of storage-only nodes in the primary cluster of this private cloud.
  * `IP_ADDRESS`: the IP address and range for this private cloud, for example `192.168.0.0/22`.
  * `NETWORK_NAME`: the name for the network.



As VMware Engine creates your new private cloud, it deploys a number of [VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) and divides the provided IP address range into subnets. Private cloud creation can take 30 minutes to 2 hours. After the provisioning is complete, you receive an email.

## Expand a cluster with storage-only nodes

You can expand a standard cluster by adding storage-only nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following:

###  Console 

To expand a cluster with storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to expand.

  3. Click the **Cluster** tab.

  4. Click the name of the cluster you want to expand.

  5. Click **Edit**.

  6. Under **Node configuration** , select a storage node model and increase the node count.

  7. Click **Save**.




###  gcloud 

To expand a cluster by adding storage-only nodes using the Google Cloud CLI, use the [`gcloud vmware private-clouds clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update):
    
    
      gcloud vmware private-clouds clusters update CLUSTER_NAME \
         --private-cloud=PC_STORAGE_NODE_NAME \
         --location=ZONE \
         --project=PROJECT_ID \
         --update-nodes-config=type=storage-only-standard-72,count=m

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster in this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `ZONE`: the zone for this private cloud.
  * `PROJECT_ID`: the project ID for the request.
  * `m`: the new total number of storage-only nodes in the specified cluster of this private cloud.



###  API 

To expand a cluster by adding storage-only nodes using the VMware Engine API, make a `PATCH` request:
    
    
    PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PC_STORAGE_NODE_NAME/clusters/CLUSTER_NAME/?alt=json&updateMask=node_type_configs.*.node_count" -d '{
      "nodeTypeConfigs": {
         "standard-72": {
            "nodeCount": n
         },
         "storage-only-standard-72": {
            "nodeCount": m
         }
       }
      }'

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the zone for this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `CLUSTER_NAME`: the name of the cluster in this private cloud.
  * `n`: the number of standard nodes in the specified cluster of this private cloud.
  * `m+1`: the new total number of storage-only nodes in the specified cluster of this private cloud.



## Shrink a cluster with storage-only nodes

You can shrink a cluster that contains storage-only nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following:

###  Console 

To shrink a cluster with storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to shrink.

  3. Click the **Cluster** tab.

  4. Click the name of the cluster you want to shrink.

  5. Click **Edit**.

  6. Under **Node configuration** , select a lower node count.

  7. Click **Save**.




###  gcloud 

To shrink a cluster that contains storage-only nodes using the Google Cloud CLI, use the [`gcloud vmware private-clouds clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update):
    
    
      gcloud vmware private-clouds clusters update CLUSTER_NAME \
         --private-cloud=PC_STORAGE_NODE_NAME \
         --location=ZONE \
         --project=PROJECT_ID \
         --update-nodes-config=type=storage-only-standard-72,count=m

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster in this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `ZONE`: the zone for this private cloud.
  * `PROJECT_ID`: the project ID for the request.
  * `m`: the new total number of storage-only nodes in the specified cluster of this private cloud.



###  API 

To shrink a cluster that contains storage-only nodes using the VMware Engine API, make a `PATCH` request:
    
    
    PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PC_STORAGE_NODE_NAME/clusters/CLUSTER_NAME/?alt=json&updateMask=node_type_configs.*.node_count" -d '{
      "nodeTypeConfigs": {
         "standard-72": {
            "nodeCount": n
         },
         "storage-only-standard-72": {
            "nodeCount": m
         }
       }
      }'

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the zone for this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `CLUSTER_NAME`: the name of the cluster in this private cloud.
  * `n`: the number of standard nodes in the specified cluster of this private cloud.
  * `m`: the new total number of storage-only nodes in the specified cluster of this private cloud.



## Create a new cluster with storage-only nodes

You can create a new cluster in an existing private cloud that includes storage-only nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following:

###  Console 

To create a new cluster with storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to create a cluster in.

  3. Click the name of the private cloud where you want to create the new cluster.

  4. Click the **Clusters** tab.

  5. Click **Add cluster**.

  6. Enter a cluster name.

  7. Select the HCI node model and node count.

  8. Optional: Click the **Customize Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  9. Select the storage node model and node count.

  10. Click **Create**.




###  gcloud 

To create a new cluster with storage-only nodes using the Google Cloud CLI, use the [`gcloud vmware private-clouds clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/create):
    
    
      gcloud vmware private-clouds clusters create CLUSTER_NAME \
         --private-cloud=PC_STORAGE_NODE_NAME \
         --location=ZONE \
         --project=PROJECT_ID \
         --node-type-config=type=standard-72,count=n \
         --node-type-config=type=storage-only-standard-72,count=m

Replace the following:

  * `CLUSTER_NAME`: the name for the new cluster in this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `ZONE`: the zone for this private cloud.
  * `PROJECT_ID`: the project ID for the request.
  * `n`: the number of standard nodes in the specified cluster of this private cloud.
  * `m`: the number of storage-only nodes in the specified cluster of this private cloud.



###  API 

To create a new cluster in a private cloud with storage-only nodes using the VMware Engine API, make a `PATCH` request:
    
    
    PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PC_STORAGE_NODE_NAME/clusters?alt=json&clusterId=CLUSTER_NAME" -d '{
      "nodeTypeConfigs": {
         "standard-72": {
            "nodeCount": n
         },
         "storage-only-standard-72": {
            "nodeCount": m
         }
       }
      }'

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the zone for this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name for the private cloud.
  * `CLUSTER_NAME`: the name for the new cluster in this private cloud.
  * `n`: the number of standard nodes in the specified cluster of this private cloud.
  * `m`: the number of storage-only nodes in the specified cluster of this private cloud.



## Delete a cluster with storage-only nodes

You can delete a cluster that contains storage-only nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following:

###  Console 

To delete a cluster with storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to delete a cluster in.

  3. Click the **Cluster** tab.

  4. Click the delete icon in the row of the cluster you want to delete.




###  gcloud 

To delete a cluster that contains storage-only nodes using the Google Cloud CLI, use the [`gcloud vmware private-clouds clusters delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete):
    
    
      gcloud vmware private-clouds clusters delete CLUSTER_NAME \
         --private-cloud=PC_STORAGE_NODE_NAME \
         --location=ZONE \
         --project=PROJECT_ID

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster in this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `ZONE`: the zone for this private cloud.
  * `PROJECT_ID`: the project ID for the request.



###  API 

To delete a cluster that contains storage-only nodes using the VMware Engine API, make a `DELETE` request:
    
    
    DELETE "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PC_STORAGE_NODE_NAME/clusters/CLUSTER_NAME/?alt=json"

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the zone for this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `CLUSTER_NAME`: the name of the cluster in this private cloud.



## Create a stretched private cloud with storage-only nodes

You can create a VMware Engine stretched private cloud that contains standard and storage-only nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API.

**Note:** The combination of standard and storage nodes in a stretched cluster must be an even number to split nodes evenly between data sites.

###  Console 

To create a stretched private cloud that contains storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the stretched private cloud with storage-only nodes.

  3. Click **Create**.

  4. Enter a name for your private cloud.

  5. Choose **Stretched** for the private cloud type.

  6. Enter your primary hosting location and select your secondary zone.

  7. Select the node type for your primary cluster.

  8. Select the number of nodes per zone for the stretched private cloud. Create your stretched private cloud with a minimum of 3 nodes per zone.

  9. Optional: Click the **Customize Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  10. Select the storage node model and node count.

  11. Enter a CIDR range for the VMware management network. Make sure that the CIDR range doesn't overlap with any of your on-premises or cloud subnets.

  12. Click **Review and create**.

  13. Review the settings. To change any settings, click **Back**.

  14. Click **Create** to begin creating the stretched private cloud.

  15. Optional: If you want to list stretched private cloud details and cluster data to confirm the creation of the new stretched private cloud, start on the **Private clouds** details page. This page contains private cloud details. Clicking the **Clusters** tab displays cluster data in the table.




###  gcloud 

To create stretched private cloud that contains storage-only nodes using the Google Cloud CLI, do the following:

  1. Create a stretched private cloud by entering the [`gcloud private-clouds create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create):
         
         gcloud vmware private-clouds create STRETCHED_PC_STORAGE_NODE_NAME \
          --description=DESCRIPTION \
          --location=REGION \
          --cluster=STRETCHED_CLUSTER_NAME \
          --node-type-config=type=standard-72,count=n \
          --node-type-config=type=storage-only-standard-72,count=m \
          --management-range=IP_ADDRESS \
          --vmware-engine-network=NETWORK_NAME
          --preferred-zone=projects/PROJECT_ID/locations/PREFERRED_ZONE \
          --secondary-zone=projects/PROJECT_ID/locations/SECONDARY_ZONE \
          --type=STRETCHED

Replace the following:

     * `STRETCHED_PC_STORAGE_NODE_NAME`: the name for the stretched private cloud with storage-only node.
     * `DESCRIPTION`: the description for this private cloud.
     * `REGION`: the region for this private cloud.
     * `STRETCHED_CLUSTER_NAME`: the name for the new cluster in this private cloud.
     * `n`: the total number of standard nodes, an even number, in the primary cluster of this private cloud.
     * `m`: the total number of storage-only nodes, an even number, in the primary cluster of this private cloud.
     * `IP_ADDRESS`: the IP address and range for this private cloud, for example `192.168.0.0/22`.
     * `NETWORK_NAME`: the name for the network.
     * `PROJECT_ID`: the project ID for the request.
     * `SECONDARY_ZONE`: the secondary zone for the request.
     * `PREFERRED_ZONE`: the preferred zone for the request.
  2. Optional: To confirm creation of the stretched private cloud and the number of standard and storage-only nodes, use the [`gcloud vmware private-clouds describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/describe) and [`gcloud vmware private-clouds clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/describe) commands, respectively:
         
         gcloud vmware private-clouds describe STRETCHED_PC_STORAGE_NODE_NAME \
          --location=REGION

Replace the following:

     * `STRETCHED_PC_STORAGE_NODE_NAME`: the name for the stretched private cloud.
     * `REGION`: the region for this private cloud.
    
    gcloud vmware private-clouds clusters describe STRETCHED_CLUSTER_NAME \
     --location=REGION \
     --project=PROJECT_ID \
     --private-cloud=STRETCHED_PC_STORAGE_NODE_NAME

Replace the following:

     * `STRETCHED_CLUSTER_NAME`: the name of the stretched cluster in this private cloud.
     * `REGION`: the region for this private cloud.
     * `PROJECT_ID`: the project ID for the request.
     * `STRETCHED_PC_STORAGE_NODE_NAME`: the name for the stretched private cloud.



###  API 

To create stretched private cloud that contains storage-only nodes using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds?alt=json&privateCloudId=PC_STORAGE_ONLY_NODE_NAME" -d '{
      "description": "DESCRIPTION",
      "managementCluster": {
         "clusterId": "CLUSTER_NAME",
         "nodeTypeConfigs": {
            "standard-72": {
               "nodeCount": n
            },
            "storage-only-standard-72": {
               "nodeCount": m
            }
         }
         },
         "networkConfig": {
            "managementCidr": "IP_ADDRESS",
            "vmwareEngineNetwork": "projects/PROJECT_ID/locations/ZONE/vmwareEngineNetworks/NETWORK_NAME"
          }
         }'

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the zone for this private cloud.
  * `PC_STORAGE_NODE_NAME`: the name for the private cloud with storage-only node.
  * `DESCRIPTION`: the description for this private cloud.
  * `CLUSTER_NAME`: the name for the new cluster in this private cloud.
  * `n`: the total number of standard nodes, an even number, in the primary cluster of this private cloud.
  * `m`: the total number of storage-only nodes, an even number, in the primary cluster of this private cloud.
  * `IP_ADDRESS`: the IP address and range for this private cloud, for example `192.168.0.0/22`.
  * `NETWORK_NAME`: the name for the network.



## Expand or shrink a stretched cluster with storage-only nodes

You can expand or shrink a stretched cluster by adding or removing storage-only nodes using the Google Cloud console, Google Cloud CLI, or VMware Engine API by doing the following:

###  Console 

To expand or shrink a stretched cluster with storage-only nodes using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the stretched private cloud you want to expand or shrink.

  3. Click the **Cluster** tab.

  4. Click the name of the stretched cluster you want to expand or shrink.

  5. Click **Edit**.

  6. Under **Node configuration** , select a storage node model and increase or decrease the existing node count.

  7. Click **Save**.




###  gcloud 

To expand or shrink a stretched cluster by adding or removing storage-only nodes using the Google Cloud CLI, use the [`gcloud vmware private-clouds clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update):
    
    
      gcloud vmware private-clouds clusters update STRETCHED_CLUSTER_NAME \
         --location=REGION \
         --project=PROJECT_ID \
         --private-cloud=STRETCHED_PC_STORAGE_NODE_NAME \
         --node-type-config=type=standard-72,count=n \
         --node-type-config=type=storage-only-standard-72,count=m

Replace the following:

  * `STRETCHED_CLUSTER_NAME`: the name of the stretched cluster in this private cloud.
  * `REGION`: the region for this private cloud.
  * `PROJECT_ID`: the project ID for the request.
  * `STRETCHED_PC_STORAGE_NODE_NAME`: the name of the private cloud.
  * `n`: the new total number of standard nodes, an even number, for this specified cluster.
  * `m`: the new total number of storage-only nodes, an even number, for this specified cluster.



###  API 

To expand or shrink a stretched cluster by adding or removing storage-only nodes using the VMware Engine API, make a `PATCH` request:
    
    
    PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/STRETCHED_PC_STORAGE_NODE_NAME/clusters/STRETCHED_CLUSTER_NAME" -d '{
      "nodeTypeConfigs": {
         "standard-72": {
            "nodeCount": n
         },
         "storage-only-standard-72": {
            "nodeCount": m
         }
       }
      }'

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `REGION`: the region for this private cloud.
  * `STRETCHED_PC_STORAGE_NODE_NAME`: the name of the stretched private cloud.
  * `STRETCHED_CLUSTER_NAME`: the name of the stretched cluster in this private cloud.
  * `n`: the new total number of standard nodes, an even number, for this specified cluster.
  * `m`: the new total number of storage-only nodes, an even number, for this specified cluster.



## What's next

  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
