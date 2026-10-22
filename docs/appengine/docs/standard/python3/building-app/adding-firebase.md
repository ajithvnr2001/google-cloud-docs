---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase/
title: Add Firebase to your web service \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:09.513161+00:00
---

# Add Firebase to your web service  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Add Firebase to your web service Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Add Firebase to your Google Cloud project, configure your authentication settings, and then add Firebase to your web service.

Adding Firebase to your web service enables you to authenticate users so that you can give each user a personalized experience.

## Before you begin

If you have completed all the previous steps in this guide, skip this section. Otherwise, complete one of the following:

  * Start from [Build a Python 3 App](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app) and complete all the steps leading up to this one.

  * If you already have a [Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project), you can continue by downloading a copy of the web service:

    1. Download the sample application repository using [Git](https://git-scm.com/):
           
           git clone https://github.com/GoogleCloudPlatform/python-docs-samples
           

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and then extract it.

    2. Navigate to the directory that contains a copy of the files from the previous step:
           
           cd python-docs-samples/appengine/standard_python3/building-an-app/building-an-app-1
           




## Add Firebase to your Google Cloud project

To use Firebase authentication with your web service, add Firebase to your Google Cloud project and configure your authentication settings.

  1. Add Firebase to your existing Google Cloud project using the **Add project** tool in the [Firebase console](https://console.firebase.google.com/).

You can also choose to use a Firebase account with a different name, not associated with your existing Google Cloud project.

  2. Enable the authentication sign-on providers in the [Firebase console](https://console.firebase.google.com/). For this web service, you will enable **Email/Password** and **Google** sign-in providers:

     1. Click **Security** > **Authentication** > **Sign-in method**.

     2. Under **Sign-in providers** , select **Add new provider** > **Email/Password**.

     3. Toggle the **Enable** button to use email and password authentication, and click **Save**.

**Tip:** For more information about enabling other providers, see the "Before you begin" sections of the [Google](https://firebase.google.com/docs/auth/web/google-signin), [Facebook](https://firebase.google.com/docs/auth/web/facebook-login), [Twitter](https://firebase.google.com/docs/auth/web/twitter-login), and [GitHub](https://firebase.google.com/docs/auth/web/github-auth) guides on Firebase.
  3. For Firebase to authenticate properly, your domain needs to be authorized for OAuth redirects. To authorize your domain:

     1. Select **Security** > **Authentication** > **Settings**.

     2. Under **Authorized domains** on the **Settings** page, click **Add Domain**.

     3. Enter the domain of your app on App Engine, excluding the `http://` prefix:

`PROJECT_ID`. `REGION_ID.r.appspot.com` where `PROJECT_ID` is the ID of your Google Cloud project.




## Add Firebase to your web service

To add Firebase to your web service, copy your Firebase project's custom code snippet, JavaScript and CSS files into your web service:

  1. Go to the [Firebase console](https://console.firebase.google.com/) and select your project.

  2. From the project overview page, under the text **Get started by adding Firebase to your app** , select **web**. If you already have an app added to the project, you may not see this text; instead, navigate to the **Project Overview** > **Project settings** > **General** page of your existing app, scroll down, and select **Add app**.

  3. Once the app is registered, a customized code snippet will be displayed. Copy the contents of the snippet. To see this code snippet again later, navigate to the **Project settings** page for your Firebase app.

  4. Update your `templates/index.html` file by completing the following:

     1. Add the following lines to the `<head>` tag:
            
            <script src="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.js"></script>
            <link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.css" />

     2. Add your customized code snippet to the `<body>` tag.

For this tutorial, you can add the code to the top of the body, since the only content in `templates/index.html` is an example of Firebase services. In your production environment, we recommend that you add the code snippet to the bottom of the body, but before you use any Firebase services.

Your custom code will look similar to this mock snippet:
            
            <!-- MOCK SNIPPET: DO NOT COPY -->
            <!-- The core Firebase JS SDK is always required and must be listed first -->
            <script src="https://www.gstatic.com/firebasejs/7.14.5/firebase-app.js"></script>
            
            <!-- TODO: Add SDKs for Firebase products that you want to use
                 https://firebase.google.com/docs/web/setup#available-libraries -->
            
            <script>
              var config = {
                apiKey: "<API_KEY>",
                authDomain: "<PROJECT_ID>.firebaseapp.com",
                databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
                projectId: "<PROJECT_ID>",
                storageBucket: "<BUCKET>.appspot.com",
                messagingSenderId: "<SENDER_ID>",
              };
              firebase.initializeApp(config);
            </script>
            

     3. Replace the TODO in the snippet above with the following script tag to enable the Authentication component of Firebase:
            
            <script src="https://www.gstatic.com/firebasejs/7.8.0/firebase-auth.js"></script>
             

These script addresses are documented in the [Firebase UI for Web documentation](https://firebaseopensource.com/projects/firebase/firebaseui-web/).

     4. Replace the rest of the body with the following code, which you will use later in this guide to display authenticated user data:
            
            <div id="firebaseui-auth-container"></div>
            
            <button id="sign-out" hidden=true>Sign Out</button>
            
            <div id="login-info" hidden=true>
              <h2>Login info:</h2>
              {% if user_data %}
                <dl>
                  <dt>Name</dt><dd>{{ user_data['name'] }}</dd>
                  <dt>Email</dt><dd>{{ user_data['email'] }}</dd>
                  <dt>Last 10 visits</dt><dd>
            	{% for time in times %}
                      <p>{{ time['timestamp'] }}</p>
                    {% endfor %} </dd>
                </dl>
              {% elif error_message %}
                <p>Error: {{ error_message }}</p>
              {% endif %}
            </div>




## Next Steps

Now that you've added Firebase to your Google Cloud project and your web service, you're ready to add code to your web service to enable it to authenticate users.

[ Previous arrow_back  Handle data  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/storing-and-retrieving-data)

[ Next Authenticate users  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
