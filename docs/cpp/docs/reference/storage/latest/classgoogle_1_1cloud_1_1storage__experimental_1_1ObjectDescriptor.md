---
url: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1ObjectDescriptor/
title: Class ObjectDescriptor (2.47.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:56.638992+00:00
---

# Class ObjectDescriptor (2.47.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1ObjectDescriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ObjectDescriptor (2.47.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

[`ObjectDescriptor`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1ObjectDescriptor) is analogous to a file descriptor. 

Applications use an [`ObjectDescriptor`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage__experimental_1_1ObjectDescriptor) to perform multiple reads on the same Google Cloud Storage object. 

## Constructors 

### ObjectDescriptor(ObjectDescriptor &&)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `ObjectDescriptor &&`   
  
  
### ObjectDescriptor(ObjectDescriptor const &)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `ObjectDescriptor const &`   
  
  
### ObjectDescriptor()

Creates an uninitialized descriptor. 

It is UB (undefined behavior) to use any functions on this descriptor. 

### ObjectDescriptor(std::shared_ptr< ObjectDescriptorConnection >)

Initialize a descriptor from its implementation class. 

**Parameter**  
---  
**Name** | **Description**  
`impl` |  `std::shared_ptr< ObjectDescriptorConnection >`   
  
  
## Operators 

### operator=(ObjectDescriptor &&)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `ObjectDescriptor &&`   
  
**Returns**  
---  
**Type** | **Description**  
`ObjectDescriptor &` |   
  
### operator=(ObjectDescriptor const &)

Move-only.

**Parameter**  
---  
**Name** | **Description**  
`` |  `ObjectDescriptor const &`   
  
**Returns**  
---  
**Type** | **Description**  
`ObjectDescriptor &` |   
  
## Functions 

### metadata() const

Returns, if available, the object metadata associated with this descriptor. 

**Returns**  
---  
**Type** | **Description**  
`absl::optional< google::storage::v2::Object >` |   
  
### Read(std::int64_t, std::int64_t)

Starts a new range read in the current descriptor. 

**Parameters**  
---  
**Name** | **Description**  
`offset` |  `std::int64_t`   
  
`limit` |  `std::int64_t`   
  
**Returns**  
---  
**Type** | **Description**  
`std::pair< AsyncReader, AsyncToken >` |   
  
### ReadFromOffset(std::int64_t)

Starts a new read beginning at the supplied offset and continuing until the end. 

**Parameter**  
---  
**Name** | **Description**  
`offset` |  `std::int64_t`   
  
**Returns**  
---  
**Type** | **Description**  
`std::pair< AsyncReader, AsyncToken >` |   
  
### ReadLast(std::int64_t)

Reads the last number of bytes from the end. 

**Parameter**  
---  
**Name** | **Description**  
`limit` |  `std::int64_t`   
  
**Returns**  
---  
**Type** | **Description**  
`std::pair< AsyncReader, AsyncToken >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
