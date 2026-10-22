---
url: https://docs.cloud.google.com/iap/docs/authenticate-users-external-identities/
title: Quickstart: Authenticate users with external identities \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:57.751577+00:00
---

# Quickstart: Authenticate users with external identities  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/authenticate-users-external-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate users with external identities

This quickstart shows you how to secure an app using Identity-Aware Proxy (IAP) and external identities. By combining IAP and [Identity Platform](https://docs.cloud.google.com/identity-platform), you can authenticate users with a wide range of identity providers, such as [OAuth](https://en.wikipedia.org/wiki/OAuth), [SAML](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language), and [OIDC](https://en.wikipedia.org/wiki/OpenID_Connect), in addition to Google Accounts.

In this quickstart, you'll secure a sample App Engine app using Facebook authentication.

## Before you begin

### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Project Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) (`roles/resourcemanager.projectCreator`)
  * App Engine Admin(`roles/appengine.appAdmin`) 
  * [Firebase Authentication Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.viewer) (`roles/firebaseauth.viewer`)
  * [IAP Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) (`roles/iap.admin`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)
  * [Identity Platform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. Initialize App Engine for your project:
         
         gcloud app create --project=project-id
         

  5. [ Install Git](https://git-scm.com/).

  6. Install a current version of [ Node.js](https://nodejs.org). 

  7. [ Install the Firebase command-line tool](https://firebase.google.com/docs/cli):
         
         npm install -g firebase-tools
         




## Enable the APIs

First, enable Identity Platform:

  1. Go to the **Identity Platform Marketplace** page in the Google Cloud console.

[ Go to the Identity Platform Marketplace page](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity)

  2. Click **Enable Identity Platform**. The Identity Platform page appears in the Google Cloud console.




Then, enable IAP:

  1. Go to the **IAP** page in the Google Cloud console.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Select the same project you used for Identity Platform. Using different projects is not supported.

  3. Click **Enable API**.




## Download and deploy the sample code

The code for this quickstart has two components: a _client app_ and an _authentication app_.

The client app is protected by IAP. When it receives a request from an unauthenticated user, it redirects the request to the authentication app to verify the user's identity. If the user signs in successfully, the authentication app responds with a JSON Web Token (JWT). For demonstration purposes, the client app displays the JWT.

First, download the code, and deploy the client app:

  1. Download the sample code:
         
         git clone https://github.com/GoogleCloudPlatform/iap-gcip-web-toolkit.git
         

  2. Change to the client app directory:
         
         cd iap-gcip-web-toolkit/sample/app
         

  3. Install dependencies:
         
         npm install
         

  4. Deploy the client app to App Engine:
         
         npm run deploy
         

The client app launches at the URL:
         
         https://[PROJECT-ID].appspot.com
         




Next, deploy the authentication app:

  1. Change to the directory for the authentication app:
         
         cd ../authui-firebaseui
         

  2. Install dependencies:
         
         npm install
         export NODE_OPTIONS=--openssl-legacy-provider
         

  3. Configure the authentication app to use Firebase Hosting. Specify the Google Cloud project ID of the Google Cloud project that contains the IAP protected client app:
         
         firebase use project-id
         

  4. Deploy the app:
         
         npm run deploy
         

The authentication app launches at the URL:
         
         https://[PROJECT-ID].firebaseapp.com
         




You've deployed the client and authentication apps! The next step is to configure Identity Platform and IAP.

## Set up Identity Platform

IAP uses Identity Platform to authenticate external identities. This quickstart uses Facebook as an example, but Identity Platform supports a wide range of identity providers.

### Create a Facebook app

To authenticate users with Facebook, you need an _App ID_ and _App Secret_.

  1. Log in to [ Meta for Developers](https://developers.facebook.com/). If you don't already have a Facebook account, you'll need to create one.

  2. Go to Facebook's [ My apps](https://developers.facebook.com/apps) page.

  3. Click **Create App**.

  4. In the left menu, select **Settings > Basic**.

  5. In the **Privacy Policy URL** box, enter any valid URL. If you deploy the app to production later, you can update the URL to point to your privacy policy.

  6. Take note of your App ID and App Secret. You'll need these in the next section.




### Add Facebook as an identity provider

Configure Identity Platform to use Facebook for authentication:

  1. Go to the **Identity providers** page in the Google Cloud console.

[ Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add a provider**.

  3. Select **Facebook** from the list of providers.

  4. Enter the App ID and App Secret you obtained in the previous section.

  5. Click **Save**.




### Configure the OAuth redirect URI

When Facebook finishes processing a request from the authentication app, it needs a URI to redirect to.

  1. Return to Facebook's [ My Apps](https://developers.facebook.com/) page and select your app.

  2. In the left menu, click **Products > Add Product**.

  3. Locate the **Facebook Login** product, and click **Set up**.

  4. In the left navigation menu, select **Settings** (you don't need to complete the guided quickstart flow).

  5. In the **Valid OAuth Redirect URIs** box, enter the redirect URI:
         
         https://project-id.firebaseapp.com/__/auth/handler
         

You can also find this URI in the Identity Platform provider configuration page.

  6. Click **Save Changes**.




You're finished setting up Identity Platform! Now you can configure IAP to use it for authentication.

## Enable IAP to use external identities

  1. Go to the IAP page in the Google Cloud console.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Click the **APPLICATIONS** tab.

  3. Select the sample App Engine app you deployed earlier. The URL in the **Published** category should look similar to:
         
         https://project-id.appspot.com
         

  4. In the IAP column, toggle the switch to **On**.

  5. In the side panel, click **Start** for **Use external identities for authorization**.

  6. Under **Sign-in page** , select **I'll provide my own**.

**Note:** IAP can also create a sign-in page for you. This quickstart provides sample client and authentication apps, but if you're building your apps from scratch, letting IAP create the sign-in page can help you get started faster.
  7. In the **Authentication URL** field, enter the URL of the authentication app. It should look something like:
         
         https://project-id.firebaseapp.com/
         

After you enter the URL, the Google Cloud console automatically appends your API key.

  8. Check the box with your project name. It should have Facebook listed as an identity provider.

  9. Click **Save**.




You've finished setting up IAP.

## Test user authentication

To test that IAP is protecting your app and authenticating users with Facebook:

  1. Go to the client App Engine app in your browser:
         
         https://project-id.appspot.com
         

After a brief loading screen, you are redirected to the Identity Platform sign-in page.

  2. Follow the on-screen prompts to authenticate with Facebook.

  3. You should be redirected back to the client app, which will display the JWT returned by Identity Platform.




To completely sign out, you must sign out of the sample app that you created and Facebook. You must sign out of both apps because Firebase establishes a session with Facebook that is valid for one hour. For more information, see [Manage User Sessions](https://firebase.google.com/docs/auth/admin/manage-sessions).

Congratulations! You successfully deployed an app to App Engine and protected it with IAP and external identities.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



Additionally, you may wish to delete the Facebook app you created.

## What's next

  * [Customize your authentication UI with FirebaseUI](https://docs.cloud.google.com/iap/docs/using-firebaseui), or [build a custom UI from scratch](https://docs.cloud.google.com/iap/docs/create-custom-auth-ui).
  * Learn more about configuring identity providers with [Identity Platform](https://docs.cloud.google.com/identity-platform/docs).
  * Learn how to create unique silos of users and configurations with [Identity Platform multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
