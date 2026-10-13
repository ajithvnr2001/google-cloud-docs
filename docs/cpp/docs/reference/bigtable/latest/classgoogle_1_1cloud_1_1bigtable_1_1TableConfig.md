---
url: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1TableConfig/
title: Class TableConfig (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:29.986822+00:00
---

# Class TableConfig (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1TableConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class TableConfig (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Specify the initial schema for a new table. 

## Constructors 

### TableConfig()

### TableConfig(std::map< std::string, GcRule >, std::vector< std::string >)

**Parameters**  
---  
**Name** | **Description**  
`column_families` |  `std::map< std::string, GcRule >`   
  
`initial_splits` |  `std::vector< std::string >`   
  
  
## Functions 

### column_families() const

Return the timestamp granularity parameter. 

Cloud Bigtable currently supports only millisecond granularity in the cell timestamps, both `TIMESTAMP_GRANULARITY_UNSPECIFIED` and `MILLIS` have the same effect. 

**Returns**  
---  
**Type** | **Description**  
`std::map< std::string, GcRule > const &` |   
  
### add_column_family(std::string, GcRule)

Return the timestamp granularity parameter. 

Cloud Bigtable currently supports only millisecond granularity in the cell timestamps, both `TIMESTAMP_GRANULARITY_UNSPECIFIED` and `MILLIS` have the same effect. 

**Parameters**  
---  
**Name** | **Description**  
`column_family_name` |  `std::string`   
  
`gc_rule` |  `GcRule`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initial_splits() const

Return the timestamp granularity parameter. 

Cloud Bigtable currently supports only millisecond granularity in the cell timestamps, both `TIMESTAMP_GRANULARITY_UNSPECIFIED` and `MILLIS` have the same effect. 

**Returns**  
---  
**Type** | **Description**  
`std::vector< std::string > const &` |   
  
### add_initial_split(std::string)

Return the timestamp granularity parameter. 

Cloud Bigtable currently supports only millisecond granularity in the cell timestamps, both `TIMESTAMP_GRANULARITY_UNSPECIFIED` and `MILLIS` have the same effect. 

**Parameter**  
---  
**Name** | **Description**  
`split` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### timestamp_granularity() const

Return the timestamp granularity parameter. 

Cloud Bigtable currently supports only millisecond granularity in the cell timestamps, both `TIMESTAMP_GRANULARITY_UNSPECIFIED` and `MILLIS` have the same effect. 

**Returns**  
---  
**Type** | **Description**  
`TimestampGranularity` |   
  
### set_timestamp_granularity(TimestampGranularity)

Set the timestamp granularity parameter. 

Cloud Bigtable currently supports only millisecond granularity in the cell timestamps, both `TIMESTAMP_GRANULARITY_UNSPECIFIED` and `MILLIS` have the same effect. Creating cells with higher granularity than the supported value is rejected by the server. 

**Parameter**  
---  
**Name** | **Description**  
`new_value` |  `TimestampGranularity`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### as_proto() &&

Move the contents to the proto to create tables. 

**Returns**  
---  
**Type** | **Description**  
`::google::bigtable::admin::v2::CreateTableRequest` |   
  
## Type Aliases 

### TimestampGranularity

**Alias Of** : `::google::bigtable::admin::v2::Table::TimestampGranularity`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
