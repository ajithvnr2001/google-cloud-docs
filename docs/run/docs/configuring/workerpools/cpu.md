---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/cpu/
title: Configure CPU limits for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:43.647861+00:00
---

# Configure CPU limits for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure CPU limits for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

## Set and update vCPU limits

### vCPU and memory table

The following are memory requirements for vCPUs:

CPUs | Memory required  
---|---  
1 vCPU | 512 MiB to 4 GiB  
2 vCPU | 512 MiB to 8 GiB  
4 vCPU | 2 to 16 GiB  
6 vCPU | 4 to 24 GiB  
8 vCPU | 4 to 32 GiB  
  
Values greater than 1 must be integer values.

**Note:** When selecting a vCPU limit greater than 1 vCPU, consider your application's threading model. If your application is single-threaded, it may only fully utilize one vCPU.

### Maximum amount of vCPU

The maximum amount of vCPU you can configure is 8 vCPU.

### Minimum amount of vCPU

The minimum vCPU setting is 1 vCPU.

### Cost considerations

The cost of your Cloud Run resource is impacted by its CPU configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which CPU configuration might be best for your resource:

  1. Establish an initial baseline configuration for a CPU limit that balances CPU utilization and costs.
  2. Monitor your CPU utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your CPU configuration as necessary.



If CPU utilization is consistently low under peak load, consider reducing vCPU allocation. If latency is high, consider increasing vCPU allocation.

You can view summary cost data, utilization data, and cost optimization recommendations for resources on the [Cloud Hub Optimization page](https://docs.cloud.google.com/hub/docs/optimize). Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure CPU limits

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set CPU limits for a Cloud Run worker pool using the Google Cloud console, the Google Cloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Containers** tab.

  4. Select the CPU limit from the **CPU** list.

  5. Click **Create** or **Deploy**.




###  gcloud 

You can [update the CPU limits](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update) for a given worker pool by using the following command:
    
    
    gcloud run worker-pools update WORKER_POOL --cpu CPU

Replace

  * WORKER_POOL with the name of your worker pool
  * CPU with the CPU limit. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs, following the requirements shown in the CPU and memory table.



You can also set CPU during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy) using the command:
    
    
    gcloud run worker-pools deploy --image IMAGE_URL --cpu CPU

Replace

  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * CPU with the value `1`, `2`, `4`, `6`, or `8` CPUs, following the requirements shown in the CPU and memory table.



### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
                 resources:
                   limits:
                     cpu: `CPU`

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
     * CPU: the CPU limit value. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs, or for less than 1 CPU, specify a value from 0.08 to less than 1.00, in increments of 0.01. (See the table under Setting and updating CPU limits for required settings.)
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
          resources {
            limits = {
              cpu = "CPU"
            }
          }
        }
      }
    }
    

Replace:

  * WORKER_POOL with the name of the worker pool.
  * REGION with the Google Cloud region. For example, europe-west1.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * CPU with the value `1`, `2`, `4`, `6`, or `8` CPUs, following the requirements shown in the CPU and memory table.



## View CPU configuration for the worker pool

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Click **Worker pools** to display the list of deployed worker pools.

  3. Click the worker pool you want to examine to display its details pane.

  4. Click the **Containers** tab to display CPU configuration for the worker pool.


**Note:** You can also use the Google Cloud CLI command [`gcloud run worker-pools describe`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/describe) to view configuration details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
