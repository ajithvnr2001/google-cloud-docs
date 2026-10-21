---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/using-guice/
title: Using Guice with Cloud Endpoints Frameworks \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:33:30.271535+00:00
---

# Using Guice with Cloud Endpoints Frameworks  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/using-guice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Using Guice with Cloud Endpoints Frameworks Stay organized with collections  Save and categorize content based on your preferences. 

[Google Guice](https://github.com/google/guice) is a dependency injection framework that you can use with an Endpoints Frameworks v2 project to configure servlet mapping and filtering programmatically in Java, rather than in [`web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java/config/webxml).

To use Guice, you need to add the following prepackaged dependency to your `pom.xml` or `build.gradle`. Also, you need to configure the Endpoints Frameworks plugins for Maven and Gradle to define which service classes the plugins use to create OpenAPI documents.

**Note:** The service classes are not auto-detected by the plugins if not defined in `web.xml`.

### Maven
    
    
    <dependency>
      <groupId>com.google.endpoints</groupId>
      <artifactId>endpoints-framework-guice</artifactId>
      <version>2.2.2</version>
    </dependency>

### Gradle
    
    
    compile 'com.google.endpoints:endpoints-framework-guice:2.2.2'
    
    
    endpointsServer {
      // Endpoints Framework Plugin server-side configuration
      hostname = "${projectId}.appspot.com"
      serviceClasses = ['com.example.echo.Echo']
    }

Next, you need to update `web.xml` to direct all traffic from `/_ah/api/*` to the Endpoints Frameworks Guice Servlet.
    
    
    <filter>
        <filter-name>guiceFilter</filter-name>
        <filter-class>com.google.inject.servlet.GuiceFilter</filter-class>
    </filter>
    
    <!--
      URL Pattern /_ah/api/* instead of /* because a legacy v1 servlet uses
      the route /_ah/api/ and using /* will erronously use the legacy v1
      servlet instead of routing to your API.
    -->
    <filter-mapping>
        <filter-name>guiceFilter</filter-name>
        <url-pattern>/_ah/api/*</url-pattern>
    </filter-mapping>
    
    <listener>
        <listener-class>com.example.echo.EchoGuiceListener</listener-class>
    </listener>

Implement the listener class in your project. It should look similar to the following depending on the number of services:
    
    
    public class EchoGuiceListener extends GuiceServletContextListener {
    
      @Override
      protected Injector getInjector() {
        return Guice.createInjector(new EchoEndpointModule());
      }
    }

The listener class creates a new injector that handles servlet mapping and filtering, which is normally defined by the `web.xml`, but instead is now defined by the EchoEndpointModule class defined as:
    
    
    public class EchoEndpointModule extends EndpointsModule {
      @Override
      public void configureServlets() {
        super.configureServlets();
    
        bind(ServiceManagementConfigFilter.class).in(Singleton.class);
        filter("/_ah/api/*").through(ServiceManagementConfigFilter.class);
    
        Map<String, String> apiController = new HashMap<>();
        apiController.put("endpoints.projectId", "YOUR-PROJECT-ID");
        apiController.put("endpoints.serviceName", "YOUR-PROJECT-ID.appspot.com");
    
        bind(GoogleAppEngineControlFilter.class).in(Singleton.class);
        filter("/_ah/api/*").through(GoogleAppEngineControlFilter.class, apiController);
    
        bind(Echo.class).toInstance(new Echo());
        configureEndpoints("/_ah/api/*", ImmutableList.of(Echo.class));
      }
    }

## What's next?

  * [Write and annotate your backend API code](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code)
  * [Learn more about annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations)
  * [Add API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management)
  * [Deploy and test your API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy)
  * [Learn more about supported parameter and return types](https://docs.cloud.google.com/endpoints/docs/frameworks/java/parameter-and-return-types)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
