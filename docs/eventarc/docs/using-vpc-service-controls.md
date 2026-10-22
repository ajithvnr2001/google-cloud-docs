---
url: https://docs.cloud.google.com/eventarc/docs/using-vpc-service-controls/
title: Set up a service perimeter using VPC Service Controls \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:24.153790+00:00
---

# Set up a service perimeter using VPC Service Controls  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/using-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Set up a service perimeter using VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

VPC Service Controls is a Google Cloud feature that lets you set up a service perimeter and create a data transfer boundary. You can use VPC Service Controls with Eventarc to help protect your services.

**Note:** Eventarc Standard handles event delivery using Pub/Sub topics and push subscriptions. To access the Pub/Sub API and manage event triggers, the Eventarc API must be protected within the same VPC Service Controls service perimeter as the Pub/Sub API.

We recommend that you protect all services when creating a service perimeter.

## Eventarc Advanced

  * An Eventarc Advanced bus outside of a service perimeter can't receive events from Google Cloud projects inside the perimeter. An Eventarc Advanced bus inside of a perimeter can't route events to a consumer outside of the perimeter.

    * To publish to an Eventarc Advanced bus, the source of an event must be inside the same service perimeter as the bus.
    * To consume a message, an event consumer must be inside the same service perimeter as the bus.
  * You can verify VPC Service Controls support for the `Enrollment`, `GoogleApiSource`, `MessageBus`, and `Pipeline` resources by viewing platform logs on ingress.




## Eventarc Standard

  * In projects protected by a service perimeter, Eventarc Standard is bound by the same limitations as Pub/Sub:

    * When routing events to Cloud Run destinations, you can only create new Pub/Sub push subscriptions when the push endpoints are set to Cloud Run services with default `run.app` URLs. [Custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains) don't work.

    * When [routing events to Workflows destinations](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc) for which the Pub/Sub push endpoint is set to a Workflows execution, you can only create new Pub/Sub push subscriptions through Eventarc. Note that the service account used for push authentication for the Workflows endpoint must be included in the service perimeter.

  * VPC Service Controls blocks the creation of Eventarc triggers for [internal HTTP endpoints](https://docs.cloud.google.com/eventarc/standard/docs/vpc-endpoints/route-vpc-internal-endpoint-events). VPC Service Controls protection does not apply when routing events to such destinations.




## What's next

  * To learn more about VPC Service Controls, see the [overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

  * For best practices for enabling VPC Service Controls, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable).

  * For best practices for designing service perimeters, see [Design and architect service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters).

  * To set up a service perimeter, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
