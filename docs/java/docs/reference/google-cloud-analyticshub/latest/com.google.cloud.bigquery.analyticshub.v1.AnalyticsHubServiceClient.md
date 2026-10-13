---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient
title: Class AnalyticsHubServiceClient (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:40.223748+00:00
---

# Class AnalyticsHubServiceClient (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AnalyticsHubServiceClient (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-analyticshub/google-cloud-analyticshub/src/main/java/com/google/cloud/bigquery/analyticshub/v1/AnalyticsHubServiceClient.java)| [Product Reference](https://cloud.google.com/bigquery/TBD)  
---|---  
  
Service Description: The `AnalyticsHubService` API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       DataExchange response = analyticsHubServiceClient.getDataExchange(name);
     }
     

Note: close() needs to be called on the AnalyticsHubServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListDataExchanges |  Lists all data exchanges in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataExchanges(ListDataExchangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataExchanges(LocationName parent) 
  * listDataExchanges(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataExchangesPagedCallable() 
  * listDataExchangesCallable() 

  
ListOrgDataExchanges |  Lists all data exchanges from projects in a given organization and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOrgDataExchanges(ListOrgDataExchangesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOrgDataExchanges(String organization) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOrgDataExchangesPagedCallable() 
  * listOrgDataExchangesCallable() 

  
GetDataExchange |  Gets the details of a data exchange. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataExchange(GetDataExchangeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataExchange(DataExchangeName name) 
  * getDataExchange(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataExchangeCallable() 

  
CreateDataExchange |  Creates a new data exchange. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataExchange(CreateDataExchangeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDataExchange(LocationName parent, DataExchange dataExchange) 
  * createDataExchange(String parent, DataExchange dataExchange) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataExchangeCallable() 

  
UpdateDataExchange |  Updates an existing data exchange. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataExchange(UpdateDataExchangeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDataExchange(DataExchange dataExchange, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataExchangeCallable() 

  
DeleteDataExchange |  Deletes an existing data exchange. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataExchange(DeleteDataExchangeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDataExchange(DataExchangeName name) 
  * deleteDataExchange(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataExchangeCallable() 

  
ListListings |  Lists all listings in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listListings(ListListingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listListings(DataExchangeName parent) 
  * listListings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listListingsPagedCallable() 
  * listListingsCallable() 

  
GetListing |  Gets the details of a listing. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getListing(GetListingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getListing(ListingName name) 
  * getListing(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getListingCallable() 

  
CreateListing |  Creates a new listing. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createListing(CreateListingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createListing(DataExchangeName parent, Listing listing) 
  * createListing(String parent, Listing listing) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createListingCallable() 

  
UpdateListing |  Updates an existing listing. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateListing(UpdateListingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateListing(Listing listing, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateListingCallable() 

  
DeleteListing |  Deletes a listing. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteListing(DeleteListingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteListing(ListingName name) 
  * deleteListing(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteListingCallable() 

  
SubscribeListing |  Subscribes to a listing.  Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * subscribeListing(SubscribeListingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * subscribeListing(ListingName name) 
  * subscribeListing(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * subscribeListingCallable() 

  
SubscribeDataExchange |  Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * subscribeDataExchangeAsync(SubscribeDataExchangeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * subscribeDataExchangeAsync(DataExchangeName name) 
  * subscribeDataExchangeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * subscribeDataExchangeOperationCallable() 
  * subscribeDataExchangeCallable() 

  
RefreshSubscription |  Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * refreshSubscriptionAsync(RefreshSubscriptionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * refreshSubscriptionAsync(SubscriptionName name) 
  * refreshSubscriptionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * refreshSubscriptionOperationCallable() 
  * refreshSubscriptionCallable() 

  
GetSubscription |  Gets the details of a Subscription. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSubscription(GetSubscriptionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSubscription(SubscriptionName name) 
  * getSubscription(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSubscriptionCallable() 

  
ListSubscriptions |  Lists all subscriptions in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSubscriptions(ListSubscriptionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSubscriptions(LocationName parent) 
  * listSubscriptions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSubscriptionsPagedCallable() 
  * listSubscriptionsCallable() 

  
ListSharedResourceSubscriptions |  Lists all subscriptions on a given Data Exchange or Listing. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSharedResourceSubscriptions(ListSharedResourceSubscriptionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSharedResourceSubscriptions(ResourceName resource) 
  * listSharedResourceSubscriptions(String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSharedResourceSubscriptionsPagedCallable() 
  * listSharedResourceSubscriptionsCallable() 

  
RevokeSubscription |  Revokes a given subscription. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * revokeSubscription(RevokeSubscriptionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * revokeSubscription(SubscriptionName name) 
  * revokeSubscription(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * revokeSubscriptionCallable() 

  
DeleteSubscription |  Deletes a subscription. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSubscriptionAsync(DeleteSubscriptionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSubscriptionAsync(SubscriptionName name) 
  * deleteSubscriptionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSubscriptionOperationCallable() 
  * deleteSubscriptionCallable() 

  
GetIamPolicy |  Gets the IAM policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
SetIamPolicy |  Sets the IAM policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns the permissions that a caller has. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
CreateQueryTemplate |  Creates a new QueryTemplate |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createQueryTemplate(CreateQueryTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createQueryTemplate(DataExchangeName parent, QueryTemplate queryTemplate, String queryTemplateId) 
  * createQueryTemplate(String parent, QueryTemplate queryTemplate, String queryTemplateId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createQueryTemplateCallable() 

  
GetQueryTemplate |  Gets a QueryTemplate |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getQueryTemplate(GetQueryTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getQueryTemplate(QueryTemplateName name) 
  * getQueryTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getQueryTemplateCallable() 

  
ListQueryTemplates |  Lists all QueryTemplates in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listQueryTemplates(ListQueryTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listQueryTemplates(DataExchangeName parent) 
  * listQueryTemplates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listQueryTemplatesPagedCallable() 
  * listQueryTemplatesCallable() 

  
UpdateQueryTemplate |  Updates an existing QueryTemplate |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateQueryTemplate(UpdateQueryTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateQueryTemplate(QueryTemplate queryTemplate, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateQueryTemplateCallable() 

  
DeleteQueryTemplate |  Deletes a query template. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteQueryTemplate(DeleteQueryTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteQueryTemplate(QueryTemplateName name) 
  * deleteQueryTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteQueryTemplateCallable() 

  
SubmitQueryTemplate |  Submits a query template for approval. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * submitQueryTemplate(SubmitQueryTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * submitQueryTemplate(QueryTemplateName name) 
  * submitQueryTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * submitQueryTemplateCallable() 

  
ApproveQueryTemplate |  Approves a query template. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * approveQueryTemplate(ApproveQueryTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * approveQueryTemplate(QueryTemplateName name) 
  * approveQueryTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * approveQueryTemplateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AnalyticsHubServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AnalyticsHubServiceSettings analyticsHubServiceSettings =
         AnalyticsHubServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AnalyticsHubServiceClient analyticsHubServiceClient =
         AnalyticsHubServiceClient.create(analyticsHubServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AnalyticsHubServiceSettings analyticsHubServiceSettings =
         AnalyticsHubServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AnalyticsHubServiceClient analyticsHubServiceClient =
         AnalyticsHubServiceClient.create(analyticsHubServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AnalyticsHubServiceSettings analyticsHubServiceSettings =
         AnalyticsHubServiceSettings.newHttpJsonBuilder().build();
     AnalyticsHubServiceClient analyticsHubServiceClient =
         AnalyticsHubServiceClient.create(analyticsHubServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AnalyticsHubServiceClient

## Static Methods 

### create()
    
    
    public static final AnalyticsHubServiceClient create()

Constructs an instance of AnalyticsHubServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AnalyticsHubServiceSettings settings)
    
    
    public static final AnalyticsHubServiceClient create(AnalyticsHubServiceSettings settings)

Constructs an instance of AnalyticsHubServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AnalyticsHubServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AnalyticsHubServiceStub stub)
    
    
    public static final AnalyticsHubServiceClient create(AnalyticsHubServiceStub stub)

Constructs an instance of AnalyticsHubServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AnalyticsHubServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AnalyticsHubServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.stub.AnalyticsHubServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient)` |   
  
## Constructors 

### AnalyticsHubServiceClient(AnalyticsHubServiceSettings settings)
    
    
    protected AnalyticsHubServiceClient(AnalyticsHubServiceSettings settings)

Constructs an instance of AnalyticsHubServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AnalyticsHubServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings)`  
  
  
### AnalyticsHubServiceClient(AnalyticsHubServiceStub stub)
    
    
    protected AnalyticsHubServiceClient(AnalyticsHubServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AnalyticsHubServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.stub.AnalyticsHubServiceStub)`  
  
  
## Methods 

### approveQueryTemplate(@Nullable QueryTemplateName name)
    
    
    public final QueryTemplate approveQueryTemplate(@Nullable QueryTemplateName name)

Approves a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       QueryTemplateName name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]");
       QueryTemplate response = analyticsHubServiceClient.approveQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.QueryTemplateName`  
Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### approveQueryTemplate(ApproveQueryTemplateRequest request)
    
    
    public final QueryTemplate approveQueryTemplate(ApproveQueryTemplateRequest request)

Approves a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ApproveQueryTemplateRequest request =
           ApproveQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       QueryTemplate response = analyticsHubServiceClient.approveQueryTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ApproveQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ApproveQueryTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### approveQueryTemplate(String name)
    
    
    public final QueryTemplate approveQueryTemplate(String name)

Approves a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
               .toString();
       QueryTemplate response = analyticsHubServiceClient.approveQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### approveQueryTemplateCallable()
    
    
    public final UnaryCallable<ApproveQueryTemplateRequest,QueryTemplate> approveQueryTemplateCallable()

Approves a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ApproveQueryTemplateRequest request =
           ApproveQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       ApiFuture<QueryTemplate> future =
           analyticsHubServiceClient.approveQueryTemplateCallable().futureCall(request);
       // Do something.
       QueryTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApproveQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ApproveQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createDataExchange(@Nullable LocationName parent, DataExchange dataExchange)
    
    
    public final DataExchange createDataExchange(@Nullable LocationName parent, DataExchange dataExchange)

Creates a new data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DataExchange dataExchange = DataExchange.newBuilder().build();
       DataExchange response = analyticsHubServiceClient.createDataExchange(parent, dataExchange);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.LocationName`  
Required. The parent resource path of the data exchange. e.g. `projects/myproject/locations/us`.  
`dataExchange` | `[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)`  
Required. The data exchange to create.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### createDataExchange(CreateDataExchangeRequest request)
    
    
    public final DataExchange createDataExchange(CreateDataExchangeRequest request)

Creates a new data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       CreateDataExchangeRequest request =
           CreateDataExchangeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataExchangeId("dataExchangeId783243752")
               .setDataExchange(DataExchange.newBuilder().build())
               .build();
       DataExchange response = analyticsHubServiceClient.createDataExchange(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateDataExchangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### createDataExchange(String parent, DataExchange dataExchange)
    
    
    public final DataExchange createDataExchange(String parent, DataExchange dataExchange)

Creates a new data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DataExchange dataExchange = DataExchange.newBuilder().build();
       DataExchange response = analyticsHubServiceClient.createDataExchange(parent, dataExchange);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the data exchange. e.g. `projects/myproject/locations/us`.  
`dataExchange` | `[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)`  
Required. The data exchange to create.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### createDataExchangeCallable()
    
    
    public final UnaryCallable<CreateDataExchangeRequest,DataExchange> createDataExchangeCallable()

Creates a new data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       CreateDataExchangeRequest request =
           CreateDataExchangeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataExchangeId("dataExchangeId783243752")
               .setDataExchange(DataExchange.newBuilder().build())
               .build();
       ApiFuture<DataExchange> future =
           analyticsHubServiceClient.createDataExchangeCallable().futureCall(request);
       // Do something.
       DataExchange response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateDataExchangeRequest),[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>` |   
  
### createListing(@Nullable DataExchangeName parent, Listing listing)
    
    
    public final Listing createListing(@Nullable DataExchangeName parent, Listing listing)

Creates a new listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       Listing listing = Listing.newBuilder().build();
       Listing response = analyticsHubServiceClient.createListing(parent, listing);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. The parent resource path of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
`listing` | `[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)`  
Required. The listing to create.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### createListing(CreateListingRequest request)
    
    
    public final Listing createListing(CreateListingRequest request)

Creates a new listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       CreateListingRequest request =
           CreateListingRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setListingId("listingId-1215024449")
               .setListing(Listing.newBuilder().build())
               .build();
       Listing response = analyticsHubServiceClient.createListing(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateListingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### createListing(String parent, Listing listing)
    
    
    public final Listing createListing(String parent, Listing listing)

Creates a new listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       Listing listing = Listing.newBuilder().build();
       Listing response = analyticsHubServiceClient.createListing(parent, listing);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
`listing` | `[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)`  
Required. The listing to create.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### createListingCallable()
    
    
    public final UnaryCallable<CreateListingRequest,Listing> createListingCallable()

Creates a new listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       CreateListingRequest request =
           CreateListingRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setListingId("listingId-1215024449")
               .setListing(Listing.newBuilder().build())
               .build();
       ApiFuture<Listing> future =
           analyticsHubServiceClient.createListingCallable().futureCall(request);
       // Do something.
       Listing response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateListingRequest),[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>` |   
  
### createQueryTemplate(@Nullable DataExchangeName parent, QueryTemplate queryTemplate, String queryTemplateId)
    
    
    public final QueryTemplate createQueryTemplate(@Nullable DataExchangeName parent, QueryTemplate queryTemplate, String queryTemplateId)

Creates a new QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       QueryTemplate queryTemplate = QueryTemplate.newBuilder().build();
       String queryTemplateId = "queryTemplateId-1884800483";
       QueryTemplate response =
           analyticsHubServiceClient.createQueryTemplate(parent, queryTemplate, queryTemplateId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. The parent resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myQueryTemplate`.  
`queryTemplate` | `[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)`  
Required. The QueryTemplate to create.  
`queryTemplateId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the QueryTemplate to create. Must contain only Unicode letters, numbers (0-9), underscores (_). Max length: 100 bytes.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### createQueryTemplate(CreateQueryTemplateRequest request)
    
    
    public final QueryTemplate createQueryTemplate(CreateQueryTemplateRequest request)

Creates a new QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       CreateQueryTemplateRequest request =
           CreateQueryTemplateRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setQueryTemplateId("queryTemplateId-1884800483")
               .setQueryTemplate(QueryTemplate.newBuilder().build())
               .build();
       QueryTemplate response = analyticsHubServiceClient.createQueryTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateQueryTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### createQueryTemplate(String parent, QueryTemplate queryTemplate, String queryTemplateId)
    
    
    public final QueryTemplate createQueryTemplate(String parent, QueryTemplate queryTemplate, String queryTemplateId)

Creates a new QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       QueryTemplate queryTemplate = QueryTemplate.newBuilder().build();
       String queryTemplateId = "queryTemplateId-1884800483";
       QueryTemplate response =
           analyticsHubServiceClient.createQueryTemplate(parent, queryTemplate, queryTemplateId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myQueryTemplate`.  
`queryTemplate` | `[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)`  
Required. The QueryTemplate to create.  
`queryTemplateId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the QueryTemplate to create. Must contain only Unicode letters, numbers (0-9), underscores (_). Max length: 100 bytes.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### createQueryTemplateCallable()
    
    
    public final UnaryCallable<CreateQueryTemplateRequest,QueryTemplate> createQueryTemplateCallable()

Creates a new QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       CreateQueryTemplateRequest request =
           CreateQueryTemplateRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setQueryTemplateId("queryTemplateId-1884800483")
               .setQueryTemplate(QueryTemplate.newBuilder().build())
               .build();
       ApiFuture<QueryTemplate> future =
           analyticsHubServiceClient.createQueryTemplateCallable().futureCall(request);
       // Do something.
       QueryTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### deleteDataExchange(@Nullable DataExchangeName name)
    
    
    public final void deleteDataExchange(@Nullable DataExchangeName name)

Deletes an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       analyticsHubServiceClient.deleteDataExchange(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. The full name of the data exchange resource that you want to delete. For example, `projects/myproject/locations/us/dataExchanges/123`.  
  
### deleteDataExchange(DeleteDataExchangeRequest request)
    
    
    public final void deleteDataExchange(DeleteDataExchangeRequest request)

Deletes an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteDataExchangeRequest request =
           DeleteDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .build();
       analyticsHubServiceClient.deleteDataExchange(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteDataExchangeRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDataExchange(String name)
    
    
    public final void deleteDataExchange(String name)

Deletes an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       analyticsHubServiceClient.deleteDataExchange(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full name of the data exchange resource that you want to delete. For example, `projects/myproject/locations/us/dataExchanges/123`.  
  
### deleteDataExchangeCallable()
    
    
    public final UnaryCallable<DeleteDataExchangeRequest,Empty> deleteDataExchangeCallable()

Deletes an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteDataExchangeRequest request =
           DeleteDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .build();
       ApiFuture<Empty> future =
           analyticsHubServiceClient.deleteDataExchangeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteDataExchangeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteListing(@Nullable ListingName name)
    
    
    public final void deleteListing(@Nullable ListingName name)

Deletes a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListingName name = ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]");
       analyticsHubServiceClient.deleteListing(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.ListingName`  
Required. Resource name of the listing to delete. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.  
  
### deleteListing(DeleteListingRequest request)
    
    
    public final void deleteListing(DeleteListingRequest request)

Deletes a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteListingRequest request =
           DeleteListingRequest.newBuilder()
               .setName(
                   ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]")
                       .toString())
               .setDeleteCommercial(true)
               .build();
       analyticsHubServiceClient.deleteListing(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteListingRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteListing(String name)
    
    
    public final void deleteListing(String name)

Deletes a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]").toString();
       analyticsHubServiceClient.deleteListing(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the listing to delete. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.  
  
### deleteListingCallable()
    
    
    public final UnaryCallable<DeleteListingRequest,Empty> deleteListingCallable()

Deletes a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteListingRequest request =
           DeleteListingRequest.newBuilder()
               .setName(
                   ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]")
                       .toString())
               .setDeleteCommercial(true)
               .build();
       ApiFuture<Empty> future =
           analyticsHubServiceClient.deleteListingCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteListingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteQueryTemplate(@Nullable QueryTemplateName name)
    
    
    public final void deleteQueryTemplate(@Nullable QueryTemplateName name)

Deletes a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       QueryTemplateName name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]");
       analyticsHubServiceClient.deleteQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.QueryTemplateName`  
Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
  
### deleteQueryTemplate(DeleteQueryTemplateRequest request)
    
    
    public final void deleteQueryTemplate(DeleteQueryTemplateRequest request)

Deletes a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteQueryTemplateRequest request =
           DeleteQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       analyticsHubServiceClient.deleteQueryTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteQueryTemplateRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteQueryTemplate(String name)
    
    
    public final void deleteQueryTemplate(String name)

Deletes a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
               .toString();
       analyticsHubServiceClient.deleteQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
  
### deleteQueryTemplateCallable()
    
    
    public final UnaryCallable<DeleteQueryTemplateRequest,Empty> deleteQueryTemplateCallable()

Deletes a query template.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteQueryTemplateRequest request =
           DeleteQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           analyticsHubServiceClient.deleteQueryTemplateCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteQueryTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSubscriptionAsync(@Nullable SubscriptionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSubscriptionAsync(@Nullable SubscriptionName name)

Deletes a subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscriptionName name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]");
       analyticsHubServiceClient.deleteSubscriptionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.SubscriptionName`  
Required. Resource name of the subscription to delete. e.g. projects/123/locations/us/subscriptions/456  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### deleteSubscriptionAsync(DeleteSubscriptionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSubscriptionAsync(DeleteSubscriptionRequest request)

Deletes a subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteSubscriptionRequest request =
           DeleteSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       analyticsHubServiceClient.deleteSubscriptionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### deleteSubscriptionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSubscriptionAsync(String name)

Deletes a subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString();
       analyticsHubServiceClient.deleteSubscriptionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the subscription to delete. e.g. projects/123/locations/us/subscriptions/456  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### deleteSubscriptionCallable()
    
    
    public final UnaryCallable<DeleteSubscriptionRequest,Operation> deleteSubscriptionCallable()

Deletes a subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteSubscriptionRequest request =
           DeleteSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       ApiFuture<Operation> future =
           analyticsHubServiceClient.deleteSubscriptionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteSubscriptionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSubscriptionOperationCallable()
    
    
    public final OperationCallable<DeleteSubscriptionRequest,Empty,OperationMetadata> deleteSubscriptionOperationCallable()

Deletes a subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DeleteSubscriptionRequest request =
           DeleteSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           analyticsHubServiceClient.deleteSubscriptionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteSubscriptionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### getDataExchange(@Nullable DataExchangeName name)
    
    
    public final DataExchange getDataExchange(@Nullable DataExchangeName name)

Gets the details of a data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       DataExchange response = analyticsHubServiceClient.getDataExchange(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. The resource name of the data exchange. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### getDataExchange(GetDataExchangeRequest request)
    
    
    public final DataExchange getDataExchange(GetDataExchangeRequest request)

Gets the details of a data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetDataExchangeRequest request =
           GetDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .build();
       DataExchange response = analyticsHubServiceClient.getDataExchange(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetDataExchangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### getDataExchange(String name)
    
    
    public final DataExchange getDataExchange(String name)

Gets the details of a data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       DataExchange response = analyticsHubServiceClient.getDataExchange(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the data exchange. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### getDataExchangeCallable()
    
    
    public final UnaryCallable<GetDataExchangeRequest,DataExchange> getDataExchangeCallable()

Gets the details of a data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetDataExchangeRequest request =
           GetDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .build();
       ApiFuture<DataExchange> future =
           analyticsHubServiceClient.getDataExchangeCallable().futureCall(request);
       // Do something.
       DataExchange response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetDataExchangeRequest),[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the IAM policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = analyticsHubServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the IAM policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           analyticsHubServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getListing(@Nullable ListingName name)
    
    
    public final Listing getListing(@Nullable ListingName name)

Gets the details of a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListingName name = ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]");
       Listing response = analyticsHubServiceClient.getListing(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.ListingName`  
Required. The resource name of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### getListing(GetListingRequest request)
    
    
    public final Listing getListing(GetListingRequest request)

Gets the details of a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetListingRequest request =
           GetListingRequest.newBuilder()
               .setName(
                   ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]")
                       .toString())
               .build();
       Listing response = analyticsHubServiceClient.getListing(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetListingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### getListing(String name)
    
    
    public final Listing getListing(String name)

Gets the details of a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]").toString();
       Listing response = analyticsHubServiceClient.getListing(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### getListingCallable()
    
    
    public final UnaryCallable<GetListingRequest,Listing> getListingCallable()

Gets the details of a listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetListingRequest request =
           GetListingRequest.newBuilder()
               .setName(
                   ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]")
                       .toString())
               .build();
       ApiFuture<Listing> future =
           analyticsHubServiceClient.getListingCallable().futureCall(request);
       // Do something.
       Listing response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetListingRequest),[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getQueryTemplate(@Nullable QueryTemplateName name)
    
    
    public final QueryTemplate getQueryTemplate(@Nullable QueryTemplateName name)

Gets a QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       QueryTemplateName name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]");
       QueryTemplate response = analyticsHubServiceClient.getQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.QueryTemplateName`  
Required. The parent resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### getQueryTemplate(GetQueryTemplateRequest request)
    
    
    public final QueryTemplate getQueryTemplate(GetQueryTemplateRequest request)

Gets a QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetQueryTemplateRequest request =
           GetQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       QueryTemplate response = analyticsHubServiceClient.getQueryTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetQueryTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### getQueryTemplate(String name)
    
    
    public final QueryTemplate getQueryTemplate(String name)

Gets a QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
               .toString();
       QueryTemplate response = analyticsHubServiceClient.getQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### getQueryTemplateCallable()
    
    
    public final UnaryCallable<GetQueryTemplateRequest,QueryTemplate> getQueryTemplateCallable()

Gets a QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetQueryTemplateRequest request =
           GetQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       ApiFuture<QueryTemplate> future =
           analyticsHubServiceClient.getQueryTemplateCallable().futureCall(request);
       // Do something.
       QueryTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### getSettings()
    
    
    public final @Nullable AnalyticsHubServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings` |   
  
### getStub()
    
    
    public AnalyticsHubServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.stub.AnalyticsHubServiceStub)` |   
  
### getSubscription(@Nullable SubscriptionName name)
    
    
    public final Subscription getSubscription(@Nullable SubscriptionName name)

Gets the details of a Subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscriptionName name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]");
       Subscription response = analyticsHubServiceClient.getSubscription(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.SubscriptionName`  
Required. Resource name of the subscription. e.g. projects/123/locations/us/subscriptions/456  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Subscription)` |   
  
### getSubscription(GetSubscriptionRequest request)
    
    
    public final Subscription getSubscription(GetSubscriptionRequest request)

Gets the details of a Subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetSubscriptionRequest request =
           GetSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       Subscription response = analyticsHubServiceClient.getSubscription(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Subscription)` |   
  
### getSubscription(String name)
    
    
    public final Subscription getSubscription(String name)

Gets the details of a Subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString();
       Subscription response = analyticsHubServiceClient.getSubscription(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the subscription. e.g. projects/123/locations/us/subscriptions/456  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Subscription)` |   
  
### getSubscriptionCallable()
    
    
    public final UnaryCallable<GetSubscriptionRequest,Subscription> getSubscriptionCallable()

Gets the details of a Subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       GetSubscriptionRequest request =
           GetSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       ApiFuture<Subscription> future =
           analyticsHubServiceClient.getSubscriptionCallable().futureCall(request);
       // Do something.
       Subscription response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetSubscriptionRequest),[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Subscription)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listDataExchanges(@Nullable LocationName parent)
    
    
    public final AnalyticsHubServiceClient.ListDataExchangesPagedResponse listDataExchanges(@Nullable LocationName parent)

Lists all data exchanges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataExchange element :
           analyticsHubServiceClient.listDataExchanges(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.LocationName`  
Required. The parent resource path of the data exchanges. e.g. `projects/myproject/locations/us`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListDataExchangesPagedResponse)` |   
  
### listDataExchanges(ListDataExchangesRequest request)
    
    
    public final AnalyticsHubServiceClient.ListDataExchangesPagedResponse listDataExchanges(ListDataExchangesRequest request)

Lists all data exchanges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListDataExchangesRequest request =
           ListDataExchangesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DataExchange element :
           analyticsHubServiceClient.listDataExchanges(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListDataExchangesPagedResponse)` |   
  
### listDataExchanges(String parent)
    
    
    public final AnalyticsHubServiceClient.ListDataExchangesPagedResponse listDataExchanges(String parent)

Lists all data exchanges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataExchange element :
           analyticsHubServiceClient.listDataExchanges(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the data exchanges. e.g. `projects/myproject/locations/us`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListDataExchangesPagedResponse)` |   
  
### listDataExchangesCallable()
    
    
    public final UnaryCallable<ListDataExchangesRequest,ListDataExchangesResponse> listDataExchangesCallable()

Lists all data exchanges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListDataExchangesRequest request =
           ListDataExchangesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDataExchangesResponse response =
             analyticsHubServiceClient.listDataExchangesCallable().call(request);
         for (DataExchange element : response.getDataExchangesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesRequest),[ListDataExchangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesResponse)>` |   
  
### listDataExchangesPagedCallable()
    
    
    public final UnaryCallable<ListDataExchangesRequest,AnalyticsHubServiceClient.ListDataExchangesPagedResponse> listDataExchangesPagedCallable()

Lists all data exchanges in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListDataExchangesRequest request =
           ListDataExchangesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DataExchange> future =
           analyticsHubServiceClient.listDataExchangesPagedCallable().futureCall(request);
       // Do something.
       for (DataExchange element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesRequest),[ListDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListDataExchangesPagedResponse)>` |   
  
### listListings(@Nullable DataExchangeName parent)
    
    
    public final AnalyticsHubServiceClient.ListListingsPagedResponse listListings(@Nullable DataExchangeName parent)

Lists all listings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       for (Listing element : analyticsHubServiceClient.listListings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. The parent resource path of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListListingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListListingsPagedResponse)` |   
  
### listListings(ListListingsRequest request)
    
    
    public final AnalyticsHubServiceClient.ListListingsPagedResponse listListings(ListListingsRequest request)

Lists all listings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListListingsRequest request =
           ListListingsRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Listing element : analyticsHubServiceClient.listListings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListListingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListListingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListListingsPagedResponse)` |   
  
### listListings(String parent)
    
    
    public final AnalyticsHubServiceClient.ListListingsPagedResponse listListings(String parent)

Lists all listings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       for (Listing element : analyticsHubServiceClient.listListings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListListingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListListingsPagedResponse)` |   
  
### listListingsCallable()
    
    
    public final UnaryCallable<ListListingsRequest,ListListingsResponse> listListingsCallable()

Lists all listings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListListingsRequest request =
           ListListingsRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListListingsResponse response =
             analyticsHubServiceClient.listListingsCallable().call(request);
         for (Listing element : response.getListingsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListListingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsRequest),[ListListingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsResponse)>` |   
  
### listListingsPagedCallable()
    
    
    public final UnaryCallable<ListListingsRequest,AnalyticsHubServiceClient.ListListingsPagedResponse> listListingsPagedCallable()

Lists all listings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListListingsRequest request =
           ListListingsRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Listing> future =
           analyticsHubServiceClient.listListingsPagedCallable().futureCall(request);
       // Do something.
       for (Listing element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListListingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsRequest),[ListListingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListListingsPagedResponse)>` |   
  
### listOrgDataExchanges(ListOrgDataExchangesRequest request)
    
    
    public final AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse listOrgDataExchanges(ListOrgDataExchangesRequest request)

Lists all data exchanges from projects in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListOrgDataExchangesRequest request =
           ListOrgDataExchangesRequest.newBuilder()
               .setOrganization("organization1178922291")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DataExchange element :
           analyticsHubServiceClient.listOrgDataExchanges(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrgDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse)` |   
  
### listOrgDataExchanges(String organization)
    
    
    public final AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse listOrgDataExchanges(String organization)

Lists all data exchanges from projects in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String organization = "organization1178922291";
       for (DataExchange element :
           analyticsHubServiceClient.listOrgDataExchanges(organization).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The organization resource path of the projects containing DataExchanges. e.g. `organizations/myorg/locations/us`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse)` |   
  
### listOrgDataExchangesCallable()
    
    
    public final UnaryCallable<ListOrgDataExchangesRequest,ListOrgDataExchangesResponse> listOrgDataExchangesCallable()

Lists all data exchanges from projects in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListOrgDataExchangesRequest request =
           ListOrgDataExchangesRequest.newBuilder()
               .setOrganization("organization1178922291")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListOrgDataExchangesResponse response =
             analyticsHubServiceClient.listOrgDataExchangesCallable().call(request);
         for (DataExchange element : response.getDataExchangesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrgDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesRequest),[ListOrgDataExchangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesResponse)>` |   
  
### listOrgDataExchangesPagedCallable()
    
    
    public final UnaryCallable<ListOrgDataExchangesRequest,AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse> listOrgDataExchangesPagedCallable()

Lists all data exchanges from projects in a given organization and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListOrgDataExchangesRequest request =
           ListOrgDataExchangesRequest.newBuilder()
               .setOrganization("organization1178922291")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DataExchange> future =
           analyticsHubServiceClient.listOrgDataExchangesPagedCallable().futureCall(request);
       // Do something.
       for (DataExchange element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrgDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesRequest),[ListOrgDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse)>` |   
  
### listQueryTemplates(@Nullable DataExchangeName parent)
    
    
    public final AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse listQueryTemplates(@Nullable DataExchangeName parent)

Lists all QueryTemplates in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       for (QueryTemplate element :
           analyticsHubServiceClient.listQueryTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. The parent resource path of the QueryTemplates. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse)` |   
  
### listQueryTemplates(ListQueryTemplatesRequest request)
    
    
    public final AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse listQueryTemplates(ListQueryTemplatesRequest request)

Lists all QueryTemplates in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListQueryTemplatesRequest request =
           ListQueryTemplatesRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (QueryTemplate element :
           analyticsHubServiceClient.listQueryTemplates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListQueryTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse)` |   
  
### listQueryTemplates(String parent)
    
    
    public final AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse listQueryTemplates(String parent)

Lists all QueryTemplates in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       for (QueryTemplate element :
           analyticsHubServiceClient.listQueryTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the QueryTemplates. e.g. `projects/myproject/locations/us/dataExchanges/123`.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse)` |   
  
### listQueryTemplatesCallable()
    
    
    public final UnaryCallable<ListQueryTemplatesRequest,ListQueryTemplatesResponse> listQueryTemplatesCallable()

Lists all QueryTemplates in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListQueryTemplatesRequest request =
           ListQueryTemplatesRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListQueryTemplatesResponse response =
             analyticsHubServiceClient.listQueryTemplatesCallable().call(request);
         for (QueryTemplate element : response.getQueryTemplatesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQueryTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesRequest),[ListQueryTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesResponse)>` |   
  
### listQueryTemplatesPagedCallable()
    
    
    public final UnaryCallable<ListQueryTemplatesRequest,AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse> listQueryTemplatesPagedCallable()

Lists all QueryTemplates in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListQueryTemplatesRequest request =
           ListQueryTemplatesRequest.newBuilder()
               .setParent(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<QueryTemplate> future =
           analyticsHubServiceClient.listQueryTemplatesPagedCallable().futureCall(request);
       // Do something.
       for (QueryTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListQueryTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesRequest),[ListQueryTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse)>` |   
  
### listSharedResourceSubscriptions(@Nullable ResourceName resource)
    
    
    public final AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse listSharedResourceSubscriptions(@Nullable ResourceName resource)

Lists all subscriptions on a given Data Exchange or Listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ResourceName resource = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       for (Subscription element :
           analyticsHubServiceClient.listSharedResourceSubscriptions(resource).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
Required. Resource name of the requested target. This resource may be either a Listing or a DataExchange. e.g. projects/123/locations/us/dataExchanges/456 OR e.g. projects/123/locations/us/dataExchanges/456/listings/789  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse)` |   
  
### listSharedResourceSubscriptions(ListSharedResourceSubscriptionsRequest request)
    
    
    public final AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse listSharedResourceSubscriptions(ListSharedResourceSubscriptionsRequest request)

Lists all subscriptions on a given Data Exchange or Listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListSharedResourceSubscriptionsRequest request =
           ListSharedResourceSubscriptionsRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setIncludeDeletedSubscriptions(true)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Subscription element :
           analyticsHubServiceClient.listSharedResourceSubscriptions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse)` |   
  
### listSharedResourceSubscriptions(String resource)
    
    
    public final AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse listSharedResourceSubscriptions(String resource)

Lists all subscriptions on a given Data Exchange or Listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String resource =
           DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       for (Subscription element :
           analyticsHubServiceClient.listSharedResourceSubscriptions(resource).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the requested target. This resource may be either a Listing or a DataExchange. e.g. projects/123/locations/us/dataExchanges/456 OR e.g. projects/123/locations/us/dataExchanges/456/listings/789  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse)` |   
  
### listSharedResourceSubscriptionsCallable()
    
    
    public final UnaryCallable<ListSharedResourceSubscriptionsRequest,ListSharedResourceSubscriptionsResponse> listSharedResourceSubscriptionsCallable()

Lists all subscriptions on a given Data Exchange or Listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListSharedResourceSubscriptionsRequest request =
           ListSharedResourceSubscriptionsRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setIncludeDeletedSubscriptions(true)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSharedResourceSubscriptionsResponse response =
             analyticsHubServiceClient.listSharedResourceSubscriptionsCallable().call(request);
         for (Subscription element : response.getSharedResourceSubscriptionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsRequest),[ListSharedResourceSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsResponse)>` |   
  
### listSharedResourceSubscriptionsPagedCallable()
    
    
    public final UnaryCallable<ListSharedResourceSubscriptionsRequest,AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse> listSharedResourceSubscriptionsPagedCallable()

Lists all subscriptions on a given Data Exchange or Listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListSharedResourceSubscriptionsRequest request =
           ListSharedResourceSubscriptionsRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setIncludeDeletedSubscriptions(true)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Subscription> future =
           analyticsHubServiceClient
               .listSharedResourceSubscriptionsPagedCallable()
               .futureCall(request);
       // Do something.
       for (Subscription element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsRequest),[ListSharedResourceSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse)>` |   
  
### listSubscriptions(@Nullable LocationName parent)
    
    
    public final AnalyticsHubServiceClient.ListSubscriptionsPagedResponse listSubscriptions(@Nullable LocationName parent)

Lists all subscriptions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Subscription element :
           analyticsHubServiceClient.listSubscriptions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.LocationName`  
Required. The parent resource path of the subscription. e.g. projects/myproject/locations/us  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSubscriptionsPagedResponse)` |   
  
### listSubscriptions(ListSubscriptionsRequest request)
    
    
    public final AnalyticsHubServiceClient.ListSubscriptionsPagedResponse listSubscriptions(ListSubscriptionsRequest request)

Lists all subscriptions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListSubscriptionsRequest request =
           ListSubscriptionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Subscription element :
           analyticsHubServiceClient.listSubscriptions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSubscriptionsPagedResponse)` |   
  
### listSubscriptions(String parent)
    
    
    public final AnalyticsHubServiceClient.ListSubscriptionsPagedResponse listSubscriptions(String parent)

Lists all subscriptions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Subscription element :
           analyticsHubServiceClient.listSubscriptions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource path of the subscription. e.g. projects/myproject/locations/us  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceClient.ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSubscriptionsPagedResponse)` |   
  
### listSubscriptionsCallable()
    
    
    public final UnaryCallable<ListSubscriptionsRequest,ListSubscriptionsResponse> listSubscriptionsCallable()

Lists all subscriptions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListSubscriptionsRequest request =
           ListSubscriptionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSubscriptionsResponse response =
             analyticsHubServiceClient.listSubscriptionsCallable().call(request);
         for (Subscription element : response.getSubscriptionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsRequest),[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsResponse)>` |   
  
### listSubscriptionsPagedCallable()
    
    
    public final UnaryCallable<ListSubscriptionsRequest,AnalyticsHubServiceClient.ListSubscriptionsPagedResponse> listSubscriptionsPagedCallable()

Lists all subscriptions in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListSubscriptionsRequest request =
           ListSubscriptionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Subscription> future =
           analyticsHubServiceClient.listSubscriptionsPagedCallable().futureCall(request);
       // Do something.
       for (Subscription element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsRequest),[ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSubscriptionsPagedResponse)>` |   
  
### refreshSubscriptionAsync(@Nullable SubscriptionName name)
    
    
    public final OperationFuture<RefreshSubscriptionResponse,OperationMetadata> refreshSubscriptionAsync(@Nullable SubscriptionName name)

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscriptionName name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]");
       RefreshSubscriptionResponse response =
           analyticsHubServiceClient.refreshSubscriptionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.SubscriptionName`  
Required. Resource name of the Subscription to refresh. e.g. `projects/subscriberproject/locations/us/subscriptions/123`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RefreshSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### refreshSubscriptionAsync(RefreshSubscriptionRequest request)
    
    
    public final OperationFuture<RefreshSubscriptionResponse,OperationMetadata> refreshSubscriptionAsync(RefreshSubscriptionRequest request)

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       RefreshSubscriptionRequest request =
           RefreshSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       RefreshSubscriptionResponse response =
           analyticsHubServiceClient.refreshSubscriptionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RefreshSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RefreshSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### refreshSubscriptionAsync(String name)
    
    
    public final OperationFuture<RefreshSubscriptionResponse,OperationMetadata> refreshSubscriptionAsync(String name)

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString();
       RefreshSubscriptionResponse response =
           analyticsHubServiceClient.refreshSubscriptionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the Subscription to refresh. e.g. `projects/subscriberproject/locations/us/subscriptions/123`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RefreshSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### refreshSubscriptionCallable()
    
    
    public final UnaryCallable<RefreshSubscriptionRequest,Operation> refreshSubscriptionCallable()

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       RefreshSubscriptionRequest request =
           RefreshSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       ApiFuture<Operation> future =
           analyticsHubServiceClient.refreshSubscriptionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RefreshSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### refreshSubscriptionOperationCallable()
    
    
    public final OperationCallable<RefreshSubscriptionRequest,RefreshSubscriptionResponse,OperationMetadata> refreshSubscriptionOperationCallable()

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       RefreshSubscriptionRequest request =
           RefreshSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .build();
       OperationFuture<RefreshSubscriptionResponse, OperationMetadata> future =
           analyticsHubServiceClient.refreshSubscriptionOperationCallable().futureCall(request);
       // Do something.
       RefreshSubscriptionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RefreshSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionRequest),[RefreshSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### revokeSubscription(@Nullable SubscriptionName name)
    
    
    public final RevokeSubscriptionResponse revokeSubscription(@Nullable SubscriptionName name)

Revokes a given subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscriptionName name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]");
       RevokeSubscriptionResponse response = analyticsHubServiceClient.revokeSubscription(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.SubscriptionName`  
Required. Resource name of the subscription to revoke. e.g. projects/123/locations/us/subscriptions/456  
**Returns**  
---  
**Type** | **Description**  
`[RevokeSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse)` |   
  
### revokeSubscription(RevokeSubscriptionRequest request)
    
    
    public final RevokeSubscriptionResponse revokeSubscription(RevokeSubscriptionRequest request)

Revokes a given subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       RevokeSubscriptionRequest request =
           RevokeSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .setRevokeCommercial(true)
               .build();
       RevokeSubscriptionResponse response = analyticsHubServiceClient.revokeSubscription(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RevokeSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RevokeSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse)` |   
  
### revokeSubscription(String name)
    
    
    public final RevokeSubscriptionResponse revokeSubscription(String name)

Revokes a given subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString();
       RevokeSubscriptionResponse response = analyticsHubServiceClient.revokeSubscription(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the subscription to revoke. e.g. projects/123/locations/us/subscriptions/456  
**Returns**  
---  
**Type** | **Description**  
`[RevokeSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse)` |   
  
### revokeSubscriptionCallable()
    
    
    public final UnaryCallable<RevokeSubscriptionRequest,RevokeSubscriptionResponse> revokeSubscriptionCallable()

Revokes a given subscription.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       RevokeSubscriptionRequest request =
           RevokeSubscriptionRequest.newBuilder()
               .setName(SubscriptionName.of("[PROJECT]", "[LOCATION]", "[SUBSCRIPTION]").toString())
               .setRevokeCommercial(true)
               .build();
       ApiFuture<RevokeSubscriptionResponse> future =
           analyticsHubServiceClient.revokeSubscriptionCallable().futureCall(request);
       // Do something.
       RevokeSubscriptionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RevokeSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionRequest),[RevokeSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the IAM policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = analyticsHubServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the IAM policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           analyticsHubServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### submitQueryTemplate(@Nullable QueryTemplateName name)
    
    
    public final QueryTemplate submitQueryTemplate(@Nullable QueryTemplateName name)

Submits a query template for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       QueryTemplateName name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]");
       QueryTemplate response = analyticsHubServiceClient.submitQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.QueryTemplateName`  
Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### submitQueryTemplate(SubmitQueryTemplateRequest request)
    
    
    public final QueryTemplate submitQueryTemplate(SubmitQueryTemplateRequest request)

Submits a query template for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubmitQueryTemplateRequest request =
           SubmitQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       QueryTemplate response = analyticsHubServiceClient.submitQueryTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubmitQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubmitQueryTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### submitQueryTemplate(String name)
    
    
    public final QueryTemplate submitQueryTemplate(String name)

Submits a query template for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           QueryTemplateName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
               .toString();
       QueryTemplate response = analyticsHubServiceClient.submitQueryTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### submitQueryTemplateCallable()
    
    
    public final UnaryCallable<SubmitQueryTemplateRequest,QueryTemplate> submitQueryTemplateCallable()

Submits a query template for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubmitQueryTemplateRequest request =
           SubmitQueryTemplateRequest.newBuilder()
               .setName(
                   QueryTemplateName.of(
                           "[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[QUERY_TEMPLATE]")
                       .toString())
               .build();
       ApiFuture<QueryTemplate> future =
           analyticsHubServiceClient.submitQueryTemplateCallable().futureCall(request);
       // Do something.
       QueryTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SubmitQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubmitQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### subscribeDataExchangeAsync(@Nullable DataExchangeName name)
    
    
    public final OperationFuture<SubscribeDataExchangeResponse,OperationMetadata> subscribeDataExchangeAsync(@Nullable DataExchangeName name)

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchangeName name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]");
       SubscribeDataExchangeResponse response =
           analyticsHubServiceClient.subscribeDataExchangeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.DataExchangeName`  
Required. Resource name of the Data Exchange. e.g. `projects/publisherproject/locations/us/dataExchanges/123`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SubscribeDataExchangeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### subscribeDataExchangeAsync(SubscribeDataExchangeRequest request)
    
    
    public final OperationFuture<SubscribeDataExchangeResponse,OperationMetadata> subscribeDataExchangeAsync(SubscribeDataExchangeRequest request)

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscribeDataExchangeRequest request =
           SubscribeDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setDestination(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDestinationDataset(DestinationDataset.newBuilder().build())
               .setSubscription("subscription341203229")
               .setSubscriberContact("subscriberContact-847205736")
               .build();
       SubscribeDataExchangeResponse response =
           analyticsHubServiceClient.subscribeDataExchangeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubscribeDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SubscribeDataExchangeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### subscribeDataExchangeAsync(String name)
    
    
    public final OperationFuture<SubscribeDataExchangeResponse,OperationMetadata> subscribeDataExchangeAsync(String name)

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name = DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString();
       SubscribeDataExchangeResponse response =
           analyticsHubServiceClient.subscribeDataExchangeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the Data Exchange. e.g. `projects/publisherproject/locations/us/dataExchanges/123`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SubscribeDataExchangeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### subscribeDataExchangeCallable()
    
    
    public final UnaryCallable<SubscribeDataExchangeRequest,Operation> subscribeDataExchangeCallable()

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscribeDataExchangeRequest request =
           SubscribeDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setDestination(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDestinationDataset(DestinationDataset.newBuilder().build())
               .setSubscription("subscription341203229")
               .setSubscriberContact("subscriberContact-847205736")
               .build();
       ApiFuture<Operation> future =
           analyticsHubServiceClient.subscribeDataExchangeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SubscribeDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### subscribeDataExchangeOperationCallable()
    
    
    public final OperationCallable<SubscribeDataExchangeRequest,SubscribeDataExchangeResponse,OperationMetadata> subscribeDataExchangeOperationCallable()

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscribeDataExchangeRequest request =
           SubscribeDataExchangeRequest.newBuilder()
               .setName(DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .setDestination(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDestinationDataset(DestinationDataset.newBuilder().build())
               .setSubscription("subscription341203229")
               .setSubscriberContact("subscriberContact-847205736")
               .build();
       OperationFuture<SubscribeDataExchangeResponse, OperationMetadata> future =
           analyticsHubServiceClient.subscribeDataExchangeOperationCallable().futureCall(request);
       // Do something.
       SubscribeDataExchangeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SubscribeDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeRequest),[SubscribeDataExchangeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### subscribeListing(@Nullable ListingName name)
    
    
    public final SubscribeListingResponse subscribeListing(@Nullable ListingName name)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       ListingName name = ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]");
       SubscribeListingResponse response = analyticsHubServiceClient.subscribeListing(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.bigquery.analyticshub.v1.ListingName`  
Required. Resource name of the listing that you want to subscribe to. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.  
**Returns**  
---  
**Type** | **Description**  
`[SubscribeListingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse)` |   
  
### subscribeListing(SubscribeListingRequest request)
    
    
    public final SubscribeListingResponse subscribeListing(SubscribeListingRequest request)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscribeListingRequest request =
           SubscribeListingRequest.newBuilder()
               .setName(
                   ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]")
                       .toString())
               .build();
       SubscribeListingResponse response = analyticsHubServiceClient.subscribeListing(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubscribeListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SubscribeListingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse)` |   
  
### subscribeListing(String name)
    
    
    public final SubscribeListingResponse subscribeListing(String name)

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       String name =
           ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]").toString();
       SubscribeListingResponse response = analyticsHubServiceClient.subscribeListing(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the listing that you want to subscribe to. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.  
**Returns**  
---  
**Type** | **Description**  
`[SubscribeListingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse)` |   
  
### subscribeListingCallable()
    
    
    public final UnaryCallable<SubscribeListingRequest,SubscribeListingResponse> subscribeListingCallable()

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       SubscribeListingRequest request =
           SubscribeListingRequest.newBuilder()
               .setName(
                   ListingName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]", "[LISTING]")
                       .toString())
               .build();
       ApiFuture<SubscribeListingResponse> future =
           analyticsHubServiceClient.subscribeListingCallable().futureCall(request);
       // Do something.
       SubscribeListingResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SubscribeListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingRequest),[SubscribeListingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse)>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns the permissions that a caller has.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = analyticsHubServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns the permissions that a caller has.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   DataExchangeName.of("[PROJECT]", "[LOCATION]", "[DATA_EXCHANGE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           analyticsHubServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDataExchange(DataExchange dataExchange, FieldMask updateMask)
    
    
    public final DataExchange updateDataExchange(DataExchange dataExchange, FieldMask updateMask)

Updates an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       DataExchange dataExchange = DataExchange.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataExchange response =
           analyticsHubServiceClient.updateDataExchange(dataExchange, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataExchange` | `[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)`  
Required. The data exchange to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask specifies the fields to update in the data exchange resource. The fields specified in the `updateMask` are relative to the resource and are not a full request.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### updateDataExchange(UpdateDataExchangeRequest request)
    
    
    public final DataExchange updateDataExchange(UpdateDataExchangeRequest request)

Updates an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       UpdateDataExchangeRequest request =
           UpdateDataExchangeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataExchange(DataExchange.newBuilder().build())
               .build();
       DataExchange response = analyticsHubServiceClient.updateDataExchange(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateDataExchangeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)` |   
  
### updateDataExchangeCallable()
    
    
    public final UnaryCallable<UpdateDataExchangeRequest,DataExchange> updateDataExchangeCallable()

Updates an existing data exchange.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       UpdateDataExchangeRequest request =
           UpdateDataExchangeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setDataExchange(DataExchange.newBuilder().build())
               .build();
       ApiFuture<DataExchange> future =
           analyticsHubServiceClient.updateDataExchangeCallable().futureCall(request);
       // Do something.
       DataExchange response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateDataExchangeRequest),[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>` |   
  
### updateListing(Listing listing, FieldMask updateMask)
    
    
    public final Listing updateListing(Listing listing, FieldMask updateMask)

Updates an existing listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       Listing listing = Listing.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Listing response = analyticsHubServiceClient.updateListing(listing, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`listing` | `[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)`  
Required. The listing to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Field mask specifies the fields to update in the listing resource. The fields specified in the `updateMask` are relative to the resource and are not a full request.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### updateListing(UpdateListingRequest request)
    
    
    public final Listing updateListing(UpdateListingRequest request)

Updates an existing listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       UpdateListingRequest request =
           UpdateListingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setListing(Listing.newBuilder().build())
               .build();
       Listing response = analyticsHubServiceClient.updateListing(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateListingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)` |   
  
### updateListingCallable()
    
    
    public final UnaryCallable<UpdateListingRequest,Listing> updateListingCallable()

Updates an existing listing.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       UpdateListingRequest request =
           UpdateListingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setListing(Listing.newBuilder().build())
               .build();
       ApiFuture<Listing> future =
           analyticsHubServiceClient.updateListingCallable().futureCall(request);
       // Do something.
       Listing response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateListingRequest),[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>` |   
  
### updateQueryTemplate(QueryTemplate queryTemplate, FieldMask updateMask)
    
    
    public final QueryTemplate updateQueryTemplate(QueryTemplate queryTemplate, FieldMask updateMask)

Updates an existing QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       QueryTemplate queryTemplate = QueryTemplate.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       QueryTemplate response =
           analyticsHubServiceClient.updateQueryTemplate(queryTemplate, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`queryTemplate` | `[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)`  
Required. The QueryTemplate to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask specifies the fields to update in the query template resource. The fields specified in the `updateMask` are relative to the resource and are not a full request.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### updateQueryTemplate(UpdateQueryTemplateRequest request)
    
    
    public final QueryTemplate updateQueryTemplate(UpdateQueryTemplateRequest request)

Updates an existing QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       UpdateQueryTemplateRequest request =
           UpdateQueryTemplateRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setQueryTemplate(QueryTemplate.newBuilder().build())
               .build();
       QueryTemplate response = analyticsHubServiceClient.updateQueryTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateQueryTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)` |   
  
### updateQueryTemplateCallable()
    
    
    public final UnaryCallable<UpdateQueryTemplateRequest,QueryTemplate> updateQueryTemplateCallable()

Updates an existing QueryTemplate

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AnalyticsHubServiceClient analyticsHubServiceClient = AnalyticsHubServiceClient.create()) {
       UpdateQueryTemplateRequest request =
           UpdateQueryTemplateRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setQueryTemplate(QueryTemplate.newBuilder().build())
               .build();
       ApiFuture<QueryTemplate> future =
           analyticsHubServiceClient.updateQueryTemplateCallable().futureCall(request);
       // Do something.
       QueryTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
