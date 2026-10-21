---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/package-summary/
title: com.google.api.server.spi.config \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:02.862707+00:00
---

# com.google.api.server.spi.config  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/package-summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  com.google.api.server.spi.config Stay organized with collections  Save and categorize content based on your preferences. 

# Package com.google.api.server.spi.config

  * Interface Summary Interface | Description  
---|---  
[Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config") |  Interface for Endpoints authenticators.  
[Transformer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "interface in com.google.api.server.spi.config")<TFrom,TTo> |  An interface used to transform between a bean type and another type during JSON serialization.  
  * Class Summary Class | Description  
---|---  
[ApiMethod.HttpMethod](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.HttpMethod.html "class in com.google.api.server.spi.config") |  Constants of HTTP method names  
[DefaultAnnotation](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/DefaultAnnotation.html "class in com.google.api.server.spi.config") |  Class used for creation of a default instance of an annotation.  
  * Enum Summary Enum | Description  
---|---  
[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") |  Enum allowing a boolean flag or unspecified.  
[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") |  Enum to choose frontend authentication level for use in endpoints annotations.  
  * Annotation Types Summary Annotation Type | Description  
---|---  
[Api](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") |  Annotation for API-wide configuration.  
[ApiAuth](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiAuth.html "annotation in com.google.api.server.spi.config") |  Annotation for API authentication configuration.  
[ApiClass](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html "annotation in com.google.api.server.spi.config") |  Annotation for configuration specific to an API class.  
[ApiFrontendLimitRule](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html "annotation in com.google.api.server.spi.config") |  Annotation for configuration of API quota frontend limit rules.  
[ApiFrontendLimits](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html "annotation in com.google.api.server.spi.config") |  Annotation for configuration of API quota frontend limits.  
[ApiIssuer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuer.html "annotation in com.google.api.server.spi.config") |  Annotation to specify a JWT issuer configuration.  
[ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config") |  An annotation that specifies a list of allowed audiences for an issuer.  
[ApiLimitMetric](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiLimitMetric.html "annotation in com.google.api.server.spi.config") |  A rate limiting metric.  
[ApiMethod](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html "annotation in com.google.api.server.spi.config") |  Annotation for API method configuration.  
[ApiMethodCacheControl](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl.html "annotation in com.google.api.server.spi.config") | Deprecated ApiMethodCacheControl is deprecated and will be removed in a future version of Cloud Endpoints.  
[ApiMetricCost](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost.html "annotation in com.google.api.server.spi.config") |  Metric cost definition for a method.  
[ApiNamespace](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html "annotation in com.google.api.server.spi.config") |  Fields populated in Discovery in order to proper namespace generated clients.  
[ApiReference](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference.html "annotation in com.google.api.server.spi.config") |  Annotation to specify that the annotated class should use the same [`Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") configuration information as the referenced class.  
[ApiResourceProperty](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiResourceProperty.html "annotation in com.google.api.server.spi.config") |  Annotation for configuring bean properties for API resources.  
[ApiTransformer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiTransformer.html "annotation in com.google.api.server.spi.config") |  An annotation for customizing API output by simple type conversion.  
[DefaultValue](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/DefaultValue.html "annotation in com.google.api.server.spi.config") |  Default value for parameters.  
[Description](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Description.html "annotation in com.google.api.server.spi.config") |  Annotation to specify the description of an API parameter.  
[Named](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Named.html "annotation in com.google.api.server.spi.config") |  Annotation to specify the name of an API parameter.  
[Nullable](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Nullable.html "annotation in com.google.api.server.spi.config") |  Annotation to specify that an API parameter is optional.  
[Singleton](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Singleton.html "annotation in com.google.api.server.spi.config") |  Annotation used with Authenticator and PeerAuthenticator to denote only one instance will be created for optimization.  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
