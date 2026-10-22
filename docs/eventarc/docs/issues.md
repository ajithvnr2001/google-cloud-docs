---
url: https://docs.cloud.google.com/eventarc/docs/issues/
title: Known issues for Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:27.536761+00:00
---

# Known issues for Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Known issues for Eventarc Standard Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

Current service limitations, symptoms, and workarounds for Eventarc Standard help you identify and mitigate operational problems.

You can also check for existing issues or open new ones in the [public issue trackers](https://docs.cloud.google.com/support/docs/issue-trackers).

## Provisioning and timing

  * **Trigger deployment time** : Newly created triggers can take up to two minutes to become operational.

  * **Provisioning of service agent** : When creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).




## Trigger configuration

  * **Cross-project triggers** : Cross-project triggers are not yet supported. The service that receives the events for the trigger must be in the same Google Cloud project as the trigger. If requests to your service are triggered by messages published to a Pub/Sub topic, the topic must also be in the same project as the trigger. See [Route events across Google Cloud projects](https://docs.cloud.google.com/eventarc/docs/cross-project-triggers).

  * **Cloud Audit Logs triggers for Compute Engine** : Regardless of where the virtual machine instance is actually located, Cloud Audit Logs triggers for [Compute Engine](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#compute-engine) result in events that originate from a single region: `us-central1`. When [creating your trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers), ensure that the trigger location is set to either `us-central1` or `global`.

  * **Cloud Storage triggers in multi-region locations** : Cloud Storage triggers can fail if a Cloud Storage event originates from a region not permitted by your Pub/Sub message storage policy, and if in-transit operations are enforced (`"enforceInTransit": true`). When you create a Cloud Storage trigger in a [multi-region](https://docs.cloud.google.com/eventarc/docs/locations#gcs-triggers) location, ensure your message storage policy allows all source regions within that multi-region. This policy defines where messages are stored during delivery and where in-transit operations are enforced. For more information, see [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

  * **Updating a trigger** : If you [update a trigger](https://docs.cloud.google.com/eventarc/docs/managing-triggers#trigger-update) before its generated event is delivered, the event is routed according to the previous filtering and delivered to the original destination within three days of the event generation. The new filtering is applied to events generated _after_ your update.




## Event payloads and delivery

  * **Duplicate transmission of Cloud Audit Logs** : There is a known duplicate transmission of Cloud Audit Logs from some Google Cloud event sources. When duplicate logs are published, duplicate events are delivered to destinations. To avoid these duplicate events, you should create triggers for fields that ensure the event is unique. This applies to the following event types:

    * Cloud Storage (serviceName: `storage.googleapis.com`), methodName: `storage.buckets.list`
    * Compute Engine (serviceName: `compute.googleapis.com`), methodName: `beta.compute.instances.insert`
    * BigQuery (serviceName: `bigquery.googleapis.com`)

Note that since Workflows handles event deduplication, you don't have to ensure that the event is unique when you create a trigger for Workflows.

  * **Handling message failures for direct Pub/Sub events** : [Direct Pub/Sub events](https://docs.cloud.google.com/eventarc/standard/docs/event-types#cloud-pubsub) don't include a [`delivery_attempt`](https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/pubsub/v1/data.proto#L45) field unless the event destination is Cloud Run or Cloud Run functions. This might impact your [handling of message failures](https://docs.cloud.google.com/pubsub/docs/handling-failures).

  * **Event payload encoding** : For some event providers, you can choose to encode the event payload as `application/json` or `application/protobuf`. However, an event payload formatted in JSON is larger than one formatted in Protobuf, and this might impact reliability depending on your event destination, and its limits on event size. When this limit is reached, the event is retried according to the [retry characteristics of Eventarc's transport layer, Pub/Sub](https://docs.cloud.google.com/eventarc/standard/docs/overview#event-retry-policy). Learn how to [handle Pub/Sub message failures](https://docs.cloud.google.com/pubsub/docs/handling-failures) if the maximum number of retries is made.




## Destinations and limits

  * **Workflows arguments size** : While using Workflows as a destination for an Eventarc trigger, events larger than the maximum Workflows arguments size will fail to trigger workflow executions. For more information, see [Quotas and limits](https://docs.cloud.google.com/workflows/quotas#resource_limit).

  * **Nested depth limit for log entries** : The maximum nested depth limit on each structured log entry for triggers that use Cloud Audit Logs is 64 levels. Log events that exceed this limit are dropped and not delivered by Eventarc.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
