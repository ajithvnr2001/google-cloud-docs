---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceGrpc.AsyncService
title: Interface DataSubscriptionServiceGrpc.AsyncService (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:09.399298+00:00
---

# Interface DataSubscriptionServiceGrpc.AsyncService (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSubscriptionServiceGrpc.AsyncService (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public static interface DataSubscriptionServiceGrpc.AsyncService

Data Subscription Service that allows clients (e.g., Fitbit 3P applications, internal Fitbit Services) to manage their subscriber endpoints. This service provides CRUD APIs for subscribers, and also offers functionalities for subscriber verification and statistics.

## Methods 

### createSubscriber(CreateSubscriberRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createSubscriber(CreateSubscriberRequest request, StreamObserver<Operation> responseObserver)

Registers a new subscriber endpoint to receive notifications. A subscriber represents an application or service that wishes to receive data change notifications for users who have granted consent. **Endpoint Verification:** For a subscriber to be successfully created, the provided `endpoint_uri` must be a valid HTTPS endpoint and must pass an automated verification check. The backend will send two HTTP POST requests to the `endpoint_uri`:

  1. **Verification with Authorization:**
     * **Headers:** Includes `Content-Type: application/json` and `Authorization` (with the exact value from `CreateSubscriberPayload.endpoint_authorization.secret`).
     * **Body:** `{"type": "verification"}`
     * **Expected Response:** HTTP `201 Created`.
  2. **Verification without Authorization:**
     * **Headers:** Includes `Content-Type: application/json`. The `Authorization` header is OMITTED.
     * **Body:** `{"type": "verification"}`
     * **Expected Response:** HTTP `401 Unauthorized` or `403 Forbidden`. Both tests must pass for the subscriber creation to succeed. If verification fails, the operation will not be completed and an error will be returned. This process ensures the endpoint is reachable and correctly validates the `Authorization` header.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSubscription(CreateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)
    
    
    public default void createSubscription(CreateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)

Creates a subscription for a specific user to a specific subscriber. This method requires the subscriber to have a `SubscriptionCreatePolicy` set to `MANUAL` for the given data types.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)>`  
  
  
### deleteSubscriber(DeleteSubscriberRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSubscriber(DeleteSubscriberRequest request, StreamObserver<Operation> responseObserver)

Deletes a subscriber registration. This will stop all notifications to the subscriber's endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSubscription(DeleteSubscriptionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteSubscription(DeleteSubscriptionRequest request, StreamObserver<Empty> responseObserver)

Deletes a specific user subscription, stopping notifications for this user to this subscriber.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### listSubscribers(ListSubscribersRequest request, StreamObserver<ListSubscribersResponse> responseObserver)
    
    
    public default void listSubscribers(ListSubscribersRequest request, StreamObserver<ListSubscribersResponse> responseObserver)

Lists all subscribers registered within the owned Google Cloud Project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersResponse)>`  
  
  
### listSubscriptions(ListSubscriptionsRequest request, StreamObserver<ListSubscriptionsResponse> responseObserver)
    
    
    public default void listSubscriptions(ListSubscriptionsRequest request, StreamObserver<ListSubscriptionsResponse> responseObserver)

Lists all active subscriptions for a given subscriber. This can be filtered, for example, by user or data type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsResponse)>`  
  
  
### updateSubscriber(UpdateSubscriberRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateSubscriber(UpdateSubscriberRequest request, StreamObserver<Operation> responseObserver)

Updates the configuration of an existing subscriber, such as the endpoint URI or the data types it's interested in. **Endpoint Verification:** If the `endpoint_uri` or `endpoint_authorization` field is included in the `update_mask`, the backend will re-verify the endpoint. The verification process is the same as described in `CreateSubscriber`:

  1. **Verification with Authorization:** POST to the new or existing `endpoint_uri` with the new or existing `Authorization` secret. Expects HTTP `201 Created`.
  2. **Verification without Authorization:** POST to the `endpoint_uri` without the `Authorization` header. Expects HTTP `401 Unauthorized` or `403 Forbidden`. Both tests must pass using the potentially updated values for the subscriber update to succeed. If verification fails, the update will not be applied, and an error will be returned.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSubscription(UpdateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)
    
    
    public default void updateSubscription(UpdateSubscriptionRequest request, StreamObserver<Subscription> responseObserver)

Updates the data types for an existing user subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriptionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
