---
url: https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime/
title: Ruby Runtime Environment \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:01.709851+00:00
---

# Ruby Runtime Environment  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/ruby/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Ruby Runtime Environment Stay organized with collections  Save and categorize content based on your preferences. 

The Ruby runtime allows you to run your app in App Engine in a sandbox environment. This document explains the details of the Ruby runtime environment, including what headers are provided to your code and other information to successfully deploy your application on App Engine.

Specify the Ruby runtime for App Engine in the standard environment in the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file:
    
    
    runtime: rubyVERSION

Where VERSION is the Ruby `MAJOR` and `MINOR` version numbers. For example, to use the latest Ruby version, Ruby 4.0, specify `40`.

For other supported Ruby versions, and the corresponding Ubuntu version for your Ruby version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#ruby).

## Ruby version

The latest supported Ruby version is 4.0. The Ruby runtime uses the latest stable release of the version that is specified in your `app.yaml` file. App Engine automatically updates to new patch release versions, but it will not automatically update the minor version.

For example, your application might be deployed at Ruby 2.6.0 and automatically updated to version 2.6.1 at a later deployment, but it will not be automatically updated to Ruby 2.7.

## Dependencies

For more information on declaring and managing dependencies, see [Specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/ruby/specifying-dependencies).

## Application startup

The runtime starts your application using the `entrypoint` defined in [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint). The entrypoint should start a process that responds to HTTP requests on the port defined by the environment variable `PORT`. For example:
    
    
    entrypoint: bundle exec rails server -p $PORT
    

Most web applications use a [Rack](http://rack.github.io/)-supported web server such as [Puma](http://puma.io/), [Unicorn](http://unicorn.bogomips.org/) or [Thin](https://github.com/macournoyer/thin).

You must add the server as a dependency in your application's `Gemfile` configuration file. The runtime will install all dependencies before your entrypoint is called.
    
    
    source "https://rubygems.org"
    
    gem "rack"
    gem "puma"
    

An example entrypoint using puma for a Rails application:
    
    
    entrypoint: bundle exec rails server Puma -p $PORT
    

An example entrypoint using puma for any Rack application:
    
    
    entrypoint: bundle exec rackup -s Puma -p $PORT
    

For applications that can handle requests without a Rack server, you can just execute a ruby script:
    
    
    entrypoint: bundle exec ruby app.rb
    

**Note:** The entrypoint command will be executed by [bash's `exec` function](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#Bourne-Shell-Builtins). Shell variables such as `$PORT` will be replaced normally, but shell syntax such as `if`, `for` and `while` embedded in the `entrypoint` command will not function.

## Environment variables

The following environment variables are set by the runtime:

Environment variable | Description  
---|---  
`GAE_APPLICATION` | The ID of your App Engine application. This ID is prefixed with 'region code~' such as 'e~' for applications deployed in Europe.  
`GAE_DEPLOYMENT_ID` | The ID of the current deployment.  
`GAE_ENV` | The App Engine environment. Set to `standard`.  
`GAE_INSTANCE` | The ID of the instance on which your service is currently running.  
`GAE_MEMORY_MB` | The amount of memory available to the application process, in MB.  
`GAE_RUNTIME` | The runtime specified in your `app.yaml` file.  
`GAE_SERVICE` | The service name specified in your `app.yaml` file. If no service name is specified, it is set to `default`.  
`GAE_VERSION` | The current version label of your service.  
`GOOGLE_CLOUD_PROJECT` | The Google Cloud project ID associated with your application.  
`PORT` | The port that receives HTTP requests.  
`NODE_ENV` (Only available in the Node.js runtime) | Set to `production` when your service is deployed.  
  
You can [define additional environment variables in your `app.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#environment_variables), but the above values cannot be overridden, except for `NODE_ENV`. 

## HTTPS and forwarding proxies

App Engine terminates HTTPS connections at the load balancer and forwards requests to your application. Some applications need to determine the original request IP and protocol. The user's IP address is available in the standard `X-Forwarded-For` header. Applications that require this information should configure their web framework to trust the proxy.

## Filesystem

The runtime includes a writable `/tmp` directory, with all other directories having read-only access. Writing to `/tmp` takes up system memory. For more information, see the [`TempDir`](https://ruby-doc.org/stdlib-2.5.0/libdoc/tmpdir/rdoc/Dir.html) and [`TempFile`](https://ruby-doc.org/stdlib-2.5.0/libdoc/tempfile/rdoc/Tempfile.html) documentation.

## Metadata server

Each instance of your application can use the App Engine metadata server to query information about the instance and your project.

**Note:** Custom metadata is not supported in the standard environment.

You can access the metadata server through the following endpoints:

  * `http://metadata`
  * `http://metadata.google.internal`



Requests sent to the metadata server must include the request header `Metadata-Flavor: Google`. This header indicates that the request was sent with the intention of retrieving metadata values.

The following table lists the endpoints where you can make HTTP requests for specific metadata:

Metadata endpoint | Description  
---|---  
`/computeMetadata/v1/project/numeric-project-id` | The project number assigned to your project.  
`/computeMetadata/v1/project/project-id` | The project ID assigned to your project.  
`/computeMetadata/v1/instance/region` | The region the instance is running in.  
`/computeMetadata/v1/instance/service-accounts/default/aliases` |   
`/computeMetadata/v1/instance/service-accounts/default/email` | The default service account email assigned to your project.  
`/computeMetadata/v1/instance/service-accounts/default/` | Lists all the default service accounts for your project.  
`/computeMetadata/v1/instance/service-accounts/default/scopes` | Lists all the supported scopes for the default service accounts.  
`/computeMetadata/v1/instance/service-accounts/default/token` | Returns the auth token that can be used to authenticate your application to other Google Cloud APIs.  
  
For example, to retrieve your project ID, send a request to `http://metadata.google.internal/computeMetadata/v1/project/project-id`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
