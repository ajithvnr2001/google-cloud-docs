---
url: https://docs.cloud.google.com/iap/docs/using-firebaseui/
title: Creating a sign-in page with FirebaseUI \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:50.593530+00:00
---

# Creating a sign-in page with FirebaseUI  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/using-firebaseui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Creating a sign-in page with FirebaseUI Stay organized with collections  Save and categorize content based on your preferences. 

To use external identities with Identity-Aware Proxy (IAP), your app needs a sign-in page. IAP will redirect users to this page to authenticate before they can access secure resources.

This article shows you how to build an authentication page using [FirebaseUI](https://github.com/firebase/firebaseui-web/blob/master/firebaseuihandler/README.md#iap-external-identities-support-with-firebaseui), an open-source JavaScript library. FirebaseUI provides customizable elements that help reduce boilerplate code, and handles the flows for signing in users with a wide range of identity providers.

To get started faster, let IAP [host the UI for you](https://docs.cloud.google.com/iap/docs/cloud-run-sign-in). This lets you try external identities without writing any additional code. For more advanced scenarios, you can also [build your own sign-in page from scratch](https://docs.cloud.google.com/iap/docs/create-custom-auth-ui). This option is more complex, but gives you full control over the authentication flow and user experience.

## Before you begin

[Enable external identities](https://docs.cloud.google.com/iap/docs/enable-external-identities), and select the **I'll provide my own UI** option during setup.

## Installing the libraries

Install the `gcip-iap`, `firebase`, and `firebaseui` libraries. The `gcip-iap` module abstracts communications between your app, IAP, and Identity Platform. The `firebase` and `firebaseui` libraries provide the building blocks for your authentication UI.
    
    
    npm install firebase --save
    npm install firebaseui --save
    npm install gcip-iap --save
    

Note that the `gcip-iap` module is not available using CDN.

You can then `import` the modules in your source files. Use the correct imports for your SDK version:

###  gcip-iap v0.1.4 or earlier 
    
    
    // Import firebase modules.
    import * as firebase from "firebase/app";
    import "firebase/auth";
    // Import firebaseui module.
    import * as firebaseui from 'firebaseui'
    // Import gcip-iap module.
    import * as ciap from 'gcip-iap';
    

###  gcip-iap v1.0.0 or later 

Starting with version v1.0.0, `gcip-iap` requires the `firebase` v9 peer dependency or greater. If you are migrating to `gcip-iap` v1.0.0 or above, complete the following actions:

  * Update the `firebase` and `firebaseui` versions in your `package.json` file to v9.6.0+ and v6.0.0+ respectively.
  * Update the `firebase` import statements as follows:


    
    
    // Import firebase modules.
    import firebase from 'firebase/compat/app';
    import 'firebase/compat/auth';
    // Import firebaseui module.
    import * as firebaseui from 'firebaseui'
    // Import gcip-iap module.
    

No additional code changes are needed.

For additional installation options, including using localized versions of the libraries, refer to the [instructions on GitHub](https://github.com/firebase/firebaseui-web/blob/master/firebaseuihandler/README.md#installation).

## Configuring your application

FirebaseUI uses a configuration object that specifies the tenants and providers to use for authentication. A full configuration can be very long, and might look something like this:
    
    
    // The project configuration.
    const configs = {
      // Configuration for project identified by API key API_KEY1.
      API_KEY1: {
        authDomain: 'project-id1.firebaseapp.com',
        // Decide whether to ask user for identifier to figure out
        // what tenant to select or whether to present all the tenants to select from.
        displayMode: 'optionFirst', // Or identifierFirst
        // The terms of service URL and privacy policy URL for the page
        // where the user select tenant or enter email for tenant/provider
        // matching.
        tosUrl: 'http://localhost/tos',
        privacyPolicyUrl: 'http://localhost/privacypolicy',
        callbacks: {
          // The callback to trigger when the selection tenant page
          // or enter email for tenant matching page is shown.
          selectTenantUiShown: () => {
            // Show title and additional display info.
          },
          // The callback to trigger when the sign-in page
          // is shown.
          signInUiShown: (tenantId) => {
            // Show tenant title and additional display info.
          },
          beforeSignInSuccess: (user) => {
            // Do additional processing on user before sign-in is
            // complete.
            return Promise.resolve(user);
          }
        },
        tenants: {
          // Tenant configuration for tenant ID tenantId1.
          tenantId1: {
            // Full label, display name, button color and icon URL of the
            // tenant selection button. Only needed if you are
            // using the option first option.
            fullLabel: 'ACME Portal',
            displayName: 'ACME',
            buttonColor: '#2F2F2F',
            iconUrl: '<icon-url-of-sign-in-button>',
             // Sign-in providers enabled for tenantId1.
            signInOptions: [
              // Microsoft sign-in.
              {
                provider: 'microsoft.com',
                providerName: 'Microsoft',
                buttonColor: '#2F2F2F',
                iconUrl: '<icon-url-of-sign-in-button>',
                loginHintKey: 'login_hint'
              },
              // Email/password sign-in.
              {
                provider: 'password',
                // Do not require display name on sign up.
                requireDisplayName: false,
                disableSignUp: {
                  // Disable user from signing up with email providers.
                  status: true,
                  adminEmail: 'admin@example.com',
                  helpLink: 'https://www.example.com/trouble_signing_in'
                }
              },
              // SAML provider. (multiple SAML providers can be passed)
              {
                provider: 'saml.my-provider1',
                providerName: 'SAML provider',
                fullLabel: 'Employee Login',
                buttonColor: '#4666FF',
                iconUrl: 'https://www.example.com/photos/my_idp/saml.png'
              },
            ],
            // If there is only one sign-in provider eligible for the user,
            // whether to show the provider selection page.
            immediateFederatedRedirect: true,
            signInFlow: 'redirect', // Or popup
            // The terms of service URL and privacy policy URL for the sign-in page
            // specific to each tenant.
            tosUrl: 'http://localhost/tenant1/tos',
            privacyPolicyUrl: 'http://localhost/tenant1/privacypolicy'
          },
          // Tenant configuration for tenant ID tenantId2.
          tenantId2: {
            fullLabel: 'OCP Portal',
            displayName: 'OCP',
            buttonColor: '#2F2F2F',
            iconUrl: '<icon-url-of-sign-in-button>',
            // Tenant2 supports a SAML, OIDC and Email/password sign-in.
            signInOptions: [
              // Email/password sign-in.
              {
                provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
                // Do not require display name on sign up.
                requireDisplayName: false
              },
              // SAML provider. (multiple SAML providers can be passed)
              {
                provider: 'saml.my-provider2',
                providerName: 'SAML provider',
                fullLabel: 'Contractor Portal',
                buttonColor: '#4666FF',
                iconUrl: 'https://www.example.com/photos/my_idp/saml.png'
              },
              // OIDC provider. (multiple OIDC providers can be passed)
              {
                provider: 'oidc.my-provider1',
                providerName: 'OIDC provider',
                buttonColor: '#4666FF',
                iconUrl: 'https://www.example.com/photos/my_idp/oidc.png'
              },
            ],
          },
          // Tenant configuration for tenant ID tenantId3.
          tenantId3: {
            fullLabel: 'Tenant3 Portal',
            displayName: 'Tenant3',
            buttonColor: '#007bff',
            iconUrl: '<icon-url-of-sign-in-button>',
            // Tenant3 supports a Google and Email/password sign-in.
            signInOptions: [
              // Email/password sign-in.
              {
                provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
                // Do not require display name on sign up.
                requireDisplayName: false
              },
              // Google provider.
              {
                provider: 'google.com',
                scopes: ['scope1', 'scope2', 'https://example.com/scope3'],
                loginHintKey: 'login_hint',
                customParameters: {
                  prompt: 'consent',
                },
              },
            ],
            // Sets the adminRestrictedOperation configuration for providers
            // including federated, email/password, email link and phone number.
            adminRestrictedOperation: {
              status: true,
              adminEmail: 'admin@example.com',
              helpLink: 'https://www.example.com/trouble_signing_in'
            }
          },
        },
      },
    };
    

The following sections provide guidance on how to configure some of the fields specific to IAP. For examples on setting other fields, see the code snippet above, or the [FirebaseUI documentation on GitHub](https://github.com/firebase/firebaseui-web/blob/master/README.md).

### Setting the API key

A typical configuration begins with an API key for your project:
    
    
    // The project configuration.
    const configs = {
      // Configuration for API_KEY.
      API_KEY: {
        // Config goes here
      }
    }
    

In most cases, you only need to specify a single API key. However, if you want to use a single authentication URL across multiple projects, you can include multiple API keys:
    
    
    const configs = {
      API_KEY1: {
        // Config goes here
      },
      API_KEY2: {
        // Config goes here
      },
    }
    

### Getting the authentication domain

Set the `authdomain` field to the domain provisioned to facilitate federated sign-in. You can retrieve this field from the [Identity Platform page in the Google Cloud console](https://console.cloud.google.com/customer-identity/).

### Specifying tenants IDs

A configuration requires a list of tenants and providers that users can authenticate with.

Each tenant is identified by its ID. If you're using project-level authentication (no tenants), use the special `_` identifier as an API key instead. For example:
    
    
    const configs = {
      // Configuration for project identified by API key API_KEY1.
      API_KEY1: {
        tenants: {
          // Project-level IdPs flow.
          _: {
            // Tenant config goes here
          },
          // Single tenant flow.
          1036546636501: {
            // Tenant config goes here
          }
        }
      }
    }
    

You can also specify a wildcard tenant configuration using the `*` operator. This tenant is used as a fallback if no matching ID is found.

### Configuring tenant providers

Each tenant has its own providers; these are specified in the `signInOptions` field:
    
    
    tenantId1: {
      signInOptions: [
        // Options go here
      ]
    }
    

See [Configuring sign-in providers](https://github.com/firebase/firebaseui-web#configuring-sign-in-providers) in the FirebaseUI documentation to learn how to configure providers.

In addition to the steps outlined in the FirebaseUI documentation, there are several fields specific to IAP that depend on the tenant selection mode you choose. See the next section for more information on these fields.

### Choosing a tenant selection mode

Users can select a tenant in two ways: **options-first mode** , or **identifier-first mode**.

In options mode, the user begins by selecting a tenant from a list, then enters their username and password. In identifier mode, the user enters their email first. The system then automatically selects the first tenant with an identity provider matching the email's domain.

To use options mode, set `displayMode` to `optionFirst`. You'll then need to provide configuration information for each tenant's button, including `displayName`, `buttonColor`, and `iconUrl`. An optional `fullLabel` can also be provided to override the entire button label instead of just the display name.

The following is an example of a tenant configured to use options mode:
    
    
    tenantId1: {
      fullLabel: 'ACME Portal',
      displayName: 'ACME',
      buttonColor: '#2F2F2F',
      iconUrl: '<icon-url-of-sign-in-button>',
      // ...
    

To use identifier mode, each sign-in option must specify an `hd` field indicating what domain it supports. This can be either a regex (such as `/@example\.com$/`) or the domain string (e.g., `example.com`).

The code below shows a tenant configured to use identifier mode:
    
    
    tenantId1: {
      signInOptions: [
        // Email/password sign-in.
        {
          hd: 'acme.com', // using regex: /@acme\.com$/
          // ...
        },
    

### Enabling immediate redirect

If your app only supports a single identity provider, setting `immediateFederatedRedirect` to `true` will skip the sign-in UI and redirect the user directly to the provider.

**Note:** This setting can lead to unexpected results for Safari users, as Safari may incorrectly interpret the redirect as a bounce tracker. For more information, see [Intelligent Tracking Prevention](https://webkit.org/blog/8311/intelligent-tracking-prevention-2-0/).

### Setting up callbacks

The configuration object contains a set of callbacks that are invoked at various points during the authentication flow. This lets you additionally customize the UI. The following hooks are available:

`selectTenantUiShown()` |  Triggered when the UI to select a tenant is shown. Use this if you want to modify the UI with a customized title or theme.   
---|---  
`signInUiShown(tenantId)` |  Triggered when a tenant is selected and the UI for the user to enter their credentials is shown. Use this if you want to modify the UI with a customized title or theme.   
`beforeSignInSuccess(user)` |  Triggered before sign-in completes. Use this to modify a signed in user before redirecting back to the IAP resource.   
  
The following example code shows how you might implement these callbacks:
    
    
    callbacks: {
      selectTenantUiShown: () => {
        // Show info of the IAP resource.
        showUiTitle(
            'Select your employer to access your Health Benefits');
      },
      signInUiShown: (tenantId) => {
        // Show tenant title and additional display info.
        const tenantName = getTenantNameFromId(tenantId);
        showUiTitle(`Sign in to access your ${tenantName} Health Benefits`);
      },
      beforeSignInSuccess: (user) => {
        // Do additional processing on user before sign-in is
        // complete.
        // For example update the user profile.
        return user.updateProfile({
          photoURL: 'https://example.com/profile/1234/photo.png',
        }).then(function() {
          // To reflect updated photoURL in the ID token, force token
          // refresh.
          return user.getIdToken(true);
        }).then(function() {
          return user;
        });
      }
    }
    

## Initializing the library

Once you've created a configuration object, follow these steps to initialize the library on your authentication page:

  1. Create an HTML container to render the UI in.
         
         <!DOCTYPE html>
         <html>
          <head>...</head>
          <body>
            <!-- The surrounding HTML is left untouched by FirebaseUI.
                 Your app may use that space for branding, controls and other
                 customizations.-->
            <h1>Welcome to My Awesome App</h1>
            <div id="firebaseui-auth-container"></div>
          </body>
         </html>
         

  2. Create a `FirebaseUiHandler` instance to render in the HTML container, and pass the `config` element you created to it.
         
         const configs = {
           // ...
         }
         const handler = new firebaseui.auth.FirebaseUiHandler(
           '#firebaseui-auth-container', configs);
         

  3. Create a new `Authentication` instance, pass the handler to it, and call `start()`.
         
         const ciapInstance = new ciap.Authentication(handler);
         ciapInstance.start();
         




Deploy your application and navigate to the authentication page. A sign-in UI containing your tenants and providers should appear.

## What's next

  * Learn how to [access non-Google resources programmatically](https://docs.cloud.google.com/iap/docs/access-external-resources).
  * Learn about [managing sessions](https://docs.cloud.google.com/iap/docs/external-identity-sessions).
  * Gain a deeper understanding of how [external identities work with IAP](https://docs.cloud.google.com/iap/docs/external-identities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
