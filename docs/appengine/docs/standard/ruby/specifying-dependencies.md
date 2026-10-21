---
url: https://docs.cloud.google.com/appengine/docs/standard/ruby/specifying-dependencies/
title: Specifying dependencies \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:39.852820+00:00
---

# Specifying dependencies  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/ruby/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specifying dependencies Stay organized with collections  Save and categorize content based on your preferences. 

Dependencies for Ruby applications are declared in a [`Gemfile`](https://bundler.io/v2.4/man/gemfile.5.html) file.

For example:
    
    
    source "https://rubygems.org"
    
    gem "rails"
    

You can use any Linux-compatible Ruby package in the App Engine standard environment, including packages that require native (C) extensions.

The Ruby runtime will [automatically install](https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime#dependencies) all dependencies declared in your `Gemfile` file during deployment.

## Installing a web framework

You'll need to use a web framework to enable your app to serve web requests. You can use any Ruby web framework including the following:

  * [Ruby on Rails](http://rubyonrails.org/)
  * [Sinatra](http://www.sinatrarb.com/)
  * [Rack](http://rack.github.io/)



To use a particular web framework, specify a startup command in your `app.yaml` file:
    
    
    runtime: ruby
    entrypoint: rails server
    

## Installing the Cloud Client Libraries

The [Cloud Client Libraries for Ruby](https://docs.cloud.google.com/ruby/docs/reference) is a client library for accessing Google Cloud services that significantly reduces the boilerplate code you have to write. The library provides high-level API abstractions so they're easier to understand and means you spend more time creating code that matters to you.

To install the library locally:
    
    
    gem install google-cloud
    

The client library can automatically handle authentication for you locally as well by using [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs):
    
    
    gcloud auth login
    

For details on configuring Cloud Client Libraries for Ruby to handle authentication automatically, see [Authenticate to Cloud services using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
