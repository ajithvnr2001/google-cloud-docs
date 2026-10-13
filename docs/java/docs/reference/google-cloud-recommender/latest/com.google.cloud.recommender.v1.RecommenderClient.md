---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient
title: Class RecommenderClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:01.672359+00:00
---

# Class RecommenderClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RecommenderClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.7  2.4.1  2.3.0  2.2.0  2.1.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-recommender/google-cloud-recommender/src/main/java/com/google/cloud/recommender/v1/RecommenderClient.java)| [Product Reference](https://cloud.google.com/recommendations/)  
---|---  
  
Service Description: Provides insights and recommendations for cloud customers for various categories like performance optimization, cost savings, reliability, feature discovery, etc. Insights and recommendations are generated automatically based on analysis of user resources, configuration and monitoring metrics.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       InsightName name =
           InsightName.ofProjectLocationInsightTypeInsightName(
               "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]");
       Insight response = recommenderClient.getInsight(name);
     }
     

Note: close() needs to be called on the RecommenderClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListInsights |  Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInsights(ListInsightsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInsights(InsightTypeName parent) 
  * listInsights(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInsightsPagedCallable() 
  * listInsightsCallable() 

  
GetInsight |  Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInsight(GetInsightRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInsight(InsightName name) 
  * getInsight(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInsightCallable() 

  
MarkInsightAccepted |  Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated.  MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markInsightAccepted(MarkInsightAcceptedRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * markInsightAccepted(InsightName name, Map<String, String> stateMetadata, String etag) 
  * markInsightAccepted(String name, Map<String, String> stateMetadata, String etag) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markInsightAcceptedCallable() 

  
ListRecommendations |  Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRecommendations(ListRecommendationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRecommendations(RecommenderName parent) 
  * listRecommendations(String parent) 
  * listRecommendations(RecommenderName parent, String filter) 
  * listRecommendations(String parent, String filter) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRecommendationsPagedCallable() 
  * listRecommendationsCallable() 

  
GetRecommendation |  Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRecommendation(GetRecommendationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRecommendation(RecommendationName name) 
  * getRecommendation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRecommendationCallable() 

  
MarkRecommendationDismissed |  Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED.  MarkRecommendationDismissed can be applied to recommendations in ACTIVE state.  Requires the recommender.*.update IAM permission for the specified recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markRecommendationDismissed(MarkRecommendationDismissedRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markRecommendationDismissedCallable() 

  
MarkRecommendationClaimed |  Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.  MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state.  Requires the recommender.*.update IAM permission for the specified recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markRecommendationClaimed(MarkRecommendationClaimedRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * markRecommendationClaimed(RecommendationName name, Map<String, String> stateMetadata, String etag) 
  * markRecommendationClaimed(String name, Map<String, String> stateMetadata, String etag) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markRecommendationClaimedCallable() 

  
MarkRecommendationSucceeded |  Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.  MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.  Requires the recommender.*.update IAM permission for the specified recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markRecommendationSucceeded(MarkRecommendationSucceededRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * markRecommendationSucceeded(RecommendationName name, Map<String, String> stateMetadata, String etag) 
  * markRecommendationSucceeded(String name, Map<String, String> stateMetadata, String etag) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markRecommendationSucceededCallable() 

  
MarkRecommendationFailed |  Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.  MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.  Requires the recommender.*.update IAM permission for the specified recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markRecommendationFailed(MarkRecommendationFailedRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * markRecommendationFailed(RecommendationName name, Map<String, String> stateMetadata, String etag) 
  * markRecommendationFailed(String name, Map<String, String> stateMetadata, String etag) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markRecommendationFailedCallable() 

  
GetRecommenderConfig |  Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRecommenderConfig(GetRecommenderConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRecommenderConfig(RecommenderConfigName name) 
  * getRecommenderConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRecommenderConfigCallable() 

  
UpdateRecommenderConfig |  Updates a Recommender Config. This will create a new revision of the config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRecommenderConfig(UpdateRecommenderConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRecommenderConfig(RecommenderConfig recommenderConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRecommenderConfigCallable() 

  
GetInsightTypeConfig |  Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInsightTypeConfig(GetInsightTypeConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInsightTypeConfig(InsightTypeConfigName name) 
  * getInsightTypeConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInsightTypeConfigCallable() 

  
UpdateInsightTypeConfig |  Updates an InsightTypeConfig change. This will create a new revision of the config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateInsightTypeConfig(UpdateInsightTypeConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateInsightTypeConfig(InsightTypeConfig insightTypeConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateInsightTypeConfigCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RecommenderSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RecommenderSettings recommenderSettings =
         RecommenderSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RecommenderClient recommenderClient = RecommenderClient.create(recommenderSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RecommenderSettings recommenderSettings =
         RecommenderSettings.newBuilder().setEndpoint(myEndpoint).build();
     RecommenderClient recommenderClient = RecommenderClient.create(recommenderSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RecommenderSettings recommenderSettings = RecommenderSettings.newHttpJsonBuilder().build();
     RecommenderClient recommenderClient = RecommenderClient.create(recommenderSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RecommenderClient

## Static Methods 

### create()
    
    
    public static final RecommenderClient create()

Constructs an instance of RecommenderClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RecommenderSettings settings)
    
    
    public static final RecommenderClient create(RecommenderSettings settings)

Constructs an instance of RecommenderClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RecommenderSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RecommenderStub stub)
    
    
    public static final RecommenderClient create(RecommenderStub stub)

Constructs an instance of RecommenderClient, using the given stub for making calls. This is for advanced usage - prefer using create(RecommenderSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RecommenderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.stub.RecommenderStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient)` |   
  
## Constructors 

### RecommenderClient(RecommenderSettings settings)
    
    
    protected RecommenderClient(RecommenderSettings settings)

Constructs an instance of RecommenderClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RecommenderSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderSettings)`  
  
  
### RecommenderClient(RecommenderStub stub)
    
    
    protected RecommenderClient(RecommenderStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RecommenderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.stub.RecommenderStub)`  
  
  
## Methods 

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

### getInsight(@Nullable InsightName name)
    
    
    public final Insight getInsight(@Nullable InsightName name)

Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       InsightName name =
           InsightName.ofProjectLocationInsightTypeInsightName(
               "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]");
       Insight response = recommenderClient.getInsight(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.InsightName`  
Required. Name of the insight.  
**Returns**  
---  
**Type** | **Description**  
`[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)` |   
  
### getInsight(GetInsightRequest request)
    
    
    public final Insight getInsight(GetInsightRequest request)

Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetInsightRequest request =
           GetInsightRequest.newBuilder()
               .setName(
                   InsightName.ofProjectLocationInsightTypeInsightName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]")
                       .toString())
               .build();
       Insight response = recommenderClient.getInsight(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInsightRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetInsightRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)` |   
  
### getInsight(String name)
    
    
    public final Insight getInsight(String name)

Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           InsightName.ofProjectLocationInsightTypeInsightName(
                   "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]")
               .toString();
       Insight response = recommenderClient.getInsight(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the insight.  
**Returns**  
---  
**Type** | **Description**  
`[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)` |   
  
### getInsightCallable()
    
    
    public final UnaryCallable<GetInsightRequest,Insight> getInsightCallable()

Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetInsightRequest request =
           GetInsightRequest.newBuilder()
               .setName(
                   InsightName.ofProjectLocationInsightTypeInsightName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]")
                       .toString())
               .build();
       ApiFuture<Insight> future = recommenderClient.getInsightCallable().futureCall(request);
       // Do something.
       Insight response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInsightRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetInsightRequest),[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)>` |   
  
### getInsightTypeConfig(@Nullable InsightTypeConfigName name)
    
    
    public final InsightTypeConfig getInsightTypeConfig(@Nullable InsightTypeConfigName name)

Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       InsightTypeConfigName name =
           InsightTypeConfigName.ofProjectLocationInsightTypeName(
               "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]");
       InsightTypeConfig response = recommenderClient.getInsightTypeConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.InsightTypeConfigName`  
Required. Name of the InsightTypeConfig to get. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`

  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)` |   
  
### getInsightTypeConfig(GetInsightTypeConfigRequest request)
    
    
    public final InsightTypeConfig getInsightTypeConfig(GetInsightTypeConfigRequest request)

Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetInsightTypeConfigRequest request =
           GetInsightTypeConfigRequest.newBuilder()
               .setName(
                   InsightTypeConfigName.ofProjectLocationInsightTypeName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
                       .toString())
               .build();
       InsightTypeConfig response = recommenderClient.getInsightTypeConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInsightTypeConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetInsightTypeConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)` |   
  
### getInsightTypeConfig(String name)
    
    
    public final InsightTypeConfig getInsightTypeConfig(String name)

Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           InsightTypeConfigName.ofProjectLocationInsightTypeName(
                   "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
               .toString();
       InsightTypeConfig response = recommenderClient.getInsightTypeConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the InsightTypeConfig to get. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config`

  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)` |   
  
### getInsightTypeConfigCallable()
    
    
    public final UnaryCallable<GetInsightTypeConfigRequest,InsightTypeConfig> getInsightTypeConfigCallable()

Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetInsightTypeConfigRequest request =
           GetInsightTypeConfigRequest.newBuilder()
               .setName(
                   InsightTypeConfigName.ofProjectLocationInsightTypeName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
                       .toString())
               .build();
       ApiFuture<InsightTypeConfig> future =
           recommenderClient.getInsightTypeConfigCallable().futureCall(request);
       // Do something.
       InsightTypeConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInsightTypeConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetInsightTypeConfigRequest),[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)>` |   
  
### getRecommendation(@Nullable RecommendationName name)
    
    
    public final Recommendation getRecommendation(@Nullable RecommendationName name)

Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommendationName name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]");
       Recommendation response = recommenderClient.getRecommendation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommendationName`  
Required. Name of the recommendation.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### getRecommendation(GetRecommendationRequest request)
    
    
    public final Recommendation getRecommendation(GetRecommendationRequest request)

Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetRecommendationRequest request =
           GetRecommendationRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .build();
       Recommendation response = recommenderClient.getRecommendation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRecommendationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetRecommendationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### getRecommendation(String name)
    
    
    public final Recommendation getRecommendation(String name)

Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
               .toString();
       Recommendation response = recommenderClient.getRecommendation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the recommendation.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### getRecommendationCallable()
    
    
    public final UnaryCallable<GetRecommendationRequest,Recommendation> getRecommendationCallable()

Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetRecommendationRequest request =
           GetRecommendationRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .build();
       ApiFuture<Recommendation> future =
           recommenderClient.getRecommendationCallable().futureCall(request);
       // Do something.
       Recommendation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRecommendationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetRecommendationRequest),[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)>` |   
  
### getRecommenderConfig(@Nullable RecommenderConfigName name)
    
    
    public final RecommenderConfig getRecommenderConfig(@Nullable RecommenderConfigName name)

Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommenderConfigName name =
           RecommenderConfigName.ofProjectLocationRecommenderName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]");
       RecommenderConfig response = recommenderClient.getRecommenderConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommenderConfigName`  
Required. Name of the Recommendation Config to get. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`

  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)` |   
  
### getRecommenderConfig(GetRecommenderConfigRequest request)
    
    
    public final RecommenderConfig getRecommenderConfig(GetRecommenderConfigRequest request)

Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetRecommenderConfigRequest request =
           GetRecommenderConfigRequest.newBuilder()
               .setName(
                   RecommenderConfigName.ofProjectLocationRecommenderName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
                       .toString())
               .build();
       RecommenderConfig response = recommenderClient.getRecommenderConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRecommenderConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetRecommenderConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)` |   
  
### getRecommenderConfig(String name)
    
    
    public final RecommenderConfig getRecommenderConfig(String name)

Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           RecommenderConfigName.ofProjectLocationRecommenderName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
               .toString();
       RecommenderConfig response = recommenderClient.getRecommenderConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the Recommendation Config to get. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config`

  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)` |   
  
### getRecommenderConfigCallable()
    
    
    public final UnaryCallable<GetRecommenderConfigRequest,RecommenderConfig> getRecommenderConfigCallable()

Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       GetRecommenderConfigRequest request =
           GetRecommenderConfigRequest.newBuilder()
               .setName(
                   RecommenderConfigName.ofProjectLocationRecommenderName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
                       .toString())
               .build();
       ApiFuture<RecommenderConfig> future =
           recommenderClient.getRecommenderConfigCallable().futureCall(request);
       // Do something.
       RecommenderConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRecommenderConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.GetRecommenderConfigRequest),[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)>` |   
  
### getSettings()
    
    
    public final @Nullable RecommenderSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommenderSettings` |   
  
### getStub()
    
    
    public RecommenderStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RecommenderStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.stub.RecommenderStub)` |   
  
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
  
### listInsights(@Nullable InsightTypeName parent)
    
    
    public final RecommenderClient.ListInsightsPagedResponse listInsights(@Nullable InsightTypeName parent)

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       InsightTypeName parent =
           InsightTypeName.ofProjectLocationInsightTypeName(
               "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]");
       for (Insight element : recommenderClient.listInsights(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.InsightTypeName`  
Required. The container resource on which to execute the request. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `folders/[FOLDER_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> INSIGHT_TYPE_ID refers to supported insight types: <https://cloud.google.com/recommender/docs/insights/insight-types>.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListInsightsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListInsightsPagedResponse)` |   
  
### listInsights(ListInsightsRequest request)
    
    
    public final RecommenderClient.ListInsightsPagedResponse listInsights(ListInsightsRequest request)

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       ListInsightsRequest request =
           ListInsightsRequest.newBuilder()
               .setParent(
                   InsightTypeName.ofProjectLocationInsightTypeName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Insight element : recommenderClient.listInsights(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInsightsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListInsightsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListInsightsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListInsightsPagedResponse)` |   
  
### listInsights(String parent)
    
    
    public final RecommenderClient.ListInsightsPagedResponse listInsights(String parent)

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String parent =
           InsightTypeName.ofProjectLocationInsightTypeName(
                   "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
               .toString();
       for (Insight element : recommenderClient.listInsights(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The container resource on which to execute the request. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `folders/[FOLDER_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> INSIGHT_TYPE_ID refers to supported insight types: <https://cloud.google.com/recommender/docs/insights/insight-types>.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListInsightsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListInsightsPagedResponse)` |   
  
### listInsightsCallable()
    
    
    public final UnaryCallable<ListInsightsRequest,ListInsightsResponse> listInsightsCallable()

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       ListInsightsRequest request =
           ListInsightsRequest.newBuilder()
               .setParent(
                   InsightTypeName.ofProjectLocationInsightTypeName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListInsightsResponse response = recommenderClient.listInsightsCallable().call(request);
         for (Insight element : response.getInsightsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInsightsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListInsightsRequest),[ListInsightsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListInsightsResponse)>` |   
  
### listInsightsPagedCallable()
    
    
    public final UnaryCallable<ListInsightsRequest,RecommenderClient.ListInsightsPagedResponse> listInsightsPagedCallable()

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       ListInsightsRequest request =
           ListInsightsRequest.newBuilder()
               .setParent(
                   InsightTypeName.ofProjectLocationInsightTypeName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Insight> future = recommenderClient.listInsightsPagedCallable().futureCall(request);
       // Do something.
       for (Insight element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInsightsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListInsightsRequest),[ListInsightsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListInsightsPagedResponse)>` |   
  
### listRecommendations(@Nullable RecommenderName parent)
    
    
    public final RecommenderClient.ListRecommendationsPagedResponse listRecommendations(@Nullable RecommenderName parent)

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommenderName parent =
           RecommenderName.ofProjectLocationRecommenderName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]");
       for (Recommendation element : recommenderClient.listRecommendations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommenderName`  
Required. The container resource on which to execute the request. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> RECOMMENDER_ID refers to supported recommenders: <https://cloud.google.com/recommender/docs/recommenders>.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListRecommendationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListRecommendationsPagedResponse)` |   
  
### listRecommendations(@Nullable RecommenderName parent, String filter)
    
    
    public final RecommenderClient.ListRecommendationsPagedResponse listRecommendations(@Nullable RecommenderName parent, String filter)

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommenderName parent =
           RecommenderName.ofProjectLocationRecommenderName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]");
       String filter = "filter-1274492040";
       for (Recommendation element :
           recommenderClient.listRecommendations(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommenderName`  
Required. The container resource on which to execute the request. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> RECOMMENDER_ID refers to supported recommenders: <https://cloud.google.com/recommender/docs/recommenders>.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Filter expression to restrict the recommendations returned. Supported filter fields: 

  * `state_info.state`


  * `recommenderSubtype`


  * `priority`


  * `targetResources`

Examples: 

  * `stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED`


  * `recommenderSubtype = REMOVE_ROLE OR recommenderSubtype = REPLACE_ROLE`


  * `priority = P1 OR priority = P2`


  * `targetResources : //compute.googleapis.com/projects/1234/zones/us-central1-a/instances/instance-1`


  * `stateInfo.state = ACTIVE AND (priority = P1 OR priority = P2)`

The max allowed filter length is 500 characters. (These expressions are based on the filter language described at <https://google.aip.dev/160>)  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListRecommendationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListRecommendationsPagedResponse)` |   
  
### listRecommendations(ListRecommendationsRequest request)
    
    
    public final RecommenderClient.ListRecommendationsPagedResponse listRecommendations(ListRecommendationsRequest request)

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       ListRecommendationsRequest request =
           ListRecommendationsRequest.newBuilder()
               .setParent(
                   RecommenderName.ofProjectLocationRecommenderName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Recommendation element : recommenderClient.listRecommendations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRecommendationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListRecommendationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListRecommendationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListRecommendationsPagedResponse)` |   
  
### listRecommendations(String parent)
    
    
    public final RecommenderClient.ListRecommendationsPagedResponse listRecommendations(String parent)

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String parent =
           RecommenderName.ofProjectLocationRecommenderName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
               .toString();
       for (Recommendation element : recommenderClient.listRecommendations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The container resource on which to execute the request. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> RECOMMENDER_ID refers to supported recommenders: <https://cloud.google.com/recommender/docs/recommenders>.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListRecommendationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListRecommendationsPagedResponse)` |   
  
### listRecommendations(String parent, String filter)
    
    
    public final RecommenderClient.ListRecommendationsPagedResponse listRecommendations(String parent, String filter)

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String parent =
           RecommenderName.ofProjectLocationRecommenderName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
               .toString();
       String filter = "filter-1274492040";
       for (Recommendation element :
           recommenderClient.listRecommendations(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The container resource on which to execute the request. Acceptable formats: 

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `projects/[PROJECT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `folders/[FOLDER_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`


  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> RECOMMENDER_ID refers to supported recommenders: <https://cloud.google.com/recommender/docs/recommenders>.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Filter expression to restrict the recommendations returned. Supported filter fields: 

  * `state_info.state`


  * `recommenderSubtype`


  * `priority`


  * `targetResources`

Examples: 

  * `stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED`


  * `recommenderSubtype = REMOVE_ROLE OR recommenderSubtype = REPLACE_ROLE`


  * `priority = P1 OR priority = P2`


  * `targetResources : //compute.googleapis.com/projects/1234/zones/us-central1-a/instances/instance-1`


  * `stateInfo.state = ACTIVE AND (priority = P1 OR priority = P2)`

The max allowed filter length is 500 characters. (These expressions are based on the filter language described at <https://google.aip.dev/160>)  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderClient.ListRecommendationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListRecommendationsPagedResponse)` |   
  
### listRecommendationsCallable()
    
    
    public final UnaryCallable<ListRecommendationsRequest,ListRecommendationsResponse> listRecommendationsCallable()

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       ListRecommendationsRequest request =
           ListRecommendationsRequest.newBuilder()
               .setParent(
                   RecommenderName.ofProjectLocationRecommenderName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRecommendationsResponse response =
             recommenderClient.listRecommendationsCallable().call(request);
         for (Recommendation element : response.getRecommendationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRecommendationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListRecommendationsRequest),[ListRecommendationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListRecommendationsResponse)>` |   
  
### listRecommendationsPagedCallable()
    
    
    public final UnaryCallable<ListRecommendationsRequest,RecommenderClient.ListRecommendationsPagedResponse> listRecommendationsPagedCallable()

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       ListRecommendationsRequest request =
           ListRecommendationsRequest.newBuilder()
               .setParent(
                   RecommenderName.ofProjectLocationRecommenderName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Recommendation> future =
           recommenderClient.listRecommendationsPagedCallable().futureCall(request);
       // Do something.
       for (Recommendation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRecommendationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.ListRecommendationsRequest),[ListRecommendationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderClient.ListRecommendationsPagedResponse)>` |   
  
### markInsightAccepted(@Nullable InsightName name, Map<String,String> stateMetadata, String etag)
    
    
    public final Insight markInsightAccepted(@Nullable InsightName name, Map<String,String> stateMetadata, String etag)

Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated.

MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       InsightName name =
           InsightName.ofProjectLocationInsightTypeInsightName(
               "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]");
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Insight response = recommenderClient.markInsightAccepted(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.InsightName`  
Required. Name of the insight.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Optional. State properties user wish to include with this state. Full replace of the current state_metadata.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Insight. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)` |   
  
### markInsightAccepted(MarkInsightAcceptedRequest request)
    
    
    public final Insight markInsightAccepted(MarkInsightAcceptedRequest request)

Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated.

MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkInsightAcceptedRequest request =
           MarkInsightAcceptedRequest.newBuilder()
               .setName(
                   InsightName.ofProjectLocationInsightTypeInsightName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       Insight response = recommenderClient.markInsightAccepted(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkInsightAcceptedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkInsightAcceptedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)` |   
  
### markInsightAccepted(String name, Map<String,String> stateMetadata, String etag)
    
    
    public final Insight markInsightAccepted(String name, Map<String,String> stateMetadata, String etag)

Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated.

MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           InsightName.ofProjectLocationInsightTypeInsightName(
                   "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]")
               .toString();
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Insight response = recommenderClient.markInsightAccepted(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the insight.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Optional. State properties user wish to include with this state. Full replace of the current state_metadata.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Insight. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)` |   
  
### markInsightAcceptedCallable()
    
    
    public final UnaryCallable<MarkInsightAcceptedRequest,Insight> markInsightAcceptedCallable()

Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated.

MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkInsightAcceptedRequest request =
           MarkInsightAcceptedRequest.newBuilder()
               .setName(
                   InsightName.ofProjectLocationInsightTypeInsightName(
                           "[PROJECT]", "[LOCATION]", "[INSIGHT_TYPE]", "[INSIGHT]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Insight> future =
           recommenderClient.markInsightAcceptedCallable().futureCall(request);
       // Do something.
       Insight response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkInsightAcceptedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkInsightAcceptedRequest),[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Insight)>` |   
  
### markRecommendationClaimed(@Nullable RecommendationName name, Map<String,String> stateMetadata, String etag)
    
    
    public final Recommendation markRecommendationClaimed(@Nullable RecommendationName name, Map<String,String> stateMetadata, String etag)

Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommendationName name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]");
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Recommendation response =
           recommenderClient.markRecommendationClaimed(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommendationName`  
Required. Name of the recommendation.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
State properties to include with this state. Overwrites any existing `state_metadata`. Keys must match the regex `/^a-z0-9{0,62}$/`. Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Recommendation. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationClaimed(MarkRecommendationClaimedRequest request)
    
    
    public final Recommendation markRecommendationClaimed(MarkRecommendationClaimedRequest request)

Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationClaimedRequest request =
           MarkRecommendationClaimedRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       Recommendation response = recommenderClient.markRecommendationClaimed(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationClaimedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationClaimedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationClaimed(String name, Map<String,String> stateMetadata, String etag)
    
    
    public final Recommendation markRecommendationClaimed(String name, Map<String,String> stateMetadata, String etag)

Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
               .toString();
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Recommendation response =
           recommenderClient.markRecommendationClaimed(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the recommendation.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
State properties to include with this state. Overwrites any existing `state_metadata`. Keys must match the regex `/^a-z0-9{0,62}$/`. Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Recommendation. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationClaimedCallable()
    
    
    public final UnaryCallable<MarkRecommendationClaimedRequest,Recommendation> markRecommendationClaimedCallable()

Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationClaimedRequest request =
           MarkRecommendationClaimedRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Recommendation> future =
           recommenderClient.markRecommendationClaimedCallable().futureCall(request);
       // Do something.
       Recommendation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkRecommendationClaimedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationClaimedRequest),[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)>` |   
  
### markRecommendationDismissed(MarkRecommendationDismissedRequest request)
    
    
    public final Recommendation markRecommendationDismissed(MarkRecommendationDismissedRequest request)

Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED.

MarkRecommendationDismissed can be applied to recommendations in ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationDismissedRequest request =
           MarkRecommendationDismissedRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       Recommendation response = recommenderClient.markRecommendationDismissed(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationDismissedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationDismissedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationDismissedCallable()
    
    
    public final UnaryCallable<MarkRecommendationDismissedRequest,Recommendation> markRecommendationDismissedCallable()

Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED.

MarkRecommendationDismissed can be applied to recommendations in ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationDismissedRequest request =
           MarkRecommendationDismissedRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Recommendation> future =
           recommenderClient.markRecommendationDismissedCallable().futureCall(request);
       // Do something.
       Recommendation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkRecommendationDismissedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationDismissedRequest),[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)>` |   
  
### markRecommendationFailed(@Nullable RecommendationName name, Map<String,String> stateMetadata, String etag)
    
    
    public final Recommendation markRecommendationFailed(@Nullable RecommendationName name, Map<String,String> stateMetadata, String etag)

Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommendationName name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]");
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Recommendation response =
           recommenderClient.markRecommendationFailed(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommendationName`  
Required. Name of the recommendation.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
State properties to include with this state. Overwrites any existing `state_metadata`. Keys must match the regex `/^a-z0-9{0,62}$/`. Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Recommendation. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationFailed(MarkRecommendationFailedRequest request)
    
    
    public final Recommendation markRecommendationFailed(MarkRecommendationFailedRequest request)

Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationFailedRequest request =
           MarkRecommendationFailedRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       Recommendation response = recommenderClient.markRecommendationFailed(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationFailedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationFailedRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationFailed(String name, Map<String,String> stateMetadata, String etag)
    
    
    public final Recommendation markRecommendationFailed(String name, Map<String,String> stateMetadata, String etag)

Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
               .toString();
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Recommendation response =
           recommenderClient.markRecommendationFailed(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the recommendation.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
State properties to include with this state. Overwrites any existing `state_metadata`. Keys must match the regex `/^a-z0-9{0,62}$/`. Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Recommendation. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationFailedCallable()
    
    
    public final UnaryCallable<MarkRecommendationFailedRequest,Recommendation> markRecommendationFailedCallable()

Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationFailedRequest request =
           MarkRecommendationFailedRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Recommendation> future =
           recommenderClient.markRecommendationFailedCallable().futureCall(request);
       // Do something.
       Recommendation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkRecommendationFailedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationFailedRequest),[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)>` |   
  
### markRecommendationSucceeded(@Nullable RecommendationName name, Map<String,String> stateMetadata, String etag)
    
    
    public final Recommendation markRecommendationSucceeded(@Nullable RecommendationName name, Map<String,String> stateMetadata, String etag)

Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommendationName name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
               "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]");
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Recommendation response =
           recommenderClient.markRecommendationSucceeded(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.recommender.v1.RecommendationName`  
Required. Name of the recommendation.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
State properties to include with this state. Overwrites any existing `state_metadata`. Keys must match the regex `/^a-z0-9{0,62}$/`. Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Recommendation. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationSucceeded(MarkRecommendationSucceededRequest request)
    
    
    public final Recommendation markRecommendationSucceeded(MarkRecommendationSucceededRequest request)

Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationSucceededRequest request =
           MarkRecommendationSucceededRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       Recommendation response = recommenderClient.markRecommendationSucceeded(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationSucceededRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationSucceededRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationSucceeded(String name, Map<String,String> stateMetadata, String etag)
    
    
    public final Recommendation markRecommendationSucceeded(String name, Map<String,String> stateMetadata, String etag)

Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       String name =
           RecommendationName.ofProjectLocationRecommenderRecommendationName(
                   "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
               .toString();
       Map<String, String> stateMetadata = new HashMap<>();
       String etag = "etag3123477";
       Recommendation response =
           recommenderClient.markRecommendationSucceeded(name, stateMetadata, etag);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the recommendation.  
`stateMetadata` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
State properties to include with this state. Overwrites any existing `state_metadata`. Keys must match the regex `/^a-z0-9{0,62}$/`. Values must match the regex `/^[a-zA-Z0-9_./-]{0,255}$/`.  
`etag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Fingerprint of the Recommendation. Provides optimistic locking.  
**Returns**  
---  
**Type** | **Description**  
`[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)` |   
  
### markRecommendationSucceededCallable()
    
    
    public final UnaryCallable<MarkRecommendationSucceededRequest,Recommendation> markRecommendationSucceededCallable()

Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified recommender.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       MarkRecommendationSucceededRequest request =
           MarkRecommendationSucceededRequest.newBuilder()
               .setName(
                   RecommendationName.ofProjectLocationRecommenderRecommendationName(
                           "[PROJECT]", "[LOCATION]", "[RECOMMENDER]", "[RECOMMENDATION]")
                       .toString())
               .putAllStateMetadata(new HashMap<String, String>())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Recommendation> future =
           recommenderClient.markRecommendationSucceededCallable().futureCall(request);
       // Do something.
       Recommendation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkRecommendationSucceededRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.MarkRecommendationSucceededRequest),[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.Recommendation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateInsightTypeConfig(InsightTypeConfig insightTypeConfig, FieldMask updateMask)
    
    
    public final InsightTypeConfig updateInsightTypeConfig(InsightTypeConfig insightTypeConfig, FieldMask updateMask)

Updates an InsightTypeConfig change. This will create a new revision of the config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       InsightTypeConfig insightTypeConfig = InsightTypeConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       InsightTypeConfig response =
           recommenderClient.updateInsightTypeConfig(insightTypeConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`insightTypeConfig` | `[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)`  
Required. The InsightTypeConfig to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)` |   
  
### updateInsightTypeConfig(UpdateInsightTypeConfigRequest request)
    
    
    public final InsightTypeConfig updateInsightTypeConfig(UpdateInsightTypeConfigRequest request)

Updates an InsightTypeConfig change. This will create a new revision of the config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       UpdateInsightTypeConfigRequest request =
           UpdateInsightTypeConfigRequest.newBuilder()
               .setInsightTypeConfig(InsightTypeConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       InsightTypeConfig response = recommenderClient.updateInsightTypeConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInsightTypeConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.UpdateInsightTypeConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)` |   
  
### updateInsightTypeConfigCallable()
    
    
    public final UnaryCallable<UpdateInsightTypeConfigRequest,InsightTypeConfig> updateInsightTypeConfigCallable()

Updates an InsightTypeConfig change. This will create a new revision of the config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       UpdateInsightTypeConfigRequest request =
           UpdateInsightTypeConfigRequest.newBuilder()
               .setInsightTypeConfig(InsightTypeConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<InsightTypeConfig> future =
           recommenderClient.updateInsightTypeConfigCallable().futureCall(request);
       // Do something.
       InsightTypeConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInsightTypeConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.UpdateInsightTypeConfigRequest),[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.InsightTypeConfig)>` |   
  
### updateRecommenderConfig(RecommenderConfig recommenderConfig, FieldMask updateMask)
    
    
    public final RecommenderConfig updateRecommenderConfig(RecommenderConfig recommenderConfig, FieldMask updateMask)

Updates a Recommender Config. This will create a new revision of the config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       RecommenderConfig recommenderConfig = RecommenderConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       RecommenderConfig response =
           recommenderClient.updateRecommenderConfig(recommenderConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recommenderConfig` | `[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)`  
Required. The RecommenderConfig to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)` |   
  
### updateRecommenderConfig(UpdateRecommenderConfigRequest request)
    
    
    public final RecommenderConfig updateRecommenderConfig(UpdateRecommenderConfigRequest request)

Updates a Recommender Config. This will create a new revision of the config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       UpdateRecommenderConfigRequest request =
           UpdateRecommenderConfigRequest.newBuilder()
               .setRecommenderConfig(RecommenderConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       RecommenderConfig response = recommenderClient.updateRecommenderConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.UpdateRecommenderConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)` |   
  
### updateRecommenderConfigCallable()
    
    
    public final UnaryCallable<UpdateRecommenderConfigRequest,RecommenderConfig> updateRecommenderConfigCallable()

Updates a Recommender Config. This will create a new revision of the config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RecommenderClient recommenderClient = RecommenderClient.create()) {
       UpdateRecommenderConfigRequest request =
           UpdateRecommenderConfigRequest.newBuilder()
               .setRecommenderConfig(RecommenderConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<RecommenderConfig> future =
           recommenderClient.updateRecommenderConfigCallable().futureCall(request);
       // Do something.
       RecommenderConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.UpdateRecommenderConfigRequest),[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1.RecommenderConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
