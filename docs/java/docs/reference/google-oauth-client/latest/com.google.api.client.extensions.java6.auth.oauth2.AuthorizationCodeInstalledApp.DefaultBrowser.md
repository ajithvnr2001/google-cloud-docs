---
url: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser
title: Class AuthorizationCodeInstalledApp.DefaultBrowser (1.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:03.638787+00:00
---

# Class AuthorizationCodeInstalledApp.DefaultBrowser (1.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuthorizationCodeInstalledApp.DefaultBrowser (1.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.39.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)
  * [ 1.38.2 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.38.2/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)
  * [ 1.37.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.37.0/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)
  * [ 1.36.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.36.0/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)
  * [ 1.34.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.34.1/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)
  * [ 1.33.3 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.33.3/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)
  * [ 1.32.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.32.1/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.DefaultBrowser)


    
    
    public static class AuthorizationCodeInstalledApp.DefaultBrowser implements AuthorizationCodeInstalledApp.Browser

Default browser that just delegates to [AuthorizationCodeInstalledApp#browse(String)](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp#com_google_api_client_extensions_java6_auth_oauth2_AuthorizationCodeInstalledApp_browse_java_lang_String_).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AuthorizationCodeInstalledApp.DefaultBrowser

## Implements

[AuthorizationCodeInstalledApp.Browser](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.java6.auth.oauth2.AuthorizationCodeInstalledApp.Browser)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### DefaultBrowser()
    
    
    public DefaultBrowser()

## Methods 

### browse(String url)
    
    
    public void browse(String url)

**Parameter**  
---  
**Name** | **Description**  
`url` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
