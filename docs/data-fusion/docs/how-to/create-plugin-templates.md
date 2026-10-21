---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/create-plugin-templates/
title: Create plugin templates \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:27.646774+00:00
---

# Create plugin templates  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/create-plugin-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create plugin templates Stay organized with collections  Save and categorize content based on your preferences. 

In the Cloud Data Fusion Studio, you can create, edit, or delete _plugin templates_. The templates are versions of a plugin that you customize. They're reusable, contain preconfigured settings, and you can choose which properties to lock or leave open for editing. You can use the plugin template in your data pipeline as you would any other plugin.

## Create a plugin template

To create a plugin template, follow these steps:

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion Studio interface, click **Studio**.

  3. In the plugins list, hold the pointer over a plugin, such as the Cloud SQL for MySQL batch source plugin, and click more_vert **More** > **Create template**. The Create Template dialog appears.

  4. If you have multiple versions of the plugin deployed, in the **Choose version** field, select a plugin version for the template.

  5. In the **Template name** field, enter a name for the template.

  6. Configure other plugin properties, as needed.

  7. Optional: Lock any property to prevent editing.

  8. To save the template, click **Add**. The template plugin appears in the plugin list with a **T** next to it, indicating that it's a template.




## Edit a plugin template

You can change the plugin template's properties. The changes don't affect existing pipelines that were built with the template.

To edit a plugin template, follow these steps:

  1. In the Cloud Data Fusion Studio interface, click **Studio**.
  2. In the plugins list, hold the pointer over a plugin and click click more_vert**More** > **Edit template**.
  3. Edit the properties.
  4. Click **Save**.



The updated template appears in the plugin list and is ready to use in pipelines.

## Delete a plugin template

When you delete a plugin template, it's removed from the plugin list on the Studio page and cannot be used when you create new pipelines. Deleting a template doesn't affect existing pipelines that were built with the template.

To delete a plugin template, follow these steps:

  1. Go to the **Studio** page in the Cloud Data Fusion web interface.
  2. In the plugins list, hold the pointer over a plugin and click more_vert **More** > **Delete template**.



The plugin template is removed from the plugin list and is no longer available to use in pipelines.

## What's next

  * Learn more about [working with multiple versions of a plugin](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-multiple-plugin-versions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
