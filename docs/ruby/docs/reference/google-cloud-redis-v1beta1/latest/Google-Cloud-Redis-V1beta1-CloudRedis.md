---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CloudRedis/
title: Google Cloud Memorystore for Redis V1beta1 API - Module Google::Cloud::Redis::V1beta1::CloudRedis (v0.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:42.609603+00:00
---

# Google Cloud Memorystore for Redis V1beta1 API - Module Google::Cloud::Redis::V1beta1::CloudRedis (v0.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CloudRedis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1beta1 API - Module Google::Cloud::Redis::V1beta1::CloudRedis (v0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1beta1 API module Google::Cloud::Redis::V1beta1::CloudRedis.

Configures and manages Cloud Memorystore for Redis instances

Google Cloud Memorystore for Redis v1beta1

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis instances:

  * The service works with a collection of cloud projects, named: `/projects/__`
  * Each project has a collection of available locations, named: `/locations/`
  * Each location has a collection of Redis instances, named: `/instances/*`
  * As such, Redis instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be referring to a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/instances/my-redis`



To load this service and instantiate a REST client:
    
    
    require "google/cloud/redis/v1beta1/cloud_redis/rest"
    client = ::Google::Cloud::Redis::V1beta1::CloudRedis::Rest::Client.new
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
