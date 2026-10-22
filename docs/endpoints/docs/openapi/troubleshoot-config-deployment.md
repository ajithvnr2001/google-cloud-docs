---
url: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment/
title: Troubleshooting Cloud Endpoints configuration deployment \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:28.576655+00:00
---

# Troubleshooting Cloud Endpoints configuration deployment  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Troubleshooting Cloud Endpoints configuration deployment Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-config-deployment "View this page for the Cloud Endpoints gRPC docs")

This page describes how to troubleshoot errors that you might encounter when you deploy your Cloud Endpoints configuration. The error messages that you see contain information specific to your project. For example, you might see an error message that has your project ID in it. On this page you'll see placeholder values such as YOUR_PROJECT_ID.

After each step, run the `gcloud endpoints services deploy` command again to see if the error is resolved.

## Cannot convert to service config

`ERROR: unknown location: http: In path template '[PATH]': unexpected end of input '/'.'`

This error is displayed when one or more paths in your OpenAPI document includes a trailing slash (`/`) character. To fix this issue, remove the trailing slash from all paths. For example, the following snippet in an OpenAPI document results in this error: 
    
    
    paths:
      "/echo/":
        post:
          description: "Echo back a given message."
    

To fix this, remove the trailing slash from `/echo/`:
    
    
    paths:
      "/echo":
        post:
          description: "Echo back a given message."
    

## Not allowed to get project settings

`ERROR: (gcloud.endpoints.services.deploy) PERMISSION_DENIED:`  
`Not allowed to get project settings for project YOUR_PROJECT_ID `

  1. Authenticate with gcloud CLI again to confirm that you authenticated with an account that has permission to access the project displayed in the error message: 
         
         gcloud auth login

A new browser tab opens and you are prompted to choose an account.

  2. Confirm that the project ID displayed in the error message corresponds to the Google Cloud project that you intend to deploy the Endpoints configuration to: 
         
         gcloud projects list

  3. Confirm that gcloud CLI has the correct project ID set as the current project: 
         
         gcloud config set project YOUR_PROJECT_ID




## Caller does not have permission

`ERROR: (gcloud.endpoints.services.deploy) PERMISSION_DENIED:`  
`Caller does not have permission 'servicemanagement.services.create' on project YOUR_PROJECT_ID`

When you first deploy the Endpoints configuration, Service Management creates a managed service for your API. To create a managed service, at a minimum you must have the **Editor** role at the project level. After Service Management creates the managed service, the minimum required permissions to redeploy an Endpoints configuration is the **Service Config Editor** role (**roles/servicemanagement.configEditor**) on the service. For more information, see [Granting access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access). 

## Ownership for domain name cannot be verified

`ERROR: (gcloud.endpoints.services.deploy) PERMISSION_DENIED:`  
`Ownership for domain name YOUR_DOMAIN_NAME on project YOUR_PROJECT_ID cannot be verified`

  * If you have a custom domain (such as `example.com`) configured in the `host` field of your OpenAPI document, you must [verify the domain name](https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name) before you can deploy your OpenAPI document. 
  * If you are using the `cloud.goog` domain, confirm that the value for the `host` field is in the following format, and that the project ID is correct: 
        
        API_NAME.endpoints.YOUR_PROJECT_ID.cloud.goog

  * If you are using the `appspot.com` domain (supported for App Engine only), confirm that the `host` field is in the following format, and that the project ID is correct: 
        
        YOUR_PROJECT_ID.appspot.com




## Troubleshooting other errors

If you received an error not listed here, or if the information didn't solve your problem, run the `gcloud` command again with the flag to display debug information:
    
    
    gcloud --verbosity=debug endpoints services deploy openapi.yaml

## What's next

  * [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy)
  * [Overview of API access](https://docs.cloud.google.com/endpoints/docs/openapi/api-access-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
