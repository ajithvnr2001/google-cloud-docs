---
url: https://docs.cloud.google.com/java/getting-started/session-handling-with-firestore/
title: Handling sessions with Firestore \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:46.484078+00:00
---

# Handling sessions with Firestore  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/getting-started/session-handling-with-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Handling sessions with Firestore Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to handle sessions on [Cloud Run](https://docs.cloud.google.com/run).

Many apps need session handling for authentication and user preferences. The [Jetty framework](https://www.eclipse.org/jetty/) comes with a memory-based implementation to perform this function. However, this implementation is unsuitable for an app that can be served from multiple instances, because the session that is recorded in one instance might differ from other instances. This tutorial shows how to handle sessions on [Cloud Run](https://docs.cloud.google.com/run).

## Objectives

  * Write the app.
  * Run the app locally.
  * Deploy the app on Cloud Run.



## Costs

In this document, you use the following billable components of Google Cloud: 

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

  4. Enable the Firestore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Firestore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com)

  8. In the Google Cloud console, open the app in [Cloud Shell](https://docs.cloud.google.com/shell). 

[Go to Cloud Shell](https://docs.cloud.google.com/console/cloudshell/open?git_branch=master&git_repo=https://github.com/GoogleCloudPlatform/java-docs-samples&working_dir=session-handling)

Cloud Shell provides command-line access to your cloud resources directly from the browser. Open Cloud Shell in your browser and click **Proceed** to download the sample code and change into the app directory. 

  9. In Cloud Shell, configure the gcloud CLI to use your new Google Cloud project: 
         
         # Configure gcloud for your project
         gcloud config set project YOUR_PROJECT_ID
         

  10. Update Maven to use Java 11 by default: 
         
         sudo update-alternatives --config java
         

When prompted, enter the number to select Java 11. Make a note of the path listed for that version. 
  11. Export the path that you copied in the previous step as an environment variable: 
         
         export JAVA_HOME=java-11-path
         




## The web app

This app displays greetings in different languages for every user. Returning users are always greeted in the same language.

![Multiple app windows displaying a greeting in different languages.](https://docs.cloud.google.com/java/images/java-sessions-app.png)

Before your app can store preferences for a user, you need a way to store information about the current user in a session. This sample app uses a `WebFilter` to retrieve and update session data in Firestore.
    
    
    @Override
    public void init(FilterConfig config) throws ServletException {
      // Initialize local copy of datastore session variables.
      firestore = FirestoreOptions.getDefaultInstance().getService();
      sessions = firestore.collection("sessions");
    
      try {
        // Delete all sessions unmodified for over two days.
        Calendar cal = Calendar.getInstance();
        cal.setTime(new Date());
        cal.add(Calendar.HOUR, -48);
        Date twoDaysAgo = Calendar.getInstance().getTime();
        QuerySnapshot sessionDocs =
            sessions.whereLessThan("lastModified", dtf.format(twoDaysAgo)).get().get();
        for (QueryDocumentSnapshot snapshot : sessionDocs.getDocuments()) {
          snapshot.getReference().delete();
        }
      } catch (InterruptedException | ExecutionException e) {
        throw new ServletException("Exception initializing FirestoreSessionFilter.", e);
      }
    }

The following diagram illustrates how Firestore handles sessions for the Cloud Run app.

![Diagram of architecture: user, Cloud Run, Firestore.](https://docs.cloud.google.com/static/languages/images/firestore-sessions-architecture-on-run.svg)

The `HttpServletRequest` uses a cookie to store a unique ID for the local session, which corresponds to a document in Firestore with the session details.

## Deleting sessions

Firestore doesn't delete old or expired sessions. You can [delete session data](https://docs.cloud.google.com/firestore/docs/using-console#delete_data) in the [Google Cloud console](https://console.cloud.google.com/firestore/) or implement an automated deletion strategy. If you use storage solutions for sessions such as Memcache or Redis, expired sessions are automatically deleted.

## Running locally

  1. Start the HTTP server:
         
         mvn jetty:run
         

  2. View the app in your web browser:

### Cloud Shell

In the Cloud Shell toolbar, click **Web preview** ![Web preview](https://docs.cloud.google.com/static/shell/docs/images/web-preview-button.png) and select **Preview on port 8080**.

### Local machine

In your browser, go to `<http://localhost:8080>`

You see one of five greetings: "Hello World", "Hallo Welt", "Hola mundo", "Salut le Monde", or "Ciao Mondo." The language changes if you open the page in a different browser or in incognito mode. You can see and edit the session data in the [Google Cloud console](https://console.cloud.google.com/firestore/).

![Firestore sessions in Google Cloud console.](https://docs.cloud.google.com/java/images/java-sessions-firestore.png)

  3. To stop the HTTP server, in your terminal window, press `Control+C`.




## Deploying and running on Cloud Run

You can use the [Cloud Run](https://docs.cloud.google.com/run) to build and deploy an app that runs reliably under heavy load and with large amounts of data.

  1. In your terminal window, build and deploy an image of your code to [Google Container Registry (GCR)](https://docs.cloud.google.com/container-registry) with the [Jib](https://github.com/GoogleContainerTools/jib) Maven plugin.

mvn clean package jib:build

  2. Deploy the app to Cloud Run:
         
         gcloud beta run deploy session-handling --image gcr.io/MY_PROJECT/session-handling   
         
                  --platform managed --region us-central1 --memory 512M
            

Replace `MY_PROJECT` with the ID of the Google Cloud project you created. Visit the URL returned by this command to see how session data persists between page loads.




## Debugging the app

If you cannot connect to your Cloud Run app, check the following:

  1. Check that the `gcloud` deploy commands successfully completed and didn't output any errors. If there were errors (for example, `message=Build failed`), fix them, and try deploying the Cloud Run app again.
  2. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer page](https://console.cloud.google.com/logs/query)

     1. In the **Recently selected resources** drop-down list, click **Cloud Run Application** , and then click **All module_id**. You see a list of requests from when you visited your app. If you don't see a list of requests, confirm you selected **All module_id** from the drop-down list. If you see error messages printed to the Google Cloud console, check that your app's code matches the code in the section about writing the web app.

     2. Make sure that the Firestore API is enabled. 




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



### Delete the Cloud Run instance

Delete the service from Cloud Run.

  * In the Google Cloud console, go to the **Services** page for Cloud Run. 

[Go to the Services page](https://console.cloud.google.com/run)

  * Select the service you wish to delete.
  * Click **Delete** _delete_ to delete the service.



## What's next

  * Try more [Cloud Run functions tutorials](https://docs.cloud.google.com/functions/docs/tutorials).
  * [Try Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container), which lets you run stateless containers on a fully managed environment or in your own Google Kubernetes Engine cluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
