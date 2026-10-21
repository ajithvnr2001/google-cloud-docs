---
url: https://docs.cloud.google.com/looker/docs/ci-content-validator/
title: Continuous Integration Content Validator \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:47.530840+00:00
---

# Continuous Integration Content Validator  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ci-content-validator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Continuous Integration Content Validator Stay organized with collections  Save and categorize content based on your preferences. 

The Continuous Integration (CI) Content Validator identifies dashboards and Looks that have errors. Often, these errors are caused by missing references to LookML fields. 

The CI Content Validator performs similar validation as the [standard Looker Content Validator](https://docs.cloud.google.com/looker/docs/content-validation), with some differences:

  * The CI Content Validator supports the following:

    * You can configure the CI Content Validator to run automatically on a [schedule](https://docs.cloud.google.com/looker/docs/ci-create-suite#schedule-trigger), automatically [when a Looker developer submits a pull request to your LookML repository](https://docs.cloud.google.com/looker/docs/ci-create-suite#pr-trigger), or manually when you [manually run a CI suite](https://docs.cloud.google.com/looker/docs/ci-run-suite#manual-run).
    * You can scope the CI Content Validator results to specific Looker content folders, or to specific models and Explores in your LookML project. By default, the results of the CI Content Validator are automatically scoped to your LookML project. The CI Content Validator scoping is post-processing: the validator runs on the entire Looker instance and then filters the results to the scoping you specified when you created the CI suite.
  * The standard Looker Content Validator supports the following:

    * You can run the Looker Content Validator [manually](https://docs.cloud.google.com/looker/docs/content-validation#running_the_content_validator) only.
    * You can scope the Looker Content Validator to specific Looker content folders, or to specific LookML projects. The Looker Content Validator scoping occurs before validation: the validator runs only on the folders and projects that you specified when you initiated content validation.
    * You can use the Looker Content Validator to [replace names for fields, views, Explores, and models](https://docs.cloud.google.com/looker/docs/content-validation#replacing_names_for_fields_views_explores_and_models), to [remove fields](https://docs.cloud.google.com/looker/docs/content-validation#removing_a_field_name), and to [delete Looks](https://docs.cloud.google.com/looker/docs/content-validation#deleting_looks).



See the Content Validator options section of this page for details on the options that you can configure when you [create or edit a CI suite](https://docs.cloud.google.com/looker/docs/ci-create-suite). For information on running the Content Validator, see the [Running Continuous Integration suites](https://docs.cloud.google.com/looker/docs/ci-run-suite) documentation page.

On the [run results page](https://docs.cloud.google.com/looker/docs/ci-view-results), the Content Validator provides the error message for each errored Look or dashboard, along with a link to the content:

![Continuous Integration results page showing Content Validator findings](https://docs.cloud.google.com/static/looker/docs/images/ci-content-results-2506.png)

## Content Validator options

You can specify several options when you [create a Continuous Integration suite](https://docs.cloud.google.com/looker/docs/ci-create-suite) to configure how the Content Validator runs. The options are described in the following sections of this page:

  * Explores to query
  * Explores to exclude
  * Folders to validate
  * Folders to exclude
  * Exclude content in personal folders
  * Incremental validation



### Explores to query

By default, the Content Validator runs content validation on all models and Explores in your LookML project.

You can use the **Explores to query** field to specify the Explore and models that you want to include in the content validation. 

You can specify Explores in the following format: `model_name/explore_name`

For example, to specify the Explores named `users` and `orders` in the `thelook.model.lkml` file, you would enter the following: `thelook/users, thelook/orders`

See the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator#explores-to-query) documentation page for more information about and examples of how to specify Explores and models in this field.

### Explores to exclude

By default, the Content Validator will run content validation on all models and Explores in your LookML project. 

You can use the **Explores to exclude** field to specify the Explore and models that you want to exclude from the content validation. 

You can specify Explores in the following format: `model_name/explore_name`

See the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator#explores-to-query) documentation page for more information about and examples of how to specify Explores and models in this field.

### Folders to validate

You can scope content validation to specific content folders on your Looker instance by specifying a folder ID or a comma-separated list of folder IDs.

To get the ID of a folder, [use the Looker main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu) to open the folder, and then get the folder ID from the browser URL. The folder ID is the last element of the URL. For example, in the following URL, the folder ID is `45`:

`https://myinstance.looker.com/folders/45`

**Note:** If you enter values in both **Folders to validate** and **Folders to exclude** in the same suite, the **Folders to exclude** field takes precedence for the specified folders and all subfolders.

### Folders to exclude

You can exclude specific content folders from content validation by specifying a folder ID or a comma-separated list of folder IDs in the **Folders to exclude** field.

**Note:** If you enter values in both **Folders to validate** and **Folders to exclude** in the same suite, the **Folders to exclude** field takes precedence for the specified folders and all subfolders.

### Exclude content in personal folders

If you want the Content Validator to validate only content in shared folders, enable the **Exclude content in personal folders** field. When the **Exclude content in personal folders** field is enabled, the Content Validator will ignore content in the personal folders on your Looker instance.

### Incremental validation

Incremental validation is a method of finding errors that are unique to a specific development branch, errors that don't already exist in production. Incremental validation helps developers find and fix the errors that they are responsible for without being distracted by existing errors in the project, and it can also make validation faster, especially for LookML projects that contain many Explores.

In the validator results, the Content Validator indicates each Explore that was skipped because it had no changes to its compiled SQL in the branch or commit that was being validated. See [Viewing results for incremental validation](https://docs.cloud.google.com/looker/docs/ci-view-results#viewing_results_for_incremental_validation) for an example of incremental validation results.

You can enable incremental validation for the Content Validator by selecting the **Only incremental errors** checkbox in the **Content Validator** section when you create or edit a Continuous Integration suite.

Note the following for incremental validation:

  * The incremental validation setting does not apply when the Content Validator is validating the production branch itself, such as with manual runs on the production branch. When validating the production branch, the Content Validator shows the full results validation.



## Limitations of content validation

If you delete a model or change its name, the Content Validator doesn't return these "dangling" content errors, because the model can no longer be associated with the project that is being tested.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
