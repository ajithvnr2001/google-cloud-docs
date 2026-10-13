---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting/latest/
title: Error Reporting \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:18.097403+00:00
---

# Error Reporting  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Error Reporting Stay organized with collections  Save and categorize content based on your preferences. 

0.45.1 (latest)  0.45.0  0.44.0  0.43.0  0.42.3 

Error Reporting counts, analyzes and aggregates the crashes in your running cloud services. The Error Reporting Instrumentation client provides a simple way to report errors from your application.

For general information about Error Reporting, read [Error Reporting Documentation](https://cloud.google.com/error-reporting/docs/).

The goal of google-cloud is to provide an API that is comfortable to Rubyists. Your authentication credentials are detected automatically in Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run. In other environments you can configure authentication easily, either directly in your code or via environment variables. Read more about the options for connecting in the [Authentication Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting/latest/AUTHENTICATION "Authentication Guide").

## How to report errors

You can easily report exceptions from your applications to Error Reporting service:
    
    
    require "google/cloud/error_reporting"
    
    # Configure Error Reporting instrumentation
    Google::Cloud::ErrorReporting.configure do |config|
      config.project_id = "my-project"
      config.keyfile = "/path/to/keyfile.json"
    end
    
    # Insert a Rack Middleware to report unhanded exceptions
    use Google::Cloud::ErrorReporting::Middleware
    
    # Or explicitly submit exceptions
    begin
      fail "Boom!"
    rescue => exception
      Google::Cloud::ErrorReporting.report exception
    end

See the [Instrumentation Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting/latest/INSTRUMENTATION "Instrumentation Guide") for more examples.

## Additional information

Error Reporting can be configured to use gRPC's logging. To learn more, see the[Logging guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-error_reporting/latest/LOGGING "Logging guide").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-18 UTC."],[],[]] 
