---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java/
title: Getting started with Cloud Endpoints Frameworks for Java \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:50.422670+00:00
---

# Getting started with Cloud Endpoints Frameworks for Java  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Getting started with Cloud Endpoints Frameworks for Java Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure, deploy, and send requests to a sample API using [Cloud Endpoints Frameworks for Java](https://docs.cloud.google.com/endpoints/docs/frameworks/java/about-cloud-endpoints-frameworks). Endpoints Frameworks for Java is integrated with the [App Engine standard Java 8 runtime environment](https://docs.cloud.google.com/appengine/docs/standard/java/runtime). Endpoints Frameworks consists of tools, libraries and capabilities that allow you to generate APIs and client libraries from an App Engine application.

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API.

  1. Set up a Google Cloud project. See Before you begin.
  2. Install required software and create an App Engine application. See Installing and configuring required software.
  3. Download the sample code. See Getting the sample code.
  4. Generate an OpenAPI configuration file. See Configuring Cloud Endpoints.
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

  6. Make note of the project ID because it is needed later. 



## Installing and configuring required software

  1. If you don't have Java 8 installed, download the Java Development Kit (JDK) from [ Oracle](http://www.java.com/en/download/manual.jsp) and install it. Because Endpoints Frameworks for Java depends on the App Engine standard Java 8 runtime environment, Endpoints Frameworks doesn't support any other versions of Java. 
  2. If you don't have Maven 3.3.9 or higher, [download](http://maven.apache.org/download.cgi) and [install](http://maven.apache.org/install.html) it. 

**Note for Windows users:** If you are installing the JDK and Maven on Windows, install them in a directory that doesn't have a space in the path. See [Maven on Windows](https://maven.apache.org/guides/getting-started/windows-prerequisites.html) for more information.

  3. You need an application to send requests to the sample API.

     * Linux and macOS users: This tutorial provides an example of using `curl`, which typically comes pre-installed on your operating system. If you don't have `curl`, you can download it from the `curl` [ Releases and downloads page](https://curl.haxx.se/download.html). 
     * Windows users: This tutorial provides an example using [`Invoke-WebRequest`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest), which is supported in PowerShell 3.0 and later. 
  4. [Download and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). 
  5. Run the following commands: 
     1. Make sure that the gcloud CLI is authorized to access your data and services on Google Cloud: 
            
            gcloud auth login

     2. Use application default credentials: 
            
            gcloud auth application-default login

     3. Install the Google Cloud SDK `app-engine-java` component: 
            
            gcloud components install app-engine-java

     4. Update to the latest version of the Google Cloud SDK and all components: 
            
            gcloud components update

  6. Create an App Engine application: 
     1. Set the default project to your project ID. 
            
            gcloud config set project YOUR_PROJECT_ID

Replace `YOUR_PROJECT_ID` with your Google Cloud project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

     2. Select the region where you want to create your App Engine application. Run the following command to get a list of regions: 
            
            gcloud app regions list

     3. Create an App Engine application by using the following command. Replace `YOUR_PROJECT_ID` with your Google Cloud project ID and `YOUR_REGION` with the region where you want the App Engine application created in. 
            
            gcloud app create \
            --project=YOUR_PROJECT_ID \
            --region=YOUR_REGION




## Getting the sample code

To clone the sample API from GitHub:

  1. Clone the sample repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples
         

  2. Change to the directory containing the sample code:
         
         cd java-docs-samples/appengine-java8/endpoints-v2-backend
         




## Configuring Endpoints

The sample code includes the Endpoints Frameworks tool that generates an [OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview) configuration file that describes the sample code's REST API. Follow the steps in this section to configure and build the sample Maven project so that you can then generate the OpenAPI configuration file.

### Adding the project ID to the sample API code

You must add the project ID obtained when you created your project to the sample's `pom.xml` before you can deploy the code.

To add the project ID:

  1. Edit the file `java-docs-samples/appengine-java8/endpoints-v2-backend/pom.xml`.

  2. Search for `<endpoints.project.id>`, and replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

For example:
         
         <endpoints.project.id>example-project</endpoints.project.id>
         

  3. Save your changes.




### Building the sample project

To build the project:

  1. Make sure you are in the directory `java-docs-samples/appengine-java8/endpoints-v2-backend`.

  2. Run the following command:
         
         mvn clean package
         

  3. Wait for the project to build. When the project successfully finishes, a message similar to this one displays:
         
         [INFO] BUILD SUCCESS
         [INFO] ------------------------------------------------------------------------
         [INFO] Total time: 14.846s
         [INFO] Finished at: Wed April 13 09:43:09 PDT 2016
         [INFO] Final Memory: 24M/331M
         




