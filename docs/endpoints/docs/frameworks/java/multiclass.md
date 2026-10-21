---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass/
title: Multiclass APIs \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:18.868043+00:00
---

# Multiclass APIs  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Multiclass APIs Stay organized with collections  Save and categorize content based on your preferences. 

If a single API is particularly complex, you might want to implement it from multiple Java classes. To make different classes part of the same API, you must:

  * Give each class the same `name` and `version` strings in their [`@Api` annotation](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#api_api-scoped_annotations).
  * Add class APIs as a comma-separated list in `web.xml`.



For example, the following two classes are both part of the `tictactoe` API:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeA { … }
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeB { … }
    

The API configuration is specified through the `@Api` annotation properties. However, for multiple classes in the same API, the `@Api` requirements extend beyond simply having the same `name` and `version` strings in the `@Api` annotation for each class. In fact, your backend API will not work if there are _any_ differences in the API configurations specified in the classes' `@Api` properties. Any difference in the `@Api` properties for classes in a multiclass API result in an "ambiguous" API configuration, which will not work in Cloud Endpoints Frameworks for App Engine.

**Note:** For a way to specify different properties for classes without using `@Api` properties, see Using `@ApiClass` for properties that can differ between classes.

There are several ways to create a unambiguous multiclass API:

  * Manually ensure that all classes in a single API have the exact same `@Api` annotation properties.
  * Use annotation inheritance through Java inheritance. In this inheritance, all classes in a single API inherit the same API configuration from a common `@Api`-annotated base class.
  * Use annotation inheritance through the `@ApiReference` annotation on all classes in a single API to have them reference the same API configuration from a common `@Api`-annotated class.



## Using `@ApiClass` for properties that can differ between classes

To use this feature, you need the following import:
    
    
    import com.google.api.server.spi.config.ApiClass;
    

While all properties in the `@Api` annotation must match for all classes in an API, you can additionally use the `@ApiClass` annotation to provides properties that don't need to be exactly the same between classes. For example:
    
    
    // API methods implemented in this class allow only "clientIdA".
    @Api(name = "tictactoe", version = "v1")
    @ApiClass(clientIds = { "clientIdA" })
    class TicTacToeA { … }
    
    // API methods implemented in this class provide unauthenticated access.
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeB { … }
    

where `TicTacToeA` limits access by using a whitelist of client IDs containing the allowed client ID, and `TicTacToeB` doesn't limit access.

All properties provided by the `@ApiClass` annotation have an equivalent property in the `@Api` annotation. Note that the `@Api` equivalent property acts as the API-wide default. If there is an API-wide default for that same property, specified in `@Api`, the class-specific `@ApiClass` property overrides the API-wide default.

The following examples illustrate the overriding of `@Api` properties by the class-specific `@ApiClass` equivalents:
    
    
    // For this class "boards" overrides "games".
    @Api(name = "tictactoe", version = "v1", resource = "games")
    @ApiClass(resource = "boards")
    class TicTacToeBoards { … }
    
    // For this class "scores" overrides "games".
    @Api(name = "tictactoe", version = "v1", resource = "games")
    @ApiClass(resource = "scores")
    class TicTacToeScores { … }
    
    // For this class, the API-wide default "games" is used as the resource.
    @Api(name = "tictactoe", version = "v1", resource = "games")
    class TicTacToeGames { … }
    

## Annotation inheritance

The `@Api` and `@ApiClass` annotation properties can be inherited from from other classes, and individual properties can be overridden either through Java inheritance or `@ApiReference` inheritance

### Using Java inheritance

A class that extends another class with `@Api` or `@ApiClass` annotations behaves as if annotated with the same properties. For example:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeBase { … }
    
    // TicTacToeA and TicTacToeB both behave as if they have the same @Api annotation as
    // TicTacToeBase
    class TicTacToeA extends TicTacToeBase { … }
    class TicTacToeB extends TicTacToeBase { … }
    

Annotations are only inherited through Java subclassing, not through interface implementation. For example:
    
    
    @Api(name = "tictactoe", version = "v1")
    interface TicTacToeBase { … }
    // Does *not* behave as if annotated.
    class TicTacToeA implements TicTacToeBase { … }
    

As a result, _there is no support for any sort of multiple inheritance_ of frameworks annotations.

Inheritance works for `@ApiClass` too:
    
    
    @ApiClass(resource = "boards")
    class BoardsBase { … }
    
    // TicTacToeBoards behaves as if annotated with the @ApiClass from BoardsBase.
    // Thus, the "resource" property will be "boards".
    @Api(name = "tictactoe", version = "v1", resource = "scores")
    class TicTacToeBoards extends BoardsBase { … }
    

where `TicTacToeBoards` inherits the `resource` property value `boards` from `BoardsBase`, thus overriding the `resource` property setting (`scores`) in its `@Api` annotation. Remember that if any class has specified the resource property in the `@Api` annotation, all of the classes need to specify that same setting in the `@Api` annotation; this inheritance technique lets you override that `@Api` property.

### Using `@ApiReference` inheritance

To use this feature, you need the following import:
    
    
    import com.google.api.server.spi.config.ApiReference;
    

The `@ApiReference` annotation provides an alternate way to specify annotation inheritance. A class that uses `@ApiReference` to specify another class with `@Api` or `@ApiClass` annotations behaves as if annotated with the same properties. For example:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeBase { … }
    
    // TicTacToeA behaves as if it has the same @Api annotation as TicTacToeBase
    @ApiReference(TicTacToeBase.class)
    class TicTacToeA { … }
    

If both Java inheritance and the `@ApiReference` are used, the annotations inherit through the `@ApiReference` annotation only. `@Api` and `@ApiClass` annotations on the class inherited through Java inheritance are ignored. For example:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeBaseA { … }
    @Api(name = "tictactoe", version = "v2")
    class TicTacToeBaseB { … }
    
    // TicTacToe will behave as if annotated the same as TicTacToeBaseA, not TicTacToeBaseB.
    // The value of the "version" property will be "v1".
    @ApiReference(TicTacToeBaseA.class)
    class TicTacToe extends TicTacToeBaseB { … }
    

### Overriding inherited configuration

Whether inheriting configuration by using Java inheritance or `@ApiReference`, you can override the inherited configuration by using a new `@Api` or `@ApiClass` annotation. Only configuration properties specified in the new annotation are overridden. Properties that are unspecified are still inherited. For example:
    
    
    @Api(name = "tictactoe", version = "v2")
    class TicTacToe { … }
    
    // Checkers will behave as if annotated with name = "checkers" and version = "v2"
    @Api(name = "checkers")
    class Checkers extends TicTacToe { … }
    

Overriding inheritance works for `@ApiClass` too:
    
    
    @Api(name = "tictactoe", version = "v1")
    @ApiClass(resource = "boards", clientIds = { "c1" })
    class Boards { … }
    
    // Scores will behave as if annotated with resource = "scores" and clientIds = { "c1" }
    @ApiClass(resource = "scores")
    class Scores { … }
    

Overriding also works when inheriting through `@ApiReference`:
    
    
    @Api(name = "tictactoe", version = "v2")
    class TicTacToe { … }
    
    // Checkers will behave as if annotated with name = "checkers" and version = "v2"
    @ApiReference(TicTacToe.class)
    @Api(name = "checkers")
    class Checkers { … }
    

### Inheriting `@ApiMethod` annotations

The `@ApiMethod` annotation can be inherited from overridden methods. For example:
    
    
    class TicTacToeBase {
      @ApiMethod(httpMethod = "POST")
      public Game setGame(Game game) { … }
    }
    @Api(name = "tictactoe", version = "v1")
    class TicTacToe extends TicTacToeBase {
      // setGame behaves as if annotated with the @ApiMethod from TicTacToeBase.setGame.
      // Thus the "httpMethod" property will be "POST".
      @Override
      public Game setGame(Game game) { … }
    }
    

Similarly to `@Api` and `@ApiClass` annotation inheritance, if multiple methods overriding each other have `@ApiMethod` annotations, individual properties can be overridden. For example:
    
    
    class TicTacToeBase {
      @ApiMethod(httpMethod = "POST", clientIds = { "c1" })
      public Game setGame(Game game) { … }
    }
    @Api(name = "tictactoe", version = "v1")
    class TicTacToe extends TicTacToeBase {
      // setGame behaves as if annotated with httpMethod = "GET" and clientIds = { "c1"}.
      @ApiMethod(httpMethod = "GET")
      @Override
      public Game setGame(Game game) { … }
    }
    

There is no `@ApiReference` annotation or equivalent for methods, so `@ApiMethod` is always inherited through Java inheritance, not through `@ApiReference`.

## Inheritance and precedence rules

To synopsize the preceding discussion, the follow table shows the inheritance rules and order of precedence.

Annotation/inheritance | Rule  
---|---  
`@Api` | Must be identical for all classes.  
`@ApiClass` | Specified for a class to override `@Api` properties.  
Java inheritance | Class inherits `@Api` and `@ApiClass` of base class.  
`@ApiReference` | Class inherits `@Api` and `@ApiClass` of referenced class.  
Using `@ApiReference` on a class (Java) inheriting from a base class | Class inherits the `@Api` and `@ApiClass` of referenced class, _not_ from the base class.  
  
## Common use cases for annotation inheritance

The following are examples of the typical use cases for inheritance:

For API versioning:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeV1 { … }
    @Api(version = "v2")
    class TicTacToeV2 extends TicTacToeV1 { … }
    

For multiclass APIs:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToeBase {}
    @ApiClass(resource = "boards")
    class TicTacToeBoards extends TicTacToeBase { … }
    @ApiClass(resource = "scores")
    class TicTacToeScores extends TicTacToeBase { … }
    

For testing different versions of the same API:
    
    
    @Api(name = "tictactoe", version = "v1")
    class TicTacToe {
      protected Foo someMethod() {
        // Do something real;
      }
    
      public Foo getFoo() { … }
    }
    
    
    @Api(version="v1test")
    class TicTacToeTest extends TicTacToe {
      protected Foo someMethod() {
        // Stub out real action;
      }
    }
    

where `someMethod` might return pre-determined responses, avoid calls with side-effects, skip a network or datastore request, and so forth.

## Adding the classes to `web.xml`

After annotating your classes, you must add them to your `web.xml` file. The following example shows a single class:
    
    
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
             http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
             version="3.1">
        <!-- Wrap the backend with Endpoints Frameworks v2. -->
        <servlet>
            <servlet-name>EndpointsServlet</servlet-name>
            <servlet-class>com.google.api.server.spi.EndpointsServlet</servlet-class>
            <init-param>
                <param-name>services</param-name>
                <param-value>com.example.skeleton.MyApi</param-value>
            </init-param>
        </servlet>
        <!-- Route API method requests to the backend. -->
        <servlet-mapping>
            <servlet-name>EndpointsServlet</servlet-name>
            <url-pattern>/_ah/api/*</url-pattern>
        </servlet-mapping>
    </web-app>

To add multiple classes:

  1. Replace `<param-value>com.example.skeleton.MyApi</param-value>` with your own API class name.

  2. Add each class inside this same `<param-value>` field separated by a comma, for example:
         
         <param-value>com.example-company.example-api.Hello,com.example-company.example-api.Goodbye</param-value>
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
