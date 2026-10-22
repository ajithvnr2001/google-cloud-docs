---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/data-collection-forms/
title: Data collection forms \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:10.082264+00:00
---

# Data collection forms  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/data-collection-forms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Data collection forms Stay organized with collections  Save and categorize content based on your preferences. 

This feature lets you set up and manage forms for consumer data collection for mobile and web SDKs. CCAI Platform supports both customer-hosted HTML forms (browser forms) and portal-defined forms rendered by the SDKs (custom forms). Consumers can complete forms during an active chat session, and submitted form data can be routed to your CRM and to your external storage based on configuration.

Before enabling the feature, confirm your SDKs meets the requirements. See Before you begin for more details.

## Form types

This page explains how to set up a data collection form that an agent can send to an end-user during a chat.

CCAI Platform supports two different ways to present forms in Web and Mobile SDKs:

  * **Browser forms** : You host the HTML form on your own web server. CCAI Platform loads the form in an embedded browser view inside the SDK. This requires a valid Form external ID and Form preview URL that point to your hosted form. Browser Forms are supported in the Widget Web SDK only. They are not supported in the Headless SDK. If your Web channel uses Headless, use Custom Forms instead.

For more information, see Add a browser form.

  * **Custom forms** : You define the form (fields, layout, and options) directly in the CCAI Platform portal. CCAI Platform renders the form in the Web and Mobile SDKs—no customer-hosted form infrastructure is required. Form data can be sent to your CRM (as ticket comments) and possibly to external storage as well, depending on your configuration.

For more information, see Add a custom form.


**Note:** When an end-user is filling out a form, they are not considered active in the chat. Therefore, when configuring [timeout](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-timeout) or [auto-dismissal](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dismiss-inactive-chats) settings, you should take into consideration the time an end-user needs to fill out a form.

## Before you begin

To turn on forms, you need your company secret code for authentication.

To get your company secret code, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Company Key & Secret Code** pane. Your company secret code appears. You need this code when you turn on forms.




## Turn on forms

To turn on forms, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Forms**. If you don't see the **Settings** menu, click menu **Menu**. The **Forms** page appears.

  2. Click the **Enable Forms** toggle to the on position.

  3. For **Form Settings** , click **Configure**. The **Browser Form Settings** pane appears.

  4. In the **Secret** field, enter your company secret code, and then click **Save**.

  5. Click **Back** to return to the **Forms** page.




## Add a browser form

