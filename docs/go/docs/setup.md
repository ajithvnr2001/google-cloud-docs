---
url: https://docs.cloud.google.com/go/docs/setup/
title: Setting up your development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:44.726578+00:00
---

# Setting up your development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Guides ](https://docs.cloud.google.com/go/docs/setup)



Send feedback 

#  Setting up your development environment Stay organized with collections  Save and categorize content based on your preferences. 

Prepare your environment for [Go](https://golang.org/) app development and deployment on Google Cloud by installing the following tools.

## Install Go

  1. To install Go, see [Go Getting Started](https://golang.org/doc/install).

  2. Confirm that you have the most recent version of Go installed:
         
         go version
         




## Install an editor

To maximize your Go development efficacy, these [popular editor plugins and IDEs](https://golang.org/doc/editors.html) provide the following features:

  * Fully integrated debugging capabilities
  * Syntax highlighting
  * Code completion



## Install the Google Cloud CLI

The [Google Cloud CLI](https://docs.cloud.google.com/sdk) is a set of tools for Google Cloud. It contains the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud) and [`bq`](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) command-line tools used to access Compute Engine, Cloud Storage, BigQuery, and other services from the command line. You can run these tools interactively or in your automated scripts.

For example, to [deploy a Go web app](https://docs.cloud.google.com/appengine/docs/standard/go/create-app) with a `main` package to App Engine, run the following command: 
    
    
    gcloud app deploy
    

To install the gcloud CLI, see [Installing the gcloud CLI](https://docs.cloud.google.com/sdk/install). 

## Install the Cloud Client Libraries for Go

The [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) is the idiomatic way for Go developers to integrate with Google Cloud services, such as Datastore and Cloud Storage.

For example, to install the package for an individual API, such as the Cloud Storage API, do the following:

  1. If you already have a Go module for your project, change to that directory. Otherwise, create a module: 
         
         go mod init YOUR_MODULE_NAME
         

Replace `YOUR_MODULE_NAME` with the name of the new module.

  2. Use the Cloud Storage package in your project: 
         
         go get cloud.google.com/go/storage
         

**Note:** The source of the Cloud Client Libraries for Go is [on GitHub](https://github.com/googleapis/google-cloud-go)



## Set up authentication

To use the Cloud Client Libraries in a local development environment, set up Application Default Credentials.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

## Install other useful tools

For a comprehensive list of Go tools and libraries, see [this list of Go frameworks, libraries, and software on GitHub](https://github.com/avelino/awesome-go).

## What's next

  * Learn more about [Go on Google Cloud](https://docs.cloud.google.com/go).

  * Deploy a Go app on [App Engine](https://docs.cloud.google.com/appengine/docs/standard/go/create-app). 

  * Explore [authentication methods at Google](https://docs.cloud.google.com/docs/authentication).

  * Browse the [documentation for Google Cloud products](https://docs.cloud.google.com/products).

  * Clone the [Go samples repository from GitHub](https://github.com/GoogleCloudPlatform/golang-samples).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
