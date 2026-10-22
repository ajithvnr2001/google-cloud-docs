---
url: https://docs.cloud.google.com/code/docs/intellij/secret-manager-ux/
title: Manage secrets with Secret Manager in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:38.809119+00:00
---

# Manage secrets with Secret Manager in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/secret-manager-ux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)



Send feedback 

#  Manage secrets with Secret Manager in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager lets you avoid storing secrets in your codebase. Instead, you store them in Secret Manager and fetch them programmatically when you need them. With Cloud Code's Secret Manager integration, you can easily create, view, update, and use secrets.

This page describes how to access Secret Manager in your IDE and how you can get started creating and managing secrets.

## Enabling Secret Manager

Your secret needs to be in the same project as your application code and Secret Manager API needs to be enabled for your project.

  1. To launch Secret Manager, click the Secret Manager tab in the right Cloud Code sidebar or go to **Tools** > **Cloud Code** > **Secret Manager**.

![Secret Manager tab in Cloud Code highlighted in the right sidebar and Secret Manager pane open with three secrets listed and the version details of the secret 'test' listed in the bottom pane](https://docs.cloud.google.com/static/code/docs/intellij/images/secret-ui.png)

  2. If you haven't enabled the Secret Manager API, enable it when Cloud Code prompts you by clicking **Enable API**.

![Enable API link available in the Secret Manager pane](https://docs.cloud.google.com/static/code/docs/intellij/images/enable-secret-manager.png)




## Creating and viewing secrets

### Creating secrets

You can create a secret using one of the following methods:

#### Using the Secret Manager pane

  1. Navigate to the Secret Manager pane.

  2. Click **\+ Add**.

  3. In the Create Secret dialog, configure your secret and then click **OK**.

![Create Secret dialog open with Name field filled out as 'life' and Secret Value filled out as '42'](https://docs.cloud.google.com/static/code/docs/intellij/images/create-secret.png)




#### Using the editor

  1. Open a file containing text you would like to store as a secret in the editor.
  2. Highlight the text to store as a secret, right-click the text, and then click **Create Secret in Secret Manager**.
  3. In the Create Secret dialog, configure your secret and then click **OK**.



#### Using the project explorer

  1. In the project explorer, without highlighting any text, right-click and then click **Create Secret in Secret Manager**.

  2. In the Create Secret dialog, configure your secret and then click **OK**.




### Creating new versions of secrets

To update an existing secret, create a new version of the secret:

  1. In the Secret Manager pane, right-click a secret and then click **New Version**.

  2. In the Add new version dialog, set the value of your existing secret by using the Secret value field or by importing a file.

![Add a new version dialog open with Secret value field for secret 'test-secret' updated as 'bar'](https://docs.cloud.google.com/static/code/docs/intellij/images/add-secret-version.png)

  3. To remove all previous versions of your secret and keep just the new version you're creating, choose **Disable all past versions**.

  4. Click **OK**. Your version is added, you can see your latest secret version, and if applicable, all the versions of your secret listed on the Versions tab.




### Viewing secrets

To view secrets, in the Secret Manager pane, select a secret from the list displayed in the Secret Name section. Its details such as name, replication policy, creation timestamp, and resource ID are listed in the Overview tab.

To view and manage a secret in your browser, right-click the secret and then choose **Open in Cloud console**.

## Accessing secrets from your application

After your secret is created, you can include it in your code and set up authentication.

![Code tab of Secret Manager pane listing steps needed to access the secret in your code](https://docs.cloud.google.com/static/code/docs/intellij/images/code-tab-secret.png)

To access your newly created secret from your application, follow these steps:

  1. In the Secret Manager pane, click the name of the secret you want to access in code and then click the **Code** tab.
  2. Click **Install the Secret Manager client library**.
  3. On the Secret Manager API page, set the Google Cloud project and enable the Secret Manager API if you haven't already.
  4. Follow the instructions under **Install Client Library** for the language you're using.
  5. Customize and include the [relevant code snippet](https://docs.cloud.google.com/secret-manager/docs/access-secret-version) in your application's code.
  6. If you're using a service account, assign your Google service account the role required to access your Secret Manager secret. For information about IAM roles available for Secret Manager, see the [Secret Manager access control guide](https://docs.cloud.google.com/secret-manager/docs/access-control).
  7. To complete your authentication setup, follow the instructions in [Setting up authentication](https://docs.cloud.google.com/code/docs/intellij/client-libraries-ux#setting_up_authentication).



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