### Generating the OpenAPI configuration file

You use a tool from the Endpoints Frameworks library to generate an OpenAPI document called `openapi.json`. This file describes the sample code's REST API.

To generate the OpenAPI configuration file:

  1. Invoke the Endpoints Frameworks tool using this command:
         
         mvn endpoints-framework:openApiDocs
         

  2. Wait for the configuration spec to build. When it finishes a message similar to this one displays:
         
         OpenAPI document written to target/openapi-docs/openapi.json
         

Ignore any messages about failure to load a static logger class.




## Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview), Google’s foundational services platform, used by Endpoints Frameworks and other services to create and manage APIs and services

To deploy the configuration file:

  1. Make sure you are in the directory `java-docs-samples/appengine-java8/endpoints-v2-backend`.

  2. Deploy the OpenAPI configuration file that was generated in the previous section:
         
         gcloud endpoints services deploy target/openapi-docs/openapi.json
         




This creates a new Endpoints service with the name in the format `YOUR_PROJECT_ID.appspot.com`. This name is configured in `pom.xml` and other configuration files included in the sample. Note that when you deploy the API on App Engine, a DNS record is created using the name format `YOUR_PROJECT_ID.appspot.com`, which is the fully qualified domain name (FQDN) that you use when you send requests to the API.

As it is creating and configuring the service, Service Management outputs information to the terminal. You can safely ignore the warnings about the paths in `openapi.json` not requiring an API key. On successful completion, a line similar to the following displays the service configuration ID and the service name:
    
    
    Service Configuration [2017-02-13-r2] uploaded for service [example-project-12345.appspot.com]
    

In the preceding example, `2017-02-13-r2` is the service configuration ID and `example-project-12345.appspot.com` is the service name.

See [`gcloud` Endpoints services deploy](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) for more information.

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

After deploying the Endpoints configuration, you can run the sample locally.

  1. Create an environment variable called `ENDPOINTS_SERVICE_NAME`, which is used in the sample's `appengine-web.xml` file to set the hostname. In the following, replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

In Linux or Mac OS:
         
         export ENDPOINTS_SERVICE_NAME=YOUR_PROJECT_ID.appspot.com
         

In Windows PowerShell:
         
         $Env:ENDPOINTS_SERVICE_NAME="YOUR_PROJECT_ID.appspot.com"
         

  2. Acquire new user credentials to use for [Application Default Credentials](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default):
         
         gcloud auth application-default login
         

  3. Run the development server:
         
         mvn appengine:run
         

The local instance is reachable on `http://localhost:8080` as indicated by the logs printed by the `mvn appengine:run` command:
         
         [INFO] GCLOUD: INFO: Module instance default is running at http://localhost:8080/
         

  4. Send a request to the local instance:




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

So far you have deployed the OpenAPI configuration to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through deploying the sample API to App Engine.

To deploy the API backend:

  1. Make sure you are in the directory `java-docs-samples/appengine-java8/endpoints-v2-backend`

  2. Deploy the API implementation code using Maven:
         
         mvn appengine:deploy
         

The first time you upload a sample app, you might be prompted to authorize the deployment. Follow the prompts. When you are presented with a browser window containing a code, copy it to the terminal window.

  3. Wait for the upload to finish.

We recommend that you wait a few minutes before sending requests to your API while App Engine completely initializes.




## Sending a request to the API

After you deploy the API and its configuration file, you can send requests to the API.

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

You just deployed and tested an API in Endpoints Frameworks!

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Tracking API activity

  1. View the activity graphs for your API in the Google Cloud console on the **Endpoints** > **Service** page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

It might take a few moments for the request to be reflected in the graphs.

  2. Look at the request logs for your API in the Logs Explorer page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




## Creating a developer portal for the API

You can use Cloud Endpoints Portal to create a developer portal, a website that you can use to interact with the sample API. To learn more, see [Cloud Endpoints Portal overview](https://docs.cloud.google.com/endpoints/docs/frameworks/dev-portal-overview).

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

  * Learn about [the Endpoints Frameworks architecture](https://docs.cloud.google.com/endpoints/docs/frameworks/frameworks-extensible-service-proxy#endpoints_frameworks).
  * Learn about [available API annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code).
  * Learn about [serving your API from a different path](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy#serve_from_different_path).
  * Learn about [monitoring your API](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api).
  * Learn about [restricting access with API keys](https://docs.cloud.google.com/endpoints/docs/restricting-api-access-with-api-keys).
  * Learn about [handling API versioning](https://docs.cloud.google.com/endpoints/docs/frameworks/java/handling-api-versioning).
  * Learn about [community support options](https://docs.cloud.google.com/endpoints/docs/community-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
