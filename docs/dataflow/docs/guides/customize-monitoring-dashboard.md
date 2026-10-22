---
url: https://docs.cloud.google.com/dataflow/docs/guides/customize-monitoring-dashboard/
title: Customize the Dataflow monitoring dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:20.174520+00:00
---

# Customize the Dataflow monitoring dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/customize-monitoring-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Customize the Dataflow monitoring dashboard Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to customize the Dataflow [project monitoring dashboard](https://docs.cloud.google.com/dataflow/docs/guides/project-monitoring), by adding a graph that queries Cloud Monitoring metrics.

The project monitoring dashboard lets you monitor a collection of jobs and see their overall health and performance. The dashboard contains a default set of charts that are useful for most workloads. By customizing the dashboard, you can add charts that are specific to your business requirements.

## Example scenario

To show how you might customize the dashboard, assume that an organization wants to track the estimated cost of the top 25 jobs in their project.

For this scenario, assume that the jobs have the following characteristics:

  * The jobs are all streaming jobs.
  * The jobs use the [data-processed billing model](https://cloud.google.com/dataflow/pricing#compute-resources).
  * The jobs save files to [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types), both Standard (HDD) and SSD.
  * The jobs don't use GPUs.



## Choose metrics

The following metrics are needed to estimate the cost of a job, given the assumptions listed the previous section:

Resource| Relevant metric  
---|---  
CPU (vCPU per hour) |  [ `job/total_vcpu_time` ](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/total_vcpu_time)  
Memory (GB per hour) |  [ `job/total_memory_usage_time` ](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/total_memory_usage_time)  
Data processed during shuffle (GB) |  [ `job/total_streaming_data_processed` ](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/total_streaming_data_processed)  
Persistent Disk usage (GB per hour, Standard and SSD) |  [ `job/total_pd_usage_time` ](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/total_pd_usage_time)  
  
For more information, see [Dataflow pricing](https://cloud.google.com/dataflow/pricing).

**Important:** The actual cost to run a job depends on factors such as Dataflow pricing model, [committed use discounts (CUDs)](https://docs.cloud.google.com/dataflow/docs/cuds), and contractual discounts. Dataflow job metrics can give you a baseline for cost optimization, but the actual costs might differ.

To learn which resources are available in Monitoring, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources).

## Write a PromQL query

To query metrics from Cloud Monitoring, use [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql). This section shows how to write a PromQL query for the scenario by building it up from smaller clauses. This section doesn't assume any prior knowledge of PromQL. For more information, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

### Map metric names to PromQL strings

To use Monitoring metrics in PromQL queries, you must map the metric name to a PromQL string, as follows:

Metric name| PromQL string  
---|---  
`job/total_vcpu_time` | `dataflow_googleapis_com:job_total_vcpu_time`  
`job/total_memory_usage_time` | `dataflow_googleapis_com:job_total_memory_usage_time`  
`job/total_streaming_data_processed` |  `dataflow_googleapis_com:job_total_streaming_data_processed`  
`job/total_pd_usage_time` | `dataflow_googleapis_com:job_total_pd_usage_time`  
  
For more information, see [Mapping Cloud Monitoring metrics to PromQL](https://docs.cloud.google.com/monitoring/promql/promql-mapping).

### Build the query

To get the estimated cost, calculate the prices for each component based on the most current value of each metric. The metrics are sampled every 60 seconds, so to get the latest value, use a 1-minute windowing function and take the maximum value within each window.

  * To get the estimated CPU cost, first convert `job/total_vcpu_time` from seconds to hours. Multiply by CPU price per vCPU per hour.
        
        # ((vCPU time)[Bucket 1m] / Seconds per hour * vCPU Price)
        max_over_time(dataflow_googleapis_com:job_total_vcpu_time[1m]) / 3600 * CPU_PRICE
        

This formula gives the estimated CPU cost for all jobs in the project. To get the estimated CPU cost per job, use the `sum` aggregation operator and group by job ID.
        
        sum(
          max_over_time(dataflow_googleapis_com:job_total_vcpu_time[1m]) / 3600 * CPU_PRICE
        ) by (job_id)
        

  * To get the estimated memory cost, convert `job/total_memory_usage_time` from seconds to hours. Multiply by memory price per GB per hour and group by job ID.
        
        #((Memory time)[Bucket 1m] / Seconds per hour) * Memory Price
        sum(
          max_over_time(dataflow_googleapis_com:job_total_memory_usage_time[1m]) / 3600 * MEMORY_PRICE
        ) by (job_id)
        

  * To get the estimated shuffle cost, convert `job/total_streaming_data_processed` from bytes to GB. Multiply by the price of data processed during shuffle per GB and group by job ID.
        
        # Shuffle Billing. Reported once every 60 seconds, measured in bytes.
        # Formula: (Shuffle Data)[Bucket 1m] / (Bytes in GB) * (Shuffle Price)
        sum(
          max_over_time(
            dataflow_googleapis_com:job_total_streaming_data_processed[1m]
         ) / 1000000000 * SHUFFLE_PRICE
        ) by (job_id)
        

  * To get the estimated Persistent Disk usage cost, indexing on the `storage_type` label to separate by disk type (Standard or SSD). Convert each value from GB-seconds to GB-hours and group by job ID.
        
        # Formula: ((Standard PD time)[Bucket 1m] / Seconds per hour) * Standard PD price
        sum(
          max_over_time(
            dataflow_googleapis_com:job_total_pd_usage_time{storage_type="HDD"}[1m]
          ) / 3600 * STANDARD_PD_PRICE
        ) by (job_id)
        
        # Formula: ((SSD PD time)[Bucket 1m] / Seconds per hour) * SSD PD price
        sum(
          max_over_time(
            dataflow_googleapis_com:job_total_pd_usage_time{storage_type="SSD"}[1m]
          ) / 3600 * SSD_PD_PRICE
        ) by (job_id)
        

  * Summing the previous values gives the estimated cost per job. To get the top 25 jobs, use a top K filter:
        
        topk(25,
          # Sum the individual values.
        )
        




### Write the complete query

The following shows the complete query:
    
    
    topk(25,
    sum(
      max_over_time(
        dataflow_googleapis_com:job_total_vcpu_time[1m]) / 3600 * CPU_PRICE
      )
      by (job_id) +
    sum(
      max_over_time(
        dataflow_googleapis_com:job_total_memory_usage_time[1m]) / 3600 * MEMORY_PRICE
      )
      by (job_id) +
    sum(
      max_over_time(
        dataflow_googleapis_com:job_total_streaming_data_processed[1m]) / 1000000000 * SHUFFLE_PRICE
      )
      by (job_id) +
    sum(
      max_over_time(
        dataflow_googleapis_com:job_total_pd_usage_time{storage_type="HDD"}[1m]) / 3600 * STANDARD_PD_PRICE
      )
      by (job_id) +
    sum(
      max_over_time(
        dataflow_googleapis_com:job_total_pd_usage_time{storage_type="SSD"}[1m]) / 3600 * SSD_PD_PRICE
      )
      by (job_id)
    )
    

Replace the following variables with values from the [Dataflow pricing page](https://cloud.google.com/dataflow/pricing) for your region.

  * CPU_PRICE: CPU price, per vCPU per hour
  * MEMORY_PRICE: Memory price, per GB per hour
  * SHUFFLE_PRICE: Shuffle price, per GB
  * STANDARD_PD_PRICE: Standard Persistent Disk price, per GB per hour
  * SSD_PD_PRICE: SSD Persistent Disk price, per GB per hour



## Edit the dashboard

If you didn't previously create a custom dashboard for Dataflow in this project, create one as follows:

  1. In the Google Cloud console, go to the **Dataflow** > **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/dataflow/monitoring)

  2. In the **Predefined** drop-down, click **Customize dashboard**.

  3. Optional: Enter a name for the dashboard in the **Custom view name** box.




If you previously created a custom dashboard, perform the following steps to edit the dashboard:

  1. In the Google Cloud console, go to the **Dataflow** > **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/dataflow/monitoring)

  2. In the **Predefined** drop-down, select the custom dashboard.

  3. Click edit**Edit dashboard**.




## Add a metrics chart

To add a metrics chart to the dashboard, perform the following steps:

  1. Click **Add widget**.
  2. In the **Add widget** pane, select **Metric**.
  3. In the **Widget title** box, enter a title for the chart, such as `Estimated cost (top 25)`.
  4. Click code**PROMQL**
  5. Paste in the PromQL query shown previously.
  6. Click **Run query**.
  7. Click **Apply**.
  8. Optional: Drag the chart to position it on the dashboard.



## What's next

  * [Add a reference line](https://docs.cloud.google.com/monitoring/charts/chart-view-options#threshold-option) so that you can see when a metric exceeds a predefined threshold.
  * [Learn PromQL](https://docs.cloud.google.com/monitoring/promql#learning-promql).
  * [Learn more about dashboards](https://docs.cloud.google.com/monitoring/dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
