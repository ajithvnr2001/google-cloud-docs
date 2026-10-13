---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Finding/
title: Web Security Scanner V1beta API - Class Google::Cloud::WebSecurityScanner::V1beta::Finding (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:22.220139+00:00
---

# Web Security Scanner V1beta API - Class Google::Cloud::WebSecurityScanner::V1beta::Finding (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Finding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Web Security Scanner V1beta API - Class Google::Cloud::WebSecurityScanner::V1beta::Finding (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Web Security Scanner V1beta API class Google::Cloud::WebSecurityScanner::V1beta::Finding.

A Finding resource represents a vulnerability instance identified during a ScanRun.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #body
    
    
    def body() -> ::String

**Returns**

  * (::String) — The body of the request that triggered the vulnerability. 



### #body=
    
    
    def body=(value) -> ::String

**Parameter**

  * **value** (::String) — The body of the request that triggered the vulnerability. 



**Returns**

  * (::String) — The body of the request that triggered the vulnerability. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The description of the vulnerability. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The description of the vulnerability. 



**Returns**

  * (::String) — The description of the vulnerability. 



### #final_url
    
    
    def final_url() -> ::String

**Returns**

  * (::String) — The URL where the browser lands when the vulnerability is detected. 



### #final_url=
    
    
    def final_url=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL where the browser lands when the vulnerability is detected. 



**Returns**

  * (::String) — The URL where the browser lands when the vulnerability is detected. 



### #finding_type
    
    
    def finding_type() -> ::String

**Returns**

  * (::String) — The type of the Finding. Detailed and up-to-date information on findings can be found here: https://cloud.google.com/security-scanner/docs/scan-result-details 



### #finding_type=
    
    
    def finding_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of the Finding. Detailed and up-to-date information on findings can be found here: https://cloud.google.com/security-scanner/docs/scan-result-details 



**Returns**

  * (::String) — The type of the Finding. Detailed and up-to-date information on findings can be found here: https://cloud.google.com/security-scanner/docs/scan-result-details 



### #form
    
    
    def form() -> ::Google::Cloud::WebSecurityScanner::V1beta::Form

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::Form](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Form)) — An addon containing information reported for a vulnerability with an HTML form, if any. 



### #form=
    
    
    def form=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::Form

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::Form](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Form)) — An addon containing information reported for a vulnerability with an HTML form, if any. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::Form](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Form)) — An addon containing information reported for a vulnerability with an HTML form, if any. 



### #frame_url
    
    
    def frame_url() -> ::String

**Returns**

  * (::String) — If the vulnerability was originated from nested IFrame, the immediate parent IFrame is reported. 



### #frame_url=
    
    
    def frame_url=(value) -> ::String

**Parameter**

  * **value** (::String) — If the vulnerability was originated from nested IFrame, the immediate parent IFrame is reported. 



**Returns**

  * (::String) — If the vulnerability was originated from nested IFrame, the immediate parent IFrame is reported. 



### #fuzzed_url
    
    
    def fuzzed_url() -> ::String

**Returns**

  * (::String) — The URL produced by the server-side fuzzer and used in the request that triggered the vulnerability. 



### #fuzzed_url=
    
    
    def fuzzed_url=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL produced by the server-side fuzzer and used in the request that triggered the vulnerability. 



**Returns**

  * (::String) — The URL produced by the server-side fuzzer and used in the request that triggered the vulnerability. 



### #http_method
    
    
    def http_method() -> ::String

**Returns**

  * (::String) — The http method of the request that triggered the vulnerability, in uppercase. 



### #http_method=
    
    
    def http_method=(value) -> ::String

**Parameter**

  * **value** (::String) — The http method of the request that triggered the vulnerability, in uppercase. 



**Returns**

  * (::String) — The http method of the request that triggered the vulnerability, in uppercase. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The resource name of the Finding. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{scanRunId}/findings/{findingId}'. The finding IDs are generated by the system. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the Finding. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{scanRunId}/findings/{findingId}'. The finding IDs are generated by the system. 



