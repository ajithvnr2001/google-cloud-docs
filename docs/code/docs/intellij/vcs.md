---
url: https://docs.cloud.google.com/code/docs/intellij/vcs/
title: Use Cloud Source Repositories in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:09.960945+00:00
---

# Use Cloud Source Repositories in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/vcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Use Cloud Source Repositories in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

Through Cloud Code, you can add new projects to [Cloud Source Repositories](https://docs.cloud.google.com/tools/cloud-repositories/docs) and check out existing projects.

**Note:** The following IDEs support this feature: 

  * IntelliJ IDEA - Ultimate
  * IntelliJ IDEA - Community
  * [ Other IntelliJ Platform-based IDEs](https://docs.cloud.google.com/code/docs/intellij/ides)



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




## Upload source code

Upload your code to Cloud Source Repositories from Cloud Code:

  1. Open the project you want to add to Cloud Source Repositories.

  2. Click **VCS** > **Upload to Cloud Source Repositories**. Alternatively, in the menu, navigate to **Tools** > **Google Cloud Code** > **Upload to Cloud Source Repositories**.

  3. In the dialog, use the drop down menu to select the **Cloud Project** associated with your project.

  4. Use the drop down menu to select your **Cloud Repository**.

     1. If you don't have a repository, or if you want to create a new one, click **Create a new cloud repository**.

Cloud Code opens a new browser window to the Google Cloud console so that you can create the new repository.

  5. By default, Cloud Code sets the **Remote Name**. You can enter a different name in the **New Remote Name** field.

  6. Click **Upload**.




## Development

For other operations such as committing and pushing new changes, navigate to **VCS** > **VCS Operations Popup**.

## Browse source files

After uploading your source code, browse the code in the Google Cloud console:

  1. In the [Google Cloud console](https://console.cloud.google.com/), select the project that contains your source code.

  2. In the search bar, search for `Cloud Source Repositories`.




## Check out source code

Check out source code from Cloud Source Repositories:

  1. Choose **VCS > Get from Version Control**. Alternatively, go to the welcome dialog and click **Get from VSC**.
  2. Select **Google Cloud** from the **Version Control** drop-down and click **Clone**.
  3. In the **Clone from Google Cloud** dialog, select the **Cloud Project** associated with your project.
  4. Select your **Cloud Repository**.
  5. Select the **Parent Directory**.
  6. Enter the **Directory Name**.
  7. Click **Clone**.



You can alternatively check out from the **Welcome** screen by selecting **Get from Version Control** and choosing **Google Cloud** from the Version Control drop-down. This displays the **Clone from Google Cloud** dialog.

## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
