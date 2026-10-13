---
url: https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1_1_1ManagedIdentitiesServiceConnection/
title: Class ManagedIdentitiesServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:10.141228+00:00
---

# Class ManagedIdentitiesServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1_1_1ManagedIdentitiesServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ManagedIdentitiesServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`ManagedIdentitiesServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1_1_1ManagedIdentitiesServiceConnection) object for [`ManagedIdentitiesServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1_1_1ManagedIdentitiesServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`ManagedIdentitiesServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1_1_1ManagedIdentitiesServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`ManagedIdentitiesServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1_1_1ManagedIdentitiesServiceClient).

To create a concrete instance, see [`MakeManagedIdentitiesServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/namespacegoogle_1_1cloud_1_1managedidentities__v1).

For mocking, see [`managedidentities_v1_mocks::MockManagedIdentitiesServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/managedidentities/latest/classgoogle_1_1cloud_1_1managedidentities__v1__mocks_1_1MockManagedIdentitiesServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateMicrosoftAdDomain(google::cloud::managedidentities::v1::CreateMicrosoftAdDomainRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::CreateMicrosoftAdDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual CreateMicrosoftAdDomain(NoAwaitTag, google::cloud::managedidentities::v1::CreateMicrosoftAdDomainRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::CreateMicrosoftAdDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateMicrosoftAdDomain(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual ResetAdminPassword(google::cloud::managedidentities::v1::ResetAdminPasswordRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::ResetAdminPasswordRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedidentities::v1::ResetAdminPasswordResponse >` |   
  
### virtual ListDomains(google::cloud::managedidentities::v1::ListDomainsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::ListDomainsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::managedidentities::v1::Domain >` |   
  
### virtual GetDomain(google::cloud::managedidentities::v1::GetDomainRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::GetDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedidentities::v1::Domain >` |   
  
### virtual UpdateDomain(google::cloud::managedidentities::v1::UpdateDomainRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::UpdateDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual UpdateDomain(NoAwaitTag, google::cloud::managedidentities::v1::UpdateDomainRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::UpdateDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateDomain(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual DeleteDomain(google::cloud::managedidentities::v1::DeleteDomainRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::DeleteDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::OpMetadata > >` |   
  
### virtual DeleteDomain(NoAwaitTag, google::cloud::managedidentities::v1::DeleteDomainRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::DeleteDomainRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteDomain(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::OpMetadata > >` |   
  
### virtual AttachTrust(google::cloud::managedidentities::v1::AttachTrustRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::AttachTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual AttachTrust(NoAwaitTag, google::cloud::managedidentities::v1::AttachTrustRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::AttachTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual AttachTrust(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual ReconfigureTrust(google::cloud::managedidentities::v1::ReconfigureTrustRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::ReconfigureTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual ReconfigureTrust(NoAwaitTag, google::cloud::managedidentities::v1::ReconfigureTrustRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::ReconfigureTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ReconfigureTrust(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual DetachTrust(google::cloud::managedidentities::v1::DetachTrustRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::DetachTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual DetachTrust(NoAwaitTag, google::cloud::managedidentities::v1::DetachTrustRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::DetachTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DetachTrust(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual ValidateTrust(google::cloud::managedidentities::v1::ValidateTrustRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedidentities::v1::ValidateTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
### virtual ValidateTrust(NoAwaitTag, google::cloud::managedidentities::v1::ValidateTrustRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::managedidentities::v1::ValidateTrustRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ValidateTrust(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::managedidentities::v1::Domain > >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
