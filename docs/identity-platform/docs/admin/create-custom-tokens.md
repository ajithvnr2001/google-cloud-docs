---
url: https://docs.cloud.google.com/identity-platform/docs/admin/create-custom-tokens/
title: Creating custom tokens \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:23.513361+00:00
---

# Creating custom tokens  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/admin/create-custom-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating custom tokens

This document shows you how to use Identity Platform to create custom JSON Web Tokens (JWTs).

Custom tokens give you complete control over the authentication process. You generate these tokens on your server, pass them back to a client device, and then call [`signInWithCustomToken()`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithCustomToken) to sign in users.

You can create custom tokens with the Identity Platform Admin SDK, or use a third-party JWT library.

## Before you begin

**Important:** Anyone who has the `iam.serviceAccounts.signBlob` [permission](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob) on the signing service account (including via an exported private key) can use it to mint custom tokens. When managing service accounts, we recommend following [best practices](https://cloud.google.com/blog/products/identity-security/help-keep-your-google-cloud-service-account-keys-safe). To reduce access, it is also recommended to [restrict service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts).

  * [Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk). If you are using service account auto-discovery or an explicitly specified service account ID, make sure the service account you are using has at least the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) role.

  * Create and deploy a server endpoint that accepts sign-in credentials from users.




## Creating custom tokens using the Admin SDK

The Admin SDK has a built-in method for creating custom tokens. At a minimum, you need to provide a `uid`. This can be any string that uniquely identifies the user or device. These tokens expire after one hour.

The following example shows how to create a custom token:

### Node.js
    
    
    const uid = 'some-uid';
    
    getAuth()
      .createCustomToken(uid)
      .then((customToken) => {
        // Send token back to client
      })
      .catch((error) => {
        console.log('Error creating custom token:', error);
      });
    
    [create_custom_tokens.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/create_custom_tokens.js#L18-L27)

### Java
    
    
    String uid = "some-uid";
    
    String customToken = FirebaseAuth.getInstance().createCustomToken(uid);
    // Send token back to client
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L238-L241)

### Python
    
    
    uid = 'some-uid'
    
    custom_token = auth.create_custom_token(uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L107-L109)

### Go
    
    
    client, err := app.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    
    token, err := client.CustomToken(ctx, "some-uid")
    if err != nil {
    	log.Fatalf("error minting custom token: %v\n", err)
    }
    
    log.Printf("Got custom token: %v\n", token)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L38-L48)

### C#
    
    
    var uid = "some-uid";
    
    string customToken = await FirebaseAuth.DefaultInstance.CreateCustomTokenAsync(uid);
    // Send token back to client
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L33-L36)

After you create a custom token, your app can use it to [sign in a user](https://docs.cloud.google.com/identity-platform/docs/web/custom).

Optionally, you can include additional claims on the custom token. These are propagated to the user's ID token as top-level claims.

The following example shows how to add a `premiumAccount` claim:

### Node.js
    
    
    const userId = 'some-uid';
    const additionalClaims = {
      premiumAccount: true,
    };
    
    getAuth()
      .createCustomToken(userId, additionalClaims)
      .then((customToken) => {
        // Send token back to client
      })
      .catch((error) => {
        console.log('Error creating custom token:', error);
      });
    
    [create_custom_tokens.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/create_custom_tokens.js#L31-L43)

### Java
    
    
    String uid = "some-uid";
    Map<String, Object> additionalClaims = new HashMap<String, Object>();
    additionalClaims.put("premiumAccount", true);
    
    String customToken = FirebaseAuth.getInstance()
        .createCustomToken(uid, additionalClaims);
    // Send token back to client
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L248-L254)

### Python
    
    
    uid = 'some-uid'
    additional_claims = {
        'premiumAccount': True
    }
    
    custom_token = auth.create_custom_token(uid, additional_claims)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L118-L123)

### Go
    
    
    client, err := app.Auth(context.Background())
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    
    claims := map[string]interface{}{
    	"premiumAccount": true,
    }
    
    token, err := client.CustomTokenWithClaims(ctx, "some-uid", claims)
    if err != nil {
    	log.Fatalf("error minting custom token: %v\n", err)
    }
    
    log.Printf("Got custom token: %v\n", token)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L56-L70)