To add a browser form, follow these steps:

  1. Follow the steps in Turn on forms.

  2. On the **Forms** page, click **Add template**. The **Add Form Template** page appears.

  3. To configure form settings, do the following:

     1. For **Type** , select **Browser form**.

     2. For **Channel** , select the channel or channels that you want the form to be available in.

     3. For **Queue languages** , select the queue languages that you want the form to be available in. For example, if you select **Channel** = **Web chat** and **Queue languages** = **German** , the form is available to end-users using the web channel and a German language queue.

  4. To configure form details, do the following:

     1. In the **Form template name** field, enter an internal-facing form template name. Agents see the form template name when selecting a form in the chat adapter.

     2. In the **Form title** field, enter a title for the form. End-users see the form title on the contact card during a chat. For more information, see [End-user experience](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-data-collection-forms#end-user-experience).

     3. In the **Form subtitle (Optional)** field, optionally enter a subtitle for the form. End-users see the form subtitle on the contact card during a chat.

     4. In the **Form External ID** field, enter an identifier for the form on your form server.

     5. In the **Preview URL** field, enter a URL for the form preview that appears in the agent adapter. For the form preview, you can use the actual form or a generic form. If a form contains PII, Google recommends using a generic form preview to help the agent identify the correct form without viewing PII.

**Caution:** The form preview an agent sees can be the actual form, or a generic version. If a form contains PII, it is recommended to set up a generic form preview that will be used to help the agent identify the correct form without viewing PII.
     6. To add a form image, do the following:

        1. In the **Form image (Optional)** field, optionally enter an image.

        2. Crop the image, and then click **Crop**.

End-users see the form image on the contact card during a chat.

  5. Click **Save & Preview**. The **Template Preview** dialog appears.

  6. Do one of the following:

     * If the form doesn't appear as expected, click **Edit**. The **Edit Form Template** page appears again and you can change your edits.

     * If the form appears as expected, click **Done**.




## Add a custom form

To add a custom form, follow these steps:

  1. Follow the steps in Turn on forms.

  2. On the **Forms** page, click **Add template**. The **Add Form Template** page appears.

  3. To configure form settings, do the following:

     1. For **Type** , select **Custom form**.

     2. For **Category** , leave **Chat** selected.

     3. For **Channel** , select the **Web chat** checkbox.

     4. For **Queue languages** , select the queue languages that you want the form to be available in. For example, if you select **Channel** = **Web chat** and **Queue languages** = **German** , the form is available to end-users using the web channel and a German language queue.

     5. Optional: For **Data Storage** , select the **Include form submission data as a CRM ticket comment** checkbox to send form data to your CRM as a ticket comment.

  4. To configure form details, do the following:

     1. In the **Form template name** field, enter an internal-facing form template name. Agents see the form template name when selecting a form in the chat adapter.

     2. In the **Form title** field, enter a title for the form. End-users see the form title on the contact card during a chat. For more information, see [End-user experience](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-data-collection-forms#end-user-experience).

     3. In the **Form subtitle (Optional)** field, optionally enter a subtitle for the form. End-users see the form subtitle on the contact card during a chat.

     4. To add a form image, do the following:

        1. In the **Form image** field, enter an image.

        2. Crop the image, and then click **Crop**.

End-users see the form image on the contact card during a chat.

  5. In the **Form header** field, enter the text that appears at the beginning of your form.

  6. In the **Form footer (Optional)** field, optionally enter the text that appears at the end of your form.

  7. Click **Next**. The **Questions** section appears.

  8. To add a question to your form, do the following:

     1. Click **Add question**. The **Add Questions** page appears.

     2. In the **Question type** list, select the question type. The options that appear depend on the question type that you select.

     3. In the **Question text** field, enter your question.

     4. To configure the **Mandatory** toggle, do the following:

        * If you previously selected `Toggle button` in the **Question type** list: To require the end-user to turn on this toggle in the form before they can submit it, click the **Mandatory** toggle to the on position.

        * If you previously selected any value except `Toggle button` in the **Question type** list: To require the end-user to answer this question before they can submit the form, click the **Mandatory** toggle to the on position.

     5. Optional: To mask the text that an end-user enters into a text field, click the **Masking** toggle to the on position. The masking toggle appears only if you previously selected `Text Entry` in the **Question type** list.

     6. Optional: In the **Placeholder text** field, enter your placeholder text. This is not available for all question types.

     7. Optional: Add help text and a help image. This is not available for all question types.

     8. In the **Character Limit** field, enter a character limit for your text field. This is available only when **Question type** = `Text Entry`.

     9. In the **Input type** list, select a input type. Available only when **Question type** = `Text Entry`.

     10. Configure any remaining fields, and then click **Add**.

  9. To add another question, click **Add question** and configure another question for your form.

  10. Click **Save**.




## Configure custom forms for web and mobile

To enable agents to send forms using the Web and Mobile SDKs, you must explicitly assign these channels to your form templates by following these steps:

  1. Navigate to **Form templates** : Sign in to the Portal and navigate to the **Add / Edit form template** page.

  2. **Select category** : In Form Settings, choose Chat as the category. When Chat is selected, the channel checkboxes for Web chat and Mobile chat become available.

  3. **Enable channels** : Locate the channel selection checkboxes. Select **Web chat** to make this form available on the Web SDK. Select **Mobile chat** to make this form available on the Mobile SDK.

**Note:** These are unselected by default for both new and existing forms.
  4. **Design your form** :

     * **Questions** : Add `Text`, `List`, or `Toggle` question types.
     * **Help context** : Optionally add **Help text** or a **Help image** to specific questions to guide the consumer.
     * **Images** : If uploading a form image, ensure it fits the 8:3 aspect ratio. You can crop the image within the portal.
     * **CRM settings** : To send form answers to your CRM as a ticket comment, enable **Include form submission data as a CRM ticket comment** in the **Form Settings**.

When enabled, the system can add form activity to your CRM ticket comments (for example, when a form is sent and when it is successfully completed), and—if this option is enabled—append submitted field values to the completion comment.

**Note** : When a consumer submits a Custom Form and leaves a non-mandatory (optional) field empty, that field may appear as `"undefined"` in the CRM ticket comment and in the data payload sent to your CRM or external storage. If you want to avoid `"undefined"` values in your CRM, consider making fields mandatory or instructing consumers to enter a value.

**Example** :

If a form contains the following fields:

     * `Name` (mandatory)
     * `Email` (optional)
     * `Comments` (optional)

And the consumer submits the form without filling in Email or Comments, the CRM ticket comment may include:

     * `"Name": "John Doe"`
     * `"Email": "undefined"`
     * `"Comments": "undefined"`
  5. **Preview and save** : Click **Save & Preview** to verify the form layout matches the expected consumer experience.

     * The preview shown in the portal is an agent preview only and may not exactly match how the form appears in the SDK.
**Note:** If you use the `Toggle` question type, you must provide specific text for the **On** and **Off** states. If marked **Mandatory** , you must toggle it to **On** to submit the form.



## Configure form data storage

Configure CCAI Platform to store your form data in external storage.

### Set up external storage

Set up an external storage location where you can store your form data. For more information, see [External storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage).

You can configure the system to push data collected from custom forms directly to your external storage (for example, S3).

**Note:** External storage for custom forms can be enabled regardless of whether CRM is enabled.

### Configure your instance to send form data to external storage

To configure your instance to send form data to external storage, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **External Storage** pane, and then click the toggle to the on position.

  3. Select the **Custom Forms** checkbox. A default path to the form data files in your external storage location appears. You can edit the path.

  4. Click **Save**.




## Permissions

To ensure security, access to form data within external storage is controlled by a specific permission.

Without this permission, portal users cannot access custom form data in external storage even if they know the path or UUID.

### Configure permissions

Assign the **View** option to the relevant user roles (for example, **Admin** , **Manager Data**).

**Note:** Edit permissions are not available for form data.

To help protect end-user data, viewing form data in external storage is controlled by CCAI Platform user roles. Only the **Admin** , **Manager** , **Manager Admin** , **Manager Team** , and **Manager Data** default roles have permissions to view form data in external storage.

If the default roles don't meet your needs, you can add a [custom role](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions) that has permissions to view form data. You can configure custom role permissions in the **Add Role** dialog at **Settings > Users & Teams > Roles & Permissions > Add Roles**.

### Permission location

In the **Add Roles** dialog, the form data settings are at the following location:

  * **Section** : External storage

  * **Page** : Forms

  * **Feature** : Form data




## What's next

  * [Use data collection forms](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-data-collection-forms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
