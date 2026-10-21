---
url: https://docs.cloud.google.com/translate/docs/advanced/automl-upgrade/
title: Upgrade AutoML resources \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:05.596195+00:00
---

# Upgrade AutoML resources  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/automl-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade AutoML resources

If you have existing resources that were created by using the [deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) AutoML API, you can upgrade those resources to manage them through the Cloud Translation - Advanced API without any service interruptions or additional costs. During the upgrade, Cloud Translation copies your AutoML (legacy) resources, such as datasets and models, and creates new Cloud Translation (native) resources through the Cloud Translation API.

We recommend that you use Cloud Translation because future enhancements to datasets and customs models will apply only to Cloud Translation. Upgraded resources can take advantage of those future enhancements such as additional language pair support.

## Upgrade considerations

After upgrading, your native and legacy resources exist together but are managed by different APIs. To access and manage the upgraded resources, you must use the Cloud Translation API, not the [deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) AutoML API.

The native resources are identical to legacy resources except for their resource IDs. Cloud Translation doesn't make any changes to legacy resources. You can continue to work with your legacy resources as before.

You can choose to upgrade some or all of your resources. When you upgrade a dataset, any models that are associated with that dataset are also automatically upgraded. Only models without an underlying dataset (like in cases where the associated dataset was deleted) can be manually upgraded on their own.

### Differences between legacy and native resources

The following table outlines the differences between legacy and native resources.

Feature | Legacy | Native  
---|---|---  
Import data into datasets when using the API | Use CSV file to specify source file locations in Cloud Storage | Specify TMX and TSV files locations in Cloud Storage  
Export data | Supports exporting segment pairs from a dataset or data from the model evaluation, which includes the test set along with model predictions | Supports exporting segment pairs from a dataset only  
View data splits by source file | The Google Cloud console shows a list of source files that were used to populate a dataset and how the data was split for each file. You can also delete imported data by source file. | Not applicable, native datasets don't track source file information.  
Model evaluation | Supports running evaluations against a new test set or from an existing dataset | Supports running evaluations against a new test set only  
Cancel operations | Supports canceling dataset import and model creation operations | You cannot cancel long-running operations  
  
### Google Cloud console behavior post upgrade

If you upgrade at least one resource, the Google Cloud console switches to using the Cloud Translation API instead of the [deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) AutoML API. So, when you create new datasets in the Google Cloud console, you create native datasets by default. This change happens at the project level, so other users of your project also see this change.

When training new custom models, the Google Cloud console uses the Cloud Translation API.

### Cloud Translation API

To manage native resources through the Cloud Translation API, you need to update your code to call the correct APIs with the correct resource IDs. For example, if you have commands that call the [deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) AutoML API and reference legacy resource IDs, you need to update those commands to call the Cloud Translation API and reference the native resource IDs.

For more information about the Cloud Translation API, see the [projects.locations.datasets](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.datasets) and [projects.locations.models](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.models) resources.

## Upgrade resources

Use the Google Cloud console to upgrade existing AutoML resources to Cloud Translation resources.

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. Click **Datasets** to view your existing datasets.

  3. Click **Upgrade** to open the **Upgrade dataset** pane, which lists the datasets that you can upgrade.

When you upgrade a dataset, any model that's associated with that dataset is also automatically upgraded.

  4. Select the datasets to upgrade, and then click **Start upgrading**.

On the **Datasets** page, the Google Cloud console lists your upgraded and legacy datasets in separate tables.

  5. To manually upgrade models, in the navigation pane, click **Models** to view your existing models.

You can manually upgrade only models without an underlying dataset (like if the model's associated dataset was deleted).

  6. Click **Upgrade** to open the **Upgrade model** pane.

  7. Select the models to upgrade, and the click **Start upgrading**.

On the **Models** page, the Google Cloud console lists your upgraded and legacy models in separate tables.




After you upgrade your resources, consider making the following changes:

  * Update existing code to use the Cloud Translation API and newly created resources. For more information, see [Create and manage datasets](https://docs.cloud.google.com/translate/docs/advanced/automl-datasets) and [Create and manage models](https://docs.cloud.google.com/translate/docs/advanced/automl-models).
  * For translation predictions, use the Cloud Translation API instead of the [deprecated](https://docs.cloud.google.com/translate/automl/docs/deprecations) AutoML API. For more information, see [translating text with a custom model](https://docs.cloud.google.com/translate/docs/advanced/translating-text-v3).



## Delete legacy resources

After you have fully migrated to using the new resources and the Cloud Translation API, you can remove your legacy resources so that you only have a single set of resources to work with.

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. In the navigation pane, click **Datasets** to view legacy datasets.

  3. For each dataset in the **Legacy datasets** table, select more_vert **More > Delete** and then click **Confirm**.

  4. In the navigation pane, click **Models** to view legacy models.

  5. For each model in the **Legacy models** table, select more_vert **More > Delete** and then click **Confirm**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
