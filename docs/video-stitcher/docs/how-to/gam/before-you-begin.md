---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin/
title: Before you begin \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:43.902162+00:00
---

# Before you begin  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up a Google Cloud project and configure service accounts to access the project.

## Set up a Google Cloud project

Following these steps to set up a Google Cloud project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Video Stitcher API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=videostitcher.googleapis.com&redirect=https%3A//cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Video Stitcher Admin** role to the service account. 

To grant the role, find the **Select a role** list, then select **Video Stitcher Admin**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  6. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  7. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Video Stitcher API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=videostitcher.googleapis.com&redirect=https%3A//cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin)

  11. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Video Stitcher Admin** role to the service account. 

To grant the role, find the **Select a role** list, then select **Video Stitcher Admin**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

  12. Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 
  13. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

  14. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  15. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  16. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 
  17. Use the gcloud CLI to test your authentication environment. Check that the following command outputs a text string without errors: 
         
         gcloud auth application-default print-access-token




## Activate the service account

  1. In your terminal, set the active project for gcloud commands. Replace `YOUR_PROJECT_ID` with your project ID. 
         
         gcloud config set project YOUR_PROJECT_ID

  2. Activate the service account. Replace `PATH_TO_YOUR_SERVICE_KEY` with the path to the JSON file you downloaded to your local machine. 
         
         gcloud auth activate-service-account --key-file PATH_TO_YOUR_SERVICE_KEY




You will use this service account to authorize access and call the Video Stitcher API.

## Create a service account with only permissions to create sessions

Since an OAuth token will be passed to a client application, create a **separate** service account with only permissions to create a session; thus a leaked OAuth token cannot compromise your resources, such as VOD/live configs or CDN keys.

Create a service account: 

  1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
  3. Select your project. 
  4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

  5. Click **Create and continue**. 
  6. Grant the **Video Stitcher User** role to the service account. 

To grant the role, find the **Select a role** list, then select **Video Stitcher User**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
  7. Click **Continue**. 
  8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 




Create a service account key: 

  1. In the Google Cloud console, click the email address for the service account that you created. 
  2. Click **Keys**. 
  3. Click **Add key** , and then click **Create new key**. 
  4. Click **Create**. A JSON key file is downloaded to your computer. 
  5. Click **Close**. 



## Livestream setup

If you are inserting ads into a livestream, follow the steps in this section (or see the steps for VOD).

### Link the service account to the Ad Manager account

Once the service account is created, you must link that service account to your Ad Manager account. This allows the Video Stitcher API to create livestream events on your behalf. To do this, follow the steps to [grant access](https://developers.google.com/ad-manager/api/authentication#configure) to your service account:

  1. [Sign in](https://admanager.google.com/) to Google Ad Manager (GAM).
  2. Click **Admin > Global Settings**.
  3. Make sure **API access** is enabled.
  4. Click **Add a service account user**.
  5. Complete the form, including the email address of the service account created previously.
  6. Select a role, which must include the **Manage video content with dynamic ad insertion from Google Cloud Video Stitcher** permission. You should [create a custom role](https://support.google.com/admanager/answer/177403#create-custom-role) named **Live Stream Manager** specifically for management of this service account. The custom role should have at least the following permissions: 
     * **Manage video content with dynamic ad insertion from Google Cloud Video Stitcher**
     * **View creatives** (required by the preceding permission)
     * **View video content, bundles, and metadata**
     * **View content sources**
  7. If your Ad Manager network uses [teams](https://support.google.com/admanager/answer/2445375), you must assign the "All entities" team to the service account user.
  8. Click **Save** and confirm the service account addition.



### Create a livestream

You can use one of the [Live Stream API quickstarts](https://docs.cloud.google.com/livestream/docs/quickstarts) to set up a livestream. Both HLS and MPEG-DASH livestreams are supported (see the source manifest requirements). This procedure is optional; you can use your own existing livestream.

The Live Stream API quickstarts use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for authentication, but you can use the service account you already set up. For this option, make sure the service account has the **Live Stream Editor** role.

Make sure to keep the livestream active; don't follow the steps in the **Clean up** section until you are done with the livestream.

### Source manifest requirements

The Video Stitcher API registers the config with Ad Manager by parsing the source manifest. The source manifest must have certain characteristics depending on the format.

#### HLS

  * Container format may be either: 
    * muxed MPEG-TS
    * unmuxed MPEG-TS
    * unmuxed FMP4
  * At least one rendition in the manifest with the following (properly populated) fields: 
    * codecs
    * bandwidth



#### MPEG-DASH

  * `MPD@type` set to dynamic (`@type="dynamic"`)
  * `MPD@profiles` includes the ISO Live profile `urn:mpeg:dash:profile:isoff-live:2011`
  * Should be multi-period with each period containing one or more Adaptation Sets
  * Each Adaptation Set contains one or more Representations
  * The Representations contain or inherit a `SegmentTemplate` with the `$Number$` or the `$Time$` identifier
  * `@segmentAlignment` set to true for all Adaptation Sets
  * Representations must be non-empty



## VOD stream setup

If you are inserting ads into a VOD stream, follow the steps in this section (or see the steps for a livestream).

### Create the VOD source files

This workflow requires an MPEG-DASH manifest (MPD) file, or an HTTP Live Streaming (HLS) manifest (M3U8) file, and the associated segment files. You can use your own existing VOD files or you can [create VOD source files](https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files) using the Transcoder API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
