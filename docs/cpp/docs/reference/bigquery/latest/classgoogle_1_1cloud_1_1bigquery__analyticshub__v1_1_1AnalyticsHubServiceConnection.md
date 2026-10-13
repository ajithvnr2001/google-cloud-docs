---
url: https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1_1_1AnalyticsHubServiceConnection/
title: Class AnalyticsHubServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:16.416309+00:00
---

# Class AnalyticsHubServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1_1_1AnalyticsHubServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AnalyticsHubServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`AnalyticsHubServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1_1_1AnalyticsHubServiceConnection) object for [`AnalyticsHubServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1_1_1AnalyticsHubServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`AnalyticsHubServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1_1_1AnalyticsHubServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`AnalyticsHubServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1_1_1AnalyticsHubServiceClient).

To create a concrete instance, see [`MakeAnalyticsHubServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/namespacegoogle_1_1cloud_1_1bigquery__analyticshub__v1).

For mocking, see [`bigquery_analyticshub_v1_mocks::MockAnalyticsHubServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/bigquery/latest/classgoogle_1_1cloud_1_1bigquery__analyticshub__v1__mocks_1_1MockAnalyticsHubServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListDataExchanges(google::cloud::bigquery::analyticshub::v1::ListDataExchangesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ListDataExchangesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::bigquery::analyticshub::v1::DataExchange >` |   
  
### virtual ListOrgDataExchanges(google::cloud::bigquery::analyticshub::v1::ListOrgDataExchangesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ListOrgDataExchangesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::bigquery::analyticshub::v1::DataExchange >` |   
  
### virtual GetDataExchange(google::cloud::bigquery::analyticshub::v1::GetDataExchangeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::GetDataExchangeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::DataExchange >` |   
  
### virtual CreateDataExchange(google::cloud::bigquery::analyticshub::v1::CreateDataExchangeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::CreateDataExchangeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::DataExchange >` |   
  
### virtual UpdateDataExchange(google::cloud::bigquery::analyticshub::v1::UpdateDataExchangeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::UpdateDataExchangeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::DataExchange >` |   
  
### virtual DeleteDataExchange(google::cloud::bigquery::analyticshub::v1::DeleteDataExchangeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::DeleteDataExchangeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ListListings(google::cloud::bigquery::analyticshub::v1::ListListingsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ListListingsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::bigquery::analyticshub::v1::Listing >` |   
  
### virtual GetListing(google::cloud::bigquery::analyticshub::v1::GetListingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::GetListingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::Listing >` |   
  
### virtual CreateListing(google::cloud::bigquery::analyticshub::v1::CreateListingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::CreateListingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::Listing >` |   
  
### virtual UpdateListing(google::cloud::bigquery::analyticshub::v1::UpdateListingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::UpdateListingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::Listing >` |   
  
### virtual DeleteListing(google::cloud::bigquery::analyticshub::v1::DeleteListingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::DeleteListingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual SubscribeListing(google::cloud::bigquery::analyticshub::v1::SubscribeListingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::SubscribeListingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::SubscribeListingResponse >` |   
  
### virtual SubscribeDataExchange(google::cloud::bigquery::analyticshub::v1::SubscribeDataExchangeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::SubscribeDataExchangeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::bigquery::analyticshub::v1::SubscribeDataExchangeResponse > >` |   
  
### virtual SubscribeDataExchange(NoAwaitTag, google::cloud::bigquery::analyticshub::v1::SubscribeDataExchangeRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::bigquery::analyticshub::v1::SubscribeDataExchangeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual SubscribeDataExchange(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::bigquery::analyticshub::v1::SubscribeDataExchangeResponse > >` |   
  
### virtual RefreshSubscription(google::cloud::bigquery::analyticshub::v1::RefreshSubscriptionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::RefreshSubscriptionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::bigquery::analyticshub::v1::RefreshSubscriptionResponse > >` |   
  
### virtual RefreshSubscription(NoAwaitTag, google::cloud::bigquery::analyticshub::v1::RefreshSubscriptionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::bigquery::analyticshub::v1::RefreshSubscriptionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RefreshSubscription(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::bigquery::analyticshub::v1::RefreshSubscriptionResponse > >` |   
  
### virtual GetSubscription(google::cloud::bigquery::analyticshub::v1::GetSubscriptionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::GetSubscriptionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::Subscription >` |   
  
### virtual ListSubscriptions(google::cloud::bigquery::analyticshub::v1::ListSubscriptionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ListSubscriptionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::bigquery::analyticshub::v1::Subscription >` |   
  
### virtual ListSharedResourceSubscriptions(google::cloud::bigquery::analyticshub::v1::ListSharedResourceSubscriptionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ListSharedResourceSubscriptionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::bigquery::analyticshub::v1::Subscription >` |   
  
### virtual RevokeSubscription(google::cloud::bigquery::analyticshub::v1::RevokeSubscriptionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::RevokeSubscriptionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::RevokeSubscriptionResponse >` |   
  
### virtual DeleteSubscription(google::cloud::bigquery::analyticshub::v1::DeleteSubscriptionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::DeleteSubscriptionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::bigquery::analyticshub::v1::OperationMetadata > >` |   
  
### virtual DeleteSubscription(NoAwaitTag, google::cloud::bigquery::analyticshub::v1::DeleteSubscriptionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::bigquery::analyticshub::v1::DeleteSubscriptionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteSubscription(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::bigquery::analyticshub::v1::OperationMetadata > >` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` |   
  
### virtual CreateQueryTemplate(google::cloud::bigquery::analyticshub::v1::CreateQueryTemplateRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::CreateQueryTemplateRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::QueryTemplate >` |   
  
### virtual GetQueryTemplate(google::cloud::bigquery::analyticshub::v1::GetQueryTemplateRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::GetQueryTemplateRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::QueryTemplate >` |   
  
### virtual ListQueryTemplates(google::cloud::bigquery::analyticshub::v1::ListQueryTemplatesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ListQueryTemplatesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::bigquery::analyticshub::v1::QueryTemplate >` |   
  
### virtual UpdateQueryTemplate(google::cloud::bigquery::analyticshub::v1::UpdateQueryTemplateRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::UpdateQueryTemplateRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::QueryTemplate >` |   
  
### virtual DeleteQueryTemplate(google::cloud::bigquery::analyticshub::v1::DeleteQueryTemplateRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::DeleteQueryTemplateRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual SubmitQueryTemplate(google::cloud::bigquery::analyticshub::v1::SubmitQueryTemplateRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::SubmitQueryTemplateRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::QueryTemplate >` |   
  
### virtual ApproveQueryTemplate(google::cloud::bigquery::analyticshub::v1::ApproveQueryTemplateRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::bigquery::analyticshub::v1::ApproveQueryTemplateRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::bigquery::analyticshub::v1::QueryTemplate >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
