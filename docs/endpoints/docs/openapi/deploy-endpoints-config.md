---
url: https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config/
title: Deploying the Endpoints configuration \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:18.866448+00:00
---

# Deploying the Endpoints configuration  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Deploying the Endpoints configuration Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config "View this page for the Cloud Endpoints gRPC docs")

After you configure Cloud Endpoints in an [OpenAPI document](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#open_api_doc), you deploy it so that Endpoints has the information that it needs to manage your API. To deploy the Endpoints configuration, you use the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview), Google's foundational services platform, used by Endpoints and other services to create and manage APIs and services. This page describes how to deploy an OpenAPI document to Endpoints.

## Prerequisites

As a starting point, this page assumes that you have:

  * Created a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) in which you have the **Editor** or **Owner** role. After the initial deployment, you can grant the more restrictive **Service Config Editor** role to a user, group, or service account. See [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access) for more information.

  * [Configured Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints).

  * If you are using a custom domain name (such as `my-api.example.com`), you must [verify the domain name](https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name) before you can deploy the OpenAPI document.




## Preparing the Google Cloud CLI for deployment

You use the `gcloud` command line tool to deploy the configuration. See the [ gcloud Reference](https://docs.cloud.google.com/sdk/gcloud/reference) for more information about the commands.

To prepare for the deployment:

  1. Install and initialize the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). 
  2. Update gcloud CLI: 
         
         gcloud components update

  3. Make sure that gcloud CLI is authorized to access your data and services: 
         
         gcloud auth login

A new browser tab opens and you are prompted to choose an account.

  4. Set the default project. Replace `[YOUR-PROJECT-ID]` with your GCP project ID 
         
         gcloud config set project [YOUR-PROJECT-ID]

  5. If you will be deploying your API backend to either Kubernetes or Kubernetes Engine, run the following command to acquire new user credentials to use for Application Default Credentials. The user credentials are needed to authorize `kubectl`. 
         
         gcloud auth application-default login

A new browser tab opens and you are prompted to choose an account. 



## Validating `openapi.json` syntax

The OpenAPI document file can be in YAML format or JSON format. If it is in JSON format, we recommend that you verify the syntax before deploying the file. To check that your `openapi.json` is a well-formatted JSON file, you can open it in a JSON-validating text editor such as `vim`, use an online JSON linter service, or use Python, for example:
    
    
    python -m json.tool openapi.json
    

To improve readability, you can pretty-print the JSON file:
    
    
    python -m json.tool input.json > output.json
    

Replace `input.json` with the path to your `openapi.json` file. `output.json` is the pretty-printed JSON file.

## Validating your OpenAPI document

Not all OpenAPI constructs are [currently supported by Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-limitations). Before deploying, you can validate your OpenAPI document.

To validate your OpenAPI document:

  1. Change directory to the location containing your OpenAPI document.

  2. Confirm the Google Cloud project where you want to create the service. If you are using a custom domain name (such as, `myapi.example.com`), make sure to validate the project ID returned from the following command so that the service isn't created in the wrong project.
         
         gcloud config list project
         

If you need to change the default project, run the following command and replace `[YOUR_PROJECT_ID]` with the Google Cloud project ID in which you want to create the service:
         
         gcloud config set project [YOUR_PROJECT_ID]
         

  3. Run the following command, and replace `[YOUR_OPENAPI_DOCUMENT]` with the name of the OpenAPI document that describes your API:
         
         gcloud endpoints services deploy [YOUR_OPENAPI_DOCUMENT] --validate-only
         




The `gcloud` command then calls the [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) API to create a managed service with the name that you specified in the `host` field in your OpenAPI document. When you specify the `--validate-only` flag, a service is still created, but the configuration isn't deployed. There isn't a way to validate your OpenAPI document without creating a service. Although you can [delete the service](https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances), Service Management prevents you from creating a service with the same name for a period of approximately 30 days.

## Deploying the OpenAPI document

When you are ready to deploy your API, you run the Google Cloud CLI, which uses Service Management to upload your API configuration and to create (or update) a managed service.

To deploy your OpenAPI document:

  1. Change directory to the location containing your OpenAPI document.

  2. Validate the project ID returned from the following command to make sure that the service isn't created in the wrong project.
         
         gcloud config list project
         

If you need to change the default project, run the following command and replace `[YOUR_PROJECT_ID]` with the Google Cloud project ID in which you want to create the service::
         
         gcloud config set project [YOUR_PROJECT_ID]
         

  3. Run the following command, and replace `[YOUR_OPENAPI_DOCUMENT]` with the name of the OpenAPI document that describes your API:
         
         gcloud endpoints services deploy [YOUR_OPENAPI_DOCUMENT]
         




The first time that you run the previous command, Service Management creates a new Endpoints service in the default project with a name that matches the text that you specified in the `host` field in your OpenAPI document and uploads your service configuration.

As it is creating and configuring the service, Service Management outputs information to the terminal. On successful completion, you see a line like the following that displays the service configuration ID and the service name:
    
    
    Service Configuration [2017-02-13r0] uploaded for service [echo-api.endpoints.example-project-12345.cloud.goog]
    

In the previous example, `2017-02-13r0` is the service configuration ID and `echo-api.endpoints.example-project-12345.cloud.goog` is the service name.

After a successful deployment, you can view the API on the [**Endpoints** > **Services**](https://console.cloud.google.com/endpoints) page in the Google Cloud console.

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment).

## Redeploying

Whenever you change something in your OpenAPI document, be sure to deploy it again so that Endpoints has the most recent version of your API's service configuration. You don't need to redeploy or restart ESP if you previously deployed ESP with the [`rollout` option set to `managed`](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend#deploying_your_api_and_esp). This option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 

After the initial Endpoints configuration deployment, you can grant a user, service account, or group a role that allows them to redeploy the Endpoints configuration. See [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access) for more information.

## What's next

  * [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend)
  * [Deploying on Kubernetes](https://docs.cloud.google.com/endpoints/docs/openapi/kubernetes-concept)
  * [Running ESP locally or on another platform](https://docs.cloud.google.com/endpoints/docs/openapi/running-esp-localdev)
  * [Getting the service name and configuration ID](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
