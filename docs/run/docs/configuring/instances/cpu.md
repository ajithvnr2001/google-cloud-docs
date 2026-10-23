---
url: https://docs.cloud.google.com/run/docs/configuring/instances/cpu/
title: Configure CPU limits for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:03.277257+00:00
---

# Configure CPU limits for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure CPU limits for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to specify the number of vCPUs to use for each Cloud Run instance. By default, Cloud Run container instances are limited to 2 vCPU. You can increase or decrease this value as described in this page. 

## Set and update vCPU limits

By default, each instance is set to 2 vCPU and 2 GiB for memory. You can change this to any of the values shown in the following table.

Concurrency is not configurable, it is set to 80.

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

The minimum vCPU for the instance is 1 vCPU. While each container can be configured with fractional CPUs, the sum of all containers in the instance must be greater than or equal to 1 vCPU.

### Cost considerations

The cost of your Cloud Run resource is impacted by its CPU configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which CPU configuration might be best for your resource:

  1. Establish an initial baseline configuration for a CPU limit that balances CPU utilization and costs.
  2. Monitor your CPU utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your CPU configuration as necessary.



If CPU utilization is consistently low under peak load, consider reducing vCPU allocation. If latency is high, consider increasing vCPU allocation.

You can view summary cost data, utilization data, and cost optimization recommendations for resources on the [Cloud Hub Optimization page](https://docs.cloud.google.com/hub/docs/optimize). Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## CPU Burst and Throttling

Cloud Run instances use a shared CPU allocation model with baseline quotas and bursting capability, managed similarly to Linux scheduler `cgroup` allocation.

When you configure vCPU limits for a Cloud Run instance, the CPU behavior consists of the following mechanisms:

  * **Baseline quota:** Each instance is allocated a continuous baseline of 6.25% (1/16th) per configured vCPU. You can run your instance within this baseline indefinitely.
  * **Burst capacity:** When your instance runs below its baseline capacity, it continuously accrues unused CPU time into a burst balance budget (up to 500 seconds). When your workload triggers computationally intensive tasks, the instance automatically bursts up to 100% of its configured vCPU allocation until its accrued burst balance is depleted.
  * **Throttling:** Once the burst balance is exhausted during high CPU utilization, the instance is throttled back to its baseline quota (6.25% per configured vCPU) until additional burst balance is accrued.
  * **Replenishment:** The burst budget replenishes whenever CPU usage drops below the 6.25% baseline.



## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure CPU limits

You can set CPU limits for a Cloud Run instance using the Google Cloud CLI or YAML:

###  gcloud 

You can [update the CPU limits](https://docs.cloud.google.com/sdk/gcloud/reference/run/instances/update) for a given instance by using the following command:
    
    
    gcloud beta run instances update INSTANCE --cpu CPU

Replace the following:

  * INSTANCE: the name of your instance.
  * CPU: the CPU limit. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs, following the requirements shown in the CPU and memory table.



You can also set CPU during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/instances/deploy) using the command:
    
    
    gcloud beta run instances deploy --image IMAGE_URL --cpu CPU

Replace the following:

  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
  * CPU: the value `1`, `2`, `4`, `6`, or `8` CPUs, following the requirements shown in the CPU and memory table.



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
           — image: IMAGE_URL
           resources:
             limits:
               cpu: `CPU`

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
     * CPU: the CPU limit value. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs, or for less than 1 CPU, specify a value from 0.08 to less than 1.00, in increments of 0.01. (See the table under Setting and updating CPU limits for required settings.)
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




### Example scenario: 2 vCPU instance

If an instance is configured with a limit of 2 vCPU:

  1. **Baseline operation:** The instance can run consistently consuming up to 0.125 vCPU (6.25% of 2 vCPU). While operating under this baseline, it accrues burst balance.
  2. **Full burst:** When the workload requires additional processing power, the instance bursts up to the full 2 vCPU (100% utilization), consuming its accrued burst budget.
  3. **Throttling:** When the burst balance budget is exhausted, the instance is throttled back to the 0.125 vCPU baseline until it accrues new burst balance.



## View CPU configuration for the instance

You can use the Google Cloud CLI command [`gcloud beta run instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/run/instances/describe) to view configuration details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
