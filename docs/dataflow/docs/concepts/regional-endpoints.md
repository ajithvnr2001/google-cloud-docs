---
url: https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints/
title: Dataflow regions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:48.245414+00:00
---

# Dataflow regions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow regions Stay organized with collections  Save and categorize content based on your preferences. 

The Dataflow region stores and handles metadata about your Dataflow job and deploys and controls your Dataflow workers.

Region names follow a standard convention based on [Compute Engine region names](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available). For example, the name for the Central US region is `us-central1`.

This feature is available in all regions where Dataflow is supported. To see available locations, read [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations).

## Guidelines for choosing a region

Use the following guidelines to choose an appropriate region for your job.

### Security and compliance

You might need to constrain Dataflow job processing to a specific geographic region in support of the security and compliance needs of your project.

### Data locality

You can minimize network latency and network transport costs by running a Dataflow job from the same region as its sources, sinks, staging file locations, and temporary file locations. If you use sources, sinks, staging file locations, or temporary file locations that are located _outside_ of your job's region, your data might be sent across regions.

**Note:** Starting with Beam SDK version 2.44.0, Dataflow does not support running jobs with workers in a region that is different from the job region.

In running a pipeline, user data is only handled by the Dataflow worker pool and the movement of the data is restricted to the network paths that connect the Dataflow workers in the pool.

