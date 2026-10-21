---
url: https://docs.cloud.google.com/application-integration/docs/create-templates/
title: Create templates \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:00.158377+00:00
---

# Create templates  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/create-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create templates

**Preview — templates**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to create project templates in Application Integration. Project templates are project-level resources and are created and managed by the project owner. Only the project owner can create, modify, and delete these project templates.

## Required role

To get the permission that you need to create templates, ask your administrator to grant you the [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `integrations.templates.create` permission, which is required to create templates. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create project templates

You can create a project template from an integration or from a template import file.

### Create a template from an integration

To create a project template from an integration, do the following:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project.

  3. Select an existing integration or click **Create integration** to [create a new one](https://docs.cloud.google.com/application-integration/docs/create-integrations). 
     * If you are using an existing integration, review your existing integration to ensure that it's complete and ready to use as a template. Make any configuration changes as needed.
     * If you are creating a new integration, add and configure the required [tasks](https://docs.cloud.google.com/application-integration/docs/tasks), [triggers](https://docs.cloud.google.com/application-integration/docs/triggers), and [connectors](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) to build your integration template.
**Tip:** Use [Config variables](https://docs.cloud.google.com/application-integration/docs/variables#config_var) when configuring the input and output parameters of the components of your integration. This allows you to create a template that can be used in multiple environments.
  4. Once your integration is ready, click **Templates > Create a new template** from the integration editor [navigation bar](https://docs.cloud.google.com/application-integration/docs/integration-designer-layout#nav). 

The integration editor switches to template mode, temporaily locking any further actions on the integration, and the **Create Template** pane appears. 

![create template pane](https://docs.cloud.google.com/static/application-integration/images/create-template.png)![create template pane](https://docs.cloud.google.com/static/application-integration/images/create-template.png)

  5. Provide the following details in the **Create Template** pane: 
     1. **Template name:** Enter a name for the template.
     2. **Category:** Categories represent the business function of the template. Select one or more categories that apply to the template.
     3. **Description:** Optionally, enter a description for the template.
     4. **Tags:** Optionally, enter a comma-delimited list tags for the template. Tags are keywords that help you find and organize your templates.
     5. **How to use:** Optionally, enter a description of how to use the template. This description is displayed in the template details page.
  6. Click **Preview**. 

The **Preview Template details** pane appears showing the details of the template including the config variables that will be created.

  7. To create the template, click **Create Template**. 

A template based on the integration is created. To view the template, go to the **Templates** page and click the [Project Templates](https://console.cloud.google.com/integrations/templates) tab.




### Create a template from a template import file

To create a project template from a template import file, see [Import templates](https://docs.cloud.google.com/application-integration/docs/import-download-templates#import-templates).

## What's next

  * Learn how to use templates to create an integration, see [Create integrations from templates](https://docs.cloud.google.com/application-integration/docs/create-integration-from-templates).
  * Learn how to import and download templates, see [import and download templates](https://docs.cloud.google.com/application-integration/docs/import-download-templates).
  * Learn how to share templates, see [share templates](https://docs.cloud.google.com/application-integration/docs/share-templates).
  * Learn how to manage templates, see [manage templates](https://docs.cloud.google.com/application-integration/docs/manage-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
