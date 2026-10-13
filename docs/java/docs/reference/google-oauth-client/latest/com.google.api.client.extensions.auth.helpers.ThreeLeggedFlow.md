---
url: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow
title: Interface ThreeLeggedFlow (1.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:04.194443+00:00
---

# Interface ThreeLeggedFlow (1.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ThreeLeggedFlow (1.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.39.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)
  * [ 1.38.2 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.38.2/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)
  * [ 1.37.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.37.0/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)
  * [ 1.36.0 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.36.0/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)
  * [ 1.34.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.34.1/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)
  * [ 1.33.3 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.33.3/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)
  * [ 1.32.1 ](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/1.32.1/com.google.api.client.extensions.auth.helpers.ThreeLeggedFlow)


    
    
    public interface ThreeLeggedFlow

**Deprecated.** _Use[com.google.api.client.auth.oauth2.AuthorizationCodeFlow](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationCodeFlow)._

Beta   
Interface for auth flows that require a user authorization step through a web browser to obtain an authorization code.

Implementations are required to be PersistenceCapable for storage in JDO compliant datastores during user authorization step.

Warning: starting with version 1.7, usage of this for OAuth 2.0 is deprecated. Instead use [com.google.api.client.auth.oauth2.AuthorizationCodeFlow](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.auth.oauth2.AuthorizationCodeFlow).

## Methods 

### complete(String authorizationCode) (deprecated)
    
    
    public abstract Credential complete(String authorizationCode)

After the user has authorized the request, the token or code obtained should be passed to this complete function to allow us to exchange the code with the authentication server for a [Credential](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.Credential).

**Parameter**  
---  
**Name** | **Description**  
`authorizationCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Code or token obtained after the user grants permission  
**Returns**  
---  
**Type** | **Description**  
`[Credential](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.Credential)` | [Credential](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.Credential) object that is obtained from token server  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getAuthorizationUrl() (deprecated)
    
    
    public abstract String getAuthorizationUrl()

After the object is created, the developer should use this method to interrogate it for the authorization URL to which the user should be redirected to obtain permission.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | URL to which the user should be directed  
  
### loadCredential(PersistenceManager pm) (deprecated)
    
    
    public abstract Credential loadCredential(PersistenceManager pm)

Convenience function that will load a credential based on the userId for which this flow was instantiated.

**Parameter**  
---  
**Name** | **Description**  
`pm` | `[PersistenceManager](https://docs.oracle.com/javase/8/docs/api/javax/jdo/PersistenceManager.html)`  
[PersistenceManager](https://docs.oracle.com/javase/8/docs/api/javax/jdo/PersistenceManager.html) instance which this flow should use to interact with the data store. The caller must remember to call PersistenceManager#close() after this method returns.  
**Returns**  
---  
**Type** | **Description**  
`[Credential](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.Credential)` | Fully initialized [Credential](https://docs.cloud.google.com/java/docs/reference/google-oauth-client/latest/com.google.api.client.extensions.auth.helpers.Credential) object or `null` if none exists.  
  
### setHttpTransport(HttpTransport transport) (deprecated)
    
    
    public abstract void setHttpTransport(HttpTransport transport)

Set HttpTransport instance for this three legged flow.

**Parameter**  
---  
**Name** | **Description**  
`transport` | `com.google.api.client.http.HttpTransport`  
  
  
### setJsonFactory(JsonFactory jsonFactory) (deprecated)
    
    
    public abstract void setJsonFactory(JsonFactory jsonFactory)

Set JsonFactory instance for this three legged flow.

**Parameter**  
---  
**Name** | **Description**  
`jsonFactory` | `com.google.api.client.json.JsonFactory`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
