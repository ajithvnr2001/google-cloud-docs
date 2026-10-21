---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService
title: Interface AppIdentityService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:55.145222+00:00
---

# Interface AppIdentityService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface AppIdentityService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface AppIdentityService

The `AppIdentityService` allows you to sign an arbitrary byte array using a per app private key maintained by App Engine, and to retrieve a list of public certificates which can be used to verify the signature.

App Engine is responsible for maintaining the per application private key. App Engine will rotate private keys periodically. App Engine never gives these private keys to the outside.

Since private keys are rotated periodically, [#getPublicCertificatesForApp](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService#com_google_appengine_api_appidentity_AppIdentityService_getPublicCertificatesForApp_) could return a list of public certificates. It is the caller's responsibility to try these certificates one by one when doing signature verification.

## Methods 

### getAccessToken(Iterable<String> scopes)
    
    
    public abstract AppIdentityService.GetAccessTokenResult getAccessToken(Iterable<String> scopes)

OAuth2 access token to act on behalf of the application.

Generates and caches an OAuth2 access token for the service account for the appengine application.

Each application has an associated Google account. This function returns OAuth2 access token corresponding to the running app. Access tokens are safe to cache and reuse until their expiry time as returned. This method will do that using memcache.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
iterable of scopes to request.  
**Returns**  
---  
**Type** | **Description**  
`[AppIdentityService.GetAccessTokenResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.GetAccessTokenResult)` | a GetAccessTokenResult object with the access token and expiration time.  
  
### getAccessTokenUncached(Iterable<String> scopes)
    
    
    public abstract AppIdentityService.GetAccessTokenResult getAccessTokenUncached(Iterable<String> scopes)

OAuth2 access token to act on behalf of the application, uncached.

Most developers should use getAccessToken instead.

**Parameter**  
---  
**Name** | **Description**  
`scopes` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
iterable of scopes to request.  
**Returns**  
---  
**Type** | **Description**  
`[AppIdentityService.GetAccessTokenResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.GetAccessTokenResult)` | a GetAccessTokenResult object with the access token and expiration time.  
  
### getDefaultGcsBucketName()
    
    
    public abstract String getDefaultGcsBucketName()

Gets the default GS bucket name for the app.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | default GS bucket name for the app.  
  
### getPublicCertificatesForApp()
    
    
    public abstract Collection<PublicCertificate> getPublicCertificatesForApp()

Retrieves a list of public certificates.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[PublicCertificate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.PublicCertificate)>` | a list of public certificates.  
  
### getServiceAccountName()
    
    
    public abstract String getServiceAccountName()

Gets service account name of the app.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | service account name of the app.  
  
### parseFullAppId(String fullAppId)
    
    
    public abstract AppIdentityService.ParsedAppId parseFullAppId(String fullAppId)

Parse a full app id into partition, domain name and display app_id.

**Parameter**  
---  
**Name** | **Description**  
`fullAppId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The full partitioned app id.  
**Returns**  
---  
**Type** | **Description**  
`[AppIdentityService.ParsedAppId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.ParsedAppId)` | An ParsedAppId instance with the parsing results.  
  
### signForApp(byte[] signBlob)
    
    
    public abstract AppIdentityService.SigningResult signForApp(byte[] signBlob)

Requests to sign arbitrary byte array using per app private key.

**Parameter**  
---  
**Name** | **Description**  
`signBlob` | `byte[]`  
string blob.  
**Returns**  
---  
**Type** | **Description**  
`[AppIdentityService.SigningResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.SigningResult)` | a SigningResult object which contains signing key name and signature.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
