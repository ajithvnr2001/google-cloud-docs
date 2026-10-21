---
url: https://docs.cloud.google.com/php/getting-started/session-handling-with-firestore/
title: Handling sessions with Firestore \u00a0|\u00a0 PHP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:48.884319+00:00
---

# Handling sessions with Firestore  |  PHP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/getting-started/session-handling-with-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Guides ](https://docs.cloud.google.com/php/getting-started)



Send feedback 

#  Handling sessions with Firestore Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to handle sessions on [App Engine](https://docs.cloud.google.com/appengine/docs/standard).

Many apps need session handling for authentication and user preferences. PHP comes with a memory-based implementation to perform this function. However, this implementation is unsuitable for an app that can be served from multiple instances, because the session that is recorded in one instance might differ from other instances.

## Objectives

  * Write the app.
  * Run the app locally.
  * Deploy the app on App Engine.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://docs.cloud.google.com/appengine/pricing)
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

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Firestore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Configure the gcloud CLI to use your new Google Cloud project: 
         
         # Configure gcloud for your project
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with the Google Cloud project ID that you created or selected previously. 



## Setting up the project

  1. In your terminal window, start in a directory of your choosing and create a new directory named `sessions`. All of the code for this tutorial is inside the `sessions` directory.

  2. Change into the `sessions` directory:
         
         cd sessions
         

  3. Install the dependencies:
         
         composer require google/cloud-firestore
         




At the end of this tutorial, the final file structure is similar to the following:
    
    
    sessions
    ├── app.yaml
    └── composer.json
    ├── index.php
    

## Writing the app

  * In your terminal window, create a file called `index.php` with the following content:
        
        <?php
        /*
         * Copyright 2019 Google LLC
         *
         * Licensed under the Apache License, Version 2.0 (the "License");
         * you may not use this file except in compliance with the License.
         * You may obtain a copy of the License at
         *
         *   http://www.apache.org/licenses/LICENSE-2.0
         *
         * Unless required by applicable law or agreed to in writing, software
         * distributed under the License is distributed on an "AS IS" BASIS,
         * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         * See the License for the specific language governing permissions and
         * limitations under the License.
         */
        
        require_once __DIR__ . '/vendor/autoload.php';
        
        use Google\Cloud\Firestore\FirestoreClient;
        
        $projectId = getenv('GOOGLE_CLOUD_PROJECT');
        // Instantiate the Firestore Client for your project ID.
        $firestore = new FirestoreClient([
            'projectId' => $projectId,
        ]);
        
        $handler = $firestore->sessionHandler(['gcLimit' => 500]);
        
        // Configure PHP to use the the Firebase session handler.
        session_set_save_handler($handler, true);
        session_save_path('sessions');
        session_start();
        
        $colors = ['red', 'blue', 'green', 'yellow', 'pink'];
        /**
         * This is an example of a front controller for a flat file PHP site. Using a
         * Static list provides security against URL injection by default.
         */
        switch (@parse_url($_SERVER['REQUEST_URI'])['path']) {
            case '/':
                if (!isset($_SESSION['views'])) {
                    $_SESSION['views'] = 0;
                    $_SESSION['color'] = $colors[rand(0, 4)];
                }
                printf(
                    '<body bgcolor="%s">Views: %s</body>',
                    $_SESSION['color'],
                    $_SESSION['views']++
                );
                break;
            default:
                http_response_code(404);
                exit('Not Found');
        }
        




This app displays greetings in different languages for every user. Returning users are always greeted in the same language.

