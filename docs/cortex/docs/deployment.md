---
url: https://docs.cloud.google.com/cortex/docs/deployment/
title: Deployment guide \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:33.230117+00:00
---

# Deployment guide  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deployment guide

This page guides you through the Cortex Framework deployment steps for production-path deployments.

## Before you begin

Ensure you have completed the prerequisites outlined on the [Prerequisites](https://docs.cloud.google.com/cortex/docs/prerequisites) page before continuing with the deployment.

Prior to deploying Cortex Framework, choose and prepare the [Source system integration](https://docs.cloud.google.com/cortex/docs/source-system-integration/overview). 

## Configure IAM roles

Configure the required Identity and Access Management (IAM) permissions to deploy Cortex Framework content within the required Google Cloud projects.

### Roles for build project

To get the permissions that you need to build Cortex Framework, ask your administrator to grant you the [BigQuery Data JobUser ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) IAM role on your build project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To grant the requested roles to a user, you can use the script:
    
    
          gcloud projects add-iam-policy-binding BUILD_PROJECT_ID \
            --member="user:USER_EMAIL" \
            --role="roles/bigquery.jobUser"
    

### Roles for source project

To get the permissions that you need to deploy Cortex Framework, ask your administrator to grant you the [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) IAM role on your source project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 
    
    
          gcloud projects add-iam-policy-binding SOURCE_PROJECT_ID \
            --member="user:USER_EMAIL" \
            --role="roles/bigquery.dataViewer"
    

### Roles for target projects

To get the permissions that you need to deploy Cortex Framework, ask your administrator to grant you the following IAM roles on your target projects: 

  * [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`)
  * [Dataform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.admin) (`roles/dataform.admin`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** 1) The Dataform Admin (`roles/dataform.admin`) privilege may be substituted with Dataform Editor (`roles/dataform.editor`) role, in case the Cortex Framework default Dataform repository `cortex-framework-demo` or repository specified using `--repository_name` [parameter](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build-and-deploy) has been created before the execution of the command `uv run cortex-demo`.

To grant the requested roles to a user, you can use the script:
    
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/bigquery.dataEditor"
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/dataform.admin"
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID --member="user:USER_EMAIL" \
            --role="roles/serviceusage.serviceUsageConsumer"
    

## Deployment Configuration

Before deployment, the data foundation and data product layers are configured through a centralized, configuration-as-code approach. Cortex Framework uses a `config/config.yaml` file to configure the Cortex Framework deployment. We recommend that you make a copy of `config/config.yaml.example` as a starting point. This file contains the essential mapping between your source data and the target Google Cloud environment. Proper configuration ensures that Cortex Framework knows exactly where to find your raw data and where to materialize the resulting layers.

For a successful Cortex Framework deployment, these mandatory values need to be added:

  * `YOUR_BUILD_PROJECT_ID`: The project where the deployment orchestration and `uv` scripts are executed.
  * `YOUR_SOURCE_PROJECT_ID`: The project containing your raw source data.
  * `YOUR_TARGET_PROJECT_ID`: The destination project where the processed data products and BigQuery datasets will reside.
  * `YOUR_REPO_PROJECT_ID`: The project hosting the Dataform repository and deployment artifacts.



For detailed information on the configuration file, see [Deployment configuration](https://docs.cloud.google.com/cortex/docs/deployment-configuration).

## Execute deployment

**Note:** Running the `uv run cortex-build-and-deploy` or `uv run cortex-deploy` commands collects anonymous telemetry data. For more information and instructions on how to opt out, see [Cortex Framework Telemetry](https://docs.cloud.google.com/cortex/docs/telemetry).

Run the following command to trigger the Cortex Framework deployment. This process will perform the following actions:

  * Verify that all prerequisites are complete.
  * Connect to the raw dataset, and based on the schema information, build and compile the `.sqlx` scripts.
  * Create the Dataform repository and workspace, then sync the compiled artefacts with the repository.


    
    
    uv run cortex-build-and-deploy --config config/config.yaml
    

**uv run cortex-build-and-deploy CLI parameters** : you can optionally display a list of possible parameters supported by the cortex-demo script by running the `uv run cortex-build-and-deploy -h` command. For more information, see [CLI Cortex Framework uv run cortex-build-and-deploy](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build-and-deploy).

**Note:** During the repository sync, `cortex-deploy` reconciles the remote Dataform workspace against your locally built artifacts. If you would like to add custom code (such as `.sqlx` or `.js` files) directly inside the remote Dataform workspace in the Google Cloud console, you must place it in `definitions/custom/`. Otherwise, any files outside `definitions/custom/` that are not part of the local build output will be deleted or overwritten during the next deployment run.

## Command line options

The `uv run` command line interface (CLI) support these actions:

  * `uv run cortex-build`: Executes compilation of the Dataform workspace, translating YAML configs and SQLX/JS templates into deployable Dataform assets. For more information, see [CLI Cortex build](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build).
  * `uv run cortex-deploy`: Pushes the compiled assets to the target Dataform workspace. For more information, see [CLI Cortex deploy](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-deploy).
  * `uv run cortex-build-and-deploy`: Combines the compilation and pushing of the build assets into Dataform workspace. For more information, see [CLI Cortex build and deploy](https://docs.cloud.google.com/cortex/docs/uv-run-cortex-build-and-deploy).



## Next steps

  * **Follow the[Post deployment steps](https://docs.cloud.google.com/cortex/docs/post-deployment-steps)** to execute the Dataform actions and verify the results in BigQuery

  * **Learn the[Knowledge catalog integration](https://docs.cloud.google.com/cortex/docs/knowledge-catalog)** to register, govern, and synchronize your enterprise data products across your organization.

  * **Create custom data products** : See the [Extensibility guide: Data product](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product) to create new data products or extend schemas.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
