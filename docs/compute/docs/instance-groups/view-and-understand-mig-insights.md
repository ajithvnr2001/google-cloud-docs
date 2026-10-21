---
url: https://docs.cloud.google.com/compute/docs/instance-groups/view-and-understand-mig-insights/
title: View and understand MIG insights \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:16.599986+00:00
---

# View and understand MIG insights  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/view-and-understand-mig-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View and understand MIG insights Stay organized with collections  Save and categorize content based on your preferences. 

Managed instance group (MIG) insights help you understand the CPU and memory usage of the virtual machine (VM) instances that are part of your MIG. These insights are generated automatically based on system metrics or metrics gathered by the Cloud Monitoring service. You can use these insights to support decisions about resizing your MIG's machine type to more efficiently use VM resources.

For more information about insights, see [Insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## View insights for MIG recommendations

Compute Engine generates [machine type recommendations](https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups) based on resource [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights). By viewing insights associated with a specific MIG, you can learn more about the CPU and memory usage for your MIG.

To view the insights that generated a specific recommendation, use the gcloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeInstanceGroupManagerCpuUsageInsights.get` on the project
  * `recommender.computeInstanceGroupManagerCpuUsageInsights.list` on the project
  * `recommender.computeInstanceGroupManagerCpuUsagePredictionInsights.get` on the project
  * `recommender.computeInstanceGroupManagerCpuUsagePredictionInsights.list` on the project
  * `recommender.computeInstanceGroupManagerCpuUsageTrendInsights.get` on the project
  * `recommender.computeInstanceGroupManagerCpuUsageTrendInsights.list` on the project
  * `recommender.computeInstanceGroupManagerMemoryUsageInsights.get` on the project
  * `recommender.computeInstanceGroupManagerMemoryUsageInsights.list` on the project
  * `recommender.computeInstanceGroupManagerMemoryUsagePredictionInsights.get` on the project
  * `recommender.computeInstanceGroupManagerMemoryUsagePredictionInsights.list` on the project



###  gcloud 

To view all the available insights in detail for a specific zone, use the [`insights list` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list).
    
    
    gcloud recommender insights list --project=PROJECT_ID \
      --location=LOCATION \
      --insight-type=INSIGHT_TYPE_ID \
      --format=FORMAT
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the zone that contains the resources for which you want to view insights.
  * `INSIGHT_TYPE_ID`: the id of the [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types). For a list of the VM insights available, see Types of MIG insights.
  * `FORMAT`: your preferred output [format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats)–for example, `json`.



A typical output of the `insights list` command using the `json` output format might look like the following.
    
    
    [
      {
        "name": "projects/PROJECT_ID/locations/us-central1-a/insightTypes/google.compute.instanceGroupManager.CpuUsagePredictionInsight/insights/0ec21a13-bb04-3121-7321-dc43a11cc3e3",
        "description": "Predicted CPU usage is 1.5 vCPUs.",
        "targetResources": [
          "//compute.googleapis.com/projects/PROJECT_ID/zones/us-central1-a/instanceGroupManagers/test-instance"
        ],
        "insightSubtype": "CPU_USAGE_PREDICTION",
        "lastRefreshTime": "2021-09-15T06:50:45Z",
        "observationPeriod": "14 days",
        "stateInfo": {
          "state": "ACTIVE"
        },
        "content": {
          "predictedCpuCores": 1.5
        },
        "category": "PERFORMANCE",
        "etag": "fds421j2340",
        "associatedRecommendations": [
          {
             "recommendation": "projects/PROJECT_ID/locations/us-central1-a/recommenders/google.compute.instanceGroupManager.MachineTypeRecommender/recommendations/0fd31b24-cc05-4132-8431-ed54a22dd4f1"
          }
        ]
      }
    ]
    

###  REST 

To view all the available insights in detail for a specific zone, use the [`insights.list` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list).
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE_ID/insights
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the zone that contains the resources for which you want to view insights.
  * `INSIGHT_TYPE_ID`: the id of the [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types). For a list of the VM insights available, see Types of MIG insights.



A typical output of the `insights.list` method might look like the following.
    
    
    [
      {
        "name": "projects/PROJECT_ID/locations/us-central1-a/insightTypes/google.compute.instanceGroupManager.CpuUsagePredictionInsight/insights/0ec21a13-bb04-3121-7321-dc43a11cc3e3",
        "description": "Predicted CPU usage is 1.5 vCPUs.",
        "targetResources": [
          "//compute.googleapis.com/projects/PROJECT_ID/zones/us-central1-a/instanceGroupManagers/test-instance"
        ],
        "insightSubtype": "CPU_USAGE_PREDICTION",
        "lastRefreshTime": "2021-09-15T06:50:45Z",
        "observationPeriod": "14 days",
        "stateInfo": {
          "state": "ACTIVE"
        },
        "content": {
          "predictedCpuCores": 1.5
        },
        "category": "PERFORMANCE",
        "etag": "fds421j2340",
        "associatedRecommendations": [
          {
             "recommendation": "projects/PROJECT_ID/locations/us-central1-a/recommenders/google.compute.instanceGroupManager.MachineTypeRecommender/recommendations/0fd31b24-cc05-4132-8431-ed54a22dd4f1"
          }
        ]
      }
    ]
    

For more information about insights, see the [reference docs](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights).

## Types of MIG insights

You can use different insights to retrieve information about the performance of your MIGs. Each insight type has specific content attributes.

The following sections provide a reference for the MIG insights available.

### CPU usage insight

Compute Engine creates CPU usage insights when the CPU usage of your MIGs has been higher or lower than usual for the last observation period.

The insight type ID is `google.compute.instanceGroupManager.CpuUsageInsight`.

The available subtypes are:

  * `HIGH_CPU_USAGE`
  * `LOW_CPU_USAGE`



These are associated with insight descriptions such as the following:

  * `In the last 7 days for 80% of the time, CPU usage was greater than or equal to 83% for the least utilized VM instance. In the last 7 days for 80% of the time, CPU usage was greater than or equal to 93% for the most utilized VM instance.`
  * `In the last 7 days for 80% of the time, CPU usage was lower than or equal to 10% for the most utilized VM instance. In the last 7 days for 80% of the time, CPU usage was lower than or equal to 3% for the least utilized VM instance.`



The following table provides some details about the content associated with CPU usage insights. 

**Attribute** | **Type** | **Description**  
---|---|---  
`pointsForLeastUtilizedVm` | ARRAY | Array of objects. Each object contains the following properties:  


  * `sampleProbability`: (DOUBLE) Relative amount of CPU usage samples below the quantile function value.
  * `quantileFunctionValue`: (DOUBLE) Upper bound for CPU usage which holds at least part (sample probability) of samples.  The value represents the ratio of the total amount of vCPUs, and is in the range [0, 1].

  
`pointsForMostUtilizedVm` | ARRAY | Array of objects. Each object contains the following properties:  


  * `sampleProbability`: (DOUBLE) Relative amount of CPU usage samples below quantile function value.
  * `quantileFunctionValue`: (DOUBLE) Upper bound for CPU usage which holds at least part (sample probability) of samples.  The value represents the ratio of the total amount of vCPUs, and is in the range [0, 1].

  
  
### CPU usage prediction insight

Compute Engine creates CPU usage prediction insights to indicate the predicted CPU usage for the following day.

The insight type ID is `google.compute.instanceGroupManager.CpuUsagePredictionInsight`.

A typical description you can find in this insight is similar to the following:

  * `Predicted CPU usage of a single instance is 1.5 vCPUs.`



The following table provides some details about the content associated with CPU usage prediction insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`predicted_cpu_cores` | DOUBLE  | Predicted amount of CPU cores.   
  
### CPU usage trend insight

Compute Engine creates CPU usage trend insights when CPU usage shows an increasing or decreasing trend in the last observation period.

The insight type ID is `google.compute.instanceGroupManager.CpuUsageTrendInsight`.

The available subtypes are:

  * `CPU_USAGE_INCREASE`
  * `CPU_USAGE_DECREASE`



These are generally associated with insight descriptions such as the following:

  * `In the last 7 days, average daily CPU usage has increased by 8% from 65% to 73%.`
  * `In the last 7 days, average daily CPU usage has decreased by 10% from 55% to 45%.`



The following table provides some details about the content associated with CPU usage trend insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`cpu_usage_percentage_at_start` | DOUBLE  | **Measured** daily mean of CPU usage at the start of the observation period.  The value represents the percentage of the total number of vCPUs, and is in the range [0, 100].   
`cpu_usage_percentage_at_end` | DOUBLE  | **Measured** daily mean of CPU usage at the end of the observation period.  The value represents the percentage of the total number of vCPUs, and is in the range [0, 100].   
`cpu_usage_percentage_change` | DOUBLE  | **Predicted** change of daily mean of CPU usage during the observation period.  Prediction uses linear regression to model the change of daily CPU usage.  The value represents the percentage of the total number of vCPUs, and is in the range [0, 100].   
  
### Memory usage insight

Compute Engine creates memory usage insights if the memory usage is exceptionally high or low during the observation period.

The insight type ID is `google.compute.instanceGroupManager.MemoryUsageInsight`.

**Note:** You can receive memory usage insights only if you install Cloud Monitoring in your VMs. For more information, see [Installing Cloud Monitoring](https://docs.cloud.google.com/monitoring/agent/monitoring/installation).

The available subtypes are:

  * `HIGH_MEMORY_USAGE`
  * `LOW_MEMORY_USAGE`



These are generally associated with insight descriptions such as the following:

  * `In the last 12 days for 80% of the time, memory usage was greater than or equal to 64%.`
  * `In the last 7 days for 50% of the time, memory usage was lower than or equal to 10%.`



The following table provides some details about the content associated with memory usage insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`sample_probability` | DOUBLE  | Relative amount of memory usage samples below quantile function value.  The value is in the range [0, 1].   
`quantile_function_lowest_value` | DOUBLE  | Upper bound for memory usage which holds at least part (sample probability) of samples for the **least utilized** VM.  The value represents the ratio of the total amount of memory, and is in the range [0, 1].   
`quantile_function_highest_value` | DOUBLE  | Upper bound for memory usage which holds at least part (sample probability) of samples for the **most utilized** VM.  The value represents the ratio of the total amount of memory, and is in the range [0, 1].   
  
### Memory usage prediction insight

Compute Engine creates memory usage prediction insights to indicate the memory usage predicted for the following day.

**Note:** You can receive memory usage insights only if you install Cloud Monitoring in your VMs.

The insight type ID is `google.compute.instanceGroupManager.MemoryUsagePredictionInsight`.

A typical insight description is the following:

  * `Predicted memory usage is 1536 MB.`



The following table provides some details about the content associated with memory usage prediction insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`predicted_memory_mb` | DOUBLE  | Predicted amount of memory expressed in MB.   
  
## What's next

  * Learn more about [machine type recommendations](https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups) that Compute Engine creates based on insights.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
