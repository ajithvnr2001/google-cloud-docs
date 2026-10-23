---
url: https://docs.cloud.google.com/pubsub/docs/monitor-topic/
title: Monitor topics within Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:52.631971+00:00
---

# Monitor topics within Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/monitor-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Monitor topics within Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Google Cloud console to access the monitoring dashboard for a single topic or all the topics available in your project.

**Key Point:** Learn how to access the monitoring dashboard for Pub/Sub topics, understand some key metrics, and learn how to create a custom monitoring experience.

## Before you begin

Ensure that you've prepared the following:

  * A Cloud Billing account

  * A Pub/Sub project with billing enabled

  * At least one topic in your Pub/Sub project

  * Familiarity with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and [Metrics Explorer](https://docs.cloud.google.com/monitoring/mql)




## View the monitoring dashboard for all topics

To view the monitoring dashboard for all the topics in a project, perform the following steps:

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click the **Metrics** tab.

The monitoring dashboard is displayed for all topics in the project.




The monitoring dashboard has two sections: **Overview** and **Quota**.

## View the monitoring dashboard for a single topic

To view the monitoring dashboard for a single topic in a project, perform the following steps:

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. In the **Topics** page, click any topic.

The topic details page is displayed.

  3. Within the topic details page, click the **Metrics** tab.

The monitoring dashboard is displayed for the single topic.




The monitoring dashboard has three sections: **Overview** , **Subscriptions** , and **Retention**. You can see the **Retention** section only if you enable message retention for the topic. For more information about message retention, see [Properties of a topic](https://docs.cloud.google.com/pubsub/docs/admin#properties_of_a_topic).

## Customize the monitoring dashboard

You can create a custom dashboard or add individual charts to an existing custom dashboard.

To create a custom dashboard, perform the following steps:

  1. Follow the steps to go to the monitoring page for all topics or for a single topic.

  2. Choose one of the following options:

     * To create a new dashboard containing all the charts, or to add all the charts to an existing custom dashboard, click **Save as custom dashboard**.

     * To add a single chart to a new or custom dashboard, in an individual chart, expand the more_vert **More Actions** option and click **Add to custom dashboard**.




You can view all your dashboards in the [Monitoring](https://console.cloud.google.com/monitoring/dashboards/) console.

## Modify a chart

To modify a chart, perform the following steps:

  1. Follow the steps to go to the monitoring page for all topics or for a single topic.

  2. In an individual chart, expand the more_vert **More Actions** option and click **View in Metrics Explorer**.

The chart opens in **Metrics Explorer**.

  3. You can use [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql) queries to make changes to your chart and test the output.

  4. Click **Save chart** to save the changes.




## Create an alerting policy

Creating an alerting policy for a chart lets you set up an alert monitoring metric in the chart, configure the circumstances under which you want to be alerted, and configure how you want to be notified.

For more information about how to create alerts, see [Create metric-based alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

Some charts might not offer a **Create alerting policy** option. In this case, perform the following steps:

  1. Save the chart to a custom dashboard.

  2. In the custom dashboard, for the individual chart, expand the more_vert **More Actions** option.

  3. Click **Convert to alert chart**.




## Key charts to monitor topics

Although there are a number of charts available to monitor a single topic, the following charts in the **Overview** section are a good starting point:

  * The **Publish requests** chart lets you check if there are sudden spikes in the topic for receiving publish requests.

  * The **Average number of messages per batch** chart lets you check if the batching size is adequate for your requirements. A smaller batch size leads to reduced publish latency.




The following charts in the **Quota** section for all topics help you monitor quotas for all the topics in your project:

  * The **Administrator operations** chart lets you monitor administrative operations regarding topics. Each administrator operation charges one unit against this quota.



For more information, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).

## Metrics to monitor imported topics

You can use the following metrics to monitor imported topics:

  * [**Ingestion byte count**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/ingestion_byte_count): This metric displays the total volume of data (in bytes) ingested from an import source into an import topic. It provides a breakdown of byte counts for each import source and partition (shard).

  * [**Ingestion message count**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/ingestion_message_count): This metric displays the total number of import messages for each import source and partition.

  * [**Ingestion data source state**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/ingestion_data_source_state): This metric displays the state of the external source from which the import topic is ingesting data. The error codes and their workarounds are listed in the troubleshooting section of the import topics. For more information, see the following:

    * [Troubleshooting Amazon Kinesis Data Streams import topics](https://docs.cloud.google.com/pubsub/docs/aws-kinesis-import-topic-troubleshooting).
    * [Troubleshooting Cloud Storage import topics](https://docs.cloud.google.com/pubsub/docs/cloud-storage-import-topic-troubleshooting).
    * [Troubleshooting Amazon MSK import topics](https://docs.cloud.google.com/pubsub/docs/amazon-msk-import-topic-troubleshooting).
    * [Troubleshooting Azure Event Hubs import topics](https://docs.cloud.google.com/pubsub/docs/azure-event-hub-import-topic-troubleshooting).
    * [Troubleshooting Confluent Cloud import topics](https://docs.cloud.google.com/pubsub/docs/confluent-cloud-import-topic-troubleshooting).
  * [**Ingestion failure count**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/ingestion_failure_count): This metric displays the number of failures encountered during ingestion. For Cloud Storage import topics, this metric includes the bucket name and the failure reason. For Amazon MSK, Azure Event Hubs, and Confluent Cloud import topics, this metric includes the Kafka topic or event hub name, the partition, and the failure reason.




To check these metrics, follow the steps described in View the monitoring dashboard for a single topic.

## What's next

  * To monitor subscriptions, see [Monitor subscriptions in Pub/Sub](https://docs.cloud.google.com/pubsub/docs/monitor-subscription).

  * To learn more about using PromQL to build monitoring charts, see [Using the Query Editor](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
