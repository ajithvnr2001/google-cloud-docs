---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass/
title: ApiClass \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:03.780836+00:00
---

# ApiClass  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiClass Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiClass

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface ApiClass

Annotation for configuration specific to an API class.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[apiKeyRequired](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#apiKeyRequired--)` Whether or not an API key is required.  
`java.lang.String[]` | `[audiences](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#audiences--)` Audience for IdTokens, applicable to all methods of the API class unless overridden by `@ApiMethod#audiences`.  
`java.lang.Class<? extends [Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config")>[]` | `[authenticators](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#authenticators--)` Custom authenticators, applicable to all methods of the API class unless overridden by `@ApiMethod#authenticators`.  
`[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")` | `[authLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#authLevel--)` Set frontend auth level, applicable to all methods of the API unless overridden by `@ApiMethod#authLevel`.  
`java.lang.String[]` | `[clientIds](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#clientIds--)` Client IDs allowed to call this method, applicable to all methods of the API class unless overridden by `@ApiMethod#clientIds`.  
`[ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config")[]` | `[issuerAudiences](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#issuerAudiences--)` Audiences for individual issuers, applicable to all methods of the API unless overridden by [`ApiMethod.issuerAudiences()`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#issuerAudiences--).  
`java.lang.Class<? extends PeerAuthenticator>[]` | `[peerAuthenticators](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#peerAuthenticators--)` Custom peer authenticators, applicable to all methods of the API class unless overridden by `@ApiMethod#peerAuthenticators`.  
`java.lang.String` | `[resource](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#resource--)` The name (in plural) of the resource collection.  
`java.lang.String[]` | `[scopes](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#scopes--)` OAuth 2 scopes, one of which is required for calling this method, applicable to all methods of the API class unless overridden by `@ApiMethod#scopes`.  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[useDatastoreForAdditionalConfig](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#useDatastoreForAdditionalConfig--)` `AnnotationBoolean.TRUE` to request that overriding configuration be loaded from the appengine datastore.  



  *     * ### Element Detail

      * #### resource
            
            public abstract java.lang.String resource

The name (in plural) of the resource collection. It is used as a part of the RESTful path and RPC method name. If it is left empty, a value is deduced from inspecting each endpoint method.

Default:
    ""
    *       * #### authLevel
            
            public abstract [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") authLevel

Set frontend auth level, applicable to all methods of the API unless overridden by `@ApiMethod#authLevel`.

Default:
    com.google.api.server.spi.config.AuthLevel.UNSPECIFIED
    *       * #### scopes
            
            public abstract java.lang.String[] scopes

OAuth 2 scopes, one of which is required for calling this method, applicable to all methods of the API class unless overridden by `@ApiMethod#scopes`.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### audiences
            
            public abstract java.lang.String[] audiences

Audience for IdTokens, applicable to all methods of the API class unless overridden by `@ApiMethod#audiences`.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### issuerAudiences
            
            public abstract [ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config")[] issuerAudiences

Audiences for individual issuers, applicable to all methods of the API unless overridden by [`ApiMethod.issuerAudiences()`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#issuerAudiences--). This is only meant to be used with EspAuthenticator in endpoints-framework-auth.

Default:
    @com.google.api.server.spi.config.ApiIssuerAudience(name="_UNSPECIFIED_LIST_STRING_VALUE", audiences="_UNSPECIFIED_LIST_STRING_VALUE")
    *       * #### clientIds
            
            public abstract java.lang.String[] clientIds

Client IDs allowed to call this method, applicable to all methods of the API class unless overridden by `@ApiMethod#clientIds`.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### authenticators
            
            public abstract java.lang.Class<? extends [Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config")>[] authenticators

Custom authenticators, applicable to all methods of the API class unless overridden by `@ApiMethod#authenticators`.

Default:
    com.google.api.server.spi.config.Authenticator.class
    *       * #### peerAuthenticators
            
            public abstract java.lang.Class<? extends PeerAuthenticator>[] peerAuthenticators

Custom peer authenticators, applicable to all methods of the API class unless overridden by `@ApiMethod#peerAuthenticators`.

Default:
    <error>
    *       * #### useDatastoreForAdditionalConfig
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") useDatastoreForAdditionalConfig

`AnnotationBoolean.TRUE` to request that overriding configuration be loaded from the appengine datastore.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### apiKeyRequired
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") apiKeyRequired

Whether or not an API key is required. This is used to output a Swagger specification and has no effect unless used with endpoints-management-control-appengine.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
