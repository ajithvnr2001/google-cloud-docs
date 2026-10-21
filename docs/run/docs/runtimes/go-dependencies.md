---
url: https://docs.cloud.google.com/run/docs/runtimes/go-dependencies/
title: Specify dependencies in Go \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:54.720699+00:00
---

# Specify dependencies in Go  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/go-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Specify dependencies in Go Stay organized with collections  Save and categorize content based on your preferences. 

You can specify your Cloud Run function dependencies with either a [Go Module](https://golang.org/doc/go1.11#modules) or a `vendor` directory.

## Specify dependencies with Go modules

To specify Cloud Run functions dependencies with a Go Module, you list them in a `go.mod` file. When you deploy your function, Go automatically incorporates the dependencies in your `go.mod` file.

To create a `go.mod` file, see [Managing dependencies in Go](https://go.dev/doc/modules/managing-dependencies).

The [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-go) is a required dependency for all functions. Although Cloud Run functions installs it on your behalf when the function is created, we recommend that you include it as an explicit dependency for clarity.

If your function relies on private dependencies, we recommend that you mirror `functions-framework` to your private registry. Include the mirrored `functions-framework` as a dependency to your function to avoid installing the package from the public internet.

## Specify dependencies with a `vendor` directory

Cloud Run functions also lets you include your dependencies with a [`vendor` directory](https://golang.org/cmd/go/#hdr-Vendor_Directories). Using a vendor directory is helpful if your dependency is not available through a dependency manager or if your Cloud Run functions environment's internet access is restricted.

Most of the time, `vendor` directories are maintained with a dependency manager. You can use any dependency manager you like. For example, you can use Go's Modules functionality to create a `vendor` directory from your `go.mod` file.

You must include the [Functions Framework for Go](https://github.com/GoogleCloudPlatform/functions-framework-go) in your vendor directory. To use the Go toolchain to do this:

  1. Add the following directive to the import block of your Go code:
         
         _ "github.com/GoogleCloudPlatform/functions-framework-go/funcframework"
         

  2. Update your `go.mod` file to include the new imported package:
         
         go mod tidy
         

  3. Create a `vendor` directory using the contents of your `go.mod` file:
         
         go mod vendor
         




### Go versions earlier than 1.16

For versions of Go earlier than 1.16, if you have a `go.mod` file and a `vendor` directory, the `vendor` directory will be ignored when you deploy your function. To ensure that your vendor directory is respected, use a [`.gcloudignore`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) file to avoid uploading your `go.mod` and `go.sum` files:

  1. Create a `.gcloudignore` file at the root of your project directory with the following contents:
         
         go.mod
         go.sum
         
         # Also ignore Git directories. Delete the following two lines if you want to
         # upload them.
         .git
         .gitignore
         


**Note:** Learn more about Cloud Run policy for [supporting existing deployments](https://docs.cloud.google.com/functions/docs/concepts/go-runtime#go_116_public_preview) for functions based on a version earlier than 1.16.

## Use private dependencies

If your function's dependencies are hosted in a repository that is not publicly accessible, you must use a `vendor` directory to fetch your dependencies before deploying your function. If you plan to use a `go.mod` file, see the preceding instructions to avoid potential conflicts between the `go.mod` file and the `vendor` directory.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
