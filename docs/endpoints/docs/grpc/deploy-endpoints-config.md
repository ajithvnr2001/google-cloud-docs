---
url: https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config/
title: Deploying the Endpoints configuration \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:39.436968+00:00
---

# Deploying the Endpoints configuration  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Deploying the Endpoints configuration Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

After you configure your `.proto` file and [gRPC API configuration file](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints), you deploy them so that Cloud Endpoints has the information that it needs to manage your API. To deploy the Endpoints configuration, you use the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview), Google's foundational services platform, used by Endpoints and other services to create and manage APIs and services. This page describes how to deploy your configuration files to Endpoints.

## Prerequisites

As a starting point, this page assumes that you have:

  * [Created a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) in which you have the **Editor** or **Owner** role. After the initial deployment, you can grant the more restrictive **Service Config Editor** role. See [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/grpc/control-api-access) for more information.

  * [Installed gRPC and the gRPC tools](https://grpc.io/docs/quickstart/)

  * Configured Endpoints, which includes:

    * [Choosing the service name](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints#service_name).
    * [Configuring the protocol buffer](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints#configuring_the_protocol_buffer).
    * [Configuring the gRPC service configuration file](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints#configuring_the_grpc_service_configuration_file).
  * If you use a custom domain name (such as, `example.com`), you must [verify the domain name](https://docs.cloud.google.com/endpoints/docs/grpc/verify-domain-name) before you can deploy the gRPC configuration files.




## Preparing Google Cloud CLI for deployment

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



## Deploying the configuration files

  1. Make sure you are in the directory where the `api_descriptor.pb` and `api_config.yaml` files are located. 
  2. Confirm that the default project that the `gcloud` command-line tool is currently using is the Google Cloud project that you want to deploy the Endpoints configuration to. Validate the project ID returned from the following command to make sure that the service doesn't get created in the wrong project. 
         
         gcloud config list project
         

If you need to change the default project, run the following command:
         
         gcloud config set project YOUR_PROJECT_ID
         

  3. Deploy the `proto descriptor` file and the configuration file by using the Google Cloud CLI: 
         
         gcloud endpoints services deploy api_descriptor.pb api_config.yaml
         

As it is creating and configuring the service, Service Management outputs information to the terminal. When the deployment completes, a message similar to the following is displayed:
         
         Service Configuration [CONFIG_ID] uploaded for service [bookstore.endpoints.example-project.cloud.goog]

CONFIG_ID is the unique Endpoints service configuration ID created by the deployment. For example:
         
         Service Configuration [2017-02-13r0] uploaded for service [bookstore.endpoints.example-project.cloud.goog]
         

In the previous example, `2017-02-13r0` is the service configuration ID and `bookstore.endpoints.example-project.cloud.goog` is the service name. The service configuration ID consists of a date stamp followed by a revision number. If you deploy the Endpoints configuration again on the same day, the revision number is incremented in the service configuration ID.




If your service's configuration is in multiple YAML files, you can pass them all to the `deploy` command. For example, the Bookstore has its basic configuration in `api_config.yaml`, but you can enable HTTP transcoding for the service by also deploying `api_config_http.yaml`, which has additional configuration for this feature:
    
    
    gcloud endpoints services deploy api_descriptor.pb api_config.yaml api_config_http.yaml
    

The above gcloud command only supports one proto descriptor file and it has to be the first file in the gcloud command arguments. If you have multiple gRPC services in different proto files, please use the `protoc` command-line tool to combine them into one descriptor file.

Note that if there are conflicting values in your YAML files, the values in the last specified file override the others. You can find out more about how Endpoints handles merging multiple YAML files in [Configuring a gRPC service](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config).

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-config-deployment) for information on troubleshooting the error.

## Redeploying

Whenever you change something in your `.proto` or service configuration YAML file, deploy the files again so that the Extensible Service Proxy (ESP) has the most recent version of your API's service configuration. If you previously deployed ESP with the [`rollout` option set to `managed`](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend#deploying_your_api_and_esp), you don't need to restart or redeploy ESP. The `rollout=managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 

After the initial Endpoints configuration deployment, you can grant a user, service account, or group a role that allows them to redeploy the Endpoints configuration. See [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/grpc/control-api-access) for more information.

## What's next

  * [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend)
  * [Running ESP Locally or on another platform](https://docs.cloud.google.com/endpoints/docs/grpc/running-esp-localdev)
  * [Getting the service name and configuration ID](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
