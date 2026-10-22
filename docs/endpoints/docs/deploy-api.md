---
url: https://docs.cloud.google.com/endpoints/docs/deploy-api/
title: Quickstart: Deploy an API managed by Cloud Endpoints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:44.725643+00:00
---

# Quickstart: Deploy an API managed by Cloud Endpoints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/deploy-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an API managed by Cloud Endpoints

This QuickStart walks you through deploying a sample API, which Cloud Endpoints manages. The sample code includes:

  * A REST API that you can query to find the name of an airport from its three-letter IATA code.
  * A script that uploads the API configuration to Endpoints.
  * A script that deploys an App Engine flexible environment backend to host the sample API.



After you send requests to the sample API, you can view the Endpoints activity graphs and Google Cloud Observability logs in the Google Cloud console. These tools let you monitor your APIs and gain insights into their usage.

This QuickStart uses scripts to simplify the configuration steps for you to quickly see the activity graphs and logs in action. To learn how to configure and deploy a sample API, choose a tutorial for one of the API frameworks:

  * [Cloud Endpoints for OpenAPI: Tutorials](https://docs.cloud.google.com/endpoints/docs/openapi/tutorials)
  * [Cloud Endpoints for gRPC: Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials)
  * [Cloud Endpoints Frameworks: Tutorials](https://docs.cloud.google.com/endpoints/docs/frameworks/tutorials)



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

To get the permissions that you need to deploy and manage an API, ask your administrator to grant you the following IAM roles on your project: 

  * Deploy the Endpoints configuration: [Service Management Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.admin) (`roles/servicemanagement.admin`) 
  * Enable required services: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * Create the App Engine application: [App Engine Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.appCreator) (`roles/appengine.appCreator`) 
  * Deploy the sample API to App Engine: 
    * [App Engine Deployer ](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.deployer) (`roles/appengine.deployer`)
    * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`)
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Starting Cloud Shell

  1. In the Google Cloud console, make sure you are in the project that you want to use for the sample API.

  2. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

A Cloud Shell session opens inside a new frame at the bottom of the Google Cloud console and displays a command-line prompt. It can take a few seconds for the session to initialize.

![Cloud Shell session](https://docs.cloud.google.com/static/endpoints/docs/images/new-console.png)

  3. If you're using an existing project, make sure you have the latest version of all installed `gcloud` components:
         
         gcloud components update
         


**Note:** If you're on a Linux or macOS machine and want to follow this quickstart using your local shell, download the [Google Cloud CLI](https://cloud.google.com/sdk/install) and carry out these quickstart instructions by using your local command-line interface instead of Cloud Shell.

## Getting the sample code

  1. In Cloud Shell, enter the following command to get the sample API and scripts:


    
    
    git clone https://github.com/GoogleCloudPlatform/endpoints-quickstart

  1. Change to the directory that contains the sample code:


    
    
    cd endpoints-quickstart

## Deploying the Endpoints configuration

To publish a REST API to Endpoints, an OpenAPI configuration file that describes the API is required. The sample API comes with a pre-configured OpenAPI file called `openapi.yaml`.

Endpoints uses Service Management, an infrastructure service of Google Cloud to create and manage APIs and services. To use Endpoints to manage an API, you deploy the API's OpenAPI configuration file to Service Management.

To deploy the Endpoints configuration:

  1. In Cloud Shell, in the `endpoints-quickstart` directory, enter the following:


    
    
    cd scripts

  1. Run the following script, which is included in the sample:


    
    
    ./deploy_api.sh

Endpoints uses the `host` field in the OpenAPI configuration file to identify the service. The `deploy_api.sh` script sets the ID of your Google Cloud project as part of the name configured in the `host` field. When you prepare an OpenAPI configuration file for your own service, you need to do this manually.

The script then deploys the OpenAPI configuration to Service Management by using the command: `gcloud endpoints services deploy openapi.yaml`

As it is creating and configuring the service, Service Management outputs information to the Google Cloud console. You can safely ignore the warnings about the paths in `openapi.yaml` not requiring an API key. On successful completion, you see a line similar to the following that displays the service configuration ID and the service name:
    
    
        Service Configuration [2017-02-13-r2] uploaded for service [airports-api.endpoints.example-project.cloud.goog]
    

## Enabling required services

At a minimum, Endpoints requires the following Google services to be enabled:

Name | Title  
---|---  
`servicecontrol.googleapis.com` | Service Control API  
`servicemanagement.googleapis.com` | Service Management API  
  
In most cases, deploying the Endpoints configuration enables these required services.

Use the following command to confirm that the required services are enabled:
    
    
    gcloud services list

If you don't see the required services listed, enable them:
    
    
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

Also enable your Endpoints service:
    
    
    gcloud services enable YOUR-PROJECT-ID.appspot.com

For more information about the `gcloud` commands, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

## Deploying the API backend

So far you have deployed the OpenAPI configuration to Service Management, but you haven't yet deployed the code to serve the API backend. The `deploy_app.sh` script included in the sample creates an App Engine flexible environment to host the API backend, and then the script deploys the API to App Engine.

To deploy the API backend:

  * In Cloud Shell, in the `endpoints-quickstart/scripts` directory, run the following script:


    
    
    ./deploy_app.sh

The script runs the following command to create an App Engine flexible environment in the `us-central` region: `gcloud app create --region="$REGION" `

It takes several minutes to create the App Engine flexible environment backend. After the application is created, the output is:
    
    
    Success! The app is now created.
    

Next, the script runs the `gcloud app deploy` command to deploy the sample API to App Engine.

The output is:
    
    
    Deploying ../app/app_template.yaml...You are about to deploy the following services:
    

It takes several minutes to deploy the API to App Engine. When the API is successfully deployed to App Engine, the output is:
    
    
    Deployed service [default] to [https://example-project.appspot.com]
    

## Sending requests to the API

  * In Cloud Shell, after deploying the sample API, you can send requests to it by running the following script:


    
    
    ./query_api.sh

The script echoes the `curl` command that it uses to send a request to the API, and then displays the result. The output is:
    
    
    curl "https://example-project.appspot.com/airportName?iataCode=SFO"
    San Francisco International Airport
    

The API expects one query parameter, `iataCode`, that is set to a valid IATA airport code such as `SEA` or `JFK`. For example:
    
    
    ./query_api.sh JFK

**Note** : App Engine may take a few minutes to respond successfully to requests. If you send a request and get an HTTP 502, 503, or some other server error, wait a minute and try the request again.

You just deployed and tested an API in Endpoints!

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Tracking API activity

With APIs deployed with Endpoints, you can monitor critical operations metrics in the Google Cloud console, and gain insight into your users and usage with Cloud Logging.

  1. In Cloud Shell, run the traffic generation script to populate the graphs and logs:


    
    
    ./generate_traffic.sh
    
    
    Note: This script generates requests in a loop and automatically times out
    in 5 minutes. To end the script sooner, enter `Control+C` in
    Cloud Shell.
    

  1. In the Google Cloud console, look at the activity graphs for your API.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

It might take a few moments for the requests to be reflected in the graphs. While you wait for data to be displayed:

     * If the Permissions side panel isn't open, click **+Permissions**. The Permissions panel lets you [control who has access](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-callers) to your API and the level of access.

     * Click **Deployment history**. This tab displays a history of your API deployments, including the deployment time and who deployed the change.

     * Click **Overview**. You see the traffic coming in. After the traffic generation script has been running for a minute, you see three lines on the **Total latency** graph (50th, 95th, and 98th percentiles). This data provides an estimate of response times.

  2. Below the graphs, and under **Links** , click **View Logs** for **GET/airportName**. The **Logs Explorer** page displays the request logs for the API.

  3. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  4. To stop the script, enter `Control+C`.




## Adding a quota to the API

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Endpoints lets you set quotas that let you control the rate at which applications can call your API. You can use quotas to protect your API from excessive usage by a single client.

  1. In Cloud Shell, deploy the Endpoints configuration that has a quota.


    
    
    ./deploy_api.sh ../openapi_with_ratelimit.yaml
    
    
    After you deploy an updated Endpoints configuration, it
    becomes active within a minute.
    

  1. In the Google Cloud console, go to the **Credentials** page.

[Go to the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then click **API key**. A new API key is displayed on the screen.

  3. Click **Copy** _file_copy_.

  4. In Cloud Shell, type the following. Replace `YOUR_API_KEY` with the API key you just created.



    
    
    export API_KEY=YOUR_API_KEY
    

  1. Send your API a request using the API key you just generated.


    
    
    ./query_api_with_key.sh $API_KEY
    
    
    The output is similar to the following:
    
    
    
    curl -H 'x-api-key: AIzeSyDbdQdaSdhPMdiAuddd_FALbY7JevoMzAB' "https://example-project.appspot.com/airportName?iataCode=SFO"
    San Francisco International Airport
    

  1. The API now has a limit of 5 requests per minute. Run the following command to send traffic to the API and trigger the quota limit.


    
    
    ./generate_traffic_with_key.sh $API_KEY

  1. After running the script for 5-10 seconds, enter `Control+C` to stop the script.

  2. Send another authenticated request to the API.



    
    
    ./query_api_with_key.sh $API_KEY
    
    
    The output is similar to the following:
    
    
    
    {
        "code": 8,
        "message": "Insufficient tokens for quota 'airport_requests' and limit 'limit-on-airport-requests' of service 'example-project.appspot.com' for consumer     'api_key:AIzeSyDbdQdaSdhPMdiAuddd_FALbY7JevoMzAB'.",
        "details": [
        {
        "@type": "type.googleapis.com/google.rpc.DebugInfo",
        "stackEntries": [],
        "detail": "internal"
        }
        ]
    }
    

If you get a different response, try running the `generate_traffic_with_key.sh` script again and then retry.

Congratulations! You've successfully rate-limited your API. You can also set varying limits on different API methods, create multiple kinds of quotas, and keep track of which consumers use which APIs.

For more information, see [About quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid incurring charges, you can delete your Google Cloud project to stop billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * For on overview of Endpoints:

    * [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints)
    * [Endpoints: Architectural overview](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview)
  * To learn about the different API frameworks that Endpoints supports:

    * [The OpenAPI Specification](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview)
    * [Endpoints for gRPC APIs](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)
    * [About Endpoints Frameworks](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * To learn how to configure and deploy a sample API, choose a tutorial for one of the API frameworks:

    * [Endpoints for OpenAPI: Tutorials](https://docs.cloud.google.com/endpoints/docs/openapi/tutorials)
    * [Endpoints for gRPC: Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials)
    * [Endpoints Frameworks: Tutorials](https://docs.cloud.google.com/endpoints/docs/frameworks/tutorials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
