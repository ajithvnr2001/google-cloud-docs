---
url: https://docs.cloud.google.com/run/docs/managing/workerpools/
title: Manage worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:42.272205+00:00
---

# Manage worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/managing/workerpools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manage worker pools Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run lets you view details, disable active worker pools, or delete the ones that you don't need. You can check deployed configurations, stop running instances, and remove unused resources.

### Required roles

To get the permissions that you need to manage Cloud Run worker pools and worker pool revisions, ask your administrator to grant you the [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) IAM role on your Cloud Run worker pool. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a worker pool

Cloud Run creates a new worker pool the first time you deploy a container image. See [Deploy a new worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools#worker-pool) for more instructions.

## View the list of worker pools in your project

Use the Google Cloud console or the Google Cloud CLI to view a list of the available worker pools in your project:

### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu. The available worker pools are listed in the page.




###  gcloud 

To list the worker pools in your project, run the following command:
    
    
    gcloud run worker-pools list
    

You can filter this list by properties of the worker pool definition, such as an [assigned label](https://docs.cloud.google.com/run/docs/configuring/workerpools/labels#label-listing).

### Client libraries

To view a list of worker pools from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_WorkerPoolsClient_ListWorkerPools)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.WorkerPoolsClient#com_google_cloud_run_v2_WorkerPoolsClient_listWorkerPools_com_google_cloud_run_v2_ListWorkerPoolsRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.workerpoolsclient#_google_cloud_run_v2_WorkerPoolsClient_listWorkerPools_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.worker_pools.WorkerPoolsClient#google_cloud_run_v2_services_worker_pools_WorkerPoolsClient_list_worker_pools)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-WorkerPools-Client#Google__Cloud__Run__V2__WorkerPools__Client_list_worker_pools_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.WorkerPoolsClient#_Google_Cloud_Run_V2_Client_WorkerPoolsClient__listWorkerPools__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.WorkerPoolsClient#Google_Cloud_Run_V2_WorkerPoolsClient_ListWorkerPools_Google_Cloud_Run_V2_ListWorkerPoolsRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view the list of worker pools in your project, send a `GET` HTTP request to the Cloud Run Admin API [`workerPool` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/list).

For example, using `curl`:
    
    
    curl -H "Authorization: Bearer ACCESS_TOKEN" \
       -X GET \
       https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to view worker pools](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * PROJECT_ID: the Google Cloud project ID.
  * REGION: the Google Cloud region of the worker pools.



## View more details about a worker pool

Use the Google Cloud console, Google Cloud CLI, or YAML to see more details about a worker pool:

### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu to display the available worker pools.

  3. Click the worker pool to display its details pane.




###  gcloud 

To view details about a worker pool: 
    
    
    gcloud run worker-pools describe WORKER_POOL

Replace WORKER_POOL with the name of the worker pool. 

You can use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--format) to format the output. For example, to format the output as YAML:
    
    
    gcloud run worker-pools describe WORKER_POOL
        --region REGION
        --format yaml

Replace:

  * WORKER_POOL with the name of the worker pool.
  * REGION with the Google Cloud region of the worker pool.



### YAML

To view details about a worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
    
    
    gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

### Client libraries

To view details about a worker pool from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_WorkerPoolsClient_GetWorkerPool)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.WorkerPoolsClient#com_google_cloud_run_v2_WorkerPoolsClient_getWorkerPool_com_google_cloud_run_v2_GetWorkerPoolRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.workerpoolsclient#_google_cloud_run_v2_WorkerPoolsClient_getWorkerPool_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.worker_pools.WorkerPoolsClient#google_cloud_run_v2_services_worker_pools_WorkerPoolsClient_get_worker_pool)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-WorkerPools-Client#Google__Cloud__Run__V2__WorkerPools__Client_get_worker_pool_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.WorkerPoolsClient#_Google_Cloud_Run_V2_Client_WorkerPoolsClient__getWorkerPool__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.WorkerPoolsClient#Google_Cloud_Run_V2_WorkerPoolsClient_GetWorkerPool_Google_Cloud_Run_V2_GetWorkerPoolRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To view details about a worker pool, send a `GET` HTTP request to the Cloud Run Admin API [`workerPool` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/get).

