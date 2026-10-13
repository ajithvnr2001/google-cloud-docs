---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersConnection/
title: Class RoutersConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:55.862128+00:00
---

# Class RoutersConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class RoutersConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

The [`RoutersConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersConnection) object for [`RoutersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`RoutersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`RoutersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersClient).

To create a concrete instance, see `MakeRoutersConnection()`.

For mocking, see [`compute_routers_v1_mocks::MockRoutersConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1__mocks_1_1MockRoutersConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual AggregatedListRouters(google::cloud::cpp::compute::routers::v1::AggregatedListRoutersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::AggregatedListRoutersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::RoutersScopedList > >` |   
  
### virtual DeleteRouter(google::cloud::cpp::compute::routers::v1::DeleteRouterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::DeleteRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteRouter(NoAwaitTag, google::cloud::cpp::compute::routers::v1::DeleteRouterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::DeleteRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual DeleteRouter(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteNamedSet(google::cloud::cpp::compute::routers::v1::DeleteNamedSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::DeleteNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteNamedSet(NoAwaitTag, google::cloud::cpp::compute::routers::v1::DeleteNamedSetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::DeleteNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual DeleteNamedSet(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteRoutePolicy(google::cloud::cpp::compute::routers::v1::DeleteRoutePolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::DeleteRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteRoutePolicy(NoAwaitTag, google::cloud::cpp::compute::routers::v1::DeleteRoutePolicyRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::DeleteRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual DeleteRoutePolicy(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual GetRouter(google::cloud::cpp::compute::routers::v1::GetRouterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::GetRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Router >` |   
  
### virtual GetNamedSet(google::cloud::cpp::compute::routers::v1::GetNamedSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::GetNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RoutersGetNamedSetResponse >` |   
  
### virtual GetNatIpInfo(google::cloud::cpp::compute::routers::v1::GetNatIpInfoRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::GetNatIpInfoRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::NatIpInfoResponse >` |   
  
### virtual GetNatMappingInfo(google::cloud::cpp::compute::routers::v1::GetNatMappingInfoRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::GetNatMappingInfoRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::VmEndpointNatMappingsList >` |   
  
### virtual GetRoutePolicy(google::cloud::cpp::compute::routers::v1::GetRoutePolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::GetRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RoutersGetRoutePolicyResponse >` |   
  
### virtual GetRouterStatus(google::cloud::cpp::compute::routers::v1::GetRouterStatusRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::GetRouterStatusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RouterStatusResponse >` |   
  
### virtual InsertRouter(google::cloud::cpp::compute::routers::v1::InsertRouterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::InsertRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual InsertRouter(NoAwaitTag, google::cloud::cpp::compute::routers::v1::InsertRouterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::InsertRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual InsertRouter(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual ListRouters(google::cloud::cpp::compute::routers::v1::ListRoutersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::ListRoutersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::Router >` |   
  
### virtual ListBgpRoutes(google::cloud::cpp::compute::routers::v1::ListBgpRoutesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::ListBgpRoutesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RoutersListBgpRoutes >` |   
  
### virtual ListNamedSets(google::cloud::cpp::compute::routers::v1::ListNamedSetsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::ListNamedSetsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RoutersListNamedSets >` |   
  
### virtual ListRoutePolicies(google::cloud::cpp::compute::routers::v1::ListRoutePoliciesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::ListRoutePoliciesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RoutersListRoutePolicies >` |   
  
### virtual PatchRouter(google::cloud::cpp::compute::routers::v1::PatchRouterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::PatchRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchRouter(NoAwaitTag, google::cloud::cpp::compute::routers::v1::PatchRouterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::PatchRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchRouter(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchNamedSet(google::cloud::cpp::compute::routers::v1::PatchNamedSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::PatchNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchNamedSet(NoAwaitTag, google::cloud::cpp::compute::routers::v1::PatchNamedSetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::PatchNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchNamedSet(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchRoutePolicy(google::cloud::cpp::compute::routers::v1::PatchRoutePolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::PatchRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchRoutePolicy(NoAwaitTag, google::cloud::cpp::compute::routers::v1::PatchRoutePolicyRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::PatchRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchRoutePolicy(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual Preview(google::cloud::cpp::compute::routers::v1::PreviewRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::PreviewRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::RoutersPreviewResponse >` |   
  
### virtual UpdateRouter(google::cloud::cpp::compute::routers::v1::UpdateRouterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::UpdateRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual UpdateRouter(NoAwaitTag, google::cloud::cpp::compute::routers::v1::UpdateRouterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::UpdateRouterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual UpdateRouter(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual UpdateNamedSet(google::cloud::cpp::compute::routers::v1::UpdateNamedSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::UpdateNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual UpdateNamedSet(NoAwaitTag, google::cloud::cpp::compute::routers::v1::UpdateNamedSetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::UpdateNamedSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual UpdateNamedSet(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual UpdateRoutePolicy(google::cloud::cpp::compute::routers::v1::UpdateRoutePolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::routers::v1::UpdateRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual UpdateRoutePolicy(NoAwaitTag, google::cloud::cpp::compute::routers::v1::UpdateRoutePolicyRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::routers::v1::UpdateRoutePolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual UpdateRoutePolicy(google::cloud::cpp::compute::v1::Operation const &)

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
