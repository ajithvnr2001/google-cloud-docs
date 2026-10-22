---
url: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences/
title: Migrate from Go 1.11 to the latest Go runtime \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:02.030395+00:00
---

# Migrate from Go 1.11 to the latest Go runtime  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from Go 1.11 to the latest Go runtime Stay organized with collections  Save and categorize content based on your preferences. 

This page covers instructions for migrating from the [first-generation to the second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) Go runtimes. To upgrade your second-generation app to use the latest supported version of Go, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/go/upgrade-go-runtime).

Go 1.11 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated). You won't be able to deploy Go 1.11 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing Go 1.11 applications will continue to run and receive traffic. We recommend that you migrate to the [latest supported version of Go](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go).

Migrating to a [supported second-generation Go runtime](https://docs.cloud.google.com/appengine/docs/standard/runtimes) lets you use up-to-date language features and build apps that are more portable, with idiomatic code.

## Changes in the second-generation runtimes

Consider the following differences when upgrading to a [supported](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#go) second-generation Go runtime:

  * To reduce runtime migration effort and complexity, the App Engine standard environment lets you [access many of the legacy bundled services and APIs in the second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/go/services/access), such as Memcache. Your second-generation Go app can call the bundled services APIs through the App Engine SDK for Go, and access most of the same features as on the Go 1.11 runtime.

**Note:** Not all the App Engine bundled services available for Go 1.11 have a corresponding service in the second-generation runtimes. For the full list of available legacy bundled services APIs in the second-generation runtimes, see the [legacy bundled services API references documentation](https://docs.cloud.google.com/appengine/docs/standard/go/services/access).

You also have the option to use Google Cloud products that offer similar features as the legacy bundled services. These Google Cloud products provide idiomatic [Cloud Client Libraries for Go](https://github.com/googleapis/google-cloud-go). For the bundled services that are not available as separate products in Google Cloud, such as image processing, search, and messaging, you can use third-party providers or other workarounds.

To learn more about migrating to unbundled services, see [Migrating from bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).

  * The behavior of some elements in the `app.yaml` configuration file has been modified. For more information, see Changes to the `app.yaml` file.

  * Logging in the second-generation runtime follows the logging standard in [Cloud Logging](https://docs.cloud.google.com/logging). In the second-generation runtimes, app logs are no longer bundled with the request logs but are separated in different records. To learn more about reading and writing logs in the second-generation runtimes, see the [logging guide](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).




### Memory usage differences

Second-generation runtimes see a higher baseline of memory usage compared to first-generation runtimes. This is due to multiple factors, such as different base image versions, and differences in how the two generations calculate memory usage.

Second-generation runtimes calculate instance memory usage as the sum of what an application process uses, and the number of application files dynamically cached in memory. To avoid memory-intensive applications from experiencing instance shutdowns due to exceeding memory limits, upgrade to a larger [instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) with more memory.

### CPU usage differences

Second-generation runtimes can see a higher baseline of CPU usage upon instance cold-start. Depending on an application's scaling configuration, this might have unintended side effects, such as, a higher instance count than anticipated if an application is configured to scale based on CPU utilization. To avoid this issue, review and test application scaling configurations to ensure the number of instances are acceptable.

### Request header differences

First-generation runtimes allow request headers with underscores (e.g. `X-Test-Foo_bar`) to be forwarded to the application. Second-generation runtimes introduces Nginx into the host architecture. As a result of this change, second-generation runtimes are configured to automatically remove headers with underscores (`_`). To prevent application issues, avoid using underscores in application request headers.

## Changes to the `app.yaml` file

The behavior of some elements in the `app.yaml` configuration file has been modified:

Element | Change type | Description  
---|---|---  
`app_engine_bundled_services` | Required for apps using legacy bundled services | Configure this field to access specific [legacy bundled services for supported Go versions](https://docs.cloud.google.com/appengine/docs/standard/go/services/access). For more information about the `app_engine_bundled_services` configuration settings, see the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file reference.  
`login` | Supported if you enable the Users API by configuring the `user` setting in the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=go#app_engine_bundled_services) list. | If you are not using the legacy bundled services for the second-generation runtimes, use these [ alternative methods to authenticate users](https://docs.cloud.google.com/appengine/docs/standard/authenticating-users).   
`runtime` | Modified |  Change the `runtime` element to [specify a second-generation runtime](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#runtime).   
  
For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

## Create a `main` package

Your service must include a `package main` statement in at least one source file.

### App Engine legacy bundled services

If your service uses the [legacy bundled services for the second-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/go/services/access):

  * Your service must only use v2 (`google.golang.org/appengine/v2`) packages. Using the older v1 (`google.golang.org/appengine`) packages causes errors.

  * In your `main()` function, call `appengine.Main()` instead of `http.ListenAndServe()`. This ensures that the `user` and `appengine` APIs have access to current request context.




### Writing a main package

If your service doesn't already contain a `main` package, add the `package main` statement and write a `main()` function. At a **minimum** , the `main()` function should:

  * Read the `PORT` environment variable and call the `http.ListenAndServe()` function:
        
        port := os.Getenv("PORT")
        if port == "" {
        	port = "8080"
        	log.Printf("Defaulting to port %s", port)
        }
        
        log.Printf("Listening on port %s", port)
        if err := http.ListenAndServe(":"+port, nil); err != nil {
        	log.Fatal(err)
        }




### Registering your HTTP handlers

You can register your HTTP handlers by choosing **one** of the following options:

  * The preferred method is to manually move all `http.HandleFunc()` calls from your packages to your `main()` function in your `main` package.
  * Alternatively, import your application's packages into your `main` package, ensuring each `init()` function that contains calls to `http.HandleFunc()` gets run on startup.

You can find all packages which use the `http.HandleFunc()` call with the following bash script, and copy the output into your `main` package's `import` block:
        
        gp=$(go env GOPATH) && p=$(pwd) && pkg=${p#"$gp/src/"} && find . -name "*.go" | xargs grep "http.HandleFunc" --files-with-matches | grep -v vendor/ | grep -v '/main.go' | sed "s#\./\(.*\)/[^/]\+\.go#\t_ \"$pkg/\1\"#" | sort | uniq
        




## Structuring your files

Go requires each package has its own directory. You can tell App Engine where your `main` package is by using `main:` in your project's `app.yaml` file. For example, if your app's file structure looked like this:
    
    
    myapp/
    ├── app.yaml
    ├── foo.go
    ├── bar.go
    └── web/
        └── main.go
    

Your `app.yaml` file would have:
    
    
    main: ./web # Relative filepath to the directory containing your main package.
    

For more information about the `main` flag, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/go/config/appref#main).

## Moving files to your `GOPATH`

Find your `GOPATH` by using the following command:
    
    
    go env GOPATH
    

Move all relevant files and imports to your `GOPATH`. If using relative imports, such as `import ./guestbook`, update your imports to use the full path: `import github.com/example/myapp/guestbook`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
