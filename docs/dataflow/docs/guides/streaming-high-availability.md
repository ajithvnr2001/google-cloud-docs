---
url: https://docs.cloud.google.com/dataflow/docs/guides/streaming-high-availability/
title: Streaming high availability \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:11.549819+00:00
---

# Streaming high availability  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/streaming-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Streaming high availability Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Dataflow streaming jobs run some of their backend resources in a single Compute Engine zone, which makes those jobs susceptible to data loss during a [zonal outage](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#view-zones). Streaming high availability makes a [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) job a regional resource by replicating backend state across multiple zones in the region. When you enable streaming high availability, a single-zone failure doesn't cause your streaming job to go down.

## Support and limitations

Streaming high availability has the following requirements and limitations:

  * **Streaming Engine required:** The job must be a streaming pipeline that uses [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine).
  * **Regional worker placement required:** Compute Engine workers must use [regional placement](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#regional-placement). If a job only has workers in a specific zone and that zone becomes unavailable, the job can't process data because its workers are unavailable, even though backend state is replicated. Therefore, Dataflow rejects jobs that specify a particular worker zone (such as `--workerZone`, `--worker_zone`, or `--zone`) when streaming high availability is enabled.
  * **Configured at job creation only:** You can only enable streaming high availability when you start a new job. You can't enable or disable streaming high availability when you perform an in-place [pipeline update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline). To change this setting on a running pipeline, either perform an [automated stop-and-replace update](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#automated-stop-replace), or [stop or drain the pipeline](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline) and start a new job without the `--update` flag.
  * **Additional watermark lag:** When you enable streaming high availability, a job's [watermark](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines#watermarks) only advances after data is both processed and replicated across zones. Because the watermark waits for cross-zone replication, you might notice a few seconds of additional watermark lag.
  * **Resource-based billing required:** Streaming high availability jobs always use [resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#compute-unit-pricing) and never use [data-processed billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#data-processed-pricing). Even though jobs use resource-based billing, there are no additional charges for streaming high availability during Preview; for more information, see Pricing.



## Enable streaming high availability

To enable streaming high availability when you launch a new Dataflow streaming job, set the `requires_high_availability` [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options).

###  Java 
    
    
    --dataflowServiceOptions=requires_high_availability
    

###  Python 
    
    
    --dataflow_service_options=requires_high_availability
    

###  Go 
    
    
    --dataflow_service_options=requires_high_availability
    

###  gcloud 

When you run a template using the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command or a Flex Template using the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command, include the `--enable-streaming-engine` and `--additional-experiments` flags:
    
    
    --enable-streaming-engine \
    --additional-experiments=requires_high_availability
    

For example, to run a Flex Template with streaming high availability enabled:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --project=PROJECT_ID \
        --template-file-gcs-location=TEMPLATE_LOCATION \
        --region=REGION \
        --parameters=KEY_1=VALUE_1,KEY_2=VALUE_2 \
        --enable-streaming-engine \
        --additional-experiments=requires_high_availability
    

Replace the following values:

  * `JOB_NAME`: the name of your Dataflow job
  * `PROJECT_ID`: your Google Cloud project ID
  * `TEMPLATE_LOCATION`: the Cloud Storage path to your Flex Template specification file
  * `REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where the job runs
  * `KEY_1=VALUE_1`, `KEY_2=VALUE_2`: key-value parameter pairs for the Flex Template



###  Console 

To enable streaming high availability when you run a template or Flex Template in the Google Cloud console:

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Click **Create job from template**.

  3. Select the template that you want to run from the **Dataflow template** menu.

  4. Expand **Optional parameters**.

  5. In the **Additional experiments** field, enter `requires_high_availability`.

  6. Click **Run job**.




###  REST 

Use the `additionalExperiments` field in the [`RuntimeEnvironment`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/RuntimeEnvironment) object, or in the [`FlexTemplateRuntimeEnvironment`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.flexTemplates/launch#FlexTemplateRuntimeEnvironment) object when launching a Flex Template:
    
    
    {
      "additionalExperiments": ["requires_high_availability"]
    }
    

## Failover behavior

In the rare event of a zonal failover, you might observe a few seconds to a few minutes of reduced throughput while the job switches to a new primary state and establishes a new secondary replica in another zone. Failover occurs automatically without dropping data, and no action is required from you. You can track failover events using the metrics described in Monitor high availability.

## Sources and sinks

Configuring a Dataflow job as a regional resource doesn't automatically make the job's sources and sinks regional or global. Both regional and global sources and sinks work well with streaming high availability, because neither depends on a single zone. The availability of each source or sink depends on that service's configuration:

  * Many Google Cloud sources and sinks, such as Pub/Sub, BigQuery, and Google Cloud Managed Service for Apache Kafka, provide regional or global availability by default.
  * If you use custom or self-managed sources and sinks, such as self-hosted Apache Kafka or Apache Iceberg, you must configure and maintain their regional availability independently.



## Monitor high availability

You can monitor the high availability status of your job in Cloud Monitoring using the `dataflow.googleapis.com/job/high_availability_mode` metric. This boolean gauge metric includes a `status` label that is `true` for the job's current status and `false` for the other statuses. The `status` label has the following possible values:

  * `Disabled`: Streaming high availability isn't enabled for this job.
  * `Highly Available`: Streaming high availability is enabled and backend state is replicated across zones.
  * `Establishing High Availability`: Backend state is temporarily not replicated (for example, after a zonal failure), but a new secondary replica is being created.



When you enable streaming high availability, the standard Dataflow watermark metrics only advance after data is both processed and replicated across zones. For more information about viewing metrics, see [Use Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring).

## Pricing

During Preview, there are no additional charges for using streaming high availability.

At general availability (GA), replication usage is billed at the same rate as primary state usage. State usage is metered as part of [Streaming Engine Compute Units](https://docs.cloud.google.com/dataflow/pricing#streaming-compute-units).

## What's next

  * Learn more about [Dataflow regions and regional placement](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#regional-placement).
  * Learn more about [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine).
  * Monitor your pipelines with [Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
