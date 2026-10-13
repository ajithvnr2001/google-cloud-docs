---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceGrpc.AsyncService
title: Interface AnalyticsHubServiceGrpc.AsyncService (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:21.119238+00:00
---

# Interface AnalyticsHubServiceGrpc.AsyncService (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnalyticsHubServiceGrpc.AsyncService (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface AnalyticsHubServiceGrpc.AsyncService

The `AnalyticsHubService` API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

## Methods 

### approveQueryTemplate(ApproveQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)
    
    
    public default void approveQueryTemplate(ApproveQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)

Approves a query template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ApproveQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ApproveQueryTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>`  
  
  
### createDataExchange(CreateDataExchangeRequest request, StreamObserver<DataExchange> responseObserver)
    
    
    public default void createDataExchange(CreateDataExchangeRequest request, StreamObserver<DataExchange> responseObserver)

Creates a new data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateDataExchangeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>`  
  
  
### createListing(CreateListingRequest request, StreamObserver<Listing> responseObserver)
    
    
    public default void createListing(CreateListingRequest request, StreamObserver<Listing> responseObserver)

Creates a new listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateListingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>`  
  
  
### createQueryTemplate(CreateQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)
    
    
    public default void createQueryTemplate(CreateQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)

Creates a new QueryTemplate

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateQueryTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>`  
  
  
### deleteDataExchange(DeleteDataExchangeRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteDataExchange(DeleteDataExchangeRequest request, StreamObserver<Empty> responseObserver)

Deletes an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteDataExchangeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteListing(DeleteListingRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteListing(DeleteListingRequest request, StreamObserver<Empty> responseObserver)

Deletes a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteListingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteQueryTemplate(DeleteQueryTemplateRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteQueryTemplate(DeleteQueryTemplateRequest request, StreamObserver<Empty> responseObserver)

Deletes a query template.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteQueryTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteSubscription(DeleteSubscriptionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSubscription(DeleteSubscriptionRequest request, StreamObserver<Operation> responseObserver)

Deletes a subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getDataExchange(GetDataExchangeRequest request, StreamObserver<DataExchange> responseObserver)
    
    
    public default void getDataExchange(GetDataExchangeRequest request, StreamObserver<DataExchange> responseObserver)

Gets the details of a data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetDataExchangeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>`  
  
  
### getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void getIamPolicy(GetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Gets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### getListing(GetListingRequest request, StreamObserver<Listing> responseObserver)
    
    
    public default void getListing(GetListingRequest request, StreamObserver<Listing> responseObserver)

Gets the details of a listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetListingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>`  
  
  
### getQueryTemplate(GetQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)
    
    
    public default void getQueryTemplate(GetQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)

Gets a QueryTemplate

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetQueryTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>`  
  
  
### getSubscription(GetSubscriptionRequest request, StreamObserver<Subscription> responseObserver)
    
    
    public default void getSubscription(GetSubscriptionRequest request, StreamObserver<Subscription> responseObserver)

Gets the details of a Subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Subscription)>`  
  
  
### listDataExchanges(ListDataExchangesRequest request, StreamObserver<ListDataExchangesResponse> responseObserver)
    
    
    public default void listDataExchanges(ListDataExchangesRequest request, StreamObserver<ListDataExchangesResponse> responseObserver)

Lists all data exchanges in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDataExchangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesResponse)>`  
  
  
### listListings(ListListingsRequest request, StreamObserver<ListListingsResponse> responseObserver)
    
    
    public default void listListings(ListListingsRequest request, StreamObserver<ListListingsResponse> responseObserver)

Lists all listings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListListingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListListingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsResponse)>`  
  
  
### listOrgDataExchanges(ListOrgDataExchangesRequest request, StreamObserver<ListOrgDataExchangesResponse> responseObserver)
    
    
    public default void listOrgDataExchanges(ListOrgDataExchangesRequest request, StreamObserver<ListOrgDataExchangesResponse> responseObserver)

Lists all data exchanges from projects in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOrgDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOrgDataExchangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesResponse)>`  
  
  
### listQueryTemplates(ListQueryTemplatesRequest request, StreamObserver<ListQueryTemplatesResponse> responseObserver)
    
    
    public default void listQueryTemplates(ListQueryTemplatesRequest request, StreamObserver<ListQueryTemplatesResponse> responseObserver)

Lists all QueryTemplates in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQueryTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListQueryTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesResponse)>`  
  
  
### listSharedResourceSubscriptions(ListSharedResourceSubscriptionsRequest request, StreamObserver<ListSharedResourceSubscriptionsResponse> responseObserver)
    
    
    public default void listSharedResourceSubscriptions(ListSharedResourceSubscriptionsRequest request, StreamObserver<ListSharedResourceSubscriptionsResponse> responseObserver)

Lists all subscriptions on a given Data Exchange or Listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSharedResourceSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsResponse)>`  
  
  
### listSubscriptions(ListSubscriptionsRequest request, StreamObserver<ListSubscriptionsResponse> responseObserver)
    
    
    public default void listSubscriptions(ListSubscriptionsRequest request, StreamObserver<ListSubscriptionsResponse> responseObserver)

Lists all subscriptions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsResponse)>`  
  
  
### refreshSubscription(RefreshSubscriptionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void refreshSubscription(RefreshSubscriptionRequest request, StreamObserver<Operation> responseObserver)

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RefreshSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### revokeSubscription(RevokeSubscriptionRequest request, StreamObserver<RevokeSubscriptionResponse> responseObserver)
    
    
    public default void revokeSubscription(RevokeSubscriptionRequest request, StreamObserver<RevokeSubscriptionResponse> responseObserver)

Revokes a given subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RevokeSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RevokeSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse)>`  
  
  
### setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)
    
    
    public default void setIamPolicy(SetIamPolicyRequest request, StreamObserver<Policy> responseObserver)

Sets the IAM policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.Policy>`  
  
  
### submitQueryTemplate(SubmitQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)
    
    
    public default void submitQueryTemplate(SubmitQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)