**Returns**

  * (::String) — The resource name of the Finding. The name follows the format of 'projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{scanRunId}/findings/{findingId}'. The finding IDs are generated by the system. 



### #outdated_library
    
    
    def outdated_library() -> ::Google::Cloud::WebSecurityScanner::V1beta::OutdatedLibrary

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::OutdatedLibrary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-OutdatedLibrary)) — An addon containing information about outdated libraries. 



### #outdated_library=
    
    
    def outdated_library=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::OutdatedLibrary

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::OutdatedLibrary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-OutdatedLibrary)) — An addon containing information about outdated libraries. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::OutdatedLibrary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-OutdatedLibrary)) — An addon containing information about outdated libraries. 



### #reproduction_url
    
    
    def reproduction_url() -> ::String

**Returns**

  * (::String) — The URL containing human-readable payload that user can leverage to reproduce the vulnerability. 



### #reproduction_url=
    
    
    def reproduction_url=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL containing human-readable payload that user can leverage to reproduce the vulnerability. 



**Returns**

  * (::String) — The URL containing human-readable payload that user can leverage to reproduce the vulnerability. 



### #tracking_id
    
    
    def tracking_id() -> ::String

**Returns**

  * (::String) — The tracking ID uniquely identifies a vulnerability instance across multiple ScanRuns. 



### #tracking_id=
    
    
    def tracking_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The tracking ID uniquely identifies a vulnerability instance across multiple ScanRuns. 



**Returns**

  * (::String) — The tracking ID uniquely identifies a vulnerability instance across multiple ScanRuns. 



### #violating_resource
    
    
    def violating_resource() -> ::Google::Cloud::WebSecurityScanner::V1beta::ViolatingResource

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::ViolatingResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ViolatingResource)) — An addon containing detailed information regarding any resource causing the vulnerability such as JavaScript sources, image, audio files, etc. 



### #violating_resource=
    
    
    def violating_resource=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::ViolatingResource

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::ViolatingResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ViolatingResource)) — An addon containing detailed information regarding any resource causing the vulnerability such as JavaScript sources, image, audio files, etc. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::ViolatingResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ViolatingResource)) — An addon containing detailed information regarding any resource causing the vulnerability such as JavaScript sources, image, audio files, etc. 



### #vulnerable_headers
    
    
    def vulnerable_headers() -> ::Google::Cloud::WebSecurityScanner::V1beta::VulnerableHeaders

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::VulnerableHeaders](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-VulnerableHeaders)) — An addon containing information about vulnerable or missing HTTP headers. 



### #vulnerable_headers=
    
    
    def vulnerable_headers=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::VulnerableHeaders

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::VulnerableHeaders](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-VulnerableHeaders)) — An addon containing information about vulnerable or missing HTTP headers. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::VulnerableHeaders](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-VulnerableHeaders)) — An addon containing information about vulnerable or missing HTTP headers. 



### #vulnerable_parameters
    
    
    def vulnerable_parameters() -> ::Google::Cloud::WebSecurityScanner::V1beta::VulnerableParameters

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::VulnerableParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-VulnerableParameters)) — An addon containing information about request parameters which were found to be vulnerable. 



### #vulnerable_parameters=
    
    
    def vulnerable_parameters=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::VulnerableParameters

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::VulnerableParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-VulnerableParameters)) — An addon containing information about request parameters which were found to be vulnerable. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::VulnerableParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-VulnerableParameters)) — An addon containing information about request parameters which were found to be vulnerable. 



### #xss
    
    
    def xss() -> ::Google::Cloud::WebSecurityScanner::V1beta::Xss

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::Xss](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Xss)) — An addon containing information reported for an XSS, if any. 



### #xss=
    
    
    def xss=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::Xss

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::Xss](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Xss)) — An addon containing information reported for an XSS, if any. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::Xss](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-Xss)) — An addon containing information reported for an XSS, if any. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
