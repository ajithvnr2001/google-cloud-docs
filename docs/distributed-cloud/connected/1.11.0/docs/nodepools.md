---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/nodepools/
title: Create and manage node pools \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:01.144196+00:00
---

# Create and manage node pools  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/nodepools/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Create and manage node pools Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud node pool resources in a Distributed Cloud connected zone.

On Distributed Cloud connected servers, node pools are created and populated automatically when you create a cluster. You also have the option to configure additional node pools after you've created the cluster.

For more information about Distributed Cloud node pools, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

## Create a node pool

To create a Distributed Cloud node pool, complete the steps in this section.

To complete this task, you must have the following roles in your Google Cloud project:

  * [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`)
  * [Edge Container Machine User role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-machine-user) (`roles/edgecontainer.machineUser`)

You must also have this role on the Google Cloud project that contains the Distributed Cloud connected machines that will be assigned to this node pool if that project is different from the Google Cloud project in which you are creating the node pool.




###  Console 

If you are using the Google Cloud console, you can only create a node pool when you create a cluster. To create a standalone node pool, you must use the Google Cloud CLI or the Distributed Cloud Edge Container API.

###  gcloud 

Use the `gcloud edge-cloud container clusters node-pools create` command:
    
    
    gcloud edge-cloud container clusters node-pools create POOL_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME \
        --node-location=ZONE_NAME \
        --node-count=NODE_COUNT \
        --node-labels=NODE_LABELS \
        --machine-filter=MACHINE_FILTER \
        --local-disk-kms-key=POOL_KMS_KEY \
        --node-storage-schema=WORKER_NODE_STORAGE_SCHEMA
    

Replace the following:

  * `POOL_NAME`: a descriptive name that uniquely identifies this node pool. This name must be RFC 1213-compliant and consist only of lowercase alphanumeric characters and hyphens (`-`). It must begin and end with an alphanumeric character.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster for this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone. This zone must be in the region specified in `REGION`.
  * `NODE_COUNT`: the number of nodes that this node pool holds.
  * `NODE_LABELS`: a comma-delimited list of key-value pairs that comprise labels for the individual nodes in the node pool.
  * `MACHINE_FILTER` (optional): specifies the [filtering criteria](https://google.aip.dev/160) for machine selection. To see the fields by which you can filter, see [Get information about a machine](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/machines#machine-info). Only machines that match this filter are allowed to join this node pool. For multi-rack clusters, use this flag to specify the Distributed Cloud connected racks whose nodes comprise this node pool. If omitted, all available nodes in the zone are added to this node pool.
  * `POOL_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this node pool. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This flag only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/security#cmek).

  * `WORKER_NODE_STORAGE_SCHEMA` (optional): specifies the local storage schema for the worker nodes included in this node pool. For more information, see [Configure local storage schemas](https://docs.cloud.google.com/distributed-cloud/connected/docs/storage#schemas).




###  API 

Make a `POST` request to the `projects.locations.clusters.nodePools.create` method:
    
    
    POST /v1/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME?nodePoolId=NODEPOOL_ID&requestId=REQUEST_ID
    {
     "name": POOL_NAME,
     "labels": { LABELS,
      },
     "nodeLocation": ZONE_NAME,
     "nodeCount": NODE_COUNT,
     "nodeLabels": NODE_LABELS,
     "machineFilter": MACHINE_FILTER,
     "localDiskEncryption": {
       "kmsKey": POOL_KMS_KEY,
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster for this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `NODEPOOL_ID`: a unique programmatic ID that identifies this node pool resource.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `POOL_NAME`: a descriptive name that uniquely identifies this node pool.
  * `LABELS`: a list of labels to apply to this node pool resource.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone. This zone must be in the region specified in `REGION`.
  * `NODE_COUNT`: the number of nodes that this node pool holds.
  * `NODE_LABELS`: a comma-delimited list of key-value pairs that comprise labels for the individual nodes in the node pool.
  * `MACHINE_FILTER` (optional): specifies the [filtering criteria](https://google.aip.dev/160) for machine selection. Only machines that match this filter are allowed to join this node pool. For multi-rack clusters, use this flag to specify the Distributed Cloud connected racks whose nodes comprise this node pool. If omitted, all available nodes in the zone are added to this node pool.
  * `POOL_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this node pool. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This parameter only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/security#cmek).




## List node pools

To list the Distributed Cloud node pools available in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters node-pools list` command:
    
    
    gcloud edge-cloud container clusters node-pools list \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster has been created.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.



###  API 

Make a `GET` request to the `projects.locations.clusters.nodePools.list` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME/nodePools?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected cluster has been created.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud cluster.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a node pool

To get information about a Distributed Cloud node pool, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters node-pools describe` command:
    
    
    gcloud edge-cloud container clusters node-pools describe POOL_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME
    

Replace the following:

  * `POOL_NAME`: the name of the target node pool.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the Distributed Cloud connected cluster associated with this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.



###  API 

Make a `GET` request to the `projects.locations.clusters.nodePools.get` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME/nodePools/POOL_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the Distributed Cloud connected cluster associated with this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `POOL_NAME`: the name of the target node pool.



## Modify a node pool

To modify a Distributed Cloud node pool, complete the steps in this section.

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters node-pools update` command:
    
    
    gcloud edge-cloud container clusters node-pools update POOL_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME \
        --node-count=NODE_COUNT \
        --machine-filter=MACHINE_FILTER \
        --local-disk-kms-key=POOL_KMS_KEY
    

Replace the following:

  * `POOL_NAME`: the name of the target node pool.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the Distributed Cloud connected cluster associated with this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `NODE_COUNT`: the number of nodes that this node pool holds.
  * `MACHINE_FILTER` (optional): specifies the [filtering criteria](https://google.aip.dev/160) for machine selection. To see the fields by which you can filter, see [Get information about a machine](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/machines#machine-info). For multi-rack clusters, use this flag to specify the Distributed Cloud connected racks whose nodes comprise this node pool.
  * `POOL_KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this node pool. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This flag only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/security#cmek).

To revert a node pool to use a Google-owned and Google-managed encryption key, use the `--use-google-managed-key` flag.




###  API 

Make a `PATCH` request to the `projects.locations.clusters.nodePools.patch` method:
    
    
    PATCH /v1/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME?nodePoolId=NODEPOOL_ID&requestId=REQUEST_ID
    {
     "name": POOL_NAME,
     "labels": { LABELS,
      },
     "nodeLocation": ZONE_NAME,
     "nodeCount": NODE_COUNT,
     "machineFilter": MACHINE_FILTER,
     "localDiskEncryption": {
       "kmsKey": KMS_KEY,
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the Distributed Cloud connected cluster associated with this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `NODEPOOL_ID`: a unique programmatic ID that identifies this node pool.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `POOL_NAME`: a descriptive name that uniquely identifies this node pool.
  * `LABELS`: a list of labels to apply to this node pool resource.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone. This zone must be in the region specified in `REGION`.
  * `NODE_COUNT`: the number of nodes that this node pool holds.
  * `MACHINE_FILTER` (optional): specifies the [filtering criteria](https://google.aip.dev/160) for machine selection. Only machines that match this filter are allowed to join this node pool. For multi-rack clusters, use this flag to specify the Distributed Cloud connected racks whose nodes comprise this node pool.
  * `KMS_KEY` (optional): the full path to the Cloud KMS key that you want to use with this node pool. For example:
        
        /projects/myProject/locations/us-west1-a/keyRings/myKeyRing/cryptoKeys/myGDCE-Key
        

This parameter only applies if you have integrated Distributed Cloud connected with Cloud Key Management Service as described in [Enable support for customer-managed encryption keys (CMEK) for local storage](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/security#cmek).




## Delete a node pool

To delete a Distributed Cloud node pool, complete the steps in this section.

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container clusters node-pools delete` command:
    
    
    gcloud edge-cloud container clusters node-pools delete POOL_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME
    

Replace the following:

  * `POOL_NAME`: the name of the target node pool.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the Distributed Cloud connected cluster associated with this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.



###  API 

Make a `DELETE` request to the `projects.locations.clusters.nodePools.delete` method:
    
    
    DELETE /v1/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME/nodePools/POOL_NAME?requestId=REQUEST_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the Distributed Cloud connected cluster associated with this node pool is hosted.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `POOL_NAME`: the name of the target node pool.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/deploy)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/machines)
  * [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/clusters)
  * [Create and manage VPN connections](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/vpn-connections)
  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/virtual-machines)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/gpu)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
