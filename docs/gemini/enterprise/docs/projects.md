---
url: https://docs.cloud.google.com/gemini/enterprise/docs/projects/
title: Create and manage projects \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:03.002223+00:00
---

# Create and manage projects  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/projects/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Create and manage projects Stay organized with collections  Save and categorize content based on your preferences. 

In Gemini Enterprise, you can use projects to build a dedicated knowledge base for your own work or to collaborate with your team. Within a project, you can upload documents and chat privately with the assistant to get answers grounded in your project documents and web search.

Project knowledge documents can include:

  * **Uploaded files** : Local files in the following formats are supported: PDF, Microsoft Word (DOCX), Microsoft PowerPoint (PPTX), Microsoft Excel (XLSX), CSV, HTML, and plain text (TXT).
  * **Google Drive files** : Google Docs, Google Slides, PDFs, or other supported file types linked directly from Google Drive.
  * **Notes** : Text notes pasted or typed directly into the project.
  * **External data connectors** : Files from third-party sources, such as Microsoft SharePoint, if enabled by your administrator.



## Before you begin

  * Ensure that a Gemini Enterprise administrator has turned on the **Enable projects** toggle in the web app feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).
  * If you want to link Microsoft SharePoint files to your projects, ensure that a Gemini Enterprise administrator has configured the SharePoint connector data store in the Google Cloud console. For instructions, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source).



## Limitations

The following limitations apply when adding documents to your project's knowledge base:

  * A project can include up to 50 files and linked documents in its knowledge base.
  * Linking Google Drive files or folders, or files from data connectors to a project doesn't change their original sharing permissions. To allow other project members to use these files, you must share them in the source application (such as Google Drive or SharePoint). Project members must have at least view access to the files.
  * When viewing the **Knowledge** tab, members only see the files and documents that they have permission to access. Members cannot view the names of files they don't have access to, and Gemini Enterprise only uses accessible files when generating answers for their chats.
  * Unlike files linked from Google Drive or external connectors, all locally uploaded files are visible, downloadable, and can be deleted by all project members.



## Create a project

To create a project in the Gemini Enterprise web app:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Projects**.
  3. Click add**New project** (or **Get started** if this is your first project).
  4. Enter a name for your project and click arrow_forward.
  5. In the **Welcome** tab, enter a description, and then click **Done**.



## Manage project knowledge

The **Knowledge** tab defines the context boundary for conversations within the project. Within that boundary, theGemini Enterprise assistant answers queries using your project documents and web search for external web context, while remaining isolated from other enterprise data sources unless they are explicitly added to the project.

To upload documents to your project:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Projects**.
  3. From the list of projects, click the project name and then select the **Knowledge** tab.
  4. To upload content, click the upload**Upload** icon.
  5. Choose one of the following upload options: 
     * **Upload files** : Select local files to upload.
     * **Google Drive** : Connect with Google Drive and select the files or folders to link.
     * **SharePoint** : Authorize the project's access to your linked SharePoint documents and folders.
     * **Notes** : Paste your text or type it directly into the editor, and click **Add text**.



Linked documents sync in real time. Any changes to file content or original sharing permissions sync automatically with the project.

## Chat with assistant

You can chat with Gemini Enterprise to get answers to your project questions. These chats are private; only you can see them. Other project members can't view or join your chats.

To chat with the assistant in a project:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Projects**.
  3. From the list of projects, click the project you want to chat in.
  4. In the **New chat** tab, enter your question or prompt in the chat box, and press **Enter** (or click  arrow_upward_alt ).



When you chat in a project:

  * Responses are grounded in the project's **Knowledge** files and web search.
  * You can create multiple different chats in the same project.



## Invite users to a project

To invite users to your project:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Projects**.
  3. From the list of projects, click the project that you want to share.
  4. In the **Team** tab in your project, click add**Add**.
  5. In the **Share project** dialog, enter the email addresses of the users you want to invite (separated by commas), and click **Done**. By default, invited members receive Editor permissions.

You can also share using one of the following methods:

     * Click person_add **Invite** from the **Team** , **Knowledge** , or **New chat** tabs to invite members from anywhere within your project.
     * In the **Team** tab, select users from **Suggested people** to quickly add them to your project.

**Note:** Only the project owner can invite new members. Invited members receive Editor permissions.

## Remove a user from a project

To remove a user from your project:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Projects**.
  3. From the list of projects, click the project you want to manage. 1 Select the **Team** tab.
  4. For the user you want to remove, in the **Role** column click the role assigned to the user and click person_remove **Remove access**.

**Note:** Only the project owner can remove members from a project.

## Delete a project

To delete your project:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Projects**.
  3. Next to the project that you want to delete, click _more_vert_ and click **Delete**.
  4. When prompted, confirm the deletion.

**Note:** Only the project owner can delete a project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
