---
url: https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email/
title: Sign in a user with an email by using Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:53.490636+00:00
---

# Sign in a user with an email by using Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sign in a user with an email by using Identity Platform

Learn how to use Identity Platform to sign in a user with an email and password.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=identity-platform__sign-in-user-email)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have the following role or roles on the project: Identity Platform Admin, Service Usage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Make sure that you have the following role or roles on the project: Identity Platform Admin, Service Usage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




### Enable Identity Platform

  1. In the Google Cloud console, go to the **Identity Platform** page in the Cloud Marketplace.

[ Go to Identity Platform](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity)

  2. Click **Enable Identity Platform**.




## Configure an email sign-in

  1. Go to the **Identity Providers** page.

[ Go to Identity Providers](https://console.cloud.google.com/customer-identity/providers)

  2. On the **Identity Providers** page, click **Add a provider**.

  3. In the **Select a provider** list, select email **Email/Password**.

  4. Click the **Enabled** toggle to on.

  5. To save the provider settings, click **Save**.




## Create a user

  1. In the Google Cloud console, go to the **Users** page.

[ Go to Users](https://console.cloud.google.com/customer-identity/users)

  2. Click **Add user**.

  3. In the **Email** field, enter an email and password. Note both of these values because you need them in a later step.

  4. To add the user, click **Add**. The new user is listed on the **Users** page.




## Sign in the user

The steps to sign in the user vary depending on which SDK version your app is using.

Ensure you are following the correct steps for your application.

**Note:** Using the v9 SDK is strongly recommended, especially for production apps. If you need support for other SDK management options, like `window.firebase`, see [Upgrade from version 8 to the modular Web SDK](https://firebase.google.com/docs/web/modular-upgrade#window-compat) or [Alternative ways to add Firebase](https://firebase.google.com/docs/web/alt-setup).

### SDK v9 (modular)

### Install the SDK and initialize Firebase

Version 9 of the Firebase JS SDK uses a [JavaScript Module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) format.

This workflow uses npm and requires module bundlers or JavaScript framework tooling because the v9 SDK is optimized to work with [module bundlers](https://firebase.google.com/docs/web/module-bundling) to eliminate unused code (tree-shaking) and decrease SDK size.

To use the v9 SDK, perform the following steps:

  1. From the project directory, install Firebase using npm:
         
         npm install firebase

  2. Initialize Firebase in your app and create a Firebase App object:
         
         import { initializeApp } from 'firebase/app';
         
         const firebaseConfig = {
             apiKey: "API_KEY",
             authDomain: "AUTH_DOMAIN"
         };
         
         const app = initializeApp(firebaseConfig);

Replace the following:

     * `API_KEY`: the `apiKey` of your Firebase project.

**Important:** Avoid using multiple API keys in your Firebase project if its application restrictions are set to `None` or `Websites`. Using multiple keys with these specific restrictions can lead to ambiguity in how Firebase selects a key, potentially causing unexpected behavior or disrupting your user-facing workflows.
     * `AUTH_DOMAIN`: the `authDomain` of your Firebase project.

You can find these values from your app's [Firebase project configuration](https://firebase.google.com/docs/web/learn-more#config-object).

A Firebase App is a container-like object that stores common configuration and shares authentication across Firebase services. After you initialize a Firebase App object in your code, you can add and start using Firebase services.

If you use ESM and want to use browser modules, replace all your `import` lines with the following pattern:  
`import { } from 'https://www.gstatic.com/firebasejs/13.0.0/firebase-SERVICE.js', `   
where SERVICE is an SDK name such as `firebase-firestore`. 

Using browser modules is a quick way to get started, but we recommend using a module bundler for production. 




### Access Identity Platform in your JavaScript

Now that you have initialized the Firebase SDK, you can use it anywhere in your app. For example, here is an app that attempts to sign in a hard-coded user and display the result on a web page.
    
    
    import { initializeApp } from 'firebase/app';
    import {
      onAuthStateChanged,
      signInWithEmailAndPassword,
      getAuth
    } from 'firebase/auth';
    
    const firebaseConfig = {
      apiKey: "API_KEY",
      authDomain: "AUTH_DOMAIN"
    };
    const app = initializeApp(firebaseConfig);
    const auth = getAuth(app, {/* extra options */ });
    
    document.addEventListener("DOMContentLoaded", () => {
      onAuthStateChanged(auth, (user) => {
          if (user) {
              document.getElementById("message").innerHTML = "Welcome, " + user.email;
          }
          else {
              document.getElementById("message").innerHTML = "No user signed in.";
          }
      });
      signIn();
    });
    
    function signIn() {
      const email = "EMAIL_ID";
      const password = "PASSWORD";
      signInWithEmailAndPassword(auth, email, password)
          .catch((error) => {
              document.getElementById("message").innerHTML = error.message;
          });
    }
    

Replace the following:

  * `API_KEY`: the `apiKey` of your Firebase project.
  * `AUTH_DOMAIN`: the `authDomain` of your Firebase project.
  * `EMAIL_ID`: the user email address you created earlier in this guide.
  * `PASSWORD`: the user password you created earlier in this guide.



### Use a module bundler for size reduction

**Note:** You can skip this step if you are using a JavaScript framework CLI tool like the [Angular CLI](https://angular.io/cli), [Next.js](https://nextjs.org/), [Vue CLI](https://cli.vuejs.org/), or [Create React App](https://reactjs.org/docs/create-a-new-react-app.html). Check out [our guide on module bundling](https://firebase.google.com/docs/web/module-bundling) for more information.

The Firebase Web SDK is designed to work with module bundlers to remove any unused code (tree-shaking). We strongly recommend using this approach for production apps. Tools such as the [Angular CLI](https://angular.io/cli), [Next.js](https://nextjs.org/), [Vue CLI](https://cli.vuejs.org/), or [Create React App](https://reactjs.org/docs/create-a-new-react-app.html) automatically handle module bundling for libraries installed through npm and imported into your codebase.

For example, you can use [Webpack](https://firebase.google.com/docs/web/module-bundling#using_firebase_with_webpack) to generate a `dist` folder containing your bundled application and dependency code. See [Using module bundlers with Firebase](https://firebase.google.com/docs/web/module-bundling) for more information.

### Import your JavaScript into your page

  1. Create a new file named `index.html`.

  2. Add two basic HTML containers and import the bundled js.
         
         <script defer src="js/bundled.js"></script>
         <div>Identity Platform Quickstart</div>
         <div id="message">Loading...</div>
         

  3. Launch `index.html` in your web browser. A welcome message displaying your user's email appears.




### SDK v8 (legacy)

### Create a web page

  1. On your local machine, create a new file named `index.html`.

  2. In the HTML file, add two HTML containers:
         
         <div>Identity Platform Quickstart</div>
         <div id="message">Loading...</div>
         




### Initialize the Identity Platform client SDK with your API key

  1. In the Google Cloud console, go to the **Identity Providers** page.

[ Go to Identity Providers](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Application setup details**.

  3. Copy the initialization code into `index.html`.




### Sign in the user

  1. To sign in the user, copy the following code into `index.html`:
         
         <script>
           var email = "EMAIL_ID";
           var password = "PASSWORD";
         
           firebase.auth().onAuthStateChanged(function(user) {
             if (user) {
               document.getElementById("message").innerHTML = "Welcome, " + user.email;
             } else {
               document.getElementById("message").innerHTML = "No user signed in.";
             }
           });
         
           firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
             document.getElementById("message").innerHTML = error.message;
           });
         </script>
         

This code calls `signInWithEmailAndPassword()` and then processes the result with the `onAuthStateChanged()` callback.

Replace the following:

     * EMAIL_ID: the email for the user that you created earlier
     * PASSWORD: the password for the user that you created earlier
  2. Open `index.html` in your web browser. A welcome message displaying your user's email appears.




There is a limit on unsuccessful user sign-in attempts. Several rapid, unsuccessful sign-in attempts temporarily locks the user out of their account. 

For more information on other Identity Platform limits, see [Quotas and limits](https://docs.cloud.google.com/identity-platform/quotas). 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the provider and user

If you used an existing Google Cloud project, delete the provider and user that you created to avoid incurring charges to your account:

  1. In the Google Cloud console, go to the **Identity Providers** page.

[ Go to Identity Providers](https://console.cloud.google.com/customer-identity/providers)

  2. To delete the provider, click delete**Delete** next to the name of the provider. To confirm, click **Delete**.

  3. In the Google Cloud console, go to the **Users** page.

[ Go to Users](https://console.cloud.google.com/customer-identity/users)

  4. To delete the user that you created, click delete**Delete** next to the name of the user. To confirm, click **Delete**.




### Delete the project

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

In a real app, your users would sign up using a dedicated registration page, and then sign in by entering their emails and passwords. Identity Platform offers a [pre-built authentication UI](https://github.com/firebase/firebaseui-web) that you can use for these pages, or you can build your own. You might also want to support additional sign-in methods, such as social providers (like Facebook or Google), phone numbers, OIDC, or SAML.

Learn more about the following:

  * Sign in users with [JavaScript](https://firebase.google.com/docs/auth/web/firebaseui), [Android](https://firebase.google.com/docs/auth/android/firebaseui), [iOS](https://firebase.google.com/docs/auth/ios/firebaseui), [C++](https://firebase.google.com/docs/auth/cpp/start), or [Unity](https://firebase.google.com/docs/auth/unity/start).

  * Sign in users with [OIDC](https://docs.cloud.google.com/identity-platform/docs/web/oidc) or [SAML](https://docs.cloud.google.com/identity-platform/docs/web/saml).

  * [Migrate users from your existing app](https://docs.cloud.google.com/identity-platform/docs/migrating-users) to Identity Platform. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
