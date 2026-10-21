---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/capability/
title: Package google.golang.org/appengine/v2/capability (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:48.111219+00:00
---

# Package google.golang.org/appengine/v2/capability (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/capability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/capability (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/capability). 

Package capability exposes information about outages and scheduled downtime for specific API capabilities. 

This package does not work in App Engine "flexible environment". 

Example:
    
    
    if !capability.Enabled(c, "datastore_v3", "write") {
        // show user a different page
    }

## Functions 

### func Enabled 
    
    
    func Enabled(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), api, capability [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)

Enabled returns whether an API's capabilities are enabled. The wildcard "*" capability matches every capability of an API. If the underlying RPC fails (if the package is unknown, for example), false is returned and information is written to the application log.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
