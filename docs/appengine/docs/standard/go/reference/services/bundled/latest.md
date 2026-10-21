---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/
title: Package google.golang.org/appengine/v2 (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:47.009272+00:00
---

# Package google.golang.org/appengine/v2 (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2 (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2). 

Package appengine provides basic functionality for Google App Engine. 

For more information on how to write Go apps for Google App Engine, see: <https://cloud.google.com/appengine/docs/go/>

## Variables 

### Middleware
    
    
    var Middleware func([http](https://pkg.go.dev/net/http).[Handler](https://pkg.go.dev/net/http#Handler)) [http](https://pkg.go.dev/net/http).[Handler](https://pkg.go.dev/net/http#Handler) = [internal](https://pkg.go.dev/google.golang.org/appengine/v2/internal).[Middleware](https://pkg.go.dev/google.golang.org/appengine/v2/internal#Middleware)

Middleware wraps an http handler so that it can make GAE API calls

## Functions 

### func APICall 
    
    
    func APICall(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), service, method [string](https://pkg.go.dev/builtin#string), in, out [proto](https://pkg.go.dev/github.com/golang/protobuf/proto).[Message](https://pkg.go.dev/github.com/golang/protobuf/proto#Message)) [error](https://pkg.go.dev/builtin#error)

APICall performs an API call.

This is not intended for general use; it is exported for use in conjunction with WithAPICallFunc.

### func AccessToken 
    
    
    func AccessToken(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), scopes [string](https://pkg.go.dev/builtin#string)) (token [string](https://pkg.go.dev/builtin#string), expiry [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time), err [error](https://pkg.go.dev/builtin#error))

AccessToken generates an OAuth2 access token for the specified scopes on behalf of service account of this application. This token will expire after the returned time.

### func AppID 
    
    
    func AppID(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [string](https://pkg.go.dev/builtin#string)

AppID returns the application ID for the current application. The string will be a plain application ID (e.g. "appid"), with a domain prefix for custom domain deployments (e.g. "example.com:appid").

### func BackgroundContext (deprecated)
    
    
    func BackgroundContext() [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)

BackgroundContext returns a context not associated with a request.

Deprecated: App Engine no longer has a special background context. Just use context.Background().

### func Datacenter 
    
    
    func Datacenter(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [string](https://pkg.go.dev/builtin#string)

Datacenter returns an identifier for the datacenter that the instance is running in.

### func DefaultVersionHostname 
    
    
    func DefaultVersionHostname(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [string](https://pkg.go.dev/builtin#string)

DefaultVersionHostname returns the standard hostname of the default version of the current application (e.g. "my-app.appspot.com"). This is suitable for use in constructing URLs.

### func InstanceID 
    
    
    func InstanceID() [string](https://pkg.go.dev/builtin#string)

InstanceID returns a mostly-unique identifier for this instance.

### func IsAppEngine 
    
    
    func IsAppEngine() [bool](https://pkg.go.dev/builtin#bool)

IsAppEngine reports whether the App Engine app is running on App Engine, in either the standard or flexible environment.

### func IsDevAppServer 
    
    
    func IsDevAppServer() [bool](https://pkg.go.dev/builtin#bool)

IsDevAppServer reports whether the App Engine app is running in the development App Server.

### func IsFlex 
    
    
    func IsFlex() [bool](https://pkg.go.dev/builtin#bool)

IsFlex reports whether the App Engine app is running in the flexible environment.

### func IsOverQuota 
    
    
    func IsOverQuota(err [error](https://pkg.go.dev/builtin#error)) [bool](https://pkg.go.dev/builtin#bool)

IsOverQuota reports whether err represents an API call failure due to insufficient available quota.

### func IsSecondGen 
    
    
    func IsSecondGen() [bool](https://pkg.go.dev/builtin#bool)

IsSecondGen reports whether the App Engine app is running on the second generation runtimes (>= Go 1.11).

### func IsStandard 
    
    
    func IsStandard() [bool](https://pkg.go.dev/builtin#bool)

IsStandard reports whether the App Engine app is running in the standard environment. This includes both the first generation runtimes (<= Go 1.9) and the second generation runtimes (>= Go 1.11).

### func IsTimeoutError 
    
    
    func IsTimeoutError(err [error](https://pkg.go.dev/builtin#error)) [bool](https://pkg.go.dev/builtin#bool)

IsTimeoutError reports whether err is a timeout error.

### func Main 
    
    
    func Main()

Main is the principal entry point for an app running in App Engine.

On App Engine Flexible it installs a trivial health checker if one isn't already registered, and starts listening on port 8080 (overridden by the $PORT environment variable).

See <https://cloud.google.com/appengine/docs/flexible/custom-runtimes#health_check_requests> for details on how to do your own health checking.

On App Engine Standard it ensures the server has started and is prepared to receive requests.

Main never returns.

Main is designed so that the app's main package looks like this:
    
    
    package main
    
    import (
            "google.golang.org/appengine/v2"
    
            _ "myapp/package0"
            _ "myapp/package1"
    )
    
    func main() {
            appengine.[Main](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/index.html#google_golang_org_appengine_v2_Main)()
    }
    

The "myapp/packageX" packages are expected to register HTTP handlers in their init functions.

### func ModuleHostname 
    
    
    func ModuleHostname(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module, version, instance [string](https://pkg.go.dev/builtin#string)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

ModuleHostname returns a hostname of a module instance. If module is the empty string, it refers to the module of the current instance. If version is empty, it refers to the version of the current instance if valid, or the default version of the module of the current instance. If instance is empty, ModuleHostname returns the load-balancing hostname.

### func ModuleName 
    
    
    func ModuleName(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [string](https://pkg.go.dev/builtin#string)

ModuleName returns the module name of the current instance.

### func Namespace 
    
    
    func Namespace(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), namespace [string](https://pkg.go.dev/builtin#string)) ([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), [error](https://pkg.go.dev/builtin#error))

Namespace returns a replacement context that operates within the given namespace.

### func NewContext 
    
    
    func NewContext(req *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request)) [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)

NewContext returns a context for an in-flight HTTP request. This function is cheap.

### func RequestID 
    
    
    func RequestID(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [string](https://pkg.go.dev/builtin#string)

RequestID returns a string that uniquely identifies the request.

### func ServerSoftware 
    
    
    func ServerSoftware() [string](https://pkg.go.dev/builtin#string)

ServerSoftware returns the App Engine release version. In production, it looks like "Google App Engine/X.Y.Z". In the development appserver, it looks like "Development/X.Y".

### func ServiceAccount 
    
    
    func ServiceAccount(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

ServiceAccount returns a string representing the service account name, in the form of an email address (typically app_id@appspot.gserviceaccount.com).

### func SignBytes 
    
    
    func SignBytes(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), bytes [][byte](https://pkg.go.dev/builtin#byte)) (keyName [string](https://pkg.go.dev/builtin#string), signature [][byte](https://pkg.go.dev/builtin#byte), err [error](https://pkg.go.dev/builtin#error))

SignBytes signs bytes using a private key unique to your application.

### func VersionID 
    
    
    func VersionID(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) [string](https://pkg.go.dev/builtin#string)

VersionID returns the version ID for the current application. It will be of the form "X.Y", where X is specified in app.yaml, and Y is a number generated when each version of the app is uploaded. It does not include a module name.

### func WithAPICallFunc 
    
    
    func WithAPICallFunc(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), f APICallFunc) [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)

WithAPICallFunc returns a copy of the parent context that will cause API calls to invoke f instead of their normal operation.

This is intended for advanced users only.

### func WithContext 
    
    
    func WithContext(parent [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request)) [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)

WithContext returns a copy of the parent context and associates it with an in-flight HTTP request. This function is cheap.

## APICallFunc
    
    
    type APICallFunc func(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), service, method [string](https://pkg.go.dev/builtin#string), in, out [proto](https://pkg.go.dev/github.com/golang/protobuf/proto).[Message](https://pkg.go.dev/github.com/golang/protobuf/proto#Message)) [error](https://pkg.go.dev/builtin#error)

APICallFunc defines a function type for handling an API call. See WithCallOverride.

## BlobKey
    
    
    type BlobKey [string](https://pkg.go.dev/builtin#string)

BlobKey is a key for a blobstore blob.

Conceptually, this type belongs in the blobstore package, but it lives in the appengine package to avoid a circular dependency: blobstore depends on datastore, and datastore needs to refer to the BlobKey type.

## Certificate
    
    
    type Certificate struct {
    	KeyName [string](https://pkg.go.dev/builtin#string)
    	Data    [][byte](https://pkg.go.dev/builtin#byte) // PEM-encoded X.509 certificate
    }

Certificate represents a public certificate for the app.

### func PublicCertificates 
    
    
    func PublicCertificates(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([]Certificate, [error](https://pkg.go.dev/builtin#error))

PublicCertificates retrieves the public certificates for the app. They can be used to verify a signature returned by SignBytes.

## GeoPoint
    
    
    type GeoPoint struct {
    	Lat, Lng [float64](https://pkg.go.dev/builtin#float64)
    }

GeoPoint represents a location as latitude/longitude in degrees.

### func (GeoPoint) Valid 
    
    
    func (g GeoPoint) Valid() [bool](https://pkg.go.dev/builtin#bool)

Valid returns whether a GeoPoint is within [-90, 90] latitude and [-180, 180] longitude.

## MultiError
    
    
    type MultiError [][error](https://pkg.go.dev/builtin#error)

MultiError is returned by batch operations when there are errors with particular elements. Errors will be in a one-to-one correspondence with the input elements; successful elements will have a nil entry.

### func (MultiError) Error 
    
    
    func (m MultiError) Error() [string](https://pkg.go.dev/builtin#string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
