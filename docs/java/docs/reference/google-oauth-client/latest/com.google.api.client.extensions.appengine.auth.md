---
url: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth
title: Package com.google.api.client.extensions.appengine.auth (1.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:58.491034+00:00
---

# Package com.google.api.client.extensions.appengine.auth (1.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.api.client.extensions.appengine.auth (1.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.39.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth)
  * [ 1.38.2 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.38.2/com.google.api.client.extensions.appengine.auth)
  * [ 1.37.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.37.0/com.google.api.client.extensions.appengine.auth)
  * [ 1.36.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.36.0/com.google.api.client.extensions.appengine.auth)
  * [ 1.34.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.34.1/com.google.api.client.extensions.appengine.auth)
  * [ 1.33.3 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.33.3/com.google.api.client.extensions.appengine.auth)
  * [ 1.32.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.32.1/com.google.api.client.extensions.appengine.auth)



[com.google.api.client.util.Beta](https://cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta.html)   
These servlets will allow an App Engine user to quickly get started with the auth object interface from the main client. They will utilize the App Engine Datastore and Credentials to manage credentials on behalf of users.

Warning: starting with version 1.7, usage of this for OAuth 2.0 is deprecated. Instead use [com.google.api.client.extensions.appengine.auth.oauth2](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth.oauth2).

## Classes 

### [AbstractAppEngineCallbackServlet](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth.AbstractAppEngineCallbackServlet)

Beta   
This servlet fills in some of the required information for the [AbstractCallbackServlet](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.servlet.auth.AbstractCallbackServlet) with reasonable defaults for App Engine. It will default the servlet to creating UrlFetchTransport objects whenever an HttpTransport is needed. It will also default the user identifier to the logged in App Engine user. This servlet requires that the App Engine user must be logged in to work correctly. This can be accomplished by adding a security constraint in your web.xml for the path at which this servlet will live.

Example that requires login for all pages:
    
    
     
     <security-constraint>
     <web-resource-collection>
     <web-resource-name>any</web-resource-name>
     <url-pattern>/*</url-pattern>
     </web-resource-collection>
     <auth-constraint>
     <role-name>*</role-name>
     </auth-constraint>
     </security-constraint>
     
     

Warning: starting with version 1.7, usage of this for OAuth 2.0 is deprecated. Instead use [com.google.api.client.extensions.appengine.auth.oauth2.AbstractAppEngineAuthorizationCodeCallbackServlet](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth.oauth2.AbstractAppEngineAuthorizationCodeCallbackServlet).

### [AbstractAppEngineFlowServlet](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth.AbstractAppEngineFlowServlet)

Beta   
This class fills in some of the unknowns of the generic [AbstractFlowUserServlet](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.servlet.auth.AbstractFlowUserServlet) with reasonable defaults for App Engine. This servlet requires that the App Engine user must be logged in to work correctly.

Warning: starting with version 1.7, usage of this for OAuth 2.0 is deprecated. Instead use [com.google.api.client.extensions.appengine.auth.oauth2.AbstractAppEngineAuthorizationCodeServlet](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.appengine.auth.oauth2.AbstractAppEngineAuthorizationCodeServlet).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
