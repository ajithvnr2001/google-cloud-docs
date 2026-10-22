---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/required_files/
title: Required Files and Configuration \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:38.230768+00:00
---

# Required Files and Configuration  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/required_files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Required Files and Configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the files that must be included in API in order to use Cloud Endpoints Frameworks for App Engine. 

Your project must contain, at a minimum, the following files: 

File and Location | Description  
---|---  
`/src/main/java/<packagepath>/<your_api_class>.java` | The class file (or files, if you implement your API across multiple classes) containing your backend API.  
`/src/main/webapp/WEB-INF/appengine-web.xml` | The web app deployment descriptor required for App Engine configuration.  
`/src/main/webapp/WEB-INF/web.xml` | The standard Java web app deployment descriptor mapping URLs to servlets and other information.  
  
The contents of each of these required files is documented in the following sections.

## The API class file

The required and optional contents of the class file (or files, if you use a [multi-class API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/multiclass)) are fully described in the topic [Endpoint Annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations).

## appengine-web.xml

The `appengine-web.xml` file is used to define the App Engine standard environment configuration when the API is deployed. See [appengine-web.xml Reference](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref) for more information.

The bare minimum contents required for this file are as follows:
    
    
    <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
        <runtime>java8</runtime>
        <threadsafe>true</threadsafe>
    
        <system-properties>
            <property name="java.util.logging.config.file" value="WEB-INF/logging.properties"/>
        </system-properties>
    </appengine-web-app>

## web.xml

You use the `web.xml` file to configure the Endpoints servlet, which handles incoming requests and forwards them to the backend service running on App Engine. The Endpoints servlet is required for your API to be [managed by Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).

The bare minimum contents required for this file are as follows:
    
    
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

**Important:** The URL pattern specified in the `web.xml` file defines the URL base path for the API. Make sure the pattern ends with a wildcard, as in `/_ah/api/*`.

For more information about `web.xml`, see [The Deployment Descriptor: web.xml](https://docs.cloud.google.com/appengine/docs/standard/java/config/webxml).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
