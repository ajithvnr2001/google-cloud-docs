---
url: https://docs.cloud.google.com/api-gateway/docs/configure-dev-env/
title: Configure the development environment \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:17.981707+00:00
---

# Configure the development environment  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/configure-dev-env/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the development environment

This document describes how to configure your API Gateway development environment.

## Prerequisites

Before you can create an API on API Gateway, you must do the following:

  * Create a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) in which you have the **Editor** or **Owner** role. After the initial deployment, you can grant the more restrictive **Service Config Editor** role to a user, group, or service account.

  * Prepare the Google Cloud CLI for deployment.

  * Enable the required Google services.

  * Configure the service account used to create API configs.




## Prepare the Google Cloud CLI for deployment

To prepare `gcloud` for the deployment:

  1. Install and initialize the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts).
  2. Update gcloud CLI: 
         
         gcloud components update

  3. Make sure that gcloud CLI is authorized to access your data and services: 
         
         gcloud auth login

A new browser tab opens and you are prompted to choose an account.

  4. Set the default project. Replace PROJECT_ID with your Google Cloud project ID: 
         
         gcloud config set project PROJECT_ID 




## Enable the required Google services

API Gateway requires that you enable the following Google Cloud services:

Name | Service name  
---|---  
API Gateway API | `apigateway.googleapis.com`  
Service Management API | `servicemanagement.googleapis.com`  
Service Control API | `servicecontrol.googleapis.com`  
  
To enable required services:

###  Google Cloud console

  1. In the Google Cloud console, go to the **APIs & Services > API Library** page.

[Go to API Library](https://console.cloud.google.com/apis/library)

  2. On the **API Library** page, enter the required API name into the search bar.
  3. In the search results, select the API page.
  4. On the API page, click **Enable**.
  5. Repeat these steps for each of the services listed in the preceding table.



### Google Cloud CLI

Use the following commands to enable the services:
    
    
    gcloud services enable apigateway.googleapis.com
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

For more information about the `gcloud` services, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

## Configure the service account used to create API configs

An API config deployed on a gateway executes with the permissions associated with the [gateway service account](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.apis.configs).

As a best practice, [create a separate service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) in the same project you are using for API Gateway. Then, assign the service account only the permissions necessary to access the backend service. In that way, you limit the permissions associated with the API config.

For API Gateway, the user creating or updating an API config or gateway requires the `iam.serviceAccounts.actAs` permission on the service account object. This permission is included in the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) role.

To add the required role and permission to the gateway service account:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **IAM & Admin** > **Service Accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the required project or create a new one.
  3. Click the required service account.
  4. Click the **Permissions** tab.
  5. Click **Manage access**.
  6. Click add **Add role** , and assign the `Service Account User` role to the principal who will reference the service account while creating the API config.
  7. Click **Save**.



###  Google Cloud CLI 

The role and permission can be added to the service account for the user with the following command:
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
    --member user:USER_EMAIL \
    --role roles/iam.serviceAccountUser

where:

  * SERVICE_ACCOUNT_EMAIL is the email of the service account, in the format `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`.
  * USER_EMAIL is the email address of the user.



For example:
    
    
    gcloud iam service-accounts add-iam-policy-binding **my-service-account@my-project.iam.gserviceaccount.com** \
    --member user:**myemail@email.com** \
    --role roles/iam.serviceAccountUser

In addition, the gateway service account requires the permissions necessary to access your backend service. For example:

  * For a Cloud Function backend, the service account must be assigned the role of **Cloud Functions Invoker**.
  * For a Cloud Run backend, the service account must be assigned the role of **Cloud Run Invoker**.
  * For an App Engine backend, you must follow the steps in [Set up IAP access](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts#iap-access) to grant the service account associated with your gateway the **IAP-secured Web App User** role.



By limiting the permissions associated with the API config, you can better secure your backend systems. For more information, see the [Identity and Access Management (IAM) documentation](https://docs.cloud.google.com/iam/docs).

After you create the service account, use the `--backend-auth-service-account` option to specify the email address of that service account when creating an API config:
    
    
    gcloud api-gateway api-configs create CONFIG_ID \
    --api=API_ID --openapi-spec=API_DEFINITION \
    **--backend-auth-service-account= SERVICE_ACCOUNT_EMAIL**

See [Create an API config](https://docs.cloud.google.com/api-gateway/docs/creating-api-config) for more on creating API configs.

### Use a default service account

Some Google Cloud products define a _default_ service account. For example, if you are using Compute Engine and have enabled the Compute Engine API for your project, a default Compute Engine service account is created for you. The default service account is identifiable by its email address:

`PROJECT_NUMBER-compute@developer.gserviceaccount.com`

If you assign the necessary permissions to the default service account, you can omit the `--backend-auth-service-account` option when creating an API config:
    
    
    gcloud api-gateway api-configs create CONFIG_ID \
      --api=API_ID --openapi-spec=API_DEFINITION 

See [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for more.

## Use OpenID Connect

Requests from API Gateway to backend services may use authentication. These requests are secured using OpenID Connect (OIDC) tokens signed by the gateway's service account. You should confirm that your backend service is correctly configured to accept OIDC tokens for authentication and authorization. Cloud Run functions, Cloud Run, and the Identity Aware Proxy (IAP) provide this option. 

## What's next

  * [Create an API](https://docs.cloud.google.com/api-gateway/docs/creating-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
