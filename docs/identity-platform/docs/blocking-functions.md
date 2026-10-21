---
url: https://docs.cloud.google.com/identity-platform/docs/blocking-functions/
title: Customize the authentication flow using blocking functions \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:20.082574+00:00
---

# Customize the authentication flow using blocking functions  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/blocking-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Customize the authentication flow using blocking functions 

This document shows you how to extend Identity Platform authentication using blocking [Cloud Run functions](https://docs.cloud.google.com/functions).

Blocking functions let you execute custom code that modifies the result of a user registering or signing in to your app. For example, you can prevent a user from authenticating if they don't meet certain criteria, or update a user's information before returning it to your client app.

**Note:** Blocking functions are only available for use with Identity Platform. For Firebase Authentication projects, blocking functions are supported only when you upgrade your project to [Firebase Authentication with Identity Platform](https://firebase.google.com/docs/auth#identity-platform).

## Before you begin

Create an app with Identity Platform. For instructions, see [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email).

## Understand blocking functions

You can register blocking functions for two events:

  * **`beforeCreate`** : Triggers before a new user is saved to the Identity Platform database, and before a token is returned to your client app.

  * **`beforeSignIn`** : Triggers after a user's credentials are verified, but before Identity Platform returns an ID token to your client app. If your app uses [multi-factor authentication](https://docs.cloud.google.com/identity-platform/docs/web/mfa), the function triggers after the user verifies their second factor. Note that creating a new user also triggers `beforeSignIn`, in addition to `beforeCreate`.




Keep the following in mind when using blocking functions:

  * Your function must respond within seven seconds. After seven seconds, Identity Platform returns an error, and the client operation fails.

  * HTTP response codes other than `200` are passed to your client apps. Ensure your client code handles any errors your function can return.

  * Functions apply to all users in your project, including any contained in a [tenant](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy). Identity Platform provides information about users to your function, including any tenants they belong to, so you can respond accordingly.

  * [Linking another identity provider to an account](https://docs.cloud.google.com/identity-platform/docs/link-accounts) re-triggers any registered `beforeSignIn` functions. This does not include email and password providers.

  * Anonymous and custom authentication don't support blocking functions.

  * If you are also using asynchronous functions, the user object that an asynchronous function receives does not contain updates from the blocking function.


**Warning:** If you delete Cloud Run functions, you must also unregister the trigger with Identity Platform. Failure to do so will prevent all users from authenticating with your app.

## Create a blocking function

The following steps demonstrate how to create a blocking function:

  1. Go to the Identity Platform **Settings** page in the Google Cloud console.

[ Go to the Settings page](https://console.cloud.google.com/customer-identity/settings)

  2. Select the **Triggers** tab.

  3. Depending on when you want to trigger the blocking function, select **Create Function** from either the **Before create (beforeCreate)** drop-down menu or the **Before sign in (beforeSignIn)** drop-down menu.

  4. In the **Create function** pane, do the following:

     1. In the **Function name** field, enter a name for your function.

     2. In the **Region** list, select a region.

     3. Copy the trigger URL.

     4. In the **Runtime, build, connections, and security settings** section, go to each tab and configure the required settings.

  5. In the **Source Code** section, build your source code.

     1. In the **Runtime** list, select your runtime.

     2. In the **Entry point** field, enter the entry point to your code.

     3. Using the inline editor, open `index.js`. Delete the example `helloWorld` code, and replace it with one of the following:

To respond to registration:
            
            import * as gcipCloudFunctions from 'gcip-cloud-functions';
            
            const authClient = new gcipCloudFunctions.Auth();
            
            exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
            });
            

To respond to sign-in:
            
            import * as gcipCloudFunctions from 'gcip-cloud-functions';
            
            const authClient = new gcipCloudFunctions.Auth();
            
            exports.beforeSignIn = authClient.functions().beforeSignInHandler((user, context) => {
            
            });
            

     4. Open `package.json` and add the following dependencies block: For the latest SDK version, see [`gcip-cloud-functions`](https://www.npmjs.com/package/gcip-cloud-functions).
            
            {
              "type": "module",
              "name": ...,
              "version": ...,
            
              "dependencies": {
                "gcip-cloud-functions": "^0.2.0"
              }
            }
            

  6. To publish your function, click **Deploy function**.

  7. Select the OAuth token credentials to pass to the function.

  8. On the **Settings** page, click **Save**.


**Note:** If you make any changes to your function, you must deploy it again.

You can also create and manage functions by using the Google Cloud CLI or the REST API. For detailed instructions, see the [Cloud Run functions documentation](https://docs.cloud.google.com/functions/docs/create-deploy-http-nodejs).

## Get user and context information

The `beforeSignIn` and `beforeCreate` events provide `User` and `EventContext` objects that contain information about the user signing in. Use these values in your code to determine whether to allow an operation to proceed.

For a list of properties available on the `User` object, see the [`UserRecord` API reference](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.userrecord).

The `EventContext` object contains the following properties:

Name | Description | Example  
---|---|---  
`locale` |  The application locale. You can set the locale using the client SDK, or by passing the locale header in the REST API.  | `fr` or `sv-SE`  
`ipAddress` |  The IP address of the device the end user is registering or signing in from.  | `114.14.200.1`  
`userAgent` | The user agent triggering the blocking function. | `Mozilla/5.0 (X11; Linux x86_64)`  
`eventId` | The event's unique identifier. | `rWsyPtolplG2TBFoOkkgyg`  
`eventType` |  The event type. This provides information on the event name, such as `beforeSignIn` or `beforeCreate`, and the associated sign-in method used, like Google or email/password.  |  `providers/cloud.auth/eventTypes/user.beforeSignIn:password`  
`authType` | Always `USER`. |  `USER`  
`resource` | The Identity Platform project or tenant. |  `projects/project-id/tenants/tenant-id`  
`timestamp` |  The time the event was triggered, formatted as an [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) string.  | `Tue, 23 Jul 2019 21:10:57 GMT`  
`additionalUserInfo` | An object containing information about the user. |  [ `AdditionalUserInfo` ](https://docs.cloud.google.com/identity-platform/docs/reference/gcip-cloud-functions#additional-user-info)  
`credential` | An object containing information about the user's credential. |  [ `AuthCredential` ](https://docs.cloud.google.com/identity-platform/docs/reference/gcip-cloud-functions#auth-credential)  
  
## Block registration or sign-in

To block a registration or sign-in attempt, throw an `HttpsError` in your function. For example:

###  Node.js 
    
    
    throw new gcipCloudFunctions.https.HttpsError('permission-denied');
    

The following table lists the errors you can raise, along with their default error message:

Name | Code | Message  
---|---|---  
`invalid-argument` | `400` | Client specified an invalid argument.  
`failed-precondition` | `400` | Request can not be executed in the current system state.  
`out-of-range` | `400` | Client specified an invalid range.  
`unauthenticated` | `401` | Missing, invalid, or expired OAuth token.  
`permission-denied` | `403` | Client does not have sufficient permission.  
`not-found` | `404` | Specified resource is not found.  
`aborted` | `409` | Concurrency conflict, such as a read-modify-write conflict.  
`already-exists` | `409` | The resource that a client tried to create already exists.  
`resource-exhausted` | `429` | Either out of resource quota or reaching rate limiting.  
`cancelled` | `499` | Request cancelled by the client.  
`data-loss` | `500` | Unrecoverable data loss or data corruption.  
`unknown` | `500` | Unknown server error.  
`internal` | `500` | Internal server error.  
`not-implemented` | `501` | API method not implemented by the server.  
`unavailable` | `503` | Service unavailable.  
`deadline-exceeded` | `504` | Request deadline exceeded.  
  
You can also specify a custom error message:

###  Node.js 
    
    
    throw new gcipCloudFunctions.https.HttpsError('permission-denied', 'Unauthorized request origin!');
    

The following example shows how to block users who are not within a specific domain from registering for your app:

###  Node.js 
    
    
    // Import the Cloud Auth Admin module.
    import * as gcipCloudFunctions from 'gcip-cloud-functions';
    // Initialize the Auth client.
    const authClient = new gcipCloudFunctions.Auth();
    // Http trigger with Cloud Run functions.
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      // If the user is authenticating within a tenant context, the tenant ID can be determined from
      // user.tenantId or from context.resource, eg. 'projects/project-id/tenant/tenant-id-1'
      // Only users of a specific domain can sign up.
      if (!user.email.endsWith('@acme.com')) {
        throw new gcipCloudFunctions.https.HttpsError('invalid-argument', `Unauthorized email "${user.email}"`);
      }
    });
    

Regardless of whether you use a default or custom message, Cloud Run functions wraps the error and returns it to the client as an internal error. For example, if you raise the following error in your function:
    
    
    throw new gcipCloudFunctions.https.HttpsError('invalid-argument', `Unauthorized email user@evil.com}`);
    

An error similar to the following is returned to your client app (if you are using the client SDK, the error is wrapped as an internal error):
    
    
    {
      "error": {
        "code": 400,
        "message": "BLOCKING_FUNCTION_ERROR_RESPONSE : HTTP Cloud Function returned an error. Code: 400, Status: \"INVALID_ARGUMENT\", Message: \"Unauthorized email user@evil.com\"",
        "errors": [
          {
            "message": "BLOCKING_FUNCTION_ERROR_RESPONSE : HTTP Cloud Function returned an error. Code: 400, Status: \"INVALID_ARGUMENT\", Message: \"Unauthorized email user@evil.com\"",
            "domain": "global",
            "reason": "invalid"
          }
        ]
      }
    }
    

Your app should catch the error, and handle it accordingly. For example:

###  JavaScript 
    
    
    // Blocking functions can also be triggered in a multi-tenant context before user creation.
    // firebase.auth().tenantId = 'tenant-id-1';
    firebase.auth().createUserWithEmailAndPassword('johndoe@example.com', 'password')
      .then((result) => {
        result.user.getIdTokenResult()
      })
      .then((idTokenResult) => {
        console.log(idTokenResult.claim.admin);
      })
      .catch((error) => {
        if (error.code !== 'auth/internal-error' && error.message.indexOf('Cloud Function') !== -1) {
          // Display error.
        } else {
          // Registration succeeds.
        }
      });
    

## Modify a user

Instead of blocking a registration or sign-in attempt, you can allow the operation to continue, but modify the `User` object that is saved to Identity Platform's database and returned to the client.

To modify a user, return an object from your event handler containing the fields to modify. You can modify the following fields:

  * `displayName`
  * `disabled`
  * `emailVerified`
  * `photoURL`
  * `customClaims`
  * `sessionClaims` (`beforeSignIn` only)



With the exception of `sessionClaims`, all modified fields are saved to Identity Platform's database, which means they are included on the response token and persist between user sessions.

The following example shows how to set a default display name:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      return {
        // If no display name is provided, set it to "guest".
        displayName: user.displayName || 'guest'
      };
    });
    

If you register an event handler for both `beforeCreate` and `beforeSignIn`, note that `beforeSignIn` executes after `beforeCreate`. User fields updated in `beforeCreate` are visible in `beforeSignIn`. If you set a field other than `sessionClaims` in both event handlers, the value set in `beforeSignIn` overwrites the value set in `beforeCreate`. For `sessionClaims` only, they are propagated to the current session's token claims, but are not persisted or stored in the database.

For example, if any `sessionClaims` are set, `beforeSignIn` will return them with any `beforeCreate` claims, and they will be merged. When they're merged, if a `sessionClaims` key matches a key in `customClaims`, the matching `customClaims` will be overwritten in the token claims by the `sessionClaims` key. However, the overwritten `customClaims` key is still persisted in the database for future requests.

## Supported OAuth credentials and data

You can pass OAuth credentials and data to blocking functions from various identity providers. The following table shows what credentials and data are supported for each identity provider:

Identity Provider | ID Token | Access Token | Expiration Time | Token Secret | Refresh Token | Sign-in Claims  
---|---|---|---|---|---|---  
Google | Yes | Yes | Yes | No | Yes | No  
Facebook | No | Yes | Yes | No | No | No  
Twitter | No | Yes | No | Yes | No | No  
GitHub | No | Yes | No | No | No | No  
Microsoft | Yes | Yes | Yes | No | Yes | No  
LinkedIn | No | Yes | Yes | No | No | No  
Yahoo | Yes | Yes | Yes | No | Yes | No  
Apple | Yes | Yes | Yes | No | Yes | No  
SAML | No | No | No | No | No | Yes  
OIDC | Yes | Yes | Yes | No | Yes | Yes  
  
### Refresh tokens

To use a refresh token in a blocking function, you must first select the checkbox in the **Triggers** section of the **Include token credentials** drop-down menu in the Google Cloud console.

Refresh tokens won't be returned by any identity providers when signing in directly with an OAuth credential, such as an ID token or access token. In this situation, the same client-side OAuth credential will be passed to the blocking function. However, for 3-legged flows, a refresh token might be available if the identity provider supports it.

The following sections describe each identity provider types and their supported credentials and data.

### Generic OIDC providers

When a user signs in with a generic OIDC provider, the following credentials will be passed:

  * **ID token** : Provided if the `id_token` flow is selected.
  * **Access token** : Provided if the code flow is selected. Note that the code flow is only supported with the REST API.
  * **Refresh token** : Provided if the [`offline_access` scope](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess) is selected.



Example:
    
    
    const provider = new firebase.auth.OAuthProvider('oidc.my-provider');
    provider.addScope('offline_access');
    firebase.auth().signInWithPopup(provider);
    

### Google

When a user signs in with Google, the following credentials will be passed:

  * **ID token**
  * **Access token**
  * **Refresh token** : Only provided if the following custom parameters are requested: 
    * `access_type=offline`
    * `prompt=consent`, if the user previously consented and no new scope was requested



Example:
    
    
    const provider = new firebase.auth.GoogleAuthProvider();
    provider.setCustomParameters({
      'access_type': 'offline',
      'prompt': 'consent'
    });
    firebase.auth().signInWithPopup(provider);
    

Learn more about [Google refresh tokens](https://developers.google.com/identity/protocols/oauth2/openid-connect#refresh-tokens).

### Facebook

When a user signs in with Facebook, the following credential will be passed:

  * **Access token** : An access token is returned that can be exchanged for another access token. Learn more about the different types of [access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) supported by Facebook and how you can exchange them for [long-lived tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension).



### GitHub

When a user signs in with GitHub, the following credential will be passed:

  * **Access token** : Does not expire unless revoked.



### Microsoft

When a user signs in with Microsoft, the following credentials will be passed:

  * **ID token**
  * **Access token**
  * **Refresh token** : Passed to the blocking function if the [`offline_access` scope](https://openid.net/specs/openid-connect-core-1_0.html#OfflineAccess) is selected.



Example:
    
    
    const provider = new firebase.auth.OAuthProvider('microsoft.com');
    provider.addScope('offline_access');
    firebase.auth().signInWithPopup(provider);
    

### Yahoo

When a user signs in with Yahoo, the following credentials will be passed without any custom parameters or scopes:

  * **ID token**
  * **Access token**
  * **Refresh token**



### LinkedIn

When a user signs in with LinkedIn, the following credential will be passed:

  * **Access token**



### Apple

When a user signs in with Apple, the following credentials will be passed without any custom parameters or scopes:

  * **ID token**
  * **Access token**
  * **Refresh token**



## Common scenarios

The following examples demonstrate some common use cases for blocking functions:

### Allow registration from a specific domain

The following example shows how to prevent users who aren't part of the `example.com` domain from registering with your app:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      if (!user.email || user.email.indexOf('@example.com') === -1) {
        throw new gcipCloudFunctions.https.HttpsError(
          'invalid-argument', `Unauthorized email "${user.email}"`);
      }
    });
    

