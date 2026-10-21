---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/endpoints_tool/
title: Cloud Endpoints Frameworks for App Engine command-line tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:22.876404+00:00
---

# Cloud Endpoints Frameworks for App Engine command-line tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/endpoints_tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Cloud Endpoints Frameworks for App Engine command-line tool Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate a client library from your backend server API by using the Endpoints Frameworks command-line tool. Any Java or Android app can use this library to call the API. 

You can generate client library bundles that allow applications to access your API using the Endpoints Frameworks command-line tool. When you generate a client library, the Endpoints Frameworks command-line tool automatically generates a [Discovery document](https://developers.google.com/discovery/v1/reference/apis) that describes the surface of your API.

To get the Endpoints Frameworks command-line tool, download [`endpoints-framework-tools`](http://search.maven.org/remotecontent?filepath=com/google/endpoints/endpoints-framework-tools/2.2.1/endpoints-framework-tools-2.2.1.zip) from the [Maven Central Repository](http://search.maven.org/). After you extract the contents of the zip file, the tool is in the `endpoints-framework-tools-2.2.1/bin/` directory.

## Generating a client library bundle from an API

You can use the Endpoints Frameworks command-line tool to generate the following types of client bundles:

  * Maven: This bundle includes a `pom.xml` file with the Endpoints Frameworks and Google API Client Library dependencies. The `readme.html` file provides detailed information on what you need to add to your `pom.xml` file for different types of client applications and how to build a client library for your API using Maven.

  * Gradle: This bundle includes a `build.gradle` file with the Endpoints Frameworks and Google API Client Library dependencies. The `readme.html` file provides detailed information on what you need to add to your `build.gradle` file for different types of client applications and how to build a client library for your API using Gradle.

  * Default client bundle: This bundle contains all the dependency libraries and the generated `source.jar` file, which is the Java library that you use in your client to call your API. This bundle provides your client with all of the Google API Client Library capabilities, including OAuth. The `readme.html` file lists the `.jar` files that are required for different types of client applications and other details for using the client library.




If you are using the client library with an Android app, we recommend that you use a Gradle client bundle.

### Command-line syntax

Before you use the Endpoints Frameworks command-line tool, you must build your backend project because this tool requires compiled binaries. You can optionally supply the `--war=` option pointing to the build target output directory containing the `WEB-INF` directory and compiled java classes if you don't want to use the default (`--war="./war"`).

The basic syntax is as follows:
    
    
    /path-to/endpoints-framework-tools-2.2.1/bin/endpoints-framework-tools \
        get-client-lib OPTIONS CLASS_NAME
    

where:

  * `OPTIONS`, if supplied, is one or more items shown in the Options table.
  * `CLASS_NAME` is the fully qualified class name of your API.



For example:
    
    
    /path-to/endpoints-framework-tools-2.2.1/bin/endpoints-framework-tools \
        get-client-lib --war=target/echo-1.0-SNAPSHOT -bs gradle com.example.echo.Echo
    

where `target/echo-1.0-SNAPSHOT` is the relative or absolute path to the target build directory containing `WEB-INF` and the compiled backend classes.

**Note:** If your API is implemented from multiple classes, specify each of them separated by a space.

### Options

You can use the following options: 

Option name | Description | Example  
---|---|---  
`build-system` | Lets you specify which type of client bundle should be produced. Specify `gradle` for a Gradle client bundle for Android, `maven` for a Maven client bundle, or `default` (or simply omit this option) for a bundle that contains only the dependency libraries and source jar. | `--build-system=gradle` `-bs gradle`  
`war` | Sets the path to the build target directory `WEB-INF` that contains `appengine-web.xml` and other metadata.Default: `./war`. | `--war=target/echo-1.0-SNAPSHOT``-w target/echo-1.0-SNAPSHOT`  
`output` | Sets the directory where the output is written to.Default: the directory the tool is invoked from. | `--output=/mydir``-o /mydir`  
  
### Supported client platforms

The following platforms are supported in the client bundle produced by the Endpoints Frameworks command-line tool:

  * Java 7 and higher:
  * [Android](https://github.com/googleapis/google-api-java-client/wiki/Android) 1.6 and higher.
  * [App Engine](https://github.com/googleapis/google-api-java-client/wiki).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
