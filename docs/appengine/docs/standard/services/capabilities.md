---
url: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/
title: Capabilities API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:06.529300+00:00
---

# Capabilities API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/capabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Capabilities API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

With the Capabilities API, your application can detect outages and scheduled downtime for specific API capabilities. You can use this API to reduce downtime in your application by detecting when a capability is unavailable and then bypassing it. 

Every `is_enabled` request to this API always returns `true` except for the "Datastore writes" capability, which returns `false` if Datastore is in read-only mode for your app.

For example, if you use the Images API to resize images, you can use the Capabilities API to detect when the Images API is unavailable and skip the resize:
    
    
    from google.appengine.api import capabilities
    
    def StoreUploadedProfileImage(self):
        uploaded_image = self.request.get('img')
        # If the images API is unavailable, we'll just skip the resize.
        if capabilities.CapabilitySet('images').is_enabled():
            uploaded_image = images.resize(uploaded_image, 64, 64)
        store(uploaded_image)
    

## Using the Capabilities API

The [`CapabilitySet`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/capabilities/CapabilitySet) class defines all of the available methods for this API. You can either name capabilities explicitly or infer them from the methods provided by this class. See the next section for a list of services currently enabled in this API.

## Supported capabilities

The API currently supports the following capabilities:

Capability | Arguments to `CapabilitySet`  
---|---  
Availability of the blobstore | `"blobstore"`  
Datastore reads | `"datastore_v3"`  
Datastore writes | `"datastore_v3", ["write"]`  
Availability of the Images service | `"images"`  
Availability of the Mail service | `"mail"`  
Availability of the Memcache service | `"memcache"`  
Availability of the Task Queue service | `"taskqueue"`  
Availability of the URL Fetch service | `"urlfetch"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
