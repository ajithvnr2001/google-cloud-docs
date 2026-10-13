---
url: https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange/
title: Class StreamRange<T> (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:19:48.699309+00:00
---

# Class StreamRange<T> (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class StreamRange<T> (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0  2.10.1 

A [`StreamRange`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange)`<T>` is a range of [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr)`<T>` where the end-of-stream is indicated by a non-OK [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status). 

Callers can iterate the range using its [`begin()`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange#classgoogle_1_1cloud_1_1StreamRange_1a0e71520c598a1649ddd54cca5a0336f8) and [`end()`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange#classgoogle_1_1cloud_1_1StreamRange_1aab2620724dbe9f681e66544cbe6d37d1) members to access iterators that will work with any normal C++ constructs and algorithms that accept [Input Iterators](https://en.cppreference.com/w/cpp/named_req/InputIterator).

Callers should only consume/iterate this range.

###### Example: Iterating a range of 10 integers
    
    
    // Some function that returns a StreamRange<int>
    StreamRange<int> MakeRangeFromOneTo(int n);
    
    StreamRange<int> sr = MakeRangeFromOneTo(10);
    for (StatusOr<int> const& x : sr) {
      if (!x) {
        std::cerr << "Fail: " << x.status() << "\n";
      } else {
        std::cout << *x << "\n";
      }
    }
    

**Note:** To construct a [`StreamRange`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange)`<T>` for testing (e.g. to mock a `Connection::ListFoo` call), see [`google::cloud::mocks::MakeStreamRange`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1_1mocks). 

## Constructors 

### StreamRange(StreamRange const &)

Move-only

**Parameter**  
---  
**Name** | **Description**  
`` |  `StreamRange const &`   
  
  
### StreamRange(StreamRange &&)

Move-only

**Parameter**  
---  
**Name** | **Description**  
`` |  `StreamRange &&`   
  
  
### StreamRange()

Default-constructs an empty range. 

## Operators 

### operator=(StreamRange const &)

Move-only

**Parameter**  
---  
**Name** | **Description**  
`` |  `StreamRange const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange &` |   
  
### operator=(StreamRange &&)

Move-only

**Parameter**  
---  
**Name** | **Description**  
`` |  `StreamRange &&`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange &` |   
  
## Functions 

### begin()

**Returns**  
---  
**Type** | **Description**  
`iterator` |   
  
### end()

**Returns**  
---  
**Type** | **Description**  
`iterator` |   
  
## Type Aliases 

### value_type

**Alias Of** : `StatusOr< T >`

### iterator

**Alias Of** : `IteratorImpl< value_type >`

### difference_type

**Alias Of** : `typename iterator::difference_type`

### reference

**Alias Of** : `typename iterator::reference`

### pointer

**Alias Of** : `typename iterator::pointer`

### const_reference

**Alias Of** : `typename iterator::const_reference`

### const_pointer

**Alias Of** : `typename iterator::const_pointer`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
