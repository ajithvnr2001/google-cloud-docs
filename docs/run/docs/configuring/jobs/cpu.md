---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/cpu/
title: Configure CPU limits for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:23.453668+00:00
---

# Configure CPU limits for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure CPU limits for jobs Stay organized with collections  Save and categorize content based on your preferences. 

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

The minimum vCPU setting is 0.08 vCPU.

If you want to use less than 1 vCPU, you can select any value between 0.08 and 1, in increments of 0.001.

_If you use less than 1 vCPU_ , the following requirements are enforced:

Setting | Requirement  
---|---  
Memory | A minimum of 0.5 vCPU is needed to set a [memory limit](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits) greater than 512MiB.  
A minimum of 1 vCPU is needed to set a memory limit greater than 1GiB.  
Concurrency | [Maximum concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency) must be set to `1`.  
Billing | The [billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings) must be set to request-based billing.  
Containers | You must [deploy multiple containers (sidecars)](https://docs.cloud.google.com/run/docs/create-jobs#sidecars).  
  
### Cost considerations

The cost of your Cloud Run resource is impacted by its CPU configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which CPU configuration might be best for your resource:

  1. Establish an initial baseline configuration for a CPU limit that balances CPU utilization and costs.
  2. Monitor your CPU utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your CPU configuration as necessary.



If CPU utilization is consistently low under peak load, consider reducing vCPU allocation. If latency is high, consider increasing vCPU allocation.

You can view summary cost data, utilization data, and cost optimization recommendations for resources on the [Cloud Hub Optimization page](https://docs.cloud.google.com/hub/docs/optimize). Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure CPU limits

You must set a minimum of 1 CPU for a Cloud Run job.

You can configure CPU limits for a Cloud Run job using the Google Cloud console, the gcloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Containers** tab, select the CPU limit from the **CPU** list. Select a value of `1`, `2`, `4`, `6`, or `8` CPUs. Jobs require a minimum of 1 CPU. (See the table under Setting and updating CPU limits for required settings.).

  5. Click **Create** or **Update**.




###  gcloud 

  * To [set the CPU limits](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create) when you create a new job, run the following command:
        
        gcloud run jobs create JOB --image IMAGE_URL --cpu CPU

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * `CPU`: the CPU limit. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs. Jobs require a minimum of 1 CPU. (See the table under Setting and updating CPU limits for required settings.).
  * To [update the CPU limits](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) for an existing job, run the following command:
        
        gcloud run jobs update JOB --cpu CPU




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `cpu` attribute:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     resources:
                       limits:
                         cpu: CPU

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `CPU`: the CPU limit. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs. Jobs require a minimum of 1 CPU. (See the table under Setting and updating CPU limits for required settings.).
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB"
      location = "REGION"
      deletion_protection = false
    
      template {
        template {
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job"
            resources {
              limits = {
                cpu    = "CPU"
              }
            }
          }
        }
      }
    }
    

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `REGION`: the Google Cloud region. For example, `europe-west1`.
  * `CPU`: the CPU limit. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs. Jobs require a minimum of 1 CPU. (See the table under Setting and updating CPU limits for required settings.).



## View CPU settings

To view the current CPU settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the CPU setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the CPU setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
