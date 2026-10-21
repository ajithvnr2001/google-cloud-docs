---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/labels/
title: Configure labels for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:52.599642+00:00
---

# Configure labels for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure labels for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run labels are key-value pairs that are applied to Cloud Run worker pools. This page shows how to set, modify, and delete labels on your Cloud Run worker pools. Note that when you set a label on a Cloud Run worker pool, a new revision with this label is created for this worker pool; the label is not applied to older revisions.

Possible uses include:

  * Cost allocation and billing breakdowns.
  * Identify resources used by individual teams or cost centers.
  * Distinguish deployment environments (prod, staging, qa, or test).
  * Identify owners and state labels.
  * Filter logs in Logging.



## Labels usage rules

The following rule applies to the use of labels set on a Cloud Run worker pool:

Only [valid Google Cloud labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) can be used on Cloud Run.

## Labels for billing data and logging

Cloud Billing and Cloud Logging only receive labels that are specified in the `spec.template.metadata.labels` attribute in YAML, or under `template` in Terraform. If you configure labels using the Google Cloud CLI, Cloud Run adds the labels to both `metadata.labels` and `spec.template.metadata.labels` attributes.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set or modify labels

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set or modify labels using the Google Cloud console, the Google Cloud CLI, or Terraform:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Locate the worker pool and select the checkbox to the left of its name.

  3. Click **Labels** to display the Labels pane.

![Set label](https://docs.cloud.google.com/static/run/docs/images/labels.png)

  4. To edit an existing label key value, locate the label and change the _Value_ as desired.

  5. To set a new label on the worker pool, click **Add Label** and supply the key and the value.

  6. Click **Save**




###  gcloud 

You can update labels for a worker pool using the command:
    
    
    gcloud run worker-pools update WORKER_POOL --update-labels KEY=VALUE

To update more than one label, supply a comma-delimited list of key and value pairs. Note that the `update-labels` command sets a new value for the label key if the label already exists, otherwise it creates a new label.

Replace the following:

  * WORKER_POOL: the name of your Cloud Run worker pool
  * KEY: the name of your label key
  * VALUE: the value for the key



You can also set labels during [deployment](https://docs.cloud.google.com/run/docs/deploy-worker-pools#worker-pool):
    
    
    gcloud run worker-pools deploy WORKER_POOL --image IMAGE --labels KEY=VALUE

To create more than one label during deployment, supply a comma-delimited list of key and value pairs.

### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           labels:
             KEY: VALUE
             KEY2: VALUE2
             KEY3: VALUE3

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool
     * KEY and VALUE: the key and value pairs for labels

`metadata.labels` sets labels on the worker pool object, while `spec.template.metadata.labels` sets labels on the created revision. Cloud Run only propagates labels set on the revision to Cloud Billing and Cloud Logging.

  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
        labels = {
          KEY : "VALUE"
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool
  * REGION: the Google Cloud region—for example, `europe-west1`
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * KEY: the name of your label key
  * VALUE: the value for the key



Adding the labels under `template` sets the revision labels. Cloud Run only propagates labels set on the revision to Cloud Logging and Cloud Billing. If you add the labels to a location other than under `template`, the label is set for the worker pool, not the revision.

## List worker pools by label

You can list worker pools by label using a [Google Cloud CLI filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):
    
    
      gcloud run worker-pools list --filter metadata.labels.LABEL=VALUE
      

Replace the following:

  * LABEL: the name of the label
  * VALUE: the value to include in your filtered list



## Delete a label on a worker pool

You can use the Google Cloud console or the Google Cloud CLI to delete labels on a worker pool.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Locate the worker pool and select the checkbox to the left of its name.

  3. Click **Labels** to display the Labels pane.

![Set label](https://docs.cloud.google.com/static/run/docs/images/labels.png)

  4. Locate the label you want to delete.

  5. To the right of the label's **Value** textbox, hover your cursor to display the trash icon, then click the trash icon.

  6. Click **Save**




###  gcloud 

To clear all labels from a worker pool:
    
    
    gcloud run worker-pools update WORKER_POOL --clear-labels

To delete specific labels from a worker pool, supply a comma-delimited list of keys:
    
    
    gcloud run worker-pools update WORKER_POOL --remove-labels LABEL

Replace the following:

  * WORKER_POOL: the name of your Cloud Run worker pool
  * LABEL: the name of your label



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
