---
url: https://docs.cloud.google.com/logging/docs/export/pubsub/
title: View logs routed to Pub/Sub \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:50.163257+00:00
---

# View logs routed to Pub/Sub  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/export/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  View logs routed to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how you can find log entries that you routed from Cloud Logging to [Pub/Sub topics](https://docs.cloud.google.com/pubsub/docs), which occurs in near real-time. We recommend using Pub/Sub for integrating Cloud Logging logs with third-party software. 

When you route log entries to a Pub/Sub topic, Logging publishes each log entry as a Pub/Sub message as soon as Logging receives that log entry. Routed log entries are generally available within seconds of their arrival to Logging, with 99% of log entries available in less than 60 seconds.

## Before you begin

For a conceptual discussion of sinks, see [Overview of routing and storage models: Sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks).

For instructions on how to route your log entries, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## View logs

To view your logs as they are streamed through Pub/Sub, do the following:

  1. In the Google Cloud console, go to the **Topics** page: 

[Go to **Topics**](https://console.cloud.google.com/cloudpubsub/topicList)

If you use the search bar to find this page, then select the result whose subheading is **Pub/Sub**.

  2. Find or create a subscription to the topic used in the log sink, and pull a log entry from it. You might have to wait for a new log entry to be published.




## Logs organization

The `data` field of each message is a base64-encoded [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object. As an example, a Pub/Sub subscriber might pull the following object from a topic that is receiving log entries. The object shown contains a list with a single message, although Pub/Sub might return several messages if several log entries are available. The `data` value (about 600 characters) and the `ackId` value (about 200 characters) have been shortened to make the example easier to read:
    
    
    {
     "receivedMessages": [
      {
       "ackId": "dR1JHlAbEGEIBERNK0EPKVgUWQYyODM...QlVWBwY9HFELH3cOAjYYFlcGICIjIg",
       "message": {
        "data": "eyJtZXRhZGF0YSI6eyJzZXZ0eSI6Il...Dk0OTU2G9nIjoiaGVsbG93b3JsZC5sb2cifQ==",
        "attributes": {
         "compute.googleapis.com/resource_type": "instance",
         "compute.googleapis.com/resource_id": "123456"
        },
        "messageId": "43913662360"
       }
      }
     ]
    }

If you decode the `data` field and format it, you get the following [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object: 
    
    
    {
      "log": "helloworld.log",
      "insertId": "2015-04-15|11:41:00.577447-07|10.52.166.198|-1694494956",
      "textPayload": "Wed Apr 15 20:40:51 CEST 2015 Hello, world!",
      "timestamp": "2015-04-15T18:40:56Z",
      "labels": {
        "compute.googleapis.com\/resource_type": "instance",
        "compute.googleapis.com\/resource_id": "123456"
      },
      "severity": "WARNING"
      }
    }

### Limitation

The `LogEntry.errorGroups` field isn't available for this destination. Log sinks route the log entries sent to your project, but those log entries don't contain error groups.

## Third-party integration with Pub/Sub

You route your log entries to a Pub/Sub topic. The third party receives your log entries by subscribing to the same topic. Logging supports logging integration with third parties, such as Splunk or Datadog. For a current list of integrations, see [Partners](https://cloud.google.com/products/observability#partners) for Google Cloud Observability integrations.

To perform the integration, expect to do something like the following:

  1. In your project where your log entries originate, create your Pub/Sub topic with a [default subscription](https://docs.cloud.google.com/pubsub/docs/create-topic#properties_of_a_topic):

     1. Enable the Pub/Sub API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub&redirect=%7B%7Bdynamic_data.site_values.console_url%7D%7Dcloudpubsub/topicList)

     2. In the Google Cloud console, go to the **Topics** page: 

[Go to **Topics**](https://console.cloud.google.com/cloudpubsub/topicList)

If you use the search bar to find this page, then select the result whose subheading is **Pub/Sub**.

     3. Click **Create topic**.

     4. In the **Topic ID** field, enter an ID for your topic. For example, `projects/my-project-id/topics/my-pubsub-topic`.

Each message sent to the topic include the timestamp of the routed log entry in the Pub/Sub message `attributes`; for example:
            
            "attributes": {
              "logging.googleapis.com/timestamp": "2024-07-01T00:00:00Z"
            }
            

     5. Retain the option **Add a default subscription.** Don't select any other option.

     6. Click **Create topic**.

  2. In your project where your log entries originate, configure Logging to route log entries to your topic:

     1. In the Google Cloud console, go to the **Log Router** page: 

[Go to **Log Router**](https://console.cloud.google.com/logs/router)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. Click **Create Sink** , enter a name and description for the sink, and then click **Next**.
     3. In the **Sink Service** menu, select **Cloud Pub/Sub topic** , select the Pub/Sub topic, and then click **Next**.
     4. Select the log entries to include in the sink and then click **Next**.
     5. Optional: Select the log entries to exclude.
     6. Click **Create Sink**.

A dialog with the message **Sink created** appears. This message indicates that your sink was successfully created with permissions to route future matching log entries to the destination you selected.

     7. Grant the principal specified in the sink's writer identity the following IAM roles:

        * [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)

        * [Pub/Sub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`)

For more information about obtaining the writer identity and granting a role, see [Set destination permissions](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-auth).

Cloud Logging is now sending log entries to your Pub/Sub topic.

  3. Create the subscription.

For example, if you use Dataflow to pull the data from your Pub/Sub topic and send it to [Datadog](https://docs.datadoghq.com/integrations/google_cloud_platform/?tab=project#log-collection), then you need to perform two steps:

     1. Create, or obtain, a service account, and then grant it the IAM roles necessary to subscribe to your topic. At a minimum, the service account requires the following roles:

        * [Pub/Sub Subscriber (`roles/pubsub.subscriber`)](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber)
        * [Dataflow Admin (`roles/dataflow.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.admin)
        * [Dataflow Worker (`roles/dataflow.worker`)](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.worker)

For more information, see the following documents:

        * [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).
        * [Grant the service account the necessary roles](https://docs.cloud.google.com/iam/docs/create-service-agents#grant-role).
     2. Create a job from a template, and then run that job. For this example, you would use the [Pub/Sub to Datadog template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-datadog).




Your third party should begin receiving the log entries right away.

For an exploration of common logs routing scenarios using Pub/Sub, see [Scenarios for exporting Cloud Logging data: Splunk](https://docs.cloud.google.com/architecture/stream-logs-from-google-cloud-to-splunk).

## Troubleshooting

If log entries seem to be missing from your sink's destination or you otherwise suspect that your sink isn't properly routing log entries, then see [Troubleshoot routing logs](https://docs.cloud.google.com/logging/docs/export/troubleshoot).

## Pricing

For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page. If you route log data to other Google Cloud services, then see the following documents:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing)
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing#data_ingestion_pricing)
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
