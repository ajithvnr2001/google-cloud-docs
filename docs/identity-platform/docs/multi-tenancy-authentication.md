---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-authentication/
title: Authenticating with multi-tenancy \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:14.982180+00:00
---

# Authenticating with multi-tenancy  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticating with multi-tenancy

This document shows you how to authenticate users in a multi-tenant Identity Platform environment.

## Before you begin

Make sure you've enabled multi-tenancy for your project and configured your tenants. See [Getting started with multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart) to learn how.

You'll also need to add the Client SDK to your app:

  1. Go to the Identity Platform page in the Google Cloud console.  
[Go to the Identity Platform users page](https://console.cloud.google.com/customer-identity/users)  


  2. On the top right, click **Application setup details**.

  3. Copy the code into your web app. For example:




### Web version 9
    
    
    import { initializeApp } from "firebase/app";
    
    const firebaseConfig = {
      apiKey: "...",
      // By default, authDomain is '[YOUR_APP].firebaseapp.com'.
      // You may replace it with a custom domain.
      authDomain: '[YOUR_CUSTOM_DOMAIN]'
    };
    const firebaseApp = initializeApp(firebaseConfig);
    
    [auth_init_custom_domain.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/index/auth_init_custom_domain.js#L8-L16)

### Web version 8
    
    
    firebase.initializeApp({
      apiKey: '...',
      // By default, authDomain is '[YOUR_APP].firebaseapp.com'.
      // You may replace it with a custom domain.
      authDomain: '[YOUR_CUSTOM_DOMAIN]'
    });
    
    [index.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/index.js#L107-L112)

## Sign in with tenants

To sign in to a tenant, the tenant ID needs to be passed to the `auth` object. Note that `tenantId` is not persisted on page reloads.

### Web version 9
    
    
    import { getAuth } from "firebase/auth";
    const auth = getAuth();
    const tenantId = "TENANT_ID1";
    auth.tenantId = tenantId;
    
    [multitenant_set_tenant.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_set_tenant.js#L8-L11)

### Web version 8
    
    
    const tenantId = "TENANT_ID1";
    firebase.auth().tenantId = tenantId;
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L9-L10)

Any future sign-in requests from this `auth` instance will include the tenant ID (`TENANT_ID1` in the preceding example) until you change or reset the tenant ID.

You can work with multiple tenants using single or multiple `auth` instances.

To use a single `auth` instance, modify the `tenantId` property whenever you want to switch between tenants. To revert back to project-level IdPs, set `tenantId` to `null`:

### Web version 9
    
    
    // One Auth instance
    // Switch to tenant1
    auth.tenantId = "TENANT_ID1";
    // Switch to tenant2
    auth.tenantId = "TENANT_ID2";
    // Switch back to project level IdPs
    auth.tenantId = null;
    
    [multitenant_switch_tenant.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_switch_tenant.js#L8-L14)

### Web version 8
    
    
    // One Auth instance
    // Switch to tenant1
    firebase.auth().tenantId = "TENANT_ID1";
    // Switch to tenant2
    firebase.auth().tenantId = "TENANT_ID2";
    // Switch back to project level IdPs
    firebase.auth().tenantId = null;
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L16-L22)

To use multiple instances, create a new `auth` instance for each tenant and assign them different IDs:

### Web version 9
    
    
    // Multiple Auth instances
    import { initializeApp } from "firebase/app";
    import { getAuth } from "firebase/auth";
    const firebaseApp1 = initializeApp(firebaseConfig1, 'app1_for_tenantId1');
    const firebaseApp2 = initializeApp(firebaseConfig2, 'app2_for_tenantId2');
    
    const auth1 = getAuth(firebaseApp1);
    const auth2 = getAuth(firebaseApp2);
    
    auth1.tenantId = "TENANT_ID1";
    auth2.tenantId = "TENANT_ID2";
    
    [multitenant_switch_tenant_multiinstance.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_switch_tenant_multiinstance.js#L8-L18)

### Web version 8
    
    
    // Multiple Auth instances
    firebase.initializeApp(config, 'app1_for_tenantId1');
    firebase.initializeApp(config, 'app2_for_tenantId2');
    
    const auth1 = firebase.app('app1').auth();
    const auth2 = firebase.app('app2').auth();
    
    auth1.tenantId = "TENANT_ID1";
    auth2.tenantId = "TENANT_ID2";
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L28-L36)

After signing in with a tenant, a tenant user will be returned with `user.tenantId` set to that tenant. Note that if you switch `tenantId` on the `auth` instance later, the `currentUser` property will not change; it will still point to the same user as the previous tenant.

### Web version 9
    
    
    import { signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";
    // Switch to TENANT_ID1
    auth.tenantId = 'TENANT_ID1';
    
    // Sign in with tenant
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // User is signed in.
        const user = userCredential.user;
        // user.tenantId is set to 'TENANT_ID1'.
        // Switch to 'TENANT_ID2'.
        auth.tenantId = 'TENANT_ID2';
        // auth.currentUser still points to the user.
        // auth.currentUser.tenantId is 'TENANT_ID1'.
      });
    
    // You could also get the current user from Auth state observer.
    onAuthStateChanged(auth, (user) => {
      if (user) {
        // User is signed in.
        // user.tenantId is set to 'TENANT_ID1'.
      } else {
        // No user is signed in.
      }
    });
    
    [multitenant_signin_password_demo.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signin_password_demo.js#L8-L32)

### Web version 8
    
    
    // Switch to TENANT_ID1
    firebase.auth().tenantId = 'TENANT_ID1';
    
    // Sign in with tenant
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((result) => {
        const user = result.user;
        // user.tenantId is set to 'TENANT_ID1'.
        // Switch to 'TENANT_ID2'.
        firebase.auth().tenantId = 'TENANT_ID2';
        // firebase.auth().currentUser still point to the user.
        // firebase.auth().currentUser.tenantId is 'TENANT_ID1'.
      });
    
    // You could also get the current user from Auth state observer.
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        // User is signed in.
        // user.tenantId is set to 'TENANT_ID1'.
      } else {
        // No user is signed in.
      }
    });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L42-L64)

