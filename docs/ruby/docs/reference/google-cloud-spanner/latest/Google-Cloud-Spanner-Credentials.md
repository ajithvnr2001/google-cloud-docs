---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Credentials/
title: Cloud Spanner API - Class Google::Cloud::Spanner::Credentials (v2.36.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:13.259711+00:00
---

# Cloud Spanner API - Class Google::Cloud::Spanner::Credentials (v2.36.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner API - Class Google::Cloud::Spanner::Credentials (v2.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.36.0 (latest)  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.1  2.11.0 

Reference documentation and code samples for the Cloud Spanner API class Google::Cloud::Spanner::Credentials.

## Credentials

Represents the authentication and authorization used to connect to the Spanner API.

## Inherits

  * Google::Cloud::Spanner::V1::Spanner::Credentials 



## Example
    
    
    require "google/cloud/spanner"
    
    keyfile = "/path/to/keyfile.json"
    creds = Google::Cloud::Spanner::Credentials.new keyfile
    
    spanner = Google::Cloud::Spanner.new(
      project_id: "my-project",
      credentials: creds
    )
    
    spanner.project_id #=> "my-project"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-09 UTC."],[],[]] 
