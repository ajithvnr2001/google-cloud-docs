---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi
title: Package com.google.appengine.spi (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:43.410788+00:00
---

# Package com.google.appengine.spi (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.spi (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Support for alternate implementations of Google App Engine services. **_This package is not intended for use by application code._**

If, for example, vendor X wanted to provide an alternate implementation of the DatastoreService, they would have to provide an implementation of [com.google.appengine.api.datastore.IDatastoreServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IDatastoreServiceFactory) that returns their implementation for [com.google.appengine.api.datastore.DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService).

Factory implementations are acquired using a [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider) registered with [ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory). These providers are typically discovered using java.util.ServiceLoader; see [com.google.appengine.spi.ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory) for details.

This package includes the utility ([ServiceProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceProvider) for inserting the appropriate "service" entries into a jar file.

## Classes 

### [FactoryProvider<I>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider)

A base class for service factory creation that can be registered with the ProviderRegistry.

### [ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory)

**This class is not intended for end users.**

Provide factory instances for AppEngine APIs. Each API will have an associated [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider) registered with this class. N.B. _Once <xref uid="com.google.appengine.spi.ServiceFactoryFactory._

To construct the runtime mapping, this class first uses `java.util.ServiceLoader` to find all registered [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider) entities using the `ClassLoader` of `ServiceFactoryFactory`. Finally, the explicitly registered providers <xref uid="com.google.appengine.spi.ServiceFactoryFactory._register(com.google.appengine.spi.FactoryProvider <I>)" data-throw-if-not-resolved="false">#register(FactoryProvider) are merged in._

__

__

_If`ServiceLoader` locates multiple providers for a given factory interface, the ambiguity can be resolved by using the [ServiceProvider#precedence](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceProvider#com_google_appengine_spi_ServiceProvider_precedence_) annotation property (higher precedence wins; _the google implementations all have precedence Integer.MIN_VALUE_). An exception is raised if the ambiguity cannot be resolved. Note that explicit registration (<xref uid="com.google.appengine.spi.ServiceFactoryFactory._register(com.google.appengine.spi.FactoryProvider <I>)" data-throw-if-not-resolved="false">#register(FactoryProvider)) always takes precedence (it does not honor the [ServiceProvider#precedence](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceProvider#com_google_appengine_spi_ServiceProvider_precedence_) annotation property).__

____

### [ServicesFile](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServicesFile)

A helper class for reading and writing Services files. See Also: java.util.ServiceLoader

## Annotation Types 

### [ServiceProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceProvider)

Specifies the precedence that [ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory) gives to the annotated [FactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.FactoryProvider).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
