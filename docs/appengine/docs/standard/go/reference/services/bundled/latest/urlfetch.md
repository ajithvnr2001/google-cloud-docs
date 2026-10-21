---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/urlfetch/
title: Package google.golang.org/appengine/v2/urlfetch (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:51.831965+00:00
---

# Package google.golang.org/appengine/v2/urlfetch (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/urlfetch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/urlfetch (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/urlfetch). 

Package urlfetch provides an http.RoundTripper implementation for fetching URLs via App Engine's urlfetch service.

## Variables 

### ErrTruncatedBody
    
    
    var ErrTruncatedBody = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("urlfetch: truncated body")

ErrTruncatedBody is the error returned after the final Read() from a response's Body if the body has been truncated by App Engine's proxy.

## Functions 

### func Client 
    
    
    func Client(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) *[http](https://pkg.go.dev/net/http).[Client](https://pkg.go.dev/net/http#Client)

Client returns an *http.Client using a default urlfetch Transport. This client will have the default deadline of 5 seconds, and will check the validity of SSL certificates.

Any deadline of the provided context will be used for requests through this client; if the client does not have a deadline then a 5 second default is used.

## Transport
    
    
    type Transport struct {
    	Context [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)
    
    	// Controls whether the application checks the validity of SSL certificates
    	// over HTTPS connections. A value of false (the default) instructs the
    	// application to send a request to the server only if the certificate is
    	// valid and signed by a trusted certificate authority (CA), and also
    	// includes a hostname that matches the certificate. A value of true
    	// instructs the application to perform no certificate validation.
    	AllowInvalidServerCertificate [bool](https://pkg.go.dev/builtin#bool)
    }

Transport is an implementation of http.RoundTripper for App Engine. Users should generally create an http.Client using this transport and use the Client rather than using this transport directly.

### func (*Transport) RoundTrip 
    
    
    func (t *Transport) RoundTrip(req *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request)) (res *[http](https://pkg.go.dev/net/http).[Response](https://pkg.go.dev/net/http#Response), err [error](https://pkg.go.dev/builtin#error))

RoundTrip issues a single HTTP request and returns its response. Per the http.RoundTripper interface, RoundTrip only returns an error if there was an unsupported request or the URL Fetch proxy fails. Note that HTTP response codes such as 5xx, 403, 404, etc are not errors as far as the transport is concerned and will be returned with err set to nil.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