For example, using `curl`:
    
    
    curl -H "Authorization: Bearer ACCESS_TOKEN" \
       -X GET \
       https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to view worker pool details](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * PROJECT_ID: the Google Cloud project ID.
  * REGION: the Google Cloud region of the worker pool.
  * WORKER_POOL: the name of the worker pool.



## Disable an existing worker pool

Disabling a worker pool shuts down all instances for that worker pool. To disable a worker pool, set scaling to zero:

### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu, then from the list of worker pools, click on the worker pool you want to disable.

  3. Click the pen icon at the right of **Scaling: Manual (Instances: )** and change the value to 0.

  4. Click **Save** to update and disable the worker pool.




###  gcloud 
    
    
    gcloud run worker-pools update WORKER_POOL --instances=0

Replace WORKER_POOL with the name of your worker pool.

### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Set scale to a value of `0` to disable the worker pool. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           annotations:
             run.googleapis.com/scalingMode: manual
             run.googleapis.com/manualInstanceCount: `0`

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Client libraries

To disable a worker pool from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_WorkerPoolsClient_UpdateWorkerPool)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.WorkerPoolsClient#com_google_cloud_run_v2_WorkerPoolsClient_updateWorkerPoolAsync_com_google_cloud_run_v2_UpdateWorkerPoolRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.workerpoolsclient#_google_cloud_run_v2_WorkerPoolsClient_updateWorkerPool_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.worker_pools.WorkerPoolsClient#google_cloud_run_v2_services_worker_pools_WorkerPoolsClient_update_worker_pool)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-WorkerPools-Client#Google__Cloud__Run__V2__WorkerPools__Client_update_worker_pool_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.WorkerPoolsClient#_Google_Cloud_Run_V2_Client_WorkerPoolsClient__updateWorkerPool__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.WorkerPoolsClient#Google_Cloud_Run_V2_WorkerPoolsClient_UpdateWorkerPool_Google_Cloud_Run_V2_UpdateWorkerPoolRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To disable a worker pool, send a `PATCH` HTTP request to the Cloud Run Admin API [`workerPool` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/patch).

For example, using `curl`:
    
    
    curl -H "Authorization: Bearer ACCESS_TOKEN" \
       -H "Content-Type: application/json" \
       -X PATCH \
       -d '{"scaling":{"manualInstanceCount":0}}' \
       https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL?update_mask=scaling.manualInstanceCount

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to disable a worker pool](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * PROJECT_ID: the Google Cloud project ID.
  * REGION: the Google Cloud region of the worker pool.
  * WORKER_POOL: the name of your worker pool.



## Delete existing worker pools

The following considerations apply to deleting a worker pool:

  * Deleting a worker pool deletes all resources related to this worker pool, including all revisions of this worker pool whether they are processing workloads or not.
  * Deleting a worker pool does not automatically remove container images from Artifact Registry. To delete container images used by the deleted revisions from Artifact Registry, refer to [Deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).
  * After you delete a worker pool, the worker pool remains visible in the Google Cloud CLI until the deletion is fully complete. However, you cannot update the worker pool.
  * Deleting a worker pool is permanent. There is no undo or restore.




### console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu, then from the list of worker pools, select the worker pool you want to delete.

  3. Click **Delete**.




###  gcloud 

To delete a worker pool, use the command:
    
    
    gcloud run worker-pools delete WORKER_POOL --region REGION

Replace:

  * WORKER_POOL with the name of your worker pool.
  * REGION with the Google Cloud region of the worker pool.



### Client libraries

To delete a worker pool from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_WorkerPoolsClient_DeleteWorkerPool)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.WorkerPoolsClient#com_google_cloud_run_v2_WorkerPoolsClient_deleteWorkerPoolAsync_com_google_cloud_run_v2_DeleteWorkerPoolRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.workerpoolsclient#_google_cloud_run_v2_WorkerPoolsClient_deleteWorkerPool_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.worker_pools.WorkerPoolsClient#google_cloud_run_v2_services_worker_pools_WorkerPoolsClient_delete_worker_pool)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-WorkerPools-Client#Google__Cloud__Run__V2__WorkerPools__Client_delete_worker_pool_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.WorkerPoolsClient#_Google_Cloud_Run_V2_Client_WorkerPoolsClient__deleteWorkerPool__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.WorkerPoolsClient#Google_Cloud_Run_V2_WorkerPoolsClient_DeleteWorkerPool_Google_Cloud_Run_V2_DeleteWorkerPoolRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To delete a worker pool, send a `DELETE` HTTP request to the Cloud Run Admin API [`workerPool` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/delete).

For example, using `curl`:
    
    
    curl -H "Authorization: Bearer ACCESS_TOKEN" \
       -X DELETE \
       https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to delete a worker pool](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * PROJECT_ID: the Google Cloud project ID.
  * REGION: the Google Cloud region of the worker pool.
  * WORKER_POOL: the name of your worker pool.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
