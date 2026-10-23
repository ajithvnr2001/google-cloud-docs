---
url: https://docs.cloud.google.com/api-gateway/docs/deploying-api/
title: Deploy an API to a gateway \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:55.558840+00:00
---

# Deploy an API to a gateway  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/deploying-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an API to a gateway

This page describes how to deploy an API to API Gateway. 

## Prerequisites

Before you can deploy an API to API Gateway, ensure that you do the following:

  * Prepare your development environment as described in [Configure your development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env).

  * [Create an API](https://docs.cloud.google.com/api-gateway/docs/creating-api), if using the Google Cloud CLI.  
**Note** : When using the Google Cloud console, this step is completed when deploying the API, as described in the following section.

  * [Create an OpenAPI spec](https://docs.cloud.google.com/api-gateway/docs/openapi-overview) that defines your API.

  * [Create an API config](https://docs.cloud.google.com/api-gateway/docs/creating-api-config) from your API definition.




## Gateway ID requirements

Many of the gcloud CLI commands described in this document require you to specify the ID of the gateway, in the form: GATEWAY_ID. API Gateway enforces the following requirements for the gateway ID:

  * Must have a maximum length of 49 characters.
  * Must contain only lowercase letters, numbers, or dashes.
  * Must not start with a dash.
  * Must not contain an underscore.



## Define the endpoint of the deployed API config

When you deploy an API config to a gateway, API Gateway creates a unique URL for the gateway in the `gateway.dev` domain. Your API clients then use a URL in the following format to access the deployed API config:
    
    
    https://GATEWAY_ID-HASH.REGION_CODE.gateway.dev
    

where GATEWAY_ID is the name of the gateway, HASH is the unique hash code generated when you deployed the API, and REGION_CODE is the code for the [Cloud location](https://cloud.google.com/about/locations) in which you deployed the gateway.

For example:
    
    
    https://**my-gateway** -**a12bcd345e67f89g0h**.**uc**.gateway.dev
    

**Note:** Gateways that use model routing can instead get a hostname in a second `gateway.dev` format, for example `https://my-gateway-123456789012.us-central1.gateway.dev`. Gateways created earlier keep their existing hostname, which for model routing is a `run.app` hostname. See [Configure model routing](https://docs.cloud.google.com/api-gateway/docs/model-routing-configure) for details.

## Deploy an API to a gateway

To deploy an API to a gateway:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click add_box **Create Gateway**

The **Create Gateway** page displays.

  3. In the **Select an API** , select **Create new API** in the **Select an API** field.
  4. In the **Display Name** field, enter the display name of the API. 
  5. In the **API ID** field, enter the ID of the API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api-id-requirements) for API naming guidelines.
  6. (Optional) Add labels for your API.
  7. In the **API Config** section, select **Create a new API config** in the **Select a Config** field 
  8. In the **Upload an API Spec** field, upload a `.yaml` or `.json` file. See [OpenAPI 2.0 and OpenAPI 3.x](https://docs.cloud.google.com/api-gateway/docs/get-started-app-engine#create-api-config) file formats for API definition.
  9. In the **Display Name** field, enter the display name of the API config. 
  10. In the **Select a Service Account** list, select the required service account. This service account will be used by API Gateway as its identity.
  11. (Optional) Add labels for your API config.
  12. In the **Gateway details** section, enter a display name for your gateway. 
  13. In the **Location** field, select the Google Cloud region where you want to deploy your gateway. 
  14. (Optional) Add labels for your API Gateway.
  15. Click **Create gateway**.

The newly created API is visible on the [API Gateway](https://console.cloud.google.com/api-gateway) homepage.




###  Google Cloud CLI 

  1. Validate the project ID returned from the following command to make sure that the gateway isn't created in the wrong project.
         
         gcloud config list project

If you need to change the default project, run the following command and replace PROJECT_ID with the Google Cloud project ID in which you want to create the service::
         
         gcloud config set project PROJECT_ID

  2. View help for the `gateway create` command:
         
         gcloud api-gateway gateways create --help

  3. Run the following command to deploy the API config to the gateway:
         
         gcloud api-gateway gateways create GATEWAY_ID \
          --api=API_ID --api-config=CONFIG_ID \
          --location=GCP_REGION 

where:

     * GATEWAY_ID specifies the ID of the new gateway. If the gateway does not already exist then this command creates it.
     * API_ID specifies the ID of the API Gateway API associated with this gateway.
     * CONFIG_ID specifies the ID of the API config deployed to the gateway. You must specify an API config when creating a gateway.
     * GCP_REGION specifies the Cloud location for the deployed gateway.
**Note:** Allowed values are: 
     * `asia-northeast1`
     * `australia-southeast1`
     * `europe-west1`
     * `europe-west2`
     * `us-east1`
     * `us-east4`
     * `us-central1`
     * `us-west2`
     * `us-west3`
     * `us-west4`

As it is creating the gateway, the gcloud CLI outputs information to the terminal.

  4. On successful completion, you can use the following command to view details about the gateway:
         
         gcloud api-gateway gateways describe GATEWAY_ID \
          --location=GCP_REGION 

This command returns the following:
         
         apiConfig: projects/PROJECT_ID/locations/global/apis/API_ID/configs/CONFIG_ID
         createTime: '2020-02-05T13:44:12.997862831Z'
         **defaultHostname : my-gateway-a12bcd345e67f89g0h.uc.gateway.dev**
         displayName: GATEWAY_ID
         name: projects/PROJECT_ID/locations/GCP_REGION/gateways/GATEWAY_ID
         serviceAccount:
          email: gateway-111111@222222-tp.iam.gserviceaccount.com
         state: ACTIVE
         updateTime: '2020-02-05T13:45:00.844705087Z'

Note the value of the `defaultHostname` property. This is the hostname portion of the gateway URL. To access an API config deployed to this gateway, you use a URL in the form:
         
         https://my-gateway-a12bcd345e67f89g0h.uc.gateway.dev




The gcloud CLI takes many options, including those described in the [gcloud Reference](https://docs.cloud.google.com/sdk/gcloud/reference). In addition, for API Gateway, you can set the following options when creating a gateway:

  * `--async`: Return control to the terminal immediately, without waiting for the operation to complete.
  * `--display-name=NAME`: Specifies the display name of the gateway, meaning the name shown in the UI. Don't use spaces in the name. Use hyphens and underscores instead. The default value is GATEWAY_ID.
  * `--labels=KEY1=VALUE1,KEY2=VALUE2,...`: Specifies labels associated with the gateway.
  * `--enable-streaming`: Specifies support for streaming (Public Preview). This is a create-time option and cannot be modified after gateway creation. If omitted, API Gateway selects the mode automatically. If this flag is not recognized, run `gcloud components update` to update your component installation. For more information, see [Configure streaming](https://docs.cloud.google.com/api-gateway/docs/streaming-configure).



## List gateways

This section explains how to view a list of all gateways deployed in your Google Cloud project.

###  Google Cloud console 

In the Google Cloud console, go to the **API Gateway** > **Gateways** page.

[Go to Gateways](https://console.cloud.google.com/api-gateway/gateway)

###  Google Cloud CLI 

To list gateways for a specific project:
    
    
    gcloud api-gateway gateways list 

This command returns output in the form:
    
    
    GATEWAY_ID        LOCATION       DISPLAY_NAME     STATE     CREATE_TIME          UPDATE_TIME
    my-gateway        us-central1    my-gateway       ACTIVE    2021-01-07T00:04:19  2022-05-21T00:33:46

To list gateways for a specific project and region:
    
    
    gcloud api-gateway gateways list --location=GCP_REGION 

Use a `filter` expression to list the gateways associated with a specific API:
    
    
    gcloud api-gateway gateways list \
    --filter="apiConfig:projects/PROJECT_ID/locations/global/apis/API_ID/*" \
    

Or use this `filter` to list gateways for a specific API config:
    
    
    gcloud api-gateway gateways list \
    --filter="apiConfig:projects/PROJECT_ID/locations/global/apis/API_ID/configs/CONFIG_ID" \
    --project=PROJECT_ID

Use the region, and gateway IDs to obtain detailed information about the gateway, including the identity of the API config deployed to the gateway:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
    --location=GCP_REGION 

## Update a gateway

Update a gateway to:

  * Deploy a different API config to the gateway
  * Update the display name
  * Update the labels

**Note:** You cannot update a gateway to change its streaming mode. Streaming mode is determined during gateway creation. For more information, see [Configure streaming](streaming-configure).

###  Google Cloud console 

Refer the following steps to update the API Gateway details: 

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click the required API.
  3. Click the **Gateways** tab.
  4. Click the required Gateway.
  5. Click edit **Edit**.
  6. Edit the **Display Name** or **Labels**.
  7. Select the required **API Config** , or click **Create new API config** and create the config as described in [Creating an API config](https://docs.cloud.google.com/api-gateway/docs/creating-api-config).
  8. Click **Update**.
  9. Click  arrow_back  to return on the Gateway list page.
  10. On the Gateway list page, you can view the updated Gateway. 



###  Google Cloud CLI 

Use the following gcloud CLI command to update an existing gateway, where UPDATE_OPTIONS is replaced with the gateway option flag and value you want to update:
    
    
    gcloud api-gateway gateways update GATEWAY_ID \
    UPDATE_OPTIONS --api=API_ID --location=GCP_REGION   

For example, to update the API config deployed to the gateway:
    
    
    gcloud api-gateway gateways update GATEWAY_ID \
    --api-config=NEW_CONFIG_ID --api=API_ID --location=GCP_REGION 

where NEW_CONFIG_ID specifies the new API config to deploy to the gateway.

**Note** : There are two important points to keep in mind when updating a gateway with a new API config: 

  * Gateways only support API configs created under the same API. To deploy an API config created under an other API, you must either create a new gateway or use a gateway that already serves configs under the new API.
  * API Gateway supports a zero-downtime update model, which means your API continues to handle requests during the deployment of the updated API config. However, there is a period of time while the new API config is being deployed when some requests might still be handled by the previous version of the API config. If you have deployed the API config across multiple regions and gateways, you have to redeploy the updated API config in each region separately.



For a complete list of available update flags and arguments, see the [gcloud api-gateway gateways update](https://docs.cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/update) reference or use the following command to view all update options:
    
    
    gcloud api-gateway gateways update --help

## Delete a gateway

This section describes how to delete an existing API Gateway. Follow these steps to permanently remove a gateway and its associated configuration from your Google Cloud project.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **API Gateway** > **Gateways** page.

[Go to Gateways](https://console.cloud.google.com/api-gateway/gateway)

  2. Click **More** more_vert and then click **Delete** to delete the chosen API Gateway. 



###  Google Cloud CLI 

Use the following gcloud CLI command to delete an existing gateway:
    
    
    gcloud api-gateway gateways delete GATEWAY_ID \
    --location=GCP_REGION 

## What's next

  * [Monitor your API](https://docs.cloud.google.com/api-gateway/docs/monitoring)
  * [Pass data to and from the backend service](https://docs.cloud.google.com/api-gateway/docs/passing-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
