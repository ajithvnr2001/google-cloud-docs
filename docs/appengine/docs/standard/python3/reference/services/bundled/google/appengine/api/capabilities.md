---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/capabilities/
title: Module: google.appengine.api.capabilities \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:23:25.232125+00:00
---

# Module: google.appengine.api.capabilities  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/capabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.capabilities Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/capabilities/__init__.py) Allows applications to identify API outages and scheduled downtime. Example:
    
    
        def StoreUploadedProfileImage(self):
          uploaded_image = self.request.get('img')
          # If the images API is unavailable, we'll just skip the resize.
          if CapabilitySet('images').is_enabled():
            uploaded_image = images.resize(uploaded_image, 64, 64)
          store(uploaded_image)
    
        def RenderHTMLForm(self):
          datastore_readonly = CapabilitySet('datastore_v3', capabilities=['write'])
          if datastore_readonly.is_enabled():
            # ...render form normally...
          else:
            # self.response.out('<p>Not accepting submissions right now: %s</p>' %
                                datastore_readonly.admin_message())
            # ...render form with form elements disabled...
         ```
    
    Individual API wrapper modules should expose `CapabilitySet` objects
    for users rather than relying on users to create them.  They can
    also create convenience methods that delegate to the relevant `CapabilitySet`;
    for example, `db.IsReadOnly()`.
    
    ## Modules
    
    [`capability_stub`](../../../google/appengine/api/capabilities/capability_stub) module: Stub version of the capability service API.
    
    ## Classes
    
    [`class CapabilitySet`](../../../google/appengine/api/capabilities/CapabilitySet): Encapsulates one or more capabilities.
    
    [`class UnknownCapabilityError`](../../../google/appengine/api/capabilities/UnknownCapabilityError): An unknown capability was requested.
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