## Email/password accounts

The following example shows how to register a new user:

### Web version 9
    
    
    import { createUserWithEmailAndPassword } from "firebase/auth";
    auth.tenantId = 'TENANT_ID';
    
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // User is signed in.
        // userCredential.user.tenantId is 'TENANT_ID'.
      }).catch((error) => {
        // Handle / display error.
        // ...
      });
    
    [multitenant_signup_password.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signup_password.js#L8-L18)

### Web version 8
    
    
    firebase.auth().tenantId = 'TENANT_ID';
    
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then((result) => {
        // result.user.tenantId is 'TENANT_ID'.
      }).catch((error) => {
        // Handle error.
      });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L70-L77)

To sign in an existing user:

### Web version 9
    
    
    import { signInWithEmailAndPassword } from "firebase/auth";
    auth.tenantId = 'TENANT_ID';
    
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // User is signed in.
        // userCredential.user.tenantId is 'TENANT_ID'.
      }).catch((error) => {
        // Handle / display error.
        // ...
      });
    
    [multitenant_signin_password.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signin_password.js#L8-L18)

### Web version 8
    
    
    firebase.auth().tenantId = 'TENANT_ID';
    
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((result) => {
        // result.user.tenantId is 'TENANT_ID'.
      }).catch((error) => {
        // Handle error.
      });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L84-L91)

## SAML

To sign in with a SAML provider, instantiate a `SAMLAuthProvider` instance with the provider ID from the Google Cloud console:

### Web version 9
    
    
    import { SAMLAuthProvider } from "firebase/auth";
    
    const provider = new SAMLAuthProvider("saml.myProvider");
    
    [auth_saml_provider_create.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/saml/auth_saml_provider_create.js#L8-L10)

### Web version 8
    
    
    const provider = new firebase.auth.SAMLAuthProvider('saml.myProvider');
    
    [saml.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/saml.js#L9-L9)

You can then use either a popup or a redirect flow to sign in to the SAML provider.

  * Popup 

### Web version 9
        
        import { signInWithPopup } from "firebase/auth";
        // Switch to TENANT_ID1.
        auth.tenantId = 'TENANT_ID1';
        
        // Sign-in with popup.
        signInWithPopup(auth, provider)
          .then((userCredential) => {
            // User is signed in.
            const user = userCredential.user;
            // user.tenantId is set to 'TENANT_ID1'.
            // Provider data available from the result.user.getIdToken()
            // or from result.user.providerData
          })
          .catch((error) => {
            // Handle / display error.
            // ...
          });
        
        [multitenant_signin_saml_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signin_saml_popup.js#L8-L24)

### Web version 8
        
        // Switch to TENANT_ID1.
        firebase.auth().tenantId = 'TENANT_ID1';
        
        // Sign-in with popup.
        firebase.auth().signInWithPopup(provider)
          .then((result) => {
            // User is signed in.
            // tenant ID is available in result.user.tenantId.
            // Identity provider data is available in result.additionalUserInfo.profile.
          })
          .catch((error) => {
            // Handle error.
          });
        
        [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L97-L109)

  * Redirect

### Web version 9
        
        import { signInWithRedirect, getRedirectResult } from "firebase/auth";
        // Switch to TENANT_ID1.
        auth.tenantId = 'TENANT_ID1';
        
        // Sign-in with redirect.
        signInWithRedirect(auth, provider);
        
        // After the user completes sign-in and returns to the app, you can get
        // the sign-in result by calling getRedirectResult. However, if they sign out
        // and sign in again with an IdP, no tenant is used.
        getRedirectResult(auth)
          .then((result) => {
            // User is signed in.
            // The tenant ID available in result.user.tenantId.
            // Provider data available from the result.user.getIdToken()
            // or from result.user.providerData
          })
          .catch((error) => {
            // Handle / display error.
            // ...
          });
        
        [multitenant_signin_saml_redirect.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signin_saml_redirect.js#L8-L28)

### Web version 8
        
        // Switch to TENANT_ID1.
        firebase.auth().tenantId = 'TENANT_ID1';
        
        // Sign-in with redirect.
        firebase.auth().signInWithRedirect(provider);
        
        // After the user completes sign-in and returns to the app, you can get
        // the sign-in result by calling getRedirectResult. However, if they sign out
        // and sign in again with an IdP, no tenant is used.
        firebase.auth().getRedirectResult()
          .then((result) => {
            // User is signed in.
            // The tenant ID available in result.user.tenantId.
            // Identity provider data is available in result.additionalUserInfo.profile.
          })
          .catch((error) => {
            // Handle error.
          });
        
        [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L115-L132)




In both cases, be sure to set the correct tenant ID on the `auth` instance.

## Email link

To initiate the authentication flow, display an interface prompting the user to provide their email address, then call `sendSignInLinkToEmail` to send them an authentication link. Make sure to set the correct tenant ID on the `auth` instance before sending the email.

### Web version 9
    
    
    import { sendSignInLinkToEmail } from "firebase/auth";
    // Switch to TENANT_ID1
    auth.tenantId = 'TENANT_ID1';
    
    sendSignInLinkToEmail(auth, email, actionCodeSettings)
      .then(() => {
        // The link was successfully sent. Inform the user.
        // Save the email locally so you don't need to ask the user for it again
        // if they open the link on the same device.
        window.localStorage.setItem('emailForSignIn', email);
      })
      .catch((error) => {
        // Handle / display error.
        // ...
      });
    
    [multitenant_send_emaillink.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_send_emaillink.js#L8-L22)

### Web version 8
    
    
    // Switch to TENANT_ID1
    firebase.auth().tenantId = 'TENANT_ID1';
    
    firebase.auth().sendSignInLinkToEmail(email, actionCodeSettings)
      .then(() => {
        // The link was successfully sent. Inform the user.
        // Save the email locally so you don't need to ask the user for it again
        // if they open the link on the same device.
        window.localStorage.setItem('emailForSignIn', email);
      })
      .catch((error) => {
        // Some error occurred, you can inspect the code: error.code
      });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L138-L150)

To complete sign-in on the landing page, first parse the tenant ID from the email link and set it on the `auth` instance. Then call `signInWithEmailLink` with the user's email and the actual email link containing the one-time code.

### Web version 9
    
    
    import { isSignInWithEmailLink, parseActionCodeURL, signInWithEmailLink } from "firebase/auth";
    if (isSignInWithEmailLink(auth, window.location.href)) {
      const actionCodeUrl = parseActionCodeURL(window.location.href);
      if (actionCodeUrl.tenantId) {
        auth.tenantId = actionCodeUrl.tenantId;
      }
      let email = window.localStorage.getItem('emailForSignIn');
      if (!email) {
        // User opened the link on a different device. To prevent session fixation
        // attacks, ask the user to provide the associated email again. For example:
        email = window.prompt('Please provide your email for confirmation');
      }
      // The client SDK will parse the code from the link for you.
      signInWithEmailLink(auth, email, window.location.href)
        .then((result) => {
          // User is signed in.
          // tenant ID available in result.user.tenantId.
          // Clear email from storage.
          window.localStorage.removeItem('emailForSignIn');
        });
    }
    
    [multitenant_signin_emaillink.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signin_emaillink.js#L8-L28)

### Web version 8
    
    
    if (firebase.auth().isSignInWithEmailLink(window.location.href)) {
      const actionCodeUrl = firebase.auth.ActionCodeURL.parseLink(window.location.href);
      if (actionCodeUrl.tenantId) {
        firebase.auth().tenantId = actionCodeUrl.tenantId;
      }
      let email = window.localStorage.getItem('emailForSignIn');
      if (!email) {
        // User opened the link on a different device. To prevent session fixation
        // attacks, ask the user to provide the associated email again. For example:
        email = window.prompt('Please provide your email for confirmation');
      }
      firebase.auth().signInWithEmailLink(email, window.location.href)
        .then((result) => {
          // User is signed in.
          // tenant ID available in result.user.tenantId.
        });
    }
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L156-L172)

## Creating custom tokens

Creating a multi-tenant aware custom token is identical to creating a regular custom token; as long as the correct tenant ID has been set on the `auth` instance, a top-level `tenant_id` claim will be added to the resulting JWT. See [Creating custom tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens) for detailed instructions on how to create and use custom tokens.

The following example shows how to create a custom token using the Admin SDK:

### Web version 9
    
    
    // Ensure you're using a tenant-aware auth instance
    const tenantManager = admin.auth().tenantManager();
    const tenantAuth = tenantManager.authForTenant('TENANT_ID1');
    
    // Create a custom token in the usual manner
    tenantAuth.createCustomToken(uid)
      .then((customToken) => {
        // Send token back to client
      })
      .catch((error) => {
        console.log('Error creating custom token:', error);
      });
    
    [multitenant_create_custom_token.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_create_custom_token.js#L8-L19)

### Web version 8
    
    
    // Ensure you're using a tenant-aware auth instance
    const tenantManager = admin.auth().tenantManager();
    const tenantAuth = tenantManager.authForTenant('TENANT_ID1');
    
    // Create a custom token in the usual manner
    tenantAuth.createCustomToken(uid)
      .then((customToken) => {
        // Send token back to client
      })
      .catch((error) => {
        console.log('Error creating custom token:', error);
      });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L178-L189)

The following code demonstrates how to sign in using a custom token:

### Web version 9
    
    
    import { signInWithCustomToken } from "firebase/auth";
    auth.tenantId = 'TENANT_ID1';
    
    signInWithCustomToken(auth, token)
      .catch((error) => {
        // Handle / display error.
        // ...
      });
    
    [multitenant_signin_custom_token.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_signin_custom_token.js#L8-L15)

### Web version 8
    
    
    firebase.auth().tenantId = 'TENANT_ID1';
    
    firebase.auth().signInWithCustomToken(token)
      .catch((error) => {
        // Handle Errors here.
        const errorCode = error.code;
        const errorMessage = error.message;
        // ...
      });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L195-L203)

Note that if the tenant IDs do not match, the `signInWithCustomToken()` method will fail.

## Linking multi-tenant user credentials

You can link other types of credentials to an existing multi-tenant user. For example, if a user previously authenticated with a SAML provider in a tenant, you can add email/password sign-in to their existing account so they can use either method to sign in to the tenant.

### Web version 9
    
    
    import { signInWithPopup, EmailAuthProvider, linkWithCredential, SAMLAuthProvider, signInWithCredential } from "firebase/auth";
    // Switch to TENANT_ID1
    auth.tenantId = 'TENANT_ID1';
    
    // Sign-in with popup
    signInWithPopup(auth, provider)
      .then((userCredential) => {
        // Existing user with e.g. SAML provider.
        const prevUser = userCredential.user;
        const emailCredential =
          EmailAuthProvider.credential(email, password);
        return linkWithCredential(prevUser, emailCredential)
          .then((linkResult) => {
            // Sign in with the newly linked credential
            const linkCredential = SAMLAuthProvider.credentialFromResult(linkResult);
            return signInWithCredential(auth, linkCredential);
          })
          .then((signInResult) => {
            // Handle sign in of merged user
            // ...
          });
      })
      .catch((error) => {
        // Handle / display error.
        // ...
      });
    
    [multitenant_account_linking.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_account_linking.js#L8-L33)

### Web version 8
    
    
    // Switch to TENANT_ID1
    firebase.auth().tenantId = 'TENANT_ID1';
    
    // Sign-in with popup
    firebase.auth().signInWithPopup(provider)
      .then((result) => {
        // Existing user with e.g. SAML provider.
        const user = result.user;
        const emailCredential =
          firebase.auth.EmailAuthProvider.credential(email, password);
        return user.linkWithCredential(emailCredential);
      })
      .then((linkResult) => {
        // The user can sign in with both SAML and email/password now.
      });
    
    [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L209-L223)

When linking or re-authenticating an existing multi-tenant user, `auth.tenantId` will be ignored; use `user.tenantId` to specify which tenant to use. This also applies to other user management APIs, such as `updateProfile` and `updatePassword`.

## Handling the account-exists-with-different-credential errors

If you enabled the **Link accounts that use the same email** setting in Google Cloud console, when a user tries to sign in to a provider (such as SAML) with an email that already exists for another provider (such as Google), the error `auth/account-exists-with-different-credential` is thrown (along with an `AuthCredential` object).

To finish signing in with the intended provider, the user must first sign in to the existing provider (Google), then link to the former `AuthCredential` (SAML).

You can use either a popup or redirect flow to handle this error.

  * Popup

### Web version 9
        
        import { signInWithPopup, fetchSignInMethodsForEmail, linkWithCredential } from "firebase/auth";
        // Step 1.
        // User tries to sign in to the SAML provider in that tenant.
        auth.tenantId = 'TENANT_ID';
        signInWithPopup(auth, samlProvider)
          .catch((error) => {
            // An error happened.
            if (error.code === 'auth/account-exists-with-different-credential') {
              // Step 2.
              // User's email already exists.
              // The pending SAML credential.
              const pendingCred = error.credential;
              // The credential's tenantId if needed: error.tenantId
              // The provider account's email address.
              const email = error.customData.email;
              // Get sign-in methods for this email.
              fetchSignInMethodsForEmail(email, auth)
                .then((methods) => {
                  // Step 3.
                  // Ask the user to sign in with existing Google account.
                  if (methods[0] == 'google.com') {
                    signInWithPopup(auth, googleProvider)
                      .then((result) => {
                        // Step 4
                        // Link the SAML AuthCredential to the existing user.
                        linkWithCredential(result.user, pendingCred)
                          .then((linkResult) => {
                            // SAML account successfully linked to the existing
                            // user.
                            goToApp();
                          });
                      });
                  }
                });
            }
          });
        
        [multitenant_account_exists_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_account_exists_popup.js#L8-L43)

### Web version 8
        
        // Step 1.
        // User tries to sign in to the SAML provider in that tenant.
        firebase.auth().tenantId = 'TENANT_ID';
        firebase.auth().signInWithPopup(samlProvider)
          .catch((error) => {
            // An error happened.
            if (error.code === 'auth/account-exists-with-different-credential') {
              // Step 2.
              // User's email already exists.
              // The pending SAML credential.
              const pendingCred = error.credential;
              // The credential's tenantId if needed: error.tenantId
              // The provider account's email address.
              const email = error.email;
              // Get sign-in methods for this email.
              firebase.auth().fetchSignInMethodsForEmail(email)
                .then((methods) => {
                  // Step 3.
                  // Ask the user to sign in with existing Google account.
                  if (methods[0] == 'google.com') {
                    firebase.auth().signInWithPopup(googleProvider)
                      .then((result) => {
                        // Step 4
                        // Link the SAML AuthCredential to the existing user.
                        result.user.linkWithCredential(pendingCred)
                          .then((linkResult) => {
                            // SAML account successfully linked to the existing
                            // user.
                            goToApp();
                          });
                      });
                  }
                });
            }
          });
        
        [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L229-L263)

  * Redirect

When using `signInWithRedirect`, `auth/account-exists-with-different-credential` errors will be raised in `getRedirectResult` when finishing the redirect flow.

The error object contains the property `error.tenantId`. Since the tenant ID on the `auth` instance is not persisted after redirecting, you'll need to set the tenant ID from the error object to the `auth` instance.

The following example shows how to handle the error:

### Web version 9
        
        import { signInWithRedirect, getRedirectResult, fetchSignInMethodsForEmail, linkWithCredential } from "firebase/auth";
        // Step 1.
        // User tries to sign in to SAML provider.
        auth.tenantId = 'TENANT_ID';
        signInWithRedirect(auth, samlProvider);
        var pendingCred;
        // Redirect back from SAML IDP. auth.tenantId is null after redirecting.
        getRedirectResult(auth).catch((error) => {
          if (error.code === 'auth/account-exists-with-different-credential') {
            // Step 2.
            // User's email already exists.
            const tenantId = error.tenantId;
            // The pending SAML credential.
            pendingCred = error.credential;
            // The provider account's email address.
            const email = error.customData.email;
            // Need to set the tenant ID again as the page was reloaded and the
            // previous setting was reset.
            auth.tenantId = tenantId;
            // Get sign-in methods for this email.
            fetchSignInMethodsForEmail(auth, email)
              .then((methods) => {
                // Step 3.
                // Ask the user to sign in with existing Google account.
                if (methods[0] == 'google.com') {
                  signInWithRedirect(auth, googleProvider);
                }
              });
          }
        });
        
        // Redirect back from Google. auth.tenantId is null after redirecting.
        getRedirectResult(auth).then((result) => {
          // Step 4
          // Link the SAML AuthCredential to the existing user.
          // result.user.tenantId is 'TENANT_ID'.
          linkWithCredential(result.user, pendingCred)
            .then((linkResult) => {
              // SAML account successfully linked to the existing
              // user.
              goToApp();
            });
        });
        
        [multitenant_account_exists_redirect.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/multi-tenancy/multitenant_account_exists_redirect.js#L8-L50)

### Web version 8
        
        // Step 1.
        // User tries to sign in to SAML provider.
        firebase.auth().tenantId = 'TENANT_ID';
        firebase.auth().signInWithRedirect(samlProvider);
        var pendingCred;
        // Redirect back from SAML IDP. auth.tenantId is null after redirecting.
        firebase.auth().getRedirectResult().catch((error) => {
          if (error.code === 'auth/account-exists-with-different-credential') {
            // Step 2.
            // User's email already exists.
            const tenantId = error.tenantId;
            // The pending SAML credential.
            pendingCred = error.credential;
            // The provider account's email address.
            const email = error.email;
            // Need to set the tenant ID again as the page was reloaded and the
            // previous setting was reset.
            firebase.auth().tenantId = tenantId;
            // Get sign-in methods for this email.
            firebase.auth().fetchSignInMethodsForEmail(email)
              .then((methods) => {
                // Step 3.
                // Ask the user to sign in with existing Google account.
                if (methods[0] == 'google.com') {
                  firebase.auth().signInWithRedirect(googleProvider);
                }
              });
          }
        });
        
        // Redirect back from Google. auth.tenantId is null after redirecting.
        firebase.auth().getRedirectResult().then((result) => {
          // Step 4
          // Link the SAML AuthCredential to the existing user.
          // result.user.tenantId is 'TENANT_ID'.
          result.user.linkWithCredential(pendingCred)
            .then((linkResult) => {
              // SAML account successfully linked to the existing
              // user.
              goToApp();
            });
        });
        
        [multi-tenancy.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/multi-tenancy.js#L269-L310)




## Disabling end-user account creation and deletion

There are situations where you want administrators to create user accounts instead of the accounts being created through user actions. In these cases, you can disable user actions via our REST API:
    
    
    curl --location --request PATCH 'https://identitytoolkit.googleapis.com/v2/projects/PROJECT_ID/tenants/TENANT_ID?updateMask=client' \
      --header 'Authorization: Bearer AUTH_TOKEN' \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "client": {
            "permissions": {
                "disabled_user_signup": true,
                "disabled_user_deletion": true
            }
        }
    }'
    

Replace the following:

  * `AUTH_TOKEN`: the auth token.
  * `PROJECT_ID`: the project ID.
  * `TENANT_ID`: the tenant ID.



## What's next

  * [Create a sign-in page for multiple tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-ui)
  * [Migrate existing users to a tenant](https://docs.cloud.google.com/identity-platform/docs/migrate-users-between-projects-tenants)
  * [Manage tenants programmatically](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
