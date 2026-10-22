---
url: https://docs.cloud.google.com/code/docs/intellij/secret-manager/
title: Manage secrets with Secret Manager in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:23.981814+00:00
---

# Manage secrets with Secret Manager in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Manage secrets with Secret Manager in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code's Secret Manager integration, you can create, view, update, and use secrets within your IDE and without having them in your codebase.

This page describes how to access Secret Manager within your IDE and how you can get started creating and managing secrets.

## Enabling Secret Manager

When managing secrets with Cloud Code, secrets are securely stored in Secret Manager and can be programmatically fetched when you need them. All you need is the Secret Manager API enabled and the right permissions to manage secrets:

  1. To launch Secret Manager, click on the Secret Manager tab in the right Cloud Code sidebar.

![Secret Manager tab in Cloud Code highlighted in the right sidebar and Secret Manager panel open with three secrets listed and the version details of the secret 'test' listed in the bottom pane](https://docs.cloud.google.com/static/code/docs/intellij/images/secret-ui.png)

  2. If you haven't enabled the Secret Manager API, Cloud Code prompts you to enable it within the Secret Manager panel by clicking **Enable API**.

Your secret also needs to be in the same project as your application code; ensure you have the right project selected or switch using the project selector in the Secret Manager panel.

![Enable API link available within the Secret Manager panel](https://docs.cloud.google.com/static/code/docs/intellij/images/enable-secret-manager.png)




## Creating and viewing secrets

### Creating secrets

You can create a secret with one of the following methods:

#### Using the Secret Manager panel

  1. Navigate to the Secret Manager panel.

  2. Click the **Add** icon.

This launches a Create Secret dialog where you can set your secret's project, name, and value, as well as choose a region to store your secret and labels to organize your secrets.

![Create Secret dialog open with Name field filled out as 'life' and Secret Value filled out as '42'](https://docs.cloud.google.com/static/code/docs/intellij/images/create-secret.png)




#### Using the editor

  1. Open a file containing text you would like to store as a secret in the editor.
  2. Highlight and right-click this text.

From the menu, select the `Create Secret in Secret Manager...` menu item. This opens the Create Secret dialog with the secret value filled in with the highlighted text. You can customize the secret's project, name, value, region, and labels here.




#### Using the project explorer

  1. In the project explorer, without highlighting any text, right-click.
  2. From the menu, select the `Create Secret in Secret Manager...` menu item. This opens the Create Secret dialog. Choose your secret's project, name, value, region, and labels here, and click **OK** when done.



### Creating new versions of secrets

If you have an existing secret and would like to update it, you can do so by navigating to the **Versions** tab of the Secret Manager panel:

  1. Click the **Add** icon within the **Versions** tab.

This launches a Add new version dialog where you can set the value of your existing secret either using the Secret value field or by importing a file.

![Add a new version dialog open with Secret value field for secret 'test-secret' updated as 'bar'](https://docs.cloud.google.com/static/code/docs/intellij/images/add-secret-version.png)

  2. If you'd prefer to remove all previous versions of your secret and keep just the new version being created, choose **Disable all past versions**.

  3. Once you click **OK** and your version is added, you can see your latest secret version, and if applicable, all the versions of your secret listed under the **Versions** tab.




### Viewing secrets

To view secrets, within the Secret Manager panel, select a secret from the list displayed in the Secret Name section. Its details such as name, replication policy, creation timestamp, and resource ID are listed in the **Overview** tab.

You can also right-click the secret and choose **Open in Cloud console** to view and manage the secret in your browser.

### Viewing secret versions

To view versions of a secret, select a secret from the list displayed in the Secret Name section and select the **Versions** tab.

Right-click the secret version you'd like to take action on and choose from the available options; viewing the secret value, copying the version ID, enabling or disabling the version, and destroying the selected version.

![Version tab selected for the secret 'test' and two available versions, '2' and '3' are tabulated along with their creation time. '3' is right-clicked and 'Enable Secret Version' is selected](https://docs.cloud.google.com/static/code/docs/intellij/images/version-tab-secret.png)

## Accessing secrets from your application

Once your secret is created, you can include it in your code and set up authentication.

![Code tab of Secret Manager panel listing steps needed to access the secret in your code](https://docs.cloud.google.com/static/code/docs/intellij/images/code-tab-secret.png)

To access your newly created secret from your application, follow these steps:

  1. Install the Secret Manager client library.

Navigate to **Tools** > **Cloud Code** > **Add Cloud Libraries and Manage Cloud APIs** and select **Secret Manager** > **Secret Manager API** from the Google Cloud APIs explorer tree. Follow the language-specific instructions laid out in the Install Client Library section.

  2. Customize and include the [relevant code snippet](https://docs.cloud.google.com/secret-manager/docs/access-secret-version) in your application's code.

  3. Finally, to complete your authentication setup, you need to follow the Client libraries authentication guide:

     * **Local development** : If you're developing on a local cluster (like minikube, Docker Desktop) or a local emulator, you should complete the steps illustrated in the [Local development section](https://docs.cloud.google.com/code/docs/intellij/client-libraries#local_development) relevant to your workflow.
     * **Remote development** : If you're using a GKE cluster or a Cloud Run service in your application, you should complete the steps illustrated in the [Remote development section](https://docs.cloud.google.com/code/docs/intellij/client-libraries#remote_development) relevant to your workflow, including the Secret Manager-specific instructions for setting up the required roles on your service account.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
