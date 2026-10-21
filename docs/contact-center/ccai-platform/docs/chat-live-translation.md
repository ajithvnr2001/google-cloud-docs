---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-live-translation/
title: Chat Live Translation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:36:57.689053+00:00
---

# Chat Live Translation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-live-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat Live Translation Stay organized with collections  Save and categorize content based on your preferences. 

Live translation provides real-time language translation between customers (end users) and agents. This enables agents to communicate with customers in their preferred language. Live translation is only available for chats with human agents.

Before you can set up live translation, you need to enable the Cloud Translation API, create a service account, grant the **cloudtranslate.admin** role to the service account, and create a service account key.

**Caution:** Follow Google's [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

## Enable the Cloud Translation API

To enable the Cloud Translation API for your Google Cloud project, follow these steps:

  1. Go to the Google Cloud console.

  2. Select your project.

  3. In the navigation menu, go to **API & Services > Library**.

  4. Search for **Cloud Translation API** and then click **Cloud Translation API**.

  5. Click **Enable**.




## Create a service account

To create a service account and grant the **cloudtranslate.admin** role to the service account, follow these steps:

  1. Go to the Google Cloud console.

  2. Select your project.

  3. In the navigation menu, go to **IAM & Admin > Service Accounts**.

  4. Click **Create service account**.

  5. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

  6. In the **Service account description** field, enter a description. For example, `Service account for Cloud Translation API`.

  7. Click **Create and continue**.

  8. Grant the **roles/cloudtranslate.admin** role to the service account.

To grant the role, in the **Role** box, search for and select **Cloud Translation API Admin**.

**Note:** The Role field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, don't grant the Owner, Editor, or Viewer roles. Instead, grant a predefined role or custom role that meets your needs.
  9. Click **Continue**.

  10. Click **Done** to finish creating the service account.

Don't close your browser window. You will use it in the next step.




## Create a service account key

To create a service account key, follow these steps:

  1. In the Google Cloud console, click the email address for the service account that you created.

  2. Click **Keys**.

  3. Click **Add key** , and then click **Create new key**.

  4. Click **Create**. A JSON key file is downloaded to your computer.

  5. Click **Close**.




## Create a translation platform

To use live translation, you need to create a translation platform and turn it on. This includes uploading and validating your service account keys.

To create a translation platform, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Developer Settings**.

  2. On the **Developer Settings** page, go to **Translation Platform**.

  3. Click **Add platform**.

  4. In the **Name** field, enter a name for your translation platform, and then click **Add**. The **Status** column displays **Invalid**.

  5. Click edit **Edit icon** to edit your translation platform.

  6. In the **Edit Translation Platform** dialog, click **Upload key**.

  7. Navigate to the key that you created in Create a service account key, and then click **Open**.

  8. Click **Save**.

  9. In the **Translation Platform** pane, click **Validate Keys**. The **Status** column should display **Valid**.

  10. In the row for your translation platform, click the toggle to the on position.




You can now turn on live translation globally.

## Turn on live translation globally

Before you can turn on live translation globally, you must create a translation platform.

Turning on live translation globally provides the ability to turn on live translation for your queues.

To turn on live translation globally, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. On the **Operation Management** page, go to **Live Translation**.

  3. Click the toggle to the on position.

  4. In the **Platform** field, select a translation platform.

  5. In the **Model** field, select a model from your translation platform, if available.

  6. In the **Glossaries** field, select a glossary from your translation platform, if available.

  7. Click **Save**.




### Turn on live translation for a queue

After you turn on live translation globally, you can turn on live translation for a queue.

To turn on live translation for a queue, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Queue**.

  2. In the **Web** pane, click **Edit/View**.

  3. Click the queue that you want to turn on live translation for.

  4. In the **Settings** pane, click the **Live Translation** toggle to the on position.




## Manage live translation

You can turn off live translation at the global and queue levels. You can edit existing translation platforms and delete them when you no longer need them.

### Turn off live translation globally

You can turn off live translation globally to immediately disable live translation for all queues.

To turn off live translation globally, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. On the **Operation Management** page, go to **Live Translation**.

  3. Click the toggle to the **Off** position.




### Edit a translation platform

You can edit an existing translation platform to make changes such as renaming the translation platform or uploading new service account keys.

To edit an existing translation platform, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Developer Settings**.

  2. On the **Developer Settings** page, go to **Translation Platform**.

  3. Click edit for the translation platform that you want to edit.

  4. Make your changes to the translation platform.

  5. Click **Save**.




### Delete a translation platform

You can delete translation platforms that you no longer need.

To delete a translation platform, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Developer Settings**.

  2. On the **Developer Settings** page, go to **Translation Platform**.

  3. Click close for the translation platform that you want to delete.

  4. In the **Delete translation platform** window, click **Delete**.




### Turn off live translation for a queue

To turn off live translation for a queue, follow these steps:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Queue**.

  2. In the **Web** pane, click **Edit/View**.

  3. Click the queue that you want to turn on live translation for.

  4. In the **Settings** pane, click the **Live Translation** toggle to the **Off** position.




## Chat translation storage

Translated messages are stored the chat transcript, either alongside or below the original messages. Messages are limited to 916 characters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
