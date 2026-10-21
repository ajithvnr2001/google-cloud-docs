---
url: https://docs.cloud.google.com/composer/docs/composer-1/enable-composer-service/
title: Enable and disable the Managed Airflow service \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:56.166648+00:00
---

# Enable and disable the Managed Airflow service  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/enable-composer-service/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Enable and disable the Managed Airflow service Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/enable-composer-service "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how to enable and disable the Managed Service for Apache Airflow service in your Google Cloud project.

For information about services management on Google Cloud, see [Enabling and Disabling Services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

For a list of services required by Managed Airflow in VPC Service Controls configurations, see [Configure VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc).

## Services required by Managed Service for Apache Airflow

**Upcoming deprecation:** We're  phasing out the APIs that aren't required by Managed Airflow (Gen 3). 

This section describes services that are required by Managed Airflow (Legacy Gen 1). In some cases, organization or project administrators can restrict which Google services can be used in their projects.

The following services are required by Managed Airflow (Legacy Gen 1):

  * composer.googleapis.com
  * compute.googleapis.com
  * logging.googleapis.com
  * monitoring.googleapis.com
  * storage.googleapis.com
  * cloudresourcemanager.googleapis.com
  * servicedirectory.googleapis.com
  * pubsub.googleapis.com
  * sqladmin.googleapis.com
  * cloudkms.googleapis.com, if you are using Cloud KMS or CMEK keys
  * secretmanager.googleapis.com, if you are using Secret Manager as a secret backend

  * deploymentmanager.googleapis.com




Google services like Cloud DNS or IAM are already allowed by default in most projects.

## Enable the Managed Airflow service

This section describes how to enable the Managed Airflow service in your Google Cloud project.

### Before you enable the service

  * To enable the Managed Airflow service, you must have the correct [Identity and Access Management](https://docs.cloud.google.com/iam) permissions. To learn about the IAM requirements for Service Usage, see Service Usage page for [Access Control](https://docs.cloud.google.com/service-usage/docs/access-control).

  * Make sure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) in your project.




### Enable Cloud Composer API

###  Console 

Enable the Cloud Composer API:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=composer.googleapis.com)

###  gcloud 

Enable the `composer.googleapis.com` API:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable composer.googleapis.com

###  API 

Use the [`services.enable`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) method to enable the `composer.googleapis.com` API.

###  Terraform 

Use the [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service) resource to configure the `composer.googleapis.com` API.

**Important:** If you disable the BigQuery API, your Managed Airflow environment stops working. This happens because Google Kubernetes Engine depends on BigQuery and Managed Service for Apache Airflow inherits this dependency from the Kubernetes Engine API.

### Enable services required by your DAGs

In addition to services required by Managed Airflow, enable all services that your DAGs use, for example:

  * bigquery.googleapis.com
  * dataflow.googleapis.com
  * datacatalog.googleapis.com



You can find the *.googleapis.com names of the services in API pages linked from the [API Explorer page](https://developers.google.com/apis-explorer).

## Disable the Managed Airflow service

This section describes how to disable the Managed Airflow service in your Google Cloud project.

### Before you disable the service

**Warning:** You cannot recover environments in your project after you disable the Cloud Composer API. After the API is disabled, you still have access to data stored in your environment's buckets, but the environments themselves are no longer usable.

  * To disable the Managed Airflow service, you must have the correct [Identity and Access Management](https://docs.cloud.google.com/iam) permissions. To learn about the IAM requirements for Service Usage, see the Service Usage page for [Access Control](https://docs.cloud.google.com/service-usage/docs/access-control).

  * Make sure that all Managed Airflow environments in your project are deleted. Disabling the API irreversibly deletes tenant project parts of Managed Airflow environments, and these environments become unusable.

  * To avoid additional charges, complete the following steps for each environment before you disable the Cloud Composer API:

    1. Pause the DAGs.
    2. If required, export the environment's data, such as DAGs from the environment's bucket.
    3. [Delete your environment](https://docs.cloud.google.com/composer/docs/composer-1/delete-environments), including the resources that are not deleted automatically.



### Disable Cloud Composer API

To disable the Managed Airflow service:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Composer API** page.

[Go to Cloud Composer API](https://console.cloud.google.com/apis/library/composer.googleapis.com)

  2. Click **Manage**.

  3. Click **Disable API**.




###  gcloud 

Run the [`gcloud services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable) command:
    
    
    gcloud services disable composer.googleapis.com
    

###  API 

Use the [`services.disable`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable) method to disable the `composer.googleapis.com` API.

###  Terraform 

Remove the configuration for the `composer.googleapis.com` API. You usually use the [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service) resource to configure Google Cloud services.

## Deprecation of services that aren't required by Managed Airflow (Gen 3)

We're phasing out the APIs that aren't required by Managed Airflow (Gen 3).

The following API dependencies **aren't detached yet** and are scheduled to be detached from the Cloud Composer API in the future:

  * sqladmin.googleapis.com
  * pubsub.googleapis.com



The following APIs **became fully detachable**. Deactivating these APIs won't cause the deactivation of the Cloud Composer API:

**Caution:** Deactivating these APIs will cause Managed Airflow (Gen 2) and Managed Airflow (Legacy Gen 1) environments to **stop working and become non-recoverable**.

  * artifactregistry.googleapis.com
  * cloudbuild.googleapis.com
  * container.googleapis.com



All APIs listed as detached **are no longer enabled automatically** when you enable the Cloud Composer API. To create Managed Airflow (Gen 2) environments in new projects, [enable the group of detached APIs](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service#enable-gen-2-dependencies) in addition to the Cloud Composer API.

Existing Managed Airflow (Gen 3) and Managed Airflow (Gen 2) environments in projects where the Cloud Composer API is already enabled aren't affected by this change. You can do the following:

  * If your project has only Managed Airflow (Gen 3) environments, then you can manually disable the detached APIs.

  * If your project has Managed Airflow (Gen 2) environments, then we recommend keeping these APIs enabled because disabling them might lead to environment malfunction.

  * If you use automation scripts to provision Managed Airflow (Gen 2) environments, then make sure that the listed APIs are enabled in addition to the Cloud Composer API. You can enable them manually or [with a gcloud CLI command](https://docs.cloud.google.com/composer/docs/composer-2/enable-composer-service#enable-gen-2-dependencies).




## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