### Block users with unverified emails from registering

The following example shows how to prevent users with unverified emails from registering with your app:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      if (user.email && !user.emailVerified) {
        throw new gcipCloudFunctions.https.HttpsError(
          'invalid-argument', `Unverified email "${user.email}"`);
      }
    });
    

### Require email verification on registration

The following example shows how to require a user to verify their email after registering:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      const locale = context.locale;
      if (user.email && !user.emailVerified) {
        // Send custom email verification on sign-up.
        return admin.auth().generateEmailVerificationLink(user.email).then((link) => {
          return sendCustomVerificationEmail(user.email, link, locale);
        });
      }
    });
    
    exports.beforeSignIn = authClient.functions().beforeSignInHandler((user, context) => {
     if (user.email && !user.emailVerified) {
       throw new gcipCloudFunctions.https.HttpsError(
         'invalid-argument', `"${user.email}" needs to be verified before access is granted.`);
      }
    });
    

### Treat certain identity provider emails as verified

The following example shows how to treat user emails from certain identity providers as verified:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      if (user.email && !user.emailVerified && context.eventType.indexOf(':facebook.com') !== -1) {
        return {
          emailVerified: true,
        };
      }
    });
    

### Block sign-in from certain IP addresses

The following example shows how to block sign-ins from certain IP address ranges.

