---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/aetest/
title: Package google.golang.org/appengine/v2/aetest (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:47.454651+00:00
---

# Package google.golang.org/appengine/v2/aetest (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/aetest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/aetest (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/aetest). 

Package aetest provides an API for running dev_appserver for use in tests. 

An example test file:
    
    
    package foo_test
    
    import (
        "testing"
    
        "google.golang.org/appengine/v2/memcache"
        "google.golang.org/appengine/v2/aetest"
    )
    
    func TestFoo(t *testing.T) {
        ctx, done, err := aetest.[NewContext](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/aetest.html#google_golang_org_appengine_v2_aetest_NewContext)()
        if err != nil {
            t.Fatal(err)
        }
        defer done()
    
        it := &memcache.[Item](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/memcache.html#google_golang_org_appengine_v2_memcache_Item){
            Key:   "some-key",
            Value: []byte("some-value"),
        }
        err = memcache.[Set](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/memcache.html#google_golang_org_appengine_v2_memcache_Set)(ctx, it)
        if err != nil {
            t.Fatalf("Set err: %v", err)
        }
        it, err = memcache.Get(ctx, "some-key")
        if err != nil {
            t.Fatalf("Get err: %v; want no error", err)
        }
        if g, w := string(it.Value), "some-value" ; g != w {
            t.Errorf("retrieved Item.Value = %q, want %q", g, w)
        }
    }

The environment variable APPENGINE_DEV_APPSERVER specifies the location of the dev_appserver.py executable to use. If unset, the system PATH is consulted.

## Variables 

### PrepareDevAppserver
    
    
    var PrepareDevAppserver func() [error](https://pkg.go.dev/builtin#error)

PrepareDevAppserver is a hook which, if set, will be called before the dev_appserver.py is started, each time it is started. If aetest.NewContext is invoked from the goapp test tool, this hook is unnecessary.

## Functions 

### func Login 
    
    
    func Login(u *[user](https://pkg.go.dev/google.golang.org/appengine/v2/user).[User](https://pkg.go.dev/google.golang.org/appengine/v2/user#User), req *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request))

Login causes the provided Request to act as though issued by the given user.

### func Logout 
    
    
    func Logout(req *[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request))

Logout causes the provided Request to act as though issued by a logged-out user.

### func NewContext 
    
    
    func NewContext() ([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), func(), [error](https://pkg.go.dev/builtin#error))

NewContext starts an instance of the development API server, and returns a context that will route all API calls to that server, as well as a closure that must be called when the Context is no longer required.

## Instance
    
    
    type Instance interface {
    	// Close kills the child api_server.py process, releasing its resources.
    	[io](https://pkg.go.dev/io).[Closer](https://pkg.go.dev/io#Closer)
    	// NewRequest returns an *http.Request associated with this instance.
    	NewRequest(method, urlStr [string](https://pkg.go.dev/builtin#string), body [io](https://pkg.go.dev/io).[Reader](https://pkg.go.dev/io#Reader)) (*[http](https://pkg.go.dev/net/http).[Request](https://pkg.go.dev/net/http#Request), [error](https://pkg.go.dev/builtin#error))
    }

Instance represents a running instance of the development API Server.

### func NewInstance 
    
    
    func NewInstance(opts *Options) (Instance, [error](https://pkg.go.dev/builtin#error))

NewInstance launches a running instance of api_server.py which can be used for multiple test Contexts that delegate all App Engine API calls to that instance. If opts is nil the default values are used.

## Options
    
    
    type Options struct {
    	// AppID specifies the App ID to use during tests.
    	// By default, "testapp".
    	AppID [string](https://pkg.go.dev/builtin#string)
    	// StronglyConsistentDatastore is whether the local datastore should be
    	// strongly consistent. This will diverge from production behaviour.
    	StronglyConsistentDatastore [bool](https://pkg.go.dev/builtin#bool)
    	// SupportDatastoreEmulator is whether use Cloud Datastore Emulator or
    	// use old SQLite based Datastore backend or use default settings.
    	SupportDatastoreEmulator *[bool](https://pkg.go.dev/builtin#bool)
    	// SuppressDevAppServerLog is whether the dev_appserver running in tests
    	// should output logs.
    	SuppressDevAppServerLog [bool](https://pkg.go.dev/builtin#bool)
    	// StartupTimeout is a duration to wait for instance startup.
    	// By default, 15 seconds.
    	StartupTimeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
    }

Options is used to specify options when creating an Instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
