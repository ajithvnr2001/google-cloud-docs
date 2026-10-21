---
url: https://docs.cloud.google.com/dataform/docs/authentication/
title: Authenticate to Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:41:53.854742+00:00
---

# Authenticate to Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Authenticate to Dataform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to authenticate to Dataform programmatically. How you authenticate to Dataform depends on the interface you use to access the API and the environment where your code is running. 

For more information about Google Cloud authentication, see the [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

## API access

Dataform supports programmatic access. You can access the API in the following ways: 

  * Client libraries
  * REST



### Client libraries

The [Dataform client libraries](https://docs.cloud.google.com/dataform/docs/reference/libraries) provide high-level language support for authenticating to Dataform programmatically. To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

### REST

You can authenticate to [the Dataform API](https://docs.cloud.google.com/dataform/reference/rest) by using your [gcloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate) or by using [ Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials). For more information about authentication for REST requests, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest). 

## Set up authentication for Dataform

How you set up authentication depends on the environment where your code is running. 

The following options for setting up authentication are the most commonly used. For more options and information about authentication, see [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

### For a local development environment

You can set up credentials for a local development environment in the following ways: 

  * User credentials for client libraries or third-party tools
  * User credentials for REST requests from the command line
  * Service account impersonation



#### Client libraries or third-party tools

Set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) in your local environment: 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




For more information about working with ADC in a local environment, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

#### REST requests from the command line

When you make a REST request from the command line, you can use your gcloud CLI credentials by including [`gcloud auth print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token) as part of the command that sends the request. 

The following example lists service accounts for the specified project. You can use the same pattern for any REST request. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID. 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts" | Select-Object -Expand Content

For more information about authenticating using REST and gRPC, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest). For information about the difference between your local ADC credentials and your gcloud CLI credentials, see [gcloud CLI authentication configuration and ADC configuration](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#gcloud-credentials). 

#### Service account impersonation

In most cases, you can use your user credentials to authenticate from a local development environment. If that is not feasible, or if you need to test the permissions assigned to a service account, you can use service account impersonation. You must have the `iam.serviceAccounts.getAccessToken` permission, which is included in the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role. 

You can set up the gcloud CLI to use service account impersonation by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config): 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For select languages, you can use service account impersonation to create a local ADC file for use by client libraries. This approach is supported only for the Go, Java, Node.js, and Python client libraries—it is not supported for the other languages. To set up a local ADC file with service account impersonation, use the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) with the [`gcloud auth application-default login` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login): 
    
    
    gcloud auth application-default login --impersonate-service-account=SERVICE_ACCT_EMAIL

For more information about service account impersonation, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). 

## Access control for Dataform

After you authenticate to Dataform, you must be authorized to access Google Cloud resources. Dataform uses Identity and Access Management (IAM) for authorization. 

For more information about the roles for Dataform, see [Access control with IAM](https://docs.cloud.google.com/dataform/docs/access-control). For more information about IAM and authorization, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 

## What's next

  * Learn about [Google Cloud authentication methods](https://docs.cloud.google.com/docs/authentication#auth-decision-tree). 
  * See a list of [authentication use cases](https://docs.cloud.google.com/docs/authentication/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
