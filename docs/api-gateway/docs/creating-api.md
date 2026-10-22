---
url: https://docs.cloud.google.com/api-gateway/docs/creating-api/
title: Create an API \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:58.060075+00:00
---

# Create an API  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/creating-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an API

This page describes how to create an API. 

## Prerequisites

Before you can create an API, do the following:

  * Prepare your development environment as described in [Configure the development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env).



## API ID requirements

Many of the `gcloud` commands shown require you to specify the ID of the API, in the form: API_ID. API Gateway enforces the following requirements for the API ID:

  * Must have a maximum length of 63 characters.
  * Must contain only lowercase letters, numbers, or dashes.
  * Must not start with a dash.
  * Must not contain an underscore.



## Create an API

Create an API.

### Google Cloud console

Create and deploy an API, as described in [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

### Google Cloud CLI

To create an API, review the following sections:

  * Steps to create an API
  * Google Cloud CLI options
  * Domain-scoped projects



#### Steps to create an API

  1. Validate the project ID returned from the following command to make sure that the service isn't created in the wrong project.
         
         gcloud config list project

If you need to change the default project, run the following command and replace PROJECT_ID with the Google Cloud project ID in which you want to create the service:
         
         gcloud config set project PROJECT_ID

If your project ID contains a colon (`:`), see Domain-scoped projects for additional details about creating an API in your project.

  2. View help for the `apis create` command:
         
         gcloud api-gateway apis create --help

  3. Run the following command to create the API:
         
         gcloud api-gateway apis create API_ID

where:

     * API_ID specifies the ID of the new API. See API ID requirements for API naming guidelines.

As it is creating the API, API Gateway outputs information to the terminal.

  4. On successful completion, you can use the following command to view details about the new API:
         
         gcloud api-gateway apis describe API_ID 

This command returns the following:
         
         createTime: '2020-02-29T21:52:20.297426875Z'
               displayName: API_ID
               managedService: MANAGED_SERVICE_NAME.apigateway.PROJECT_ID.cloud.goog
               name: projects/PROJECT_ID/locations/global/apis/API_ID
               state: ACTIVE
               updateTime: '2020-02-29T21:52:20.647923711Z'




#### Google Cloud CLI options

The Google Cloud CLI takes many options, including those described in the [gcloud Reference](https://docs.cloud.google.com/sdk/gcloud/reference). In addition, for API Gateway, you can set the following options when creating an API:

  * `--async`: Return control to the terminal immediately, without waiting for the operation to complete.
  * `--display-name=NAME`: Specifies the display name of the API, meaning the name shown in the UI. Do not use spaces in the name. Use hyphens and underscores instead. The default value is API_ID. 
  * `--labels=KEY1=VALUE1,KEY2=VALUE2,...`: Specifies labels associated with the API config.
  * `--managed-service`: Specifies a pre-existing managed service for the API. See also Domain-scoped projects



#### Domain-scoped projects

If your project is scoped to your domain, the project ID includes the name of the domain followed by a colon (`:`), for example, `example.com:my-project`. You must provide a valid managed service when creating an API in a domain-scoped project.

If using `gcloud`, provide the managed service name using the `--managed-service` flag, as described in Google Cloud CLI options.

**Note:** Scoping projects to a domain is a legacy feature. You cannot create new domain-scoped projects.

## List APIs

List all APIs in a project.

### Google Cloud console

In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

### Google Cloud CLI
    
    
    gcloud api-gateway apis list 

This command returns output in the form:
    
    
      NAME                                              DISPLAY_NAME  MANAGED_SERVICE                          STATE
      projects/PROJECT_ID/locations/global/apis/API_ID  API_ID        MANAGED_SERVICE_NAME.apigateway.PROJECT_ID.cloud.goog  ACTIVE

Use the API ID to obtain detailed information about the API:
    
    
    gcloud api-gateway apis describe API_ID 

## Update an API

After creation, you can update the labels and display name of an existing API.

### Google Cloud console

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click the required API.
  3. Click the **Details** tab.
  4. Click edit **Edit**.
  5. Edit **Display Name** or **Labels** , then click **Save**.



### Google Cloud CLI

Use the following `gcloud` options to update an existing API:

  * `--display-name`
  * `--update-labels`
  * `--clear-labels`
  * `--remove-labels`



For example:
    
    
      gcloud api-gateway apis **update** API_ID \
        --update-labels=a=1,b=2

Use the following command to view all update options:
    
    
    gcloud api-gateway apis update --help

## Delete an API

**Note:** If you deployed an API config to a gateway, then deleting the API causes the gateway to stop serving traffic. 

To delete an API, you must:

  * Delete the API Gateways associated with the API and its API configs.
  * Delete the API configs associated with the API.
  * Delete the API.



### Google Cloud console

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway)

  2. Click the API chosen to be deleted.
  3. Click the **Configs** tab.
  4. Select the API Config(s) and click **More** more_vert and then click **Delete**. 
  5. Click arrow_back to return to the **API Gateway** homepage. 
  6. Click **More** more_vert and then click **Delete** to delete the chosen API. 



### Google Cloud CLI

  1. Determine the list of API Gateways associated with the API:
         
         gcloud api-gateway gateways list --filter='apiConfig:"projects/PROJECT_ID/locations/global/apis/API_ID"'
         

  2. Delete each API config associated with the API:
         
         gcloud api-gateway api-configs delete CONFIG_ID --api=API_ID 

  3. Delete the API:
         
         gcloud api-gateway apis delete API_ID 




## What's next

  * [Create an API config](https://docs.cloud.google.com/api-gateway/docs/creating-api-config)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
