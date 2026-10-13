---
url: https://docs.cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/latest/
title: Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:22.766054+00:00
---

# Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.11.0 (latest) ](https://docs.cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/latest/)
  * [ 0.10.0 ](https://docs.cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/0.10.0/)
  * [ 0.9.1 ](https://docs.cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/0.9.1/)



# Ruby Client for the Google Analytics Admin V1alpha API

API Client library for the Google Analytics Admin V1alpha API

The Analytics Admin API allows for programmatic access to the Google Analytics App+Web configuration data. You can use the Google Analytics Admin API to manage accounts and App+Web properties.

<https://github.com/googleapis/google-cloud-ruby>

This gem is a _versioned_ client. It provides basic client classes for a specific version of the Google Analytics Admin V1alpha API. Most users should consider using the main client gem, [google-analytics-admin](https://rubygems.org/gems/google-analytics-admin). See the section below titled _Which client should I use?_ for more information.

## Installation
    
    
    $ gem install google-analytics-admin-v1alpha
    

## Before You Begin

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)
  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)
  3. [Enable the API.](https://console.cloud.google.com/apis/library/analyticsadmin.googleapis.com)
  4. [Set up authentication.](https://docs.cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/latest/AUTHENTICATION "Set up authentication.")



## Quick Start
    
    
    require "google/analytics/admin/v1alpha"
    
    client = ::Google::Analytics::Admin::V1alpha::AnalyticsAdminService::Client.new
    request = ::Google::Analytics::Admin::V1alpha::GetAccountRequest.new # (request fields as keyword arguments...)
    response = client.get_account request

View the [Client Library Documentation](https://cloud.google.com/ruby/docs/reference/google-analytics-admin-v1alpha/latest) for class and method documentation.

## Enabling Logging

To enable logging for this library, set the logger for the underlying [gRPC](https://github.com/grpc/grpc/tree/master/src/ruby) library. The logger that you set may be a Ruby stdlib [`Logger`](https://ruby-doc.org/stdlib/libdoc/logger/rdoc/Logger.html) as shown below, or a [`Google::Cloud::Logging::Logger`](https://googleapis.dev/ruby/google-cloud-logging/latest) that will write logs to [Cloud Logging](https://cloud.google.com/logging/). See [grpc/logconfig.rb](https://github.com/grpc/grpc/blob/master/src/ruby/lib/grpc/logconfig.rb) and the gRPC [spec_helper.rb](https://github.com/grpc/grpc/blob/master/src/ruby/spec/spec_helper.rb) for additional information.

Configuring a Ruby stdlib logger:
    
    
    require "logger"
    
    module MyLogger
      LOGGER = Logger.new $stderr, level: Logger::WARN
      def logger
        LOGGER
      end
    end
    
    # Define a gRPC module-level logger method before grpc/logconfig.rb loads.
    module GRPC
      extend MyLogger
    end

## Supported Ruby Versions

This library is supported on Ruby 2.5+.

Google provides official support for Ruby versions that are actively supported by Ruby Core—that is, Ruby versions that are either in normal maintenance or in security maintenance, and not end of life. Currently, this means Ruby 2.5 and later. Older versions of Ruby _may_ still work, but are unsupported and not recommended. See <https://www.ruby-lang.org/en/downloads/branches/> for details about the Ruby support schedule.

## Which client should I use?

Most modern Ruby client libraries for Google APIs come in two flavors: the main client library with a name such as `google-analytics-admin`, and lower-level _versioned_ client libraries with names such as `google-analytics-admin-v1alpha`. _In most cases, you should install the main client._

### What's the difference between the main client and a versioned client?

A _versioned client_ provides a basic set of data types and client classes for a _single version_ of a specific service. (That is, for a service with multiple versions, there might be a separate versioned client for each service version.) Most versioned clients are written and maintained by a code generator.

The _main client_ is designed to provide you with the _recommended_ client interfaces for the service. There will be only one main client for any given service, even a service with multiple versions. The main client includes factory methods for constructing the client objects we recommend for most users. In some cases, those will be classes provided by an underlying versioned client; in other cases, they will be handwritten higher-level client objects with additional capabilities, convenience methods, or best practices built in. Generally, the main client will default to a recommended service version, although in some cases you can override this if you need to talk to a specific service version.

### Why would I want to use the main client?

We recommend that most users install the main client gem for a service. You can identify this gem as the one _without_ a version in its name, e.g. `google-analytics-admin`. The main client is recommended because it will embody the best practices for accessing the service, and may also provide more convenient interfaces or tighter integration into frameworks and third-party libraries. In addition, the documentation and samples published by Google will generally demonstrate use of the main client.

### Why would I want to use a versioned client?

You can use a versioned client if you are content with a possibly lower-level class interface, you explicitly want to avoid features provided by the main client, or you want to access a specific service version not be covered by the main client. You can identify versioned client gems because the service version is part of the name, e.g. `google-analytics-admin-v1alpha`.

### What about the google-apis-

Client library gems with names that begin with `google-apis-` are based on an older code generation technology. They talk to a REST/JSON backend (whereas most modern clients talk to a [gRPC](https://grpc.io/) backend) and they may not offer the same performance, features, and ease of use provided by more modern clients.

The `google-apis-` clients have wide coverage across Google services, so you might need to use one if there is no modern client available for the service. However, if a modern client is available, we generally recommend it over the older `google-apis-` clients.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
