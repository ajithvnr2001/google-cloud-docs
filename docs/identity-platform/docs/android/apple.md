---
url: https://docs.cloud.google.com/identity-platform/docs/android/apple/
title: Signing in users with Apple on Android \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:59.358737+00:00
---

# Signing in users with Apple on Android  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/android/apple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with Apple on Android

This document shows you how to use Identity Platform to add _Sign in with Apple_ to your Android app.

## Before you begin

  * Enable Identity Platform and have a basic Android app. To learn about how to enable Identity Platform and sign in, see [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email).

  * Join the [Apple Developer Program](https://developer.apple.com/programs).




## Configuring your app with Apple

On the Apple Developer site:

  1. Follow the steps in [Configure Sign in with Apple for the web](https://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web). This includes:

     1. Registering a _Return URL_ , which looks like:
            
            https://project-id.firebaseapp.com/__/auth/handler
            

     2. Temporarily hosting a file at the following URL to verify your domain:
            
            https://project-id.firebaseapp.com/.well-known/apple-developer-domain-association.txt
            

Additionally, take note of your _Services ID_ and _Apple team ID_ — you'll need them in the next section.

  2. [Use an Apple private key to create a sign in](https://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key). You'll need the _key_ and its _ID_ in the next section.

  3. If you use Identity Platform to send emails to your users, [configure your project with Apple's private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) using the following email:
         
         noreply@project-id.firebaseapp.com
         

You can also use a custom email template, if your app has one.




## Complying with Apple's anonymized data requirements

Apple gives users the option of anonymizing their data, including their email address. Apple assigns users who select this option an obfuscated email address with the domain `privaterelay.appleid.com`.

Your app must comply with any applicable developer policies or terms from Apple regarding anonymized Apple IDs. This includes obtaining user consent before associating any personally identifying information (PII) with an anonymized Apple ID. Actions that involve PII include, but are not limited to:

  * Linking an email address to an anonymized Apple ID, or vice versa.
  * Linking a phone number to an anonymized Apple ID, or vice versa
  * Linking a non-anonymous social credential, such as Facebook or Google, to to anonymized Apple ID, or vice versa.



For more information, refer to the _Apple Developer Program License Agreement_ for your Apple developer account.

## Configuring Apple as a provider

To configure Apple as an identity provider:

  1. Go to the **Identity Providers** page in the Google Cloud console.

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add a Provider**.

  3. Select **Apple** from the list.

  4. Under **Platform** , select **Android**.

  5. Enter your **Services ID** , **Apple team ID** , **Key ID** , and **Private key**.

  6. Register your app's domains by clicking **Add domain** under **Authorized domains**. For development purposes, `localhost` is already enabled by default.

**Important:** In projects created after April 28, 2025, Identity Platform no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.
  7. Under **Configure your application** , click **Android**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  8. Click **Save**.




## Signing in users with the client SDK

  1. Create an instance of the `OAuthProvider` provider object, using the ID `apple.com`:

###  Java 
         
         OAuthProvider.Builder provider = OAuthProvider.newBuilder("apple.com");
         

###  Kotlin 
         
         val provider = OAuthProvider.newBuilder("apple.com")
         

  2. **Optional:** Add OAuth scopes. Scopes specify what data you are requesting from Apple. More sensitive data may require specific scopes. By default, when **One account per email address** is enabled, Identity Platform requests the `email` and `name` scopes.

###  Java 
         
         List<String> scopes =
             new ArrayList<String>() {
               {
                 add("email");
                 add("name");
               }
             };
         provider.setScopes(scopes);
         

###  Kotlin 
         
         provider.setScopes(arrayOf("email", "name"))
         

  3. **Optional:** Localize the authentication flow. You can specify a language, or use the device's default language:

###  Java 
         
         // Localize the Apple authentication screen in French.
         provider.addCustomParameter("locale", "fr");
         

###  Kotlin 
         
         // Localize the Apple authentication screen in French.
         provider.addCustomParameter("locale", "fr");
         

  4. Sign in the user with Identity Platform.

**Note:** When a user signs in, Identity Platform takes control of your UI and opens a [Custom Chrome Tab](https://developer.chrome.com/multidevice/android/customtabs). Because of this, you shouldn't reference your Activity in the `OnSuccessListener` and `OnFailureListener` listeners; they will immediately detach when the authentication operation starts.
     1. Check if a response is already present by calling `startActivityForSignInWithProvider()`:

###  Java 
            
            mAuth = FirebaseAuth.getInstance();
            Task<AuthResult> pending = mAuth.getPendingAuthResult();
            if (pending != null) {
                pending.addOnSuccessListener(new OnSuccessListener<AuthResult>() {
                    @Override
                    public void onSuccess(AuthResult authResult) {
                        Log.d(TAG, "checkPending:onSuccess:" + authResult);
                        // Get the user profile with authResult.getUser() and
                        // authResult.getAdditionalUserInfo(), and the ID
                        // token from Apple with authResult.getCredential().
                    }
                }).addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Log.w(TAG, "checkPending:onFailure", e);
                    }
                });
            } else {
                Log.d(TAG, "pending: null");
            }
            

###  Kotlin 
            
            val pending = auth.pendingAuthResult
            if (pending != null) {
                pending.addOnSuccessListener { authResult ->
                    Log.d(TAG, "checkPending:onSuccess:$authResult")
                    // Get the user profile with authResult.getUser() and
                    // authResult.getAdditionalUserInfo(), and the ID
                    // token from Apple with authResult.getCredential().
                }.addOnFailureListener { e ->
                    Log.w(TAG, "checkPending:onFailure", e)
                }
            } else {
                Log.d(TAG, "pending: null")
            }
            

Signing in puts your Activity in the background, which means the system can reclaim it during the authentication flow. Checking if a result is already present prevents the user from having to sign in twice.

     2. If there's no pending result, call `startActivityForSignInWithProvider()`:

###  Java 
            
            mAuth.startActivityForSignInWithProvider(this, provider.build())
                .addOnSuccessListener(
                        new OnSuccessListener<AuthResult>() {
                            @Override
                            public void onSuccess(AuthResult authResult) {
                                // Sign-in successful!
                                Log.d(TAG, "activitySignIn:onSuccess:" + authResult.getUser());
                                FirebaseUser user = authResult.getUser();
                                // ...
                            }
                        })
                .addOnFailureListener(
                        new OnFailureListener() {
                            @Override
                            public void onFailure(@NonNull Exception e) {
                                Log.w(TAG, "activitySignIn:onFailure", e);
                            }
                        });
            

###  Kotlin 
            
            auth.startActivityForSignInWithProvider(this, provider.build())
              .addOnSuccessListener { authResult ->
                  // Sign-in successful!
                  Log.d(TAG, "activitySignIn:onSuccess:${authResult.user}")
                  val user = authResult.user
                  // ...
              }
              .addOnFailureListener { e ->
                  Log.w(TAG, "activitySignIn:onFailure", e)
              }
            




Unlike many other identity providers, Apple does not provide a photo URL.

If a user chooses not to share their real email with your app, Apple provisions a unique email address for that user to share instead. This email takes the form `xyz@privaterelay.appleid.com`. If you configured the private email relay service, Apple forwards emails sent to the anonymized address to the user's real email address.

Apple only shares user information, such as display names, with apps the first time a user signs in. In most cases, Identity Platform stores this data, which lets you fetch it using `firebase.auth().currentUser.displayName` during future sessions. However, if you allowed users to sign into your app using Apple before integrating with Identity Platform, user information is not available.

## What's next

  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users).
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
