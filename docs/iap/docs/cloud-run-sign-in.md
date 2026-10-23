---
url: https://docs.cloud.google.com/iap/docs/cloud-run-sign-in/
title: Hosting a sign-in page with Cloud Run \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:10.321613+00:00
---

# Hosting a sign-in page with Cloud Run  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/cloud-run-sign-in/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Hosting a sign-in page with Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

To use external identities with Identity-Aware Proxy (IAP), your app needs a sign-in page. IAP will redirect users to this page to authenticate before they can access secure resources.

This document shows you how to deploy and customize a prebuilt sign-in page using Cloud Run. This is the fastest way to get started with external identities, and doesn't require you to write any code.

You can also build a sign-in page yourself. Building your own page is more difficult, but increases your control over the authentication flow and user experience. See [Creating a sign-in page with FirebaseUI](https://docs.cloud.google.com/iap/docs/using-firebaseui) and [Creating a custom sign-in page](https://docs.cloud.google.com/iap/docs/create-custom-auth-ui) to learn more.

## Sign-in page limitations

You cannot use the prebuilt sign-in page if your project has [email enumeration protection](https://docs.cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) enabled.

If your project has email enumeration protection enabled, [disable email-enumeration-protection](https://docs.cloud.google.com/identity-platform/docs/admin/email-enumeration-protection#disable) before continuing with the procedures in this document.

**Note:** Starting June 24 2024, the sign-in page and `admin/` page might not work properly on browsers that disable third-party cookies tracking or implement storage partitioning. Follow Third-party Cookies and Storage Partitioning in Browsers for fixes.

## Before you begin

  * Enable the Compute Engine API.

[Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

  * [Enable external identities](https://docs.cloud.google.com/iap/docs/enable-external-identities), and select the **Create a sign-in page for me** option during setup. This lets Cloud Run and FirebaseUI create a sign-in page for you.

  * Ensure that the service account used by Cloud Run, PROJECT_NUMBER-compute@developer.gserviceaccount.com, has the following [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles):

    * `roles/identitytoolkit.viewer`
    * `roles/iap.settingsAdmin`
    * `roles/compute.networkViewer`



## Setting the Authorized Redirect URI for Identity Platform providers

If you use Identity Platform providers that require sign-in redirect (redirect to the external IdP sign-in page). You must add the hosted sign-in page's URL as an authorized redirect URL in your provider configuration.

For example, for a Google provider, you need to do the following:

  1. Copy the **Login URL** after selecting your IAP-secured application.

  2. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)  


  3. Add `LOGIN_URL/__/auth/handler` as one of the authorized redirect URIs for your app's OAuth 2.0 client. Select the same OAuth client ID that you used when configuring the Google provider.




For other SAML and OIDC providers, do the same by adding `LOGIN_URL/__/auth/handler` as the authorized redirect URI or ACS URL.

## Testing the sign-in page

The initial sign-in page created by IAP is fully functional. To test it:

  1. Navigate to a resource protected by IAP. You should be automatically redirected to the sign-in page.

  2. Select a tenant and provider to sign-in with. If you don't see any tenants or providers listed, make sure you've configured one using [Identity Platform](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email).

  3. Sign in with your credentials.




You should be redirected to the protected resource.

## Customizing the sign-in page

You can customize the sign-in page using a JSON configuration file. Some options include:

  * Adding a header and logo to the sign-in page.
  * Specifying the available tenants and providers.
  * Customizing the icons and styling of each tenant and provider button.
  * Adding links to your app's privacy policy and terms of service.



The following sections explain how to access and update the JSON configuration file.

### Obtaining an access token

In order to administer the sign-in page, you need a Google access token. The easiest way to obtain one is by enabling Google as a provider for Identity Platform. If your app already uses Google as an identity provider, you can skip this section.

**Warning:** These steps will allow users to sign in to your app using a Google account. If you don't want to allow this, disable Google as an identity provider after you've finished customizing the hosted UI.

  1. Go to the **Identity Platform Providers** page in the Google Cloud console.

[ Go to the Identity Platform Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add a Provider**.

  3. Select **Google** from the list of providers.

  4. Configure the **Web Client ID** and **Web Client Secret** :

     1. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)  


     2. Use an existing OAuth 2.0 client or create a new one. Configure the `Client ID` and `Client secret` to **Web Client ID** and **Web Client Secret**. Add `LOGIN_URL/__/auth/handler` as one of the authorized redirect URIs for the OAuth 2.0 client. The `LOGIN_URL` is the **Login URL** created by IAP after selecting the **Create a sign-in page for me** option. It can be found on the IAP page in the Google Cloud console, by selecting the IAP-secured resource.

  5. Click **Save** on both pages.




### Signing in to the admin panel

The JSON configuration for the sign-in page hosted by Cloud Run at `LOGIN_URL/admin` panel. The following steps show how to access the panel. Note that you'll need the Storage Admin (`roles/storage.admin`) role.

**Important:** If you don't sign in to the admin panel, then you might encounter the following error: `404 Response: The specified bucket does not exist`.

  1. Go to the **IAP** page in the Google Cloud console.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Select your resource from the list.

  3. Launch the URL listed under **Customize page** in the info panel. It should look something like `https://servicename-xyz-uc.a.run.app/admin`.

**Note:** If you see a warning indicating the app isn't verified yet, you can safely bypass it for development purposes. See [Exceptions to verification requirements](https://support.google.com/cloud/answer/9110914#exceptions-ver-reqts) to learn more.
  4. Sign in with the same Google account you used to configure IAP. A text editor containing the JSON configuration file appears.




### Modifying the configuration

The configuration schema for the sign-in page is based on [FirebaseUI](https://github.com/firebase/firebaseui-web/tree/master/firebaseuihandler), and inherits many of its properties. Instead of using the IAP created `LOGIN_URL` as the default authDomain, you can use `PROJECT_ID.firebaseapp.com`.

If you want to use `PROJECT_ID.firebaseapp.com` as your `authDomain`, change `signInFlow` as `popup` to avoid third-parity storage access issue on major browsers(See [Best practices for using signInWithRedirect on browsers that block third-party storage access](https://docs.cloud.google.com/identity-platform/docs/web/redirect-best-practices)). Additionally, following instructions in Setting Authorized Redirect URI for Identity Platform Providers  to add the `PROJECT_ID.firebaseapp.com/__/auth/handler` as one of the authorized redirect URIs or ACS URLs for the Identity Platform provider that users will sign in with.

The following code shows an example configuration with three tenants:
    
    
    {
      "AIzaSyC5DtmRUR...": {
        "authDomain": "awesomeco.firebaseapp.com",
        "displayMode": "optionFirst",
        "selectTenantUiTitle": "Awesome Company Portal",
        "selectTenantUiLogo": "https://awesome.com/abcd/logo.png",
        "styleUrl": "https://awesome.com/abcd/overrides/stylesheet.css",
        "tosUrl": "https://awesome.com/abcd/tos.html",
        "privacyPolicyUrl": "https://awesome.com/abcd/privacypolicy.html",
        "tenants": {
          "tenant-a-id": {
            "fullLabel": "Company A Portal",
            "displayName": "Company A",
            "iconUrl": "https://companya.com/img/icon.png",
            "logoUrl": "https://companya.com/img/logo.png",
            "buttonColor": "#007bff",
            "signInFlow": "popup",
            "signInOptions": [
              {
                "provider": "password",
                "requireDisplayName": false,
                "disableSignUp": {
                  "status": true,
                  "adminEmail": "admin@example.com",
                  "helpLink": "https://www.example.com/trouble_signing_in"
                }
              },
              "facebook.com",
              "google.com",
              "microsoft.com",
              {
                "provider": "saml.okta-cicp-app",
                "providerName": "Corp Account",
                "fullLabel": "Employee Corporate Login",
                "buttonColor": "#ff0000",
                "iconUrl": "https://companya.com/abcd/icon-1.png"
              },
              {
                "provider": "oidc.okta-oidc",
                "providerName": "Contractor Account",
                "fullLabel": "Contractor Account Portal",
                "buttonColor": "#00ff00",
                "iconUrl": "https://companya.com/abcd/icon-2.png"
              }
            ],
            "tosUrl": "https://companya.com/abcd/tos.html",
            "privacyPolicyUrl": "https://companya.com/abcd/privacypolicy.html"
          },
          "tenant-b-id": {
            "fullLabel": "Company B Portal",
            "displayName": "Company B",
            "iconUrl": "https://companyb.com/img/icon.png",
            "logoUrl": "https://companyb.com/img/logo.png",
            "buttonColor": "#007bff",
            "immediateFederatedRedirect": true,
            "signInFlow": "popup",
            "signInOptions": [
              {
                "provider": "saml.okta-bla-app",
                "providerName": "Corp Account",
                "buttonColor": "#0000ff",
                "iconUrl": "https://companyb.com/abcd/icon.png"
              }
            ],
            "tosUrl": "https://companyb.com/abcd/tos.html",
            "privacyPolicyUrl": "https://companyb.com/abcd/privacypolicy.html"
          },
          "tenant-c-id": {
            "fullLabel": "Company C Portal",
            "displayName": "Company C",
            "iconUrl": "https://companyc.com/img/icon.png",
            "logoUrl": "https://companyc.com/img/logo.png",
            "buttonColor": "#007bff",
            "immediateFederatedRedirect": true,
            "signInFlow": "popup",
            "signInOptions": [
              {
                "provider": "password",
                "requireDisplayName": false
              },
              {
                "provider": "google.com",
                "scopes": ["scope1", "scope2", "https://example.com/scope3"],
                "loginHintKey": "login_hint",
                "customParameters": {
                  "prompt": "consent",
                },
              }
            ],
            "tosUrl": "https://companyc.com/abcd/tos.html",
            "privacyPolicyUrl": "https://companyc.com/abcd/privacypolicy.html",
            "adminRestrictedOperation": {
              "status": true,
              "adminEmail": "admin@example.com",
              "helpLink": "https://www.example.com/trouble_signing_in"
            }
          },
        }
      }
    }
    

For a complete list of available properties, see the [reference documentation](https://docs.cloud.google.com/iap/docs/reference/ui-config).

### Overriding CSS

You can use the `styleUrl` property to specify a custom CSS file. Styles in this file will override the default CSS. The file must be publicly accessible using HTTPS (for example, hosted in a Cloud Storage bucket).

The following example demonstrates overriding the default CSS:
    
    
    /** Change header title style. */
    .heading-center {
      color: #7181a5;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 20px;
      font-weight: bold;
    }
    
    /** Use round edged borders for container. */
    .main-container {
      border-radius: 5px;
    }
    
    /** Change page background color. */
    body {
      background-color: #e6eaf0;
    }
    

## Redeploying the Cloud Run service

In some cases, you might want to redeploy the Cloud Run service that hosts the sign-in page. Example scenarios include:

  * Adding, modifying, or removing identity providers
  * Modifying tenant configurations
  * Setting environment variables
  * Updating the container image to the latest version



Regularly updating and redeploying the container image ensures you have the latest bug fixes and security patches. You can view the list of changes between versions on [GitHub](https://github.com/GoogleCloudPlatform/iap-gcip-web-toolkit/tree/master/authui-container/CHANGELOG.md).

You can get the current version of the deployed container using the `/versionz` endpoint. For example:
    
    
    curl 'https://servicename-xyz-uc.a.run.app/versionz'
    

To redeploy the Cloud Run service:

  1. Go to the **Cloud Run** page in the Google Cloud console.

[ Go to the Cloud Run page](https://console.cloud.google.com/run)

  2. Select the service that hosts the sign-in page.

  3. Click **Edit & Deploy New Revision**.

  4. Optionally, specify advanced settings for the revision, or add an environment variable by clicking the **Variables & Secrets** tab.

  5. Click **Deploy**.




## Advanced options

### Customizing the sign-in page programmatically

In addition to using the `/admin` console, you can update the JSON configuration programmatically.

To get the current configuration, use the `/get_admin_config` endpoint. For example:
    
    
    curl -H 'Authorization: Bearer [TOKEN]'
      'https://servicename-xyz-uc.a.run.app/get_admin_config'
    

To update the configuration, use `/set_admin_config`. For example:
    
    
    curl -XPOST -H 'Authorization: Bearer [TOKEN]' -H "Content-type: application/json"
      -d '[UPDATED-CONFIG]' 'https://servicename-xyz-uc.a.run.app/set_admin_config'
    

Both REST calls require the `https://www.googleapis.com/auth/devstorage.read_write` scope, and a valid OAuth token must be attached to the `Authorization` header.

### Setting environment variables

You can set environment variables on the Cloud Run service to customize advanced settings. The following table lists the available variables:

Variable | Description  
---|---  
`DEBUG_CONSOLE` |  A boolean value (`0` or `1`) indicating whether to log all network request errors and details. Sensitive data will not be logged. Disabled (`0`) by default.   
`UI_CONFIG` |  A string containing the JSON configuration for the sign-in page. Using this variable instead of the `/admin` panel avoids reading and writing to a Cloud Storage when accessing the configuration. Invalid configurations are ignored. Using the `/admin` panel to validate your JSON before setting this variable can help minimize syntax errors.   
`GCS_BUCKET_NAME` |  A string overriding the default Cloud Storage bucket used to store the JSON configuration. The file is named `config.json`, and the default location is `gcip-iap-bucket-[CLOUD-RUN-SERVICE-NAME]-[PROJECT-NUMBER]`.   
`ALLOW_ADMIN` |  A boolean value (`0` or `1`) indicating whether to allow access to the `/admin` configuration panel. Enabled (`1`) by default.   
  
You'll need to deploy a new revision of the Cloud Run service after updating variables before the changes take effect. To learn more about environment variables, see the [Cloud Run documentation](https://docs.cloud.google.com/run/docs/configuring/environment-variables).

### Customizing the domain

By default, users will see the URL of the Cloud Run service when signing in. To specify a custom domain instead:

  1. Follow the steps in [Mapping custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains) to set a custom domain for the Cloud Run service.

  2. Configure IAP to use the new authentication URL:

     1. Go to the **IAP** page in the Google Cloud console.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

     2. Select the resource protected by IAP.

     3. In the side panel, select the **Edit** icon next to the **Login URL** field.

     4. Select **Use an existing hosted sign-in page** , and choose your domain from the drop-down menu.

     5. Click **Save**.




### Using one sign-in page for multiple IAP resources

You can protect multiple IAP resources using the same sign-in page. This reduces the work associated with managing multiple configurations.

To re-use a sign-in page:

  1. Follow the steps in this article to deploy the authentication page for the first resource protected by IAP.

  2. Enable IAP for the second resource. When prompted to specify a sign-in page, select **I'll provide my own** , and enter the URL of the Cloud Run service as the **URL**.

  3. Redeploy the Cloud Run service.




## Troubleshooting

### Service unavailable with hosted sign-in page

When using hosted sign-in page, you receive the following error:
    
    
    Service unavailable
    

You are then unable to access the sign-in page.

To resolve this error, do the following:

  1. Verify that the default Cloud Storage bucket is in the format `gcip-iap-bucket-CLOUD_RUN_SERVICE_NAME-PROJECT-NUMBER`.

  2. Verify that the default Cloud Storage bucket exists and contains a file named `config.json`.

**Note:** If the bucket or `config.json` file is missing, it means that the initial configuration wasn't saved. To create them, visit the `/admin` page and save the configuration file.



### Third-party cookies and storage partitioning in browsers

For browsers that disable third-party cookies or implement storage partitioning, the login page or the `admin/` page might not work properly. To resolve this issue, do the following:

  1. [Redeploy the sign-in page](https://docs.cloud.google.com/iap/docs/cloud-run-sign-in#redeploy) to use the latest version 1.0.1.

  2. If you customize the sign-in page, make sure that `authDomain` is set as the `LOGIN_URL` that IAP created. Alternatively, if the `signInFlow` is set to `popup`, you can set the `authDomain` to `PROJECT_ID.firebaseapp.com`.

The following snippet shows the configuration of `authDomain` for a custom sign-in page:
         
         {
           "AIzaSyC5DtmRUR...": {
             "authDomain": "LOGIN_URL",
             ...
           }
         }
         

The following snippet describes the `authDomain` for a `popup` sign-in page:
         
         {
           "AIzaSyC5DtmRUR...": {
             "authDomain": "PROJECT_ID.firebaseapp.com",
             "tenants": {
               "tenant-a-id": {
                 ...
                 "signInFlow": "popup"
                 ...
               }
             }
             ...
           }
         }
         




## What's next

  * [Create an authentication UI with FirebaseUI](https://docs.cloud.google.com/iap/docs/using-firebaseui).
  * [Create a custom authentication UI](https://docs.cloud.google.com/iap/docs/create-custom-auth-ui).
  * Gain a deeper understanding of how [external identities work with IAP](https://docs.cloud.google.com/iap/docs/external-identities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
