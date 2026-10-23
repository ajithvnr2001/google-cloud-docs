---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python/
title: Getting started with Cloud Endpoints Frameworks for Python \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:47.531574+00:00
---

# Getting started with Cloud Endpoints Frameworks for Python  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/get-started-frameworks-python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Getting started with Cloud Endpoints Frameworks for Python Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure, deploy, and send requests to a sample API by using [Cloud Endpoints Frameworks for Python](https://docs.cloud.google.com/endpoints/docs/frameworks/python/about-cloud-endpoints-frameworks). Endpoints Frameworks for Python is integrated with the [App Engine standard Python 2.7 runtime environment](https://docs.cloud.google.com/appengine/docs/standard/python/runtime). Endpoints Frameworks consists of tools, libraries, and capabilities that let you generate APIs and client libraries from an App Engine application.

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API.

  1. Set up a Google Cloud project. See Before you begin.
  2. Install required software and create an App Engine application. See Installing and configuring required software.
  3. Download the sample code. See Getting the sample code.
  4. Generate an OpenAPI document. See Configuring Endpoints.
  5. Deploy the Endpoints configuration to create an Endpoints service. See Deploying the Endpoints configuration.
  6. Run the sample on your computer. See Running the sample locally.
  7. Create a backend to serve the API and deploy the API. See Deploying the API backend.
  8. Send a request to the API. See Sending a request to the API.
  9. Track API activity. See Tracking API activity.
  10. Avoid incurring charges to your Google Cloud account. See Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Endpoints](https://docs.cloud.google.com/endpoints/pricing)
  * [App Engine](https://docs.cloud.google.com/appengine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

**Note:** Make sure you have Python 2.7.x installed. Python 3.x isn't supported by Endpoints Frameworks.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make a note of the Google Cloud project ID because it is needed later. 



## Installing and configuring required software

  1. Follow the instructions in [Installing Google Cloud CLI for Python](https://docs.cloud.google.com/appengine/docs/standard/python/download) to get your App Engine standard development environment set up. Make sure you install the `app-engine-python` and `app-engine-python-extras` `gcloud` components. 
  2. Run the following commands: 
     1. Update the gcloud CLI. 
            
            gcloud components update

     2. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud: 
            
            gcloud auth login

     3. In the new browser tab that opens, choose an account. 
     4. Set the default project to your project ID. 
            
            gcloud config set project [YOUR_PROJECT_ID]

Replace `[YOUR_PROJECT_ID]` with your Google Cloud project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

  3. You need an application to send requests to the sample API.

     * Linux and macOS users: This tutorial provides an example of using `curl`, which typically comes pre-installed on your operating system. If you don't have `curl`, you can download it from the `curl` [ Releases and downloads page](https://curl.haxx.se/download.html). 
     * Windows users: This tutorial provides an example using [`Invoke-WebRequest`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest), which is supported in PowerShell 3.0 and later. 
  4. Make sure your Python development environment includes [ pip](https://pip.pypa.io/en/stable/). 
  5. Be sure you can compile C extensions for Python. 
     * Windows: Microsoft Visual C++ 9.0 or greater is required. You can download the Microsoft Visual C++ Compiler for Python 2.7 from the [Microsoft Download Center](http://aka.ms/vcpython27) . 
     * Other operating systems: Depending on your operating system, you may need to install compiler tools (sometimes in a package called `build-essential`) or the Python development headers (sometimes in a package called `python-dev`). 
  6. For Linux, set the `ENDPOINTS_GAE_SDK` environment variable to the path of your App Engine SDK folder: `[Path-to-Google-Cloud-SDK]/platform/google_appengine`. 

Replace `[Path-to-Google-Cloud-SDK]` with the output of the following command: 
         
         gcloud info --format="value(installation.sdk_root)"

  7. Create an App Engine application: 
     1. Select the region where you want to create your App Engine application. Run the following command to get a list of regions: 
            
            gcloud app regions list

     2. Create an App Engine application using the following command. Replace `[YOUR_PROJECT_ID]` with your Google Cloud project ID and `[YOUR_REGION]` with the region that you want the App Engine application created in. 
            
            gcloud app create \
            --project=[YOUR_PROJECT_ID] \
            --region=[YOUR_REGION]

For example:
            
            gcloud app create --project=example-project-12345 --region=us-central




## Getting the sample code

To clone the sample API from GitHub:

  1. Clone the sample repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples
         

  2. Change to the directory containing the sample code:
         
         cd python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo
         




## Configuring Endpoints

To configure Endpoints, you first have to install the Endpoints Frameworks Python library. You then use a tool from the Endpoints Frameworks library to generate an [OpenAPI document](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#open_api_doc) for the sample API. You need the Endpoints Frameworks library and the OpenAPI document so that Endpoints can manage the API. For more information see [Adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/python/adding-api-management).

### Installing the Endpoints Frameworks library

This section walks you through using Python's `pip` to add the Endpoints Frameworks library to the sample API's project directory.

**Note:** Don't run Python in a virtual environment. The Endpoints Frameworks packages must be installed in the `lib` subdirectory under the project directory on your computer.

To add the Endpoints Frameworks library to the sample:

  1. Make sure you are in the sample API's main directory, `python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo`.

  2. Make a `/lib` subdirectory in the project:
         
         mkdir lib
         

  3. From the sample main directory `python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo`, run the install command:
         
         pip install --target lib --requirement requirements.txt --ignore-installed
         

Note the following:

     * This `pip` command may use GNU Compiler Collection (GCC) to compile extension modules. If you are on macOS and this is the first time you have run GCC on your system, you may have to accept Apple's XCode license. To do so, run `sudo xcodebuild -license`.

     * If you have multiple Python versions installed on your computer, make sure you are using a version of `pip` corresponding to the Python version you are using in this tutorial. Version mismatches (`pip` from Python 3.4 while using `python` from Python 2.7, for example) can cause errors which can be difficult to understand. If need be, you can run pip as a Python module: replace the `pip` in the preceding command with `python -m pip`.

     * If `pip` is unable to find a suitable package when running the command, try upgrading it by running `pip install --upgrade pip`. After the upgrade is complete, try the installation command again.

     * On some Debian and Ubuntu releases `pip` might fail with DistutilsOptionError. If you see this error, add --system flag.




On successful completion, the `lib` directory is populated with the files required to build the Endpoints Frameworks application.

### Generating the OpenAPI document

You use a tool from the Endpoints Frameworks library to generate a document that describes the sample code's REST API.

To generate the OpenAPI document:

  1. Make sure you are in the sample main directory:
         
         python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo
         

  2. Generate the OpenAPI document:
         
         python lib/endpoints/endpointscfg.py get_openapi_spec main.EchoApi --hostname [YOUR_PROJECT_ID].appspot.com
         

Replace `[YOUR_PROJECT_ID]` with your Google Cloud project ID. Ignore the warnings that are displayed. The Endpoints tool generates an OpenAPI document called `echov1openapi.json` in the current directory. The Endpoints tool names the file based on the name and version of the service specified in the `@endpoints.api` decorator. See [Creating the API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api) for more information.

Endpoints uses the text specified in the `hostname` argument as the service name. The `YOUR_PROJECT_ID.appspot.com` name format matches the DNS entry that is created automatically when you deploy the API to the App Engine backend. So in this case, both the Endpoints service name and fully qualified domain name (FQDN) are the same.




On successful completion, the following message is displayed: `OpenAPI spec written to ./echov1openapi.json`

## Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview), Google's foundational services platform, used by Endpoints and other services to create and manage APIs and services.

To deploy the configuration file:

  1. Make sure you are in the sample main directory: 
         
         python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo
         

  2. Deploy the OpenAPI document that was generated in the previous section by running the following command: 
         
         gcloud endpoints services deploy echov1openapi.json

This creates a new Endpoints service with the name that you specified in the `hostname` argument when you ran the Endpoints tool to generate the OpenAPI document. No matter what the Endpoints service name is, when you deploy the API on App Engine, a DNS record is created using the name format `YOUR_PROJECT_ID.appspot.com`, which is the FQDN that you use when you send requests to the API.

As it is creating and configuring the service, Service Management outputs a great deal of information to the terminal. You can safely ignore the warnings about the paths in `echov1openapi.json` not requiring an API key. When the deployment completes, a message similar to the following displays:
         
         Service Configuration [2017-02-13r2] uploaded for service [example-project-12345.appspot.com]
         

In the preceding example, `2017-02-13-r2` is the service configuration ID and `example-project-12345.appspot.com` is the service name.

See [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) in the `gcloud` reference documentation for more information.




### Checking required services

To provide API management, Endpoints Frameworks requires the following services: Name | Title  
---|---  
`servicemanagement.googleapis.com` | Service Management API  
`servicecontrol.googleapis.com` | Service Control API  
  
In most cases, the `gcloud endpoints services deploy` command enables these required services. However, the `gcloud` command completes successfully but doesn't enable the required services in the following circumstances:

  * If you used a third-party application such as Terraform, and you don't include these services.

  * You deployed the Endpoints configuration to an existing Google Cloud project in which these services were explicitly disabled.




Use the following command to confirm that the required services are enabled:
    
    
    gcloud services list

If you do not see the required services listed, enable them:
    
    
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

Also enable your Endpoints service:
    
    
    gcloud services enable ENDPOINTS_SERVICE_NAME

To determine the ENDPOINTS_SERVICE_NAME you can either:

  * After deploying the Endpoints configuration, go to the **Endpoints** page in the Cloud console. The list of possible ENDPOINTS_SERVICE_NAME are shown under the **Service name** column.

  * For OpenAPI, the ENDPOINTS_SERVICE_NAME is what you specified in the `host` field of your OpenAPI spec. For gRPC, the ENDPOINTS_SERVICE_NAME is what you specified in the `name` field of your gRPC Endpoints configuration.




For more information about the `gcloud` commands, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

## Running the sample locally

After deploying the Endpoints configuration, you can run the sample locally by using the [Local development server](https://docs.cloud.google.com/appengine/docs/standard/python/tools/using-local-server).

  1. Make sure you are in the sample main directory:
         
         python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo
         

  2. Start the local development server:
         
         dev_appserver.py ./app.yaml
         

By default, the development server listens on `http://localhost:8080`, as indicated in the Google Cloud console logs printed by `dev_appserver.py`:
         
         INFO 2018-01-01 [...] Starting module "default" running at: http://localhost:8080
         

  3. Send a request to the local development server:




### Linux or Mac OS
    
    
    curl \
        --request POST \
        --header "Content-Type: application/json" \
        --data '{"message":"hello world"}' \
        http://localhost:8080/_ah/api/echo/v1/echo
    

In the preceding `curl`: 

  * The `--data` option specifies the data to post to the API.
  * The `--header` option specifies that the data is in JSON format.



### PowerShell
    
    
    (Invoke-WebRequest -Method POST -Body '{"message": "hello world"}' `
        -Headers @{"content-type"="application/json"} `
        -URI "http://localhost:8080/_ah/api/echo/v1/echo").Content
    

In the previous example, the first two lines end in a backtick. When you paste the example into PowerShell, make sure there isn't a space following the backticks. For information about the options used in the example request, see [Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-6) in the Microsoft documentation.

The API echoes back the message that you send it, and responds with the following:
    
    
    {
     "message": "hello world"
    }
    

## Deploying the API backend

So far you have deployed the OpenAPI document to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through deploying the sample API to App Engine.

To deploy the API backend:

  1. Display the service configuration ID by running the following command: 
         
         gcloud endpoints configs list --service=[YOUR_PROJECT_ID].appspot.com

Replace `[YOUR_PROJECT_ID]` with your project ID. For example:
         
         gcloud endpoints configs list --service=example-project-12345.appspot.com
         
         

  2. Open the `app.yaml` file in the `python-docs-samples/appengine/standard/endpoints-frameworks-v2/echo` directory.
         
         env_variables:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy swagger.json' command.
           ENDPOINTS_SERVICE_NAME: YOUR-PROJECT-ID.appspot.com
           ENDPOINTS_SERVICE_VERSION: 2016-08-01r0

  3. Make the following changes in the `env_variables` section: 
     * In the `ENDPOINTS_SERVICE_NAME` field, replace `YOUR-PROJECT-ID` with your Google Cloud project ID. 
     * In the `ENDPOINTS_SERVICE_VERSION` field, replace the text with the service configuration ID. For example: 
    
    ENDPOINTS_SERVICE_NAME: example-project-12345.appspot.com
      ENDPOINTS_SERVICE_VERSION: 2017-02-13r2
    

  4. Run the following command: 
         
         gcloud app deploy

  5. Follow the on-screen prompts. Wait a few moments for the deployment to succeed, ignoring the warning messages. When the deployment completes, a message similar to the following displays: 
         
         File upload done.
         Updating service [default]...done.
         

If you got an error message, see the [ Troubleshooting](https://docs.cloud.google.com/appengine/docs/standard/python/tools/uploadinganapp#troubleshooting) section in the App Engine documentation for information.

We recommend that you wait a few minutes before sending requests to your API while App Engine completely initializes.




## Sending a request to the sample API

### Linux or Mac OS

Send an HTTP request by using `curl`. Replace `[YOUR_PROJECT_ID]` with your Google Cloud project ID:
    
    
    curl \
        --request POST \
        --header "Content-Type: application/json" \
        --data '{"message":"hello world"}' \
        https://[YOUR_PROJECT_ID].appspot.com/_ah/api/echo/v1/echo
    

In the preceding `curl`: 

  * The `--data` option specifies the data to post to the API.
  * The `--header` option specifies that the data is in JSON format.



### PowerShell

Send an HTTP request by using `Invoke-WebRequest`. Replace `[YOUR_PROJECT_ID]` with your Google Cloud project ID:
    
    
    (Invoke-WebRequest -Method POST -Body '{"message": "hello world"}' `
        -Headers @{"content-type"="application/json"} -URI `
         "https://[YOUR_PROJECT_ID].appspot.com/_ah/api/echo/v1/echo").Content
    

In the previous example, the first two lines end in a backtick. When you paste the example into PowerShell, make sure there isn't a space following the backticks. For information about the options used in the example request, see [Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-6) in the Microsoft documentation.

### Third-party app

You can use a third-party application such as the Chrome browser extension [Postman](https://www.getpostman.com/) to send the request: 

  * Select `POST` as the HTTP verb.
  * For the header, select the key `content-type` and the value `application/json`.
  * For the body, enter the following:  
` {"message":"hello world"} `
  * Enter the URL to the sample application. For example:   
` https://example-project-12345.appspot.com/_ah/api/echo/v1/echo `



The API echoes back the message that you send it, and responds with the following:
    
    
    {
     "message": "hello world"
    }
    

If you didn't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/frameworks/troubleshoot-response-errors).

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Tracking API activity

  1. View the activity graphs for your API in the Google Cloud console on the **Endpoints** > **Service** page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

It might take a few moments for the request to be reflected in the graphs.

  2. Look at the request logs for your API in the Logs Explorer page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn about [the Endpoints Frameworks architecture](https://docs.cloud.google.com/endpoints/docs/frameworks/frameworks-extensible-service-proxy).
  * Learn about [creating an API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api).
  * Learn about [creating a web server](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server) to serve your API.
  * Learn about [serving your API from a different path](https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server#serve_from_different_path).
  * Learn about [monitoring your API](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api).
  * Learn about [restricting access with API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks).
  * Learn about [configuring a custom domain name](https://docs.cloud.google.com/endpoints/docs/frameworks/serving-apis-from-domains).
  * Learn about [handling API versioning](https://docs.cloud.google.com/endpoints/docs/frameworks/python/handling-api-versioning).
  * Learn about [support options](https://docs.cloud.google.com/endpoints/docs/frameworks/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
