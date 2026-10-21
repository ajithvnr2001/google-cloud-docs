---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities
title: Package com.google.appengine.api.capabilities (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:36.637096+00:00
---

# Package com.google.appengine.api.capabilities (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.capabilities (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides status information about the services available via the GAE APIs. Status details include current availability, scheduled downtime and outages. See Also: [com.google.appengine.api.capabilities.CapabilitiesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesService), [The Capabilities Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/capabilities/).

## Classes 

### [CapabilitiesPb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb)

### [CapabilitiesPb.CapabilityConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfig)

### [CapabilitiesPb.CapabilityConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfig.Builder)

### [CapabilitiesPb.CapabilityConfigList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfigList)

### [CapabilitiesPb.CapabilityConfigList.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfigList.Builder)

### [CapabilitiesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesServiceFactory)

Factory for creating a [CapabilitiesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesService).

### [Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability)

A capability represents a particular feature or set of features available on the App Engine platform.

To check the availability of a particular capability, use the [CapabilitiesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesService) API.

### [CapabilityServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb)

### [CapabilityServicePb.IsEnabledRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledRequest)

### [CapabilityServicePb.IsEnabledRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledRequest.Builder)

### [CapabilityServicePb.IsEnabledResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledResponse)

### [CapabilityServicePb.IsEnabledResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledResponse.Builder)

### [CapabilityState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityState)

Represents the state of a [Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability).

The state of a capability is valid at a particular point in time.

If a particular capability is enabled at time T, there is no guarantee as to if it will be available at time T+1. When a maintenance period is scheduled, there will be usually advance notice as to when the capability is disabled.

### [ICapabilitiesServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.ICapabilitiesServiceFactoryProvider)

Factory provider for [ICapabilitiesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.ICapabilitiesServiceFactory).

**Note:** This class is not intended for end users.

## Interfaces 

### [CapabilitiesPb.CapabilityConfigListOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfigListOrBuilder)

### [CapabilitiesPb.CapabilityConfigOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfigOrBuilder)

### [CapabilitiesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesService)

Allows applications to identify API outages. This service is **deprecated** except for the specific case of querying whether datastore writes are enabled.

### [CapabilityServicePb.IsEnabledRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledRequestOrBuilder)

### [CapabilityServicePb.IsEnabledResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledResponseOrBuilder)

### [ICapabilitiesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.ICapabilitiesServiceFactory)

Factory for creating a [CapabilitiesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesService).

## Enums 

### [CapabilitiesPb.CapabilityConfig.Status](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilitiesPb.CapabilityConfig.Status)

### [CapabilityServicePb.IsEnabledResponse.SummaryStatus](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityServicePb.IsEnabledResponse.SummaryStatus)

### [CapabilityStatus](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.CapabilityStatus)

Represents the status of a [Capability](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.capabilities.Capability).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
