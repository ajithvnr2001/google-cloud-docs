---
url: https://docs.cloud.google.com/dotnet/docs/getting-started/session-handling-with-firestore/
title: Handling sessions with Firestore \u00a0|\u00a0 .NET \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:04.536715+00:00
---

# Handling sessions with Firestore  |  .NET  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/getting-started/session-handling-with-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Handling sessions with Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Many apps need [session management](https://wikipedia.org/wiki/Session_\(computer_science\)#HTTP_session_token) for authentication and user preferences. ASP.NET core comes with [middleware](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/app-state?view=aspnetcore-2.1#session-state) to store sessions in a distributed cache.

ASP.NET's default distributed cache is actually not distributed at all. It stores session data in the memory of the web server. When only one web server is serving a web site, this strategy is fine. But when many web servers are serving a web site, the web site's users can experience errors and lost data.

To avoid errors and lost data, an ASP.NET app must use a distributed cache that stores data in a persistent data store. This tutorial shows how to manage sessions on [Cloud Run](https://docs.cloud.google.com/run/docs) by storing them in Firestore and encrypting cookies with Cloud Key Management Service.

## Objectives

  * Deploy the app on Cloud Run.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Key Management Service](https://docs.cloud.google.com/kms/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Cloud Run](https://docs.cloud.google.com/run/pricing)
  * [Firestore](https://docs.cloud.google.com/firestore/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Firestore, Cloud Run, Cloud Key Management Service, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com,run.googleapis.com,cloudkms.googleapis.com,storage-api.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Firestore, Cloud Run, Cloud Key Management Service, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com,run.googleapis.com,cloudkms.googleapis.com,storage-api.googleapis.com)

  8. To create a Firestore database in Native mode, complete the following steps: 
     1. In the Google Cloud console, go to the **Firestore viewer** page.   
[Go to the Firestore viewer](https://console.cloud.google.com/firestore/data)
     2. From the **Select a Firestore mode** screen, click **Select Native Mode**. 
     3. Select a [location](https://docs.cloud.google.com/firestore/docs/locations#types) for your Firestore database. This location setting is the [ default Google Cloud resource location for your Google Cloud project ](https://docs.cloud.google.com/firestore/docs/locations#default-cloud-location). This location is used for Google Cloud services in your Google Cloud project that require a location setting, specifically, your default [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket and your [App Engine](https://docs.cloud.google.com/appengine/docs) app.  Warning: After you set the default resource location for your Google Cloud project, you cannot change it. 
     4. Click **Create Database**. 
  9. In Cloud Shell, open the app's source code.   
[Go to Cloud Shell](https://docs.cloud.google.com/console/cloudshell/open?git_branch=main&git_repo=https://github.com/GoogleCloudPlatform/getting-started-dotnet&working_dir=Sessions)

Cloud Shell provides command-line access to your Google Cloud resources directly from the browser. 

  10. To download the sample code and change into the app directory, click **Proceed**. 
  11. In Cloud Shell, configure the gcloud CLI to use your new Google Cloud project: 
         
         # Configure gcloud for your project
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with the Google Cloud project ID that you created using the Google Cloud console. 

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) is the primary way you interact with your Google Cloud resources from the command line. In this tutorial, you use the gcloud CLI to deploy and monitor your app. 




## Examining the source code

The following diagram illustrates how Firestore handles sessions for the Cloud Run app.

![Diagram of architecture: user, Cloud Run, Firestore.](https://docs.cloud.google.com/static/languages/images/firestore-sessions-architecture-on-run.svg)

The `ConfigureServices` method in the `Startup.cs` file sets up the app to use Cloud KMS for encryption and Cloud Storage to store encrypted keys.

  1. In Cloud Shell, click ![launch editor](https://docs.cloud.google.com/static/dotnet/docs/getting-started/launch-editor.png) to launch the editor and examine the `Startup.cs` file. 
         
         public void ConfigureServices(IServiceCollection services)
         {
             // Antiforgery tokens require data protection.
             services.AddDataProtection()
                 // Store keys in Cloud Storage so that multiple instances
                 // of the web application see the same keys.
                 .PersistKeysToGoogleCloudStorage(
                     Configuration["DataProtection:Bucket"],
                     Configuration["DataProtection:Object"])
                 // Protect the keys with Google KMS for encryption and fine-
                 // grained access control.
                 .ProtectKeysWithGoogleKms(
                     Configuration["DataProtection:KmsKeyName"]);
             services.AddFirestoreDistributedCache(
                     Configuration["FIRESTORE_PROJECT_ID"])
                 .AddFirestoreDistributedCacheGarbageCollector();
             services.AddSession();
         }
         




## Setting up the Google Cloud project

  1. In the Cloud Shell editor, edit the `appsettings.json` file and replace the two instances of `YOUR-PROJECT-ID` with your Google Cloud project ID. Save the file. 
         
         {
           "Logging": {
             "LogLevel": {
               "Default": "Warning"
             }
           },
           "AllowedHosts": "*",
           "DataProtection": {
             "Bucket": "YOUR-PROJECT-ID-bucket",
             "Object": "DataProtectionProviderKeys.xml",
             "KmsKeyName": "projects/YOUR-PROJECT-ID/locations/global/keyRings/dataprotectionprovider/cryptoKeys/masterkey"
           }
         }
         

  2. Create a new Cloud Key Management Service key ring named `dataprotectionprovider`: 
         
         gcloud kms keyrings create dataprotectionprovider --location global

  3. Create a new Cloud Key Management Service key named `masterkey`: 
         
         gcloud kms keys create masterkey --location global --keyring dataprotectionprovider --purpose=encryption

  4. Create a Cloud Storage bucket to store the encrypted keys:
         
         gcloud storage buckets create gs://PROJECT_ID-bucket




## Deploying and running on Cloud Run

You can use the [Cloud Run](https://docs.cloud.google.com/run) to build and deploy an app that runs reliably under heavy load and with large amounts of data.

This tutorial uses the Cloud Run to deploy the server.

  1. In your Cloud Shell, publish your app:
         
         dotnet publish -c Release
         

  2. Use Cloud Build to build a Docker container and publish to Container Registry: 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/sessions bin/Release/netcoreapp2.1/publish

  3. Run the container with Cloud Run: 
         
         gcloud beta run deploy sessions --region us-central1 --platform managed --image gcr.io/PROJECT_ID/sessions --allow-unauthenticated

Make a note of the URL in the output:
         
         Service [sessions] revision [sessions-00003-xiz] has been deployed and is serving
         100 percent of traffic at https://sessions-r3f3em7nuq-uc.a.run.app

  4. To view the live app, go to the URL that you copied from the previous step.




## Deleting sessions

You can [delete session data](https://docs.cloud.google.com/firestore/docs/using-console#delete_data) in the [Google Cloud console](https://console.cloud.google.com/firestore/) or implement an automated deletion strategy. If you use storage solutions for sessions such as Memcache or Redis, expired sessions are automatically deleted.

## Debugging the app

If you cannot connect to your Cloud Run app, check the following:

  1. Check that the `gcloud` deploy commands successfully completed and didn't output any errors. If there were errors (for example, `message=Build failed`), fix them, and try deploying the Cloud Run app again.
  2. See the [Cloud Run guide to viewing logs](https://docs.cloud.google.com/run/docs/logging). 



## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Learn more about Cloud Run](https://docs.cloud.google.com/run/docs).
  * [Learn more about Cloud KMS](https://docs.cloud.google.com/kms/docs).
  * [Learn more about Cloud Storage](https://docs.cloud.google.com/storage/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
