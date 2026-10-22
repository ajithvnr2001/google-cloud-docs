---
url: https://docs.cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access/
title: Authorize service-to-service access \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:14.234080+00:00
---

# Authorize service-to-service access  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Authorize service-to-service access Stay organized with collections  Save and categorize content based on your preferences. 

If your architecture is using multiple services, you likely require credentials to enable communication between services. Cloud Build provides built-in support for the [OpenID Connect (OIDC)](https://openid.net/connect/) standard for secure authentication and authorization between services.

You can use Cloud Build to generate ID tokens. With these tokens, you can call secure endpoints from within Cloud Build.

For example, if you are running a serverless platform application like Cloud Run functions, Cloud Run, or App Engine, you can securely interact with your application from within Cloud Build workloads.

**Note:** The following instructions are only supported for user-specified service accounts. Cloud Build does not support ID token generation with the default service account.

## Before you begin

  * Enable the Cloud Build and IAM APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,iam.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access)

  * If you plan to use this account to [create short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct), then you also need to enable the IAM Service Account Credentials API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access)

  * To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk).

**Note:** If you've installed Google Cloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  * Make sure you've [created the service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) you want to use. You **must** create the account in the same Google Cloud project where you're running builds.




### Required IAM permissions

Your user-specified service account must have the `iam.serviceAccounts.getOpenIdToken` permission.

  * Grant the [Service Account OpenID Connect Identity Token Creator (`roles/iam.serviceAccountOpenIdTokenCreator`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountOpenIdTokenCreator) to your user-specified service account in the project where you created the service account.



For instructions on granting IAM roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

## Methods for obtaining an ID token

There are two ways to configure your build steps to obtain ID tokens:

  * use the gcloud CLI
  * send a direct request to the metadata server



### Get an ID token via gcloud

In this section, the following code snippet demonstrates how to use the gcloud CLI to obtain ID tokens:

###  YAML 
    
    
    steps:
    
    - name: 'gcr.io/cloud-builders/gcloud'
      script: 'gcloud auth print-identity-token --audiences ${_TOKEN_AUDIENCE} > /workspace/identity_token.txt'
      env:
      - _TOKEN_AUDIENCE=${_TOKEN_AUDIENCE}
    service_account: '$_SERVICE_ACCOUNT'
    substitutions:
      _TOKEN_AUDIENCE: 'TOKEN_AUDIENCE'
      _SERVICE_ACCOUNT_ID: 'SERVICE_ACCOUNT_ID'
      _SERVICE_ACCOUNT: 'projects/${PROJECT_ID}/serviceAccounts/${_SERVICE_ACCOUNT_ID}'
    logsBucket: 'LOGS_BUCKET_LOCATION'
    options:
      logging: GCS_ONLY
      dynamic_substitutions: true
    

###  JSON 
    
    
    {
      "steps": [
          {
              "name": "gcr.io/cloud-builders/gcloud",
              "script": "gcloud auth print-identity-token --audiences ${_TOKEN_AUDIENCE} > /workspace/identity_token.txt"
              "env": [
                  "_TOKEN_AUDIENCE=${_TOKEN_AUDIENCE}"
              ]
          }
      ],
      "service_account": "$_SERVICE_ACCOUNT",
      "substitutions": {
          "_TOKEN_AUDIENCE": "TOKEN_AUDIENCE",
          "_SERVICE_ACCOUNT_ID": "SERVICE_ACCOUNT_ID",
          "_SERVICE_ACCOUNT": "projects/${PROJECT_ID}/serviceAccounts/${_SERVICE_ACCOUNT_ID}"
      },
      "logsBucket": "LOGS_BUCKET_LOCATION",
      "options": {
          "logging": "GCS_ONLY",
          "dynamic_substitutions": true
      }
    }
    

Replace the following:

  * `TOKEN_AUDIENCE` is the URL or target audience to obtain the ID token for, such as `http://www.example.com`.
  * `SERVICE_ACCOUNT_ID` is the email address or unique ID for the user-specified service account. For example, `service-account-name@project-id.iam.gserviceaccount.com`.
  * `LOGS_BUCKET_LOCATION` is the Cloud Storage bucket to store build logs. For example, `gs://mylogsbucket`.



### Send a direct request to the metadata server

In this section, the following code snippet demonstrates how to make a direct request to the metadata server to obtain ID tokens:

###  YAML 
    
    
    steps:
    - name: 'gcr.io/cloud-builders/curl'
      id: 'printTokenFromCurl'
      script: |
        curl -H 'Metadata-Flavor: Google' http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=${_TOKEN_AUDIENCE} -o /workspace/identity_token.txt
      env:
      - _TOKEN_AUDIENCE=${_TOKEN_AUDIENCE}
    service_account: '$_SERVICE_ACCOUNT'
    substitutions:
      _TOKEN_AUDIENCE: 'TOKEN_AUDIENCE'
      _SERVICE_ACCOUNT_ID: 'SERVICE_ACCOUNT_ID'
      _SERVICE_ACCOUNT: 'projects/${PROJECT_ID}/serviceAccounts/${_SERVICE_ACCOUNT_ID}'
    logsBucket: 'LOGS_BUCKET_LOCATION'
    options:
      logging: GCS_ONLY
      dynamic_substitutions: true
    

###  JSON 
    
    
    {
      "steps": [
          {
              "name": "gcr.io/cloud-builders/curl",
              "id": "printTokenFromCurl"
              "script": "curl -H 'Metadata-Flavor: Google' http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=${_TOKEN_AUDIENCE} -o /workspace/identity_token.txt"
              "env":
                  "_TOKEN_AUDIENCE=${_TOKEN_AUDIENCE}"
          }
      ],
      "service_account": "$_SERVICE_ACCOUNT",
      "substitutions": {
          "_TOKEN_AUDIENCE": "TOKEN_AUDIENCE",
          "_SERVICE_ACCOUNT_ID": "SERVICE_ACCOUNT_ID",
          "_SERVICE_ACCOUNT": "projects/${PROJECT_ID}/serviceAccounts/${_SERVICE_ACCOUNT_ID}"
      },
      "logsBucket": "LOGS_BUCKET_LOCATION",
      "options": {
          "logging": "GCS_ONLY",
          "dynamic_substitutions": true
      }
    }
    

Replace the following:

  * `TOKEN_AUDIENCE` is the URL or target audience to obtain the ID token for, such as `http://www.example.com`.
  * `SERVICE_ACCOUNT_ID` is the email address or unique ID for the user-specified service account. For example, `service-account-name@project-id.iam.gserviceaccount.com`.
  * `LOGS_BUCKET_LOCATION` is the Cloud Storage bucket to store build logs. For example, `gs://mylogsbucket`.



For additional instructions on generating and using ID tokens in your workloads, see [Methods for getting an ID token](https://docs.cloud.google.com/docs/authentication/get-id-token#methods).

## What's next

  * [Pass data between build steps](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps)
  * [Deploy to Cloud Run](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run)
  * [Deploy to App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
