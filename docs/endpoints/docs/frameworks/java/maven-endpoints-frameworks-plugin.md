---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/maven-endpoints-frameworks-plugin/
title: Endpoints Framework Maven plugin \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:14.132661+00:00
---

# Endpoints Framework Maven plugin  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/maven-endpoints-frameworks-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Endpoints Framework Maven plugin Stay organized with collections  Save and categorize content based on your preferences. 

The Endpoints Framework Maven plugin provides tasks and configurations to build Endpoints Framework projects. This plugin provides server-side and client-side support. The _server-side_ goals generate Discovery documents and OpenAPI specifications from an annotated Endpoints Framework Java project and client libraries. The _client-side_ goal generates client libraries when a discovery document is available.

## Add the Endpoints Framework Maven plugin

Add the Endpoints Framework Maven plugin by using the following plugin snippet to your `pom.xml`:
    
    
    <plugin>
      <groupId>com.google.cloud.tools</groupId>
      <artifactId>endpoints-framework-maven-plugin</artifactId>
      <version>1.0.2</version>
      <configuration>
        <!-- plugin configuration -->
        <hostname>${endpoints.project.id}.appspot.com</hostname>
      </configuration>
    </plugin>

## Plugin goals

After you add the Endpoints Framework Maven plugin, the following Endpoints Framework-specific Maven goals are available:

### Server-side

Goal | Description  
---|---  
`endpoints-framework:clientLibs` | Generates client libraries  
`endpoints-framework:discoveryDocs` | Generates discovery documents  
`endpoints-framework:openApiDocs` | Generates OpenAPI documents  
  
### Client-side

Goal | Description  
---|---  
`endpoints-framework:generateSrc` | Generates client libraries from discovery documents.  
  
## Goal parameters

Each goal has associated parameters that you can use. You can specify these settings in the `pom.xml` or in the command line.

To configure these settings in the `pom.xml`, add the parameter name in the `<configuration>` section.

Alternatively, to configure these settings in the command line, follow the pattern `-D[USER_PROPERTY]=[PARAMETER_VALUE]`.

See the following sections for a list of the parameters that are available for each goal.

### `endpoints-framework:clientLibs`

This goal generates client libraries from the server-side.

Parameter | Description | User Property  
---|---|---  
`clientLibDir` |  Define the location of generated client libraries. The default location is defined as `target/client-libs`.  | `endpoints.clientLibDir`  
`serviceClasses` |  Optional parameter to provide a List of names of service classes (endpoints classes). This can be inferred from the `web.xml`.  | `endpoints.serviceClasses`  
`webappDir` |  Provide the location of the `webapp` directory. The default location is defined as `src/main/webapp`.  | `endpoints.webappDir`  
`hostname` |  To set the root url for client libs. For example using `hostname = myapp.appspot.com` will result in a default root url of`https://myapp.appspot.com/_ah/api`  | `endpoints.hostname`  
  
### `endpoints-framework:discoveryDocs`

This goal generates discovery documents.

Parameter | Description | User Property  
---|---|---  
`discoveryDocDir` |  Define a location for generated discovery documents. The default location is defined as `target/discovery-docs`.  | `endpoints.discoveryDocDir`  
`serviceClasses` |  Optional parameter to provide a List of names of service classes (endpoints classes). This can be inferred from the `web.xml`.  | `endpoints.serviceClasses`  
`webappDir` |  Provide the location of the `webapp` directory. The default location is defined as `src/main/webapp`.  | `endpoints.webappDir`  
`hostname` |  To set the root url for discovery docs. For example using `hostname = myapp.appspot.com` will result in a default root url of`https://myapp.appspot.com/_ah/api`  | `endpoints.hostname`  
  
### `endpoints-framework:openApiDocs`

This goal generates OpenAPI documents.

Parameter | Description | User Property  
---|---|---  
`openApiDocDir` |  Define a location for generated OpenAPI documents. The default location is defined as `target/openapi-docs`.  | `endpoints.openApiDocDir`  
`serviceClasses` |  Optional parameter to provide a List of names of service classes (endpoints classes). This can be inferred from the `web.xml`.  | `endpoints.serviceClasses`  
`webappDir` |  Provide the location of the `webapp` directory. The default location is defined as `src/main/webapp`.  | `endpoints.webappDir`  
`hostname` |  To set the root url for OpenAPI documents. For example using `hostname = myapp.appspot.com` will result in a default root url of`https://myapp.appspot.com/_ah/api`  | `endpoints.hostname`  
  
### `endpoints-framework:generateSrc`

This goal generates client sources from discovery documents.

Parameter | Description | User Property  
---|---|---  
`discoveryDocs` |  Define a list of discovery documents.  | `endpoints.discoveryDocs`  
`generatedSrcDir` |  Output directory for generated client library sources. Default location is at `target/generated-sources/`.  | `endpoints.generatedSrcDir`  
  
## What's next

  * Explore the plugin code and report issues on [GitHub](https://github.com/GoogleCloudPlatform/endpoints-framework-maven-plugin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
