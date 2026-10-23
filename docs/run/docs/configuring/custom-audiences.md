---
url: https://docs.cloud.google.com/run/docs/configuring/custom-audiences/
title: Set custom audiences for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:16.662601+00:00
---

# Set custom audiences for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/custom-audiences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set custom audiences for services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use custom audiences for authorization.

Clients that call an Identity and Access Management-protected Cloud Run service must provide a valid ID token that includes an audience (`aud`) claim matching the receiving service's `*.run.app` URL. For clients that don't know this URL, you can use a custom audience value.

## Understanding custom audiences

Cloud Run provides an Invoker (`roles/run.invoker`) role to support [access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access). IAM access control makes use of Google-signed ID tokens, which are packaged as [JSON Web Tokens (JWTs)](https://en.wikipedia.org/wiki/JSON_Web_Token). The contents of these tokens conform to an OIDC standard.

An audience field is encoded in the token to specify the intended target that can use the token. This limits the risk of a replay attack, where an intercepted token intended for use with one service is replayed against a different service.

By convention, the audience is the full URL of the target service. By default in Cloud Run, this is the Google-generated URL for a service ending in `run.app`.

However, a Cloud Run service might sit behind a URL other than the default-generated URL, such as in the following scenarios:

  * When using a [custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) to reach a service where the client is unaware of the Google-generated URL.
  * When deploying multiple services [behind a load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless) where a client can't anticipate which regional service a request reaches. Google-generated URLs for services are region-specific even if the service name is the same.



In these scenarios, you must configure a service to accept custom audience values that allow additional targets known by a client. The default Google-generated URL always remains as an accepted audience value.

## Set and update custom audiences

Setting custom audiences for Cloud Run is done at the service level and applies to all serving revisions, similar to IAM authorization membership.

You can set multiple custom audiences, as long as JSON-encoding of the audiences as a string list does not exceed 32,768 characters.

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

###  gcloud 

You can set custom audiences on a service by using the following command:
    
    
    gcloud run services update SERVICE --add-custom-audiences=AUDIENCE

Replace

  * SERVICE with the name of your Cloud Run service
  * AUDIENCE with a string for the custom audience you want to support, for example, `myservice` or `https://myservice.example.com`



You can remove all custom audiences from a service by using the following command:
    
    
    gcloud run services update SERVICE --clear-custom-audiences

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Set the `run.googleapis.com/custom-audiences` annotation on the Service metadata (**not** on the `template` metadata):
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           annotations:
             run.googleapis.com/custom-audiences: '["AUDIENCE"]'
         spec:
           template:
             ...

Replace

     * SERVICE with the name of your Cloud Run service
     * AUDIENCE with a string for the custom audience you want to support, for example, `myservice` or `https://myservice.example.com`

Note that the value of the attribute is a quoted JSON array of strings, requiring the use of both double and single quotes.

  3. Replace the service with its new configuration by using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      custom_audiences = ["AUDIENCE"]
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    }
    

Replace:

  * SERVICE with the name of your Cloud Run service.
  * REGION with the Google Cloud region. For example, `europe-west1`.
  * AUDIENCE with a string for the custom audience you want to support, for example, `myservice`.



## Verifying custom audiences

  1. Get an ID token for a service account which has IAM permission to invoke the service. Note the use of the custom audience AUDIENCE.
         
         export TOKEN=$(gcloud auth print-identity-token --impersonate-service-account SERVICE_ACCOUNT_EMAIL --audiences='AUDIENCE')

Replace:

     * SERVICE_ACCOUNT_EMAIL with the email of the service account. It ends with `.iam.gserviceaccount.com`.
     * AUDIENCE with the custom audience value that you set on the service.
  2. Call the endpoint of the service with that ID token
         
         curl -H "Authorization: Bearer ${TOKEN}" ENDPOINT

Replace ENDPOINT with the endpoint to reach your service, for example its custom domain or `.run.app` URL.

  3. Confirm that the request is authorized and you see the expected response of your service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
