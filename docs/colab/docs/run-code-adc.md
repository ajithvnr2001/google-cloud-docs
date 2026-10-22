---
url: https://docs.cloud.google.com/colab/docs/run-code-adc/
title: Access Google Cloud services and APIs \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:48.081903+00:00
---

# Access Google Cloud services and APIs  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/run-code-adc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access Google Cloud services and APIs

This page describes how to access Google Cloud services and APIs through your Colab Enterprise notebook.

## Overview

When you run code in a Colab Enterprise notebook, you can access Google Cloud services and APIs by using the credentials associated with your Google Account, also called _user credentials_. This means that the runtime that you use has the same level of access to Google Cloud that the user does. This makes it easier to write and run code that interacts with Google Cloud services and APIs.

Colab Enterprise can use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate your user credentials to Google Cloud services and APIs. This page describes the following ways to provide your user credentials to ADC:

  * Use a runtime that has end-user credentials enabled.

  * Provide your user credentials to ADC by running code in your notebook.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to access Google Cloud services and APIs in a Colab Enterprise notebook, ask your administrator to grant you the Colab Enterprise Admin ([`roles/aiplatform.colabEnterpriseAdmin`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.colabEnterpriseAdmin)) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Use a runtime with end-user credentials enabled

You can use the default runtime, which has end-user credentials enabled, or any runtime created from a [runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template) in which end-user credentials are enabled.

If you don't have a sufficient runtime template with end-user credentials enabled, you must create one. You must enable or turn off end-user credentials when you create a runtime template. This setting can't be modified later.

**Note:** The first time that you connect to a runtime that has end-user credentials enabled, a dialog asks you to grant Colab Enterprise access to your user credentials. If you complete the dialog without granting access, you must take additional steps before you can successfully run code that interacts with Google Cloud services and APIs. See User credentials not found when running code.

### Connect to a runtime with end-user credentials enabled

To connect to a runtime with end-user credentials enabled:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open. If you haven't created a notebook yet, [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart#create). 

  4. In your notebook, click the **Additional connection options** expander arrow, and then select **Connect to a runtime**.  
