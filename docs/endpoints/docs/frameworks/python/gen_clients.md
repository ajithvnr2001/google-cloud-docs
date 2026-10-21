---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/gen_clients/
title: Generating a client library \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:34:49.336610+00:00
---

# Generating a client library  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/gen_clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Generating a client library Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate a client library from your Python backend API (the code that runs on the server). Any Java or Android app can use this library to call the API.

To create iOS clients for your API, we recommend that you use [Google APIs Objective-C Client Library for REST APIs](https://github.com/google/google-api-objectivec-client-for-rest/wiki).

## Before you begin

  * Download the Cloud Endpoints Frameworks library and tools into your app directory as described in [Getting started with Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/python/quickstart-frameworks-python).
  * Make sure you have properly [decorated](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api) your API code with the expected frameworks code.



## Generating the client library

The following instructions demonstrate how to use the Endpoints Frameworks [command-line tool](https://docs.cloud.google.com/endpoints/docs/frameworks/python/endpoints_tool) to generate a Gradle client bundle from the sample code from [Getting started with Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/frameworks/python/quickstart-frameworks-python).

To generate a client library:

  1. Change directory to the directory containing your API `app.yaml` file and API classes.

  2. Run the Endpoints command-line tool similar to the following:
         
         python lib/endpoints/endpointscfg.py get_client_lib java -bs gradle main.EchoApi
         

where `main` is the class containing your API and `EchoApi` is your API name.

Wait for the tool to generate the library; on success the tool displays a message similar to this one:
         
         API client library written to ./echo-v1.zip
         

  3. Unzip the file using the unzip utility, or use another ZIP-compatible unarchiving utility:
         
         unzip ./echo-v1-java.zip
         

  4. Change directory:
         
         cd echo
         

  5. Build the client library:
         
         gradle build
         

The output is in the `build/libs` directory. The exact filename depends on the version of the client. It is similar to `echo-v1-1.23.0-SNAPSHOT.jar`.

  6. Add the client library JAR to your app.

  7. Repeat these steps every time you modify your API code.




## What's next

For information and sample code showing how to access a backend API from a Python client, see [Accessing backend APIs from Python clients](https://docs.cloud.google.com/endpoints/docs/frameworks/python/access_from_python). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
