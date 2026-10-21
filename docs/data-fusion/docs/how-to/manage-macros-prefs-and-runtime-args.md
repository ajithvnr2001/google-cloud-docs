---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args/
title: Manage macros, preferences, and runtime arguments \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:54:54.641940+00:00
---

# Manage macros, preferences, and runtime arguments  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage macros, preferences, and runtime arguments Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion macros, preferences, and runtime arguments let you dynamically parameterize pipelines and create reusable templates. You can establish hierarchical default settings across your environments and override configuration values when previewing or running a pipeline.

## Key terms

Macros
    Macros are placeholders within Cloud Data Fusion plugin configurations. They're represented by variables enclosed within `${ }`, such as `${input_file_path}`. Macros introduce flexibility into your pipelines by letting you use placeholder values, which are replaced with actual values at runtime. This enables dynamic configuration for parameters, such as file paths and table names.
Preferences
    Preferences are predefined configurations that apply at various levels within Cloud Data Fusion, including the system itself, namespaces, applications (which contain pipelines), and individual programs within pipelines. Preferences let you set default values for commonly used configurations. The defaults can be inherited by pipelines and programs at lower levels, reducing repetitive configuration tasks.
Runtime arguments
    Runtime arguments are key-value pairs that supply values for macros, and potentially override preferences, when you deploy or run a pipeline. They are highly customizable, letting you adjust configurations on a per-pipeline-run basis, without modifying the underlying pipeline or preferences.

## Set up macros

To use a macro for a plugin property value, follow these steps:

  1. In the Cloud Data Fusion Studio, go to the plugin node and click Properties.
  2. Go to the field where you want to use a macro and click the **M** next to the field.
  3. Enter a key for the macro. For example, in the File source's plugin properties, enter the following key in the Format field: `${format.type}`.

**Note:** The **M** that appears next to a plugin property field is a toggle that enables macros. Click it again to reset the default value of the plugin property.

### Set macro values

Set values for macros before you preview data for a pipeline and before you run a pipeline. You can set macro values in the following places:

  * Argument setter plugins
  * Runtime arguments
  * Application preferences
  * Namespace preferences
  * System preferences



Running a pipeline with macros does the following:

  * Cloud Data Fusion first checks if the pipeline includes an argument setter plugin: 
    * If it has an argument setter, Cloud Data Fusion uses the values for macros from it.
    * If there isn't an argument setter, or if there are macros that aren't assigned in the Argument Setter, Cloud Data Fusion instead uses the values in the pipeline runtime arguments.
  * Runtime arguments inherit macros from Application preferences.
  * Application preferences inherit macros from Namespace preferences
  * Namespace preferences inherit macros from System preferences.



**Examples**

A common use of macros is in path fields. Instead of using hard coded paths, you can use dynamic paths. For example, in a Cloud Storage source plugin, you can replace the path value with multiple macros. The following value divides the bucket, folder, and file elements: `gs://${bucket.name}/${folder}/${file.name}`.

The following example loads data from a bucket that's static and a file with a name that isn't static, enter the name of the bucket and use a macro for the filename: `gs://<BUCKET_NAME>/${folder}/${file.name}`.