Although user data is strictly handled by Dataflow workers in their assigned geographic region, pipeline log messages are stored in [Cloud Logging](https://docs.cloud.google.com/logging/docs), which has a single global presence in Google Cloud.

If you need more control over the location of pipeline log messages, you can do the following:

  1. [Create an exclusion filter](https://docs.cloud.google.com/logging/docs/exclusions#create-filter-existing) for the `_Default` log router sink to prevent Dataflow logs from being exported to the `_Default` log bucket.
  2. [Create a log bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket) in the region of your choice.
  3. Configure a new log router sink that exports your Dataflow logs to your new log bucket.



To learn more about configuring logging, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview) and [Log routing overview](https://docs.cloud.google.com/logging/docs/export).

Notes about common Dataflow job sources:

  * When using a Cloud Storage bucket as a source, we recommend that you perform **read** operations in the same [region as the bucket](https://docs.cloud.google.com/storage/docs/bucket-locations).
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/architecture) topics, when published to the global Pub/Sub endpoint, are stored in the nearest Google Cloud region. However, you can modify the topic storage policy to a specific [region or a set of regions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction). Similarly, [Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite#comparison_table) topics support only zonal storage.



### Resilience and geographic separation

You might want to isolate your normal Dataflow operations from outages that could occur in other [geographic regions](https://docs.cloud.google.com/docs/geography-and-regions). Or, you might need to plan alternate sites for business continuity in the event of a region-wide disaster.

In your [disaster recovery and business continuity plans](https://docs.cloud.google.com/solutions/designing-a-disaster-recovery-plan), we recommend incorporating details for sources and sinks used with your Dataflow jobs. The [Google Cloud sales team](https://cloud.google.com/contact/) can help you work towards meeting your requirements.

## Regional placement

By default, the region that you select configures the Dataflow worker pool to utilize all available zones within the region. Zone selection is calculated for each worker at its creation time, optimizing for resource acquisition and utilization of unused [reservations](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources).

Regional placement offers benefits such as:

  * Improved resource availability: Dataflow jobs are more resilient to [zonal resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability) errors, because workers can continue to be created in other zones with remaining availability.
  * Improved reliability: In the event of a zonal failure, Dataflow jobs can continue to run, because workers are recreated in other zones.



The following limitations apply:

  * Regional placement is supported only for jobs using Streaming Engine or Dataflow Shuffle. Jobs that have opted out of Streaming Engine or Dataflow Shuffle cannot use regional placement.
  * Regional placement applies to VMs only, and doesn't apply to backend resources.
  * VMs are not replicated across multiple zones. If a VM becomes unavailable, for example, its work items are considered lost and are reprocessed by another VM.
  * If Compute Engine does not have capacity in the configured region, the Dataflow service cannot create any more VMs.
  * If Compute Engine does not have capacity in one or more zones in the configured region, the Dataflow service might fail to start a job.



## View job resource zones

Dataflow jobs depend on internal resources. Some of these backend job resources are zonal. If a single zone fails and a zonal resource necessary for your Dataflow job is in that zone, the job might fail.

To understand whether a job failed because of a zonal outage, review the service zones that your job's backend resources are using. This feature is only available for Streaming Engine jobs.

  * To view the service zones in the Google Cloud console, use the **Service zones** field in the **Job info** panel.

  * To use the API to review the service zones, use the [`ServiceResources`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.ServiceResources) field.




The values in this field update throughout the duration of the job, because the resources that the job uses change while the job runs.

## Automatic zone placement

For jobs not supported for regional placement, the best zone within the region is selected automatically, based on the available zone capacity at the time of the job creation request. Automatic zone selection helps ensure that job workers run in the best zone for your job.

Because the job is configured to run in a single zone, the operation might fail with a [zonal resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability) error if sufficient Compute Engine resources are not available. If capacity is exhausted in a region, you might see a [`ZONE_RESOURCE_POOL_EXHAUSTED`](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#worker-pool-failure) error. You can implement a retry loop to start the job when resources are available.

Also, when a zone is unavailable, the streaming backend can also become unavailable, which might result in data loss.

To avoid zonal resource availability errors and resource pool exhausted errors, we recommend using `--region` and enabling Streaming Engine or Dataflow Shuffle to take advantage of regional placement. Regional placement allows Dataflow to create workers across all available zones within a region instead of pinning your job to a single zone.

## Specify a region

**Note:** Region configuration requires Apache Beam SDK version 2.0.0 or higher.

To specify a region for your job, set the `--region` option to one of the [**supported**](https://docs.cloud.google.com/dataflow/docs/resources/locations) regions. The `--region` option overrides the default region that is set in the metadata server, your local client, or the environment variables.

The [Dataflow command-line interface](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow) also supports the `--region` option to specify regions.

## Override the worker region or zone

By default, when you submit a job with the `--region` option, workers are automatically assigned to either zones across the region or the single best zone within the region, depending on the job type.

In cases where you want to ensure that the workers for your Dataflow job run strictly in a specific zone, you can specify the zone using the following [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options). This usage pattern is uncommon for Dataflow jobs.

This option only controls the zone used for the Dataflow workers. It doesn't apply to backend resources. Backend resources might be created in any zone within the job region.

###  Java 
    
    
    --workerZone
    

###  Python 
    
    
    --worker_zone
    

###  Go 
    
    
    --worker_zone
    

For all other cases, we don't recommend overriding the worker location. The common scenarios table contains usage recommendations for these situations.

Because the job is configured to run in a single zone, the operation might fail with a [zonal resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability) error if sufficient Compute Engine resources are not available. If you experience zonal resource availability errors or resource pool exhausted errors, avoid using `--workerZone` or `--worker_zone` to pin your job to a specific zone. Instead, specify `--region` and enable Streaming Engine or Dataflow Shuffle to use regional placement, which utilizes all available zones within the region.

**Caution:** If you override the worker zone and the workers are in a different region than the job region, there might be a negative impact on performance, network traffic, network latency, and network cost.

You can run the `gcloud compute regions list` command to see a listing of regions and zones that are available for worker deployment.

## Common scenarios

The following table contains usage recommendations for common scenarios.

Scenario | Recommendation  
---|---  
I want to use a supported region and have no zone preference within the region. In this case, the best zone is automatically selected based on available capacity. | Use `--region` to specify a job region. This ensures that Dataflow manages your job and processes data within the specified region.  
I want to avoid zonal resource availability errors and resource pool exhausted errors. | Specify `--region` and enable Streaming Engine or Dataflow Shuffle to use regional placement across all zones in the region. Avoid specifying `--workerZone` or `--worker_zone`, which pins workers to a single zone.  
I need worker processing to occur in a specific zone of a region. | Specify both `--region` and either `--workerZone` or `--worker_zone`.  
Use `--region` to specify the job region. Use either `--workerZone` or `--worker_zone` to specify the specific [zone](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) within that region.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
