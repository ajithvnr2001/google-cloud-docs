---
url: https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies/
title: Specify dependencies \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:38.105721+00:00
---

# Specify dependencies  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specify dependencies Stay organized with collections  Save and categorize content based on your preferences. 

Apps that run in the Go 1.12+ standard runtime can use any linux/amd64-compatible package.

App Engine requires all import statements in your Go code to specify absolute paths. For example, use:
    
    
    import "github.com/example/mypackage"
    

## Use Go modules

We recommend that you use [Go modules](https://blog.golang.org/using-go-modules) to manage dependencies in your Go app. You can continue to use the older `GOPATH` mode if you aren't ready to [migrate to Go modules](https://blog.golang.org/migrating-to-go-modules).

Starting in Go **version 1.22 and later** :

  * You can't use `go get` outside of a module in the legacy `GOPATH` mode (`GO111MODULE`=`off`). For more information, see [Tools](https://tip.golang.org/doc/go1.22#:%7E:text=enables%20this%20feature.-,Tools,-Go%20command).

  * Go recommends that you use a `go.mod` file for managing dependencies. To install dependencies during deployment, include a `go.mod` file in the same folder as the `app.yaml` file. For more information about Go versions, and managing dependencies for vendor directories, see [`GOPATH` and Modules](https://pkg.go.dev/cmd/go#hdr-GOPATH_and_Modules).




When you deploy your app, App Engine uses the `go build` command to build your app and matches the behavior of Go itself. To ensure that your app uses `module-aware` mode, do the following in your development environment:

  * Create your module's `go.mod` file in the same directory as your `app.yaml` file. App Engine searches the current directory and the successive parent directories until it finds a [`go.mod` file](https://golang.org/cmd/go/#hdr-Defining_a_module).

If App Engine doesn't find a `go.mod` file, it follows `GOPATH` mode.

  * If you set the [`GO111MODULE` environment variable](https://golang.org/ref/mod#mod-commands), make sure that the variable's value enables `module-aware` mode. When you deploy your app, App Engine checks your environment for `GO111MODULE` and matches the behavior of Go itself. App Engine only applies the `GO111MODULE` variable setting if you have included a `go.mod` file for your app.

  * For Go 1.12, don't locate your app directory within the `$GOPATH/src` folder. If your Go 1.12 app is anywhere in the `$GOPATH/src` directory tree, App Engine follows `GOPATH` mode even if you've defined a `go.mod` file for your app.

For Go 1.13 and later, App Engine uses [`module-aware` mode](https://golang.org/cmd/go/#hdr-Module_support) by default, unless `GO111MODULE` overrides the default or a `go.mod` file doesn't exist in the app's directory.




### Vendoring dependencies

**Vendoring** copies the packages your app uses into the application directory instead of downloading modules from their sources during the build process. Go provides the `go build` command to [vendor the packages your app needs](https://golang.org/cmd/go/#hdr-Modules_and_vendoring) into a directory named `vendor` in your app's root directory.

In Go 1.14 and later, if your app's root directory contains a directory named `vendor`, the `go build` command and the App Engine deployment process use the packages in the vendor directory instead of downloading modules.

In Go 1.13 and earlier, vendoring is only available if you set up your environment to use [`GOPATH` mode](https://golang.org/cmd/go/#hdr-GOPATH_and_Modules).

### Use private dependencies

App Engine can't download your private dependencies during the build process, so you must include the dependencies with your application code upon deployment.

Use the `replace` directive in your `go.mod` file to declare private dependencies. The following example assumes your app is in the `/myapp/` directory:

  1. Change to your app directory:
         
         cd /myapp
         

  2. Create a directory containing your private dependencies:
         
         mkdir private
         

Make sure your private dependency is in the `private` directory. One approach is by creating a symlink:
         
         mkdir private/private.example.com
         ln -s /path/to/private.example.com/foo private/private.example.com/foo
         

  3. Update your `go.mod` file to use the `replace` directive to use the `private` directory for your dependency:
         
         go mod edit -replace=private.example.com/foo=./private/private.example.com/foo
         

Your `go.mod` file should now look like:

### Final `go.mod` file
         
         module private.example.com/myapp
         
         require private.example.com/foo v1.2.3
         
         replace private.example.com/foo => ./private/private.example.com/foo
         

### Original `go.mod` file
         
         module private.example.com/myapp
         
         require private.example.com/foo v1.2.3
         

  4. Don't modify how you import and use your private package. Your `import` statement should look like this:
         
         import "private.example.com/foo"
         

  5. Include your private dependency in your deployment by deploying your app:
         
         gcloud app deploy
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
