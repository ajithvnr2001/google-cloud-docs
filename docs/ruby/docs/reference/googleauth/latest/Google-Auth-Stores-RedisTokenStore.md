---
url: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Stores-RedisTokenStore/
title: googleauth - Class Google::Auth::Stores::RedisTokenStore (v1.17.4) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:36.013346+00:00
---

# googleauth - Class Google::Auth::Stores::RedisTokenStore (v1.17.4)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Stores-RedisTokenStore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  googleauth - Class Google::Auth::Stores::RedisTokenStore (v1.17.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.4 (latest)  1.17.3  1.16.2  1.15.1  1.14.0  1.13.1  1.12.2 

Reference documentation and code samples for the googleauth class Google::Auth::Stores::RedisTokenStore.

Implementation of user token storage backed by Redis. Tokens are stored as JSON using the supplied key, prefixed with `g-user-token:`

## Inherits

  * [Google::Auth::TokenStore](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-TokenStore)



## Methods 

### #delete
    
    
    def delete(id)

### #initialize
    
    
    def initialize(options = {}) -> RedisTokenStore

Create a new store with the supplied redis client.

**Parameters**

  * **redis** (::Redis, String) — Initialized redis client to connect to. 
  * **prefix** (String) — Prefix for keys in redis. Defaults to 'g-user-token:' 



**Returns**

  * ([RedisTokenStore](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Stores-RedisTokenStore)) — a new instance of RedisTokenStore 



### #load
    
    
    def load(id)

### #store
    
    
    def store(id, token)

## Constants 

### DEFAULT_KEY_PREFIX

**value:** "g-user-token:".freeze

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
