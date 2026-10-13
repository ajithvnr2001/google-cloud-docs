---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/runtime/
title: Package google.golang.org/appengine/v2/runtime (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:50.906030+00:00
---

# Package google.golang.org/appengine/v2/runtime (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/runtime (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/runtime). 

Package runtime exposes information about the resource usage of the application. It also provides a way to run code in a new background context of a module. 

This package does not work on App Engine "flexible environment".

## Functions 

### func RunInBackground 
    
    
    func RunInBackground(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), f func(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context))) [error](https://pkg.go.dev/builtin#error)

RunInBackground runs f in a background goroutine in this process. f is provided a context that may outlast the context provided to RunInBackground. This is only valid to invoke from a service set to basic or manual scaling.

## Statistics
    
    
    type Statistics struct {
    	// CPU records the CPU consumed by this instance, in megacycles.
    	CPU struct {
    		Total   [float64](https://pkg.go.dev/builtin#float64)
    		Rate1M  [float64](https://pkg.go.dev/builtin#float64) // consumption rate over one minute
    		Rate10M [float64](https://pkg.go.dev/builtin#float64) // consumption rate over ten minutes
    	}
    	// RAM records the memory used by the instance, in megabytes.
    	RAM struct {
    		Current    [float64](https://pkg.go.dev/builtin#float64)
    		Average1M  [float64](https://pkg.go.dev/builtin#float64) // average usage over one minute
    		Average10M [float64](https://pkg.go.dev/builtin#float64) // average usage over ten minutes
    	}
    }

Statistics represents the system's statistics.

### func Stats 
    
    
    func Stats(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context)) (*Statistics, [error](https://pkg.go.dev/builtin#error))

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
