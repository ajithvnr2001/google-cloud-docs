---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options/
title: Event routes \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:17.696200+00:00
---

# Event routes  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/event-routing-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Event routes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

You can route events to your destination by configuring filters for an Eventarc trigger. The trigger configuration varies depending on the type of event. The event route you select also depends on the event type.

## Event types

  * **Direct events from an integrated Google provider** — Eventarc can route direct events such as an update to an object in a Cloud Storage bucket or an update to a Firebase Remote Config template. See the list of [supported direct events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source).

  * **Cloud Audit Logs and Eventarc** — When an audit log is produced that matches the Eventarc trigger's filter criteria, events are routed, allowing you to capture and act on specific events. See the list of [supported audit log events](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#using-cloud-audit-logs).

  * **Pub/Sub and Eventarc** — When a message is published to a Pub/Sub topic specified by the Eventarc trigger's filter criteria (`"type=google.cloud.pubsub.topic.v1.messagePublished"`), events are routed. You can integrate Eventarc with any service that can publish messages using Pub/Sub.

  * **Direct Pub/Sub push** — Instead of using Eventarc, you can use Pub/Sub to directly push messages to your service. This applies to applications or services that have a direct Pub/Sub integration. For more information, see [Trigger from Pub/Sub push](https://docs.cloud.google.com/run/docs/triggering/pubsub-push).




## Select an event route

To determine how best to route your events to a destination, ask yourself the following questions:

  1. Does Eventarc support direct events for the event that you want to route? If yes, create an Eventarc trigger to route that direct event. If no, consider the next question (#2).

For the event that you want to route, if both direct and audit log options are supported, we recommend that you create a trigger to route the direct event. Direct events offer the following advantages over audit log events:

     * Improved trigger responsiveness and event delivery latency
     * Strongly typed event formats that are more predictable and discoverable
     * Support for filtering on collection IDs ([resource name](https://docs.cloud.google.com/apis/design/resource_names) components)
     * No additional costs incurred from enabling Cloud Audit Logs
  2. Does your Google service or application support Cloud Audit Logs, Pub/Sub, or both?

  3. If both Cloud Audit Logs and Pub/Sub are supported, which of the two provides the required information? For example, Cloud Build can generate both audit logs and Pub/Sub messages; however, Pub/Sub can provide build status notifications (success or failure) while the Cloud Build audit logs can provide information about build creation and deletion operations. In some cases, the content and latency impact of both the audit logs and Pub/Sub messages is comparable, and you can choose either. You should then consider the next question (#4).

  4. If using Pub/Sub, is there any advantage to receiving events through Eventarc and a common [CloudEvents](https://docs.cloud.google.com/eventarc/docs/cloudevents) format? For example, are there multiple event sources? Although you might be more familiar with pushing Pub/Sub messages directly, you might want the efficiency and convenience of a standard delivery mechanism and format.




## What's next

  * [Learn how to create an Eventarc trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).
  * [Determine event filters for Cloud Audit Logs](https://docs.cloud.google.com/eventarc/docs/determining-filters-cal).
  * [Learn how to receive Cloud Storage events using Cloud Audit Logs](https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-cloud-audit-logs-gcloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
