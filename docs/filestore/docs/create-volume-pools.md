---
url: https://docs.cloud.google.com/filestore/docs/create-volume-pools/
title: Create and manage volume pools \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:25.063500+00:00
---

# Create and manage volume pools  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/create-volume-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create and manage volume pools Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

A volume pool is the top-level regional resource that manages a shared pool of storage capacity and IOPS for your project and Virtual Private Cloud (VPC) network. Within a volume pool, you can provision up to 1 million independent, lightweight volumes for AI agent sandboxes, developer workspaces, or general multi-tenant workloads.

## Before you begin

Complete the prerequisites described in [Set up Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites).

## Create a volume pool

### REST API

To create a volume pool, send an HTTP `POST` request to the `volumePools.create` endpoint:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d '{
        "description": "Production volume pool for AI agent sandboxes",
        "network": "projects/PROJECT_ID/global/networks/VPC_NETWORK",
        "defaultVolumeQuotaMib": 2048,
        "labels": {
          "env": "production",
          "workload": "ai-sandboxes"
        }
      }' \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools?volumePoolId=VOLUME_POOL_ID"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region where the pool is deployed, such as `us-central1`.
  * `VOLUME_POOL_ID`: the identifier for the volume pool, matching `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.
  * `VPC_NETWORK`: the name of an existing VPC network.



### Request fields

The request body contains the following fields:

Field | Type | Required | Description  
---|---|---|---  
`network` | `string` | Required | The resource path of your VPC network, in the format: `projects/{project}/global/networks/{network}`. The network must have a valid PSC service connection policy.  
`defaultVolumeQuotaMib` | `int64` | Optional | The default quota per volume in MiB. The value must be between 100 MiB and 102400 MiB (100 GiB). The default value is 1024 MiB.  
`description` | `string` | Optional | A user-friendly description of the volume pool.  
`labels` | `map[string, string]` | Optional | Key-value pairs that allow you to organize and filter resources in Google Cloud.  
  
### Response

The method returns a long-running operation (LRO) object:
    
    
    {
      "name": "projects/my-project/locations/us-central1/operations/operation-1694000000000-abcde",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.filestore.v1beta1.OperationMetadata",
        "createTime": "2026-09-08T10:00:00.000Z",
        "target": "projects/my-project/locations/us-central1/volumePools/my-volume-pool",
        "verb": "create"
      },
      "done": false
    }
    

Poll the operation until `done` is `true`:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region where the volume pool is deployed, such as `us-central1`.
  * `OPERATION_ID`: the operation ID returned in the creation response.



When completed, the operation returns the `VolumePool` object with state `READY`.

## Manage volume pools

You can view details about existing volume pools, list pools within a region, update configurations such as labels and capacity quotas, or delete volume pools.

### REST API

In each of the following requests, replace:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region where the volume pool is deployed, such as `us-central1`.
  * `VOLUME_POOL_ID`: the identifier of the volume pool.



### Get information about a volume pool

To retrieve details about a specific volume pool:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID"
    

### List volume pools

To list all volume pools in a given region:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools"
    

### Update a volume pool

To update the description, labels, or default quota of an existing volume pool, send an HTTP `PATCH` request with an `updateMask` query parameter:
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID?updateMask=description,labels" \
      -d '{
        "description": "Updated pool description",
        "labels": {
          "env": "production",
          "owner": "platform-team"
        }
      }'
    

### Delete a volume pool

Before deleting a volume pool, you must delete all child volumes provisioned within the pool. To delete a volume pool:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID"
    

## Manage volumes using the REST API

**Note:** If you deploy workloads on GKE, you don't need to manually provision or manage volumes. The Filestore CSI driver and GKE orchestration automatically manage volume provisioning from your volume pool. For more information, see [Use Filestore agent volumes with GKE](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).

If you want to use Filestore agent volumes without GKE through your own orchestration platform for storage, you can provision and manage individual volumes directly using the REST API.

### REST API

In each of the following requests, replace:

  * `PROJECT_ID`: the Google Cloud project ID.
  * `LOCATION`: the region containing the parent volume pool.
  * `VOLUME_POOL_ID`: the identifier of the parent volume pool.
  * `VOLUME_ID`: the identifier for the volume, matching `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.



### Create a volume

To provision an individual volume inside a volume pool, send an HTTP `POST` request to the `volumes.create` endpoint:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes?volumeId=VOLUME_ID" \
      -d '{
        "description": "Dynamic tool scratchpad for Agent Worker 12",
        "labels": {
          "agent_id": "worker-12",
          "workflow": "code_eval"
        }
      }'
    

Volume provisioning completes in under one second. The API returns the `Volume` resource directly:
    
    
    {
      "name": "projects/my-project/locations/us-central1/volumePools/my-volume-pool/volumes/my-volume",
      "description": "Dynamic tool scratchpad for Agent Worker 12",
      "mountPoint": {
        "ipAddress": "10.128.0.45",
        "mountName": "my_volume"
      }
    }
    

Note the values returned inside `mountPoint`:

  * `ipAddress`: the internal IP address of the NFS mount endpoint within your VPC network.
  * `mountName`: the NFS export path component to mount.



### Get volume details

To view details for an existing volume, including its `mountPoint`:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID"
    

### List volumes in a pool

To list all volumes provisioned in a volume pool:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes"
    

### Delete a volume

When an agent session concludes or an ephemeral sandbox terminates, delete the volume to reclaim quota within the pool:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://file.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/volumePools/VOLUME_POOL_ID/volumes/VOLUME_ID"
    

## What's next

  * Set up [Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites).
  * Configure [GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
