---
url: https://docs.cloud.google.com/recaptcha/docs/manage-keys/
title: Edit or delete reCAPTCHA keys \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:53.315657+00:00
---

# Edit or delete reCAPTCHA keys  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/manage-keys/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Edit or delete reCAPTCHA keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to edit or delete reCAPTCHA keys (also known as _keys_).

## Before you begin

Ensure that you have the following Identity and Access Management role: reCAPTCHA Enterprise Admin (`roles/recaptchaenterprise.admin`).

The simplest way to edit or delete a reCAPTCHA key is through the Google Cloud console. Alternatively, you can use the reCAPTCHA Enterprise API or the Google Cloud CLI.

## Edit a reCAPTCHA key

You can edit only some attributes of a reCAPTCHA key. You cannot change the platform type of a reCAPTCHA key. For example, if a reCAPTCHA key was created for a website, you cannot change the platform type to Android or iOS.

**Note:** Changes to a reCAPTCHA key's settings or allowed domain list can take up to 30 minutes to take effect.

### Console

  1. In the Google Cloud console, go to the **reCAPTCHA** page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, and then select your project.

  3. Select the **Keys** tab.

The **Keys** tab has two views: **Table** and **Cards**. If your project has many reCAPTCHA keys, only the **Table** view is available.

  4. In the **reCAPTCHA keys** section, identify the reCAPTCHA key you want to edit.

  5. For the reCAPTCHA key, click more_vert  **View key actions** and then select edit **Edit key**.

  6. On the **Edit the reCAPTCHA key** page, edit the required fields, and click **Update key**.




### gcloud

To edit reCAPTCHA keys, use the [`gcloud recaptcha keys update`](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update) command.

### REST API

To edit reCAPTCHA keys, use the [`projects.keys.patch`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/patch) method.

## Delete a reCAPTCHA key

If you delete a reCAPTCHA key from an active integration of reCAPTCHA, the website or the mobile application can show errors to your users, and the reCAPTCHA API calls return errors.

After you delete reCAPTCHA keys, you cannot recover them.

### Console

  1. In the Google Cloud console, go to the **reCAPTCHA** page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

  3. Select the **Keys** tab.

The **Keys** tab has two views: **Table** and **Cards**. If your project has many reCAPTCHA keys, only the **Table** view is available.

  4. In the **reCAPTCHA keys** section, identify the reCAPTCHA key you want to delete.

  5. For the reCAPTCHA key, click more_vert  **View key actions** and then select delete **Delete key**.

  6. In the confirmation dialog, enter `DELETE` and click **Delete**.




### gcloud

To edit reCAPTCHA keys, use the [`gcloud recaptcha keys delete`](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/delete) command.

### REST API

To edit reCAPTCHA keys, use the [`projects.keys.delete`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/delete) method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
