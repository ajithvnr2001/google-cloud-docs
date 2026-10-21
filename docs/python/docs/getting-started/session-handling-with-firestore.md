---
url: https://docs.cloud.google.com/python/docs/getting-started/session-handling-with-firestore/
title: Handling sessions with Firestore \u00a0|\u00a0 Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:34.070407+00:00
---

# Handling sessions with Firestore  |  Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/getting-started/session-handling-with-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Handling sessions with Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Many apps need session handling for authentication and user preferences. The [Flask framework](http://flask.pocoo.org/ "Python Flask framework") comes with a memory-based implementation to perform this function. However, this implementation is unsuitable for an app that can be served from multiple instances, because the session that is recorded in one instance might differ from other instances. This tutorial shows how to handle sessions on [App Engine](https://docs.cloud.google.com/appengine/docs/standard).

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

  14. Install Python, `pip`, and `virtualenv` on your system. For instructions, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup) for Google Cloud. 



## Setting up the project

  1. In your terminal window, start in a directory of your choosing and create a new directory named `sessions`. All of the code for this tutorial is inside the `sessions` directory.

  2. Change into the `sessions` directory:
         
         cd sessions
         

  3. Create the `requirements.txt` with the following contents:
         
         google-cloud-firestore==2.11.1
         flask==2.2.5
         

  4. Install the dependencies:
         
         pip install  -r requirements.txt
         




At the end of this tutorial, the final file structure is similar to the following:
    
    
    sessions
    ├── app.yaml
    ├── main.py
    └── requirements.txt
    

## Writing the web app

This app displays greetings in different languages for every user. Returning users are always greeted in the same language.

![Multiple app windows displaying a greeting in different languages.](https://docs.cloud.google.com/python/docs/images/python-sessions-app.png)

Before your app can store preferences for a user, you need a way to store information about the current user in a session. This sample app uses cookies and Firestore to store session data.

  * In your terminal window, create a file called `main.py` with the following content:
        
        import random
        from uuid import uuid4
        
        from flask import Flask, make_response, request
        from google.cloud import firestore
        
        
        app = Flask(__name__)
        db = firestore.[Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html)()
        sessions = db.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)('sessions')
        greetings = [
            'Hello World',
            'Hallo Welt',
            'Ciao Mondo',
            'Salut le Monde',
            'Hola Mundo',
        ]
        
        
        @firestore.[transactional](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.html)
        def get_session_data(transaction, session_id):
            """ Looks up (or creates) the session with the given session_id.
                Creates a random session_id if none is provided. Increments
                the number of views in this session. Updates are done in a
                transaction to make sure no saved increments are overwritten.
            """
            if session_id is None:
                session_id = str(uuid4())   # Random, unique identifier
        
            doc_ref = sessions.document(document_id=session_id)
            doc = doc_ref.get(transaction=transaction)
            if doc.[exists](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot.html#google_cloud_firestore_v1_base_document_DocumentSnapshot_exists):
                session = doc.[to_dict](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot.html#google_cloud_firestore_v1_base_document_DocumentSnapshot_to_dict)()
            else:
                session = {
                    'greeting': random.choice(greetings),
                    'views': 0
                }
        
            session['views'] += 1   # This counts as a view
            transaction.set(doc_ref, session)
        
            session['session_id'] = session_id
            return session
        
        
        @app.route('/', methods=['GET'])
        def home():
            template = '<body>{} views for "{}"</body>'
        
            transaction = db.[transaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_transaction)()
            session = get_session_data(transaction, request.cookies.get('session_id'))
        
            resp = make_response(template.format(
                session['views'],
                session['greeting']
                )
            )
            resp.set_cookie('session_id', session['session_id'], httponly=True)
            return resp
        
        
        if __name__ == '__main__':
            app.run(host='127.0.0.1', port=8080)

  * The following diagram illustrates how Firestore handles sessions for the App Engine app.

![Diagram of architecture: user, App Engine, Firestore.](https://docs.cloud.google.com/static/languages/images/firestore-sessions-architecture-on-gae.svg)




## Deleting sessions

You can [delete session data](https://docs.cloud.google.com/firestore/docs/using-console#delete_data) or implement an automated deletion strategy. If you use storage solutions for sessions such as Memcache or Redis, expired sessions are automatically deleted.

## Running locally

  1. In your terminal window, install the [Gunicorn HTTP server](https://gunicorn.org/):
         
         pip install gunicorn
         

  2. Run the Gunicorn HTTP server:
         
         gunicorn -b :8080 main:app
         

  3. View the app in your web browser:

### Cloud Shell

In the Cloud Shell toolbar, click **Web preview** ![Web preview](https://docs.cloud.google.com/static/shell/docs/images/web-preview-button.png) and select **Preview on port 8080**.

### Local machine

In your browser, go to `<http://localhost:8080>`

You see one of five greetings: "Hello World", "Hallo Welt", "Hola mundo", "Salut le Monde", or "Ciao Mondo." The language changes if you open the page in a different browser or in incognito mode. You can see and edit the session data in the [Google Cloud console](https://console.cloud.google.com/firestore/).

![Firestore sessions in Google Cloud console.](https://docs.cloud.google.com/python/docs/images/python-sessions-firestore.png)

  4. To stop the HTTP server, in your terminal window, press `Control+C`.




## Deploying and running on App Engine

You can use the [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard) to build and deploy an app that runs reliably under heavy load and with large amounts of data.

This tutorial uses the App Engine standard environment to deploy the server.

  1. In your terminal window, create an `app.yaml` file and copy the following:
         
         runtime: python37

  2. Deploy the app on App Engine:
         
         gcloud app deploy
         

  3. View the live app at `https://your-project-id.appspot.com`:
         
         gcloud app browse
         

Where your-project-id is your Google Cloud project ID.




The greeting is now delivered by a web server running on an App Engine instance.

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

  * Try additional [Cloud Run functions tutorials](https://docs.cloud.google.com/functions/docs/tutorials).
  * [Learn more about App Engine](https://docs.cloud.google.com/appengine/docs).
  * [Try Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container), which lets you run stateless containers on a fully managed environment or in your own Google Kubernetes Engine cluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
