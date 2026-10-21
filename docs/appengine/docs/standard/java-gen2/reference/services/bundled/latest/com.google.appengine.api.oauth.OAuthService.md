---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthService
title: Interface OAuthService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:12:12.385445+00:00
---

# Interface OAuthService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface OAuthService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface OAuthService

The OAuthService provides methods useful for validating OAuth requests. See Also: [RFC 5849](http://tools.ietf.org/html/rfc5849) for the OAuth specification.

## Methods 

### getAuthorizedScopes(String[] scopes)
    
    
    public abstract String[] getAuthorizedScopes(String[] scopes)

Return authorized scopes from input scopes.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The custom OAuth scopes at least one of which is accepted.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth2 request.  
  
### getClientId(String scope)
    
    
    public abstract String getClientId(String scope)

Returns the client_id from oauth2 request.

**Parameter**  
---  
**Name** | **Description**  
`scope` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth2 request.  
  
### getClientId(String[] scopes)
    
    
    public abstract String getClientId(String[] scopes)

Returns the client_id from oauth2 request.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The custom OAuth scopes at least one of which is accepted.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth2 request.  
  
### getCurrentUser()
    
    
    public abstract User getCurrentUser()

Returns the [User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User) on whose behalf the request was made.

**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth request.  
  
### getCurrentUser(String scope)
    
    
    public abstract User getCurrentUser(String scope)

Returns the [User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User) on whose behalf the request was made.

**Parameter**  
---  
**Name** | **Description**  
`scope` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The custom OAuth scope that is accepted.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth request.  
  
### getCurrentUser(String[] scopes)
    
    
    public abstract User getCurrentUser(String[] scopes)

Returns the [User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User) on whose behalf the request was made.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The custom OAuth scopes at least one of which is accepted.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth request.  
  
### getOAuthConsumerKey() (deprecated)
    
    
    public abstract String getOAuthConsumerKey()

**Deprecated.** _OAuth1 is no longer supported_

Throws OAuthRequestException

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` |   
  
### isUserAdmin()
    
    
    public abstract boolean isUserAdmin()

Returns true if the user on whose behalf the request was made is an admin for this application, false otherwise.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth request.  
  
### isUserAdmin(String scope)
    
    
    public abstract boolean isUserAdmin(String scope)

Returns true if the user on whose behalf the request was made is an admin for this application, false otherwise.

**Parameter**  
---  
**Name** | **Description**  
`scope` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The custom OAuth scope that is accepted.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth request.  
  
### isUserAdmin(String[] scopes)
    
    
    public abstract boolean isUserAdmin(String[] scopes)

Returns true if the user on whose behalf the request was made is an admin for this application, false otherwise.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
The custom OAuth scopes at least one of which is accepted.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)` | If the request was not a valid OAuth request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
