---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/upgrade-python-runtime/
title: Upgrade an existing application \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:08.192715+00:00
---

# Upgrade an existing application  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/upgrade-python-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Upgrade an existing application Stay organized with collections  Save and categorize content based on your preferences. 

You must upgrade your applications to the [latest supported runtime version ](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python) to continue receiving security updates and be eligible for technical support.

The process of upgrading an existing app depends on the runtime version that your app currently uses:

  * **Python 2.7 (first-generation runtime)** : You must migrate your app to the [latest supported Python version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python). Python 2.7 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on January 31, 2024. Your existing Python 2.7 applications will continue to run and receive traffic. However, App Engine might block re-deployment of applications that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python). To migrate from Python 2.7 to the latest supported version of Python, see [Migrate to the Python 3 runtime](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences).

  * **Python second-generation runtimes (after end of support)** : To upgrade to a [supported version of Python](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python), update the `app.yaml` file by specifying a version of Python that you want your app to run. For example:
        
        runtime: pythonVERSION
        

Where VERSION is the Python `MAJOR` and `MINOR` version numbers. For example, to use the latest Python version, Python 3.14, specify `314`. For more information, see the [Python runtime overview](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
