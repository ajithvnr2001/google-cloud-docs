---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/module/
title: Package google.golang.org/appengine/v2/module (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:50.657300+00:00
---

# Package google.golang.org/appengine/v2/module (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/module (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/module). 

Package module provides functions for interacting with modules. 

The appengine package contains functions that report the identity of the app, including the module name.

## Functions 

### func DefaultVersion 
    
    
    func DefaultVersion(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module [string](https://pkg.go.dev/builtin#string)) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

DefaultVersion returns the default version of the specified module. If module is the empty string, it means the default module.

### func List 
    
    
    func List(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) ([][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

List returns the names of modules belonging to this application.

### func NumInstances 
    
    
    func NumInstances(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module, version [string](https://pkg.go.dev/builtin#string)) ([int](https://pkg.go.dev/builtin#int), [error](https://pkg.go.dev/builtin#error))

NumInstances returns the number of instances of the given module/version. If either argument is the empty string it means the default. This only works if you are using manual_scaling in your app's config file.

### func SetNumInstances 
    
    
    func SetNumInstances(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module, version [string](https://pkg.go.dev/builtin#string), instances [int](https://pkg.go.dev/builtin#int)) [error](https://pkg.go.dev/builtin#error)

SetNumInstances sets the number of instances of the given module.version to the specified value. If either module or version are the empty string it means the default.

### func Start 
    
    
    func Start(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module, version [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

Start starts the specified version of the specified module. If either module or version are the empty string, it means the default.

### func Stop 
    
    
    func Stop(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module, version [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

Stop stops the specified version of the specified module. If either module or version are the empty string, it means the default.

### func Versions 
    
    
    func Versions(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), module [string](https://pkg.go.dev/builtin#string)) ([][string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Versions returns the names of the versions that belong to the specified module. If module is the empty string, it means the default module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
