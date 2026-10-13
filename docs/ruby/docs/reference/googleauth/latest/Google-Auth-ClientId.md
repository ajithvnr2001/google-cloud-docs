---
url: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-ClientId/
title: googleauth - Class Google::Auth::ClientId (v1.17.4) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:54.271106+00:00
---

# googleauth - Class Google::Auth::ClientId (v1.17.4)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-ClientId/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  googleauth - Class Google::Auth::ClientId (v1.17.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.4 (latest)  1.17.3  1.16.2  1.15.1  1.14.0  1.13.1  1.12.2 

Reference documentation and code samples for the googleauth class Google::Auth::ClientId.

Representation of an application's identity for user authorization flows.

## Inherits

  * Object 



## Methods 

### .default
    
    
    def self.default()

Returns the value of attribute default.

### .default=
    
    
    def self.default=(value)

Sets the attribute default

### .from_file
    
    
    def self.from_file(file) -> Google::Auth::ClientID

Constructs a Client ID from a JSON file downloaded from the Google Developers Console.

**Parameter**

  * **file** (String, File) — Path of file to read from 



**Returns**

  * (Google::Auth::ClientID) 



**Raises**

  * ([Google::Auth::InitializationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-InitializationError)) — If file is nil 



### .from_hash
    
    
    def self.from_hash(config) -> Google::Auth::ClientID

Constructs a Client ID from a previously loaded JSON file. The hash structure should match the expected JSON format.

**Parameter**

  * **config** (hash) — Parsed contents of the JSON file 



**Returns**

  * (Google::Auth::ClientID) 



**Raises**

  * ([Google::Auth::InitializationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-InitializationError)) — If config is nil or missing required elements 



### #id
    
    
    def id() -> String

Text identifier of the client ID

**Returns**

  * (String) 



### #initialize
    
    
    def initialize(id, secret) -> ClientId

Initialize the Client ID. Both id and secret must be non-nil.

**Parameters**

  * **id** (String) — Text identifier of the client ID 
  * **secret** (String) — Secret associated with the client ID 



**Returns**

  * ([ClientId](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-ClientId)) — a new instance of ClientId 



**Raises**

  * ([Google::Auth::InitializationError](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-InitializationError)) — If id or secret is nil 



### #secret
    
    
    def secret() -> String

Secret associated with the client ID

**Returns**

  * (String) 



## Constants 

### INSTALLED_APP

**value:** "installed".freeze  
Toplevel JSON key for the an installed app configuration. Must include client_id and client_secret subkeys if present.

### WEB_APP

**value:** "web".freeze  
Toplevel JSON key for the a webapp configuration. Must include client_id and client_secret subkeys if present.

### CLIENT_ID

**value:** "client_id".freeze  
JSON key for the client ID within an app configuration.

### CLIENT_SECRET

**value:** "client_secret".freeze  
JSON key for the client secret within an app configuration.

### MISSING_TOP_LEVEL_ELEMENT_ERROR

**value:** "Expected top level property 'installed' or 'web' to be present.".freeze  
An error message raised when none of the expected toplevel properties can be found.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