For more information, see [Macros and macro functions](https://docs.cloud.google.com/data-fusion/docs/concepts/macros).

## Set up preferences

The following section describes the preference hierarchy, where preferences are set, inherited, or overridden.

### Set system preferences

You can set preferences for the system. Because macro names must be unique, each preference applies to all pipelines that use that macro.

For example, you have a pipeline with a Database source and use macros for the database name and username. You can set database and username preferences in system preferences. Every namespace and every pipeline in that instance inherits those preferences.

To set System preferences, follow these steps:

  1. In the Cloud Data Fusion Studio, click **System admin > Configuration**.
  2. Click expand_more **System preferences** > **Edit system preferences**.
  3. In the **Preferences** dialog, enter new preferences or edit existing preferences.
  4. Click **Save & Close**. These preferences are available in all namespaces, applications, and pipelines.



### Set namespace preferences

You can set preferences for individual namespaces.

When you set namespace preferences, any inherited system preferences display. When you set preferences for a namespace, you can override inherited preferences by setting different values. You can also add new namespace preferences.

To set namespace preferences, follow these steps:

  1. In the Cloud Data Fusion Studio, click **System admin** > **Configuration**.
  2. Click expand_more **Namespaces** and select a namespace to open its configurations page.
  3. To edit the inherited preferences or add new preferences, go to the **Preferences tab** and click **Edit**. A **Preferences** dialog opens where you can enter a new preference, or override inherited system preferences. Click add **Add** and enter the key and new value for the macro.
  4. Click **Save & Close**. Namespace preference is created with the new value, which takes precedence over the system preference.



### Set application preferences

You can set preferences for each deployed pipeline in a namespace. When you set application preferences, any inherited system and namespace preferences appear. When you set preferences for an application, you can override inherited preferences by setting different values, or add new preferences for the application:

  1. In the Cloud Data Fusion Studio, click menu and click the **Namespace** menu to select the namespace where you want to add application preferences.
  2. Click **Control center**.
  3. Click the **Set preferences** wrench icon. A list of all inherited preferences appears.
  4. To edit the inherited preferences or add new preferences, go to the **Preferences tab** and click **Edit**. A **Preferences** dialog opens where you can enter a new preference, or override inherited system preferences. Click add **Add** and enter the key and new value for the macro.
  5. Click **Save & Close**. The application preference is created with the new value, which overrides the system or namespace preferences. When you run the deployed pipeline, the application preferences appear as runtime arguments, which you can optionally edit.



## Set up runtime arguments

Set up runtime arguments to provide values for macros, and potentially override preferences, when you deploy or run a pipeline.

### Runtime arguments for previewing data

To set the values for each macro in the pipeline when you preview data in the Cloud Data Fusion Studio, click **List > Configure**.

### Runtime arguments for running deployed pipelines

If a pipeline includes macros, after you deploy a pipeline, you add runtime arguments, which set the values for the macros.

When you deploy a pipeline with macros, click arrow_drop_down drop-down menu next to **Run** to open the **Runtime arguments** dialog and set the values for each macro.

## Set pipeline preferences

To set preferences for a pipeline, follow these steps:

  1. In the Cloud Data Fusion Studio, click **List > Deployed**, and select a deployed pipeline to view it.
  2. From the Pipeline canvas, click arrow_drop_down drop-down menu next to **Run**. The **Runtime arguments** dialog opens.
  3. In the **Runtime arguments** dialog that opens, specify the value for each macro in the pipeline.



## Overview of preferences, macros, and runtime arguments

You can set up preferences at following levels:

  * **System preferences** : the highest level where you set preferences, such as defaults, for the entire instance.
  * **Namespace preferences** : inherits preferences from **System preferences**. You can set preferences for a specific namespace.
  * **Application preferences** : inherits preferences from **Namespace preferences**. They can be unique to individual applications (containing pipelines).
  * **Runtime arguments** : key-value pairs that override preferences at higher levels.



If you set a preference at the system preferences level, the macro values automatically populate in the namespace preferences, application preferences, and runtime arguments.

If you set preferences at the namespace level, they appear in the list of inherited preferences in the application's preferences. If a pipeline uses a macro that's defined in a preference, the runtime arguments use the key-value pair defined in the preference. You can override the values for preferences at each preference level and in runtime arguments.

Use preferences, macros, and runtime arguments for the following use cases:

  * **Developing a pipeline**. Embed macros where you need dynamic values for plugin properties.
  * **Optional: setting preferences**. Set default values for the macros in preferences at various levels.
  * **Deploying and running a pipeline**. When you run a pipeline, the following happens: 
    * Preferences for the relevant level, such as system preferences or namespace preferences, are applied.
    * Any runtime arguments you provide override the values that are assigned to the macros in the preferences.
    * Cloud Data Fusion resolves the macros by substituting their values from the runtime arguments (or preferences if a runtime argument is not provided).



**Example**

A pipeline has a BigQuery sink that has a table name value that must change dynamically. To set this up, you do the following:

  1. **Set the macro.** In the sink's properties, use the following macro in the **Table name** field: `${output_table}.`
  2. **Set the preference.** In the application preferences, set a preference for `${output_table}` with the following default value: `data_staging`.
  3. **Set the runtime argument.** When running the pipeline, provide a runtime argument—for example, `output_table=final_analytics_data`.



During pipeline execution, the macro, `${output_table},` is replaced with `final_analytics_data`.

# What's next

  * [Orchestrate pipelines](https://docs.cloud.google.com/data-fusion/docs/concepts/orchestrate-pipelines)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
