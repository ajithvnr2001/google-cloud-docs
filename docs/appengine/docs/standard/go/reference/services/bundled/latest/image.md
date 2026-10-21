---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/image/
title: Package google.golang.org/appengine/v2/image (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:49.324967+00:00
---

# Package google.golang.org/appengine/v2/image (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/image (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/image). 

Package image provides image services.

## Functions 

### func DeleteServingURL 
    
    
    func DeleteServingURL(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey)) [error](https://pkg.go.dev/builtin#error)

DeleteServingURL deletes the serving URL for an image.

### func ServingURL 
    
    
    func ServingURL(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), key [appengine](https://pkg.go.dev/google.golang.org/appengine/v2).[BlobKey](https://pkg.go.dev/google.golang.org/appengine/v2#BlobKey), opts *ServingURLOptions) (*[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL), [error](https://pkg.go.dev/builtin#error))

ServingURL returns a URL that will serve an image from Blobstore.

## ServingURLOptions
    
    
    type ServingURLOptions struct {
    	Secure [bool](https://pkg.go.dev/builtin#bool) // whether the URL should use HTTPS
    
    	// Size must be between zero and 1600.
    	// If Size is non-zero, a resized version of the image is served,
    	// and Size is the served image's longest dimension. The aspect ratio is preserved.
    	// If Crop is true the image is cropped from the center instead of being resized.
    	Size [int](https://pkg.go.dev/builtin#int)
    	Crop [bool](https://pkg.go.dev/builtin#bool)
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
