---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch
title: Package com.google.appengine.api.urlfetch (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:12:38.123469+00:00
---

# Package com.google.appengine.api.urlfetch (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.urlfetch (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a service to make HTTP/S requests of other servers on the internet. The java.net.URLConnection class can also be used to do this, and in App Engine is implemented by using URL Fetch. Chunked and hanging requests, however, are not supported.

As is typical for App Engine services, the URLFetchServiceFactory returns a URLFetchService, which is used to actually make requests of the service. See Also: [The URL Fetch Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/urlfetch/)., [com.google.appengine.api.urlfetch.URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService)

## Classes 

### [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions)

Allows users to customize the behavior of [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operations. 

If [#allowTruncate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_allowTruncate__) is called, [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) will truncate large responses and return them without error. 

If [#disallowTruncate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_disallowTruncate_) is called, [ResponseTooLargeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.ResponseTooLargeException) will be thrown if the response is too large. 

If [#followRedirects()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_followRedirects__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation will follow redirects. 

If [#doNotFollowRedirects()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_doNotFollowRedirects__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation will not follow redirects. 

If [#validateCertificate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_validateCertificate__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation will, if using an HTTPS connection, instruct the application to send a request to the server only if the certificate is valid and signed by a trusted certificate authority (CA), and also includes a hostname that matches the certificate. If the certificate validation fails, a javax.net.ssl.SSLHandshakeException exception is thrown. HTTP connections are unaffected by this option. 

If [#doNotValidateCertificate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_doNotValidateCertificate__) is called the [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) will not validate the server's SSL certificate in any fashion. This is the default behavior. Note, however, that validation will be turned on by default in the near future. If you rely upon making requests to a site with an invalid or untrusted certificate, you should explicitly call [#doNotValidateCertificate()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions#com_google_appengine_api_urlfetch_FetchOptions_doNotValidateCertificate__) to avoid errors in future versions. 

Notes on usage:  
The recommended way to instantiate a `FetchOptions` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.urlfetch.FetchOptions.Builder.*;
    
     ...
     URL url = getURLToFetch();
     urlFetchService.fetch(new HTTPRequest(url, HTTPMethod.GET,
         allowTruncate()));
    
     urlFetchService.fetch(new HTTPRequest(url, HTTPMethod.GET,
         allowTruncate().doNotFollowRedirects()));
     

### [FetchOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions.Builder)

Contains static creation methods for [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions).

### [HTTPHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPHeader)

`HTTPHeader` can represent either an HTTP request header, or an HTTP response header.

### [HTTPRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPRequest)

`HTTPRequest` encapsulates a single HTTP request that is made via the `URLFetchService`.

### [HTTPResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPResponse)

`HTTPResponse` encapsulates the results of a ` HTTPRequest` made via the `URLFetchService`.

### [IURLFetchServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.IURLFetchServiceFactoryProvider)

Factory provider for [IURLFetchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.IURLFetchServiceFactory).

**Note:** This class is not intended for end users.

### [URLFetchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServiceFactory)

Factory for [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService)

### [URLFetchServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb)

### [URLFetchServicePb.URLFetchRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest)

### [URLFetchServicePb.URLFetchRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.Builder)

### [URLFetchServicePb.URLFetchRequest.Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.Header)

### [URLFetchServicePb.URLFetchRequest.Header.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.Header.Builder)

### [URLFetchServicePb.URLFetchResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse)

### [URLFetchServicePb.URLFetchResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.Builder)

### [URLFetchServicePb.URLFetchResponse.Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.Header)

### [URLFetchServicePb.URLFetchResponse.Header.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.Header.Builder)

### [URLFetchServicePb.URLFetchServiceError](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchServiceError)

### [URLFetchServicePb.URLFetchServiceError.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchServiceError.Builder)

## Interfaces 

### [IURLFetchServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.IURLFetchServiceFactory)

Factory for [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService)

### [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService)

The `URLFetchService` provides a way for user code to execute HTTP requests to external URLs.

Chunked and hanging requests are not supported, and all content will be returned in a single block.

### [URLFetchServicePb.URLFetchRequest.HeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.HeaderOrBuilder)

### [URLFetchServicePb.URLFetchRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequestOrBuilder)

### [URLFetchServicePb.URLFetchResponse.HeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponse.HeaderOrBuilder)

### [URLFetchServicePb.URLFetchResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchResponseOrBuilder)

### [URLFetchServicePb.URLFetchServiceErrorOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchServiceErrorOrBuilder)

## Enums 

### [HTTPMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.HTTPMethod)

`HTTPMethod` is an enumeration of HTTP methods that can be sent to a remote server via the `URLFetchService`.

### [URLFetchServicePb.URLFetchRequest.RequestMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchRequest.RequestMethod)

### [URLFetchServicePb.URLFetchServiceError.ErrorCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchServicePb.URLFetchServiceError.ErrorCode)

## Exceptions 

### [InternalTransientException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.InternalTransientException)

`InternalTransientException` is thrown when a temporary error occurs in retrieving the URL.

### [RequestPayloadTooLargeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.RequestPayloadTooLargeException)

`RequestPayloadTooLargeException` is thrown when the payload of a [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) request is too large.

This is a subclass of MalformedURLException for backwards compatibility as it is thrown in places where MalformedURLException was thrown previously.

### [ResponseTooLargeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.ResponseTooLargeException)

`ResponseTooLargeException` is thrown when the result of a [URLFetchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.URLFetchService) operation is too large.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
