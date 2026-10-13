---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-AsyncWriterError/
title: Cloud Logging API - Class Google::Cloud::Logging::AsyncWriterError (v2.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:48.753416+00:00
---

# Cloud Logging API - Class Google::Cloud::Logging::AsyncWriterError (v2.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-AsyncWriterError/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Logging API - Class Google::Cloud::Logging::AsyncWriterError (v2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.0 (latest)  2.6.1  2.5.0  2.4.0  2.3.3  2.2.2 

Reference documentation and code samples for the Cloud Logging API class Google::Cloud::Logging::AsyncWriterError.

## AsyncWriterError

Used to indicate a problem preventing [AsyncWriter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-AsyncWriter "Google::Cloud::Logging::AsyncWriter \(class\)") from asynchronously calling the API. This can occur when the [AsyncWriter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-AsyncWriter "Google::Cloud::Logging::AsyncWriter \(class\)") has too few resources allocated for the amount of usage.

## Inherits

  * Google::Cloud::Error 



## Example
    
    
    require "google/cloud/logging"
    require "google/cloud/error_reporting"
    
    logging = Google::Cloud::Logging.new
    
    resource = logging.resource "gae_app",
                                module_id: "1",
                                version_id: "20150925t173233"
    
    async = logging.async_writer
    
    # Register to be notified when unhandled errors occur.
    async.on_error do |error|
      # error can be a AsyncWriterError, with entries
      Google::Cloud::ErrorReporting.report error
    end
    
    logger = async.logger "my_app_log", resource, env: :production
    logger.info "Job started."

## Methods 

### #count
    
    
    def count() -> Array<Google::Cloud::Logging::Entry>

objects that were not written to the API due to the error.

**Returns**

  * (Array<[Google::Cloud::Logging::Entry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-Entry)>) — entries The entry 



### #entries
    
    
    def entries()

Returns the value of attribute entries.

### #initialize
    
    
    def initialize(message, entries = nil) -> AsyncWriterError

**Returns**

  * ([AsyncWriterError](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging-AsyncWriterError)) — a new instance of AsyncWriterError 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-25 UTC."],[],[]] 