###  Node.js 
    
    
    exports.beforeSignIn = authClient.functions().beforeSignInHandler((user, context) => {
      if (isSuspiciousIpAddress(context.ipAddress)) {
        throw new gcipCloudFunctions.https.HttpsError(
          'permission-denied', 'Unauthorized access!');
      }
    });
    

### Set custom and session claims

The following example shows how to set custom and session claims:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      if (context.credential &&
          context.credential.providerId === 'saml.my-provider-id') {
        return {
          // Employee ID does not change so save in persistent claims (stored in
          // Auth DB).
          customClaims: {
            eid: context.credential.claims.employeeid,
          },
          // Copy role and groups to token claims. These will not be persisted.
          sessionClaims: {
            role: context.credential.claims.role,
            groups: context.credential.claims.groups,
          }
        }
      }
    });
    

### Track IP addresses to monitor suspicious activity

You can prevent token theft by tracking the IP address a user signs in from, and comparing it to the IP address on subsequent requests. If the request appears suspicious — for example, the IPs are from different geographical regions — you can ask the user to sign in again.

  1. Use session claims to track the IP address the user signs in with:

###  Node.js 
         
         exports.beforeSignIn = authClient.functions().beforeSignInHandler((user, context) => {
           return {
             sessionClaims: {
               signInIpAddress: context.ipAddress,
             },
           };
         });
         

  2. When a user attempts to access resources that require authentication with Identity Platform, compare the IP address in the request with the IP used to sign in:

