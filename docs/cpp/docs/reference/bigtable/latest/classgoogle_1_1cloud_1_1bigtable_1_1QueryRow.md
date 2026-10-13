---
url: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow/
title: Class QueryRow (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:29.108190+00:00
---

# Class QueryRow (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class QueryRow (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

A [`QueryRow`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow) is a sequence of columns each with a name and an associated [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value). 

The [`QueryRow`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow) class is a regular value type that may be copied, moved, assigned, compared for equality, etc. Instances may be large if they hold lots of [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value) data, so copy only when necessary.

[`QueryRow`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow) instances are typically returned as the result of queries or reads of a Cloud Bigtable table (see `Client::Read` and [`Client::ExecuteQuery`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Client#classgoogle_1_1cloud_1_1bigtable_1_1Client_1acedbec17139f1988a208ec00925223d7)). Users will mostly just use the accessor methods on [`QueryRow`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow)`, and will rarely (if ever) need to construct a`QueryRow` of their own.

The number of columns in a [`QueryRow`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow) can be obtained from the [`size()`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow#classgoogle_1_1cloud_1_1bigtable_1_1QueryRow_1a6e61291fac956eab4905f1b714359329) member function. The [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value)s can be obtained using the [`values()`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow#classgoogle_1_1cloud_1_1bigtable_1_1QueryRow_1a17f620cfaac8b560b45960bf1d0d4f34) accessor. The names of each column in the row can be obtained using the [`columns()`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1QueryRow#classgoogle_1_1cloud_1_1bigtable_1_1QueryRow_1a67f52efbb424dd2ce222bc54da169258) accessor.

Perhaps the most convenient way to access the `Values` in a row is through the variety of "get" accessors. A user may access a column's [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value) by calling `get` with a `std::size_t` 0-indexed position, or a `std::string` column name. Furthermore, callers may directly extract the native C++ type by specifying the C++ type along with the column's position or name.

###### Example
    
    
    QueryRow row = ...;
    if (StatusOr<std::string> x = row.get<std::string>("LastName")) {
      std::cout << "LastName=" << *x << "\n";
    }
    

## Constructors 

### QueryRow(QueryRow const &)

Copy and move.

**Parameter**  
---  
**Name** | **Description**  
`` |  `QueryRow const &`   
  
  
### QueryRow(QueryRow &&)

Copy and move.

**Parameter**  
---  
**Name** | **Description**  
`` |  `QueryRow &&`   
  
  
### QueryRow()

Default constructs an empty row with no columns nor values. 

## Operators 

### operator=(QueryRow const &)

Copy and move.

**Parameter**  
---  
**Name** | **Description**  
`` |  `QueryRow const &`   
  
**Returns**  
---  
**Type** | **Description**  
`QueryRow &` |   
  
### operator=(QueryRow &&)

Copy and move.

**Parameter**  
---  
**Name** | **Description**  
`` |  `QueryRow &&`   
  
**Returns**  
---  
**Type** | **Description**  
`QueryRow &` |   
  
## Functions 

### size() const

Returns the number of columns in the row. 

**Returns**  
---  
**Type** | **Description**  
`std::size_t` |   
  
### columns() const

Returns the column names for the row. 

**Returns**  
---  
**Type** | **Description**  
`std::vector< std::string > const &` |   
  
### values() const &

Returns the [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value) objects in the given row. 

**Returns**  
---  
**Type** | **Description**  
`std::vector< Value > const &` |   
  
### values() &&

Returns the [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value) objects in the given row. 

**Returns**  
---  
**Type** | **Description**  
`std::vector< Value > &&` |   
  
### get(std::size_t) const

Returns the [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value) at the given `pos`. 

**Parameter**  
---  
**Name** | **Description**  
`pos` |  `std::size_t`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Value >` |   
  
### get(std::string const &) const

Returns the [`Value`](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1Value) in the column with `name`. 

**Parameter**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Value >` |   
  
### get(Arg &&) const

Returns the native C++ value at the given position or column name. 

**Parameters**  
---  
**Name** | **Description**  
`arg` |  `Arg &&`   
  
`typename T` |  ``   
the native C++ type, e.g., std::int64_t or std::string   
`typename Arg` |  ``   
a deduced parameter convertible to a std::size_t or std::string   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< T >` |   
  
### get() const &

Returns all the native C++ values for the whole row in a `std::tuple` with the specified type. 

**Parameter**  
---  
**Name** | **Description**  
`typename Tuple` |  ``   
the `std::tuple` type that the whole row must unpack into.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Tuple >` |   
  
### get() &&

Returns all the native C++ values for the whole row in a `std::tuple` with the specified type. 

**Parameter**  
---  
**Name** | **Description**  
`typename Tuple` |  ``   
the `std::tuple` type that the whole row must unpack into.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< Tuple >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
