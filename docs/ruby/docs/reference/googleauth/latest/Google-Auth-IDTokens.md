---
url: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens/
title: googleauth - Module Google::Auth::IDTokens (v1.17.4) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:12.849681+00:00
---

# googleauth - Module Google::Auth::IDTokens (v1.17.4)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  googleauth - Module Google::Auth::IDTokens (v1.17.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.4 (latest)  1.17.3  1.16.2  1.15.1  1.14.0  1.13.1  1.12.2 

Reference documentation and code samples for the googleauth module Google::Auth::IDTokens.

### Verifying Google ID tokens

This module verifies ID tokens issued by Google. This can be used to authenticate signed-in users using OpenID Connect. See <https://developers.google.com/identity/sign-in/web/backend-auth> for more information.

#### Basic usage

To verify an ID token issued by Google accounts:
    
    
    payload = Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html).[verify_oidc](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html) the_token,
                                                 aud: "my-app-client-id"
    

If verification succeeds, you will receive the token's payload as a hash. If verification fails, an exception (normally a subclass of [VerificationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-VerificationError "Google::Auth::IDTokens::VerificationError \(class\)")) will be raised.

To verify an ID token issued by the Google identity-aware proxy (IAP):
    
    
    payload = Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html).[verify_iap](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html) the_token,
                                                aud: "my-app-client-id"
    

These methods will automatically download and cache the Google public keys necessary to verify these tokens. They will also automatically verify the issuer (`iss`) field for their respective types of ID tokens.

#### Advanced usage

If you want to provide your own public keys, either by pointing at a custom URI or by providing the key data directly, use the Verifier class and pass in a key source.

To point to a custom URI that returns a JWK set:
    
    
    source = Google::Auth::IDTokens::JwkHttpKeySource.new "https://example.com/jwk"
    verifier = Google::Auth::IDTokens::Verifier.new key_source: source
    payload = verifier.verify the_token, aud: "my-app-client-id"
    

To provide key data directly:
    
    
    jwk_data = {
      keys: [
        {
          alg: "ES256",
          crv: "P-256",
          kid: "LYyP2g",
          kty: "EC",
          use: "sig",
          x: "SlXFFkJ3JxMsXyXNrqzE3ozl_0913PmNbccLLWfeQFU",
          y: "GLSahrZfBErmMUcHP0MGaeVnJdBwquhrhQ8eP05NfCI"
        }
      ]
    }
    source = Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html)::[StaticKeySource](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-StaticKeySource.html).from_jwk_set jwk_data
    verifier = Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html)::Verifier key_source: source
    payload = verifier.[verify](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-Verifier.html) the_token, aud: "my-app-client-id"
    

## Methods 

### .iap_key_source
    
    
    def self.iap_key_source() -> Google::Auth::IDTokens::JwkHttpKeySource

The key source providing public keys that can be used to verify ID tokens issued by Google IAP.

**Returns**

  * ([Google::Auth::IDTokens::JwkHttpKeySource](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-JwkHttpKeySource)) 



### .oidc_key_source
    
    
    def self.oidc_key_source() -> Google::Auth::IDTokens::JwkHttpKeySource

The key source providing public keys that can be used to verify ID tokens issued by Google OIDC.

**Returns**

  * ([Google::Auth::IDTokens::JwkHttpKeySource](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-JwkHttpKeySource)) 



### .verify_iap
    
    
    def self.verify_iap(token, aud: nil, azp: nil, iss: IAP_ISSUERS) -> Hash

A convenience method that verifies a token allegedly issued by Google IAP.

**Parameters**

  * **token** (String) — The ID token to verify 
  * **aud** (String, Array<String>, nil) _(defaults to: nil)_ — The expected audience. At least one `aud` field in the token must match at least one of the provided audiences, or the verification will fail with {Google::Auth::IDToken::AudienceMismatchError}. If `nil` (the default), no audience checking is performed. 
  * **azp** (String, Array<String>, nil) _(defaults to: nil)_ — The expected authorized party (azp). At least one `azp` field in the token must match at least one of the provided values, or the verification will fail with {Google::Auth::IDToken::AuthorizedPartyMismatchError}. If `nil` (the default), no azp checking is performed. 
  * **iss** (String, Array<String>, nil) _(defaults to: IAP_ISSUERS)_ — The expected issuer. At least one `iss` field in the token must match at least one of the provided issuers, or the verification will fail with {Google::Auth::IDToken::IssuerMismatchError}. If `nil`, no issuer checking is performed. Default is to check against {IAP_ISSUERS}. 



**Returns**

  * (Hash) — The decoded token payload. 



**Raises**

  * ([Google::Auth::IDTokens::KeySourceError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeySourceError)) — if the key source failed to obtain public keys 
  * ([Google::Auth::IDTokens::VerificationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-VerificationError)) — if the token verification failed. Additional data may be available in the error subclass and message. 



### .verify_oidc
    
    
    def self.verify_oidc(token, aud: nil, azp: nil, iss: OIDC_ISSUERS) -> Hash

A convenience method that verifies a token allegedly issued by Google OIDC.

**Parameters**

  * **token** (String) — The ID token to verify 
  * **aud** (String, Array<String>, nil) _(defaults to: nil)_ — The expected audience. At least one `aud` field in the token must match at least one of the provided audiences, or the verification will fail with {Google::Auth::IDToken::AudienceMismatchError}. If `nil` (the default), no audience checking is performed. 
  * **azp** (String, Array<String>, nil) _(defaults to: nil)_ — The expected authorized party (azp). At least one `azp` field in the token must match at least one of the provided values, or the verification will fail with {Google::Auth::IDToken::AuthorizedPartyMismatchError}. If `nil` (the default), no azp checking is performed. 
  * **iss** (String, Array<String>, nil) _(defaults to: OIDC_ISSUERS)_ — The expected issuer. At least one `iss` field in the token must match at least one of the provided issuers, or the verification will fail with {Google::Auth::IDToken::IssuerMismatchError}. If `nil`, no issuer checking is performed. Default is to check against {OIDC_ISSUERS}. 



**Returns**

  * (Hash) — The decoded token payload. 



**Raises**

  * ([Google::Auth::IDTokens::KeySourceError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeySourceError)) — if the key source failed to obtain public keys 
  * ([Google::Auth::IDTokens::VerificationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-VerificationError)) — if the token verification failed. Additional data may be available in the error subclass and message. 



## Constants 

### OIDC_ISSUERS

**value:**["accounts.google.com", "https://accounts.google.com"].freeze  
A list of issuers expected for Google OIDC-issued tokens.

### IAP_ISSUERS

**value:**["https://cloud.google.com/iap"].freeze  
A list of issuers expected for Google IAP-issued tokens.

### OAUTH2_V3_CERTS_URL

**value:** "[https://www.googleapis.com/oauth2/v3/certs"](https://www.googleapis.com/oauth2/v3/certs&quot);  
The URL for Google OAuth2 V3 public certs

### IAP_JWK_URL

**value:** "[https://www.gstatic.com/iap/verify/public_key-jwk"](https://www.gstatic.com/iap/verify/public_key-jwk&quot);  
The URL for Google IAP public keys

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
