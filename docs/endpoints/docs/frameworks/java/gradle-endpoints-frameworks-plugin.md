---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/gradle-endpoints-frameworks-plugin/
title: Endpoints Framework Gradle Plugin \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:39.348752+00:00
---

# Endpoints Framework Gradle Plugin  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/gradle-endpoints-frameworks-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Endpoints Framework Gradle Plugin Stay organized with collections  Save and categorize content based on your preferences. 

The Endpoints Framework Gradle plugin provides tasks and configurations to build and connect Endpoints Framework for App Engine projects. This plugin provides server-side and client-side support. The _server-side_ plugin generates Discovery documents and OpenAPI specifications from an annotated Endpoints Framework Java project and client libraries. The _client-side_ plugin generates client libraries when a discovery document is available.

## Plugin dependency

Add the Endpoints Framework Gradle plugin dependency by using the following snippet in your `build.gradle`. The following snippet retrieves the dependency from Maven Central:
    
    
    classpath 'com.google.cloud.tools:endpoints-framework-gradle-plugin:1.0.2'

## Server-side plugin

Add the server-side Endpoints Framework Gradle plugin using the following snippet in your `build.gradle`:
    
    
    apply plugin: 'com.google.cloud.tools.endpoints-framework-server'

Set server-side configuration in your `build.gradle` by the `endpointsServer` closure:
    
    
    endpointsServer {
      // Endpoints Framework Plugin server-side configuration
      hostname = "${projectId}.appspot.com"
    }

## Server-side tasks and properties

The following tasks are exposed for the server-side only.

### `endpointsClientLibs`

This task generates endpoints client libraries based on service classes.

You can use the following properties:

Property | Description  
---|---  
`serviceClasses` |  List of service classes (endpoints classes), this can be inferred from the `web.xml`.   
`clientLibDir` |  Output directory for generated client libraries.   
`hostname` |  To set the root url for the generated client libraries. For example using `hostname = myapp.appspot.com` will result in a default root url of `https://myapp.appspot.com/_ah/api`.   
  
### `endpointsDiscoveryDocs`

This task generates discovery documents based on service classes.

You can use the following properties:

Property | Description  
---|---  
`serviceClasses` |  List of service classes (endpoints classes), this can be inferred from the `web.xml`.   
`hostname` |  To set the root url for the generated discovery document. For example using `hostname = myapp.appspot.com` will result in a default root url of `https://myapp.appspot.com/_ah/api`.   
  
### `endpointsOpenApiDocs`

This task generates OpenAPI documents based on service classes.

You can use the following properties:

Property | Description  
---|---  
`serviceClasses` |  List of service classes (endpoints classes), this can be inferred from the `web.xml`.   
`hostname` |  To set the root url for the generated OpenAPI document. For example using `hostname = myapp.appspot.com` will result in the `host` url of `https://myapp.appspot.com` and `basePath` as `/_ah/api`.   
  
## Client-side plugin

To add the client-side Endpoints Framework Gradle plugin using the following in your `build.gradle`:
    
    
    apply plugin: 'com.google.cloud.tools.endpoints-framework-client'
    

Set server-side configuration in your `build.gradle` by the `endpointsClient` closure:
    
    
    endpointsClient {
      // client-side properties
    }
    

## Client-side properties

The client-side plugin doesn't expose tasks like the server-side plugin. Applying the client-side plugin will generate sources according to the following configuration properties.

Property | Description  
---|---  
`discoveryDocs` | A list of discovery docs to use when generating sources.  
  
## What's next

  * Explore the plugin code and report issues on [GitHub](https://github.com/GoogleCloudPlatform/endpoints-framework-gradle-plugin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
