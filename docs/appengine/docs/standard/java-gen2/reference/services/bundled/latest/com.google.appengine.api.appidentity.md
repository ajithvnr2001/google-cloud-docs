---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity
title: Package com.google.appengine.api.appidentity (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:56.585705+00:00
---

# Package com.google.appengine.api.appidentity (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.appidentity (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a service to sign arbitrary byte arrays using an internally-generated, rotated private key. See Also: [com.google.appengine.api.appidentity.AppIdentityService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService), [The App Identity Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/appidentity/).

## Classes 

### [AppIdentityService.GetAccessTokenResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.GetAccessTokenResult)

`GetAccessTokenResult` is returned by getAccessToken. It contains the access token and the expiration time for the token.

### [AppIdentityService.ParsedAppId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.ParsedAppId)

Class holding the results of parsing a full application id into its constituent parts. See Also: #parseFullAppId

### [AppIdentityService.SigningResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService.SigningResult)

`SigningResult` is returned by signForApp, which contains signing key name and signature.

### [AppIdentityServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServiceFactory)

Creates new instances of the App Identity service.

### [AppIdentityServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb)

### [AppIdentityServicePb.AppIdentityServiceError](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.AppIdentityServiceError)

### [AppIdentityServicePb.AppIdentityServiceError.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.AppIdentityServiceError.Builder)

### [AppIdentityServicePb.GetAccessTokenRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetAccessTokenRequest)

### [AppIdentityServicePb.GetAccessTokenRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetAccessTokenRequest.Builder)

### [AppIdentityServicePb.GetAccessTokenResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetAccessTokenResponse)

### [AppIdentityServicePb.GetAccessTokenResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetAccessTokenResponse.Builder)

### [AppIdentityServicePb.GetDefaultGcsBucketNameRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetDefaultGcsBucketNameRequest)

### [AppIdentityServicePb.GetDefaultGcsBucketNameRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetDefaultGcsBucketNameRequest.Builder)

### [AppIdentityServicePb.GetDefaultGcsBucketNameResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetDefaultGcsBucketNameResponse)

### [AppIdentityServicePb.GetDefaultGcsBucketNameResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetDefaultGcsBucketNameResponse.Builder)

### [AppIdentityServicePb.GetPublicCertificateForAppRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetPublicCertificateForAppRequest)

### [AppIdentityServicePb.GetPublicCertificateForAppRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetPublicCertificateForAppRequest.Builder)

### [AppIdentityServicePb.GetPublicCertificateForAppResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetPublicCertificateForAppResponse)

### [AppIdentityServicePb.GetPublicCertificateForAppResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetPublicCertificateForAppResponse.Builder)

### [AppIdentityServicePb.GetServiceAccountNameRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetServiceAccountNameRequest)

### [AppIdentityServicePb.GetServiceAccountNameRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetServiceAccountNameRequest.Builder)

### [AppIdentityServicePb.GetServiceAccountNameResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetServiceAccountNameResponse)

### [AppIdentityServicePb.GetServiceAccountNameResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetServiceAccountNameResponse.Builder)

### [AppIdentityServicePb.PublicCertificate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.PublicCertificate)

### [AppIdentityServicePb.PublicCertificate.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.PublicCertificate.Builder)

### [AppIdentityServicePb.SignForAppRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.SignForAppRequest)

### [AppIdentityServicePb.SignForAppRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.SignForAppRequest.Builder)

### [AppIdentityServicePb.SignForAppResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.SignForAppResponse)

### [AppIdentityServicePb.SignForAppResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.SignForAppResponse.Builder)

### [IAppIdentityServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.IAppIdentityServiceFactoryProvider)

Factory provider for [IAppIdentityServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.IAppIdentityServiceFactory).

**Note:** This class is not intended for end users.

### [PublicCertificate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.PublicCertificate)

`PublicCertificate` contains an x509 public certificate in PEM format and a string which is used to identify this certificate. See Also: [RFC 5280](http://tools.ietf.org/html/rfc5280) for the specification of x509 certificates.

## Interfaces 

### [AppIdentityService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService)

The `AppIdentityService` allows you to sign an arbitrary byte array using a per app private key maintained by App Engine, and to retrieve a list of public certificates which can be used to verify the signature.

App Engine is responsible for maintaining the per application private key. App Engine will rotate private keys periodically. App Engine never gives these private keys to the outside.

Since private keys are rotated periodically, [#getPublicCertificatesForApp](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityService#com_google_appengine_api_appidentity_AppIdentityService_getPublicCertificatesForApp_) could return a list of public certificates. It is the caller's responsibility to try these certificates one by one when doing signature verification.

### [AppIdentityServicePb.AppIdentityServiceErrorOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.AppIdentityServiceErrorOrBuilder)

### [AppIdentityServicePb.GetAccessTokenRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetAccessTokenRequestOrBuilder)

### [AppIdentityServicePb.GetAccessTokenResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetAccessTokenResponseOrBuilder)

### [AppIdentityServicePb.GetDefaultGcsBucketNameRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetDefaultGcsBucketNameRequestOrBuilder)

### [AppIdentityServicePb.GetDefaultGcsBucketNameResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetDefaultGcsBucketNameResponseOrBuilder)

### [AppIdentityServicePb.GetPublicCertificateForAppRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetPublicCertificateForAppRequestOrBuilder)

### [AppIdentityServicePb.GetPublicCertificateForAppResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetPublicCertificateForAppResponseOrBuilder)

### [AppIdentityServicePb.GetServiceAccountNameRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetServiceAccountNameRequestOrBuilder)

### [AppIdentityServicePb.GetServiceAccountNameResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.GetServiceAccountNameResponseOrBuilder)

### [AppIdentityServicePb.PublicCertificateOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.PublicCertificateOrBuilder)

### [AppIdentityServicePb.SignForAppRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.SignForAppRequestOrBuilder)

### [AppIdentityServicePb.SignForAppResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.SignForAppResponseOrBuilder)

### [IAppIdentityServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.IAppIdentityServiceFactory)

Creates new instances of the App Identity service.

## Enums 

### [AppIdentityServicePb.AppIdentityServiceError.ErrorCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServicePb.AppIdentityServiceError.ErrorCode)

## Exceptions 

### [AppIdentityServiceFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServiceFailureException)

[AppIdentityServiceFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.appidentity.AppIdentityServiceFailureException) is thrown when any unknown error occurs while communicating with the App Identity service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
