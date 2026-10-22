---
url: https://docs.cloud.google.com/appengine/docs/standard/go/upgrade-go-runtime/
title: Upgrade an existing application \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:55.422629+00:00
---

# Upgrade an existing application  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/upgrade-go-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Upgrade an existing application Stay organized with collections  Save and categorize content based on your preferences. 

You must upgrade your applications to the [latest supported runtime version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go) to continue receiving security updates and be eligible for technical support.

The process of upgrading an existing app depends on the runtime version that your app currently uses:

  * **Go 1.11 (first-generation runtime)** : You must migrate your app to the [latest supported Go version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go). Go 1.11 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on January 30, 2024. Your existing Go 1.11 applications will continue to run and receive traffic. However, App Engine might block re-deployment of applications that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go). To migrate to the latest supported version of Go, see [Migrate from Go 1.11 to the latest Go runtime](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences).

  * **Go second-generation runtimes (after end of support)** : To upgrade to a [supported version of Go](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go), update the `app.yaml` file by specifying a version of Go that you want your app to run. For example:
        
        runtime: goVERSION
        

Where VERSION is the Go `MAJOR` and `MINOR` version numbers. For example, to use the latest Go version, Go 1.27, specify `127`. For more information, see the [Go runtime overview](https://docs.cloud.google.com/appengine/docs/standard/go/runtime).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
