---
url: https://docs.cloud.google.com/cortex/docs/post-deployment-steps/
title: Post-deployment steps \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:57.572760+00:00
---

# Post-deployment steps  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/post-deployment-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Post-deployment steps

This page guides you through the post-deployment steps of Cortex Framework to execute your data pipelines and verify the results.

After deployment, all transformation templates and configurations are compiled and deployed to your target Dataform repository. However, to materialize the tables and views in BigQuery, you must first execute the Dataform pipeline actions.

## Execute the transformations in Dataform

By executing the pipeline, you initiate the logic to transform raw data into the relevant data foundation and data product layers, ready for immediate business use.

You can execute actions manually in the Google Cloud console for verification, or configure recurring schedules for production.

**Note:** If you would like to add custom code (such as `.sqlx` or `.js` files) directly inside your remote Dataform workspace in the Google Cloud console, you must place it in the `definitions/custom/` directory. Otherwise, any files outside of `definitions/custom/` that are not part of the build output will be deleted or overwritten during the next Cortex Framework deployment run (`cortex-deploy`).

### Manual execution for verification

To execute a manual verification run of the entire pipeline within your Dataform workspace, follow these steps:

  1. In the Google Cloud console, go to the [**Dataform**](https://console.cloud.google.com/bigquery/dataform) page.
  2. Confirm that you have selected the correct Google Cloud project from the project drop-down.
  3. Click the name of the repository created during deployment (e.g., `cortex`).
  4. Click the workspace name (e.g., `cortex`).
  5. Click **Start execution**.
  6. Click **Execute actions**.
  7. Select **All actions**. You can also choose key subsets of transformations by selecting specific tags or actions.
  8. Click **Start execution**.



### Verify execution success

To monitor progress and check whether the pipeline completed successfully, follow these steps:

  1. Click the **Executions** tab to view the execution history.
  2. Verify that the status is **Completed successfully**.
  3. Click the execution run link to inspect details of specific actions, compilation errors, or execution timings.



## Review data assets in BigQuery

After your Dataform pipeline executes successfully, verify the generated datasets and look at the materialized tables in BigQuery.

  1. Navigate to [**BigQuery**](https://console.cloud.google.com/bigquery) in the Google Cloud console.
  2. Locate the target datasets configured in your `config.yaml` file (e.g., the dataset identified by `datasetId` in the `data.targets` entry referenced by the module's `dataTargetId`). For example, in the template configurations, these may be: 
     * **Data foundation layer** : Look for the dataset matching your foundation target ID (configured as `cortex7_sap_data_foundation` by default).
     * **Data products layer** : Look for the dataset matching your product target ID (configured as `cortex7_data_products` by default).
  3. Preview the tables and run sample queries to verify that they are populated with the expected records.



## Next steps

Now that your data systems are operational, you can explore how to:

  * **Register your data products in Knowledge Catalog** : See the Knowledge Catalog integration] (/cortex/docs/knowledge-catalog) documentation to automate the registration process.
  * **Extend your data model** : See the [Extensibility guide](https://docs.cloud.google.com/cortex/docs/extensibility-guide) to customize schemas or instantiate new modules.
  * **Build new or customize data products** : See the [Agentic skills for data product building](https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building) documentation to get started.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