![](https://docs.cloud.google.com/static/colab/images/additional-connection-options.png)

The **Connect to Agent Platform runtime** dialog opens.

  5. For **Select a runtime** , select **Connect to an existing runtime**. 

  6. For **Select an existing runtime option** , select the runtime that you want to connect to. If there aren't any runtimes in the list, [create a runtime](https://docs.cloud.google.com/colab/docs/create-runtime#create) or [connect to the default runtime](https://docs.cloud.google.com/colab/docs/connect-to-runtime#default). 

  7. In the **Runtime details** table, verify that **Personal credentials** are `Enabled`. 

  8. Click **Connect**.

  9. If this is your first time connecting to a runtime with end-user credentials enabled, a **Sign in** dialog appears. 

To grant Colab Enterprise access to your user credentials, complete the following steps: 

     1. In the **Sign in** dialog, click your user account.

     2. Select **See, edit, configure, and delete your Google Cloud data...** to grant Colab Enterprise access to your user credentials. 

![The checkbox is next to a statement
      that says, "See, edit, configure, and delete your Google Cloud data and see the
      email address for your Google Account."](https://docs.cloud.google.com/static/colab/images/access-checkbox.png)
     3. Click **Continue**.




When you access Google Cloud services and APIs by using end-user credentials, be aware that if your Google Account doesn't have the required Identity and Access Management (IAM) permissions in your project, your code might not be able to access some resources. If this happens, ask your administrator to grant you the required permissions.

## Provide your user credentials to ADC by running code in your notebook

If your runtime doesn't have end-user credentials enabled, you can still use your user credentials to access Google Cloud services and APIs. To do so, provide your user credentials to ADC by using the Google Cloud CLI.

  1. Use the following command to create a credential file:
         
         !gcloud auth application-default login

A **Sign in** dialog appears.

  2. Complete the dialog to grant Colab Enterprise access.

After you sign in, your credentials are stored in the [local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). This file is stored on your runtime's VM. 




When you provide user credentials to create a local ADC file, you should be aware of the following:

  * User credentials might not work for some methods and APIs, such as the Cloud Translation API or the Cloud Vision API, without extra parameters or configuration. If you see an error message about the API not being enabled in the project, or that there is no quota project available, see [Troubleshooting your ADC setup](https://docs.cloud.google.com/docs/authentication/troubleshoot-adc).

  * The local ADC contains your access and refresh tokens. Any user with access to your file system can use those credentials. If you no longer need these local credentials, you can revoke them by using the [`gcloud auth application-default revoke` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/revoke).

  * If your Google Account doesn't have the required Identity and Access Management (IAM) roles in your project, your code might not be able to access some resources. If this happens, someone must grant you the required roles.

  * ADC access is limited to Google Cloud. If you have access to other services through your Google Account, ADC won't automatically grant your Colab Enterprise notebook access, but you can grant additional access to some services. For example, to grant access to Google Drive, run the following in a code cell of your notebook:
        
        !gcloud auth application-default login \
            --scopes="https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/cloud-platform"
        




## Troubleshoot

This section shows you how to resolve issues with running code that interacts with Google Cloud services and APIs.

### User credentials not found when running code

This issue occurs when you try to run code in a notebook that interacts with Google Cloud services and APIs, but you haven't granted Colab Enterprise access to your user credentials. 

The error message might look like one of the following:
    
    
    Request had invalid authentication credentials.
    Expected OAuth 2 access token, login cookie or other valid authentication credential
    
    
    
    DefaultCredentialsError: Your default credentials were not found.
    

See the following common reasons for this issue and their resolutions:

  * You didn't complete a **Sign in** dialog that appears when you first connect to a runtime that has end-user credentials enabled. By completing this dialog, you grant Colab Enterprise access to your user credentials. 

To resolve this issue, try connecting to the runtime again and grant access.

To validate that access has been granted:

    1. Click **Account > Managed Google Account > Data and Privacy > Third-party Apps & Services**.

    2. Verify that Colab Enterprise is listed.

![](https://docs.cloud.google.com/static/colab/images/access-granted.png)
  * In the **Sign in** dialog (consent screen) that appears when you first connect to a runtime that has end-user credentials enabled, you didn't select your user account to grant Colab Enterprise access to your user credentials. 

To resolve this issue:

    1. In the [Google Cloud console](https://console.cloud.google.com/agent-platform/colab/notebooks), click your account profile image, and then click **Google Account**. 

    2. Click **Data & privacy**.

    3. In **Data from apps and services you use** , click **Third-party apps & services**. 

    4. Click **Colab Enterprise**.

    5. In **Colab Enterprise has some access to your Google Account** , click **See details**.

    6. Click **Remove access**.

    7. Click **Confirm**.

This removes your current access settings.

    8. The next time you [connect to a runtime that has end-user credentials enabled](https://docs.cloud.google.com/colab/docs/run-code-adc#connect), make sure to select the correct user account when you complete the **Sign in** dialog. 

  * A pop-up blocker might be preventing the Colab Enterprise **Sign in** dialog (consent screen) from appearing.

To resolve this issue, enable pop-ups temporarily in your browser and try to connect to the runtime again.

  * Enterprise service restrictions might be blocking access to Colab Enterprise. 

To isolate this issue, [ verify that your organization's service restrictions aren't blocking access to Google services](https://support.google.com/a/answer/7646040). 

**Service Status** should be **ON for everyone**. 

  * You aren't using a runtime with end-user credentials enabled, and you haven't provided your user credentials to Application Default Credentials (ADC) by using the Google Cloud CLI. 

To resolve this issue, see [Provide your user credentials to ADC by running code in your notebook](https://docs.cloud.google.com/colab/docs/run-code-adc#run-code). 




## What's next

  * Learn more about [how Application Default Credentials work](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

  * [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template) with end-user credentials enabled.

  * You can interact with Agent Platform by using the Colab Enterprise side panel. To learn more, see:

    * [Tune a model.](https://docs.cloud.google.com/colab/docs/tuning)
    * [Create an experiment.](https://docs.cloud.google.com/colab/docs/experiments)
  * To find a notebook that can help you get your project started quickly, see the [notebook gallery](https://console.cloud.google.com/agent-platform/colab/notebook-gallery). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
