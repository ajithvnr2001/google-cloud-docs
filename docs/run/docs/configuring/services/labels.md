---
url: https://docs.cloud.google.com/run/docs/configuring/services/labels/
title: Configure labels for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:38.215744+00:00
---

# Configure labels for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure labels for services Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run labels are key-value pairs that are applied to Cloud Run service and revisions. This page shows how to set, modify, and delete labels on your Cloud Run service and revisions. Note that when you set a label on a Cloud Run service, a new revision with this label is created for this service; the label is not applied to older revisions.

Possible uses include:

  * Cost allocation and billing breakdowns.
  * Identify resources used by individual teams or cost centers.
  * Distinguish deployment environments (prod, staging, qa, or test).
  * Identify owners and state labels.
  * Filter logs in Logging.



## Labels usage rules

The following rule applies to the use of labels set on a Cloud Run service:

Only [valid Google Cloud labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) can be used on Cloud Run.

## Labels for billing data and logging

Cloud Billing and Cloud Logging only receive labels that are specified in the `spec.template.metadata.labels` attribute in YAML, or under `template` in Terraform. If you configure labels using the Google Cloud console or Google Cloud CLI, Cloud Run adds the labels to both `metadata.labels` and `spec.template.metadata.labels` attributes.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set or modify labels

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

Labels you previously set for your Cloud Run functions using either `gcloud functions` commands or the Cloud Functions v2 API propagate to Cloud Run when you [deploy your functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions).

You can set or modify labels using the Google Cloud console, the Google Cloud CLI, or a YAML file when you [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision).

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Check the checkbox at the left of the service you are setting the label on.

  3. Make sure the _Info Panel_ at the far right is toggled on (**Show Info Panel**).

  4. Click **Labels** to display the labels pane.

![Set label](https://docs.cloud.google.com/static/run/docs/images/labels.png)

  5. To edit an existing label key value, locate the label and change the _Value_.

  6. To set a new label on the service, click **Add Label** and supply the key and the value.

  7. Click **Save**




###  gcloud 

You can update labels for a service using the command:
    
    
    gcloud run services update SERVICE --update-labels KEY=VALUE

To update more than one label, supply a comma delimited list of key-value pairs. Note that the `update-labels` command sets a new value for the label key if the label already exists, otherwise it creates a new label.

Replace the following:

  * SERVICE: the name of your Cloud Run service
  * KEY: the name of your label key
  * VALUE: the value for the key



You can also set labels during [deployment](https://docs.cloud.google.com/run/docs/deploying#service):
    
    
    gcloud run deploy SERVICE --image IMAGE --labels KEY=VALUE

To create more than one label during deployment, supply a comma delimited list of key-value pairs.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `labels` attributes in two places:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           labels:
             LABEL: VALUE
         spec:
           template:
             metadata:
               labels:
                 LABEL: VALUE
               name: REVISION

Replace the following:

     * SERVICE: the name of your Cloud Run service
     * LABEL: the name of the label
     * VALUE: the required value
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters

`metadata.labels` sets labels on the service object, while `spec.template.metadata.labels` sets labels on the created revision. Cloud Run only propagates labels set on the revision to Cloud Logging and Cloud Billing.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-labels"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
    ** image = "us-docker.pkg.dev/cloudrun/container/hello"**
    **}**
    **# Labels**
    ** labels = {**
    ** foo : "bar"**
          baz : "quux"
        }
      }
    }

The preceding snippet adds two labels, `foo` (whose value is `bar`) and `baz` (whose value is `quux`), to your Cloud Run instance.

Adding the labels under `template` sets the labels for the revision: only labels set for the revision are passed to Cloud Logging and Cloud Billing. If you add the labels to a location other than under `template`, the label is set for the service not the revision.

Replace the following:

  * `name`: the name of your service.
  * `location`: the location used for your service.
  * `image`: your container image.
  * `foo` and `baz`: your own label names.
  * `bar` and `quux`: your own label values.



## List services by label

You can list services by label using a [Google Cloud CLI filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters):
    
    
      gcloud run services list --filter metadata.labels.LABEL=VALUE
      

Replace the following:

  * LABEL: the name of the label
  * VALUE: the value to include in your filtered list



## Delete a label on a service

You can use the console or the command line delete labels on a service.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Check the checkbox at the left of the service you are deleting the label from.

  3. Make sure the _Info Panel_ at the far right is toggled on (**Show Info Panel**).

  4. Click **Labels** to display the labels pane.

  5. Locate the label you want to delete.

  6. Hover your cursor to the right of the _Value_ textbox for the label to display the trash icon, and click the trash icon.

  7. Click **Save**.




###  gcloud 

To clear all labels from a service:
    
    
    gcloud run services update SERVICE --clear-labels

To delete specific labels from a service, supply a comma delimited list of keys:
    
    
    gcloud run services update SERVICE --remove-labels LABEL

Replace the following:

  * SERVICE: the name of your Cloud Run service
  * LABEL: the name of your label



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
