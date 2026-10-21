---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-model-configuration-errors/
title: How to fix model configuration errors \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:10:49.274902+00:00
---

# How to fix model configuration errors  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-model-configuration-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to fix model configuration errors Stay organized with collections  Save and categorize content based on your preferences. 

One of the errors you may encounter when you [validate](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) your LookML is `Model <model_name> is not allowed to use connection <connection_name>`. 

This error means that you need to look at the LookML [project settings](https://docs.cloud.google.com/looker/docs/manage-projects#projects_with_only_a_configuration) and verify that the model has the necessary and correct permissions to reference the connections it needs. 

For example, the following error indicates that the model `lauren_ecommerce` is not allowed to use the **athena** connection: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-model-configuration-error-2210.png)

There are two ways to fix the error: 

  * Changing the connection referenced in the model file's [`connection` parameter](https://docs.cloud.google.com/looker/docs/reference/param-model-connection)
  * Editing the project's configuration settings to provide access to the connection 



This page provides instructions for editing the project's configuration settings. 

## Editing the model's configuration settings

To edit the model's configuration settings: 

  1. Expand the [validation error](https://docs.cloud.google.com/looker/docs/lookml-validation#lookml_errors) in the IDE. 
  2. Select the **Manage Projects** link in the error message. This will take you to the LookML Projects page. 

You can also navigate to the LookML Projects page by using the URL `https://<your_looker_domain.com>/projects`, or by selecting **Projects** from the **Develop** menu in the left navigation panel. 
  3. On the LookML Projects page, find the model that triggered the error. In this example, look for the `lauren_ecommerce` model for the **l_ecommerce** project. The model will be made more visible by a critical error in red: ![Manage Projects page with the lauren_ecommerce model highlighted.](https://docs.cloud.google.com/static/looker/docs/images/hc-model-configuration-lookml-project-error-2210.png)
  4. Select the **Configure** button to open the **Edit Model Configuration** page. 
  5. Review the connections currently selected for the model in the **Allowed Connections** section. In this example, the error states that `model 'lauren_ecommerce' is not allowed to use connection 'athena'.` The connection **athena** is not selected in the model's **Allowed Connections**. The `ecommerce_demo` connection was selected by mistake in this case: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-model-configuration-error-model-config-2318.png)
  6. Check the box next to the correct connection — in this case, **athena**. Alternatively, you can select the **All** option to grant the model access to all connections, including new connections added in the future. 
  7. Adjust other connection selections as needed. 
  8. Select **Save**. 
  9. Navigate back to your LookML model and re-validate to verify that the model configuration error is no longer there: ![LookML validation result in the IDE showing no LookML errors.](https://docs.cloud.google.com/static/looker/docs/images/hc-model-configuration-error-no-validation-error-2210.png)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
