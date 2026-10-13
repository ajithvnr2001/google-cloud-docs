---
url: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeyInfo/
title: googleauth - Class Google::Auth::IDTokens::KeyInfo (v1.17.4) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:47.255529+00:00
---

# googleauth - Class Google::Auth::IDTokens::KeyInfo (v1.17.4)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeyInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  googleauth - Class Google::Auth::IDTokens::KeyInfo (v1.17.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.4 (latest)  1.17.3  1.16.2  1.15.1  1.14.0  1.13.1  1.12.2 

Reference documentation and code samples for the googleauth class Google::Auth::IDTokens::KeyInfo.

A public key used for verifying ID tokens.

This includes the public key data, ID, and the algorithm used for signature verification. RSA and Elliptical Curve (EC) keys are supported.

## Inherits

  * Object 



## Methods 

### .from_jwk
    
    
    def self.from_jwk(jwk) -> KeyInfo

Create a KeyInfo from a single JWK, which may be given as either a hash or an unparsed JSON string.

**Parameter**

  * **jwk** (Hash, String) — The JWK specification. 



**Returns**

  * ([KeyInfo](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeyInfo)) 



**Raises**

  * ([Google::Auth::IDTokens::KeySourceError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeySourceError)) — If the key could not be extracted from the JWK due to invalid type, malformed JSON, or invalid key data. 



### .from_jwk_set
    
    
    def self.from_jwk_set(jwk_set) -> Array<KeyInfo>

Create an array of KeyInfo from a JWK Set, which may be given as either a hash or an unparsed JSON string.

**Parameter**

  * **jwk_set** (Hash, String) — The JWK Set specification. 



**Returns**

  * (Array<[KeyInfo](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeyInfo)>) 



**Raises**

  * ([Google::Auth::IDTokens::KeySourceError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeySourceError)) — If a key could not be extracted from the JWK Set, or if the set contains no keys. 



### #algorithm
    
    
    def algorithm() -> String

The signature algorithm. (normally `RS256` or `ES256`)

**Returns**

  * (String) 



### #id
    
    
    def id() -> String

The key ID.

**Returns**

  * (String) 



### #initialize
    
    
    def initialize(id: nil, key: nil, algorithm: nil) -> KeyInfo

Create a public key info structure.

**Parameters**

  * **id** (String) _(defaults to: nil)_ — The key ID. 
  * **key** (OpenSSL::PKey::RSA, OpenSSL::PKey::EC) _(defaults to: nil)_ — The key itself. 
  * **algorithm** (String) _(defaults to: nil)_ — The algorithm (normally `RS256` or `ES256`) 



**Returns**

  * ([KeyInfo](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens-KeyInfo)) — a new instance of KeyInfo 



### #key
    
    
    def key() -> OpenSSL::PKey::RSA, OpenSSL::PKey::EC

The key itself.

**Returns**

  * (OpenSSL::PKey::RSA, OpenSSL::PKey::EC) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
