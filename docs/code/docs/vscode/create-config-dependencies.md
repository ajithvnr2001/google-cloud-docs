---
url: https://docs.cloud.google.com/code/docs/vscode/create-config-dependencies/
title: Create an app with configuration dependencies \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:12.621372+00:00
---

# Create an app with configuration dependencies  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/create-config-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an app with configuration dependencies

In this quickstart, you set up an application with configuration dependencies based on a sample application and then deploy parts of the app separately.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  8. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is required for copying samples to your machine.
  9. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/vscode/install#installing) if you haven't already.



## Creating an application

  1. Clone the Bank of Anthos repository:

     1. In the top menu bar, click **Terminal** > **New Terminal**.
     2. Clone the Bank of Anthos repository:
            
            git clone https://github.com/GoogleCloudPlatform/bank-of-anthos.git
            

  2. To open the workspace based on Bank of Anthos, in VS Code, click **File** > **Open folder** and then navigate to the folder where the repository was cloned.

  3. Double-click the `skaffold.yaml` file.

     1. The file contains multiple configurations, separated by YAML document separators (`---`). Each configuration can be deployed or referenced as a dependency separately.
            
            ---
            apiVersion: skaffold/v2beta18
            kind: Config
            

     2. Configurations with a name specified are known as _modules_. The following excerpt defines the `frontend` module.
            
            metadata:
            name: frontend # module defining frontend service
            

     3. Dependencies between configurations are specified using the `configs` tag. Required configurations must be deployed before the current configuration. The sample shows a dependency that's defined in the same file. The `configs` tag can also reference other `skaffold.yaml` files in the current project.
            
            requires:
            - configs: [db]
            




## Deploying modules

  1. Open the Command Palette (`Ctrl`/`Cmd`+`Shift`+`P`) and then run **Cloud Code: Run on Kubernetes**.
  2. Click **Select modules**.
  3. Choose the modules that you want to deploy and then click **OK**.

If you click **db** , the **db** config and the **setup** config that it requires are built.

  4. When prompted, choose an image registry and then press `Enter`.




## Cleaning up

After you terminate your application, all Kubernetes resources deployed during the run are deleted automatically.

To avoid incurring charges to your account for other resources used in this quickstart, be sure to delete the cluster and project you created.

If you're using Google Cloud and would like to delete just your cluster, you can do so by following these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Hold the pointer over your cluster name and then click open_in_new **Open in Google Cloud console**.
  3. Click **Delete** and then click **Delete**.



To delete your project (and associated resources, including any clusters):

  1. Go to the Projects page in the Google Cloud console:

[Go to the Projects page](https://console.cloud.google.com/project)

  2. Select the project that you created for this quickstart and then click **Delete**.

  3. Type the project ID to confirm and then click **Shut down**.

This shuts down the project and schedules it for deletion.




## What's next

  * Learn more about [modules](https://docs.cloud.google.com/code/docs/vscode/skaffold-modules).
  * Learn about the language-specific [debugging support](https://docs.cloud.google.com/code/docs/vscode/debug) in Cloud Code.
  * Customize your Cloud Code experience by configuring [settings](https://docs.cloud.google.com/code/docs/vscode/configuring-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
