---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-LocationPolicy/
title: Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::LocationPolicy (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:15.748804+00:00
---

# Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::LocationPolicy (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-LocationPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::LocationPolicy (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.2  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.21.0  0.20.1  0.19.2  0.18.3  0.17.4  0.16.2  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.5  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.3  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Batch V1 API class Google::Cloud::Batch::V1::AllocationPolicy::LocationPolicy.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allowed_locations
    
    
    def allowed_locations() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of location names that are allowed for the job's VMs formatted as URLs. Each location can be a region or a zone, but you can only specify one region or multiple zones in one region per job. For example, `["regions/us-central1"]` allow VMs in any zones in region `us-central1`, and `["zones/us-central1-a", "zones/us-central1-c"]` only allow VMs in zones `us-central1-a` and `us-central1-c`. However, `["regions/us-central1", "zones/us-central1-a", "zones/us-central1-b", "zones/us-west1-a"]` causes an error because it contains multiple regions (`us-central1` and `us-west1`).

The specified region or zones must be in the same region in which the job is created starting on the following dates:

    * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.

    * For all other projects, the changes are starting on _July 31, 2026_.

For example, for job `projects/123/locations/us-central1/jobs/jobid`, the specified region or zones must be in `us-central1`. Using a different region (e.g. `regions/us-west1`) or a zone not in `us-central1` (e.g. `zones/us-west1-a`) causes an error. 




### #allowed_locations=
    
    
    def allowed_locations=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of location names that are allowed for the job's VMs formatted as URLs. Each location can be a region or a zone, but you can only specify one region or multiple zones in one region per job. For example, `["regions/us-central1"]` allow VMs in any zones in region `us-central1`, and `["zones/us-central1-a", "zones/us-central1-c"]` only allow VMs in zones `us-central1-a` and `us-central1-c`. However, `["regions/us-central1", "zones/us-central1-a", "zones/us-central1-b", "zones/us-west1-a"]` causes an error because it contains multiple regions (`us-central1` and `us-west1`).

The specified region or zones must be in the same region in which the job is created starting on the following dates:

    * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.

    * For all other projects, the changes are starting on _July 31, 2026_.

For example, for job `projects/123/locations/us-central1/jobs/jobid`, the specified region or zones must be in `us-central1`. Using a different region (e.g. `regions/us-west1`) or a zone not in `us-central1` (e.g. `zones/us-west1-a`) causes an error. 




**Returns**

  * (::Array<::String>) — A list of location names that are allowed for the job's VMs formatted as URLs. Each location can be a region or a zone, but you can only specify one region or multiple zones in one region per job. For example, `["regions/us-central1"]` allow VMs in any zones in region `us-central1`, and `["zones/us-central1-a", "zones/us-central1-c"]` only allow VMs in zones `us-central1-a` and `us-central1-c`. However, `["regions/us-central1", "zones/us-central1-a", "zones/us-central1-b", "zones/us-west1-a"]` causes an error because it contains multiple regions (`us-central1` and `us-west1`).

The specified region or zones must be in the same region in which the job is created starting on the following dates:

    * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, the changes are starting on _June 30, 2027_.

    * For all other projects, the changes are starting on _July 31, 2026_.

For example, for job `projects/123/locations/us-central1/jobs/jobid`, the specified region or zones must be in `us-central1`. Using a different region (e.g. `regions/us-west1`) or a zone not in `us-central1` (e.g. `zones/us-west1-a`) causes an error. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
