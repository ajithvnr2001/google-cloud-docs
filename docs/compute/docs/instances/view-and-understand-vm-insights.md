---
url: https://docs.cloud.google.com/compute/docs/instances/view-and-understand-vm-insights/
title: View and understand VM instance insights \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:28.243776+00:00
---

# View and understand VM instance insights  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-and-understand-vm-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View and understand VM instance insights Stay organized with collections  Save and categorize content based on your preferences. 

Virtual machine (VM) instance insights help you understand the CPU, memory, and network usage of your Compute Engine VMs. Insights are generated automatically based on system metrics or metrics gathered by Cloud Monitoring. You can use insights to support decisions about resizing your machine types to more efficiently use VM resources.

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




## View insights for VM recommendations

Compute Engine generates recommendations based on resource [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights). Recommendations include [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) and [idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations).

By viewing insights associated with a specific VM, you can learn more about the CPU, memory, and network usage for your VM.

To view the insights that generated a specific recommendation, use the gcloud CLI or the API.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeInstanceCpuUsageInsights.get` on the project
  * `recommender.computeInstanceCpuUsageInsights.list` on the project
  * `recommender.computeInstanceCpuUsagePredictionInsights.get` on the project
  * `recommender.computeInstanceCpuUsagePredictionInsights.list` on the project
  * `recommender.computeInstanceCpuUsageTrendInsights.get` on the project
  * `recommender.computeInstanceCpuUsageTrendInsights.list` on the project
  * `recommender.computeInstanceMemoryUsageInsights.get` on the project
  * `recommender.computeInstanceMemoryUsageInsights.list` on the project
  * `recommender.computeInstanceMemoryUsagePredictionInsights.get` on the project
  * `recommender.computeInstanceMemoryUsagePredictionInsights.list` on the project
  * `recommender.computeInstanceNetworkThroughputInsights.get` on the project
  * `recommender.computeInstanceNetworkThroughputInsights.list` on the project



###  gcloud 

To view all the available insights in detail for a specific zone, use the [`insights list` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) and provide the `--format` option.
    
    
    gcloud recommender insights list --project=PROJECT_ID \
      --location=LOCATION \
      --insight-type=INSIGHT_TYPE_ID \
      --format=FORMAT
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the zone that contains the resources for which you want to view insights.
  * `INSIGHT_TYPE_ID`: the id of the [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types). For a list of the VM insights available, see Types of VM instance insights.
  * `FORMAT`: your preferred output [format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats)–for example, `json`.



A typical output of the `insights list` command using the `json` output format might look like the following.
    
    
    [
      {
        "associatedRecommendations": [
          {
            "recommendation": "projects/PROJECT_ID/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations/7618763b-fee2-42e5-8b9b-e6eee0b2077f"
          }
        ],
        "category": "PERFORMANCE",
        "content": {
          "predictedCpuCores": 0.15
        },
        "description": "Predicted CPU usage is 0.1 vCPUs.",
        "etag": "\"fdb51460cac758a0\"",
        "insightSubtype": "CPU_USAGE_PREDICTION",
        "lastRefreshTime": "2021-09-15T06:50:45Z",
        "name": "projects/PROJECT_ID/locations/us-central1-a/insightTypes/google.compute.instance.CpuUsagePredictionInsight/insights/cb2ab4e6-2c5e-4f0e-8cbe-1487e8bae8c0",
        "observationPeriod": "604800s",
        "severity": "LOW",
        "stateInfo": {
          "state": "ACTIVE"
        },
        "targetResources": [
          "//compute.googleapis.com/projects/PROJECT_ID/zones/us-central1-a/instances/instance-name-1"
        ]
      }
    ]
    

###  REST 

To view all the available insights in detail for a specific zone, use the [`insights.list` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list).
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE_ID/insights
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the zone that contains the resources for which you want to view insights.
  * `INSIGHT_TYPE_ID`: the id of the [insight Type](https://docs.cloud.google.com/recommender/docs/insights/insight-types). For a list of the VM insights available, see Types of VM instance insights.



A typical output of the `insights.list` method might look like the following.
    
    
    [
      {
        "associatedRecommendations": [
          {
            "recommendation": "projects/PROJECT_ID/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations/7618763b-fee2-42e5-8b9b-e6eee0b2077f"
          }
        ],
        "category": "PERFORMANCE",
        "content": {
          "predictedCpuCores": 0.15
        },
        "description": "Predicted CPU usage is 0.1 vCPUs.",
        "etag": "\"fdb51460cac758a0\"",
        "insightSubtype": "CPU_USAGE_PREDICTION",
        "lastRefreshTime": "2021-09-15T06:50:45Z",
        "name": "projects/PROJECT_ID/locations/us-central1-a/insightTypes/google.compute.instance.CpuUsagePredictionInsight/insights/cb2ab4e6-2c5e-4f0e-8cbe-1487e8bae8c0",
        "observationPeriod": "604800s",
        "severity": "LOW",
        "stateInfo": {
          "state": "ACTIVE"
        },
        "targetResources": [
          "//compute.googleapis.com/projects/PROJECT_ID/zones/us-central1-a/instances/instance-name-1"
        ]
      }
    ]
    

For more information about insights, see the [reference docs](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights).

## Types of VM instance insights

You can use different insights to retrieve information about the performance of your VMs. Each insight type has specific content attributes.

The following sections provide a reference for the VM insights available.

### CPU usage insight

Compute Engine creates CPU usage insights when the CPU usage of your VMs has been higher or lower than usual for the last observation period.

The insight type ID is `google.compute.instance.CpuUsageInsight`.

The available subtypes are:

  * `HIGH_CPU_USAGE`
  * `LOW_CPU_USAGE`



These are associated with insight descriptions such as the following:

  * `In the last 12 days for 90% of the time, CPU usage was greater than or equal to 83%.`
  * `In the last 10 days for 70% of the time, CPU usage was lower than or equal to 20%.`



The following table provides some details about the content associated with CPU usage insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`points` | ARRAY  | Array of objects. Each object contains the following properties:  


  * `sampleProbability`: (DOUBLE) Relative amount of CPU usage samples below quantile function value.
  * `quantileFunctionValue`: (DOUBLE) Upper bound for CPU usage which holds at least part (sample probability) of samples.  
The value represents the ratio of the total amount of vCPUs, and is in the range [0, 1].

  
  
### CPU usage prediction insight

Compute Engine creates CPU usage prediction insights to indicate the predicted CPU usage for the following day.

The insight type ID is `google.compute.instance.CpuUsagePredictionInsight`.

A typical description you can find in this insight is similar to the following:

  * `Predicted CPU usage is 0.1 vCPUs.`



The following table provides some details about the content associated with CPU usage prediction insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`predicted_cpu_cores` | DOUBLE  | Predicted amount of CPU cores.   
  
### CPU usage trend insight

Compute Engine creates CPU usage trend insights when CPU usage shows an increasing or decreasing trend in the last observation period.

The insight type ID is `google.compute.instance.CpuUsageTrendInsight`.

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

The insight type ID is `google.compute.instance.MemoryUsageInsight`.

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
`points` | ARRAY  |  Array of objects. Each object contains the following properties: 

  * `sampleProbability`: (DOUBLE) Relative amount of memory usage samples below quantile function value.
  * `quantileFunctionValue`: (DOUBLE) Upper bound for memory usage which holds at least part (sample probability) of samples.  
The value represents the ratio of the total amount of memory, and is in the range [0, 1].

  
  
### Memory usage prediction insight

Compute Engine creates memory usage prediction insights to indicate the memory usage predicted for the following day.

**Note:** You can receive memory usage insights only if you install Cloud Monitoring in your VMs.

The insight type ID is `google.compute.instance.MemoryUsagePredictionInsight`.

A typical insight description is the following:

  * `Predicted memory usage is 1536 MB.`



The following table provides some details about the content associated with memory usage prediction insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`predicted_memory_mb` | DOUBLE  | Predicted amount of memory expressed in MB.   
  
### Network throughput insight

Compute Engine creates network throughput insights when the network throughput during the observation period is exceptionally low for the incoming or outgoing traffic.

The insight type ID is `google.compute.instance.NetworkThroughputInsight`.

The available subtypes are:

  * `LOW_RECEIVED_NETWORK_THROUGHPUT`
  * `LOW_SENT_NETWORK_THROGHPUT`



These are generally associated with insight descriptions such as the following:

  * `In the last 7 days for 80% of the time, received network throughput was lower than or equal to 500 B/s.`
  * `In the last 7 days for 80% of the time, sent network throughput was lower than or equal to 200 B/s.`



The following table provides some details about the content associated with network throughput insights.

**Attribute** | **Type** | **Description**  
---|---|---  
`sample_probability` | DOUBLE  | Relative amount of network throughput samples below the quantile function value.  The value is in the range [0, 1].   
`quantile_function_value_in_bytes_per_second` | DOUBLE  | Upper bound for network throughput which holds at least part (sample probability) of samples. The value is expressed in bytes per second.   
  
## What's next

  * Learn more about [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) that Compute Engine creates based on insights.
  * Learn more about [idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
