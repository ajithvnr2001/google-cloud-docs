---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api/
title: Api \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:03.419322+00:00
---

# Api  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Api Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type Api

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface Api

Annotation for API-wide configuration.




  *     * ### Field Summary

Fields Modifier and Type | Fields and Description  
---|---  
`static int` | `[UNSPECIFIED_INT](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#UNSPECIFIED_INT)`  
`static java.lang.String` | `[UNSPECIFIED_STRING_FOR_LIST](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#UNSPECIFIED_STRING_FOR_LIST)`  
    * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[apiKeyRequired](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#apiKeyRequired--)` Whether or not an API key is required.  
`java.lang.String[]` | `[audiences](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#audiences--)` Audience for IdTokens, applicable to all methods of the API unless overridden by `@ApiClass#audiences` or `@ApiMethod#audiences`.  
`[ApiAuth](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiAuth.html "annotation in com.google.api.server.spi.config")` | `[auth](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#auth--)` Configures authentication information.  
`java.lang.Class<? extends [Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config")>[]` | `[authenticators](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#authenticators--)` Custom authenticators.  
`[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")` | `[authLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#authLevel--)` Set frontend auth level, applicable to all methods of the API unless overridden by `@ApiClass#authLevel` or `@ApiMethod#authLevel`.  
`java.lang.String` | `[backendRoot](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#backendRoot--)` Backend root URL, e.g.  
`ApiCacheControl` | `[cacheControl](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#cacheControl--)` Configures the Cache-Control header in the response.  
`java.lang.String` | `[canonicalName](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#canonicalName--)` Optional name, which indicates how an API name should be split into parts.  
`java.lang.String[]` | `[clientIds](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#clientIds--)` Client IDs allowed to call this method, applicable to all methods of the API unless overridden by `@ApiClass#clientIds` or `@ApiMethod#clientIds`.  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[defaultVersion](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#defaultVersion--)` Marks this version of an API as the default version to use when a JSON-RPC call is executed against the API.  
`java.lang.String` | `[description](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#description--)` Description of this API.  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[discoverable](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#discoverable--)` Whether or not the API is discoverable.  
`java.lang.String` | `[documentationLink](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#documentationLink--)` A link to human readable documentation for the API.  
`[ApiFrontendLimits](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html "annotation in com.google.api.server.spi.config")` | `[frontendLimits](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#frontendLimits--)` Configures quota enforcement.  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[isAbstract](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#isAbstract--)` `true` if this API configuration is used as the base for another.  
`[ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config")[]` | `[issuerAudiences](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#issuerAudiences--)` Audiences for individual issuers, applicable to all methods of the API unless overridden by [`ApiClass.issuerAudiences()`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#issuerAudiences--) or [`ApiMethod.issuerAudiences()`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#issuerAudiences--).  
`[ApiIssuer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuer.html "annotation in com.google.api.server.spi.config")[]` | `[issuers](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#issuers--)` Custom JWT issuer configurations.  
`[ApiLimitMetric](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiLimitMetric.html "annotation in com.google.api.server.spi.config")[]` | `[limitDefinitions](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#limitDefinitions--)` Rate limiting metric definitions that are used in this API.  
`java.lang.String` | `[name](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#name--)` Name of the API, e.g.  
`[ApiNamespace](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html "annotation in com.google.api.server.spi.config")` | `[namespace](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#namespace--)` Configures namespacing for generated clients.  
`java.lang.Class<? extends PeerAuthenticator>[]` | `[peerAuthenticators](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#peerAuthenticators--)` Custom peer authenticators.  
`java.lang.String` | `[resource](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#resource--)` The name (in plural) of the resource collection.  
`java.lang.String` | `[root](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#root--)` Frontend root URL, e.g.  
`java.lang.String[]` | `[scopes](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#scopes--)` OAuth 2 scopes, one of which is required for calling this method, applicable to all methods of the API unless overridden by `@ApiClass#scopes` or `@ApiMethod#scopes`.  
`java.lang.String` | `[title](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#title--)` The title of an API.  
`java.lang.Class<? extends [Transformer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "interface in com.google.api.server.spi.config")<?,?>>[]` | `[transformers](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#transformers--)` Custom transformers to be used for this API.  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[useDatastoreForAdditionalConfig](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#useDatastoreForAdditionalConfig--)` `AnnotationBoolean.TRUE` to request that overriding configuration be loaded from the appengine datastore for all API classes except for those classes that override using `@ApiClass#useDatastoreForAdditionalConfig`.  
`java.lang.String` | `[version](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html#version--)` Version of the API, e.g.  



  *     * ### Field Detail

      * #### UNSPECIFIED_INT
            
            public static final int UNSPECIFIED_INT

    *       * #### UNSPECIFIED_STRING_FOR_LIST
            
            public static final java.lang.String UNSPECIFIED_STRING_FOR_LIST

    * ### Element Detail

      * #### root
            
            public abstract java.lang.String root

Frontend root URL, e.g. "https://example.appspot.com/_ah/api". All api methods will be exposed below this path. This will default to "https://yourapp.appspot.com/_ah/api".

Default:
    ""
    *       * #### name
            
            public abstract java.lang.String name

Name of the API, e.g. "guestbook". This is used as the prefix for all api methods and paths. If not set a default of "myapi" will be used.

Default:
    ""
    *       * #### canonicalName
            
            public abstract java.lang.String canonicalName

Optional name, which indicates how an API name should be split into parts. This is useful in generating better client library names. For example, the API name might be "myapi" and the canonical name might be "My API", which indicates that the camel case name should be myApi while the underscore name should be my_api.

Default:
    ""
    *       * #### version
            
            public abstract java.lang.String version

Version of the API, e.g. "v0.2". If not set a default of "v1" will be used.

Default:
    ""
    *       * #### title
            
            public abstract java.lang.String title

The title of an API. This is the title displayed by API Explorer.

Default:
    ""
    *       * #### description
            
            public abstract java.lang.String description

Description of this API. This will be exposed in the discovery service to describe your API, and may also be used to generate documentation.

Default:
    ""
    *       * #### documentationLink
            
            public abstract java.lang.String documentationLink

A link to human readable documentation for the API. By default no link is is exposed in discovery.

Default:
    ""
    *       * #### backendRoot
            
            public abstract java.lang.String backendRoot

Backend root URL, e.g. "https://example.appspot.com/_ah/spi". This is the root of all backend method calls. This will default to "https://yourapp.appspot.com/_ah/spi". Non-secure http URLs will be automatically converted to use https.

Default:
    ""
    *       * #### auth
            
            public abstract [ApiAuth](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiAuth.html "annotation in com.google.api.server.spi.config") auth

Configures authentication information. See [`ApiAuth`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiAuth.html "annotation in com.google.api.server.spi.config") for details.

Default:
    @com.google.api.server.spi.config.ApiAuth
    *       * #### frontendLimits
            
            public abstract [ApiFrontendLimits](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html "annotation in com.google.api.server.spi.config") frontendLimits

Configures quota enforcement. See [`ApiFrontendLimits`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html "annotation in com.google.api.server.spi.config") for details.

Default:
    @com.google.api.server.spi.config.ApiFrontendLimits
    *       * #### cacheControl
            
            public abstract ApiCacheControl cacheControl

Configures the Cache-Control header in the response. See `ApiCacheControl` for details.

Default:
    <error>
    *       * #### authLevel
            
            public abstract [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") authLevel

Set frontend auth level, applicable to all methods of the API unless overridden by `@ApiClass#authLevel` or `@ApiMethod#authLevel`.

Default:
    com.google.api.server.spi.config.AuthLevel.UNSPECIFIED
    *       * #### scopes
            
            public abstract java.lang.String[] scopes

OAuth 2 scopes, one of which is required for calling this method, applicable to all methods of the API unless overridden by `@ApiClass#scopes` or `@ApiMethod#scopes`.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### audiences
            
            public abstract java.lang.String[] audiences

Audience for IdTokens, applicable to all methods of the API unless overridden by `@ApiClass#audiences` or `@ApiMethod#audiences`.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### issuers
            
            public abstract [ApiIssuer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuer.html "annotation in com.google.api.server.spi.config")[] issuers

Custom JWT issuer configurations. This is only meant to be used with EspAuthenticator in endpoints-framework-auth.

Default:
    @com.google.api.server.spi.config.ApiIssuer(name="_UNSPECIFIED_LIST_STRING_VALUE")
    *       * #### issuerAudiences
            
            public abstract [ApiIssuerAudience](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiIssuerAudience.html "annotation in com.google.api.server.spi.config")[] issuerAudiences

Audiences for individual issuers, applicable to all methods of the API unless overridden by [`ApiClass.issuerAudiences()`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiClass.html#issuerAudiences--) or [`ApiMethod.issuerAudiences()`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethod.html#issuerAudiences--). This is only meant to be used with EspAuthenticator in endpoints-framework-auth.

Default:
    @com.google.api.server.spi.config.ApiIssuerAudience(name="_UNSPECIFIED_LIST_STRING_VALUE", audiences="_UNSPECIFIED_LIST_STRING_VALUE")
    *       * #### clientIds
            
            public abstract java.lang.String[] clientIds

Client IDs allowed to call this method, applicable to all methods of the API unless overridden by `@ApiClass#clientIds` or `@ApiMethod#clientIds`.

Default:
    "_UNSPECIFIED_LIST_STRING_VALUE"
    *       * #### authenticators
            
            public abstract java.lang.Class<? extends [Authenticator](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config")>[] authenticators

Custom authenticators. Applies to all methods of the API unless overridden by `@ApiClass#authenticators` or `@ApiMethod#authenticators`. See [`Authenticator`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Authenticator.html "interface in com.google.api.server.spi.config").

Default:
    com.google.api.server.spi.config.Authenticator.class
    *       * #### peerAuthenticators
            
            public abstract java.lang.Class<? extends PeerAuthenticator>[] peerAuthenticators

Custom peer authenticators. Applies to all methods of the API unless overridden by `@ApiClass#peerAuthenticators` or `@ApiMethod#peerAuthenticators`. See `PeerAuthenticator`.

Default:
    <error>
    *       * #### isAbstract
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") isAbstract

`true` if this API configuration is used as the base for another. Should be `false` for most situations.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### defaultVersion
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") defaultVersion

Marks this version of an API as the default version to use when a JSON-RPC call is executed against the API.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### resource
            
            public abstract java.lang.String resource

The name (in plural) of the resource collection. It is used as a part of the RESTful path and RPC method name. If it is left empty, a value is deduced from inspecting each endpoint method.

Default:
    ""
    *       * #### transformers
            
            public abstract java.lang.Class<? extends [Transformer](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "interface in com.google.api.server.spi.config")<?,?>>[] transformers

Custom transformers to be used for this API.

Default:
    {}
    *       * #### useDatastoreForAdditionalConfig
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") useDatastoreForAdditionalConfig

`AnnotationBoolean.TRUE` to request that overriding configuration be loaded from the appengine datastore for all API classes except for those classes that override using `@ApiClass#useDatastoreForAdditionalConfig`.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### namespace
            
            public abstract [ApiNamespace](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html "annotation in com.google.api.server.spi.config") namespace

Configures namespacing for generated clients. See [`ApiNamespace`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html "annotation in com.google.api.server.spi.config") for details.

Default:
    @com.google.api.server.spi.config.ApiNamespace(ownerDomain="", ownerName="")
    *       * #### discoverable
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") discoverable

Whether or not the API is discoverable. This prevents the JavaScript client from working, and by extension, the API Explorer.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### apiKeyRequired
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") apiKeyRequired

Whether or not an API key is required. This is used to output a Swagger specification and has no effect unless used with endpoints-management-control-appengine.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED
    *       * #### limitDefinitions
            
            public abstract [ApiLimitMetric](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiLimitMetric.html "annotation in com.google.api.server.spi.config")[] limitDefinitions

Rate limiting metric definitions that are used in this API.

Default:
    {}



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
