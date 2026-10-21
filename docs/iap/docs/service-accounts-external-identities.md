---
url: https://docs.cloud.google.com/iap/docs/service-accounts-external-identities/
title: Using service accounts with external identities \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:54.401110+00:00
---

# Using service accounts with external identities  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/service-accounts-external-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Using service accounts with external identities Stay organized with collections  Save and categorize content based on your preferences. 

This article shows you how to authenticate using service accounts when you're using Identity-Aware Proxy (IAP) with external identities.

## Obtaining your client ID and secret

  1. Go to the IAP page in the Google Cloud console.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Click the **APPLICATIONS** tab.

  3. Locate the app to configure to use service accounts.

  4. Select **Go to OAuth configuration** from the overflow menu.




A page displaying the client ID and secret for your app appears. You'll need these to configure Identity Platform in the next section.

## Configuring Google as an identity provider

If your Identity Platform project isn't already using Google for authentication, create a new configuration using your client ID and secret:

  1. Go to the **Identity Platform Providers** page in the Google Cloud console.  
[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)  


  2. If you are using Identity Platform multi-tenancy, select the tenant associated with your IAP resource.

  3. Click **Add provider**.

  4. Select **Google** from the list of providers.

  5. Under **Web SDK configuration** , enter the client ID and secret you obtained in the previous section.

  6. Click **Save**.




If you're already using Google authentication, you can use your client ID instead. This won't disrupt your existing users.

  1. Go to the **Identity Platform Providers** page in the Google Cloud console.  
[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)  


  2. If you are using Identity Platform multi-tenancy, select the tenant associated with your IAP resource.

  3. Locate **Google** in the list of providers, and click **Edit**.

  4. Under **Allowed client IDs** , click **Add**.

  5. Enter the client ID you obtained in the previous section.

  6. Click **Save**.




## Exchanging a Google token for an Identity Platform token

When you first authenticate with Google, Identity Platform will return a Google ID token. You can then exchange it for an Identity Platform token by calling [`signInWithIdp`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithIdp):

###  Node.js 
    
    
    import * as firebase from 'firebase/app';
    import 'firebase/auth';
    
    const config = {
      apiKey: '...',
    };
    firebase.initializeApp(config);
    const cred = firebase.auth.GoogleAuthProvider.credential(google_oidc_id_token);
    firebase.auth().signInWithCredential(cred)
      .then((userCredential) => {
        return userCredential.user.getIdToken();
      })
      .then((gcipIdToken) => {
        // This token can now be used to access the resource.
      })
      .catch((error) => {
        // Error occurred.
      });
    

###  Python 
    
    
    SIGN_IN_WITH_IDP_API = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp'
    
    def exchange_google_id_token_for_gcip_id_token(api_key, tenant_id, google_open_id_connect_token):
      url = SIGN_IN_WITH_IDP_API + '?key=' + api_key
      data={'requestUri': 'http://localhost',
            'returnSecureToken': True,
            'postBody':'id_token=' + google_open_id_connect_token + '&providerId=google.com',
            'tenantId': tenant_id}
      resp = requests.post(url, data)
      res = resp.json()
      return res['idToken']
    

###  REST 

Request:
    
    
    POST https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key=API-KEY
    

Body:
    
    
    {
    "postBody":"id_token=GOOGLE-ID-TOKEN&providerId=google.com"
    "requestUri": "http://localhost",
    "returnIdpCredential": true,
    "returnSecureToken": true,
    "tenantId": "TENANT-ID"
    }
    

Include the Identity Platform ID token in your authorization header to access resources by IAP:
    
    
    curl -H "Authorization: Bearer GCIP-ID-TOKEN" "https://example.appspot.com/api"

Note that external identities do not support IAM, so you'll need to manually update your app's access control to grant access to your service account. See [JWTs for external identities](https://docs.cloud.google.com/iap/docs/signed-headers-howto#jwts-for-external-identities) to learn more.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
