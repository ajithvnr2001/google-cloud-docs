---
url: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six/
title: Step 6: Execute deployment \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:20.979716+00:00
---

# Step 6: Execute deployment  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/deployment-step-six/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Step 6: Execute deployment 

This page describes the sixth step to deploy Cortex Framework Data Foundation, the core of Cortex Framework. In this step, you execute the deployment of Cortex Framework Data Foundation.

**Note:** The steps outlined in this page are specifically designed for deploying Cortex Framework Data Foundation from the [official GitHub repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation).

## Build process

After configuring the [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file as described in [Step 5: Configure deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five), follow these instructions to build your process.

  1. Run the following command to locate yourself in the cloned repository:
         
         cd cortex-data-foundation
         

  2. Run the build command with the target log bucket:
         
         gcloud builds submit \
          --substitutions=_GCS_BUCKET=LOGS_BUCKET_NAME,_BUILD_ACCOUNT='projects/SOURCE_PROJECT/serviceAccounts/CLOUD_BUILD_SA@SOURCE_PROJECT.iam.gserviceaccount.com'
         

Replace the following:

     * `LOGS_BUCKET_NAME` with the bucket name for logs storage. Cloud Build Service Account needs access to write them here.
     * `SOURCE_PROJECT` with the source project.
     * `CLOUD_BUILD_SA` with the cloud build service account ID created in deplyoment step 4.
  3. Follow the main build process from looking at the logs in the terminal or in the [Cloud Build console](https://console.cloud.google.com/cloud-build/), if you have enough permissions. See the following images for more reference.

![Logs progress](https://docs.cloud.google.com/cortex/docs/images/logs-progress-terminal.png)

**Figure 1**. Example of viewing logs progress in the terminal.

![Logs progress](https://docs.cloud.google.com/cortex/docs/images/logs-progress-console.png)

**Figure 2**. Example of viewing logs progress in the console.
  4. Track the child build steps triggered from the Cloud Build console or within the logs created from the steps. See the following images for more reference.

![Child build steps tracking](https://docs.cloud.google.com/cortex/docs/images/child-build-steps-console.png)

**Figure 3**. Example of tracking child build steps in the console.

![Child build steps tracking](https://docs.cloud.google.com/cortex/docs/images/child-build-steps-logs.png)

**Figure 4**. Example of tracking child build steps within the logs.
  5. Identify any issues with individual builds. Correct errors, if any. It's recommended to paste the generated SQL into BigQuery to identify and correct the errors. Most errors are related to fields that are selected, but not present in the replicated source. The BigQuery UI helps to identify and comment those out.

![Identifying issues](https://docs.cloud.google.com/cortex/docs/images/issues-individual-builds.png)

**Figure 5**. Example of identifying issues through Cloud Build logs.



## Move files to the Managed Service for Apache Airflow (Airflow) DAG bucket

If you opted to generate integration or CDC files and have an instance of Managed Airflow (Airflow), you can move them into their final bucket with the following command:
    
    
      gcloud storage -m cp -r  gs://OUTPUT_BUCKET/dags/ gs://COMPOSER_DAG_BUCKET/
      gcloud storage -m cp -r  gs://OUTPUT_BUCKET/data/ gs://COMPOSER_DAG_BUCKET/
    

Replace the following:

  * `OUTPUT_BUCKET` with the output bucket.
  * `COMPOSER_DAG_BUCKET` with the Managed Airflow (Airflow) DAG bucket.

**Note:** This step is only applicable if you have an instance of Airflow running, as Airflow is commonly used to manage and orchestrate data pipelines.

## Customize and prepare for upgrade

Many enterprise customers have specific customizations of their systems, such as additional documents in a flow or specific types of a record. These are specific to each customer and configured by functional analysts as the business needs arise.

Cortex utilizes `## CORTEX-CUSTOMER` tags in code to denote places where such customizations are likely required. Use the command `grep -R CORTEX-CUSTOMER` to check all `## CORTEX-CUSTOMER` comments that you should customize.

In addition to the `CORTEX-CUSTOMER` tags, you might need to further customize the following by committing all of these changes with a clear tag in the code to your own forked or cloned repository:

  * Adding business rules.
  * Adding other datasets and joining them with existing views or tables
  * Reusing the provided templates to call additional APIs.
  * Modifying deployment scripts.
  * Adapting some tables or landed APIs to include additional fields not included in the standard.



Adopt a CI/CD pipeline that works for your organization to keep these enhancements tested and your overall solution in a reliable and robust state. A pipeline can reuse the `cloudbuild.yaml` scripts to trigger end-to-end deployment periodically, or based on git operations depending on your repository of choice by [automating builds](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

Use the`config.json` file to define different sets of projects and datasets for development, staging, and production environments. Use automated testing with your own sample data to ensure the models always produce what you expect.

Tagging your own changes visibly in your fork or clone of a repository together with some deployment and testing automation helps [perform upgrades](https://docs.cloud.google.com/cortex/docs/v6/upgrade-recommendations).

## Support

If you encounter any issues or have feature requests related to these models or deployers, create an issue in the [Cortex Framework Data Foundation](https://github.com/GoogleCloudPlatform/cortex-data-foundation) repository. To assist with gathering the necessary information, execute `support.sh` from the cloned directory. This script guides you through a series of steps to help troubleshoot.

For any Cortex Framework requests or issues, go to the [support](https://docs.cloud.google.com/cortex/docs/v6/overview#support) section in the overview page.

## Looker Blocks and Dashboards

Take advantage of the available Looker Blocks and Dashboards. These are essentially reusable data models for common analytical patterns and data sources for Cortex Framework. For more information, see [Looker Blocks and Dashboards overview](https://docs.cloud.google.com/cortex/docs/v6/looker-block-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
