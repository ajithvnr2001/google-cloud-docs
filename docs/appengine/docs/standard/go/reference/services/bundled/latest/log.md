---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/log/
title: Package google.golang.org/appengine/v2/log (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:49.644140+00:00
---

# Package google.golang.org/appengine/v2/log (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/log/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/log (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/log). 

## Functions 

### func Criticalf 
    
    
    func Criticalf(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), format [string](https://pkg.go.dev/builtin#string), args ...interface{})

Criticalf is like Debugf, but at Critical level.

### func Debugf 
    
    
    func Debugf(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), format [string](https://pkg.go.dev/builtin#string), args ...interface{})

Debugf formats its arguments according to the format, analogous to fmt.Printf, and records the text as a log message at Debug level. The message will be associated with the request linked with the provided context.

### func Errorf 
    
    
    func Errorf(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), format [string](https://pkg.go.dev/builtin#string), args ...interface{})

Errorf is like Debugf, but at Error level.

### func Infof 
    
    
    func Infof(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), format [string](https://pkg.go.dev/builtin#string), args ...interface{})

Infof is like Debugf, but at Info level.

### func Warningf 
    
    
    func Warningf(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), format [string](https://pkg.go.dev/builtin#string), args ...interface{})

Warningf is like Debugf, but at Warning level.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
