---
url: https://docs.cloud.google.com/appengine/docs/flexible/go/runtime/
title: The Go runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:33.454200+00:00
---

# The Go runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/go/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Go runtime Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [Go runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversions) to use the latest version of Go. 

The Go runtime is the software stack responsible for installing your application code and dependencies, and then running that application in the flexible environment.

## Go versions

Go 1.27 uses [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview). For the full list of supported Go versions, and their corresponding Ubuntu version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go).

To use a [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go) Go version, you must:

  * Install `gcloud CLI` version **420.0.0 or later**. You can update your CLI tooling by running the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command. To view your installed version, you can run the [`gcloud version`](https://docs.cloud.google.com/sdk/gcloud/reference/version) command.

  * Go recommends that you use a `go.mod` file for managing dependencies. To install dependencies during deployment, include a `go.mod` file in the same folder as the `app.yaml` file.

For example, the folder structure of your app with `go.mod` must represent:
        
        <application-root>/
        --> app.yaml
        --> go.mod
        --> Other source files used in your application.
        
        

  * Include the `runtime_config` and `operating_system` settings in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) file to specify an operating system.

  * Optionally, you can specify a runtime version by including the `runtime_version` setting in your `app.yaml`. By default, the latest Go version is used if the `runtime_version` setting is not specified.




**Examples**

  * To specify Go 1.27 on Ubuntu 24:
        
        runtime: go
        env: flex
        
        runtime_config:
            operating_system: "ubuntu24"
            runtime_version: "1.27"
        

  * To specify the latest supported Go version on Ubuntu 24:
        
        runtime: go
          env: flex
        
          runtime_config:
              operating_system: "ubuntu24"
        




Your app uses the latest stable release of the version that is specified in your `app.yaml` file. App Engine automatically updates to new patch revisions, but it won't automatically update the major version.

For example, your application might be deployed at Go 1.18.10, and later it might be automatically updated to Go 1.18.11, but it won't be automatically updated to the major version Go 1.19.

Choosing Go 1.27 in your `app.yaml` file results in the latest `patch` version of Go 1.27 available.
    
    
      runtime: go
      env: flex
    
      runtime_config:
          operating_system: "ubuntu24"
          runtime_version: "1.27"
    

See the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) reference for more information.

### Previous runtime versions

**Warning:** Go **version 1.15 and earlier** have reached end of support. App Engine blocks you from deploying your applications using runtimes that have reached end of support. We recommend that you migrate your app to use a [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go) of Go or use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes).

To use Go **version 1.15 and earlier** , specify a version in `runtime` setting using the `go1.x` format in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) file. For example:
    
    
      runtime: go1.14
      env: flex

If no version is specified, the default version of `go1.11` will be automatically selected.

Your app uses the latest stable release of the version that is specified in your `app.yaml` file. App Engine automatically updates to new patch revisions, but it won't automatically update the major version.

For example, your application might be deployed at Go 1.14.10, and later it might be automatically updated to Go 1.14.11, but it won't be automatically updated to the major version Go 1.15.

Choosing the go runtime version `go1.15` in your `app.yaml` file results in the latest version of 1.15 available, for example, 1.15.15.
    
    
      runtime: go1.15
      env: flex

### Support for other Go runtimes

If you need to use a Go version that isn't [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go), you can create a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) and select a valid base image with the Go version you need.

For Google-supplied base images or [Docker Go base images](https://hub.docker.com/_/golang), see [Building custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base).

## Import packages

Your code compiles when you deploy your app to App Engine. When you run the deployment command, your app's dependencies are first collected from your local `GOPATH` and then they are all sent to the build server. Any missing dependencies, for example third-party libraries, results in build failures.

To avoid build failures and ensure that all your app's dependencies get deployed with your code, you should [test your app locally before deploying it](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app).

## Extending the runtime

For instructions on how to extend and customize the Go runtime, read the [Go runtime builder on GitHub](https://github.com/GoogleCloudPlatform/golang-docker/tree/master/runtime-builder).

## Metadata server

Each instance of your application can use the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to query information about the instance, including its host name, external IP address, instance ID, custom metadata, and service account information. App Engine does not allow you to set custom metadata for each instance, but you can set [project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide) and read it from your App Engine and Compute Engine instances.

Use the [`cloud.google.com/go/compute/metadata`](https://godoc.org/cloud.google.com/go/compute/metadata) package to access the metadata server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
