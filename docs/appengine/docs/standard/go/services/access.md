---
url: https://docs.cloud.google.com/appengine/docs/standard/go/services/access/
title: Access legacy bundled services for Go \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:39.003179+00:00
---

# Access legacy bundled services for Go  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/services/access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Access legacy bundled services for Go Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install and use the bundled services with the [Go runtime](https://docs.cloud.google.com/appengine/docs/standard/go/runtime) for App Engine standard environment. Your app can access the bundled services through the **App Engine services SDK for Go**.

## Before you begin

  * Refer to the [list of legacy bundled services APIs](https://docs.cloud.google.com/appengine/docs/standard/services/overview) you can call in the Go runtime.
  * Before starting a migration project to Go, see the [runtime migration overview](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences) and migration considerations when using legacy bundled services.



## Installing the App Engine services SDK

To call the legacy bundled services APIs with Go, you must use the latest SDK. Follow these steps:

  1. Update your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=go#app_engine_bundled_services) file to specify one or more legacy bundled services. For example:
         
         app_engine_bundled_services:
         - datastore_v3
         - memcache
         - user
         

If you use features such as `login: admin` in the `handlers` section of `app.yaml` file, enable the Users API by configuring the `user` setting in the `app_engine_bundled_services` list.

  2. Add a reference to the latest SDK in your `go.mod` file by running `go get` in the terminal as follows:
         
         go get google.golang.org/appengine/v2
         

The main difference when upgrading to Go is using v2 of the App Engine services SDK.

  3. In your app, modify your import statements by inserting `/v2/` in the old package names. For example, if using Memcache, do the following:
         
         import (
           "google.golang.org/appengine/v2"
           "google.golang.org/appengine/v2/memcache"
         )
         

For the full list of available package names, see the [legacy bundled services API references documentation](https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest).

  4. Run `go mod tidy` to clean up references in your `go.mod` file.
         
         go mod tidy
         


**Note:** When upgrading to a new major version of a Go dependency, such as a package or library, make sure to include the major version number of the dependency in your import statements. If you run `go mod tidy` and find that it is still importing an older version of the App Engine services SDK for Go, you have probably missed upgrading an import statement.

## Migration considerations

You should be aware of the following considerations if you are migrating to the Go runtime and your app uses legacy bundled services:

  * To test the legacy bundled services functionality in your Go app, [run your application in your local environment](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#running_locally) with the development tools that you usually use, such as `go run`.
  * To deploy your app, use the [`gcloud app deploy`](https://docs.cloud.google.com/appengine/docs/standard/go/building-app#deploying_your_web_service_on) command.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
