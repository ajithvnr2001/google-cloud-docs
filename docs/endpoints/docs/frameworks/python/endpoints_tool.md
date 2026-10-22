---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/endpoints_tool/
title: Cloud Endpoints Frameworks for App Engine command-line tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:26.019072+00:00
---

# Cloud Endpoints Frameworks for App Engine command-line tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/endpoints_tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Cloud Endpoints Frameworks for App Engine command-line tool Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Endpoints Frameworks command-line tool to generate a client library from your Python backend API (the code that runs on the server). Any Java or Android app can use this library to call the API. 

You can generate client library bundles that allow applications to access your API using the Endpoints Frameworks command-line tool. When you generate a client library, the Endpoints Frameworks command-line tool automatically generates a [Discovery document](https://developers.google.com/discovery/v1/reference/apis) that describes the surface of your API.

The Endpoints Frameworks command-line tool,`endpointscfg.py` is available in the Endpoints Frameworks library. For information on installing the Endpoints Frameworks library using `pip`, see [Installing the Endpoints Frameworks library](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python#installing_the_endpoints_frameworks_library). Note that the following commands assume you have installed the Endpoints Frameworks library in a directory called `lib`. Additionally, the instructions assume you have created your backend API. See the [Endpoints Frameworks for Python tutorial](https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python) for an example of using the Endpoints Frameworks command-line tool on sample code. 

## Generating a client library bundle from an API

You can use the Endpoints Frameworks command-line tool to generate the following types of client bundles:

  * Maven: This bundle includes a `pom.xml` file with the Endpoints Frameworks and Google API Client Library dependencies. The `readme.html` file provides detailed information on what you need to add to your `pom.xml` file for different types of client applications and how to build a client library for your API using Maven.

  * Gradle: This bundle includes a `build.gradle` file with the Endpoints Frameworks and Google API Client Library dependencies. The `readme.html` file provides detailed information on what you need to add to your `build.gradle` file for different types of client applications and how to build a client library for your API using Gradle.

  * Default client bundle: This bundle contains all the dependency libraries and the generated `source.jar` file, which is the Java library that you use in your client to call your API. This bundle provides your client with all of the Google API Client Library capabilities, including OAuth. The `readme.html` file lists the `.jar` files that are required for different types of client applications and other details for using the client library.




If you are using the client library with an Android app, we recommend that you use a Gradle client bundle.

### Generating the client library

To generate the client library:

  1. Change directory to the directory containing your API's `app.yaml` file and API service classes. Alternatively, use the `--application` option to specify some other location of your application directory.

  2. Invoke the Endpoints Frameworks command-line tool similar to the following:
         
         lib/endpoints/endpointscfg.py get_client_lib java -bs gradle main.EchoApi
         

where `main` is the class containing your API and `EchoApi` is your API name.

  3. Wait for the tool to generate the client library; on success the tool displays a message similar to this one:
         
         API client library written to ./echo-v1.zip
         

  4. Add the client library JAR to your Android app.

  5. Repeat the preceding steps every time you modify your API code.




The client library bundle is written to the current directory unless you specify some other output directory using the `output` option.

### Command-line syntax

The basic syntax is as follows:
    
    
    /path-to/your-app/lib/endpointscfg.py get_client_lib TARGET_LANG OPTIONS CLASS_NAME
    

where:

  * `TARGET_LANG` specifies the type of client bundle you want to create. Currently, you are required to supply the value `java` (for Java clients such as Android).
  * `OPTIONS`, if supplied, is one or more items shown in the Options table
  * `CLASS_NAME` is the fully qualified class name of your API.

**Note:** If your API is implemented from multiple classes, specify each of them separated by a space.

### Options

You can use the following options: 

Option name | Description | Example  
---|---|---  
`application` | By default, the tool generates from the backend API in the current directory.If you want to generate using a different directory, specify the path to the directory containing the `app.yaml` and service classes that implement your API. | `--application /my_path/my_api_dir`  
`build-system` | Lets you specify which type of client bundle should be produced. Specify `gradle` for a Gradle client bundle for Android, `maven` for a Maven client bundle, or `default` (or simply omit this option) for a bundle that contains only the dependency libraries and source jar. | `--build-system=gradle` `-bs gradle`  
`hostname` | Specifies the discovery document `rootURL`.This option overrides the default value derived from the `application` entry inside the backend API project `app.yaml` (`[YOUR_APP_ID].appspot.com`) and the `hostname` defined in the [decorator for your API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi).One use of this option is to supply the hostname `localhost` as the rootURL for local testing. | `--hostname localhost`  
`format` | Don't specify this because the only supported value is the default value, `rest` for REST. | Not needed, use default.  
`output` | Sets the directory where the output is written to.Default: the directory the tool is invoked from. | `--output /mydir``-o /mydir`  
  
### Supported client platforms

The following platforms are supported in the client bundle produced by the Endpoints Frameworks command-line tool:

  * Java 7 and higher:
  * [Android](https://github.com/googleapis/google-api-java-client/wiki/Android) 1.6 and higher.
  * [App Engine](https://github.com/googleapis/google-api-java-client/wiki).



## Generating an OpenAPI document from an API

The `endpointscfg.py` tool provides a command to generate an OpenAPI document from an API backend. The command syntax is:
    
    
    lib/endpoints/endpointscfg.py get_openapi_spec
        [-h]
        [-a APPLICATION]
        [--hostname HOSTNAME]
        [-o OUTPUT]
        service [service ...]
    
    positional arguments:
      service               Fully qualified service class name.
    
    optional arguments:
      -h, --help            Show this help message and exit.
      -a APPLICATION, --application APPLICATION
                            The path to the Python App Engine application.
      --hostname HOSTNAME   Default application hostname, if none is specified for the API service.
      -o OUTPUT, --output OUTPUT
                            The directory to store output files.
      --x-google-api-name   Add the 'x-google-api-name' field to the generated OpenAPI document.
    

For example, using [the `echo` example](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/endpoints-frameworks-v2/echo):
    
    
    $ lib/endpoints/endpointscfg.py get_openapi_spec --hostname=echo-example.appspot.com main.EchoApi
    OpenAPI spec written to ./echov1openapi.json
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
