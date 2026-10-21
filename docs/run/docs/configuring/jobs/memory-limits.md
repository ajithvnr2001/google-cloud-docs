---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits/
title: Configure memory limits for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:01.962976+00:00
---

# Configure memory limits for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure memory limits for jobs Stay organized with collections  Save and categorize content based on your preferences. 

You can choose the amount of memory to provide for your Cloud Run job. This page describes how to specify the amount of memory available for your job.

## Understand memory usage

Cloud Run instances that exceed their allowed memory limit are terminated.

The available memory for your instance needs to be sufficient for:

  * Running the job executable, because the executable must be loaded to memory
  * Allocating memory in your job process
  * Writing files to the file system



The size of the deployed container image does not affect memory that is available for the instance.

## Set and update memory limits

You can set memory limits on Cloud Run jobs. By default, the memory allocated to each job is , and the memory allocated for a function is 256 MiB.

### Required memory when setting a CPU value

When setting a CPU value, the following memory is required:

CPUs | Memory required  
---|---  
1 vCPU | 512 MiB to 4 GiB  
2 vCPU | 512 MiB to 8 GiB  
4 vCPU | 2 to 16 GiB  
6 vCPU | 4 to 24 GiB  
8 vCPU | 4 to 32 GiB  
  
### Maximum amount of memory

The maximum amount of memory you can configure is 32 gibibyte (`32 Gi`).

### Minimum memory

The minimum memory setting is 512 MiB.

### Cost considerations

The cost of your Cloud Run job is impacted by its memory configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which memory configuration might be best for your resource:

  1. Establish an initial baseline configuration.
  2. Monitor your memory utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your configuration as necessary.



If memory utilization is consistently low, consider reducing the allocated memory. If latency is high and memory utilization is near 100%, consider increasing the allocated memory. If you are experiencing Out of Memory (OOM) errors, you should increase the allocated memory or modify your application to prevent memory leaks and use less memory. See the [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards) to better understand your memory utilization.

Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure memory limits

You must specify a minimum of 512Mi for a Cloud Run job.

You can configure memory limits for a Cloud Run job using the Google Cloud console, the gcloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Containers** tab, select the memory size from the **Memory** list.

  5. Click **Create** or **Update**.




###  gcloud 

  * To set memory limits when you [create a new job](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create), run the following command:
        
        gcloud run jobs create JOB --image IMAGE_URL --memory SIZE

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * `SIZE`: the memory size. The format for size is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.
  * To set memory limits when you [update an existing job](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update), run the following command:
        
        gcloud run jobs update JOB --memory SIZE




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `memory` attribute:
         
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
                         memory: SIZE

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `SIZE`: the memory size, specifying a minimum of 512Mi. The format is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.

You can also specify more configuration such as environment variables or memory limits.

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
                cpu    = "2"
                memory = "SIZE"
              }
            }
          }
        }
      }
    }
    

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `REGION`: the Google Cloud region. For example, `europe-west1`.
  * `SIZE`: the required memory size, specifying a minimum of 512Mi. The format is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.



## View memory limit settings

To view the current memory limit settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the memory limit setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the memory limit setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
