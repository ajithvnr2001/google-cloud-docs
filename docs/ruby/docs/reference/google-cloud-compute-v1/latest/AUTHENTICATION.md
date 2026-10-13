---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/AUTHENTICATION/
title: Authentication \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:25.626090+00:00
---

# Authentication  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/AUTHENTICATION/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Authentication Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

The recommended way to authenticate to the google-cloud-compute-v1 library is to use [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials). To review all of your authentication options, see Credentials lookup.

## Quickstart

The following example shows how to set up authentication for a local development environment with your user credentials. 

**NOTE:** This method is _not_ recommended for running in production. User credentials should be used only during development.

  1. [Download and install the Google Cloud CLI](https://cloud.google.com/sdk).
  2. Set up a local ADC file with your user credentials:


    
    
    gcloud auth application-default login
    

  1. Write code as if already authenticated.



For more information about setting up authentication for a local development environment, see [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev).

## Credential Lookup

The google-cloud-compute-v1 library provides several mechanisms to configure your system. Generally, using Application Default Credentials to facilitate automatic credentials discovery is the easist method. But if you need to explicitly specify credentials, there are several methods available to you.

Credentials are accepted in the following ways, in the following order or precedence:

  1. Credentials specified in method arguments
  2. Credentials specified in configuration
  3. Credentials pointed to or included in environment variables
  4. Credentials found in local ADC file
  5. Credentials returned by the metadata server for the attached service account (GCP)



### Configuration

You can configure a path to a JSON credentials file, either for an individual client object or globally, for all client objects. The JSON file can contain credentials created for [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation), [workforce identity federation](https://cloud.google.com/iam/docs/workforce-identity-federation), or a [service account key](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-key).

Note: Service account keys are a security risk if not managed correctly. You should [choose a more secure alternative to service account keys](https://cloud.google.com/docs/authentication#auth-decision-tree) whenever possible.

To configure a credentials file for an individual client initialization:
    
    
    require "google/cloud/compute/v1"
    
    client = ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new do |config|
      config.credentials = "path/to/credentialfile.json"
    end

To configure a credentials file globally for all clients:
    
    
    require "google/cloud/compute/v1"
    
    ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.configure do |config|
      config.credentials = "path/to/credentialfile.json"
    end
    
    client = ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new

### Environment Variables

You can also use an environment variable to provide a JSON credentials file. The environment variable can contain a path to the credentials file or, for environments such as Docker containers where writing files is not encouraged, you can include the credentials file itself.

The JSON file can contain credentials created for [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation), [workforce identity federation](https://cloud.google.com/iam/docs/workforce-identity-federation), or a [service account key](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-key).

Note: Service account keys are a security risk if not managed correctly. You should [choose a more secure alternative to service account keys](https://cloud.google.com/docs/authentication#auth-decision-tree) whenever possible.

The environment variables that google-cloud-compute-v1 checks for credentials are:

  * `GOOGLE_CLOUD_CREDENTIALS` \- Path to JSON file, or JSON contents
  * `GOOGLE_APPLICATION_CREDENTIALS` \- Path to JSON file


    
    
    require "google/cloud/compute/v1"
    
    ENV["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/credentialfile.json"
    
    client = ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new

### Local ADC file

You can set up a local ADC file with your user credentials for authentication during development. If credentials are not provided in code or in environment variables, then the local ADC credentials are discovered.

Follow the steps in Quickstart to set up a local ADC file.

### Google Cloud Platform environments

When running on Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run, credentials are retrieved from the attached service account automatically. Code should be written as if already authenticated.

For more information, see [Set up ADC for Google Cloud services](https://cloud.google.com/docs/authentication/provide-credentials-adc#attached-sa).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
