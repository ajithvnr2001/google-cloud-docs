---
url: https://docs.cloud.google.com/appengine/docs/flexible/go/specifying-dependencies/
title: Specify dependencies \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:29:02.294428+00:00
---

# Specify dependencies  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/go/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specify dependencies Stay organized with collections  Save and categorize content based on your preferences. 

You can use any linux/amd64-compatible package with instances running in the App Engine flexible environment. These instructions assume you are using the `go get` command to get the packages directly from supported repositories, such as GitHub, Bitbucket, LaunchPad, and others.

Starting in Go version 1.22 and later:

  * You can't use `go get` outside of a module in the legacy `GOPATH` mode (`GO111MODULE`=`off`). For more information, see [Tools](https://tip.golang.org/doc/go1.22#:%7E:text=enables%20this%20feature.-,Tools,-Go%20command).

  * Go recommends that you use a `go.mod` file for managing dependencies. To install dependencies during deployment, include a `go.mod` file in the same folder as the `app.yaml` file. For more information about Go versions, and managing dependencies for vendor directories, see [GOPATH and Modules](https://pkg.go.dev/cmd/go#hdr-GOPATH_and_Modules).




## Declare and manage dependencies

Go applications are organized into packages that mirror the directory structure of your source files. When you use an import statement, the relative paths in the import are interpreted. Valid import paths are fully-qualified paths that are relative to the `src` subdirectory of all the directories that are specified in your `GOPATH`.

For example, consider an example app where you define the following:

  * `GOPATH` module:
        
        export GOPATH=/home/fred/go.
        

  * `src1-1.go` file:
        
        import "foo/bar"
        

  * The gcloud CLI looks for the `foo/bar` package in the `/home/fred/go/src/foo/bar` location when you run or deploy the app.




If you include your package sources in `GOPATH`, you must be careful not to place your source code within your app's directory where the `app.yaml` file is located. If that happens, subtle problems can occur because a package might get loaded twice, once for the path relative to a service's directory, and once again for the fully-qualified path. To avoid problems, the gcloud CLI will scan both your app's directory and `GOPATH`, and then report an error if a conflict is detected.

For best results, we recommend the following:

  * Create a separate directory in your app's directory for each service.
  * Each service's directory should contain the service's `app.yaml` file and one or more `.go` files.
  * Don't include any subdirectories in a service's directory.
  * Your `GOPATH` should specify a directory that is outside your app's directory and contain all the dependencies that your app imports.



## Download required packages

You can use the `go get` command to download packages. For example, to download `packagename` from the GitHub `my_repo`:
    
    
    go get github.com/my_repo/packagename
    

## Deploy to App Engine

To deploy your application to App Engine, you must deploy the libraries that are required by your app along with your application code. For complete details, see [Testing and deploying your application](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app#deploy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
