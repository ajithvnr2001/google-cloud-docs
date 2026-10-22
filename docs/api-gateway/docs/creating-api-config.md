---
url: https://docs.cloud.google.com/api-gateway/docs/creating-api-config/
title: Create an API config \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:35.006479+00:00
---

# Create an API config  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/creating-api-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an API config

This page describes how to create an API config to deploy on API Gateway.

## Before you begin

Before you create an API config, do the following:

  * Prepare your development environment as described in [Configure your development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env).

  * Create an API definition as an [OpenAPI spec](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

  * If using the Google Cloud CLI, optionally [create an API](https://docs.cloud.google.com/api-gateway/docs/creating-api). If the API doesn't exist, then creating the API config creates it. 

**Note** : When using the Google Cloud console, the API and API config are created when [deploying the API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).




## API config ID requirements

Many of the gcloud CLI commands shown require you to specify the ID of the API config, in the form: CONFIG_ID. API Gateway enforces the following requirements for the API config ID:

  * Must have a maximum length of 63 characters.
  * Must contain only lowercase letters, numbers, or dashes.
  * Must not start with a dash.
  * Must not contain an underscore.



## Create an API config

Create an API config by uploading your API definition.

**Note:** API Gateway supports creation of API definitions as [OpenAPI specs](https://docs.cloud.google.com/api-gateway/docs/openapi-overview) for all available backend services. API Gateway also supports the use of gRPC service definitions and configurations for gRPC services on Cloud Run. 

If the `managedService` in your API definition is set to an ESPv2 Beta service, make sure that the `host` field (OpenAPI 2.0) or `server.url` field (OpenAPI 3.x) is set to an `x-google-endpoint` extension in your API config.

If your API definition configures [quotas](https://docs.cloud.google.com/api-gateway/docs/quotas-overview), ensure that your quota metrics and limits remain consistent across all active API configs before you create a new one. API Gateway applies them to the entire API rather than to an individual API config, so any metric or limit that a new API config declares replaces the definition for the whole API. If you rename or remove a metric, gateways that still serve an earlier API config return errors for their quota-enforced methods. For more information, see [Quotas apply to the whole API](https://docs.cloud.google.com/api-gateway/docs/quotas-overview#quotas_apply_to_the_whole_api).

To create an API config:

###  Google Cloud console

Create an API config when you [deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

###  Google Cloud CLI

Upload your API definition to create an API config. When you upload the API definition, you are required to specify the name of the API. If the API does not already exist in API Gateway then this command also creates it.

**Note** : If you want to use OpenAPI 3.x, make sure to update the gcloud CLI components before you create an API config to avoid errors when uploading your API definition.

  1. Change to the directory containing your API definition.

For more on creating the OpenAPI spec for your API definition, see [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview) and [Quickstart: Secure traffic to a service with the gcloud CLI.](https://docs.cloud.google.com/api-gateway/docs/quickstart)

For more on creating a gRPC service definition and configuration for your API definition, see [Configure a gRPC service](https://docs.cloud.google.com/api-gateway/docs/grpc-service-config) and [Get started with API Gateway and Cloud Run for gRPC](https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc).

  2. Validate the project ID returned from the following command to make sure that the service isn't created in the wrong project.
         
         gcloud config list project

If you need to change the default project, run the following command and replace PROJECT_ID with the Google Cloud project ID in which you want to create the service:
         
         gcloud config set project PROJECT_ID

  3. View help for the `api-configs create` command:
         
         gcloud api-gateway api-configs create --help

  4. Run the following command to create the API config:
         
         gcloud api-gateway api-configs create CONFIG_ID \
               --api=API_ID --openapi-spec=API_DEFINITION \
               --project=PROJECT_ID --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

where:

     * CONFIG_ID specifies the ID of the new API config.
     * API_ID specifies the ID of the API Gateway API associated with this API config. If the API does not already exist then this command creates it.
     * API_DEFINITION specifies the name of the OpenAPI spec containing the API definition.
     * SERVICE_ACCOUNT_EMAIL specifies the service account used to sign tokens for backends with authentication configured. See [Configure the service account used to create API configs](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env#configure-service-account) for more details.

As it is creating the API and API config, API Gateway outputs information to the terminal. This operation may take several minutes to complete as the API config is propagated to downstream systems. Creation of a complex API config could take up to ten minutes to complete successfully. While a config is being created, don't attempt to create another config for the same API. Only one config may be created for any API at a time.

  5. On successful completion, you can use the following command to view details about the new API config:
         
         gcloud api-gateway api-configs describe CONFIG_ID \
               --api=API_ID

This command returns the following:
         
         createTime: '2020-02-04T18:33:11.882707149Z'
         displayName: CONFIG_ID
         gatewayConfig:
               backendConfig:
                 googleServiceAccount: 1111111@developer.gserviceaccount.com
         labels: ''
         name: projects/PROJECT_ID/locations/global/apis/API_ID/configs/CONFIG_ID
         serviceRollout:
               rolloutId: 2020-02-04r2
         state: ACTIVE
         updateTime: '2020-02-04T18:33:12.219323647Z'

  6. Enable the API using the managed service name of the API. You can find this value in the Managed Service column for your API on the APIs landing page:
         
         gcloud services enable MANAGED_SERVICE_NAME.apigateway.PROJECT_ID.cloud.goog

You only have to run this command once when you create the API. If you later modify the API, you don't have to rerun the command.




The gcloud CLI takes many options, including those described in the [Google Cloud CLI Reference](https://docs.cloud.google.com/sdk/gcloud/reference). In addition, for API Gateway, you can set the following options when creating an API config:

  * `--async`: Return control to the terminal immediately, without waiting for the operation to complete.
  * `--display-name=NAME`: Specifies the display name of the API config, meaning the name shown in the UI. Don't use spaces in the name. Use hyphens and underscores instead. The default value is CONFIG_ID.
  * `--labels=KEY1=VALUE1,KEY2=VALUE2,...`: Specifies labels associated with the API config.



For example:
    
    
    gcloud api-gateway api-configs create CONFIG_ID \
      --api=API_ID --openapi-spec=API_DEFINITION \
      --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL \
      --async --display-name=MyConfig --labels=a=1,b=2

You can see the labels in the output of the `describe` command shown, or in the `list` command by including the `--format` option:
    
    
    gcloud api-gateway api-configs list \
      --api=API_ID --format="table(name, labels)"

## List API configs

List all of the API Gateways deployed in your Google Cloud project.

###  Google Cloud console

To list API configs for a specific API in a project:

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click the required API.
  3. Click the **Configs** tab.



You will see the list of available API configs on the page.

###  Google Cloud CLI

To list API configs for a specific project:
    
    
    gcloud api-gateway api-configs list 

This command returns the following:
    
    
    NAME                                                                                                 DISPLAY_NAME             ROLLOUT_ID    STATE     CREATE_TIME
    projects/PROJECT_ID/locations/global/apis/API_ID/configs/CONFIG_ID  CONFIG_ID     2020-02-04r0  ACTIVE  2020-02-04T16:18:02.369859863Z

To list API configs for a specific API in a project:
    
    
    gcloud api-gateway api-configs list --api=API_ID 

Use the API and config IDs to obtain detailed information about the API config:
    
    
    gcloud api-gateway api-configs describe CONFIG_ID \
      --api=API_ID 

## Update an API config

You cannot modify an existing API config other than to update its labels and its display name.

**Note:** Every time you upload an API definition, API Gateway creates a new API config. 

To update an API definition:

  1. Update the OpenAPI spec containing the API definition.
  2. Upload the API definition to create a **new** API config. 



Use the same command to create the **new** API config as you used to create the initial API config, as shown in Create an API config.

###  Google Cloud console

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click the required API.
  3. Click the **Configs** tab.
  4. Click the required API config. 
  5. Click edit **Edit**.
  6. Edit **Display Name** or **Labels**.
  7. Click **Save**. 



###  Google Cloud CLI

Use the following `gcloud` to update an existing API config:

  * `--display-name`
  * `--update-labels`
  * `--clear-labels`
  * `--remove-labels`



For example:
    
    
    gcloud api-gateway api-configs **update** CONFIG_ID \
      --api=API_ID \
      --update-labels=a=1,b=2

Use the following command to view all update options:
    
    
    gcloud api-gateway api-configs update --help

## Delete an API config

**Warning:** If you deployed the API config to a gateway, the API config may not be deleted until the gateway is no longer using that API config.

Before you delete an API config that is in use, you must either:

  * Deploy a different API config to the gateway.
  * Delete the gateway.



See [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api) for more.

###  Google Cloud console

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click the required API.
  3. Click the **Configs** tab.
  4. Click **More** more_vert and then click **Delete** to delete the chosen API config. 



###  Google Cloud CLI

Use the following gcloud CLIcommand to delete an existing API config:
    
    
    gcloud api-gateway api-configs delete CONFIG_ID --api=API_ID --project=PROJECT_ID

## What's next

  * [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
