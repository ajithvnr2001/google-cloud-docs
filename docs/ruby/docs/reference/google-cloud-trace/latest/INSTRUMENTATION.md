---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace/latest/INSTRUMENTATION/
title: Stackdriver Trace Instrumentation \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:08.833516+00:00
---

# Stackdriver Trace Instrumentation  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-trace/latest/INSTRUMENTATION/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Stackdriver Trace Instrumentation Stay organized with collections  Save and categorize content based on your preferences. 

0.46.0 (latest)  0.45.0  0.44.1  0.43.0  0.42.2  0.41.4 

Then google-cloud-trace gem provides a Rack Middleware class that integrates with Rack-based application frameworks, such as Rails and Sinatra. When installed, the middleware collects performance traces of requests and, subject to sampling constraints, submits them to the Stackdriver Trace service.

Additionally, the google-cloud-trace gem provides a Railtie class that automatically enables the Rack Middleware in Rails applications when used.

## Configuration

The default configuration enables Stackdriver instrumentation features to run on Google Cloud Platform. You can easily configure the instrumentation library if you want to run on a non Google Cloud environment or you want to customize the default behavior.

See the [Configuration Guide](https://googleapis.dev/ruby/stackdriver/latest/file.INSTRUMENTATION_CONFIGURATION.html) for full configuration parameters.

## Rails Integration

To use the Stackdriver Logging Railtie for Ruby on Rails applications, simply add this line to `config/application.rb`:
    
    
    require "google/cloud/trace/rails"

Alternatively, check out the [stackdriver](https://googleapis.dev/ruby/stackdriver/latest) gem, which enables this Railtie by default.

## Rack Integration

Other Rack base frameworks can also directly leverage the built-in Middleware.
    
    
    require "google/cloud/trace"
    use Google::Cloud::Trace::Middleware

## Faraday Middleware

On top of the Rack Middleware, you can also trace outbound Faraday requests by using the Faraday Middleware provided with this gem:
    
    
    require "google/cloud/trace/faraday_middleware"
    
    conn = Faraday.new "https://www.google.com"
    conn.use Google::Cloud::Trace::FaradayMiddleware
    
    result = conn.get

A child span will be create for each outbound Faraday request, and will be submitted together with the overall application request trace by the Rack Middleware.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
