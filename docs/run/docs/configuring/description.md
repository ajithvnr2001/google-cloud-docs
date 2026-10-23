---
url: https://docs.cloud.google.com/run/docs/configuring/description/
title: Set service descriptions \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:15.047537+00:00
---

# Set service descriptions  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/description/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set service descriptions Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to set a custom description on your Cloud Run services. A description is an optional human-readable text attached to the service. A description is limited to 512 characters. If present, the description is displayed when [viewing details of a service using `gcloud run services describe`](https://docs.cloud.google.com/run/docs/managing/services#details).

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set or modify a description

You can set a description on Cloud Run services.

###  gcloud 

You can set or update the description during [deployment](https://docs.cloud.google.com/run/docs/deploying#service):
    
    
    gcloud run deploy SERVICE --description DESCRIPTION

Replace

  * SERVICE with name of your Cloud Run service
  * DESCRIPTION with the description of the service



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `run.googleapis.com/description` annotation:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           annotations:
             run.googleapis.com/description: "DESCRIPTION"
         spec:
           template:
             ...

Replace

     * SERVICE with the name of your Cloud Run service
     * DESCRIPTION with the description of the service
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-description"
      location = "us-central1"
    
    ** description = "This service has a custom description"**
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    
    }

Replace the description with your desired value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
