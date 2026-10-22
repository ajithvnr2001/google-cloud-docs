---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/troubleshoot-providers/
title: Troubleshoot event publishing \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:33.355320+00:00
---

# Troubleshoot event publishing  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/troubleshoot-providers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Troubleshoot event publishing Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Eventarc lets you identify and resolve errors when publishing third-party events to a channel. Classifying transient and fatal publishing issues helps you fix channel connection failures and maintain reliable event delivery to your destinations.

## Error status

If event publishing fails, the error that is returned includes an error `status` field, the value of which corresponds to an error class:

HTTP code | Error status | Error class  
---|---|---  
409 | ABORTED | Transient  
429 | RESOURCE_EXHAUSTED | Transient  
499 | CANCELLED | Transient  
500 | INTERNAL | Transient  
500 | UNKNOWN | Transient  
503 | UNAVAILABLE | Transient  
504 | DEADLINE_EXCEEDED | Transient  
400 | FAILED_PRECONDITION | Fatal  
400 | INVALID_ARGUMENT | Fatal  
400 | OUT_OF_RANGE | Fatal  
401 | UNAUTHENTICATED | Fatal  
403 | PERMISSION_DENIED | Fatal  
409 | ALREADY_EXISTS | Fatal  
501 | UNIMPLEMENTED | Fatal  
404 | NOT_FOUND | Fatal Channel  
500 | DATA_LOSS | Fatal Channel  
  
## Error class

The error class indicates how you should handle the error:

Error class  
---  
Transient |  The publish request has failed due to a temporary condition. You can retry the process. Examples:

  * Publishing quota has been met.
  * An internal Eventarc error has occurred.

  
Fatal | Publishing this event can't succeed and can't be retried in its current form. Depending on the specific error, you can try altering or restructuring the event to correct the error, and then retry the publish request. Examples:

  * The event is malformed, or contains invalid input.
  * The publish request contains too many events.

  
Fatal Channel | The subscriber's channel can't be published to; either it no longer exists, or has become permanently disabled. This request can't be retried and you should stop all event publishing. You can safely delete the [`channelConnection`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channelConnections) resource. Examples:

  * The subscriber has deleted the connected channel.
  * The subscriber has deleted the Pub/Sub transport topic for the channel.

  
  
Learn more about the [error model for Google APIs](https://docs.cloud.google.com/apis/design/errors).

## Related information

  * To learn more about Eventarc, see the [overview](https://docs.cloud.google.com/eventarc/standard/docs/overview).
  * To resolve other issues that you might encounter, see [Troubleshoot issues](https://docs.cloud.google.com/eventarc/docs/troubleshooting).
  * To get additional help, see [Get support](https://docs.cloud.google.com/eventarc/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