###  Node.js 
         
         app.post('/getRestrictedData', (req, res) => {
           // Get the ID token passed.
           const idToken = req.body.idToken;
           // Verify the ID token, check if revoked and decode its payload.
           admin.auth().verifyIdToken(idToken, true).then((claims) => {
             // Get request IP address
             const requestIpAddress = req.connection.remoteAddress;
             // Get sign-in IP address.
             const signInIpAddress = claims.signInIpAddress;
             // Check if the request IP address origin is suspicious relative to
             // the session IP addresses. The current request timestamp and the
             // auth_time of the ID token can provide additional signals of abuse,
             // especially if the IP address suddenly changed. If there was a sudden
             // geographical change in a short period of time, then it will give
             // stronger signals of possible abuse.
             if (!isSuspiciousIpAddressChange(signInIpAddress, requestIpAddress)) {
               // Suspicious IP address change. Require re-authentication.
               // You can also revoke all user sessions by calling:
               // admin.auth().revokeRefreshTokens(claims.sub).
               res.status(401).send({error: 'Unauthorized access. Please login again!'});
             } else {
               // Access is valid. Try to return data.
               getData(claims).then(data => {
                 res.end(JSON.stringify(data);
               }, error => {
                 res.status(500).send({ error: 'Server error!' })
               });
             }
           });
         });
         




### Screen user photos

The following example shows how to sanitize users' profile photos:

###  Node.js 
    
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      if (user.photoURL) {
        return isPhotoAppropriate(user.photoURL)
          .then((status) => {
            if (!status) {
              // Sanitize inappropriate photos by replacing them with guest photos.
              // Users could also be blocked from sign-up, disabled, etc.
              return {
                photoURL: PLACEHOLDER_GUEST_PHOTO_URL,
              };
            }
          });
    });
    

