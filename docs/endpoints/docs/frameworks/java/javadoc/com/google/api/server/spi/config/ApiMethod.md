---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod/
title: ApiMethod \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:08.577094+00:00
---

# ApiMethod  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiMethod Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiMethod

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=METHOD)
        public @interface ApiMethod

Annotation for API method configuration.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[apiKeyRequired](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#apiKeyRequired--)` Whether or not an API key is required.  
`java.lang.String[]` | `[audiences](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#audiences--)` Audience for IdTokens.  
`java.lang.Class<? extends [Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config")>[]` | `[authenticators](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#authenticators--)` Custom authenticators used for authentication for this method.  
`[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")` | `[authLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#authLevel--)` Set frontend auth level.  
`[ApiMethodCacheControl](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl.html "annotation in com.google.api.server.spi.config")` | `[cacheControl](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#cacheControl--)` Deprecated. ApiMethodCacheControl is deprecated and will be removed in a future version of Cloud Endpoints.  
`java.lang.String[]` | `[clientIds](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#clientIds--)` Client IDs allowed to call this method.  
`java.lang.String` | `[description](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#description--)` Description of this API method.  
`java.lang.String` | `[httpMethod](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#httpMethod--)` The HTTP method to use to access this method.  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[ignored](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#ignored--)` Whether or not API method should be ignored.  
`[ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config")[]` | `[issuerAudiences](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#issuerAudiences--)` Audiences for individual issuers.  
`[ApiMetricCost](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost.html "annotation in com.google.api.server.spi.config")[]` | `[metricCosts](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#metricCosts--)` A list of metric costs associated with this method.  
`java.lang.String` | `[name](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#name--)` The name for this method in the .api file.  
`java.lang.String` | `[path](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#path--)` The URI path to use to access this method.  
`java.lang.Class<? extends PeerAuthenticator>[]` | `[peerAuthenticators](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#peerAuthenticators--)` Custom peer authenticators used to verify peer for this method.  
`java.lang.String[]` | `[scopes](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#scopes--)` OAuth 2 scopes, one of which is required for calling this method.  



  *     * ### Element Detail

      * #### name
            
            public abstract java.lang.String name

The name for this method in the .api file. This will automatically be prefixed with `"<apiname>."` to create a unique name for the method. If not set the method name will be derived from the Java method name.

Default:
    ""
    *       * #### description
            
            public abstract java.lang.String description

Description of this API method. This will be exposed in the discovery service to describe your API method, and may also be used to generate documentation.

Default:
    ""
    *       * #### path
            
            public abstract java.lang.String path

The URI path to use to access this method. If not set a default will be created based on the Java method name.

Default:
    ""
    *       * #### httpMethod
            
            public abstract java.lang.String httpMethod

The HTTP method to use to access this method. If not set a default will be chosen based on the name of the method.

Default:
    ""
    *       * #### cacheControl
            
            @Deprecated
            public abstract [ApiMethodCacheControl](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl.html "annotation in com.google.api.server.spi.config") cacheControl

Deprecated. ApiMethodCacheControl is deprecated and will be removed in a future version of Cloud Endpoints.

Cache-Control header settings for this method. See [`ApiMethodCacheControl`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl.html "annotation in com.google.api.server.spi.config") for details.

Default:
    @com.google.api.server.spi.config.ApiMethodCacheControl
    *       * #### authLevel
            
            public abstract [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") authLevel

Set frontend auth level.

Default:
    com.google.api.server.spi.config.AuthLevel.UNSPECIFIED
    *       * #### scopes
            
            public abstract java.lang.String[] scopes

OAuth 2 scopes, one of which is required for calling this method.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### audiences
            
            public abstract java.lang.String[] audiences

Audience for IdTokens.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### issuerAudiences
            
            public abstract [ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config")[] issuerAudiences

Audiences for individual issuers. This is only meant to be used with EspAuthenticator in endpoints-framework-auth.

Default:
    @com.google.api.server.spi.config.ApiIssuerAudience(name="_UNSPECIFIED_LIST_STRING_VALUE", audiences="_UNSPECIFIED_LIST_STRING_VALUE")
    *       * #### clientIds
            
            public abstract java.lang.String[] clientIds

Client IDs allowed to call this method.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### authenticators
            
            public abstract java.lang.Class<? extends [Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config")>[] authenticators

Custom authenticators used for authentication for this method.

Default:
    com.google.api.server.spi.config.Authenticator.class
    *       * #### peerAuthenticators
            
            public abstract java.lang.Class<? extends PeerAuthenticator>[] peerAuthenticators

Custom peer authenticators used to verify peer for this method.

Default:
    <error>
    *       * #### ignored
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") ignored

Whether or not API method should be ignored.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### apiKeyRequired
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") apiKeyRequired

Whether or not an API key is required. This is used to output a Swagger specification and has no effect unless used with endpoints-management-control-appengine.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### metricCosts
            
            public abstract [ApiMetricCost](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost.html "annotation in com.google.api.server.spi.config")[] metricCosts

A list of metric costs associated with this method.

Default:
    {}



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
