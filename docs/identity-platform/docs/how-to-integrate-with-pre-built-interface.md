---
url: https://docs.cloud.google.com/identity-platform/docs/how-to-integrate-with-pre-built-interface/
title: Integrating Identity Platform UI elements into your web app \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:49.606586+00:00
---

# Integrating Identity Platform UI elements into your web app  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/how-to-integrate-with-pre-built-interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Integrating Identity Platform UI elements into your web app 

This guide shows you how to integrate a user interface (UI) provided by Identity Platform into an existing web app.

## Before you begin

To complete this guide, you'll need the following:

  * A Google Cloud project for which you're a Project Owner, with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).



### Open-source UI components for other clients

This article shows you how to integrate UI components into a web app. For other app types, see the following pages:

  * [iOS](https://github.com/firebase/firebaseui-ios)
  * [Android](https://github.com/firebase/firebaseui-android)



## Integrating the UI components into your app

  1. Add the UI script and CSS from the CDN in the `<head>` tag of your page.

  

         
         <script src="https://www.gstatic.com/firebasejs/ui/6.1.0/firebase-ui-auth.js"></script>
         <link rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.1.0/firebase-ui-auth.css" />
         

**Note:** You should always use the most up-to-date UI components to get the benefits of new functionality that is added to the pre-integrated UI. For the latest SDK version, see the [firebaseui-web GitHub repository](https://github.com/firebase/firebaseui-web#installation).
  2. Enable at least one one sign-in method using the Google Cloud console. See the [Quickstart](https://docs.cloud.google.com/identity-platform/docs/quickstart-cicp) to learn how.

  3. In the `<head>` tag of your page, configure how your users can sign in:   

         
         <script>
         // UI Configuration
         var uiConfig = {
          signInSuccessUrl: '[URL_TO_REDIRECT_ON_SIGNIN_SUCCESS]',
          signInOptions: [
            // Leave the lines as is for the providers you want to offer your users.
            firebase.auth.GoogleAuthProvider.PROVIDER_ID,
            firebase.auth.FacebookAuthProvider.PROVIDER_ID,
            firebase.auth.TwitterAuthProvider.PROVIDER_ID,
            firebase.auth.GitHubAuthProvider.PROVIDER_ID,
            firebase.auth.EmailAuthProvider.PROVIDER_ID,
            firebase.auth.PhoneAuthProvider.PROVIDER_ID,
            firebaseui.auth.AnonymousAuthProvider.PROVIDER_ID
          ],
          // tosUrl and privacyPolicyUrl accept either url string or a callback
          // function.
          // Terms of service url/callback.
          tosUrl: '[YOUR_TOS_URL]',
          // Privacy policy url/callback.
          privacyPolicyUrl: function() {
            window.location.assign('[YOUR_PRIVACY_POLICY_URL]');
          }
         };
         
         // Initialize the UI Components.
         var ui = new firebaseui.auth.AuthUI(firebase.auth());
         // The start method will wait until the DOM is loaded.
         ui.start('#firebaseui-auth-container', uiConfig);
         </script>
         

  4. In the `<body>` element of your page, insert the UI widget:   

         
         <body>
         <!-- The surrounding HTML is left untouched. Your app can use that space for branding, controls and other customizations.-->
         <h1>Welcome to [APP_NAME]</h1>
         <div id="firebaseui-auth-container"></div>
         </body>
         

When you render your page, the UI provided by Identity Platform will appear, allowing users to sign in to your app.




To learn about more customizations, see the [UI component documentation on GitHub](https://github.com/firebase/firebaseui-web).

## What's next

  * Learn how to [Configure custom claims on users](https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims).
  * Read about the [Admin Auth API](https://docs.cloud.google.com/identity-platform/docs/concepts-admin-auth-api).
  * Learn how to [Authenticate users on App Engine using Identity Platform](https://docs.cloud.google.com/identity-platform/docs/how-to-auth-users-app-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
