---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/collect/
title: Method: projects.locations.catalogs.userEvents.collect \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:17.804123+00:00
---

# Method: projects.locations.catalogs.userEvents.collect  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/collect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.userEvents.collect Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Writes a single user event from the browser.

For larger user event payload over 16 KB, the POST method should be used instead, otherwise a 400 Bad Request error is returned.

This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly.

### HTTP request

`GET https://retail.googleapis.com/v2/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent catalog name, such as `projects/1234/locations/global/catalogs/default_catalog`.  
  
### Query parameters

Parameters  
---  
`userEvent` |  `string` Required. URL encoded UserEvent proto with a length limit of 2,000,000 characters.  
`uri` |  `string` The URL including cgi-parameters but excluding the hash fragment with a length limit of 5,000 characters. This is often more useful than the referer URL, because many browsers only send the domain for 3rd party requests.  
`ets` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The event timestamp in milliseconds. This prevents browser caching of otherwise identical get requests. The name is abbreviated to reduce the payload bytes.  
`rawJson` |  `string` An arbitrary serialized JSON string that contains necessary information that can comprise a user event. When this field is specified, the userEvent field will be ignored. Note: line-delimited JSON is not supported, a single JSON only.  
Union parameter `conversion_rule`. The rule that can convert the raw_json to a user event. It is needed only when the raw_json is set. `conversion_rule` can be only one of the following:  
`prebuiltRule` |  `string` The prebuilt rule name that can convert a specific type of rawJson. For example: "ga4_bq" rule for the GA4 user event schema.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
