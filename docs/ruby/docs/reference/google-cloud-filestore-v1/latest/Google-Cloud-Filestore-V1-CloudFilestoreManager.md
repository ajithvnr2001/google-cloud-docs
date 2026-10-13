---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-filestore-v1/latest/Google-Cloud-Filestore-V1-CloudFilestoreManager/
title: Filestore V1 API - Module Google::Cloud::Filestore::V1::CloudFilestoreManager (v2.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:26.886644+00:00
---

# Filestore V1 API - Module Google::Cloud::Filestore::V1::CloudFilestoreManager (v2.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-filestore-v1/latest/Google-Cloud-Filestore-V1-CloudFilestoreManager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Filestore V1 API - Module Google::Cloud::Filestore::V1::CloudFilestoreManager (v2.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.1 (latest)  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.1  2.0.0  1.2.0  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Filestore V1 API module Google::Cloud::Filestore::V1::CloudFilestoreManager.

Configures and manages Filestore resources.

Filestore Manager v1.

The `file.googleapis.com` service implements the Filestore API and defines the following resource model for managing instances:

  * The service works with a collection of cloud projects, named: `/projects/__`
  * Each project has a collection of available locations, named: `/locations/`
  * Each location has a collection of instances and backups, named: `/instances/__`and`/backups/` respectively.
  * As such, Filestore instances are resources of the form: `/projects/{project_number}/locations/{location_id}/instances/{instance_id}` and backups are resources of the form: `/projects/{project_number}/locations/{location_id}/backup/{backup_id}`



Note that location_id must be a Google Cloud `zone` for instances, but a Google Cloud `region` for backups; for example:

  * `projects/12345/locations/us-central1-c/instances/my-filestore`
  * `projects/12345/locations/us-central1/backups/my-backup`



To load this service and instantiate a REST client:
    
    
    require "google/cloud/filestore/v1/cloud_filestore_manager/rest"
    client = ::Google::Cloud::Filestore::V1::CloudFilestoreManager::Rest::Client.new
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
