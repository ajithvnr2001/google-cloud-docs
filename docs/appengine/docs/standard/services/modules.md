---
url: https://docs.cloud.google.com/appengine/docs/standard/services/modules/
title: Using the Modules API \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:34.317133+00:00
---

# Using the Modules API  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/modules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using the Modules API Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The Modules API provides functions that return information about the current operating environment (module, version, and instance).

The Modules API also has functions that retrieve the address of a module, a version, or an instance. This allows an application to send requests from one instance to another, in both the development and production environments.

You must import the `google.appengine.api.modules` module from the SDK.
    
    
    from google.appengine.api import modules

The following code sample shows how to get the module name and instance id for a request:
    
    
    module = modules.get_current_module_name()
    instance_id = modules.get_current_instance_id()
    self.response.write(
        'module_id={}&instance_id={}'.format(module, instance_id))

The instance ID of an automatic scaled module will be returned as a unique base64 encoded value, e.g. `e4b565394caa`.

You can communicate between modules in the same app by fetching the hostname of the target module:
    
    
    backend_hostname = modules.get_hostname(module='my-backend')
    url = "http://{}/".format(backend_hostname)
    try:
        result = urllib2.urlopen(url).read()
        self.response.write('Got response {}'.format(result))
    except urllib2.URLError:
        pass

You can also use the [URL Fetch](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/outbound-requests) service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
