---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users/
title: Authenticate users with Firebase \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:52.814568+00:00
---

# Authenticate users with Firebase  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Authenticate users with Firebase Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Add a user sign-in flow to your web service that uses [Firebase Authentication](https://firebase.google.com/docs/auth/).

In this step of the guide, you update your web service to authenticate users and to retrieve and display a user's own information after they authenticate. Note that, for this step, the site request times will still be global rather than user-specific.

## Before you begin

If you have completed all the previous steps in this guide, skip this section. Otherwise, complete one of the following:

  * Start from [Build a Python 3 App](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app) and complete all the steps leading up to this one.

  * If you already have a [Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project), you can continue by downloading a copy of the web service and adding Firebase:

    1. Download the sample application repository using [Git](https://git-scm.com/):
           
           git clone https://github.com/GoogleCloudPlatform/python-docs-samples
           

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and then extract it.

    2. Navigate to the directory that contains a copy of the files from the previous step:
           
           cd python-docs-samples/appengine/standard_python3/building-an-app/building-an-app-2
           

    3. [Add Firebase to your Google Cloud project and web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase#adding_firebase_to_your_gcp_project).




## Add Firebase authentication methods

Firebase provides JavaScript methods and variables that you can use to configure sign-in behavior for your web service. For this web service, add a sign out function, a variable that configures the sign in UI, and a function controlling what changes when a user signs in or out.

To add the behaviors required for an authentication flow, replace your `static/script.js` file's current event listener method with the following code:
    
    
    window.addEventListener('load', function () {
      document.getElementById('sign-out').onclick = function () {
        firebase.auth().signOut();
      };
    
      // Initialize the FirebaseUI Widget outside of onAuthStateChanged
      // to avoid multiple instantiation errors when logging out and back in.
      var ui = firebaseui.auth.AuthUI.getInstance() || new firebaseui.auth.AuthUI(firebase.auth());
    
      // FirebaseUI config.
      var uiConfig = {
        signInSuccessUrl: '/',
        signInOptions: [
          // Comment out any lines corresponding to providers you did not check in
          // the Firebase console.
          firebase.auth.GoogleAuthProvider.PROVIDER_ID,
          firebase.auth.EmailAuthProvider.PROVIDER_ID,
          //firebase.auth.FacebookAuthProvider.PROVIDER_ID,
          //firebase.auth.TwitterAuthProvider.PROVIDER_ID,
          //firebase.auth.GithubAuthProvider.PROVIDER_ID,
          //firebase.auth.PhoneAuthProvider.PROVIDER_ID
        ],
        // Terms of service url.
        tosUrl: '<your-tos-url>',
        // Add callbacks to handle successful sign in before redirecting
        callbacks: {
          signInSuccessWithAuthResult: function (authResult, redirectUrl) {
            // Wait for the token to be fetched before redirecting to ensure the backend gets it.
            authResult.user.getIdToken().then(function (token) {
              // Set the cookie with a path so it applies globally
              document.cookie = "token=" + token + ";path=/";
              window.location.assign(redirectUrl || '/');
            });
            // Return false to prevent Firebase UI from redirecting automatically
            return false; 
          }
        }
      };
    
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
          // User is signed in, so display the "sign out" button and login info.
          document.getElementById('sign-out').hidden = false;
          document.getElementById('login-info').hidden = false;
          console.log(`Signed in as ${user.displayName} (${user.email})`);
          user.getIdToken().then(function (token) {
            // Add the token to the browser's cookies. The server will then be
            // able to verify the token against the API.
            // SECURITY NOTE: As cookies can easily be modified, only put the
            // token (which is verified server-side) in a cookie; do not add other
            // user information.
            document.cookie = "token=" + token + ";path=/;SameSite=Lax";
          });
        } else {
          // User is signed out.
          // Show the Firebase login button.
          ui.start('#firebaseui-auth-container', uiConfig);
          // Update the login state indicators.
          document.getElementById('sign-out').hidden = true;
          document.getElementById('login-info').hidden = true;
          // Clear the token cookie safely.
          document.cookie = "token=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;SameSite=Lax";
        }
      }, function (error) {
        console.log(error);
        alert('Unable to log in: ' + error)
      });
    });

Notice that the `onAuthStateChanged()` method, which controls what changes when a user signs in or out, stores the user's ID token as a cookie. This ID token is a unique token that Firebase generates automatically when a user successfully signs in, and is used by the server to authenticate the user.

**Tip:** including a terms of service URL is optional.

## Update your web service to use tokens

Next, verify users on the server using their unique Firebase ID token, then decrypt their token so that you can print their data back to them.

To use the Firebase ID token:

  1. Retrieve, verify, and decrypt the token in the `root` method of your `main.py` file:
         
         from flask import Flask, render_template, request
         from google.auth.transport import requests
         from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
         import google.oauth2.id_token
         
         firebase_request_adapter = requests.Request()
         @app.route("/")
         def root():
             # Verify Firebase auth.
             id_token = request.cookies.[get](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_get)("token")
             error_message = None
             claims = None
             times = None
         
             if id_token:
                 try:
                     # Verify the token against the Firebase Auth API. This example
                     # verifies the token on each page load. For improved performance,
                     # some applications may wish to cache results in an encrypted
                     # session store (see for instance
                     # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
                     claims = google.oauth2.id_token.verify_firebase_token(
                         id_token, firebase_request_adapter
                     )
                 except ValueError as exc:
                     # This will be raised if the token is expired or any other
                     # verification checks fail.
                     error_message = str(exc)
         
                 # Record and fetch the recent times a logged-in user has accessed
                 # the site. This is currently shared amongst all users, but will be
                 # individualized in a following step.
                 store_time(datetime.datetime.now(tz=datetime.timezone.utc))
                 times = fetch_times(10)
         
             return render_template(
                 "index.html", user_data=claims, error_message=error_message, times=times
             )
         
         

**Tip:** Make sure to import `request` from Flask so that you can fetch the cookie containing the user's ID token.
  2. Ensure that your `requirements.txt` file includes all necessary dependencies:
         
         Flask==3.1.3; python_version >= '3.9'
         google-cloud-datastore==2.15.1
         google-auth==2.17.3
         requests==2.34.2; python_version >= '3.10'
         




## Test your web service

Test your web service by running it locally in a virtual environment:

  1. Run the following commands in your project's main directory to install new dependencies and run your web service. If you have not set up a virtual enviornment for local testing, see [testing your web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service#testing_your_web_service).
         
         pip install -r requirements.txt
         python main.py
         

  2. Enter the following address in your web browser to view your web service:
         
         http://localhost:8080
         


**Note:** Because this web service uses Firebase, you must use the `localhost` URL rather than the full IP address of your local host or you will get an authentication error. This is because your local host's IP address is not listed as an authorized domain in your Firebase project.

## Deploy your web service

Now that you have authentication working locally, you can re-deploy your web service to App Engine.

Run the following command from the root directory of your project, where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

All traffic is automatically routed to the new version you deployed.

For more information on managing versions, see [Managing Services and Versions](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service#managing_services_and_versions).

## View your service

To quickly launch your browser and access your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, run the following command:
    
    
    gcloud app browse
    

## Next steps

Now that you've set up user authentication, you're ready to learn how to update your web service to personalize data for authenticated users.

[ Previous arrow_back  Add Firebase  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase)

[ Next Personalize data  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/personalizing-data-for-authenticated-users)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
