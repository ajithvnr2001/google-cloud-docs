---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/parameter-and-return-types/
title: Supported parameter and return types \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:03.669727+00:00
---

# Supported parameter and return types  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/parameter-and-return-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Supported parameter and return types Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the data types you can use as API parameter types in the path or query parameters for your a backend API methods, and the types you can use as method return types or request body types.

## Supported types for path and query parameters

The supported types for path and query parameter are the following:

  * `java.lang.String`
  * `java.lang.Boolean` and `boolean`
  * `java.lang.Integer` and `int`
  * `java.lang.Long` and `long`
  * `java.lang.Float` and `float`
  * `java.lang.Double` and `double`
  * `java.util.Date`
  * `com.google.api.server.spi.types.DateAndTime`
  * `com.google.api.server.spi.types.SimpleDate`
  * Any `enum`
  * Any array or `java.util.Collection` of the types listed here. Arrays or collections of other types aren't supported.



To specify a parameter as either a path or query parameter, annotate the parameter with [`@Named`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#named). For example:
    
    
    public Resource get(@Named("id") int id) { … }
    

### Path parameters

Path parameters are the method parameters included in the `path` property of the [`@ApiMethod`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#apimethod_method-scoped_annotations) annotation. If `path` is unspecified, any parameters not annotated with [`@Nullable`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#nullable) or `@DefaultValue` are automatically added to the path as path parameters. For example:
    
    
    public Resource get(@Named("id") int id) { … }
    

To manually add a parameter to `path`, include the parameter name in `{}` marks in the path. Parameters manually added to `path` cannot be annotated with `@Nullable` or `@DefaultValue`. For example:
    
    
    @ApiMethod(path = "resources/{id}")
    public Resource get(@Named("id") int id) { … }
    

### Query parameters

Query parameters are the method parameters not included in the `path` property of the `@ApiMethod` annotation. Note that optional parameters, namely, those annotated with `@Nullable` or `@DefaultValue`, are never automatically added to `path`, so they are automatically query parameters if no `path` is specified. For example:
    
    
    public Resource get(@Named("id") @Nullable int id) { … }
    

If `path` is specified, you can make parameters be query parameters by not including them in the `path`. For example:
    
    
    @ApiMethod(path = "resources")
    public Resource get(@Named("id") int id) { … }
    

## Injected types

Injected types are those types that receive special treatment by Cloud Endpoints Frameworks. If such a type is used as a method parameter, it isn't made a part of the API. Instead, the parameter is filled in by Endpoints Frameworks.

The injected types are the following:

  * `com.google.appengine.api.users.User`
  * `javax.servlet.http.HttpServletRequest`
  * `javax.servlet.ServletContext`



## Entity types

In the Endpoints Frameworks documentation, _entity types_ are synonymous with [Java Beans](https://wikipedia.org/wiki/JavaBeans). The classes that you define for use in your API must:

  * Have a public constructor that takes no arguments.
  * Control access to private properties using [getters and setters](https://wikipedia.org/wiki/Mutator_method). Additionally, each setter must take only one parameter.



Typically entity types also implement [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html), but this isn't a requirement to use Endpoints Frameworks.

Don't use the [`@Named`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#named) annotation for entity type parameters.

## The request body

When you pass an entity type as a parameter in a method, the properties in the entity type are mapped to JSON fields in the request body. Your methods must contain only one entity type parameter. For example:
    
    
    public Resource set(Resource resource) { … }
    

You can include non-entity type parameters and an entity type parameter in a method. For example:
    
    
    @ApiMethod(name = "echo")
    public Message echo(Message message, @Named("n") @Nullable Integer n) { … }
    

In the preceding example, the properties in the `message` parameter are mapped to JSON fields in the request body. The [`@Nullable`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#nullable) annotation indicates that the `n` parameter is optional, so it is passed as a query parameter.

## The response object

The method return value must be one of the following:

  * An entity type
  * A [generic type](https://wikipedia.org/wiki/Generics_in_Java)
  * CollectionResponse (`com.google.api.server.spi.response.CollectionResponse`) or a subclass of CollectionResponse



The JSON fields in the response object are mapped from the properties in the return value.

**Note:** Returning a simple type, such as `String` or `int`, an array or an entity type with a parameterized constructor isn't supported.

## Effect of `@ApiTransformer` on types

If you use [`@ApiTransformer`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#apitransformer), you need to be aware of how the type is impacted by the transformation.

### `@ApiTransformer` and parameter types

When an `@ApiTransformer` is used, whether or not the resulting method parameter is considered a _parameter type_ depends on the result of transformation, _not on the original type_. If a type is transformed to a parameter type, the method parameter is considered an API parameter and must be annotated with `@Named`.

### `@ApiTransformer` and entity types

Similarly, whether or not a method parameter or return type is considered an _entity type_ depends on the result of transformation, not on the original type. If a type is transformed to an entity type, the type can be used as a return type, and when used as a method parameter, it cannot be annotated with `@Named` as it is considered an entity type.

### `@ApiTransformer` and injected types

Injected types aren't affected by an `@ApiTransformer`. A method parameter is only considered an injected type if its original non-transformed type is an injected type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
