---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/labels/
title: Configure labels for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:57.485570+00:00
---

# Configure labels for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure labels for jobs Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run labels are key-value pairs that are applied to Cloud Run jobs. This page shows how to set, modify, and delete labels on your Cloud Run jobs. 

Possible uses include:

  * Cost allocation and billing breakdowns.
  * Identify resources used by individual teams or cost centers.
  * Distinguish deployment environments (prod, staging, qa, or test).
  * Identify owners and state labels.
  * Filter logs in Logging.



## Labels usage rules

The following rule applies to the use of labels set on a Cloud Run job:

Only [valid Google Cloud labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) can be used on Cloud Run.

## Labels for billing data and logging

Cloud Billing and Cloud Logging only receive labels that are specified in the `spec.template.metadata.labels` attribute in YAML, or under `template` in Terraform. If you configure labels using the Google Cloud console or Google Cloud CLI, Cloud Run adds the labels to both `metadata.labels` and `spec.template.metadata.labels` attributes.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set or modify labels

You can use Google Cloud console, Google Cloud CLI, YAML, or Terraform to set a label on a Cloud Run job.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Check the checkbox at the left of the job you are setting the label on.

  3. Make sure the _Info Panel_ at the far right is toggled on (**Show Info Panel**).

  4. Click **Labels** to display the labels pane.

![Set label](https://docs.cloud.google.com/static/run/docs/images/labels.png)

  5. To edit an existing label key value, locate the label and change the _Value_.

  6. To set a new label on the service, click **Add Label** and supply the key and the value.

  7. Click **Save**




###  gcloud 

  1. To [set a label](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create) on a new job:
         
         gcloud run jobs create JOB_NAME --image IMAGE_URL --labels KEY=VALUE

Replace the following:

     * JOB_NAME with the name of your job.
     * KEY with the name of your label key.
     * VALUE with the value for the key.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  2. To set a label on an existing job:
         
         gcloud run jobs update JOB_NAME --labels KEY=VALUE

  3. To create more than one label, supply a comma delimited list of key/value pairs.
         
         gcloud run jobs update JOB_NAME --labels KEY1=VALUE1,KEY2=VALUE2 




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `labels` attributes in two places:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           labels:
             LABEL: VALUE
         spec:
           template:
             metadata:
               labels:
                 LABEL: VALUE

Replace the following:

     * LABEL with the name of the label.
     * VALUE with the chosen value.

You can also specify more configuration such as environment variables or memory limits.

Cloud Run only propagates labels set in the `spec.template.metadata.labels` attribute to Cloud Billing and Cloud Logging.

  3. Update the existing job configuration:
         
         gcloud run jobs replace job.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job"
          }
        }
        labels = {
        "LABEL":"VALUE"
        }
      }
      labels = {
        "LABEL":"VALUE"
      }
    }
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * LABEL: the name of the label.
  * VALUE: the chosen value.



Cloud Run only propagates labels set under `template` to Cloud Billing and Cloud Logging.

## List jobs by label

You can list jobs by label using a [Google Cloud CLI filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):
    
    
      gcloud run jobs list --filter metadata.labels.LABEL=VALUE
      

Replace the following:

  * LABEL: the name of the label
  * VALUE: the value to include in your filtered list



## Delete a label on a job

To clear all labels from a job: 
    
    
    gcloud run jobs update JOB --clear-labels

To delete specific labels from a service, supply a comma delimited list of keys: 
    
    
    gcloud run jobs update JOB --remove-labels LABEL

Replace the following:

  * JOB: the name of your Cloud Run job
  * LABEL: the name of your label



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
