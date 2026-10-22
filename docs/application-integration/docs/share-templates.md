---
url: https://docs.cloud.google.com/application-integration/docs/share-templates/
title: Share templates \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:23.410675+00:00
---

# Share templates  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/share-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Share templates

**Preview — templates**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can share templates that you create with other projects or organizations in the Google Cloud console. These templates are categorized as _shared templates_ and can be viewed in the **Shared templates** tab in the [Templates](https://console.cloud.google.com/integrations/templates) page. The following page describes how to share templates in Application Integration.

## Required role

To get the permissions that you need to share templates, ask your administrator to grant you the [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to share templates. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to share templates:

  * `integrations.templates.share`
  * `integrations.templates.unshare`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Share templates

To share an existing template, do the following:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Templates**. 

The **Templates** page appears listing all the templates (global, shared, and project) available in your Google Cloud project.

  3. To share a shared template, click the **Shared templates** tab. To share a project template, click the **Project templates** tab. 
  4. Click the template that you want to share from the respective tab selected.
  5. In the template details page, click group **Share**. 

The **Share template** pane appears displaying any existing projects or organizations that the template is shared with.

![share template pane](https://docs.cloud.google.com/static/application-integration/images/share-template-screen.png)![share template pane](https://docs.cloud.google.com/static/application-integration/images/share-template-screen.png)

  6. Under **Add projects or organizations** , perform one of the following actions: 
     * Click **Browse** and select the projects or organizations that you want to share the template with.
     * Alternatively, you can enter the organization ID (organizations/{org-id}) or the project ID (projects/{project-id}) in the text box. 
User can also alternatively add the organization or project. The format for adding organization is organizations/{org-id} & for project projects/{project-id} 
  7. Under **Add projects or organizations** , click **Browse**.
  8. Select the projects or organizations that you want to share the template with, and click **Select**.
  9. Click **Share**. 

The template is shared with the selected projects or organizations, and is automatically added to the **Shared templates** tab.




## What's next

  * Learn how to use templates to create an integration, see [Create integrations from templates](https://docs.cloud.google.com/application-integration/docs/create-integration-from-templates).
  * Learn how to import and download templates, see [import and download templates](https://docs.cloud.google.com/application-integration/docs/import-download-templates).
  * Learn how to create templates, see [create templates](https://docs.cloud.google.com/application-integration/docs/create-templates).
  * Learn how to manage templates, see [manage templates](https://docs.cloud.google.com/application-integration/docs/manage-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
