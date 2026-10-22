---
url: https://docs.cloud.google.com/eventarc/advanced/docs/event-providers-targets/
title: Event providers and destinations \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:22.596944+00:00
---

# Event providers and destinations  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/event-providers-targets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Event providers and destinations Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

Eventarc Advanced lets you use buses to collect event messages from diverse providers and route them to supported destinations. You can use pipelines to filter, transform, and deliver events to target services such as Cloud Run and Workflows.

## Supported providers

Supported providers include Google providers and direct publishers of events (using the Eventarc Publishing API).

  * Google providers send [Google events](https://docs.cloud.google.com/eventarc/advanced/docs/event-types) directly from the source (for example, the creation of a Cloud Run function or a status change to a Dataflow job). You must first enable support for Google event types. For more information, see [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources).

  * Event publishers can publish a [CloudEvents event](https://docs.cloud.google.com/eventarc/advanced/docs/event-format) directly to a message bus in a supported format such as Avro or Protobuf. For more information, see [Publish events directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format).




## Supported destinations

An Eventarc Advanced pipeline delivers events between a bus and a destination. Each pipeline forwards messages to a single destination. The following destinations are supported:

  * Cloud Run—Use the stable, [auto-assigned `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request) provided on the first deployment of the Cloud Run-hosted service. You can also target a [Cloud Run job](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#cloud-run-jobs) or specify an HTTP endpoint for Cloud Run functions ([1st gen](https://docs.cloud.google.com/functions/1stgendocs/calling/http) and [current version](https://docs.cloud.google.com/functions/docs/calling/http)). When you specify an HTTP trigger for a Cloud Run function, the function is assigned a URL at which it can receive requests.

  * Eventarc Advanced bus—The [message bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus) must be deployed in the same project and region as the pipeline.

  * HTTP endpoint—A destination URI. The host can be either a static IP addressable from a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc), or the internal [Domain Name System (DNS)](https://docs.cloud.google.com/dns/docs/dns-overview) hostname of a service resolvable using Cloud DNS. For example, you can target a [Cloud Run service URL](https://docs.cloud.google.com/run/docs/triggering/https-request#url) or a [BigQuery table](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll) that will receive events as HTTP `POST` requests.

  * Pub/Sub topic—The [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publish-message-overview) must first be created before messages can be routed to it and must be located in the same project as the pipeline. If using a [topic schema](https://docs.cloud.google.com/pubsub/docs/create-topic#use_a_schema), make sure to [transform your event message](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events) appropriately.

  * Workflows—You can trigger the [execution of a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow) which is a single run of the logic contained in a workflow definition. This lets you run services in an order that you specify. The workflow must be deployed in the same project as the pipeline.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