Submits a query template for approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubmitQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubmitQueryTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>`  
  
  
### subscribeDataExchange(SubscribeDataExchangeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void subscribeDataExchange(SubscribeDataExchangeRequest request, StreamObserver<Operation> responseObserver)

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubscribeDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### subscribeListing(SubscribeListingRequest request, StreamObserver<SubscribeListingResponse> responseObserver)
    
    
    public default void subscribeListing(SubscribeListingRequest request, StreamObserver<SubscribeListingResponse> responseObserver)

Subscribes to a listing. Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SubscribeListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SubscribeListingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse)>`  
  
  
### testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)
    
    
    public default void testIamPermissions(TestIamPermissionsRequest request, StreamObserver<TestIamPermissionsResponse> responseObserver)

Returns the permissions that a caller has.

**Parameters**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<com.google.iam.v1.TestIamPermissionsResponse>`  
  
  
### updateDataExchange(UpdateDataExchangeRequest request, StreamObserver<DataExchange> responseObserver)
    
    
    public default void updateDataExchange(UpdateDataExchangeRequest request, StreamObserver<DataExchange> responseObserver)

Updates an existing data exchange.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateDataExchangeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>`  
  
  
### updateListing(UpdateListingRequest request, StreamObserver<Listing> responseObserver)
    
    
    public default void updateListing(UpdateListingRequest request, StreamObserver<Listing> responseObserver)

Updates an existing listing.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateListingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>`  
  
  
### updateQueryTemplate(UpdateQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)
    
    
    public default void updateQueryTemplate(UpdateQueryTemplateRequest request, StreamObserver<QueryTemplate> responseObserver)

Updates an existing QueryTemplate

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateQueryTemplateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