### C#
    
    
    var uid = "some-uid";
    var additionalClaims = new Dictionary<string, object>()
    {
        { "premiumAccount", true },
    };
    
    string customToken = await FirebaseAuth.DefaultInstance
        .CreateCustomTokenAsync(uid, additionalClaims);
    // Send token back to client
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L44-L52)

Identity Platform complies with the [OpenID Connect JWT specification](https://openid.net/specs/openid-connect-core-1_0.html). This means the following claims are reserved and cannot be specified:

  * `acr`
  * `amr`
  * `at_hash`
  * `aud`
  * `auth_time`
  * `azp`
  * `cnf`
  * `c_hash`
  * `exp`
  * `firebase`
  * `iat`
  * `iss`
  * `jti`
  * `nbf`
  * `nonce`
  * `sub`



## Creating custom tokens using a third-party JWT library

If your backend is written in a language that the Admin SDK doesn't support, you can still manually create custom tokens. First, [find a third-party JWT library](https://jwt.io/) for your language. Then, use that library to mint a JWT which includes the following claims:

`alg` | Algorithm | `"RS256"`  
---|---|---  
`iss` | Issuer | Your project's service account email address.  
`sub` | Subject | Your project's service account email address.  
`aud` | Audience | `"https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit"`  
`iat` | Issued-at time | The current time, in seconds, since the UNIX epoch.  
`exp` | Expiration time |  The time, in seconds since the UNIX epoch, at which the token expires. It can be a **maximum of 3600 seconds later** than the `iat`.   
Note that this only controls the time when the custom token itself expires. Once you sign in a user with `signInWithCustomToken()`, they will remain signed in until they sign out or their session is invalidated.   
`uid` |  |  The unique identifier of the signed-in user. Must be a string between 1-36 characters long.   
`claims` (optional) |  |  Additional custom claims to include.   
  
The following examples demonstrate how to create custom tokens in languages the Admin SDK does not support:

### PHP

Using [`php-jwt`](https://github.com/firebase/php-jwt):
    
    
    // Requires: composer require firebase/php-jwt
    use Firebase\JWT\JWT;
    
    // Get your service account's email address and private key from the JSON key file
    $service_account_email = "abc-123@a-b-c-123.iam.gserviceaccount.com";
    $private_key = "-----BEGIN PRIVATE KEY-----...";
    
    function create_custom_token($uid, $is_premium_account) {
      global $service_account_email, $private_key;
    
      $now_seconds = time();
      $payload = array(
      "iss" => $service_account_email,
      "sub" => $service_account_email,
      "aud" => "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
      "iat" => $now_seconds,
      "exp" => $now_seconds+(60*60),  // Maximum expiration time is one hour
      "uid" => $uid,
      "claims" => array(
          "premium_account" => $is_premium_account
      )
      );
      return JWT::encode($payload, $private_key, "RS256");
    }
    

### Ruby

Using [`ruby-jwt`](https://github.com/jwt/ruby-jwt):
    
    
    require "jwt"
    
    # Get your service account's email address and private key from the JSON key file
    $service_account_email = "service-account@my-project-abc123.iam.gserviceaccount.com"
    $private_key = OpenSSL::PKey::RSA.new "-----BEGIN PRIVATE KEY-----\n..."
    
    def create_custom_token(uid, is_premium_account)
      now_seconds = Time.now.to_i
      payload = {:iss => $service_account_email,
                  :sub => $service_account_email,
                  :aud => "https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit",
                  :iat => now_seconds,
                  :exp => now_seconds+(60*60), # Maximum expiration time is one hour
                  :uid => uid,
                  :claims => {:premium_account => is_premium_account}}
      JWT.encode payload, $private_key, "RS256"
    end
    

After you create a custom token, your app can use it to [sign in a user](https://docs.cloud.google.com/identity-platform/docs/web/custom).

## What's next

  * [Sign in users](https://docs.cloud.google.com/identity-platform/docs/web/custom) with custom tokens.
  * [Configure custom claims](https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims) on users.
  * [Use the REST API](https://docs.cloud.google.com/identity-platform/docs/use-rest-api) to integrate Identity Platform with other parts of your custom authentication system.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
