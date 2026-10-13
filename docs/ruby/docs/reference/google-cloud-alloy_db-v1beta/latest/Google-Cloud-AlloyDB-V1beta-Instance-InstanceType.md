---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance-InstanceType/
title: AlloyDB V1BETA API - Module Google::Cloud::AlloyDB::V1beta::Instance::InstanceType (v0.25.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:48.608023+00:00
---

# AlloyDB V1BETA API - Module Google::Cloud::AlloyDB::V1beta::Instance::InstanceType (v0.25.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance-InstanceType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1BETA API - Module Google::Cloud::AlloyDB::V1beta::Instance::InstanceType (v0.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.25.0 (latest)  0.24.1  0.23.1  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1BETA API module Google::Cloud::AlloyDB::V1beta::Instance::InstanceType.

Type of an Instance

## Constants 

### INSTANCE_TYPE_UNSPECIFIED

**value:** 0  
The type of the instance is unknown.

### PRIMARY

**value:** 1  
PRIMARY instances support read and write operations.

### READ_POOL

**value:** 2  


READ POOL instances support read operations only. Each read pool instance consists of one or more homogeneous nodes.

  * Read pool of size 1 can only have zonal availability.
  * Read pools with node count of 2 or more can have regional availability (nodes are present in 2 or more zones in a region).



### SECONDARY

**value:** 3  
SECONDARY instances support read operations only. SECONDARY instance is a cross-region read replica

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
