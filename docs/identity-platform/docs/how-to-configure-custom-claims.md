---
url: https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims/
title: Configure custom claims on users \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:07.417947+00:00
---

# Configure custom claims on users  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure custom claims on users

This document explains how to configure custom claims on users with Identity Platform. Custom claims are inserted into user tokens during authentication. Your app can use these claims to handle complex authorization scenarios, such as restricting a user's access to a resource based on their role.

## Set up custom claims

To preserve security, set custom claims using the Admin SDK on your server:

  1. If you haven't already, [Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk).

  2. Set the custom claim you want to use. In the following example, a custom claim is set on the user to describe that they're an administrator:

###  Node.js 
         
         // Set admin privilege on the user corresponding to uid.
         
         getAuth()
           .setCustomUserClaims(uid, { admin: true })
           .then(() => {
             // The new custom claims will propagate to the user's ID token the
             // next time a new one is issued.
           });
         
         [custom_claims.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/custom_claims.js#L13-L20)

###  Java 
         
         // Set admin privilege on the user corresponding to uid.
         Map<String, Object> claims = new HashMap<>();
         claims.put("admin", true);
         FirebaseAuth.getInstance().setCustomUserClaims(uid, claims);
         // The new custom claims will propagate to the user's ID token the
         // next time a new one is issued.
         
         [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L157-L162)

###  Python 
         
         # Set admin privilege on the user corresponding to uid.
         auth.set_custom_user_claims(uid, {'admin': True})
         # The new custom claims will propagate to the user's ID token the
         # next time a new one is issued.
         
         [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L282-L285)

###  Go 
         
         // Get an auth client from the firebase.App
         client, err := app.Auth(ctx)
         if err != nil {
         	log.Fatalf("error getting Auth client: %v\n", err)
         }
         
         // Set admin privilege on the user corresponding to uid.
         claims := map[string]interface{}{"admin": true}
         err = client.SetCustomUserClaims(ctx, uid, claims)
         if err != nil {
         	log.Fatalf("error setting custom claims %v\n", err)
         }
         // The new custom claims will propagate to the user's ID token the
         // next time a new one is issued.
         
         [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L295-L308)

###  C# 
         
         // Set admin privileges on the user corresponding to uid.
         var claims = new Dictionary<string, object>()
         {
             { "admin", true },
         };
         await FirebaseAuth.DefaultInstance.SetCustomUserClaimsAsync(uid, claims);
         // The new custom claims will propagate to the user's ID token the
         // next time a new one is issued.
         
         [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/c08a6533b109f960bfec5eaa93a55126dd62fe9e/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L527-L534)

  3. Validate the custom claim the next time it's sent to your server:

###  Node.js 
         
         // Verify the ID token first.
         getAuth()
           .verifyIdToken(idToken)
           .then((claims) => {
             if (claims.admin === true) {
               // Allow access to requested admin resource.
             }
           });
         
         [custom_claims.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/custom_claims.js#L24-L31)

###  Java 
         
         // Verify the ID token first.
         FirebaseToken decoded = FirebaseAuth.getInstance().verifyIdToken(idToken);
         if (Boolean.TRUE.equals(decoded.getClaims().get("admin"))) {
           // Allow access to requested admin resource.
         }
         
         [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L167-L171)

###  Python 
         
         # Verify the ID token first.
         claims = auth.verify_id_token(id_token)
         if claims['admin'] is True:
             # Allow access to requested admin resource.
             pass
         
         [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L290-L294)

###  Go 
         
         // Verify the ID token first.
         token, err := client.VerifyIDToken(ctx, idToken)
         if err != nil {
         	log.Fatal(err)
         }
         
         claims := token.Claims
         if admin, ok := claims["admin"]; ok {
         	if admin.(bool) {
         		//Allow access to requested admin resource.
         	}
         }
         
         [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L316-L327)

###  C# 
         
         // Verify the ID token first.
         FirebaseToken decoded = await FirebaseAuth.DefaultInstance.VerifyIdTokenAsync(idToken);
         object isAdmin;
         if (decoded.Claims.TryGetValue("admin", out isAdmin))
         {
             if ((bool)isAdmin)
             {
                 // Allow access to requested admin resource.
             }
         }
         
         
         [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/c08a6533b109f960bfec5eaa93a55126dd62fe9e/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L539-L549)

  4. To determine what custom claims are present for a user:

###  Node.js 
         
         // Lookup the user associated with the specified uid.
         getAuth()
           .getUser(uid)
           .then((userRecord) => {
             // The claims can be accessed on the user record.
             console.log(userRecord.customClaims['admin']);
           });
         
         [custom_claims.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/custom_claims.js#L35-L41)

###  Java 
         
         // Lookup the user associated with the specified uid.
         UserRecord user = FirebaseAuth.getInstance().getUser(uid);
         System.out.println(user.getCustomClaims().get("admin"));
         
         [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L175-L177)

###  Python 
         
         # Lookup the user associated with the specified uid.
         user = auth.get_user(uid)
         # The claims can be accessed on the user record.
         print(user.custom_claims.get('admin'))
         
         [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L298-L301)

###  Go 
         
         // Lookup the user associated with the specified uid.
         user, err := client.GetUser(ctx, uid)
         if err != nil {
         	log.Fatal(err)
         }
         // The claims can be accessed on the user record.
         if admin, ok := user.CustomClaims["admin"]; ok {
         	if admin.(bool) {
         		log.Println(admin)
         	}
         }
         
         [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L334-L344)

###  C# 
         
         // Lookup the user associated with the specified uid.
         UserRecord user = await FirebaseAuth.DefaultInstance.GetUserAsync(uid);
         Console.WriteLine(user.CustomClaims["admin"]);
         
         [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/c08a6533b109f960bfec5eaa93a55126dd62fe9e/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L553-L555)




When setting up custom claims, keep the following in mind:

  * Custom claims cannot exceed 1000 bytes in size. Attempting to pass claims larger than 1000 bytes results in an error.
  * Custom claims are inserted into the user JWT when the token is issued. New claims are not available until the token is refreshed. You can refresh a token silently by calling `user.getIdToken(true)`.
  * To maintain continuity and security, only set custom claims in a secure server environment.



## What's next

  * Learn more about [blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions), which can also be used to set custom claims.
  * Learn more about Identity Platform custom claims in the [Admin SDK reference documentation](https://firebase.google.com/docs/auth/admin/custom-claims).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
