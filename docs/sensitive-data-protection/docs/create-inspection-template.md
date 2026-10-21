---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/create-inspection-template/
title: Quickstart: Create a Sensitive Data Protection inspection template \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:58.966633+00:00
---

# Quickstart: Create a Sensitive Data Protection inspection template  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/create-inspection-template/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Sensitive Data Protection inspection template

This quickstart shows you how to create and use a Sensitive Data Protection inspection template in the Google Cloud console. [Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates) let you create and persist configuration information in Sensitive Data Protection.

To complete this quickstart, you need to have data that you can scan in Cloud Storage, BigQuery, or Firestore in Datastore mode (Datastore).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=dlp--quickstart-create-template-inspect)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Sensitive Data Protection API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)




## Create a template

In the following sections, you configure and create an inspection template.

### Define template

  1. In the Sensitive Data Protection section of the Google Cloud console, go to the **Create template** page.

[Go to Create template](https://console.cloud.google.com/security/sensitive-data-protection/create/template;source=7)

  2. On the **Create template** page, define the following options:

     * For **Template type** , use the default setting **Inspect (find sensitive data)**.

     * For **Template ID** , enter `quickstart-template`.

     * For **Display name** , enter `Quickstart template`.

     * For **Description** , leave the field empty.

     * For **Resource location** , use the default setting **Global (any region)**.

  3. Click **Continue**.




### Configure detection

You now configure the template to detect for an infoType such as credit card numbers.

  1. In the **Configure detection** section of the **Create template** page, do the following:

     * In the **InfoTypes** section, click **Manage infoTypes** , select the infoTypes that you want to scan for, and then click **Done**.

     * In the **Confidence threshold** section, select **Possible** from the **Likelihood** list.

The default value **Possible** is sufficient for most purposes. If you routinely get matches that are too broad when you use this template, move the slider up. If you get too few matches, move the slider down.

  2. To create the template, click **Create**.

The template's summary information page appears. To return to the main Sensitive Data Protection page, click arrow_back **Inspection template details**.




## Use the template

The following steps describe how to configure the template for use in a scan:

  1. In the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

  2. Follow the prompts to create an inspection job or job trigger (a recurring job). When you are prompted to configure the detection, select the template that you created.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the template

There are no costs associated with creating and storing templates. However, if you want to delete a template, follow these steps:

  1. In the Google Cloud console, go to the **Configuration** tab of Sensitive Data Protection.

[Go to Configuration](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration;source=7)

  2. Select the project that contains the inspection template that you want to delete.

  3. On the **Configuration** tab, click the **Templates** subtab. The Google Cloud console displays a list of all templates for the current project.

  4. In the **Actions** column for the template you want to delete, click the trigger actions menu (more_vert), click **Delete** , and then click **Confirm**.




## What's next

  * Learn more about [creating and scheduling Sensitive Data Protection inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers).

  * Learn more about [creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect).

  * Learn more about the [infoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

  * Learn more about how Sensitive Data Protection matches your content using the [likelihood value](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
