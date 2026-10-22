---
url: https://docs.cloud.google.com/composer/docs/composer-1/delete-environments/
title: Delete Managed Airflow environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:49.870469+00:00
---

# Delete Managed Airflow environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/delete-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Delete Managed Airflow environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/delete-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how to delete your Managed Airflow environment.

## Resources that are not deleted automatically

Deleting your environment does not delete the following data in your project:

  * Your environment's Cloud Storage bucket.
  * Cloud Logging logs.



To avoid incurring charges to your Google Cloud account, export your data and [delete the environment's bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) and Cloud Logging logs, as needed.

If you use [alerting policies](https://docs.cloud.google.com/monitoring/alerts/manage-alerts) to monitor your environment's metrics, delete these policies before deleting your environment.

## Your environment's cluster is deleted automatically

**Warning:** Do not delete the GKE cluster of your environment manually. This happens automatically during the environment deletion. If you delete the cluster before the environment, then attempting to delete your environment results in an error. To fix this problem, see [Troubleshooting](https://docs.cloud.google.com/composer/docs/composer-1/known-issues#deleted-cluster).

## Delete a Managed Airflow environment

###  Console 

  1. Delete the Managed Airflow environment:

     1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     2. Select your environment and click **Delete**.

     3. Wait until the environment is deleted.

  2. Delete your environment's bucket. Managed Airflow does not delete the environment's bucket automatically.

**Warning:** Deleting your environment's bucket deletes all objects stored within the bucket, such as DAGs and plugins. You might not be able to recover these objects, depending on the [bucket's settings](https://docs.cloud.google.com/storage/docs/soft-delete) and the length of time since the bucket was deleted.
     1. In the Google Cloud console, go to the **Storage** > **Browser** page.

[Go to Storage > Browser](https://console.cloud.google.com/storage/browser)

     2. Select the environment's bucket and click **Delete**. For example, this bucket can be named `us-central1-example-environ-c1616fe8-bucket`.




###  gcloud 

  1. Delete the Managed Airflow environment:
         
         gcloud composer environments delete ENVIRONMENT_NAME \
             --location LOCATION
         

Replace:

     * `ENVIRONMENT_NAME` with the name of the environment.
     * `LOCATION` with the region where the environment is located.
  2. Delete your environment's bucket. Managed Airflow does not delete the environment's bucket automatically.

**Warning:** Deleting your environment's bucket deletes all objects stored within the bucket, such as DAGs and plugins. You might not be able to recover these objects, depending on the [bucket's settings](https://docs.cloud.google.com/storage/docs/soft-delete) and the length of time since the bucket was deleted.
         
         gcloud storage rm gs://BUCKET_NAME --recursive
         

Replace:

     * `BUCKET_NAME` with the name of your environment's bucket. For example, this bucket can be named `us-central1-example-environ-c1616fe8-bucket`.



###  API 

To delete an environment, construct an [`environments.delete`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/delete) API request with the environment ID.

**Caution:** Managed Airflow doesn't automatically delete the environment's bucket. If it's no longer needed, delete it manually.

###  Terraform 

To delete an environment using Terraform, remove the Managed Airflow configuration from your overall resource configuration and run `terraform apply`.

**Caution:** Managed Airflow does not automatically delete the environment's bucket. If it's no longer needed, delete it manually.

## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [Enable and disable Managed Airflow service](https://docs.cloud.google.com/composer/docs/composer-1/enable-composer-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
