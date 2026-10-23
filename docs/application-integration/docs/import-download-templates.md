---
url: https://docs.cloud.google.com/application-integration/docs/import-download-templates/
title: Import and download templates \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:44.388352+00:00
---

# Import and download templates  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/import-download-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Import and download templates

**Preview — templates**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can download your project templates as a JSON file and save it in your local system. As a result, your entire template is available in a file, which you can import in another integration project without any modifications. [Importing a project template](https://docs.cloud.google.com/application-integration/docs/import-download-templates#import-templates) creates a new template with the same configuration as the downloaded template file.

## Before you begin

  1. To get the permissions that you need to import and download templates, ask your administrator to grant you the Application Integration Editor (`roles/integrations.integrationEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Download templates

To download a template, do the following:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Templates**. 

The **Templates** page appears listing all the templates (global, shared, and project) available in your Google Cloud project.

  3. To download a global template, click the template that you want to download from the **Global templates** tab. 

To download a shared template, click the template that you want to download from the **Shared templates** tab.

To download a project template, click the template that you want to download from the **Project templates** tab.

  4. Click the template that you want to download from the respective tab selected.
  5. In the template details page, click download **Download template**. 

The TEMPLATE_NAME.json file is automatically saved in your web browser's default download folder.




## Import templates

To import a template, do the following:

  1. In the Google Cloud console, go to the **Templates** page. 

[Go to Templates](https://console.cloud.google.com/integrations/templates)

  2. Click **Import to project templates** , and select the template JSON file that you want to import from your local system. 

The **Upload template - Preview** page appears.

![Import template pane](https://docs.cloud.google.com/static/application-integration/images/import-template.png)![Import template pane](https://docs.cloud.google.com/static/application-integration/images/import-template.png)

  3. Review the rendered template details, and click **Upload**. 

The template is imported to your project and is available in the **Project templates** tab.




## What's next

  * Learn how to use templates to create an integration, see [Create integrations from templates](https://docs.cloud.google.com/application-integration/docs/create-integration-from-templates).
  * Learn how to create templates, see [create templates](https://docs.cloud.google.com/application-integration/docs/create-templates).
  * Learn how to share templates, see [share templates](https://docs.cloud.google.com/application-integration/docs/share-templates).
  * Learn how to manage templates, see [manage templates](https://docs.cloud.google.com/application-integration/docs/manage-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