To learn more about how to detect and sanitize images, see the [Cloud Vision](https://docs.cloud.google.com/vision) documentation.

### Access a user's identity provider OAuth credentials

The following example demonstrates how to obtain a refresh token for a user that signed in with Google, and use it to call the Google Calendar APIs. The refresh token is stored for offline access.

###  Node.js 
    
    
    const {OAuth2Client} = require('google-auth-library');
    const {google} = require('googleapis');
    const gcipCloudFunctions = require('gcip-cloud-functions');
    
    // ...
    // Initialize Google OAuth client.
    const keys = require('./oauth2.keys.json');
    const oAuth2Client = new OAuth2Client(
      keys.web.client_id,
      keys.web.client_secret
    );
    
    exports.beforeCreate = authClient.functions().beforeCreateHandler((user, context) => {
      if (context.credential &&
          context.credential.providerId === 'google.com') {
        // Store the refresh token for later offline use.
        // These will only be returned if refresh tokens credentials are included
        // (enabled by Cloud console).
        return saveUserRefreshToken(
            user.uid,
            context.credential.refreshToken,
            'google.com'
          )
          .then(() => {
            // Blocking the function is not required. The function can resolve while
            // this operation continues to run in the background.
            return new Promise((resolve, reject) => {
              // For this operation to succeed, the appropriate OAuth scope should be requested
              // on sign in with Google, client-side. In this case:
              // https://www.googleapis.com/auth/calendar
              // You can check granted_scopes from within:
              // context.additionalUserInfo.profile.granted_scopes (space joined list of scopes).
    
              // Set access token/refresh token.
              oAuth2Client.setCredentials({
                access_token: context.credential.accessToken,
                refresh_token: context.credential.refreshToken,
              });
              const calendar = google.calendar('v3');
              // Setup Onboarding event on user's calendar.
              const event = {/** ... */};
              calendar.events.insert({
                auth: oauth2client,
                calendarId: 'primary',
                resource: event,
              }, (err, event) => {
                // Do not fail. This is a best effort approach.
                resolve();
              });
          });
        })
      }
    });
    

## What's next

  * Extend authentication with [asynchronous functions](https://docs.cloud.google.com/identity-platform/docs/asynchronous-functions).
  * Learn more about [Cloud Run functions](https://docs.cloud.google.com/functions/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
