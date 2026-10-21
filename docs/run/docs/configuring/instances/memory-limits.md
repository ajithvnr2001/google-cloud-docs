---
url: https://docs.cloud.google.com/run/docs/configuring/instances/memory-limits/
title: Configure memory limits for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:22.228621+00:00
---

# Configure memory limits for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/memory-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure memory limits for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can choose the amount of memory to provide for your Cloud Run instance. This page describes how to specify the amount of memory available for your instance.

## Understand memory usage

Cloud Run instances that exceed their allowed memory limit are terminated.

The available memory for your instance needs to be sufficient for:

  * Running the instance executable, because the executable must be loaded to memory
  * Allocating memory in your instance process
  * Writing files to the file system



The size of the deployed container image does not affect memory that is available for the instance.

## Set and update memory limits

You can set memory limits on Cloud Run instances. By default, the memory allocated to each instance is 2 GiB .

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

You can enforce a maximum memory limit by using [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints#memory-limit). 

### Minimum memory

The minimum memory setting is 512 MiB.

### Cost considerations

The cost of your Cloud Run instance is impacted by its memory configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which memory configuration might be best for your resource:

  1. Establish an initial baseline configuration.
  2. Monitor your memory utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your configuration as necessary.



If memory utilization is consistently low, consider reducing the allocated memory. If latency is high and memory utilization is near 100%, consider increasing the allocated memory. If you are experiencing Out of Memory (OOM) errors, you should increase the allocated memory or modify your application to prevent memory leaks and use less memory. See the [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards) to better understand your memory utilization.

Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure memory limits

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set memory limits for a Cloud Run instance using Google Cloud CLI or YAML:

###  gcloud 

You can [update the memory allocation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/update) of a given instance by using the following command:
    
    
    gcloud beta run instances update INSTANCE --memory SIZE

Replace the following:

  * INSTANCE: the name of your instance
  * SIZE: a memory size from the CPU and memory table. The format for size is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.



You can also set memory limits during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/deploy) using the command:
    
    
    gcloud beta run instances deploy --image IMAGE_URL --memory SIZE

Replace the following:

  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
  * SIZE: a memory size from the CPU and memory table. The format for size is a fixed or floating point number followed by a unit: G or M corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: Gi or Mi corresponding to gibibyte or mebibyte respectively.



### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - image: IMAGE_URL
             resources:
               limits:
                 memory: SIZE

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
     * SIZE: the chosen memory size. The format is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
