---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management/
title: Adding API management \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:21.194899+00:00
---

# Adding API management  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Adding API management Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints Frameworks provides API management features that are comparable to the features that the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#extensible_service_proxy) provides for Cloud Endpoints. Endpoints Frameworks includes a built-in [API gateway](https://en.wikipedia.org/wiki/API_management) that intercepts all requests and performs any necessary checks, such as authentication, before forwarding the request to the API backend. When the backend responds, Endpoints Frameworks gathers and reports telemetry. You can view metrics for your API on the **Endpoints** > **Services** page in the Google Cloud console.

The API management features available in Endpoints Frameworks include:

  * [Monitoring](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api)
  * [Logging](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api#logs)
  * [Quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview)
  * [Developer portal](https://docs.cloud.google.com/endpoints/docs/openapi/dev-portal-overview)



For your API to be managed by Endpoints, you must deploy an OpenAPI document that describes your API using version 2.0 of the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md). This page describes how to generate and deploy an OpenAPI document that enables Endpoints to manage your API.

If you don't add API management, your API still serves requests, but your API doesn't appear on the **Endpoints** > **Services** page in the Google Cloud console, and the functionality provided by Endpoints, such as logging, monitoring, and setting quotas, isn't available.

## Installing and configuring required software

If you haven't already done so, install and configure the Google Cloud CLI for Python, and add the Endpoints Frameworks Python library to your API project directory so it is uploaded with the API code upon deployment

### Install and configure the gcloud CLI for Python

  1. Install and initialize gcloud CLI:

[Download and install gcloud CLI](https://docs.cloud.google.com/sdk/docs)

  2. Install the `gcloud` component that includes the App Engine extension for Python:
         
         gcloud components install app-engine-python
         

  3. Update the gcloud CLI:
         
         gcloud components update
         

  4. Make sure that the gcloud CLI is authorized to access your data and services on Google Cloud:
         
         gcloud auth login
         

A new browser tab opens and you are prompted to choose an account.

  5. Set the default project to your project ID. Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.
         
         gcloud config set project YOUR_PROJECT_ID
         

  6. For Linux, set the `ENDPOINTS_GAE_SDK` environment variable to the path of your App Engine SDK folder:
         
         PATH_TO_CLOUD_SDK/platform/google_appengine
         

Replace `PATH_TO_CLOUD_SDK` with the output of the following command:
         
         gcloud info --format="value(installation.sdk_root)"
         




### Add the Endpoints Frameworks Python library

  1. Be sure you can compile C extensions for Python.

     * Windows: Microsoft Visual C++ 9.0 or greater is required. You can download the Microsoft Visual C++ Compiler for Python 2.7 from the [Microsoft download center](http://aka.ms/vcpython27)

     * Other operating systems: Depending on your operating system, you may need to install compiler tools (sometimes in a package called `build-essential`) and/or the Python development headers (sometimes in a package called `python-dev`).

  2. Change directory to your API's main directory.

  3. Make a `/lib` subdirectory in the API’s main directory:
         
         mkdir lib
         

  4. Install the library:
         
         pip install -t lib google-endpoints --ignore-installed
         




## Generate the OpenAPI document

From the API's main directory, generate an OpenAPI document by using the framework tools. For example:

### Single Class

In the following command, replace `YOUR_PROJECT_ID` with your Google Cloud project ID.
    
    
    python lib/endpoints/endpointscfg.py get_openapi_spec main.EchoApi \
        --hostname YOUR_PROJECT_ID.appspot.com
    

Ignore the warnings that are displayed.

### Multiple Classes

You can list multiple classes on the command line. Endpoints generates an OpenAPI document for each API name/version combination.

If you want to deploy multiple API classes with different API names as part of a single service, you must also add the `--x-google-api-name` flag. Enabling this flag adds extra restrictions on your API names. Specifically, the names must match the regular expression `[a-z][a-z0-9]{0,39}`; that is, the name must consist of 1-40 characters, which can all be either lowercase alphabetical characters or numbers, except that the first character must not be a number. For example:

In the following command, replace `YOUR_PROJECT_ID` with your Google Cloud project ID.
    
    
    python lib/endpoints/endpointscfg.py get_openapi_spec main.FooApi main.BarApi \
       --hostname YOUR_PROJECT_ID.appspot.com \
       --x-google-api-name
    

Ignore the warnings that are displayed.

Endpoints uses the text that you specify in the `hostname` argument as the service name. When you deploy the API to App Engine, a DNS entry with a name in the format `YOUR_PROJECT_ID.appspot.com` is created automatically.

## Deploy the OpenAPI document

### Single Class
    
    
    gcloud endpoints services deploy echov1openapi.json
    

### Multiple Classes

If you have multiple OpenAPI documents, list them all on the command line. For example:
    
    
     gcloud endpoints services deploy foov1openapi.json barv1openapi.json
    

This first time you deploy your OpenAPI document (or documents), a new Endpoints service is created with the name `YOUR_PROJECT_ID.appspot.com`.

On successful completion, a line similar to the following displays the service configuration ID and the service name:
    
    
    Service Configuration 2017-02-13r0 uploaded for service example-project-12345.appspot.com
    

In the example above, `2017-02-13r0` is the service configuration ID. The service configuration ID consists of a date stamp followed by a revision number. If you deploy your OpenAPI document again, the revision number is incremented in the service configuration ID.

If you need to display the service configuration ID again, run the following command, but replace `YOUR_PROJECT_ID` with the project ID of your Google Cloud project:
    
    
    gcloud endpoints configs list --service=YOUR_PROJECT_ID.appspot.com
    

You can create your own OpenAPI document and deploy it, rather than using a generated one. Simply replace `echov1openapi.json` above with the path to your OpenAPI document. For more information on writing an OpenAPI document, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).

## Redeploy your API and test

  1. Edit your project's file `app.yaml` and add an `env_variables` section as follows:
         
         env_variables:
           ENDPOINTS_SERVICE_NAME: YOUR_PROJECT_ID.appspot.com
           ENDPOINTS_SERVICE_VERSION: YOUR_SERVICE_VERSION
         

Replace `YOUR_PROJECT_ID` with your Google Cloud project ID, and `YOUR_SERVICE_VERSION` with your service configuration ID from the previous section. With this addition to the `app.yaml` file, Endpoints manages your API after you redeploy your application.

  2. Redeploy your application:
         
         gcloud app deploy
         

  3. Wait a few moments for the deployment to succeed, ignoring the warning messages. When the deployment completes, a message similar to the following is displayed:
         
         File upload done.
         Updating service [default]...done.
         

  4. Test for a successful redeployment, for example, using curl:
         
         curl --request POST \
             --header "Content-Type: application/json" \
             --data '{"content":"echo"}' \
             https://YOUR_PROJECT_ID.appspot.com/_ah/api/echo/v1/echo?n=2
         

Replace `echo` with the name of your API.

The results should display something similar to:
         
         {
          "content": "echo echo"
         }
         

  5. Make some additional requests to your API.

  6. To [view your API metrics](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api), open the **Endpoints** > **Services** page in the Google Cloud console for your project:  


[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
