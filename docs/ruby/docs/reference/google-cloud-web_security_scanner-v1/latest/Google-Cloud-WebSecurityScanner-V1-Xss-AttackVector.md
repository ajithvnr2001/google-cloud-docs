---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1/latest/Google-Cloud-WebSecurityScanner-V1-Xss-AttackVector/
title: Web Security Scanner V1 API - Module Google::Cloud::WebSecurityScanner::V1::Xss::AttackVector (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:39.582786+00:00
---

# Web Security Scanner V1 API - Module Google::Cloud::WebSecurityScanner::V1::Xss::AttackVector (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1/latest/Google-Cloud-WebSecurityScanner-V1-Xss-AttackVector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Web Security Scanner V1 API - Module Google::Cloud::WebSecurityScanner::V1::Xss::AttackVector (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.1  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.1  0.3.5 

Reference documentation and code samples for the Web Security Scanner V1 API module Google::Cloud::WebSecurityScanner::V1::Xss::AttackVector.

Types of XSS attack vector.

## Constants 

### ATTACK_VECTOR_UNSPECIFIED

**value:** 0  
Unknown attack vector.

### LOCAL_STORAGE

**value:** 1  
The attack comes from fuzzing the browser's localStorage.

### SESSION_STORAGE

**value:** 2  
The attack comes from fuzzing the browser's sessionStorage.

### WINDOW_NAME

**value:** 3  
The attack comes from fuzzing the window's name property.

### REFERRER

**value:** 4  
The attack comes from fuzzing the referrer property.

### FORM_INPUT

**value:** 5  
The attack comes from fuzzing an input element.

### COOKIE

**value:** 6  
The attack comes from fuzzing the browser's cookies.

### POST_MESSAGE

**value:** 7  
The attack comes from hijacking the post messaging mechanism.

### GET_PARAMETERS

**value:** 8  
The attack comes from fuzzing parameters in the url.

### URL_FRAGMENT

**value:** 9  
The attack comes from fuzzing the fragment in the url.

### HTML_COMMENT

**value:** 10  
The attack comes from fuzzing the HTML comments.

### POST_PARAMETERS

**value:** 11  
The attack comes from fuzzing the POST parameters.

### PROTOCOL

**value:** 12  
The attack comes from fuzzing the protocol.

### STORED_XSS

**value:** 13  
The attack comes from the server side and is stored.

### SAME_ORIGIN

**value:** 14  
The attack is a Same-Origin Method Execution attack via a GET parameter.

### USER_CONTROLLABLE_URL

**value:** 15  
The attack payload is received from a third-party host via a URL that is user-controllable

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
