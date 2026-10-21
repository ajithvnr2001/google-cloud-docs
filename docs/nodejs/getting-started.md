---
url: https://docs.cloud.google.com/nodejs/getting-started/
title: Get started with Node.js \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:58.718014+00:00
---

# Get started with Node.js  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Guides ](https://docs.cloud.google.com/nodejs/docs/setup)



Send feedback 

#  Get started with Node.js Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial is intended for those new to building apps in the cloud, such as engineers and web developers, who want to learn key app development concepts as they apply to Google Cloud. 

## Objectives

  * Learn basic Google Cloud tools, such as the [Google Cloud console](https://docs.cloud.google.com/cloud-console) and `[gcloud](https://docs.cloud.google.com/sdk/gcloud)`.
  * Deploy your app to [Cloud Run](https://docs.cloud.google.com/run/docs).
  * Persist your data with [Firestore](https://docs.cloud.google.com/firestore).
  * Store file uploads in [Cloud Storage](https://docs.cloud.google.com/storage).
  * Monitor your app using [Google Cloud Observability](https://docs.cloud.google.com/stackdriver).



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Run](https://docs.cloud.google.com/run/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Firestore](https://docs.cloud.google.com/firestore/pricing)
  * [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/pricing)



The instructions in this document are designed to keep your resource usage within the limits of Google Cloud's [Always Free](https://docs.cloud.google.com/free/docs/frequently-asked-questions#always-free) tier. To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

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

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. To create a Firestore database in Native mode, complete the following steps: 
     1. In the Google Cloud console, go to the **Firestore create database** page.   


[Go to Firestore create database](https://console.cloud.google.com/firestore/create-database)

     2. From the **Select a Cloud Firestore mode** screen, click **Select Native Mode**. 
     3. Select a [location](https://docs.cloud.google.com/firestore/docs/locations#types) for your Firestore database. This location setting is the [ default Google Cloud resource location for your Google Cloud project ](https://docs.cloud.google.com/firestore/docs/locations#default-cloud-location). This location is used for Google Cloud services in your Google Cloud project that require a location setting, specifically, your default [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket and your [Cloud Run](https://docs.cloud.google.com/run/docs) app.  Warning: After you set the default resource location for your Google Cloud project, you cannot change it. 
     4. Click **Create Database**. 
  7. Enable the Cloud Run Admin, Cloud Storage, Cloud Logging, and Error Reporting APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,storage-api.googleapis.com,logging.googleapis.com,clouderrorreporting.googleapis.com&redirect=https%3A//console.cloud.google.com)

  8. Clone the sample repo and open the sample application in Cloud Shell:   
[Go to Cloud Shell](https://docs.cloud.google.com/console/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/nodejs-getting-started&working_dir=bookshelf)

Cloud Shell provides command-line access to your Google Cloud resources directly from the browser. 

  9. At the prompt to clone the repo, click **Confirm**. 
  10. In Cloud Shell, configure the `gcloud` tool to use your new Google Cloud project: 
         
         # Configure gcloud for your project
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the Google Cloud project ID that you created using the Google Cloud console. 

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) is the primary way you interact with your Google Cloud resources from the command line. In this tutorial, you use the `gcloud` tool to deploy and monitor your app. 




## Run your app

  1. Install your app dependencies using the `npm` command: 
         
         npm install
         

  2. Run the app: 
         
         npm start
         

  3. In Cloud Shell, click **Web preview** , and select **Preview on port 8080**. This opens a new window with your running app. 



## Deploying your app to Cloud Run

Google Cloud offers [several options for running your code](https://cloud.google.com/hosting-options/). For this example, you use [Cloud Run](https://docs.cloud.google.com/run/docs) to deploy a scalable app to Google Cloud. Cloud Run doesn't require you to manage servers and automatically scales to support traffic spikes. 

  1. Use Cloud Build to build a Docker container and publish to Container Registry:  

         
         gcloud builds submit --tag gcr.io/PROJECT_ID/bookshelf .

Replace `PROJECT_ID` with the Google Cloud project ID that you created.

  2. Run the container with Cloud Run: 
         
         gcloud run deploy bookshelf --image gcr.io/PROJECT_ID/bookshelf \
         --region us-central1 --allow-unauthenticated

Your app is now viewable at the URL displayed in the output of `gcloud run`:
         
         Service [bookshelf] revision [bookshelf-00001] has been deployed and is serving 100 percent of traffic. 
         Service URL: https://bookshelf-PROJECT-uc.a.run.app

  3. Copy the URL into your web browser to view the app. ![Bookshelf app homepage](https://docs.cloud.google.com/static/languages/images/bookshelf-homepage.png)**Note** : This SSL-protected domain is created automatically, and is useful for development. You can [ set up a custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) with Cloud Run as well. 



For more information on deploying to Cloud Run, see the [Cloud Run documentation](https://docs.cloud.google.com/run/docs). 

## Persist your data with Firestore

You cannot store information on your Cloud Run instances, because it is lost if the instance is restarted, and doesn't exist when new instances are created. Instead, you use a database that all your instances read from and write to. 

Google Cloud offers [several options for storing your data](https://cloud.google.com/products/storage/). In this example, you use Firestore to store the data for each book. Firestore is a fully managed, serverless, NoSQL document database that lets you store and query data. Firestore auto scales to meet your app needs, and scales to zero when you're not using it. Add your first book now. 

  1. To create a book for your deployed app, click **Add book**. 

![Add a book to the Bookshelf app](https://docs.cloud.google.com/static/languages/images/bookshelf-add-book.png)
  2. In the **Title** field, enter `Moby Dick`.
  3. In the **Author** field, enter `Herman Melville`.
  4. Click **Save**. There is now an entry to your Bookshelf app. 

![Moby Dick Bookshelf app entry](https://docs.cloud.google.com/static/languages/images/moby-dick-bookshelf-no-image.png)
  5. In the Google Cloud console, to refresh the Firestore page, click **Refresh** _refresh_. The data appears in Firestore. The Bookshelf app stores each book as a [Firestore document](https://docs.cloud.google.com/firestore/docs/data-model#documents) with a unique ID, and all these documents are stored in a [Firestore collection](https://docs.cloud.google.com/firestore/docs/data-model#collections). For the purposes of this tutorial, the collection is called books. ![Example of a Firestore document.](https://docs.cloud.google.com/static/languages/images/moby-dick-firestore-document.png)



Firestore stores the books by using the [Firestore client library](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest). Here is an example of fetching a Firestore document: 
    
    
    const {Firestore} = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    
    const db = new [Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore.html)();
    const collection = 'Book';
    
    
    
    async function read(id) {
      const doc = await db.collection(collection).doc(id).get();
    
      if (!doc.exists) {
        throw new Error('No such document!');
      }
      return doc.data();
    }

For more information on using Firestore, see [Adding data to Firestore](https://docs.cloud.google.com/firestore/docs/manage-data/add-data). 

## Store file uploads in Cloud Storage

Now that you've added a book, it's time to add the book cover image. You cannot store files on your instances. A database isn't the right choice for image files. Instead, you use Cloud Storage. 

[Cloud Storage](https://docs.cloud.google.com/storage/docs/creating-buckets) is the primary blob store for Google Cloud. You can use Cloud Storage to host app assets that you want to share across Google Cloud. To use Cloud Storage, you need to create a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets), a basic container to hold your data. 

  1. In the Google Cloud console, go to the **Cloud Storage Browser** page. 

[Go to the Cloud Storage Browser page](https://docs.cloud.google.com/console/storage/browser)

  2. Click **Create bucket**. 
  3. In the **Create bucket** dialog, enter a name for your bucket by appending your Google Cloud project ID to the string `_bucket` so the name looks like `YOUR_PROJECT_ID_bucket`. This name is subject to the [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). All other fields can remain at their default values. 
  4. Click **Create**. 
  5. After your bucket is created, objects must be made publicly accessible to be viewed by users. To make your objects publicly accessible see [Making Data Public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public). 
  6. Click **Edit book** , and select an image to upload as your book's cover. For example, you can use this public domain image:  
![Moby Dick book cover](https://docs.cloud.google.com/static/languages/images/moby-dick.jpg)
  7. Click **Save**. You're redirected to the homepage, where there is an entry to your Bookshelf app.  
![Moby Dick Bookshelf app entry](https://docs.cloud.google.com/static/languages/images/moby-dick-bookshelf-with-image.png)



The bookshelf app sends uploaded files to Cloud Storage by using the [Cloud Storage client library](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest). 
    
    
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    const bucket = storage.bucket(CLOUD_BUCKET);

**Note:** You can change the bucket name by setting the `CLOUD_BUCKET` variable in the preceding code to a different name and redeploying your app by running the `gcloud app deploy` command.

For more information on using Cloud Storage, see the [Cloud Storage introduction](https://docs.cloud.google.com/storage/docs/introduction). 

## Monitor your app using Google Cloud Observability

You've deployed your app and created and modified books. To monitor these events for your users, use Application Performance Management. 

### Monitor logs with Cloud Logging

  1. In the Google Cloud, go to the **Logs Explorer**

[Go to Logs Explorer](https://docs.cloud.google.com/console/logs/viewer?resource=cloud_run_revision%2Fservice_name%2Fbookshelf)

You can monitor your app in real time. If you have any issues with your app, this is one of the first places to look. 

![Stackdriver Log Viewer](https://docs.cloud.google.com/static/languages/images/logging-ui-cloud-run.png)
  2. In the **Resource** drop-down list, select **Cloud Run Revision, bookshelf**. 



### Monitor errors with Error Reporting

  1. In the Google Cloud console, go to the **Error Reporting** page.  
[Go to Error Reporting page](https://docs.cloud.google.com/console/errors)  
Error Reporting highlights errors and exceptions in your app and lets you set up alerting around them. 
  2. In your browser, go to the `/errors` URL in your app.  

         
         YOUR_CLOUD_RUN_URL/errors

This generates a new test exception and sends it to Google Cloud Observability. 

  3. In the Google Cloud console, return to the **Error Reporting** page, and in a few moments the new error is visible. Click **Auto Reload** so you don't need to manually refresh the page. 

![Error message from Error Reporting.](https://docs.cloud.google.com/static/nodejs/images/error-message-bookshelf.png)



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

#### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Deploying an app to Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image)
  * [Deploying an app to Compute Engine](https://docs.cloud.google.com/nodejs/getting-started/getting-started-on-compute-engine)
  * [Handling sessions with Firestore](https://docs.cloud.google.com/nodejs/getting-started/session-handling-with-firestore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
