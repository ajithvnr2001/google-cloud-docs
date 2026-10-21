---
url: https://docs.cloud.google.com/identity-platform/docs/link-accounts/
title: Linking multiple providers to an account \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:20.386456+00:00
---

# Linking multiple providers to an account  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/link-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Linking multiple providers to an account 

This document shows you how to link multiple providers to a single Identity Platform account.

Identity Platform uses a unique ID to identify users. This allows users to sign in to the same account with different providers. For example, a user who initially registered with a phone number could later link their Google account, and then use either method to sign in.

## Before you begin

Add support for two or more [identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#sign-in) to your app.

## Enabling or disabling account linking

The account linking setting determines how Identity Platform handles users attempting to sign in with the same email using different providers.

  * **Link accounts that use the same email** : Identity Platform will raise an error if a user tries to sign in with an email that's already in use. Your app can catch this error, and link the new provider to their existing account.

  * **Create multiple accounts for each identity provider** : A new Identity Platform user account will be created each time a user signs in with a different provider.


**Note:** These settings configure how Identity Platform responds when a user tries to sign in. You can always link multiple providers to an account manually by following the steps in the sections below.

To choose a setting:

  1. Go to the Identity Platform **Settings** page in the Google Cloud console.

[Go to the Settings page](https://console.cloud.google.com/customer-identity/settings)

  2. Select a setting under **User account linking**.

  3. Click **Save**.




## Linking federated provider credentials

To link credentials from a federated provider:

  1. Sign in the user with any authentication provider or method.

  2. Get the provider object that corresponds to the provider you want to link to the user's account. For example:

### Web version 9
         
         import { GoogleAuthProvider, FacebookAuthProvider, TwitterAuthProvider, GithubAuthProvider } from "firebase/auth";
         
         const googleProvider = new GoogleAuthProvider();
         const facebookProvider = new FacebookAuthProvider();
         const twitterProvider = new TwitterAuthProvider();
         const githubProvider = new GithubAuthProvider();
         
         [auth_get_providers.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/auth_get_providers.js#L8-L13)

### Web version 8
         
         var googleProvider = new firebase.auth.GoogleAuthProvider();
         var facebookProvider = new firebase.auth.FacebookAuthProvider();
         var twitterProvider = new firebase.auth.TwitterAuthProvider();
         var githubProvider = new firebase.auth.GithubAuthProvider();
         
         [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L34-L37)

  3. Prompt the user to sign in with the provider you want to link. You can either open a pop-up window, or redirect the current page. Redirecting is easier for users on mobile devices.

To show a pop-up, call `linkWithPopup()`:

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

To redirect the page, first call `linkWithRedirect()`:

Follow the [best practices](https://docs.cloud.google.com/identity-platform/docs/web/redirect-best-practices) when using `signInWithRedirect`, `linkWithRedirect`, or `reauthenticateWithRedirect`. 

### Web version 9
         
         import { getAuth, linkWithRedirect, GoogleAuthProvider } from "firebase/auth";
         const provider = new GoogleAuthProvider();
         
         const auth = getAuth();
         linkWithRedirect(auth.currentUser, provider)
           .then(/* ... */)
           .catch(/* ... */);
         
         [auth_link_with_redirect.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/auth_link_with_redirect.js#L8-L14)

### Web version 8
         
         auth.currentUser.linkWithRedirect(provider)
           .then(/* ... */)
           .catch(/* ... */);
         
         [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L85-L87)

After the user signs in, they'll be redirected back to your app. Then, you can retrieve the sign-in result by calling `getRedirectResult()`:

### Web version 9
         
         import { getRedirectResult } from "firebase/auth";
         getRedirectResult(auth).then((result) => {
           const credential = GoogleAuthProvider.credentialFromResult(result);
           if (credential) {
             // Accounts successfully linked.
             const user = result.user;
             // ...
           }
         }).catch((error) => {
           // Handle Errors here.
           // ...
         });
         
         [auth_get_redirect_result.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/auth_get_redirect_result.js#L8-L19)

### Web version 8
         
         auth.getRedirectResult().then((result) => {
           if (result.credential) {
             // Accounts successfully linked.
             var credential = result.credential;
             var user = result.user;
             // ...
           }
         }).catch((error) => {
           // Handle Errors here.
           // ...
         });
         
         [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L91-L101)




The user's account with the federated provider is now linked to their Identity Platform account, and they can use the provider to sign in.

## Linking email and password credentials

To add an email address and password to an existing user account:

  1. Sign in the user with any identity provider or method.

  2. Prompt the user for an email address and password.

  3. Create an `AuthCredential` object with the email address and password:

### Web version 9
         
         import { EmailAuthProvider } from "firebase/auth";
         
         const credential = EmailAuthProvider.credential(email, password);
         
         [auth_make_email_credential.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/index/auth_make_email_credential.js#L8-L10)

### Web version 8
         
         var credential = firebase.auth.EmailAuthProvider.credential(email, password);
         
         [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L145-L145)

  4. Pass the `AuthCredential` object to the `linkWithCredential()` method on the signed-in user:

### Web version 9
         
         import { getAuth, linkWithCredential } from "firebase/auth";
         
         const auth = getAuth();
         linkWithCredential(auth.currentUser, credential)
           .then((usercred) => {
             const user = usercred.user;
             console.log("Account linking success", user);
           }).catch((error) => {
             console.log("Account linking error", error);
           });
         
         [auth_simple_link.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/auth_simple_link.js#L8-L17)

### Web version 8
         
         auth.currentUser.linkWithCredential(credential)
           .then((usercred) => {
             var user = usercred.user;
             console.log("Account linking success", user);
           }).catch((error) => {
             console.log("Account linking error", error);
           });
         
         [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L43-L49)




The email and password credentials are now linked to the user's Identity Platform account, and they can use them to sign in.

Note that a [federated provider](https://docs.cloud.google.com/identity-platform/docs/link-accounts#federated) credential can be linked to an email/password account with a different email. If this happens, the email corresponding to the federated provider can be used to create a separate email/password account.

## Handling the account-exists-with-different-credential error

If you enabled the **Link accounts that use the same email** setting in Google Cloud console, when a user tries to sign in to a provider (such as SAML) with an email that already exists for another provider (such as Google), the error `auth/account-exists-with-different-credential` is thrown (along with an `AuthCredential` object).

To handle this error, prompt the user to sign in with the existing provider. Then call `linkWithCredential()`, `linkWithPopup()`, or `linkWithRedirect()` to associate the new provider to their account using the `AuthCredential`.

The following example shows how to handle this error when a user attempts to sign in using Facebook:

### Web version 9
    
    
      import { signInWithPopup, signInWithEmailAndPassword, linkWithCredential, FacebookAuthProvider } from "firebase/auth";
    
      // User tries to sign in with Facebook.
      signInWithPopup(auth, facebookProvider).catch((error) => {
      // User's email already exists.
      if (error.code === 'auth/account-exists-with-different-credential') {
        // The pending Facebook credential.
        const pendingCred = FacebookAuthProvider.credentialFromError(error);
        // The provider account's email address.
        const email = error.customData.email;
    
        // Present the user with a list of providers they might have
        // used to create the original account.
        // Then, ask the user to sign in with the existing provider.
        const method = promptUserForSignInMethod();
    
        if (method === 'password') {
          // TODO: Ask the user for their password.
          // In real scenario, you should handle this asynchronously.
          const password = promptUserForPassword();
          signInWithEmailAndPassword(auth, email, password).then((result) => {
            return linkWithCredential(result.user, pendingCred);
          }).then(() => {
            // Facebook account successfully linked to the existing user.
            goToApp();
          });
          return;
        }
    
        // All other cases are external providers.
        // Construct provider object for that provider.
        // TODO: Implement getProviderForProviderId.
        const provider = getProviderForProviderId(method);
        // At this point, you should let the user know that they already have an
        // account with a different provider, and validate they want to sign in
        // with the new provider.
        // Note: Browsers usually block popups triggered asynchronously, so in
        // real app, you should ask the user to click on a "Continue" button
        // that will trigger signInWithPopup().
        signInWithPopup(auth, provider).then((result) => {
          // Note: Identity Platform doesn't control the provider's sign-in
          // flow, so it's possible for the user to sign in with an account
          // with a different email from the first one.
    
          // Link the Facebook credential. We have access to the pending
          // credential, so we can directly call the link method.
          linkWithCredential(result.user, pendingCred).then((userCred) => {
            // Success.
            goToApp();
          });
        });
      }
    });
    
    [account_exists_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/account_exists_popup.js#L8-L60)

### Web version 8
    
    
      // User tries to sign in with Facebook.
          auth.signInWithPopup(facebookProvider).catch((error) => {
      // User's email already exists.
      if (error.code === 'auth/account-exists-with-different-credential') {
        // The pending Facebook credential.
        const pendingCred = error.credential;
        // The provider account's email address.
        const email = error.email;
    
        // Present the user with a list of providers they might have
        // used to create the original account.
        // Then, ask the user to sign in with the existing provider.
        const method = promptUserForSignInMethod();
    
        if (method === 'password') {
          // TODO: Ask the user for their password.
          // In real scenario, you should handle this asynchronously.
          const password = promptUserForPassword();
          auth.signInWithEmailAndPassword(email, password).then((result) => {
            return result.user.linkWithCredential(pendingCred);
          }).then(() => {
            // Facebook account successfully linked to the existing user.
            goToApp();
          });
          return;
        }
    
        // All other cases are external providers.
        // Construct provider object for that provider.
        // TODO: Implement getProviderForProviderId.
        const provider = getProviderForProviderId(method);
        // At this point, you should let the user know that they already have an
        // account with a different provider, and validate they want to sign in
        // with the new provider.
        // Note: Browsers usually block popups triggered asynchronously, so in
        // real app, you should ask the user to click on a "Continue" button
        // that will trigger signInWithPopup().
        auth.signInWithPopup(provider).then((result) => {
          // Note: Identity Platform doesn't control the provider's sign-in
          // flow, so it's possible for the user to sign in with an account
          // with a different email from the first one.
    
          // Link the Facebook credential. We have access to the pending
          // credential, so we can directly call the link method.
          result.user.linkWithCredential(pendingCred).then((userCred) => {
            // Success.
            goToApp();
          });
        });
      }
    });
    
    [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L165-L215)

Using a redirect is similar to a popup, except you'll need to cache the pending credential between page redirects (for example, by using session storage).

Note that some providers, such as Google and Microsoft, serve as both email and social identity providers. Email providers are considered authoritative for all addresses related to their hosted email domain. This means a user logging in with an email address hosted by the same provider will never raise this error (for example, signing in with Google using an `@gmail.com` email, or Microsoft using an `@live.com` or `@outlook.com` email).

## Merging accounts manually

If a user attempts to sign in with credentials that are already linked to another user account using the same provider, the client SDK's built-in methods for account linking will fail. In this situation, you'll need to merge the accounts manually, and then delete the second account. For example:

###  Web version 9
    
    
    // Sign in first account.
    const result1 = await signInWithCredential(auth, cred1);
    const user1 = result1.user;
    // Try to link a credential that belongs to an existing account
    try {
      await linkWithCredential(user1, cred2);
    } catch (error) {
      // cred2 already exists so an error is thrown.
      const result2 = await signInWithCredential(auth, error.credential);
      const user2 = result2.user;
      // Merge the data.
      mergeData(user1, user2);
      // Delete one of the accounts, and try again.
      await user2.delete();
      // Linking now will work.
      await linkWithCredential(user1, result2.credential);
    }
    

###  Web version 8
    
    
    // Sign in first account.
    const result1 = await auth.signInWithCredential(cred1);
    const user1 = result1.user;
    // Try to link a credential that belongs to an existing account
    try {
      await user1.linkWithCredential(cred2);
    } catch (error) {
      // cred2 already exists so an error is thrown.
      const result2 = await auth.signInWithCredential(error.credential);
      const user2 = result2.user;
      // Merge the data.
      mergeData(user1, user2);
      // Delete one of the accounts, and try again.
      await user2.delete();
      // Linking now will work.
      await user1.linkWithCredential(result2.credential);
    }
    

## Unlinking a provider

You can unlink a provider from a user's account. The user will no longer be able to authenticate with that provider.

To unlink a provider, pass the provider ID to the `unlink()` method. You can get the provider IDs of the auth providers linked to a user from the `providerData` property.

### Web version 9
    
    
    import { getAuth, unlink } from "firebase/auth";
    
    const auth = getAuth();
    unlink(auth.currentUser, providerId).then(() => {
      // Auth provider unlinked from account
      // ...
    }).catch((error) => {
      // An error happened
      // ...
    });
    
    [auth_unlink_provider.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/link-multiple-accounts/auth_unlink_provider.js#L8-L17)

### Web version 8
    
    
    user.unlink(providerId).then(() => {
      // Auth provider unlinked from account
      // ...
    }).catch((error) => {
      // An error happened
      // ...
    });
    
    [link-multiple-accounts.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/link-multiple-accounts.js#L153-L159)

## What's next

  * Add support for different [identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#sign-in) to your app.
  * Learn how to [manage providers programmatically](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