![Multiple app windows displaying a greeting in different languages.](https://docs.cloud.google.com/php/images/php-sessions-app.png)

Before your app can store preferences for a user, you need a way to store information about the current user in a session. This sample app uses Firestore to store session data.

You can use the [`Firestore session handler`](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/FirestoreSessionHandler) to use Firestore for PHP sessions.

The following diagram illustrates how Firestore handles sessions for the App Engine app.

![Diagram of architecture: user, App Engine, Firestore.](https://docs.cloud.google.com/static/languages/images/firestore-sessions-architecture-on-gae.svg)

After you’ve set `session_set_save_handler`, every request has a `$_SESSION` global variable that you can use to access the session. The session data is stored in Firestore.

## Running locally

  1. Start the built-in PHP web server:
         
         php -S localhost:8080
         

  2. View the app in your web browser:

### Cloud Shell

In the Cloud Shell toolbar, click **Web preview** ![Web preview](https://docs.cloud.google.com/static/shell/docs/images/web-preview-button.png) and select **Preview on port 8080**.

### Local machine

In your browser, go to `<http://localhost:8080>`

You see one of five greetings: “Hello World”, “Hallo Welt”, "Hola mundo”, “Salut le Monde”, or “Ciao Mondo.” The language changes if you open the page in a different browser or in incognito mode. You can see and edit the session data in the [Google Cloud console](https://console.cloud.google.com/firestore/).

![Firestore sessions in Google Cloud console.](https://docs.cloud.google.com/php/images/php-sessions-firestore.png)

  3. To stop the HTTP server, in your terminal window, press `Control+C`.




## Deploying and running on App Engine

You can use the [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard) to build and deploy an app that runs reliably under heavy load and with large amounts of data.

This tutorial uses the App Engine standard environment to deploy the server.

  1. In your terminal window, create an `app.yaml` file and copy the following:
         
         runtime: php73
         

  2. Deploy the app on App Engine:
         
         gcloud app deploy
         

  3. To view the live app, enter the following URL:

`https://PROJECT_ID.REGION_ID.r.appspot.com`

Replace the following:

     * `PROJECT_ID`: Your Google Cloud project ID
     * `REGION_ID`: A [code that App Engine assigns to your app](https://docs.cloud.google.com/appengine/docs/standard/php/how-requests-are-routed#region-id)



The greeting is now delivered by a web server running on an App Engine instance.

## Deleting sessions

PHP performs session [garbage collection (GC)](https://www.php.net/manual/en/function.session-gc.php), which removes old and expired sessions according to your `php.ini` configuration. The Firestore session handler doesn't clean up sessions by default, but you can configure it to do so by passing a `gcLimit` option when creating the session handler:
    
    
    $handler = $firestore->sessionHandler(['gcLimit' => 500]);

Sessions are removed using probability based session GC, or when you call the `session_gc` function explicitly.

## Debugging the app

If you cannot connect to your App Engine app, check the following:

  1. Check that the `gcloud` deploy commands successfully completed and didn't output any errors. If there were errors (for example, `message=Build failed`), fix them, and try deploying the App Engine app again.
  2. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer page](https://console.cloud.google.com/logs/query)

     1. In the **Recently selected resources** drop-down list, click **App Engine Application** , and then click **All module_id**. You see a list of requests from when you visited your app. If you don't see a list of requests, confirm you selected **All module_id** from the drop-down list. If you see error messages printed to the Google Cloud console, check that your app's code matches the code in the section about writing the web app.

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



### Delete the App Engine instance

  1. In the Google Cloud console, go to the **Versions** page for App Engine. 

[Go to Versions](https://console.cloud.google.com/appengine/versions)

  2. Select the checkbox for the non-default app version that you want to delete. **Note:** The only way you can delete the default version of your App Engine app is by deleting your project. However, you can [stop the default version in the Google Cloud console](https://console.cloud.google.com/appengine/versions). This action shuts down all instances associated with the version. You can restart these instances later if needed. 

In the App Engine standard environment, you can stop the default version only if your app has manual or basic scaling. 

  3. To delete the app version, click delete **Delete**. 



## What's next

  * [Learn more about App Engine](https://docs.cloud.google.com/appengine/docs).
  * [Add background processing with Pub/Sub and Cloud Run](https://docs.cloud.google.com/php/getting-started/background-processing).
  * [Deploy an app to Compute Engine](https://docs.cloud.google.com/php/tutorials/getting-started-on-compute-engine).
  * [Deploy an app to Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image).
  * [Authenticate users with IAP](https://docs.cloud.google.com/php/getting-started/authenticate-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
