---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-Jobs-SnapshotJob-sync/
title: Snapshot the state of a streaming job (Ruby) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:37.054769+00:00
---

# Snapshot the state of a streaming job (Ruby)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-Jobs-SnapshotJob-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Snapshot the state of a streaming job (Ruby) Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to snapshot the state of a streaming job.

## Code sample

### Ruby

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataflow/v1beta3"
    
    ##
    # Snippet for the snapshot_job call in the Jobs service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataflow::V1beta3::Jobs::Client#snapshot_job.
    #
    def snapshot_job
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataflow::V1beta3::Jobs::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataflow::V1beta3::SnapshotJobRequest.new
    
      # Call the snapshot_job method.
      result = client.snapshot_job request
    
      # The returned object is of type Google::Cloud::Dataflow::V1beta3::Snapshot.
      p result
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
