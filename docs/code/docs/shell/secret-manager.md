---
url: https://docs.cloud.google.com/code/docs/shell/secret-manager/
title: Manage secrets with Secret Manager in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:13.160466+00:00
---

# Manage secrets with Secret Manager in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Manage secrets with Secret Manager in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code's [Secret Manager](https://docs.cloud.google.com/secret-manager) integration, you can create, view, update, and use secrets in your IDE and without storing them in your codebase.

This page describes how to access Secret Manager in your IDE and how you can get started creating and managing secrets.

## Enable Secret Manager API

When managing secrets with Cloud Code, secrets are securely stored in Secret Manager and can be programmatically fetched when you need them. All you need is the Secret Manager API enabled and the right permissions to manage secrets:

  1. Make sure that you're working in the project where your application code resides. Your secret must be in the same project as your application code.

  2. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Secret Manager** explorer.

  3. If you haven't enabled the Secret Manager API, click **Enable Secret Manager API** in the Secret Manager explorer.




## Create secrets

To create a secret using the Secret Manager explorer, follow these steps:

  1. In your IDE, click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Secret Manager** explorer.

  2. Click add **Create Secret** in the **Secret Manager** explorer.

In the **Create Secret** dialog, set your secret's project, name, value, and region, and specify labels to organize your secrets.




Alternatively, you can create a secret using the editor:

  1. Open a file containing text that you want to store as a secret in the editor.
  2. Highlight the text to store as a secret, right-click, and then click **Create Secret in Secret Manager**.
  3. In the **Create Secret** dialog, customize the secret's project, name, value, region, and labels.



## Create new versions of secrets

To create a new version of a secret using Secret Manager, follow these steps:

  1. Right-click an existing secret and then choose **Create Secret Version**.

  2. In the **Create Version** dialog, set the new value of your existing secret using the **Secret value** field or by importing a file.

  3. To remove all previous versions of your secret and keep just the new version you're creating, choose **Disable all past versions**.

  4. Click **Create Version**. Your version is added and you can see the latest secret version and previous versions listed under the **Versions** dropdowns.




Alternatively, you can create a new version of a secret in the editor:

  1. In the editor, open a file and highlight the text to store as a secret.

  2. Right-click the highlighted text and then choose **Add Version to Secret in Secret Manager**.




### Manage secret versions

To enable, disable, or destroy a version of a secret, right-click the secret and then select the command for the action you want to perform. For enabled versions of secrets, you can also view the version's value.

## View secrets

To view secrets, in the **Secret Manager** explorer, select a secret from the list. Details of the secret such as name, replication policy, creation timestamp, and resource ID are listed below the secret name.

### View secrets in Google Cloud console

Alternatively, you can view secrets in Google Cloud console by right-clicking the secret in the **Secret Manager** explorer and clicking **Open in Cloud console**.

### View secrets in Kubernetes explorer

To view secrets in the **Kubernetes** explorer, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Expand your cluster and then expand **Secrets**.
  3. Expand the secret to view its details.



## Access secrets from your application

After your secret is created, you can include it in your code and set up authentication.

To access a secret from your application:

  1. Install the Secret Manager client library.

     1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Cloud APIs** explorer.

     2. Expand **Cloud Security** > **Secret Manager API** and then follow the instructions in the Install Client Library section for the language you're using.

  2. Customize and include the [relevant code snippet](https://docs.cloud.google.com/secret-manager/docs/access-secret-version) in your application's code.

To obtain your secret's version name to use in your code, select the secret in the Secret Manager panel, right-click, and then choose **Copy Resource ID**.

  3. To complete your authentication setup, follow the Client libraries authentication guide:

     * **Local development** : If you're developing on a local cluster (like minikube or Docker Desktop) or a local emulator, you should complete the steps illustrated in the [Local development section](https://docs.cloud.google.com/code/docs/shell/client-libraries#local_development) relevant to your workflow.
     * **Remote development** : If you're using a GKE cluster or a Cloud Run service in your application, you should complete the steps illustrated in the [Remote development section](https://docs.cloud.google.com/code/docs/shell/client-libraries#remote_development) relevant to your workflow, including the Secret Manager-specific instructions for setting up the required roles on your service account.



## Add a secret as an environment variable

To add an existing [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) to the deployment as an environment variable, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Expand your minikube cluster and then expand **Secrets**.
  3. Right-click a secret that represents a deployment object and then click **Add Secret as Environment Variable**.



## Mount a secret as a volume

To mount an existing [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) as a volume in the deployment's container, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Expand your minikube cluster and then expand **Secrets**.
  3. Right-click a secret that represents a deployment object and then click **Mount Secret as Volume**.



## Delete secrets

**Note:** Deleting a secret requires the Secret Admin role (`roles/secretmanager.admin`) on the secret, project, folder, or organization. IAM roles can't be granted on a secret version.

To delete a secret using the Secret Manager in Cloud Code, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Secret Manager** explorer.

  2. Right-click an existing secret and select **Open in Cloud Console**.

  3. On the **Secret details** page, click **DELETE** and follow the prompts to delete the secret.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
