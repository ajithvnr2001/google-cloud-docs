---
url: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1RowRange/
title: Class RowRange (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:14.445607+00:00
---

# Class RowRange (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1RowRange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class RowRange (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Define the interfaces to create row key ranges. 

Example: 
    
    
    // Create a range for the keys starting with the given prefix.
    auto range = bigtable::RowRange::StartingAt("foo/");
    

## Constructors 

### RowRange(::google::bigtable::v2::RowRange)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `::google::bigtable::v2::RowRange`   
  
  
### RowRange(RowRange &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `RowRange &&`   
  
  
### RowRange(RowRange const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `RowRange const &`   
  
  
## Operators 

### operator=(RowRange &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `RowRange &&`   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange &` |   
  
### operator=(RowRange const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `RowRange const &`   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange &` |   
  
## Functions 

### static RightOpen(T &&, U &&)

Return a range representing the interval (`begin`, `end`]. 

Return a range representing the interval [`begin`, `end`). 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `T &&`   
  
`end` |  `U &&`   
  
`typename T` |  ``   
  
`typename U` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static LeftOpen(T &&, U &&)

Return a range representing the interval (`begin`, `end`]. 

Return a range representing the interval [`begin`, `end`). 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `T &&`   
  
`end` |  `U &&`   
  
`typename T` |  ``   
  
`typename U` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static Open(T &&, U &&)

Return a range representing the interval (`begin`, `end`). 

Return a range representing the interval [`begin`, `end`). 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `T &&`   
  
`end` |  `U &&`   
  
`typename T` |  ``   
  
`typename U` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static Closed(T &&, U &&)

Return a range representing the interval [`begin`, `end`]. 

Return a range representing the interval [`begin`, `end`). 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `T &&`   
  
`end` |  `U &&`   
  
`typename T` |  ``   
  
`typename U` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### IsEmpty() const

Return true if the range is empty. 

Note that some ranges (such as `["", ""]`) are not empty but only include invalid row keys. 

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### Contains(T const &) const

Return true if `key` is in the range. 

**Parameters**  
---  
**Name** | **Description**  
`key` |  `T const &`   
  
`typename T` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### Intersect(RowRange const &) const

Compute the intersection against another [RowRange](https://docs.cloud.google.com/cpp/docs/reference/bigtable/latest/classgoogle_1_1cloud_1_1bigtable_1_1RowRange). 

**Parameter**  
---  
**Name** | **Description**  
`range` |  `RowRange const &`   
  
**Returns**  
---  
**Type** | **Description**  
`std::pair< bool, RowRange >` | a 2-tuple, the first element is a boolean, with value `true` if there is some intersection, the second element is the intersection. If there is no intersection the first element is `false` and the second element has a valid, but unspecified value.   
  
### as_proto() const &

Return the filter expression as a protobuf. 

**Returns**  
---  
**Type** | **Description**  
`::google::bigtable::v2::RowRange const &` |   
  
### as_proto() &&

Move out the underlying protobuf value. 

**Returns**  
---  
**Type** | **Description**  
`::google::bigtable::v2::RowRange &&` |   
  
### static InfiniteRange()

Return the infinite range, i.e., a range including all possible keys. 

**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static StartingAt(T &&)

Return the range starting at `begin` (included), with no upper limit. 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `T &&`   
  
`typename T` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static EndingAt(T &&)

Return the range ending at `end` (included), with no lower limit. 

**Parameters**  
---  
**Name** | **Description**  
`end` |  `T &&`   
  
`typename T` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static Empty()

Return an empty range. 

**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static Range(T &&, U &&)

Return the range representing the interval [`begin`, `end`). 

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `T &&`   
  
`end` |  `U &&`   
  
`typename T` |  ``   
  
`typename U` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
### static Prefix(T &&)

Return a range that contains all the keys starting with `prefix`. 

**Parameters**  
---  
**Name** | **Description**  
`prefix` |  `T &&`   
  
`typename T` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`RowRange` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
