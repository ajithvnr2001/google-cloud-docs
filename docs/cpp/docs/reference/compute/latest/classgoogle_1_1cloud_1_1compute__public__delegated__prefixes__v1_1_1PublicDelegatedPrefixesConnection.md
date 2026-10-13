---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesConnection/
title: Class PublicDelegatedPrefixesConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:23.929276+00:00
---

# Class PublicDelegatedPrefixesConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class PublicDelegatedPrefixesConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

The [`PublicDelegatedPrefixesConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesConnection) object for [`PublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`PublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`PublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesClient).

To create a concrete instance, see `MakePublicDelegatedPrefixesConnection()`.

For mocking, see [`compute_public_delegated_prefixes_v1_mocks::MockPublicDelegatedPrefixesConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1__mocks_1_1MockPublicDelegatedPrefixesConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual AggregatedListPublicDelegatedPrefixes(google::cloud::cpp::compute::public_delegated_prefixes::v1::AggregatedListPublicDelegatedPrefixesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::AggregatedListPublicDelegatedPrefixesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::PublicDelegatedPrefixesScopedList > >` |   
  
### virtual Announce(google::cloud::cpp::compute::public_delegated_prefixes::v1::AnnounceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::AnnounceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual Announce(NoAwaitTag, google::cloud::cpp::compute::public_delegated_prefixes::v1::AnnounceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::AnnounceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual Announce(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeletePublicDelegatedPrefix(google::cloud::cpp::compute::public_delegated_prefixes::v1::DeletePublicDelegatedPrefixRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::DeletePublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeletePublicDelegatedPrefix(NoAwaitTag, google::cloud::cpp::compute::public_delegated_prefixes::v1::DeletePublicDelegatedPrefixRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::DeletePublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual DeletePublicDelegatedPrefix(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual GetPublicDelegatedPrefix(google::cloud::cpp::compute::public_delegated_prefixes::v1::GetPublicDelegatedPrefixRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::GetPublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::PublicDelegatedPrefix >` |   
  
### virtual InsertPublicDelegatedPrefix(google::cloud::cpp::compute::public_delegated_prefixes::v1::InsertPublicDelegatedPrefixRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::InsertPublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual InsertPublicDelegatedPrefix(NoAwaitTag, google::cloud::cpp::compute::public_delegated_prefixes::v1::InsertPublicDelegatedPrefixRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::InsertPublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual InsertPublicDelegatedPrefix(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual ListPublicDelegatedPrefixes(google::cloud::cpp::compute::public_delegated_prefixes::v1::ListPublicDelegatedPrefixesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::ListPublicDelegatedPrefixesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::PublicDelegatedPrefix >` |   
  
### virtual PatchPublicDelegatedPrefix(google::cloud::cpp::compute::public_delegated_prefixes::v1::PatchPublicDelegatedPrefixRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::PatchPublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchPublicDelegatedPrefix(NoAwaitTag, google::cloud::cpp::compute::public_delegated_prefixes::v1::PatchPublicDelegatedPrefixRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::PatchPublicDelegatedPrefixRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchPublicDelegatedPrefix(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual Withdraw(google::cloud::cpp::compute::public_delegated_prefixes::v1::WithdrawRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::WithdrawRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual Withdraw(NoAwaitTag, google::cloud::cpp::compute::public_delegated_prefixes::v1::WithdrawRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::public_delegated_prefixes::v1::WithdrawRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual Withdraw(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
