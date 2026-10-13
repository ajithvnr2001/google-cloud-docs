---
url: https://docs.cloud.google.com/ruby/docs/reference/signet/latest/Signet-OAuth1/
title: signet - Module Signet::OAuth1 (v0.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:50.250671+00:00
---

# signet - Module Signet::OAuth1 (v0.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/signet/latest/Signet-OAuth1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  signet - Module Signet::OAuth1 (v0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.21.0  0.20.0 

Reference documentation and code samples for the signet module Signet::OAuth1.

:nodoc:

## Methods 

### .encode
    
    
    def self.encode(value) -> String

Converts a value to a percent-encoded `String` according to the rules given in RFC 5849. All non-unreserved characters are percent-encoded.

**Parameter**

  * **value** (Symbol, #to_str) — The value to be encoded. 



**Returns**

  * (String) — The percent-encoded value. 



### .extract_credential_key_option
    
    
    def self.extract_credential_key_option(credential_type, options) -> String

Processes an options `Hash` to find a credential key value. Allows for greater flexibility in configuration.

**Parameter**

  * **credential_type** (Symbol) — One of `:client`, `:temporary`, `:token`, `:consumer`, `:request`, or `:access`. 



**Returns**

  * (String) — The credential key value. 



### .extract_credential_secret_option
    
    
    def self.extract_credential_secret_option(credential_type, options) -> String

Processes an options `Hash` to find a credential secret value. Allows for greater flexibility in configuration.

**Parameter**

  * **credential_type** (Symbol) — One of `:client`, `:temporary`, `:token`, `:consumer`, `:request`, or `:access`. 



**Returns**

  * (String) — The credential secret value. 



### .generate_authorization_header
    
    
    def self.generate_authorization_header(parameters, realm = nil) -> String

Generates an `Authorization` header from a parameter list according to the rules given in RFC 5849.

**Parameters**

  * **parameters** (Enumerable) — The OAuth parameter list. 
  * **realm** (String) — The `Authorization` realm. See RFC 2617. 



**Returns**

  * (String) — The `Authorization` header. 



### .generate_authorization_uri
    
    
    def self.generate_authorization_uri(authorization_uri, options = {}) -> String

Appends the optional 'oauth_token' and 'oauth_callback' parameters to the base authorization URI.

**Parameter**

  * **authorization_uri** (Addressable::URI, String, #to_str) — The base authorization URI. 



**Returns**

  * (String) — The authorization URI to redirect the user to. 



### .generate_base_string
    
    
    def self.generate_base_string(method, uri, parameters) -> String

Generates a signature base string according to the algorithm given in RFC 5849. Joins the method, URI, and normalized parameter string with '&' characters.

**Parameters**

  * **method** (String) — The HTTP method. 
  * **uri** (Addressable::URI, String, #to_str) — The URI. 
  * **parameters** (Enumerable) — The OAuth parameter list. 



**Returns**

  * (String) — The signature base string. 



**Raises**

  * (TypeError) 



### .generate_nonce
    
    
    def self.generate_nonce() -> String

Returns a nonce suitable for use as an `'oauth_nonce'` value.

**Returns**

  * (String) — A random nonce. 



### .generate_timestamp
    
    
    def self.generate_timestamp() -> String

Returns a timestamp suitable for use as an `'oauth_timestamp'` value.

**Returns**

  * (String) — The current timestamp. 



### .normalize_parameters
    
    
    def self.normalize_parameters(parameters) -> String

Normalizes a set of OAuth parameters according to the algorithm given in RFC 5849. Sorts key/value pairs lexically by byte order, first by key, then by value, joins key/value pairs with the '=' character, then joins the entire parameter list with '&' characters.

**Parameter**

  * **parameters** (Enumerable) — The OAuth parameter list. 



**Returns**

  * (String) — The normalized parameter list. 



**Raises**

  * (TypeError) 



### .parse_authorization_header
    
    
    def self.parse_authorization_header(field_value)

Parses an `Authorization` header into its component parameters. Parameter keys and values are decoded according to the rules given in RFC 5849.

**Raises**

  * (TypeError) 



### .parse_form_encoded_credentials
    
    
    def self.parse_form_encoded_credentials(body) -> Signet::OAuth1::Credential

Parses an `application/x-www-form-urlencoded` HTTP response body into an OAuth key/secret pair.

**Parameter**

  * **body** (String) — The response body. 



**Returns**

  * ([Signet::OAuth1::Credential](https://docs.cloud.google.com/ruby/docs/reference/signet/latest/Signet-OAuth1-Credential)) — The OAuth credentials. 



**Raises**

  * (TypeError) 



### .sign_parameters
    
    
    def self.sign_parameters(method, uri, parameters, client_credential_secret, token_credential_secret = nil) -> String

Generates an OAuth signature using the signature method indicated in the parameter list. Unsupported signature methods will result in a `NotImplementedError` exception being raised.

**Parameters**

  * **method** (String) — The HTTP method. 
  * **uri** (Addressable::URI, String, #to_str) — The URI. 
  * **parameters** (Enumerable) — The OAuth parameter list. 
  * **client_credential_secret** (String) — The client credential secret. 
  * **token_credential_secret** (String) — The token credential secret. Omitted when unavailable. 



**Returns**

  * (String) — The signature. 



### .unencode
    
    
    def self.unencode(value) -> String

Converts a percent-encoded String to an unencoded value.

**Parameter**

  * **value** (#to_str) — The percent-encoded `String` to be unencoded. 



**Returns**

  * (String) — The unencoded value. 



### .unsigned_resource_parameters
    
    
    def self.unsigned_resource_parameters(options = {}) -> Array

Generates an OAuth parameter list to be used when requesting a protected resource.

**Parameter**

  * **options** (Hash) — 

The configuration parameters for the request.

    * `:client_credential_key` \- The client credential key.
    * `:token_credential_key` \- The token credential key.
    * `:signature_method` \- The signature method. Defaults to `'HMAC-SHA1'`.
    * `:two_legged` \- A switch for two-legged OAuth. Defaults to `false`.



**Returns**

  * (Array) — The parameter list as an `Array` of key/value pairs. 



**Raises**

  * (ArgumentError) 



### .unsigned_temporary_credential_parameters
    
    
    def self.unsigned_temporary_credential_parameters(options = {}) -> Array

Generates an OAuth parameter list to be used when obtaining a set of temporary credentials.

**Parameter**

  * **options** (Hash) — 

The configuration parameters for the request.

    * `:client_credential_key` \- The client credential key.
    * `:callback` \- The OAuth callback. Defaults to [OUT_OF_BAND](https://docs.cloud.google.com/ruby/docs/reference/signet/latest/Signet-OAuth1#Signet__OAuth1__OUT_OF_BAND "Signet::OAuth1::OUT_OF_BAND \(constant\)").
    * `:signature_method` \- The signature method. Defaults to `'HMAC-SHA1'`.
    * `:additional_parameters` \- Non-standard additional parameters.



**Returns**

  * (Array) — The parameter list as an `Array` of key/value pairs. 



**Raises**

  * (ArgumentError) 



### .unsigned_token_credential_parameters
    
    
    def self.unsigned_token_credential_parameters(options = {}) -> Array

Generates an OAuth parameter list to be used when obtaining a set of token credentials.

**Parameter**

  * **options** (Hash) — 

The configuration parameters for the request.

    * `:client_credential_key` \- The client credential key.
    * `:temporary_credential_key` \- The temporary credential key.
    * `:verifier` \- The OAuth verifier.
    * `:signature_method` \- The signature method. Defaults to `'HMAC-SHA1'`.



**Returns**

  * (Array) — The parameter list as an `Array` of key/value pairs. 



**Raises**

  * (ArgumentError) 



## Constants 

### OUT_OF_BAND

**value:** "oob".freeze

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-04 UTC."],[],[]] 
