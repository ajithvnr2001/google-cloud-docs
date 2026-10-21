---
url: https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime/
title: The Ruby runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:25:25.170442+00:00
---

# The Ruby runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Ruby runtime Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [Ruby runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/ruby/runtime#newversions) to use the latest version of Ruby. 

The Ruby runtime is the software stack responsible for installing your application code and dependencies, and then running that application in the flexible environment.

## Ruby versions

Ruby 4.0 uses [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview). For the full list of supported Ruby versions, and their corresponding Ubuntu version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby).

To use a supported Ruby version, you must:

  * Specify a Ruby version in your [`Gemfile`](https://bundler.io/v2.4/man/gemfile.5.html).
        
        RUBY VERSION
          ruby "4.0.x"
        

  * Install gcloud CLI version **420.0.0 or later**. You can update your CLI tooling by running the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command. To view your installed version, you can run the [`gcloud version`](https://docs.cloud.google.com/sdk/gcloud/reference/version) command.

  * Specify the `operating_system` setting in your `app.yaml` file:
        
        runtime: ruby
          env: flex
        
          runtime_config:
              operating_system: "ubuntu24"
        

  * Optionally, you can specify a version of the Ruby interpreter using a `.ruby-version` file in your application directory. For example, `4.0.x`




### Previous versions

**Warning:** Ruby **version 3.1 and earlier** have reached end of support. App Engine blocks you from deploying your applications using runtimes that have reached end of support. We recommend that you migrate your app to use a [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby) of Ruby or use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes).

To use Ruby runtime **version 3.1 and earlier** , specify a version of the Ruby interpreter using a `.ruby-version` file in your application directory.

When this file is present, the runtime installs the requested version of Ruby when you deploy your application using [rbenv](https://github.com/rbenv/rbenv). If the requested version cannot be installed, App Engine shows an error message during deployment.

If you don't provide a `.ruby-version` file, the Ruby runtime defaults to version 2.7. Note that the default can change at any time, so it is recommended that your app specifies a Ruby version.

### Support for other Ruby runtimes

If you need to use a Ruby version that isn't [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#ruby), you can create a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) and select a valid base image with the Ruby version you need.

For Google-supplied base images or [Docker Ruby base images](https://hub.docker.com/_/ruby), see [Building custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base).

## Dependencies

The runtime looks for a [`Gemfile`](https://bundler.io/v2.4/man/gemfile.5.html) file in your application's source directory and uses [`Bundler`](http://bundler.io/) to install any dependencies before starting your application. For more information on declaring and managing packages, see [Using Ruby Libraries](https://docs.cloud.google.com/appengine/docs/flexible/ruby/specifying-dependencies).

### Using C libraries with Ruby

For Ruby libraries that require C extensions, the headers for the current Ruby version and the following [Ubuntu packages](https://packages.ubuntu.com/) are pre-installed on the system.

  * `autoconf`
  * `build-essential`
  * `ca-certificates`
  * `cmake`
  * `curl`
  * `file`
  * `git`
  * `imagemagick`
  * `libcurl3`
  * `libcurl3-gnutls`
  * `libcurl4-openssl-dev`
  * `libffi-dev`
  * `libgdbm-dev`
  * `libgit2-dev`
  * `libgmp-dev`
  * `libicu-dev`
  * `libjemalloc-dev`
  * `libjemalloc1`
  * `libmagickwand-dev`
  * `libmysqlclient-dev`
  * `libncurses5-dev`
  * `libpq-dev`
  * `libqdbm-dev`
  * `libreadline6-dev`
  * `libsqlite3-dev`
  * `libssl-dev`
  * `libxml2-dev`
  * `libxslt-dev`
  * `libyaml-dev`
  * `libz-dev`
  * `systemtap`
  * `tzdata`



These packages allow the installation of most popular Ruby libraries. If your application requires additional operating-system level dependencies, you will need to use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) based on this runtime to install the appropriate packages.

## Application startup

The runtime starts your application using the `entrypoint` defined in [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#entrypoint). The entrypoint should start a process that responds to HTTP requests on the port defined by the environment variable `PORT`. For example:
    
    
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

The following environment variables are set by the runtime environment:

Environment Variable | Description  
---|---  
`GAE_INSTANCE` | The name of the current instance.  
`GAE_MEMORY_MB` | The amount of memory available to the application process.  
`GAE_SERVICE` | The service name specified in your application's `app.yaml` file, or if no service name is specified, it is set to `default`.  
`GAE_VERSION` | The version label of the current application.  
`GOOGLE_CLOUD_PROJECT` | The Project ID associated with your application, which is visible in the Google Cloud console  
`PORT` | The port that will receive HTTP requests.  
`RACK_ENV` | Set to `production`.  
`RAILS_ENV` | Set to `production`.  
`RAILS_SERVE_STATIC_FILES` | Set to `true`.  
  
You can set additional environment variables with [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#defining_environment_variables).

## Metadata server

Each instance of your application can use the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to query information about the instance, including its hostname, external IP address, instance ID, custom metadata, and service account information. App Engine doesn't allow you to set custom metadata for each instance, but you can set [project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide) and read it from your App Engine and Compute Engine instances.

This example function uses the metadata server to get an external IP address of an instance.
    
    
    require "sinatra"
    require "net/http"
    
    get "/" do
      uri = URI.parse(
        "http://metadata.google.internal/computeMetadata/v1" +
        "/instance/network-interfaces/0/access-configs/0/external-ip"
      )
    
      request = Net::HTTP::Get.new uri.path
      request.add_field "Metadata-Flavor", "Google"
    
      http = Net::HTTP.new uri.host, uri.port
    
      response = http.request request
    
      "External IP: #{response.body}"
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
