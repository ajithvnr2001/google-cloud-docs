---
url: https://docs.cloud.google.com/iap/docs/create-custom-auth-ui/
title: Creating a custom sign-in page \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:57.462889+00:00
---

# Creating a custom sign-in page  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/create-custom-auth-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Creating a custom sign-in page Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to build your own authentication page using external identities and IAP. Constructing this page yourself gives you full control over the authentication flow and user experience.

If you don't need to fully customize your UI, you can let IAP [host a sign-in page for you](https://docs.cloud.google.com/iap/docs/cloud-run-sign-in), or use [FirebaseUI](https://docs.cloud.google.com/iap/docs/using-firebaseui) for a more streamlined experience.

## Overview

To build your own authentication page, follow these steps:

  1. [Enable external identities](https://docs.cloud.google.com/iap/docs/enable-external-identities). Select **I'll provide my own UI option** during setup.
  2. Install the `gcip-iap` library.
  3. Configure the UI by implementing the `AuthenticationHandler` interface.

Your authentication page must handle the following scenarios:

     * Tenant selection

     * User authorization

     * User sign in

     * Error handling

  4. Optional: Customize your authentication page with additional features, such as progress bars, sign out pages, and user processing.

  5. Test your UI.




## Install the gcip-iap library

To install the `gcip-iap` library, run the following command:
    
    
    npm install gcip-iap --save

The `gcip-iap` NPM module abstracts the communications between your application, IAP, and Identity Platform. This lets you customize the entire authentication flow without having to manage the underlying exchanges between the UI and IAP.

Use the correct imports for your SDK version:

###  gcip-iap v0.1.4 or earlier 
    
    
    // Import Firebase/GCIP dependencies. These are installed on npm install.
    import * as firebase from 'firebase/app';
    import 'firebase/auth';
    // Import GCIP/IAP module.
    import * as ciap from 'gcip-iap';
    

###  gcip-iap v1.0.0 to v1.1.0 

Starting with version v1.0.0, `gcip-iap` requires the `firebase` v9 peer dependency or greater. If you are migrating to `gcip-iap` v1.0.0 or above, complete the following actions:

  * Update the `firebase` version in your `package.json` file to v9.6.0+.
  * Update the `firebase` import statements as follows:


    
    
    // Import Firebase modules.
    import firebase from 'firebase/compat/app';
    import 'firebase/compat/auth';
    // Import the gcip-iap module.
    import * as ciap from 'gcip-iap';
    

No additional code changes are needed.

###  gcip-iap v2.0.0 

Starting with version v2.0.0, `gcip-iap` requires rewrite of your custom UI application using the [modular SDK format](https://cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade). If you are migrating to `gcip-iap` v2.0.0 or above, complete the following actions:

  * Update the `firebase` version in your `package.json` file to v9.8.3+.
  * Update the `firebase` import statements as follows:


    
    
      // Import Firebase modules.
      import { initializeApp } from 'firebase/app';
      import { getAuth, GoogleAuthProvider } 'firebase/auth';
      // Import the gcip-iap module.
      import * as ciap from 'gcip-iap';
    

## Configure the UI

To configure the UI, create a custom class that implements the `AuthenticationHandler` interface:
    
    
    interface AuthenticationHandler {
      languageCode?: string | null;
      getAuth(apiKey: string, tenantId: string | null): FirebaseAuth;
      startSignIn(auth: FirebaseAuth, match?: SelectedTenantInfo): Promise<UserCredential>;
      selectTenant?(projectConfig: ProjectConfig, tenantIds: string[]): Promise<SelectedTenantInfo>;
      completeSignOut(): Promise<void>;
      processUser?(user: User): Promise<User>;
      showProgressBar?(): void;
      hideProgressBar?(): void;
      handleError?(error: Error | CIAPError): void;
    }
    

During authentication, the library automatically calls `AuthenticationHandler`'s methods.

### Select tenants

To select a tenant, implement `selectTenant()`. You can implement this method to choose a tenant programmatically, or display a UI so the user can select one themselves.

In either case, the library uses the returned `SelectedTenantInfo` object to complete the authentication flow. It contains the ID of the selected tenant, any provider IDs, and the email the user entered.

If you have multiple tenants in your project, you must select one before you can authenticate a user. If you only have a single tenant, or are using project-level authentication, you don't need to implement `selectTenant()`.

IAP supports the same providers as Identity Platform, such as:

  * Email and password
  * OAuth (Google, Facebook, Twitter, GitHub, Microsoft, etc)
  * SAML
  * OIDC
  * Phone number
  * Custom
  * Anonymous



Phone number, custom, and anonymous authentication types are not supported for multi-tenancy.

#### Select tenants programmatically

To select a tenant programmatically, leverage the current context. The `Authentication` class contains `getOriginalURL()` that returns the URL the user was accessing before authentication.

Use this to locate a match from a list of associated tenants:
    
    
    // Select provider programmatically.
    selectTenant(projectConfig, tenantIds) {
      return new Promise((resolve, reject) => {
        // Show UI to select the tenant.
        auth.getOriginalURL()
          .then((originalUrl) => {
            resolve({
              tenantId: getMatchingTenantBasedOnVisitedUrl(originalUrl),
              // If associated provider IDs can also be determined,
              // populate this list.
              providerIds: [],
            });
          })
          .catch(reject);
      });
    }
    

#### Allow users to select tenants

To allow the user to select a tenant, display a list of tenants and have the user choose one, or ask them to enter their email address and then locate a match based on the domain:
    
    
    // Select provider by showing UI.
    selectTenant(projectConfig, tenantIds) {
      return new Promise((resolve, reject) => {
        // Show UI to select the tenant.
        renderSelectTenant(
            tenantIds,
            // On tenant selection.
            (selectedTenantId) => {
              resolve({
                tenantId: selectedTenantId,
                // If associated provider IDs can also be determined,
                // populate this list.
                providerIds: [],
                // If email is available, populate this field too.
                email: undefined,
              });
            });
      });
    }
    

### Authenticate users

After you have a provider, implement `getAuth()` to return an [Auth](https://firebase.google.com/docs/reference/js/auth.auth) instance, corresponding to the API key and tenant ID provided. If no tenant ID is provided, use project-level identity providers.

`getAuth()` tracks where the user corresponding to the provided configuration is stored. It also makes it possible to silently refresh a previously authenticated user's Identity Platform ID token without requiring the user to re-enter their credentials.

If you're using multiple IAP resources with different tenants, we recommended using a unique authentication instance for each resource. This allows multiple resources with different configurations to use the same authentication page. It also allows multiple users to sign in at the same time without logging out the previous user.

The following is an example of how to implement `getAuth()`:

###  gcip-iap v1.0.0
    
    
    getAuth(apiKey, tenantId) {
      let auth = null;
      // Make sure the expected API key is being used.
      if (apiKey !== expectedApiKey) {
        throw new Error('Invalid project!');
      }
      try {
        auth = firebase.app(tenantId || undefined).auth();
        // Tenant ID should be already set on initialization below.
      } catch (e) {
        // Use different App names for every tenant so that
        // multiple users can be signed in at the same time (one per tenant).
        const app = firebase.initializeApp(this.config, tenantId || '[DEFAULT]');
        auth = app.auth();
        // Set the tenant ID on the Auth instance.
        auth.tenantId = tenantId || null;
      }
      return auth;
    }
    

###  gcip-iap v2.0.0
    
    
    import {initializeApp, getApp} from 'firebase/app';
    import {getAuth} from 'firebase/auth';
    
    getAuth(apiKey, tenantId) {
      let auth = null;
      // Make sure the expected API key is being used.
      if (apiKey !== expectedApiKey) {
        throw new Error('Invalid project!');
      }
      try {
        auth = getAuth(getApp(tenantId || undefined));
        // Tenant ID should be already set on initialization below.
      } catch (e) {
        // Use different App names for every tenant so that
        // multiple users can be signed in at the same time (one per tenant).
        const app = initializeApp(this.config, tenantId || '[DEFAULT]');
        auth = getAuth(app);
        // Set the tenant ID on the Auth instance.
        auth.tenantId = tenantId || null;
      }
      return auth;
    }
    
    

### Sign in users

To handle sign in, implement `startSignIn()`, display a UI for the user to authenticate, and then return a [`UserCredential`](https://firebase.google.com/docs/reference/js/firebase.auth#usercredential) for the signed in user on completion.

**Note:** Even if your app only supports a single identity provider, consider requiring user interaction, such as a "Sign in" button, before starting the authentication flow. Redirecting immediately may cause Safari to incorrectly register the redirect as a bounce tracker. For more information, see [Intelligent Tracking Prevention](https://webkit.org/blog/8311/intelligent-tracking-prevention-2-0/).

In a multi-tenant environment, you can determine available authentication methods from `SelectedTenantInfo`, if it was provided. This variable contains the same information returned by `selectTenant()`.

The following example shows a `startSignIn()` implementation for an existing user with an email and password:

###  gcip-iap v1.0.0
    
    
    startSignIn(auth, selectedTenantInfo) {
      return new Promise((resolve, reject) => {
        // Show the UI to sign-in or sign-up a user.
        $('#sign-in-form').on('submit', (e) => {
          const email = $('#email').val();
          const password = $('#password').val();
          // Example: Ask the user for an email and password.
          // Note: The method of sign in may have already been determined from the
          // selectedTenantInfo object.
          auth.signInWithEmailAndPassword(email, password)
            .then((userCredential) => {
              resolve(userCredential);
            })
            .catch((error) => {
              // Show the error message.
            });
        });
      });
    }
    

###  gcip-iap v2.0.0
    
    
    import {signInWithEmailAndPassword} from 'firebase/auth';
    
    startSignIn(auth, selectedTenantInfo) {
      return new Promise((resolve, reject) => {
        // Show the UI to sign-in or sign-up a user.
        $('#sign-in-form').on('submit', (e) => {
          const email = $('#email').val();
          const password = $('#password').val();
          // Example: Ask the user for an email and password.
          // Note: The method of sign in may have already been determined from the
          // selectedTenantInfo object.
            signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
              resolve(userCredential);
            })
            .catch((error) => {
              // Show the error message.
            });
        });
      });
    }
    

You can also sign in users with a federated provider, such as SAML or OIDC, using a popup or redirect:

###  gcip-iap v1.0.0
    
    
    startSignIn(auth, selectedTenantInfo) {
      // Show the UI to sign-in or sign-up a user.
      return new Promise((resolve, reject) => {
        // Provide the user multiple buttons to sign-in.
        // For example sign-in with popup using a SAML provider.
        // Note: The method of sign in may have already been determined from the
        // selectedTenantInfo object.
        const provider = new firebase.auth.SAMLAuthProvider('saml.myProvider');
        auth.signInWithPopup(provider)
          .then((userCredential) => {
            resolve(userCredential);
          })
          .catch((error) => {
            // Show the error message.
          });
        // Using redirect flow. When the page redirects back and sign-in completes,
        // ciap will detect the result and complete sign-in without any additional
        // action.
        auth.signInWithRedirect(provider);
      });
    }
    

###  gcip-iap v2.0.0
    
    
    import {signInWithPopup, SAMLAuthProvider} from 'firebase/auth';
    
    startSignIn(auth, selectedTenantInfo) {
      // Show the UI to sign-in or sign-up a user.
      return new Promise((resolve, reject) => {
        // Provide the user multiple buttons to sign-in.
        // For example sign-in with popup using a SAML provider.
        // Note: The method of sign in might have already been determined from the
        // selectedTenantInfo object.
        const provider = new SAMLAuthProvider('saml.myProvider');
        signInWithPopup(auth, provider)
          .then((userCredential) => {
            resolve(userCredential);
          })
          .catch((error) => {
            // Show the error message.
          });
        // Using redirect flow. When the page redirects back and sign-in completes,
        // ciap will detect the result and complete sign-in without any additional
        // action.
        signInWithRedirect(auth, provider);
      });
    }
    

Some OAuth providers support passing a login hint for sign-in:

###  gcip-iap v1.0.0
    
    
    startSignIn(auth, selectedTenantInfo) {
      // Show the UI to sign-in or sign-up a user.
      return new Promise((resolve, reject) => {
        // Use selectedTenantInfo to determine the provider and pass the login hint
        // if that provider supports it and the user specified an email address.
        if (selectedTenantInfo &&
            selectedTenantInfo.providerIds &&
            selectedTenantInfo.providerIds.indexOf('microsoft.com') !== -1) {
          const provider = new firebase.auth.OAuthProvider('microsoft.com');
          provider.setCustomParameters({
            login_hint: selectedTenantInfo.email || undefined,
          });
        } else {
          // Figure out the provider used...
        }
        auth.signInWithPopup(provider)
          .then((userCredential) => {
            resolve(userCredential);
          })
          .catch((error) => {
            // Show the error message.
          });
        });
    }
    

###  gcip-iap v2.0.0
    
    
    import {signInWithPopup, OAuthProvider} from 'firebase/auth';
    
    startSignIn(auth, selectedTenantInfo) {
      // Show the UI to sign in or sign up a user.
      return new Promise((resolve, reject) => {
        // Use selectedTenantInfo to determine the provider and pass the login hint
        // if that provider supports it and the user specified an email address.
        if (selectedTenantInfo &&
            selectedTenantInfo.providerIds &&
            selectedTenantInfo.providerIds.indexOf('microsoft.com') !== -1) {
          const provider = new OAuthProvider('microsoft.com');
          provider.setCustomParameters({
            login_hint: selectedTenantInfo.email || undefined,
          });
        } else {
          // Figure out the provider used...
        }
        signInWithPopup(auth, provider)
          .then((userCredential) => {
            resolve(userCredential);
          })
          .catch((error) => {
            // Show the error message.
          });
        });
    }
    

See [Authenticating with multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-authentication) for more information.

### Handling errors

To display error messages to users or to attempt recovery from errors such as network timeouts, implement `handleError()`.

The following example implements `handleError()`:
    
    
    handleError(error) {
      showAlert({
        code: error.code,
        message: error.message,
        // Whether to show the retry button. This is only available if the error is
        // recoverable via retrial.
        retry: !!error.retry,
      });
      // When user clicks retry, call error.retry();
      $('.alert-link').on('click', (e) => {
        error.retry();
        e.preventDefault();
        return false;
      });
    }
    

The table below lists IAP specific error codes that can be returned. Identity Platform can also return errors; see the documentation for [`firebase.auth.Auth`](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth).

Error code | Description  
---|---  
`invalid-argument` | Client specified an invalid argument.  
`failed-precondition` | Request can not be executed in the current system state.  
`out-of-range` | Client specified an invalid range.  
`unauthenticated` | Request not authenticated due to a missing, invalid, or expired OAuth token.  
`permission-denied` | Client does not have sufficient permission, or the UI is hosted on an unauthorized domain.  
`not-found` . | Specified resource is not found.  
`aborted` | Concurrency conflict, such as read-modify-write conflict.  
`already-exists` | The resource that a client tried to create already exists.  
`resource-exhausted` | Either out of resource quota or reaching rate limiting.  
`cancelled` | Request cancelled by the client.  
`data-loss` | Unrecoverable data loss or data corruption.  
`unknown` | Unknown server error.  
`internal` | Internal server error.  
`not-implemented` | API method not implemented by the server.  
`unavailable` | Service unavailable.  
`restart-process` | Revisit the URL that redirected you to this page to restart the authentication process.  
`deadline-exceeded` | Request deadline exceeded.  
`authentication-uri-fail` | Failed to generate authentication URI.  
`gcip-token-invalid` | Invalid GCIP ID token provided.  
`gcip-redirect-invalid` | Invalid redirect URL.  
`get-project-mapping-fail` | Failed to get project ID.  
`gcip-id-token-encryption-error` | GCIP ID token encryption error.  
`gcip-id-token-decryption-error` | GCIP ID token decryption error.  
`gcip-id-token-unescape-error` | Web safe base64 unescape failed.  
`resource-missing-gcip-sign-in-url` | Missing GCIP authentication URL for the specified IAP resource.  
  
## Customizing the UI

You can customize your authentication page with optional features such as progress bars and sign out pages.

### Displaying a progress UI

To display a custom progress UI to the user whenever the `gcip-iap` module executes long-running network tasks, implement `showProgressBar()` and `hideProgressBar()`.

### Signing users out

In some cases, you may want to allow users to sign out from all current sessions that share the same authentication URL.

After a user signs out, there may be no URL to redirect them back to. This commonly occurs when a user signs out from all tenants associated with a sign-in page. In this case, implement `completeSignOut()` to display a message indicating the user logged out successfully. If you don't implement this method, a blank page appears when a user signs out.

### Processing users

To modify a signed in user before redirecting to the IAP resource, implement `processUser()`.

You can use this method to do the following:

  * Link to additional providers.
  * Update the user's profile.
  * Ask the user for additional data after registration.
  * Process OAuth access tokens returned by `getRedirectResult()` after calling `signInWithRedirect()`.



The following is an example of implementing `processUser()`:

###  gcip-iap v1.0.0
    
    
    processUser(user) {
      return lastAuthUsed.getRedirectResult().then(function(result) {
        // Save additional data, or ask the user for additional profile information
        // to store in database, etc.
        if (result) {
          // Save result.additionalUserInfo.
          // Save result.credential.accessToken for OAuth provider, etc.
        }
        // Return the user.
        return user;
      });
    }
    

###  gcip-iap v2.0.0
    
    
    import {getRedirectResult} from 'firebase/auth';
    
    processUser(user) {
      return getRedirectResult(lastAuthUsed).then(function(result) {
        // Save additional data, or ask the user for additional profile information
        // to store in database, etc.
        if (result) {
          // Save result.additionalUserInfo.
          // Save result.credential.accessToken for OAuth provider, etc.
        }
        // Return the user.
        return user;
      });
    }
    

If you want any changes to a user reflected in the ID token claims propagated by IAP to your app, you must force the token to refresh:

###  gcip-iap v1.0.0
    
    
    processUser(user) {
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
    

###  gcip-iap v2.0.0
    
    
    import {updateProfile} from 'firebase/auth';
    
    processUser(user) {
      return updateProfile(user, {
        photoURL: 'https://example.com/profile/1234/photo.png',
      }).then(function() {
        // To reflect updated photoURL in the ID token, force token
        // refresh.
        return user.getIdToken(true);
      }).then(function() {
        return user;
      });
    }
    

## Test the UI

After you've created a class that implements `AuthenticationHandler`, you can use it to create a new `Authentication` instance, and start it:
    
    
    // Implement interface AuthenticationHandler.
    // const authHandlerImplementation = ....
    const ciapInstance = new ciap.Authentication(authHandlerImplementation);
    ciapInstance.start();
    

Deploy your application and navigate to the authentication page. You should see your custom sign-in UI.

## What's next

  * Learn how to [access non-Google resources programmatically](https://docs.cloud.google.com/iap/docs/access-external-resources).
  * Learn about [managing sessions](https://docs.cloud.google.com/iap/docs/external-identity-sessions).
  * Learn how [external identities work with IAP](https://docs.cloud.google.com/iap/docs/external-identities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
