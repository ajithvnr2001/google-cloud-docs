---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.UrlMapOrBuilder
title: Interface UrlMapOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:04.265240+00:00
---

# Interface UrlMapOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.UrlMapOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UrlMapOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.4  2.2.0  2.1.10  0.2.0 
    
    
    public interface UrlMapOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApiEndpoint()
    
    
    public abstract ApiEndpointHandler getApiEndpoint()

Uses API Endpoints to handle requests.

`.google.appengine.v1.ApiEndpointHandler api_endpoint = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ApiEndpointHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ApiEndpointHandler)` | The apiEndpoint.  
  
### getApiEndpointOrBuilder()
    
    
    public abstract ApiEndpointHandlerOrBuilder getApiEndpointOrBuilder()

Uses API Endpoints to handle requests.

`.google.appengine.v1.ApiEndpointHandler api_endpoint = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ApiEndpointHandlerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ApiEndpointHandlerOrBuilder)` |   
  
### getAuthFailAction()
    
    
    public abstract AuthFailAction getAuthFailAction()

Action to take when users access resources that require authentication. Defaults to `redirect`.

`.google.appengine.v1.AuthFailAction auth_fail_action = 7;`

**Returns**  
---  
**Type** | **Description**  
`[AuthFailAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.AuthFailAction)` | The authFailAction.  
  
### getAuthFailActionValue()
    
    
    public abstract int getAuthFailActionValue()

Action to take when users access resources that require authentication. Defaults to `redirect`.

`.google.appengine.v1.AuthFailAction auth_fail_action = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for authFailAction.  
  
### getHandlerTypeCase()
    
    
    public abstract UrlMap.HandlerTypeCase getHandlerTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[UrlMap.HandlerTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.UrlMap.HandlerTypeCase)` |   
  
### getLogin()
    
    
    public abstract LoginRequirement getLogin()

Level of login required to access this resource. Not supported for Node.js in the App Engine standard environment.

`.google.appengine.v1.LoginRequirement login = 6;`

**Returns**  
---  
**Type** | **Description**  
`[LoginRequirement](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.LoginRequirement)` | The login.  
  
### getLoginValue()
    
    
    public abstract int getLoginValue()

Level of login required to access this resource. Not supported for Node.js in the App Engine standard environment.

`.google.appengine.v1.LoginRequirement login = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for login.  
  
### getRedirectHttpResponseCode()
    
    
    public abstract UrlMap.RedirectHttpResponseCode getRedirectHttpResponseCode()

`30x` code to use when performing redirects for the `secure` field. Defaults to `302`.

`.google.appengine.v1.UrlMap.RedirectHttpResponseCode redirect_http_response_code = 8; `

**Returns**  
---  
**Type** | **Description**  
`[UrlMap.RedirectHttpResponseCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.UrlMap.RedirectHttpResponseCode)` | The redirectHttpResponseCode.  
  
### getRedirectHttpResponseCodeValue()
    
    
    public abstract int getRedirectHttpResponseCodeValue()

`30x` code to use when performing redirects for the `secure` field. Defaults to `302`.

`.google.appengine.v1.UrlMap.RedirectHttpResponseCode redirect_http_response_code = 8; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for redirectHttpResponseCode.  
  
### getScript()
    
    
    public abstract ScriptHandler getScript()

Executes a script to handle the requests that match this URL pattern. Only the `auto` value is supported for Node.js in the App Engine standard environment, for example `"script": "auto"`.

`.google.appengine.v1.ScriptHandler script = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ScriptHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ScriptHandler)` | The script.  
  
### getScriptOrBuilder()
    
    
    public abstract ScriptHandlerOrBuilder getScriptOrBuilder()

Executes a script to handle the requests that match this URL pattern. Only the `auto` value is supported for Node.js in the App Engine standard environment, for example `"script": "auto"`.

`.google.appengine.v1.ScriptHandler script = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ScriptHandlerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ScriptHandlerOrBuilder)` |   
  
### getSecurityLevel()
    
    
    public abstract SecurityLevel getSecurityLevel()

Security (HTTPS) enforcement for this URL.

`.google.appengine.v1.SecurityLevel security_level = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.SecurityLevel)` | The securityLevel.  
  
### getSecurityLevelValue()
    
    
    public abstract int getSecurityLevelValue()

Security (HTTPS) enforcement for this URL.

`.google.appengine.v1.SecurityLevel security_level = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for securityLevel.  
  
### getStaticFiles()
    
    
    public abstract StaticFilesHandler getStaticFiles()

Returns the contents of a file, such as an image, as the response.

`.google.appengine.v1.StaticFilesHandler static_files = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StaticFilesHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.StaticFilesHandler)` | The staticFiles.  
  
### getStaticFilesOrBuilder()
    
    
    public abstract StaticFilesHandlerOrBuilder getStaticFilesOrBuilder()

Returns the contents of a file, such as an image, as the response.

`.google.appengine.v1.StaticFilesHandler static_files = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StaticFilesHandlerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.StaticFilesHandlerOrBuilder)` |   
  
### getUrlRegex()
    
    
    public abstract String getUrlRegex()

URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings. All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.

`string url_regex = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The urlRegex.  
  
### getUrlRegexBytes()
    
    
    public abstract ByteString getUrlRegexBytes()

URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings. All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.

`string url_regex = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for urlRegex.  
  
### hasApiEndpoint()
    
    
    public abstract boolean hasApiEndpoint()

Uses API Endpoints to handle requests.

`.google.appengine.v1.ApiEndpointHandler api_endpoint = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the apiEndpoint field is set.  
  
### hasScript()
    
    
    public abstract boolean hasScript()

Executes a script to handle the requests that match this URL pattern. Only the `auto` value is supported for Node.js in the App Engine standard environment, for example `"script": "auto"`.

`.google.appengine.v1.ScriptHandler script = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the script field is set.  
  
### hasStaticFiles()
    
    
    public abstract boolean hasStaticFiles()

Returns the contents of a file, such as an image, as the response.

`.google.appengine.v1.StaticFilesHandler static_files = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the staticFiles field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
