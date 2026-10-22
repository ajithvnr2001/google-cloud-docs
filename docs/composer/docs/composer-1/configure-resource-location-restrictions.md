---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-resource-location-restrictions/
title: Configure resource location restrictions \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:29.581663+00:00
---

# Configure resource location restrictions  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-resource-location-restrictions/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure resource location restrictions Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/configure-resource-location-restrictions "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-resource-location-restrictions "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page shows how to configure [resource location restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) so that your data stored by Managed Airflow is kept within the locations you specify.

## How location restrictions work

Location restrictions for Managed Airflow are determined based on the organizational policy that is applied to the project where the Managed Airflow environment is created. This policy is assigned either within the project or is inherited from the organization.

With location restrictions enabled, it is not possible to create an environment in a region that is prohibited by the policy. If a region is listed in the Deny list, or is not listed in the Allow list, then you cannot create environments in this region.

To enable the creation of environments, the policy must allow the whole region and not a specific zone within this region. For example, the `europe-west3` region must be allowed by the policy in order to create Managed Airflow environments in this region.

Managed Airflow checks location restrictions at:

  * Environment creation.
  * Environment upgrade, if any additional resources are created during the operation.
  * Environment update, for older environments that do not enforce location restrictions on Managed Airflow dependencies.



In addition to checking the location restrictions, Managed Airflow does the following:

  * Stores user-customized Airflow images in regional Artifact Registry repositories. As an example, such images are created when you install custom PyPI images in your environment.
  * If the [`US` multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) is explicitly prohibited by the policy, Cloud Build use is disabled. In this case, user-customized Airflow images are built in your environment's cluster.



## Install a Python dependency to a private IP environment with resource location restrictions

If you set resource location restrictions for your project, then Cloud Build can't be used to install Python packages. As a consequence, direct access to repositories on the public internet is disabled.

To install Python dependencies in a Private IP environment when your location restrictions don't allow the [`US` multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr), use one of the following options:

  * Use a private [PyPI repository hosted in your VPC network](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-private-repo).

  * Use a [proxy server](https://pip.pypa.io/en/stable/user_guide/#using-a-proxy-server) in your VPC network to connect to a PyPI repository on the public internet. Specify the proxy address in the `/config/pip/pip.conf` file in the Cloud Storage bucket. 

  * If your security policy permits access to your VPC network from external IP addresses, you can configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview).

  * Store the Python dependencies in the `dags` folder in the Cloud Storage bucket, to [install them as local libraries](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-local). This might not be a good option if the dependency tree is large.




## Restrict locations for Managed Airflow logs

If your Managed Airflow logs contain sensitive data, you might want to redirect Managed Airflow logs to a regional Cloud Storage bucket. To do so, use a [log sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). After you redirect logs to a Cloud Storage bucket, your logs are not sent to Cloud Logging.

**Caution:** To get support from Cloud Customer Care, you might need to grant Google support engineers access to the Managed Airflow logs stored in Cloud Storage.

###  gcloud 

  1. Create a new Cloud Storage bucket.
         
         gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION
         

Replace:

     * `LOCATION` with the region where the environment is located.
     * `BUCKET_NAME` with the name of the bucket. For example, `composer-logs-us-central1-example-environment`.
  2. Create a new log sink.
         
         gcloud logging sinks create \
         composer-log-sink-ENVIRONMENT_NAME \
         storage.googleapis.com/BUCKET_NAME \
         --log-filter "resource.type=cloud_composer_environment AND \
         resource.labels.environment_name=ENVIRONMENT_NAME AND \
         resource.labels.location=LOCATION"
         

Replace:

     * `ENVIRONMENT_NAME` with the name of the environment.
     * `BUCKET_NAME` with the name of the bucket.
     * `LOCATION` with the region where the environment is located.
  3. The output of the previous command contains the service account number. Grant the **Storage Object Creator** role to this service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member="serviceAccount:SA_NUMBER@gcp-sa-logging.iam.gserviceaccount.com" \
         --role='roles/storage.objectCreator' \
         --condition=None
         

Replace:

     * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * `SA_NUMBER` with the service account number provided by the `gcloud logging sinks create` command on the previous step.
  4. Exclude the logs for your environment from Logging.

**Caution:** [Audit logs](https://docs.cloud.google.com/logging/docs/audit) cannot be excluded. They are always sent to the default storage.
         
         gcloud logging sinks update _Default \
         --add-exclusion name=ENVIRONMENT_NAME-exclusion,filter=\
         "resource.type=cloud_composer_environment AND \
         resource.labels.environment_name=ENVIRONMENT_NAME AND \
         resource.labels.location=LOCATION"
         

Replace:

     * `ENVIRONMENT_NAME` with the name of the environment.
     * `LOCATION` with the region where the environment is located.



## What's next

  * [Managed Airflow security overview](https://docs.cloud.google.com/composer/docs/composer-1/composer-security-overview)
  * [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
