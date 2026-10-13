---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommenderGrpc.AsyncService
title: Interface RecommenderGrpc.AsyncService (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:15.740261+00:00
---

# Interface RecommenderGrpc.AsyncService (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommenderGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RecommenderGrpc.AsyncService (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.7  2.4.1  2.3.0  2.2.0  2.1.5 
    
    
    public static interface RecommenderGrpc.AsyncService

Provides insights and recommendations for cloud customers for various categories like performance optimization, cost savings, reliability, feature discovery, etc. Insights and recommendations are generated automatically based on analysis of user resources, configuration and monitoring metrics.

## Methods 

### getInsight(GetInsightRequest request, StreamObserver<Insight> responseObserver)
    
    
    public default void getInsight(GetInsightRequest request, StreamObserver<Insight> responseObserver)

Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInsightRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.GetInsightRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Insight)>`  
  
  
### getInsightTypeConfig(GetInsightTypeConfigRequest request, StreamObserver<InsightTypeConfig> responseObserver)
    
    
    public default void getInsightTypeConfig(GetInsightTypeConfigRequest request, StreamObserver<InsightTypeConfig> responseObserver)

Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInsightTypeConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.GetInsightTypeConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.InsightTypeConfig)>`  
  
  
### getRecommendation(GetRecommendationRequest request, StreamObserver<Recommendation> responseObserver)
    
    
    public default void getRecommendation(GetRecommendationRequest request, StreamObserver<Recommendation> responseObserver)

Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRecommendationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.GetRecommendationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Recommendation)>`  
  
  
### getRecommenderConfig(GetRecommenderConfigRequest request, StreamObserver<RecommenderConfig> responseObserver)
    
    
    public default void getRecommenderConfig(GetRecommenderConfigRequest request, StreamObserver<RecommenderConfig> responseObserver)

Gets the requested Recommender Config. There is only one instance of the config for each Recommender.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRecommenderConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.GetRecommenderConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommenderConfig)>`  
  
  
### listInsightTypes(ListInsightTypesRequest request, StreamObserver<ListInsightTypesResponse> responseObserver)
    
    
    public default void listInsightTypes(ListInsightTypesRequest request, StreamObserver<ListInsightTypesResponse> responseObserver)

Lists available InsightTypes. No IAM permissions are required.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInsightTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListInsightTypesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInsightTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListInsightTypesResponse)>`  
  
  
### listInsights(ListInsightsRequest request, StreamObserver<ListInsightsResponse> responseObserver)
    
    
    public default void listInsights(ListInsightsRequest request, StreamObserver<ListInsightsResponse> responseObserver)

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInsightsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListInsightsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInsightsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListInsightsResponse)>`  
  
  
### listRecommendations(ListRecommendationsRequest request, StreamObserver<ListRecommendationsResponse> responseObserver)
    
    
    public default void listRecommendations(ListRecommendationsRequest request, StreamObserver<ListRecommendationsResponse> responseObserver)

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRecommendationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListRecommendationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRecommendationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListRecommendationsResponse)>`  
  
  
### listRecommenders(ListRecommendersRequest request, StreamObserver<ListRecommendersResponse> responseObserver)
    
    
    public default void listRecommenders(ListRecommendersRequest request, StreamObserver<ListRecommendersResponse> responseObserver)

Lists all available Recommenders. No IAM permissions are required.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRecommendersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListRecommendersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRecommendersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.ListRecommendersResponse)>`  
  
  
### markInsightAccepted(MarkInsightAcceptedRequest request, StreamObserver<Insight> responseObserver)
    
    
    public default void markInsightAccepted(MarkInsightAcceptedRequest request, StreamObserver<Insight> responseObserver)

Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkInsightAcceptedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.MarkInsightAcceptedRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Insight](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Insight)>`  
  
  
### markRecommendationClaimed(MarkRecommendationClaimedRequest request, StreamObserver<Recommendation> responseObserver)
    
    
    public default void markRecommendationClaimed(MarkRecommendationClaimedRequest request, StreamObserver<Recommendation> responseObserver)

Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationClaimedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Recommendation)>`  
  
  
### markRecommendationFailed(MarkRecommendationFailedRequest request, StreamObserver<Recommendation> responseObserver)
    
    
    public default void markRecommendationFailed(MarkRecommendationFailedRequest request, StreamObserver<Recommendation> responseObserver)

Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationFailedRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Recommendation)>`  
  
  
### markRecommendationSucceeded(MarkRecommendationSucceededRequest request, StreamObserver<Recommendation> responseObserver)
    
    
    public default void markRecommendationSucceeded(MarkRecommendationSucceededRequest request, StreamObserver<Recommendation> responseObserver)

Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkRecommendationSucceededRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Recommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.Recommendation)>`  
  
  
### updateInsightTypeConfig(UpdateInsightTypeConfigRequest request, StreamObserver<InsightTypeConfig> responseObserver)
    
    
    public default void updateInsightTypeConfig(UpdateInsightTypeConfigRequest request, StreamObserver<InsightTypeConfig> responseObserver)

Updates an InsightTypeConfig change. This will create a new revision of the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInsightTypeConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.UpdateInsightTypeConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InsightTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.InsightTypeConfig)>`  
  
  
### updateRecommenderConfig(UpdateRecommenderConfigRequest request, StreamObserver<RecommenderConfig> responseObserver)
    
    
    public default void updateRecommenderConfig(UpdateRecommenderConfigRequest request, StreamObserver<RecommenderConfig> responseObserver)

Updates a Recommender Config. This will create a new revision of the config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.UpdateRecommenderConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RecommenderConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommenderConfig)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
