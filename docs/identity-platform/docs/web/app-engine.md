---
url: https://docs.cloud.google.com/identity-platform/docs/web/app-engine/
title: Signing in users on App Engine \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:45.453352+00:00
---

# Signing in users on App Engine  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback 

#  Signing in users on App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to retrieve, verify, and store third-party credentials using Identity Platform, the App Engine standard environment, and Datastore.

This document walks you through a simple note-taking application called Firenotes that stores users' notes in their own personal notebooks. Notebooks are stored per user, and identified by each user's unique Identity Platform ID. The application has the following components:

  * The frontend configures the sign-in user interface and retrieves the Identity Platform ID. It also handles authentication state changes and lets users see their notes.

  * [FirebaseUI](https://github.com/firebase/FirebaseUi-Web) is an open-source, drop-in solution that simplifies authentication and UI tasks. The SDK handles user login, linking multiple providers to one account, recovering passwords, and more. It implements authentication best practices for a smooth and secure sign-in experience. 

  * The backend verifies the user's authentication state and returns user profile information as well as the user's notes.




The application stores user credentials in Datastore by using the [NDB client library](https://docs.cloud.google.com/appengine/docs/standard/python/ndb), but you can store the credentials in a database of your choice.

Firenotes is based on the [Flask](http://flask.pocoo.org/) web application framework. The sample app uses Flask because of its simplicity and ease of use, but the concepts and technologies explored are applicable regardless of which framework you use.

## Objectives

By completing this tutorial, you'll accomplish the following:

  * Configure the user interface with FirebaseUI for Identity Platform.
  * Obtain an Identity Platform ID token and verify it using server-side authentication.
  * Store user credentials and associated data in Datastore.
  * Query a database using the NDB client library.
  * Deploy an app to App Engine.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * Datastore 
  * Identity Platform 



Use the [Pricing Calculator](https://docs.cloud.google.com/products/calculator) to generate a cost estimate based on your projected usage. 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free-trial). 

## Before you begin

  1. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/), [Python 2.7](https://www.python.org/), and [ virtualenv](https://docs.cloud.google.com/python/setup#installing_and_using_virtualenv). For more information on setting up your Python development environment, such as installing the latest version of Python, refer to [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/setup) for Google Cloud. 

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




If you have already installed and initialized the SDK to a different project, set the `gcloud` project to the App Engine project ID you're using for Firenotes. See [Managing Google Cloud SDK Configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations) for specific commands to update a project with the `gcloud` tool.

## Cloning the sample app

To download the sample to your local machine:

  1. Clone the sample application repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and extract it.

  2. Navigate to the directory that contains the sample code:
         
         cd python-docs-samples/appengine/standard/firebase/firenotes
         




## Adding the user interface

To configure FirebaseUI for Identity Platform and enable identity providers:

  1. Add Identity Platform to your app by following these steps:

     1. Go to the [Google Cloud console](https://console.cloud.google.com/).   
[Go to the Google Cloud console](https://console.cloud.google.com/)
     2. Select the Google Cloud project you want to use: 
        * If you have an existing project, select it on the **Select organization** drop-down list at the top of the page.
        * If you don't have an existing Google Cloud project, [create a new project](https://console.cloud.google.com/projectcreate) in the Google Cloud console.
     3. Go to the [Identity Platform Marketplace](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity) page in the Google Cloud console.   
[Go to the Identity Platform Marketplace page](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity)
     4. On the Identity Platform Marketplace page, click **Enable Customer Identity**.
     5. Go to the Customer Identity [Users](https://console.cloud.google.com/customer-identity/users) page in the Google Cloud console.   
[Go to the Users page](https://console.cloud.google.com/customer-identity/users)
     6. On the top right, click application **setup details**.
     7. Copy the application setup details into your Web Application.
            
            // This code is for illustration purposes only.
            
            // Obtain the following from the "Add Firebase to your web app" dialogue
            // Initialize Firebase
            var config = {
              apiKey: "<API_KEY>",
              authDomain: "<PROJECT_ID>.firebaseapp.com",
              databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
              projectId: "<PROJECT_ID>",
              storageBucket: "<BUCKET>.appspot.com",
              messagingSenderId: "<MESSAGING_SENDER_ID>"
            };

  2. Edit the `backend/app.yaml` file to add `GOOGLE_CLOUD_PROJECT : 'PROJECT_ID'` in the `env_variables` section:
         
         # Copyright 2021 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         # This code is designed for Python 2.7 and
         # the App Engine first-generation Runtime which has reached End of Support.
         
         runtime: python27
         api_version: 1
         threadsafe: true
         service: backend
         
         handlers:
         - url: /.*
           script: main.app
         
         env_variables:
           GAE_USE_SOCKETS_HTTPLIB : 'true'
         

  3. In the `frontend/main.js` file, configure the [FirebaseUI login widget](https://github.com/firebase/FirebaseUI-Web) by selecting which providers you want to offer your users.
         
         // This code is for illustration purposes only.
         
         // Firebase log-in widget
         function configureFirebaseLoginWidget() {
           var uiConfig = {
             'signInSuccessUrl': '/',
             'signInOptions': [
               // Leave the lines as is for the providers you want to offer your users.
               firebase.auth.GoogleAuthProvider.PROVIDER_ID,
               firebase.auth.FacebookAuthProvider.PROVIDER_ID,
               firebase.auth.TwitterAuthProvider.PROVIDER_ID,
               firebase.auth.GithubAuthProvider.PROVIDER_ID,
               firebase.auth.EmailAuthProvider.PROVIDER_ID
             ],
             // Terms of service url
             'tosUrl': '<your-tos-url>',
           };
         
           var ui = new firebaseui.auth.AuthUI(firebase.auth());
           ui.start('#firebaseui-auth-container', uiConfig);
         }

  4. In the Google Cloud console, enable the providers you chose to keep:

     1. Go to the Customer Identity [Providers](https://console.cloud.google.com//customer-identity/providers) page in the Google Cloud console.   
[Go to the Providers page](https://console.cloud.google.com/customer-identity/providers)
     2. Click **Add A Provider**.
     3. On the **Select a provider** drop-down list, select the providers you want to use.
     4. Next to **Enabled** , click the button to enable the provider. 
        * For third-party identity providers, enter the provider ID and secret from the provider's developer site. The Firebase docs give specific instructions in the "Before you begin" sections of the [Facebook](https://firebase.google.com/docs/auth/web/facebook-login), [Twitter](https://firebase.google.com/docs/auth/web/twitter-login), and [GitHub](https://firebase.google.com/docs/auth/web/github-auth) guides.
        * For SAML and OIDC integrations, refer to the configuration at your IdP.
  5. Add your domain to the list of authorized domains in Identity Platform:

     1. Go to the Customer Identity [Settings](https://console.cloud.google.com//customer-identity/settings) page in the Google Cloud console.   
[Go to the Settings page](https://console.cloud.google.com/customer-identity/settings)
     2. Under **Authorized Domains** , click **Add Domain**.
     3. Enter the domain of your app in the following format:
            
            [PROJECT_ID].appspot.com
            

Don't include `http://` before the domain name.




## Installing dependencies

  1. Navigate to the `backend` directory and complete the application setup:
         
         cd backend/
         

  2. Install the dependencies into a `lib` directory in your project:
         
         pip install -t lib -r requirements.txt
         

  3. In `appengine_config.py`, the `vendor.add()` method registers the libraries in the `lib` directory.




## Running the application locally

To run the application locally, use the App Engine local development server:

  1. Add the following URL as the `backendHostURL` in `main.js`:

`http://localhost:8081`

  2. Navigate to the root directory of the application. Then, start the development server:
         
         dev_appserver.py frontend/app.yaml backend/app.yaml
         

  3. Visit <http://localhost:8080/> in a web browser.




## Authenticating users on the server

Now that you have set up a project and initialized an application for development, you can walk through the code to understand how to retrieve and verify Identity Platform ID tokens on the server.

### Getting an ID token from Identity Platform

The first step in server-side authentication is retrieving an access token to verify. Authentication requests are handled with the `onAuthStateChanged()` listener from Identity Platform:
    
    
    firebase.auth().onAuthStateChanged(function (user) {
      if (user) {
        $('#logged-out').hide();
        var name = user.displayName;
    
        /* If the provider gives a display name, use the name for the
        personal welcome message. Otherwise, use the user's email. */
        var welcomeName = name ? name : user.email;
    
        user.getIdToken().then(function (idToken) {
          userIdToken = idToken;
    
          /* Now that the user is authenicated, fetch the notes. */
          fetchNotes();
    
          $('#user').text(welcomeName);
          $('#logged-in').show();
    
        });
    
      } else {
        $('#logged-in').hide();
        $('#logged-out').show();
    
      }
    });

When a user is signed in, the Identity Platform `getToken()` method in the callback returns a Identity Platform ID token in the form of a JSON Web Token (JWT).

### Verifying tokens on the server

After a user signs in, the frontend service fetches any existing notes in the user's notebook through an AJAX `GET` request. This requires authorization to access the user's data, so the JWT is sent in the `Authorization` header of the request using the `Bearer` schema:
    
    
    // Fetch notes from the backend.
    function fetchNotes() {
      $.ajax(backendHostUrl + '/notes', {
        /* Set header for the XMLHttpRequest to get data from the web server
        associated with userIdToken */
        headers: {
          'Authorization': 'Bearer ' + userIdToken
        }
      })

Before the client can access server data, your server must verify the token is signed by Identity Platform. You can verify this token using the [Google Authentication Library for Python](http://google-auth.readthedocs.io/). Use the authentication library's [`verify_firebase_token`](http://google-auth.readthedocs.io/en/stable/reference/google.oauth2.id_token.html#google.oauth2.id_token.verify_firebase_token) function to verify the bearer token and extract the claims:
    
    
    # This code is for illustration purposes only.
    
    id_token = request.headers["Authorization"].split(" ").pop()
    claims = google.oauth2.id_token.verify_firebase_token(
        id_token, HTTP_REQUEST, audience=os.environ.get("GOOGLE_CLOUD_PROJECT")
    )
    if not claims:
        return "Unauthorized", 401

Each identity provider sends a different set of claims, but each has at least a `sub` claim with a unique user ID and a claim that provides some profile information, such as `name` or `email`, that you can use to personalize the user experience on your app.

## Managing user data in Datastore

After authenticating a user, you need to store their data for it to persist after a signed-in session has ended. The following sections explain how to store a note as a Datastore _entity_ and segregate entities by user ID.

### Creating entities to store user data

You can create an entity in Datastore by declaring an [NDB model class](https://docs.cloud.google.com/appengine/docs/standard/python/ndb/creating-entity-models) with certain properties such as integers or strings. Datastore indexes entities by _kind_ ; in the case of Firenotes, the kind of each entity is `Note`. For querying purposes, each `Note` is stored with a _key name_ , which is the user ID obtained from the `sub` claim in the previous section.

The following code demonstrates how to set properties of an entity, both with the constructor method for the model class when the entity is created and through assignment of individual properties after creation:
    
    
    # This code is for illustration purposes only.
    
    data = request.get_json()
    
    # Populates note properties according to the model,
    # with the user ID as the key name.
    note = Note(parent=ndb.Key(Note, claims["sub"]), message=data["message"])
    
    # Some providers do not provide one of these so either can be used.
    note.friendly_id = claims.get("name", claims.get("email", "Unknown"))

To write the newly created `Note` to Datastore, call the `put()` method on the `note` object.

### Retrieving user data

To retrieve user data associated with a particular user ID, use the NDB `query()` method to search the database for notes in the same entity group. Entities in the same group, or _[ancestor path](https://docs.cloud.google.com/appengine/docs/standard/python/datastore/entities#Ancestor_paths)_ , share a common key name, which in this case is the user ID.
    
    
    # This code is for illustration purposes only.
    
    def query_database(user_id):
        """Fetches all notes associated with user_id.
    
        Notes are ordered them by date created, with most recent note added
        first.
        """
        ancestor_key = ndb.Key(Note, user_id)
        query = Note.query(ancestor=ancestor_key).order(-Note.created)
        notes = query.fetch()
    
        note_messages = []
    
        for note in notes:
            note_messages.append(
                {
                    "friendly_id": note.friendly_id,
                    "message": note.message,
                    "created": note.created,
                }
            )
    
        return note_messages
    
    

You can then fetch the query data and display the notes in the client:
    
    
    // This code is for illustration purposes only.
    
    // Fetch notes from the backend.
    function fetchNotes() {
      $.ajax(backendHostUrl + '/notes', {
        /* Set header for the XMLHttpRequest to get data from the web server
        associated with userIdToken */
        headers: {
          'Authorization': 'Bearer ' + userIdToken
        }
      }).then(function (data) {
        $('#notes-container').empty();
        // Iterate over user data to display user's notes from database.
        data.forEach(function (note) {
          $('#notes-container').append($('<p>').text(note.message));
        });
      });
    }

## Deploying your app

You have successfully integrated Identity Platform with your App Engine application. To see your application running in a live production environment:

  1. Change the backend host URL in `main.js` to `https://backend-dot-[PROJECT_ID].appspot.com`. Replace `[PROJECT_ID]` with your project ID.
  2. Deploy the application using the Google Cloud SDK command-line interface:
         
         gcloud app deploy backend/index.yaml frontend/app.yaml backend/app.yaml
         

  3. View the application live at `https://[PROJECT_ID].appspot.com`.

**Note:** Datastore indexes take a few minutes to update, so the application might not be fully functional immediately after deployment.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete your App Engine project:

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
