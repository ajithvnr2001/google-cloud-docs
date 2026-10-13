---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Asset::DiscoverySpec (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:53.828894+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Asset::DiscoverySpec (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Asset::DiscoverySpec (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::Asset::DiscoverySpec.

Settings to manage the metadata discovery and publishing for an asset.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #csv_options
    
    
    def csv_options() -> ::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::CsvOptions

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::CsvOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec-CsvOptions)) — Optional. Configuration for CSV data. 



### #csv_options=
    
    
    def csv_options=(value) -> ::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::CsvOptions

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::CsvOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec-CsvOptions)) — Optional. Configuration for CSV data. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::CsvOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec-CsvOptions)) — Optional. Configuration for CSV data. 



### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether discovery is enabled. 



### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether discovery is enabled. 



**Returns**

  * (::Boolean) — Optional. Whether discovery is enabled. 



### #exclude_patterns
    
    
    def exclude_patterns() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. 



### #exclude_patterns=
    
    
    def exclude_patterns=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. 



**Returns**

  * (::Array<::String>) — Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. 



### #include_patterns
    
    
    def include_patterns() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. 



### #include_patterns=
    
    
    def include_patterns=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. 



**Returns**

  * (::Array<::String>) — Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. 



### #json_options
    
    
    def json_options() -> ::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::JsonOptions

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::JsonOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec-JsonOptions)) — Optional. Configuration for Json data. 



### #json_options=
    
    
    def json_options=(value) -> ::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::JsonOptions

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::JsonOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec-JsonOptions)) — Optional. Configuration for Json data. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Asset::DiscoverySpec::JsonOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Asset-DiscoverySpec-JsonOptions)) — Optional. Configuration for Json data. 



### #schedule
    
    
    def schedule() -> ::String

**Returns**

  * (::String) — Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes.

To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *`, or `TZ=America/New_York 1 * * * *`. 




### #schedule=
    
    
    def schedule=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes.

To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *`, or `TZ=America/New_York 1 * * * *`. 




**Returns**

  * (::String) — Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes.

To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *`, or `TZ=America/New_York 1 * * * *`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
