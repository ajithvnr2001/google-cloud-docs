---
url: https://docs.cloud.google.com/identity-platform/docs/web/reauth/
title: Reauthenticating users \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:47.601406+00:00
---

# Reauthenticating users  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/reauth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reauthenticating users

Certain sensitive operations—such as deleting an account, updating a user's email, changing a password, or enabling multi-factor authentication—require the user to have signed in recently. If you perform one of these actions, and the user signed in too long ago, the action fails with an error. Depending on the use case, this can be done with `reauthenticateWithPopup()`, `reauthenticateWithRedirect()` or `reauthenticateWithCredential()`.

## Example: Reauthenticate Apple Sign-in with Popup

### Web version 9
    
    
    import { getAuth, reauthenticateWithPopup, OAuthProvider } from "firebase/auth";
    
    // Result from Redirect auth flow.
    const auth = getAuth();
    const provider = new OAuthProvider('apple.com');
    
    reauthenticateWithPopup(auth.currentUser, provider)
      .then((result) => {
        // User is re-authenticated with fresh tokens minted and can perform
        // sensitive operations like account deletion, or updating their email
        // address or password.
    
        // The signed-in user info.
        const user = result.user;
    
        // You can also get the Apple OAuth Access and ID Tokens.
        const credential = OAuthProvider.credentialFromResult(result);
        const accessToken = credential.accessToken;
        const idToken = credential.idToken;
    
        // ...
      })
      .catch((error) => {
        // Handle Errors here.
        const errorCode = error.code;
        const errorMessage = error.message;
        // The email of the user's account used.
        const email = error.customData.email;
        // The credential that was used.
        const credential = OAuthProvider.credentialFromError(error);
    
        // ...
      });
    
    [auth_apple_reauthenticate_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_reauthenticate_popup.js#L8-L40)

### Web version 8
    
    
    const provider = new firebase.auth.OAuthProvider('apple.com');
    
    firebase
      .auth()
      .currentUser
      .reauthenticateWithPopup(provider)
      .then((result) => {
        // User is re-authenticated with fresh tokens minted and can perform
        // sensitive operations like account deletion, or updating their email
        // address or password.
        /** @type {firebase.auth.OAuthCredential} */
        var credential = result.credential;
    
        // The signed-in user info.
        var user = result.user;
         // You can also get the Apple OAuth Access and ID Tokens.
        var accessToken = credential.accessToken;
        var idToken = credential.idToken;
    
        // IdP data available in result.additionalUserInfo.profile.
          // ...
      })
      .catch((error) => {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        // The email of the user's account used.
        var email = error.email;
        // The firebase.auth.AuthCredential type that was used.
        var credential = error.credential;
    
        // ...
      });
    
    [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L103-L135)

## Example: `reauthenticateWithCredential()`

### Web version 9
    
    
    import { getAuth, reauthenticateWithCredential } from "firebase/auth";
    
    const auth = getAuth();
    const user = auth.currentUser;
    
    // TODO(you): prompt the user to re-provide their sign-in credentials
    const credential = promptForCredentials();
    
    reauthenticateWithCredential(user, credential).then(() => {
      // User re-authenticated.
    }).catch((error) => {
      // An error ocurred
      // ...
    });
    
    [auth_reauth_with_credential.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/manage/auth_reauth_with_credential.js#L8-L21)

### Web version 8
    
    
    const user = firebase.auth().currentUser;
    
    // TODO(you): prompt the user to re-provide their sign-in credentials
    const credential = promptForCredentials();
    
    user.reauthenticateWithCredential(credential).then(() => {
      // User re-authenticated.
    }).catch((error) => {
      // An error occurred
      // ...
    });
    
    [manage.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/manage.js#L140-L150)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
