---
url: https://docs.cloud.google.com/eventarc/standard/docs/event-format/
title: Event format \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:38.099081+00:00
---

# Event format  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/event-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Event format Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

Eventarc delivers events, regardless of provider, to the target destination in a CloudEvents ([cloudevents.io](http://cloudevents.io/)) format in binary content mode.

CloudEvents is the Cloud Native Computing Foundation's [open standard specification](https://github.com/cloudevents/spec) for describing event metadata in a common way. Using a standard way to describe event metadata ensures consistency, accessibility, and portability.

A CloudEvent in binary content mode has its context attributes described as HTTP headers. The names of the HTTP headers are the context attribute names prefixed with `ce-`. The `Content-Type` header reflects the media type in which the event data is encoded.

Target destinations consume events using an [HTTP protocol binding](https://docs.cloud.google.com/eventarc/docs/cloudevents).

For Workflows destinations, the Workflows service converts the event to a [JSON object](https://docs.cloud.google.com/eventarc/docs/cloudevents-json), and passes the event into the workflow execution as a runtime argument.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
