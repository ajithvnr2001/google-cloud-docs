---
url: https://docs.cloud.google.com/identity-platform/docs/web/saml/
title: Signing in users with SAML \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:03.419068+00:00
---

# Signing in users with SAML  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/saml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with SAML

This document shows you how to use Identity Platform to sign in users with a Security Assertion Markup Language (SAML) 2.0 provider.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable Identity Platform, and add the client SDK to your app. For more information and instructions, see the [Sign in a user with an email by using Identity Platform](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email) quickstart. 



## Configure the provider

  1. In the Google Cloud console, go to the **Identity Platform > Identity providers** page.  
[Go to Identity providers](https://console.cloud.google.com/customer-identity/providers)  


  2. Click **Add a Provider** , and select **SAML** from the list.

  3. Enter the following details:

     1. The **Name** of the provider. This can be the same as the provider ID or a custom name. If you enter a custom name, click **Edit** next to **Provider ID** to specify the ID (which must begin with `saml`).

     2. The provider's **Entity ID**.

     3. The provider's **SAML SSO URL**.

     4. The certificate used for token-signing on the provider. Make sure to include the start and end strings. For example:
            
            -----BEGIN CERTIFICATE-----
            MIICajCCAdOgAwIBAgIBADANBgkqhkiG9w0BAQ0FADBSMQswCQYDVQQGEwJ1czEL
            ...
            LEzc1JwEGQQVDYQCwsQMSBDAF0QAB0w9GikhqkgBNADABIgABIwAgOdACCjaCIIM
            -----END CERTIFICATE-----
            

  4. In the **Service provider** section, enter the **Entity ID** of your app. This is typically your app's URL. On your SAML identity provider, this is referred to as the audience.

  5. In the **Project settings** side pane, click **Add Domain** , and add your app's domain. For example, if your app's sign-in URL is `https://example.com/login`, add `example.com`.

  6. To complete the setup, do one of the following:

     * Copy the default authorization callback URL from the **Authorization callback (URL)** field and add it to your SAML app configuration.

Using the default authorization callback URL reduces the complexity of validating the SAML response.

     * Add your customized authorization callback URL to your SAML app configuration—for example, `https://PROJECT-ID.firebaseapp.com/__/auth/handler`.

  7. In the **Configure your application** section, click **Setup Details**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  8. Click **Save**.




### Provider required elements

Identity Platform expects the `<saml:Subject>` and `<saml:NameID>` elements in responses from the provider. If you don't define values for these elements when configuring your provider, the SAML assertion fails.

### Sign requests

You can increase the security of your authentication requests by signing them.

To sign requests, first enable signed requests for your identity provider by calling [`inboundSamlConfigs.patch()`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs/patch) and setting `idp_config.sign_request` to `true`:

###  REST 

Before using any of the request data, make the following replacements: 

  * `project-id`: the ID for the Google Cloud project
  * `provider-id`: the SAML provider ID



HTTP method and URL: 
    
    
    PATCH https://identitytoolkit.googleapis.com/admin/v2/projects/project-id/inboundSamlConfigs/provider-id?updateMask=idpConfig.signRequest

Request JSON body: 
    
    
    {
      "idp_config": {
        "sign_request": true
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://identitytoolkit.googleapis.com/admin/v2/projects/project-id/inboundSamlConfigs/provider-id?updateMask=idpConfig.signRequest"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://identitytoolkit.googleapis.com/admin/v2/projects/project-id/inboundSamlConfigs/provider-id?updateMask=idpConfig.signRequest" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You must use the REST API to enable signed requests; using the Google Cloud console or Google Cloud CLI is not supported.

The response is an [`InboundSamlConfig`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs#spconfig) object, which includes an array of [`SpCertificate`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs#spcertificate) objects. Configure the value of the X509 certificate with your SAML identity provider so it can validate the signature of your requests.

**Caution:** To prevent authentication disruption, monitor the expiration date of your SP certificates and plan certificate rotation in advance during scheduled downtime. 

### Rotate service provider certificates

When using signed SAML requests, Identity Platform uses a Service Provider (SP) certificate. To prevent authentication disruption, monitor the expiration date of your SP certificates and rotate them before they expire.

**Caution:**

  * **Irreversible operation:** Rotating the SP certificate is irreversible. You cannot reinstate a previous certificate.
  * **Service disruption:** Updating the SP certificate breaks SSO for all users until the new certificate is updated at your IdP. This rotation must be coordinated in advance across Cloud Customer Care, your organization's team, and IdP administrators.



  1. To check SP certificate expiration, extract the certificate expiration timestamps using [`jq`](https://jqlang.github.io/jq/):
         
         curl -s -X GET "https://identitytoolkit.googleapis.com/v2/projects/PROJECT_ID/inboundSamlConfigs" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "X-Goog-User-Project: PROJECT_ID" \
             -H "Content-Type: application/json" | \
             jq -r '.inboundSamlConfigs[].spConfig.spCertificates[]?.expiresAt'
         

Replace `PROJECT_ID` with your Google Cloud project ID.

Check the `expiresAt` value under `spConfig.spCertificates`.

  2. If the expiration timestamp (`expiresAt`) is within 30 days or within the timeframe required by your organization, contact [Cloud Customer Care](https://cloud.google.com/support) and your IdP administrator to plan the update during a scheduled downtime.

  3. To rotate the certificate and receive the new public certificate, work with Cloud Customer Care.

  4. To update the certificate configuration on your IdP, share the new SP certificate with your IdP administrator.

  5. Test whether single sign-on (SSO) works with the updated configuration.




## Sign in users

When you sign a user in, the client SDK handles the authentication handshake, then returns ID tokens containing the SAML attributes in their payloads. To sign a user in and get attributes from the SAML provider:

  1. Create a [`SAMLAuthProvider`](https://firebase.google.com/docs/reference/js/firebase.auth.SAMLAuthProvider) instance with the provider ID you configured in the previous section. The provider ID must start with `saml`.

### Web version 9
         
         import { SAMLAuthProvider } from "firebase/auth";
         
         const provider = new SAMLAuthProvider("saml.myProvider");
         
         [auth_saml_provider_create.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/saml/auth_saml_provider_create.js#L8-L10)

### Web version 8
         
         const provider = new firebase.auth.SAMLAuthProvider('saml.myProvider');
         
         [saml.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/saml.js#L9-L9)

  2. Start the sign in flow. You can choose to either use a dialog or a redirect.

###  Popup 

### Web version 9
         
         import { getAuth, signInWithPopup, SAMLAuthProvider } from "firebase/auth";
         
         const auth = getAuth();
         signInWithPopup(auth, provider)
           .then((result) => {
             // User is signed in.
             // Provider data available from the result.user.getIdToken()
             // or from result.user.providerData
           }).catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // The AuthCredential type that was used.
             const credential = SAMLAuthProvider.credentialFromError(error);
             // Handle / display error.
             // ...
           });
         
         [auth_saml_signin_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/saml/auth_saml_signin_popup.js#L8-L26)

### Web version 8
         
         firebase.auth().signInWithPopup(provider)
           .then((result) => {
             // User is signed in.
             // Identity provider data available in result.additionalUserInfo.profile,
             // or from the user's ID token obtained from result.user.getIdToken()
             // as an object in the firebase.sign_in_attributes custom claim
             // This is also available from result.user.getIdTokenResult()
             // idTokenResult.claims.firebase.sign_in_attributes.
           })
           .catch((error) => {
             // Handle / display error.
             // ...
           });
         
         [saml.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/saml.js#L15-L27)

###  Redirect 

To redirect to a sign-in page, call `signInWithRedirect()`:

### Web version 9
         
         import { getAuth, signInWithRedirect } from "firebase/auth";
         
         const auth = getAuth();
         signInWithRedirect(auth, provider);
         
         [auth_saml_signin_redirect.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/saml/auth_saml_signin_redirect.js#L8-L11)

### Web version 8
         
         firebase.auth().signInWithRedirect(provider);
         
         [saml.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/saml.js#L33-L33)

Then, call `getRedirectResult()` to get the results when the user returns to your app:

### Web version 9
         
         import { getAuth, getRedirectResult, SAMLAuthProvider } from "firebase/auth";
         
         const auth = getAuth();
         getRedirectResult(auth)
           .then((result) => {
             // User is signed in.
             // Provider data available from the result.user.getIdToken()
             // or from result.user.providerData
           })
           .catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // The AuthCredential type that was used.
             const credential = SAMLAuthProvider.credentialFromError(error);
             // Handle / display error.
             // ...
           });
         
         [auth_saml_signin_redirect_result.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/saml/auth_saml_signin_redirect_result.js#L8-L27)

### Web version 8
         
         firebase.auth().getRedirectResult()
           .then((result) => {
             // User is signed in.
             // Provider data available in result.additionalUserInfo.profile,
             // or from the user's ID token obtained from result.user.getIdToken()
             // as an object in the firebase.sign_in_attributes custom claim
             // This is also available from result.user.getIdTokenResult()
             // idTokenResult.claims.firebase.sign_in_attributes.
           }).catch((error) => {
             // Handle / display error.
             // ...
           });
         
         [saml.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/saml.js#L39-L50)

  3. Retrieve the user attributes associated with the SAML provider from the ID token using the `firebase.sign_in_attributes` claim. Make sure to verify the ID token using the Admin SDK when you send it to your server.

The ID token includes the user's email address only if it is provided in the `NameID` attribute of the SAML assertion from the identity provider:
         
         <Subject>
           <NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">test@email.com</NameID>
         </Subject>
         

This is populated in the Firebase-issued ID token and in the [UserInfo](https://firebase.google.com/docs/reference/js/auth.userinfo.md#userinfoemail) object.




Only service-provider initiated SAML flows from the client SDK are supported.

## Link user accounts

If a user has already signed in to your app using a different method (such as email/password), you can [link their existing account](https://docs.cloud.google.com/identity-platform/docs/link-accounts) to the SAML provider by using `linkWithPopup()` or `linkWithRedirect()`.

The following code snippet shows how to link a user's Google Account to the SAML provider:

### Web version 9
    
    
    import { getAuth, linkWithPopup, GoogleAuthProvider } from "firebase/auth";
    const provider = new GoogleAuthProvider();
    
    const auth = getAuth();
    linkWithPopup(auth.currentUser, provider).then((result) => {
      // Accounts successfully linked.
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const user = result.user;
      // ...
    }).catch((error) => {
      // Handle Errors here.
      // ...
    });
    
    [auth_link_with_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/auth_link_with_popup.js#L8-L20)

### Web version 8
    
    
    auth.currentUser.linkWithPopup(provider).then((result) => {
      // Accounts successfully linked.
      var credential = result.credential;
      var user = result.user;
      // ...
    }).catch((error) => {
      // Handle Errors here.
      // ...
    });
    
    [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L69-L77)

## What's next

  * [Signing in users with OIDC](https://docs.cloud.google.com/identity-platform/docs/web/oidc)
  * [Showing a custom domain during sign in](https://docs.cloud.google.com/identity-platform/docs/show-custom-domain)
  * [Managing OIDC and SAML providers programmatically](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
