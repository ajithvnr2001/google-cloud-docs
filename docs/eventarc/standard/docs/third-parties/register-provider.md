---
url: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/register-provider/
title: Register as an event provider \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:56.562360+00:00
---

# Register as an event provider  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/third-parties/register-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Register as an event provider Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Eventarc allows events to be asynchronously delivered from third-party providers to interested subscribers. For details, see [Third-party events in Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/third-parties-overview).

The following information is required when you [register as an event provider using this form](https://forms.gle/n5EnafzdsK4tBQek9).

Ensure that all the details you provide are accurate and complete. If you have any questions or for more information, contact [eventarc-integration@google.com](mailto:%20eventarc-integration@google.com.).

General information | Description  
---|---  
Provider display name | The event provider name. This name will be visible to event subscribers through the Eventarc interface.  For example: "Company Name"   
Provider name |  An identifier that subscribers will use when subscribing to events from the event provider.  The name should consist of lowercase alphanumeric characters.  For example: `companyname` or `company-name-123`  
Supported regions |  A list of regions supported by the event provider. Subscribers will only be able to subscribe to events (that is, create channels and triggers) for this event provider in these regions.  This list must be a subset of the [regions supported by Eventarc](https://docs.cloud.google.com/eventarc/docs/locations#regions). It is expected that all Eventarc regions will be supported in due course; until then, you can ask for the addition of new regions through the registration form.  Note that dual and multi-regions are not supported for third-party events.   
Publisher project | The Google Cloud project ID that the event provider will use to publish events. You can find your project ID on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.  
Event types |  The list of event types published by the event provider. A subscriber's trigger can route exactly one event type from one event provider.  Event types must follow the format: `PROVIDER_ID.PROVIDER_SPECIFIED_TYPE_NAME.VERSION.ACTION` For example: `companyname.fooProcess.v1.resourceUpdated` The `PROVIDER_SPECIFIED_TYPE_NAME` can include multiple segments (for example, `foo.processA`) or can be omitted if not required.  If you don't supply any event types, the default event type of `PROVIDER_ID.v1.event` is used.   
Event type description  
(for each event type) | A user-visible description of each event type.  
Event attributes  
(for each event type) |  This is the list of attributes available to filter events of each event type. Each attribute can be included (with any value) as an [extension context attribute](https://github.com/cloudevents/spec/blob/v1.0.1/spec.md#extension-context-attributes) in any published event.  Each subscriber's trigger can filter on these attributes to limit the events matched and delivered to the trigger destination.   
Development and test information | Description  
Test subscriber projects | A list of Google Cloud project IDs authorized to subscribe to events for testing or during any alpha period. You can find project IDs on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.  
Other | Description  
Contact email | The email address to which information should be sent.  
Customer issues | For any customer problems related to your events, how you would like Eventarc to convey these issues to you.   
  
## What's next

  * [Learn more about Eventarc](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
