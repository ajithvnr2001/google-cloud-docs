---
url: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database/
title: Class Database (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:13.550626+00:00
---

# Class Database (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class Database (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

This class identifies a Cloud Spanner [Database](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database). 

A Cloud Spanner database is identified by its `project_id`, `instance_id`, and `database_id`.

**Note:** This class makes no effort to validate the components of the database name. It is the application's responsibility to provide valid project, instance, and database ids. Passing invalid values will not be checked until the database name is used in a RPC to spanner.  For more info about the `database_id` format, see <https://cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateDatabaseRequest>

## Constructors 

### Database(Database const &)

Copy and move

**Parameter**  
---  
**Name** | **Description**  
`` |  `Database const &`   
  
  
### Database(Database &&)

Copy and move

**Parameter**  
---  
**Name** | **Description**  
`` |  `Database &&`   
  
  
### Database(Instance, std::string)

Constructs a [Database](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database) object identified by the given `instance` and `database_id`. 

**Parameters**  
---  
**Name** | **Description**  
`instance` |  `Instance`   
  
`database_id` |  `std::string`   
  
  
### Database(std::string, std::string, std::string)

Constructs a [Database](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database) object identified by the given IDs. 

This is equivalent to first constructing an [`Instance`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Instance) from the given `project_id` and `instance_id` arguments and then calling the [`Database(Instance, std::string)`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database#classgoogle_1_1cloud_1_1spanner_1_1Database_1a5b2239e1f2fb2210272f05580a2f7e8c) constructor. 

**Parameters**  
---  
**Name** | **Description**  
`project_id` |  `std::string`   
  
`instance_id` |  `std::string`   
  
`database_id` |  `std::string`   
  
  
## Operators 

### operator=(Database const &)

Copy and move

**Parameter**  
---  
**Name** | **Description**  
`` |  `Database const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Database &` |   
  
### operator=(Database &&)

Copy and move

**Parameter**  
---  
**Name** | **Description**  
`` |  `Database &&`   
  
**Returns**  
---  
**Type** | **Description**  
`Database &` |   
  
## Functions 

### instance() const

Returns the [`Instance`](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Instance) containing this database. 

**Returns**  
---  
**Type** | **Description**  
`Instance const &` |   
  
### database_id() const

Returns the [Database](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest/classgoogle_1_1cloud_1_1spanner_1_1Database) ID. 

**Returns**  
---  
**Type** | **Description**  
`std::string const &` |   
  
### FullName() const

Returns the fully qualified database name as a string of the form: "projects/

**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
