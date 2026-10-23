---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-gcloud/
title: Quickstart: Transcribe speech to text by using the gcloud CLI \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:29.706706+00:00
---

# Quickstart: Transcribe speech to text by using the gcloud CLI  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Transcribe speech to text by using the gcloud CLI

This page shows you how to send a speech recognition request to Cloud Speech-to-Text by using the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech) tool from the command line.

Cloud Speech-to-Text enables easy integration of Google speech recognition technologies into developer applications. You can send audio data to the Cloud Speech-to-Text API, which then returns a text transcription of that audio file. For more information about the service, see [Cloud STT basics](https://docs.cloud.google.com/speech-to-text/docs/basics). 

## Before you begin

Before you can send a request to the Cloud Speech-to-Text API, you must complete the following actions.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Speech-to-Text API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable speech.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud Speech-to-Text API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable speech.googleapis.com

  16. Optional: Create a new Cloud Storage bucket to store your audio data. For more information, see [Create a Cloud Storage bucket](https://docs.cloud.google.com/speech-to-text/docs/setup#create-gcs-bucket).



For more information about enabling the API, see [Set up Cloud Speech-to-Text for your Google Cloud project](https://docs.cloud.google.com/speech-to-text/docs/setup).

### Required roles

To ensure that Cloud Composer Service Agent has the necessary permissions to run Cloud Speech-to-Text, ask your administrator to grant the Service Account Token Creator (`iam.serviceAccountTokenCreator`) IAM role to Cloud Composer Service Agent on your project. **Important:** You must grant this role to Cloud Composer Service Agent, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give Cloud Composer Service Agent the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To get the permissions that you need to store audio in Cloud Storage, ask your administrator to grant you the [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) IAM role on Cloud Storage bucket. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Make an audio transcription request

Use Cloud STT to transcribe an audio file to text. Use the following code sample to send a [`recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize) request to the Cloud Speech-to-Text API.

Open the command line shell and run the following command.
    
    
    gcloud ml speech recognize gs://cloud-samples-tests/speech/brooklyn.flac \
        --language-code=en-US

This command requests that Cloud STT transcribe the audio contained in a [FLAC](https://docs.cloud.google.com/speech-to-text/docs/v1/encoding) hosted at a publicly accessible location.

If the request is successful, the server returns a response in JSON format:
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "confidence": 0.9840146,
              "transcript": "how old is the Brooklyn Bridge"
            }
          ]
        }
      ]
    }

Congratulations! You sent your first request to Cloud STT.

If you receive an error or an empty response from Cloud STT, take a look at the [troubleshooting](https://docs.cloud.google.com/speech-to-text/docs/troubleshooting) and [error mitigation](https://docs.cloud.google.com/speech-to-text/docs/error-messages) steps. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.



## What's next

  * Practice [transcribing short audio files](https://docs.cloud.google.com/speech-to-text/docs/sync-recognize). 
  * Learn how to [batch long audio files for speech recognition](https://docs.cloud.google.com/speech-to-text/docs/async-recognize). 
  * Learn how to [transcribe streaming audio](https://docs.cloud.google.com/speech-to-text/docs/streaming-recognize) like from a microphone. 
  * Get started with the Cloud STT in your language of choice by using a [Cloud STT client library](https://docs.cloud.google.com/speech-to-text/docs/reference/libraries). 
  * Work through the [sample applications](https://docs.cloud.google.com/speech-to-text/docs/samples). 
  * For best performance, accuracy, and other tips, see the [best practices](https://docs.cloud.google.com/speech-to-text/docs/best-practices) documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
