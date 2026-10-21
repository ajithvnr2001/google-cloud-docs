---
url: https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data/
title: Protect sensitive data in sources \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:12.445136+00:00
---

# Protect sensitive data in sources  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Protect sensitive data in sources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to apply Sensitive Data Protection content policies to Gemini Enterprise connectors and apps and to Gemini Notebook Enterprise notebooks.

## About Sensitive Data Protection in Gemini Enterprise

[Sensitive Data Protection content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy) are designed to inspect data for data violations or unwanted content and choose when to allow or block this content. This includes blocking confidential or inappropriate source material, such as preventing sensitive data from being shown to users and blocking file uploads to the assistant or Gemini Notebook Enterprise if they violate policy. This capability enhances the security and safety of your Gemini Enterprise apps by protecting against various risks and ensuring responsible AI practices.

### Sensitive Data Protection and Model Armor work together

Sensitive Data Protection and Model Armor work together in Gemini Enterprise to provide a layered security defense for your data. They protect different aspects of your AI interactions.

#### Sensitive Data Protection safeguards inbound data

For data connectors, Sensitive Data Protection prevents sensitive data from being ingested or indexed. Content policies can inspect various content types, including textual content (with OCR for images), image object detection, image safety, rich documents (like PDF, DOCx, PPTx, and XLSx) with embedded images, and metadata labels (Microsoft sensitivity labels and Google Workspace labels). Sensitive Data Protection focuses on ensuring only compliant information enters the system as the source.

For uploaded sources to the assistant and Gemini Notebook Enterprise, if content violates the content policy, the source is not uploaded.

#### Model Armor safeguards the serving path

Model Armor helps protect the user interaction in Gemini Enterprise by screening prompts before LLM processing and in model responses before delivery to the user. By screening prompts, Model Armor guards against prompt injection and malicious URLs. If a policy is violated, Gemini Enterprise blocks the request and displays an error message.

For more information about using Model Armor with Gemini Enterprise, see [Enable Model Armor](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor).

### Supported sources

Sensitive Data Protection content policies can inspect data in connectors, metadata labels, and file uploads.

#### Connectors

You can apply content policies to the following connectors:

  * **Third-party connectors:** Sensitive Data Protection supports both ingestion and federated third-party connectors. For a list of these connectors, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).

  * **Custom MCP servers:** Sensitive Data Protection supports content in custom Model Context Protocol (MCP) servers. For general information about custom MCP servers, see [Set up your custom MCP server data store](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server).

  * **Google Workspace connectors:**

    * [Google Calendar](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal)
    * [Google Chat](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat)
    * [Google Drive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive)
    * [Gmail](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail)



#### Metadata labels

Sensitive Data Protection supports two types of metadata labels for certain connectors and uploads:

  * **Microsoft sensitivity labels:** Also known as Purview Information Protection (MSIP) labels, Azure Information Protection (AIP) labels, and Microsoft Information Protection (MIP) labels, these are sensitivity labels applied to Microsoft 365 assets (such as Word, Excel, and Outlook). They embed metadata directly into the file or email header to denote sensitivity (for example, "Highly Confidential" or "Internal Only"). Sensitive Data Protection supports Microsoft sensitivity labels in connectors as follows:

    * **[Microsoft SharePoint](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint):** Labels on Office 365 files and PDFs. Microsoft sensitivity labels on other file types, such as SharePoint sites and pages, aren't supported.

    * **[Microsoft OneDrive](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive):** Labels on Office 365 files and PDFs.

    * **[Microsoft Outlook](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook):** Labels on email messages and calendar events.

    * **[Microsoft Teams](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams):** Labels on Office 365 files and PDFs.

    * **Direct uploads and non-Microsoft connectors:** Labels on Office 365 files and PDFs, if the files contain embedded labels.

  * **Google Workspace labels:** These labels are for data classification across Google Workspace. Administrators define custom schemas that users or automated systems can apply to Google Workspace items to classify them (for example, "Confidential" or "Internal"). Sensitive Data Protection supports Google Workspace labels for files in Google Workspace connectors and files uploaded to the Gemini Enterprise assistant from Google Drive.




#### File uploads

When you upload files from a local drive, Google Drive, or Microsoft OneDrive to the assistant or Gemini Notebook Enterprise, Sensitive Data Protection scans the files and blocks uploads that violate the content policy.

The following table lists the supported file types for scanning:

MIME type | Description  
---|---  
`application/pdf` | PDF  
`text/html` | HTML  
`text/plain` | Plain text  
`application/json` | JSON  
`application/vnd.openxmlformats-officedocument.wordprocessingml.document` | Microsoft Word (DOCX)  
`application/vnd.openxmlformats-officedocument.presentationml.presentation` | Microsoft PowerPoint (PPTX)  
`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` | Microsoft Excel (XLSX)  
`application/vnd.ms-excel.sheet.macroenabled.12` | Microsoft Excel Macro-Enabled Worksheet (XLSM)  
`application/xml` | XML  
`image/bmp` | BMP image  
`image/gif` | GIF image  
`image/jpeg` | JPEG image  
`image/png` | PNG image  
`image/tiff` | TIFF image  
`image/svg+xml` | SVG image  
`text/csv` | CSV (Comma-separated values)  
`text/tab-separated-values` | TSV (Tab-separated values)  
**Note:** Although you can upload video and audio files to the assistant, Sensitive Data Protection doesn't scan these file types.

### Supported editions of Gemini Enterprise

You can use Sensitive Data Protection with all Gemini Enterprise [editions](https://docs.cloud.google.com/gemini/enterprise/docs/editions) except the Gemini Enterprise Business edition.

There's no additional cost to use Sensitive Data Protection.

### Supported regions

Sensitive Data Protection supports the global, EU, and US multi-regions.

## Limitations

The following limitations apply to Sensitive Data Protection content policies in Gemini Enterprise:

  * Content policies don't apply to the older type of data store, such as data from Cloud Storage or BigQuery or websites. Only the connectors, which contain entity data, can be protected by content policies.

  * Although you can apply a content policy from one project to Gemini Enterprise in another project, the two projects must be in the same VPC Service Controls perimeter. For general information about VPC Service Controls for Gemini Enterprise, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).

  * Google Workspace labels and content scanning aren't supported for uploads to Gemini Notebook Enterprise notebooks.

  * Sensitive Data Protection has limits on file size support that can be different from Gemini Enterprise. For information about the maximum size of PDFs, Office 365 files, text files, and image files, see [Content policy limits](https://docs.cloud.google.com/sensitive-data-protection/limits#content-policy-limits). By default, content policies allow content in large files. However, you can configure policies to block content in large files.

  * For Microsoft connectors that contain encrypted files, because neither Gemini Enterprise nor Sensitive Data Protection can decrypt the files, the files aren't scanned for content violations. If users ask questions about the content, Gemini Enterprise can't answer because the content is encrypted. But, if users ask questions that can be answered from any unencrypted snippets and metadata, then Gemini Enterprise does provide those answers.




## Before you begin

Before you begin, make sure that you have completed the following prerequisites:

  * You have the required roles assigned to you and the Gemini Enterprise service account:

    * You need the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

    * The Gemini Enterprise service account needs the DLP User (`roles/dlp.user`) role.

For more information, see [Required roles](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies#required-roles) in _Create and manage content policies_ in the Sensitive Data Protection documentation set.

**Note:** To grant multiple IAM roles to a service account, see [Grant or revoke multiple IAM roles using the Google Cloud console](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#multiple-roles-console).
  * You have created a Gemini Enterprise app or have Gemini Notebook Enterprise configured. For more information, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) or [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm).




## Create a content policy

To prepare a Sensitive Data Protection content policy to apply to a Gemini Enterprise connector or app or to Gemini Notebook Enterprise, do the following:

  1. Create a content policy following the instructions in [Create and manage content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies) in the Sensitive Data Protection documentation.

Make sure to create the policy in the same region as the apps you want to apply it to.

  2. Make a note of the policy name. To add a policy to a connector, you need the full path, in the form `projects/PROJECT_ID/locations/LOCATION/contentPolicies/POLICY_ID`.




## Protect sensitive data in connectors with content policies

To block entity information being shown to users if the entity contains sensitive data, apply a Sensitive Data Protection content policy to the connector, follow the instructions in Apply a content policy to a Gemini Enterprise connector.

If you subsequently need to remove the content policy from the connector, see Remove the content policy from a connector.

### Apply a content policy to a Gemini Enterprise connector

Applying a Sensitive Data Protection content policy to a connector prevents Gemini Enterprise from returning entity data that contains sensitive content from the connector.

For certain types of connectors, applying the content policy can also block the return of entity data based on metadata labels.

**Note:** Applying a Sensitive Data Protection content policy can increase latency.

To apply a content policy to a connector, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page and then click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

  2. Click the name of the connector that you want to apply the policy to.

  3. In the **Content policy** field, enter the full name for the content policy resource.

After you enter the policy into the field, it is applied right away.

**Note:** If you don't have the full policy name, do the following: 
     1. Open the **Content policy** tooltip help_outline and click the link to navigate to the content policies list.
     2. If the policy is in a different project from your Gemini Enterprise connector, switch to that project.
     3. Click the **Resource name** for the policy and copy the policy's **Name** from the **Content Policy Details** page. Policy names typically look like this: `projects/my-project/locations/global/contentPolicies/123-abc`. 
  4. Optional: Test the content policy. If you have data in the connector that violates the policy, [ask the assistant to tell you about it](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat).

![chat assistant is unable to retrieve the information](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/chat-against-policy.png)




### Remove the content policy from a connector

To remove a policy from a connector, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page, and then click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

  2. Click the name of the connector that you want to remove the policy from.

  3. Delete the text in the **Content policy** field, and enter an empty field.

The policy is removed right away.




## Protect uploads to the assistant with content policies

To protect uploads to the assistant for a Gemini Enterprise app, follow the instructions in Apply a content policy to Gemini Enterprise assistant uploads.

If you subsequently need to remove a Sensitive Data Protection content policy from the assistant, see Remove the content policy from the assistant.

### Apply a content policy to the assistant uploads

Applying a Sensitive Data Protection content policy to the assistant causes Gemini Enterprise to scan and block files uploaded to the app (from a local device, Google Drive, or Microsoft OneDrive) if they contain content or metadata labels that violate the policy. If a user attempts to upload a file that violates the policy, the upload fails and the file is not added to the session.

**Note:** Applying a Sensitive Data Protection content policy can increase latency.

To apply a content policy to assistant uploads, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to apply the policy to.

  3. Click **Security**.

  4. In the **Sensitive Data Protection configuration** , under the **Assistant setting** , select a content policy from the menu.

If the content policy isn't in the menu, do one of the following:

     * Click **Switch project** to select a policy from a different project.

     * Click **Enter manually** to enter the path to the policy: `projects/PROJECT_ID/locations/LOCATION/contentPolicies/POLICY_ID`.

     * Click **Create new** to navigate to the **Create Content Policy** page.

Make sure to choose a policy in the same region as the app.

  5. Click **Save**.

  6. Optional: Test the policy:

     1. Create a file that contains a harmless violation of the policy. For example, if the content policy blocks US social security numbers, create a file that contains "999-00-0000".

     2. Attempt to upload the file to the app's chat. The upload should fail and the file should be blocked.




### Remove the content policy from the assistant

To remove the content policy from assistant uploads for an app, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app.

  3. Click **Security**.

  4. In the **Sensitive Data Protection configuration** , under the **Assistant setting** , click the drop-down arrow and select **Enter manually**.

  5. Delete the text in the **Resource Name** field so that the field is empty, and then click **Confirm**.

  6. Click **Save**.




## Protect uploads to Gemini Notebook Enterprise with a content policy

Applying a content policy to Gemini Notebook Enterprise prevents users from uploading source material that violates the policy.

Gemini Notebook Enterprise notebooks aren't associated with any particular app. To apply the content policy to all notebooks in a project, you apply it to any app in the project. Similarly, if you remove a content policy from any app in the project, none of the notebooks associated with the project are protected by the policy.

Procedures for adding or removing a Sensitive Data Protection content policy in Gemini Notebook Enterprise:

  * Apply a content policy to Gemini Notebook Enterprise

  * Remove the content policy from Gemini Notebook Enterprise




### Apply a content policy to Gemini Notebook Enterprise

Applying a content policy to Gemini Notebook Enterprise prevents users from uploading source material that violates the policy. Gemini Notebook Enterprise notebooks aren't associated with any particular app. To apply the content policy to all notebooks, you apply it to any app in the project.

**Note:** Applying a Sensitive Data Protection content policy can increase latency.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of any app in the region for which you want to protect notebooks.

  3. Click **Security**.

  4. In the **Sensitive Data Protection configuration** , under the **NotebookLM setting** , select a content policy from the menu.

If the content policy isn't in the menu, do one of the following:

     * Click **Switch project** to select a policy from a different project.

     * Click **Enter manually** to enter the path to the policy `projects/PROJECT_ID/locations/LOCATION/contentPolicies/POLICY_NAME`.

     * Click **Create new** to navigate to the **Create Content Policy** page and follow the instructions above.

However you specify the policy, make sure to choose a policy in the same region as the app.

  5. Click **Save**.

  6. Wait approximately 10 minutes for the content policy to propagate. Gemini Notebook Enterprise will then start using the specified policy to scan uploaded source documents.

  7. Optional: Test the content policy:

     1. Create a source document that contains a harmless violation of the policy. For example, if the content policy blocks US social security numbers, create a source file that says "Mickey Mouse's social security number is 999-00-0000".

     2. Upload the source document to a notebook. If the policy is in effect, the document appears as blocked in the source list.

![Unable to import this source. It violates policies](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/blocked-notebook-source.png)




### Remove the content policy from Gemini Notebook Enterprise

To remove the content policy from Gemini Notebook Enterprise so that uploaded source files won't be blocked based on content, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of any app in the region.

  3. Click **Security**.

  4. In the **Sensitive Data Protection configuration** , under the **NotebookLM setting** , click the drop-down arrow and select **Enter manually**.

  5. Select the text in the field and press delete so that the **Resource Name** field is empty, then click **Confirm**.

  6. Click **Save**.

  7. Wait approximately 10 minutes for the removal of the content policy to propagate. Gemini Notebook Enterprise will then stop scanning source files for all notebooks in that region and project.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
