---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserService
title: Interface UserService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:51.677198+00:00
---

# Interface UserService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.UserService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface UserService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface UserService

The UserService provides information useful for forcing a user to log in or out, and retrieving information about the user who is currently logged-in.

## Methods 

### createLoginURL(String destinationURL)
    
    
    public abstract String createLoginURL(String destinationURL)

Returns a URL that can be used to display a login page to the user.

**Parameter**  
---  
**Name** | **Description**  
`destinationURL` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
where the user will be redirected after they log in.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The URL that will present a login prompt.  
  
### createLoginURL(String destinationURL, @Nullable String authDomain)
    
    
    public abstract String createLoginURL(String destinationURL, @Nullable String authDomain)

Returns a URL that can be used to display a login page to the user.

**Parameters**  
---  
**Name** | **Description**  
`destinationURL` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
where the user will be redirected after they log in.  
`authDomain` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
not used.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The URL that will present a login prompt.  
  
### createLoginURL(String destinationURL, String authDomain, String federatedIdentity, Set<String> attributesRequest) (deprecated)
    
    
    public abstract String createLoginURL(String destinationURL, String authDomain, String federatedIdentity, Set<String> attributesRequest)

**Deprecated.** _Use of federatedIdentity is no longer supported. Please change calls to a method that does not take the parameter._

Returns a URL that can be used to redirect the user to a third party for federated login.

**Parameters**  
---  
**Name** | **Description**  
`destinationURL` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
where the user will be redirected after they log in.  
`authDomain` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
not used.  
`federatedIdentity` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Setting this parameter to a non-null value will throw an IllegalArgumentException. OpenID 2.0 support has been decommissioned. Please see <https://cloud.google.com/appengine/docs/deprecations/open_id> for details.  
`attributesRequest` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
not used.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The URL that will present a login prompt.  
  
### createLogoutURL(String destinationURL)
    
    
    public abstract String createLogoutURL(String destinationURL)

Returns a URL that can be used to log the current user out of this app.

**Parameter**  
---  
**Name** | **Description**  
`destinationURL` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
where the user will be redirected after they log out.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The URL that will log the user out.  
  
### createLogoutURL(String destinationURL, @Nullable String authDomain)
    
    
    public abstract String createLogoutURL(String destinationURL, @Nullable String authDomain)

Returns a URL that can be used to log the current user out of this app.

**Parameters**  
---  
**Name** | **Description**  
`destinationURL` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
where the user will be redirected after they log out.  
`authDomain` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
not used.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The URL that will log the user out.  
  
### getCurrentUser()
    
    
    public abstract @Nullable User getCurrentUser()

If the user is logged in, this method will return a `User` that contains information about them.

Note that repeated calls may not necessarily return the same `User` object.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.users.@org.jspecify.annotations.Nullable User` | User if the user is logged in, null otherwise.  
  
### isUserAdmin()
    
    
    public abstract boolean isUserAdmin()

Returns true if the user making this request is an admin for this application, false otherwise.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isUserLoggedIn()
    
    
    public abstract boolean isUserLoggedIn()

Returns true if there is a user logged in, false otherwise.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
