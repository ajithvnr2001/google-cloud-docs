---
url: https://docs.cloud.google.com/code/docs/vscode/modernize-dotnet-apps/
title: Modernize your .NET application \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:15.251695+00:00
---

# Modernize your .NET application  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/modernize-dotnet-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Modernize your .NET application Stay organized with collections  Save and categorize content based on your preferences. 

Code modernization for .NET, powered by Gemini Generative AI models, is a code generation and application modernization tool. It helps you modernize your Microsoft .NET Framework applications that are Windows-dependent by refactoring your applications to cross-platform .NET code.

Cross-platform .NET applications, unlike .NET Framework applications, can run on Linux, eliminating the need for Windows licenses and enabling cloud-native capabilities including containerization.

In this guide, you'll grant IAM roles for your Google Cloud project, create a Cloud Storage bucket, create a Gemini API key, and install the `code-modernization-for-dotnet` extension on your local machine to re-factor your .NET Framework application to cross-platform .NET code.

## Before you begin

  1. [Create a Google Account](https://support.google.com/accounts/answer/27441), if you don't already have one. You can use any email address to create a Google Account, including your work email address.
  2. Submit the [Code Modernization for .NET: Allowlist Request form](https://docs.google.com/forms/d/1KPLECo92gZ8Q36L1h6EyVpmKr_QieOl6QFROrLOBvd4/edit) to join the allow list. You can't proceed with the steps on this page until this request has been approved.

  3. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Build, Secret Manager, Cloud Storage JSON API, Generative Language API, Cloud Logging, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com,storage-api.googleapis.com,generativelanguage.googleapis.com,logging.googleapis.com,compute.googleapis.com)

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud Build, Secret Manager, Cloud Storage JSON API, Generative Language API, Cloud Logging, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com,storage-api.googleapis.com,generativelanguage.googleapis.com,logging.googleapis.com,compute.googleapis.com)

  10. [Install VS Code](https://code.visualstudio.com/), if you haven't already.



## Grant Identity and Access Management (IAM) roles

###  Console 

  1. To grant the IAM roles for your Google Cloud project, go to the **IAM & Admin** page.

[Go to IAM & Admin](https://console.cloud.google.com/projectselector/iam-admin/iam)

  2. Add the following IAM roles:



  * **User Permissions**

    * Storage Object User (`roles/storage.objectUser`)
    * Cloud Build Editor (`roles/cloudbuild.builds.editor`)
  * **Cloud Build Service Account**

    * Cloud Build Service Account (`roles/cloudbuild.builds.builder`)
    * Secret Manager Accessor (`roles/secretmanager.secretAccessor`)
    * Logs Writer (`roles/logging.logWriter`)
    * Storage Object User (`roles/storage.objectUser`)



###  gcloud 

To add the required IAM roles, run the following `gcloud` commands:

  * Assign the Storage Object User (`roles/storage.objectUser`) role:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_ID" \
        --role="roles/storage.objectUser"
        

  * Assign the Cloud Build Editor (`roles/cloudbuild.builds.editor`) role:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_ID" \
        --role="roles/cloudbuild.builds.editor"
        

  * Assign the Cloud Build Service Account (`roles/cloudbuild.builds.builder`) role:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT" \
          --role="roles/cloudbuild.builds.builder"
        

  * Assign the Secret Manager Accessor (`roles/secretmanager.secretAccessor`) role:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT" \
          --role="roles/secretmanager.secretAccessor"
        

  * Assign the Logs Writer (`roles/logging.logWriter`) role:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT" \
          --role="roles/logging.logWriter"
        

  * Assign the Storage Object User (`roles/storage.objectUser`) role:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT" \
          --role="roles/storage.objectUser"
        




## Create a Cloud Storage bucket

To create a Cloud Storage bucket, run the following:
    
    
    gcloud storage buckets create gs://BUCKET_NAME \
    --project=PROJECT_ID
    

## Create Gemini API key and save in Secret Manager

To create a Gemini API key, run the following:
    
    
    gcloud services api-keys create --project=PROJECT_ID \
      --display-name="API Key for .Net Modernization" \
      --api-target="service=generativelanguage.googleapis.com" \
      --key-id="gemini-api-key"
    

To save the Gemini API key in Secret Manager, run the following:
    
    
    gcloud services api-keys get-key-string gemini-api-key \
    --project=PROJECT_ID \
    --format="value(keyString)" | \
    
    gcloud secrets create "gemini-api-key" \
    --project=PROJECT_ID \
    --data-file=- \
    --replication-policy="automatic"
    

## Install and configure the extension

**Note:** After submitting the [Code Modernization for .NET: Allowlist Request form](https://docs.google.com/forms/d/1KPLECo92gZ8Q36L1h6EyVpmKr_QieOl6QFROrLOBvd4/edit) to join the allow list, you'll need to wait for the request to be approved before proceeding with the steps in this section.

Once your [Code Modernization for .NET: Allowlist Request form](https://docs.google.com/forms/d/1KPLECo92gZ8Q36L1h6EyVpmKr_QieOl6QFROrLOBvd4/edit) is approved, you'll receive the extension as a `.VSIX` file. To install the extension to your local machine, follow these steps:

  1. In VS Code, navigate to **Extensions** in the activity bar.

  2. Click more_horiz **Views and More Actions** and select **Install from VSIX**.

  3. Navigate to and select the VSIX package file. This initiates the installation of the `Code-modernization-for-dotnet` extension in VS Code on your local machine.

  4. Once the installation is complete, restart VS Code.

  5. Update `Code Modernization for .NET extension` settings to the following:

     * **Extension Mode** : `Version 2`
     * **Project ID** : `PROJECT_ID`
     * **Bucket Name** : `BUCKET_NAME`
     * **Region** : `us-central1`
     * **Gemini API Secret** : `gemini-api-key`
     * **Google Account** : `GOOGLE_ACCOUNT`
     * **Target Framework** : `.NET 8.0`

Replace the following:

     * `PROJECT_ID`: The ID of your Google Cloud project—for example, `1234567890`.
     * `BUCKET_NAME`: The name of your Cloud Storage bucket.
     * `GOOGLE_ACCOUNT`: Your Google Account—for example, `your_full_name@gmail.com`.



## Trigger the build

  1. To login to Google Cloud, run the following command:
         
         gcloud auth login --update-adc
         

  2. To trigger the modernization workflow, in the activity bar, select **Source Control** , click more_horiz **More Actions** to open the context menu, and select **Google Cloud: Modernize .NET code**.




## Add your project to the allow list

To get your project on the allow list, email your Cloud Build Service Account ID to `code-modernization-for-dotnet-discuss@google.com`.

You can also contact the same email address for support, to ask questions, or to provide feedback. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
