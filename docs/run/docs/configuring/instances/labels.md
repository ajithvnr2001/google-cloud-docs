---
url: https://docs.cloud.google.com/run/docs/configuring/instances/labels/
title: Configure labels for instancess \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:52:21.213620+00:00
---

# Configure labels for instancess  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure labels for instancess Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run labels are key-value pairs that are applied to Cloud Run instances. This page shows how to set, modify, and delete labels on your Cloud Run instances. Note that when you set a label on a Cloud Run instance, a new revision with this label is created for this instance; the label is not applied to older revisions.

Possible uses include:

  * Cost allocation and billing breakdowns.
  * Identify resources used by individual teams or cost centers.
  * Distinguish deployment environments (prod, staging, qa, or test).
  * Identify owners and state labels.
  * Filter logs in Logging.



## Labels usage rules

The following rule applies to the use of labels set on a Cloud Run instance:

Only [valid Google Cloud labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) can be used on Cloud Run.

## Labels for billing data and logging

Cloud Billing and Cloud Logging only receive labels that are specified in the `spec.template.metadata.labels` attribute in YAML, or under `template` in Terraform. If you configure labels using the Google Cloud CLI, Cloud Run adds the labels to both `metadata.labels` and `spec.template.metadata.labels` attributes.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set or modify labels

You can set or modify labels using the Google Cloud CLI:

###  gcloud 

You can update labels for an instance using the command:
    
    
    gcloud beta run instances update INSTANCE --update-labels KEY=VALUE

To update more than one label, supply a comma-delimited list of key and value pairs. Note that the `update-labels` command sets a new value for the label key if the label already exists, otherwise it creates a new label.

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * KEY: the name of your label key.
  * VALUE: the value for the key.



You can also set labels during [deployment](https://docs.cloud.google.com/run/docs/create-and-manage-instances):
    
    
    gcloud beta run instances deploy INSTANCE --image IMAGE --labels KEY=VALUE

To create more than one label during deployment, supply a comma-delimited list of key and value pairs.

### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
           labels:
             KEY: VALUE
             KEY2: VALUE2
             KEY3: VALUE3

Replace the following:

     * INSTANCE: the name of your Cloud Run instance.
     * KEY and VALUE: the key and value pairs for labels.

`metadata.labels` sets labels on the instance object, while `spec.template.metadata.labels` sets labels on the created revision. Cloud Run only propagates labels set on the revision to Cloud Billing and Cloud Logging.

  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




## List instances by label

You can list instances by label using a [Google Cloud CLI filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):
    
    
      gcloud beta run instances list --filter metadata.labels.LABEL=VALUE
      

Replace the following:

  * LABEL: the name of the label.
  * VALUE: the value to include in your filtered list.



## Delete a label on an instance

You can use the Google Cloud CLI to delete labels on an instance.

###  gcloud 

To clear all labels from an instance:
    
    
    gcloud beta run instances update INSTANCE --clear-labels

To delete specific labels from an instance, supply a comma-delimited list of keys:
    
    
    gcloud beta run instances update INSTANCE --remove-labels LABEL

Replace the following:

  * INSTANCE: the name of your Cloud Run instance.
  * LABEL: the name of your label.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
