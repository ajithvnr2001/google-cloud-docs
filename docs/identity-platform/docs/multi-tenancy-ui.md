---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-ui/
title: Create a sign-in page for multiple tenants with Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:30.095410+00:00
---

# Create a sign-in page for multiple tenants with Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a sign-in page for multiple tenants with Identity Platform

This page shows you how to build a sign-in page for multiple tenants in Identity Platform by using [FirebaseUI](https://github.com/firebase/firebaseui-web), which is a collection of open-source, prebuilt UI components, and the [Client SDK](https://github.com/firebase/firebase-js-sdk).

## Before you begin

  1. [Enable multi-tenancy and create at least two tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart).
  2. [Configure identity providers for each tenant](https://docs.cloud.google.com/identity-platform/docs/quickstart-cicp#add-provider).



## Get the components

You can fetch the UI script, Client SDK, and CSS files directly from the CDN by adding them to the `<head>` element of your page:
    
    
    <script src="https://www.gstatic.com/firebasejs/x.x.x/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/x.x.x/firebase-auth.js"></script>
    <script src="https://cdn.firebase.com/libs/firebaseui/x.x.x/firebaseui.js"></script>
    <link rel="stylesheet" href="https://cdn.firebase.com/libs/firebaseui/x.x.x/firebaseui.css" />
    

Alternatively, you can install the modules using `npm`, and then reference them as ES6 imports:
    
    
    npm install firebase --save && \
    npm install firebaseui --save
    
    
    
    // Import Firebase JS SDK.
    import * as firebase from "firebase/app";
    import "firebase/auth";
    import * as firebaseui from 'firebaseui'
    

## Build a UI for selecting tenants

FirebaseUI only handles sign-in flows; you need to build your own UI for users to select a tenant to sign in with.

To build a basic tenant selection page with two buttons, do the following:

  1. Create two tenant selection elements.
         
         <div id="tenant-selection-buttons">
           <button id="tenant1-select-button" data-val="tenantId1">Display name of Tenant 1</button>
           <button id="tenant2-select-button" data-val="tenantId2">Display name of Tenant 2</button>
         </div>
         

  2. Create a container element for FirebaseUI.
         
         <div id="firebaseui-auth-container"></div>
         

  3. Create a configuration for each tenant.
         
         <script>
           var uiConfigs = {
           'TENANT_ID1': {
             'signInOptions': [firebase.auth.EmailAuthProvider.PROVIDER_ID],
             'credentialHelper': 'none',
             'signInFlow': 'popup',
             'callbacks': {
               'signInSuccessWithAuthResult': function(authResult, redirectUrl) {
                 // The sign in success callback.
                 return false;
                }
             },
             // tosUrl and privacyPolicyUrl accept either url string or a callback
             // function.
             // Terms of service url/callback.
             tosUrl: '[YOUR_TOS_URL]',
             // Privacy policy url/callback.
             privacyPolicyUrl: function() {
               window.location.assign('[YOUR_PRIVACY_POLICY_URL]');
             }
           },
           'TENANT_ID2': {
             'signInOptions': [firebase.auth.GoogleAuthProvider.PROVIDER_ID],
             'credentialHelper': 'none',
             'signInFlow': 'popup',
             'callbacks': {
               'signInSuccessWithAuthResult': function(authResult, redirectUrl) {
                 // The sign in success callback.
                 return false;
                }
             },
             // tosUrl and privacyPolicyUrl accept either url string or a callback
             // function.
             // Terms of service url/callback.
             tosUrl: '[YOUR_TOS_URL]',
             // Privacy policy url/callback.
             privacyPolicyUrl: function() {
               window.location.assign('[YOUR_PRIVACY_POLICY_URL]');
             }
           }
         };
         </script>
         

  4. To render the sign-in component with FirebaseUI, add tenant selection click handlers. Before rendering the UI component, set the tenant ID on the `Auth` instance.
         
         <script>
           var ui = new firebaseui.auth.AuthUI(firebase.auth());
           tenantSelectionButton.addEventListener('click', (e) => {
           var tenantId = e.target.getAttribute('data-val');
           firebase.auth().tenantId = tenantId;
           ui.reset();
           ui.start('#firebaseui-auth-container', uiConfigs[tenantId]);
           });
         </script>
         

  5. Launch your app. A sign-in screen with two tenant buttons appears.




You can also build multi-page workflows. For example, you can create a workflow where the first page asks users for their email, and the next page lets them select a tenant. Additionally, you can host separate login pages for each tenant. To do this, you must parse the tenant ID from the URL and then set it on the `Auth` object.

## What's next

  * [See the FirebaseUI source code on GitHub](https://github.com/firebase/firebaseui-web).
  * [See the sample code on GitHub](https://github.com/firebase/quickstart-js/blob/master/auth/multi-tenant-ui.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
