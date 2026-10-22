---
url: https://docs.cloud.google.com/cortex/docs/v6/looker-block-deployment/
title: Deploy Looker Blocks \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:02.958650+00:00
---

# Deploy Looker Blocks  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/looker-block-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy Looker Blocks

This page describes the steps for installing a prebuilt Looker block for Cortex Framework located in a public GitHub repository, such as:

  * [SAP for Cortex](https://github.com/looker-open-source/block-cortex-sap)
  * [Salesforce Sales Cloud (SFDC) for Cortex](https://github.com/looker-open-source/block-cortex-salesforce)
  * [Oracle EBS for Cortex](https://github.com/looker-open-source/block-cortex-oracle-ebs)
  * [Salesforce Marketing Cloud (SFMC) for Cortex](https://github.com/looker-open-source/block-cortex-sfmc)
  * [Meta for Cortex](https://github.com/looker-open-source/block-cortex-meta)
  * [YouTube (with DV360) for Cortex](https://github.com/looker-open-source/block-cortex-youtube)
  * [Cross Media & Product Connected Insights for Cortex](https://github.com/looker-open-source/block-cortex-cross-media)



For deploying the Looker Dashboard for Dun & Bradstreet, see [Data Studio Dashboard for Dun & Bradstreet](https://docs.cloud.google.com/cortex/docs/v6/looker-dashboard-dun-and-bradstreet).

## Prerequisites

To access and use these pre built dashboards, you need to priorly do the following:

  1. **Deploy Cortex Framework** : Ensure you have Cortex Framework set up and configured with your data sources. For more information, see [Cortex Framework prerequisites for deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).
  2. **Access Looker:** Access Looker and get familiar with the platform.
  3. **Explore available dashboards** : Explore the prebuilt dashboards and the available insights in the dashboard you would like to deploy. For more information, see [Available Looker Blocks](https://docs.cloud.google.com/cortex/docs/v6/looker-block-overview).



After completing the prerequisites, you are ready to install your Looker Block.

## Installation

Looker Blocks use [LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) (Looker Modeling Language) to define the semantic model for the Looker dashboards. To install the LookML Model that corresponds to your Cortex data source, use one of the following options:

  * **Option A** : Install through Looker Marketplace from a Git URL.
  * **Option B** : Install by forking the repository.



The following sections describe the steps for each option.

### Option A: Install through Looker Marketplace from a Git URL

The [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) is a central location within Looker for finding, deploying, and managing Looker Blocks, applications, visualizations, and plug-ins. To install through Looker Marketplace from a Git URL, follow these steps:

  1. Go to your Looker instance.
  2. Click the **Marketplace** button on the Looker menu bar storefront.
  3. From the Marketplace menu, select the **Manage** option.
  4. On the **Manage** page, select the three-dot **Options** menu more_vert.
  5. Select **Install via Git URL** button. 
  6. Enter the URL and commit SHA of the chosen repository: 
     * [SAP for Cortex](https://github.com/looker-open-source/block-cortex-sap)
     * [Salesforce Sales Cloud (SFDC) for Cortex](https://github.com/looker-open-source/block-cortex-salesforce)
     * [Oracle EBS for Cortex](https://github.com/looker-open-source/block-cortex-oracle-ebs)
     * [Salesforce Marketing Cloud (SFMC) for Cortex](https://github.com/looker-open-source/block-cortex-sfmc)
     * [Meta for Cortex](https://github.com/looker-open-source/block-cortex-meta)
     * [YouTube (with DV360) for Cortex](https://github.com/looker-open-source/block-cortex-youtube)
     * [Cross Media & Product Connected Insights for Cortex](https://github.com/looker-open-source/block-cortex-cross-media)
  7. Click **Install**.
  8. Agree and Continue at the terms and conditions dialog.
  9. Enter the required parameters that corresponds to your data: 
     * Connection Name
     * Project ID
     * Reporting Dataset
  10. Click **Install**.



For more information, see the Looker documentation for [Installing a Tool from a Git URL.](https://docs.cloud.google.com/looker/docs/marketplace#installing_a_tool_from_a_git_url)

### Option B: Install by forking the repository

To install Looker blocks by forking the repository, follow these steps:

  1. **Fork the GitHub repository** :

     1. Navigate to the GitHub repository for the chosen Looker Block: 
        * [SAP for Cortex](https://github.com/looker-open-source/block-cortex-sap)
        * [Salesforce Sales Cloud (SFDC) for Cortex](https://github.com/looker-open-source/block-cortex-salesforce)
        * [Oracle EBS for Cortex](https://github.com/looker-open-source/block-cortex-oracle-ebs)
        * [Salesforce Marketing Cloud (SFMC) for Cortex](https://github.com/looker-open-source/block-cortex-sfmc)
        * [Meta for Cortex](https://github.com/looker-open-source/block-cortex-meta)
        * [YouTube (with DV360) for Cortex](https://github.com/looker-open-source/block-cortex-youtube)
        * [Cross Media & Product Connected Insights for Cortex](https://github.com/looker-open-source/block-cortex-cross-media)
     2. Click **Fork** in the top-right corner of the repository.
     3. Create a fork with your username. This creates a copy of the repository in your GitHub account.
  2. **Create a blank LookML project** :

**Note:** For Looker versions prior to 24.20, see [Creating a Blank Project](https://docs.cloud.google.com/looker/docs/create-projects#creating_a_blank_project) from the [New Project Page](https://docs.cloud.google.com/looker/docs/create-projects)-
     1. [Verify that you are in Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
     2. Select **Projects** from the **Develop** menu.
     3. From the top left of the **LookML Projects** page, select **Configure New Model** to open the **Configure a Model** page.

     4. On the **Configure a Model** page, specify the options for your model:

        1. **Model** : Name your model with the same name of the `model.lkml` file in the repository. For example, name the model `cortex-<datasource>`.

**Note:** Looker enforces unique model names. If a model with the intended name already exists, an error message will be displayed. Ensure model name uniqueness to avoid installation failures.
        2. **Project** : Name your project. Either name it the same as the model or specify a different name.

        3. **Allowed Connections:** Specify which database connections can be used by the model, or specify that the model is allowed to use any current or future connections.

     5. Click **Save** to save the project as a **Pending Project**.

     6. From the **LookML Projects** page, locate the new project under the **Pending Projects** section.

     7. Click **Add LookML** to open the **New Project** page.

     8. On the New Project page, specify the options for your project:

        1. **Project Name** : Already populated with value specified in prior step.
        2. **Starting Point** : Select **Blank Project**.
     9. Select **Create Project**. Looker creates the project and opens it in the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide).

For more information, see the original Looker documentation for [Generating a LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model).

  3. **Connect the new LookML project to the forked repository** : Follow the steps in the Looker documentation, [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection).

  4. **Update the values of constants in the`manifest.lkml` file**:

     1. Open the `manifest.lkml` file in your forked repository in Looker.
     2. Locate the constants section and update the values as described in the Required parameters section.
  5. **Commit and deploy changes to production**. With the Looker project based on your forked repository, you can customize the LookML to fit your unique business needs. Follow the steps in [Getting your changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production).




### Required parameters

These required values are configured during the Marketplace Installation process or if this Block was installed from a forked Git repository, you need to update the values for these constants in the `manifest.lkml` file for the project.

Parameter Value Description Looker Blocks   
`Connection Name` Name of the connection The BigQuery connection name allowing Looker to query the Cortex REPORTING dataset. must be enabled. All   
`Project ID` Project ID The Google Cloud project where the reporting dataset resides in BigQuery. For more information, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). All   
`Reporting Dataset` Name of the dataset for reporting The deployed Cortex Data Foundation REPORTING dataset where the data source dataset views reside within the Google Cloud BigQuery project. Depending on the deployment settings for the Cortex Data Foundation, this dataset name would typically be of the pattern ending with `_REPORTING`. All   
` Client ` SAP Client number (`mandt`) The SAP Client number (`mandt`) to use for Reporting. SAP   
` Sign Change ` `Yes` or `No` For Profit and Loss/Income Statement reporting, revenue is generally displayed in general ledger as a negative number, which indicates a credit. By setting Sign Change value to `Yes`, it's displayed as a positive number in income statement reports. SAP   
  
### Additional block-specific requirements

Some blocks have specific requirements for its deployment. For more information, see the block-specific deployment:

Block Link to Additional Requirements   
SAP [Additional specifications for Cortex Framework Looker Block for SAP](https://docs.cloud.google.com/cortex/docs/v6/looker-block-sap#additional_specifications_for_deployment).   
Oracle EBS [Additional specifications for Cortex Framework Looker Block for Oracle EBS](https://docs.cloud.google.com/cortex/docs/v6/looker-block-oracle-ebs#additional_specifications_for_deployment).   
  
## Extra Resources

For more information about LookML, see the following documentation and training:

  * [Looker Best Practices](https://docs.cloud.google.com/looker/docs/best-practices/home)
  * [Looker Google Cloud Training](https://www.cloudskillsboost.google/catalog?keywords=looker&locale=&skill-badge%5B%5D=any&format%5B%5D=any&language%5B%5D=any)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
