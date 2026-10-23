---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/manual-scaling/
title: Manual scaling for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:23.245404+00:00
---

# Manual scaling for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/manual-scaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manual scaling for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to manually scale your worker pool.

## Overview

Manual scaling lets you set a specific instance count without requiring redeployment. This gives you the option to write your own scaling logic using an external system. See [Autoscale worker pools with external metrics](https://docs.cloud.google.com/run/docs/configuring/workerpools/crema-autoscaling) for an example of this.

## Billing considerations when using manual scaling

When you use manual scaling, all the instances that you requested are billed as _active_ instances, even if they happen to be idle. For complete billing details, see the [pricing page](https://cloud.google.com/run/pricing).

## Required roles

To get the permissions that you need to deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the Artifact Registry repository of the deployed container image (if applicable)



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure scaling

Changing scaling mode or changing the manual instance count does not create a new revision.

To configure the scaling mode, use the Google Cloud console, the Google Cloud CLI, YAML, Terraform, or REST API:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. If you are configuring a new worker pool, select **Worker pools** from the menu, and click **Deploy container**. If you are configuring an existing worker pool, click the worker pool to display its detail pane, then click the pen icon next to **Scaling** at the top right of the detail panel.

  3. Locate the **Scaling** form (for a new worker pool) or the **Edit scaling** form for an existing worker pool.

![image](https://docs.cloud.google.com/static/run/docs/images/edit-scaling.png)

  4. In the field labelled **Number of instances** , specify the number of container instances for the service.

  5. Finish the specification.

  6. Click **Create** for a new worker pool or **Save** for an existing worker pool.




###  gcloud 

To specify scaling for a new worker pool, use the [deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy) command:
    
    
    gcloud run worker-pools deploy WORKER_POOL \
        --instances=INSTANCE_COUNT \
        --image IMAGE_URL

Replace the following:

  * WORKER_POOL: the name of your worker pool.
  * INSTANCE_COUNT: the number of instances for the worker pool. This sets the worker pool to manual scaling. Specify a value of `0` to disable the worker pool. 
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.



Specify scaling for an existing worker pool by using the following [update](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update) command:
    
    
    gcloud run worker-pools update WORKER_POOL \
       --instances=INSTANCE_COUNT

### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           annotations:
             run.googleapis.com/manualInstanceCount: `INSTANCE_COUNT`

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * INSTANCE_COUNT: the number of instances you are manually scaling for the worker pool. Specify a value of `0` to disable the worker pool.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
      scaling {
        scaling_mode = "MANUAL"
        manual_instance_count = "INSTANCE_COUNT"
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * INSTANCE_COUNT: the number of instances for the worker pool. This sets the worker pool to manual scaling. Specify a value of `0` to disable the worker pool.



###  REST API

To update the number of instances for a given worker pool, send a `PATCH` HTTP request to the Cloud Run Admin API [`workerPools` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/patch).

For example, using `curl`:
    
    
        curl -H "Content-Type: application/json" \
        -H "Authorization: Bearer ACCESS_TOKEN" \
        -X PATCH \
        -d '{"scaling":{"manualInstanceCount":INSTANCE_COUNT }}' \
        https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/workerPools/WORKER_POOL?update_mask=scaling.manualInstanceCount

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to update a worker pool](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into `gcloud`, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * INSTANCE_COUNT: the number of instances for the worker pool.
  * PROJECT_ID: the Google Cloud project ID.
  * REGION: the Google Cloud region that the worker pool is deployed in.
  * WORKER_POOL: the name of the worker pool.



## View scaling configuration for a worker pool

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Click **Worker pools** to display the list of deployed worker pools.

  3. Click the worker pool you want to examine to display its details pane.

  4. The current scaling setting is shown above the worker pools revision list: **Scaling: Manual (Instances: )**.


**Note:** You can also use the Google Cloud CLI command [`gcloud run worker-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/describe) to view configuration details.

## Disable a worker pool

To disable a worker pool, use the following command to set scaling to zero:
    
    
    gcloud run worker-pools update WORKER_POOL --instances=0

Replace WORKER_POOL with the name of your worker pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
