---
url: https://docs.cloud.google.com/logging/docs/samples/logging-rails-shared-configure/
title: Ruby: Configure Rails Logging Client \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:57:10.888792+00:00
---

# Ruby: Configure Rails Logging Client  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-rails-shared-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Ruby: Configure Rails Logging Client Stay organized with collections  Save and categorize content based on your preferences. 

Configure logging-specific client authentication for Rails.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Instrument Ruby apps for Error Reporting](https://docs.cloud.google.com/error-reporting/docs/setup/ruby)
  * [Setting Up Cloud Logging for Ruby](https://docs.cloud.google.com/logging/docs/setup/ruby)



## Code sample

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Add this to config/environments/*.rb
    Rails.application.configure do |config|
      # Stackdriver Shared parameters
      config.google_cloud.project_id = "YOUR-PROJECT-ID"
      config.google_cloud.keyfile    = "/path/to/service-account.json"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
