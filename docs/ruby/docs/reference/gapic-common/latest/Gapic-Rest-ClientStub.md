---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ClientStub/
title: gapic-common - Class Gapic::Rest::ClientStub (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:13.881990+00:00
---

# gapic-common - Class Gapic::Rest::ClientStub (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ClientStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Rest::ClientStub (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Rest::ClientStub.

A class for making REST calls through Faraday ClientStub's responsibilities:

  * wrap Faraday methods with a bounded explicit interface
  * store service endpoint and create full url for the request
  * store credentials and add auth information to the request



## Inherits

  * Object 



## Includes

  * [Gapic::LoggingConcerns](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-LoggingConcerns)
  * [Gapic::UniverseDomainConcerns](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-UniverseDomainConcerns)



## Methods 

### #initialize
    
    
    def initialize(credentials:, endpoint: nil, endpoint_template: nil, universe_domain: nil, numeric_enums: false, raise_faraday_errors: true, logging_system: nil, service_name: nil, logger: :default) -> ClientStub

Initializes with an endpoint and credentials

**Parameters**

  * **endpoint** (String) _(defaults to: nil)_ — The endpoint of the API. Overrides any endpoint_template. 
  * **endpoint_template** (String) _(defaults to: nil)_ — The endpoint of the API, where the universe domain component of the hostname is marked by the string in the constant [UniverseDomainConcerns::ENDPOINT_SUBSTITUTION](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-UniverseDomainConcerns#Gapic__UniverseDomainConcerns__ENDPOINT_SUBSTITUTION "Gapic::UniverseDomainConcerns::ENDPOINT_SUBSTITUTION \(constant\)"). 
  * **universe_domain** (String) _(defaults to: nil)_ — The universe domain in which calls should be made. Defaults to `googleapis.com`. 
  * **credentials** (Google::Auth::Credentials) — Credentials to send with calls in form of a googleauth credentials object. (see the [googleauth docs](https://googleapis.dev/ruby/googleauth/latest/index.html)) 
  * **numeric_enums** (Boolean) _(defaults to: false)_ — Whether to signal the server to JSON-encode enums as ints 
  * **raise_faraday_errors** (Boolean) _(defaults to: true)_ — Whether to raise Faraday errors instead of wrapping them in `Gapic::Rest::Error` Added for backwards compatibility. Default is `true`. All REST clients (except for old versions of `google-cloud-compute-v1`) should explicitly set this parameter to `false`. 
  * **logger** (Logger, :default, nil) _(defaults to: :default)_ — An explicit logger to use, or one of the values `:default` (the default) to construct a default logger, or `nil` to disable logging explicitly. 



**Yields**

  * (Faraday::Connection) 



**Returns**

  * ([ClientStub](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Rest-ClientStub)) — a new instance of ClientStub 



### #make_delete_request
    
    
    def make_delete_request(uri:, params: {}, options: {}, method_name: nil) -> Faraday::Response

Makes a DELETE request

**Parameters**

  * **uri** (String) — uri to send this request to 
  * **params** (Hash) _(defaults to: {})_ — query string parameters for the request 
  * **options** ([::Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: {})_ — gapic options to be applied to the REST call. Currently only timeout and headers are supported. 



**Returns**

  * (Faraday::Response) 



### #make_get_request
    
    
    def make_get_request(uri:, params: {}, options: {}, method_name: nil) -> Faraday::Response

Makes a GET request

**Parameters**

  * **uri** (String) — uri to send this request to 
  * **params** (Hash) _(defaults to: {})_ — query string parameters for the request 
  * **options** ([::Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: {})_ — gapic options to be applied to the REST call. Currently only timeout and headers are supported. 



**Returns**

  * (Faraday::Response) 



### #make_patch_request
    
    
    def make_patch_request(uri:, body:, params: {}, options: {}, method_name: nil) -> Faraday::Response

Makes a PATCH request

**Parameters**

  * **uri** (String) — uri to send this request to 
  * **body** (String) — a body to send with the request, nil for requests without a body 
  * **params** (Hash) _(defaults to: {})_ — query string parameters for the request 
  * **options** ([::Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: {})_ — gapic options to be applied to the REST call. Currently only timeout and headers are supported. 



**Returns**

  * (Faraday::Response) 



### #make_post_request
    
    
    def make_post_request(uri:, body: nil, params: {}, options: {}, method_name: nil) -> Faraday::Response

Makes a POST request

**Parameters**

  * **uri** (String) — uri to send this request to 
  * **body** (String) _(defaults to: nil)_ — a body to send with the request, nil for requests without a body 
  * **params** (Hash) _(defaults to: {})_ — query string parameters for the request 
  * **options** ([::Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: {})_ — gapic options to be applied to the REST call. Currently only timeout and headers are supported. 



**Returns**

  * (Faraday::Response) 



### #make_put_request
    
    
    def make_put_request(uri:, body: nil, params: {}, options: {}, method_name: nil) -> Faraday::Response

Makes a PUT request

**Parameters**

  * **uri** (String) — uri to send this request to 
  * **body** (String) _(defaults to: nil)_ — a body to send with the request, nil for requests without a body 
  * **params** (Hash) _(defaults to: {})_ — query string parameters for the request 
  * **options** ([::Gapic::CallOptions](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-CallOptions), Hash) _(defaults to: {})_ — gapic options to be applied to the REST call. Currently only timeout and headers are supported. 



**Returns**

  * (Faraday::Response) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
