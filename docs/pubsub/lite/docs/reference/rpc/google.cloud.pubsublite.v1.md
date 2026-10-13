---
url: https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1
title: Package google.cloud.pubsublite.v1 \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:45.415643+00:00
---

# Package google.cloud.pubsublite.v1  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)



Send feedback 

#  Package google.cloud.pubsublite.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AdminService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.AdminService)` (interface)
  * `[CursorService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CursorService)` (interface)
  * `[KafkaService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.KafkaService)` (interface)
  * `[PartitionAssignmentService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignmentService)` (interface)
  * `[PublisherService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PublisherService)` (interface)
  * `[SubscriberService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SubscriberService)` (interface)
  * `[TopicStatsService](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.TopicStatsService)` (interface)
  * `[AttributeValues](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.AttributeValues)` (message)
  * `[CommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CommitCursorRequest)` (message)
  * `[CommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CommitCursorResponse)` (message)
  * `[ComputeHeadCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeHeadCursorRequest)` (message)
  * `[ComputeHeadCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeHeadCursorResponse)` (message)
  * `[ComputeMessageStatsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeMessageStatsRequest)` (message)
  * `[ComputeMessageStatsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeMessageStatsResponse)` (message)
  * `[ComputeTimeCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeTimeCursorRequest)` (message)
  * `[ComputeTimeCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeTimeCursorResponse)` (message)
  * `[CreateReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CreateReservationRequest)` (message)
  * `[CreateSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CreateSubscriptionRequest)` (message)
  * `[CreateTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CreateTopicRequest)` (message)
  * `[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)` (message)
  * `[DeleteReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.DeleteReservationRequest)` (message)
  * `[DeleteSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.DeleteSubscriptionRequest)` (message)
  * `[DeleteTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.DeleteTopicRequest)` (message)
  * `[ExportConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig)` (message)
  * `[ExportConfig.PubSubConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig.PubSubConfig)` (message)
  * `[ExportConfig.State](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig.State)` (enum)
  * `[FlowControlRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.FlowControlRequest)` (message)
  * `[GetReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetReservationRequest)` (message)
  * `[GetSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetSubscriptionRequest)` (message)
  * `[GetTopicPartitionsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetTopicPartitionsRequest)` (message)
  * `[GetTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetTopicRequest)` (message)
  * `[InitialCommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialCommitCursorRequest)` (message)
  * `[InitialCommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialCommitCursorResponse)` (message)
  * `[InitialPartitionAssignmentRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialPartitionAssignmentRequest)` (message)
  * `[InitialPublishRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialPublishRequest)` (message)
  * `[InitialPublishResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialPublishResponse)` (message)
  * `[InitialSubscribeRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialSubscribeRequest)` (message)
  * `[InitialSubscribeResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialSubscribeResponse)` (message)
  * `[ListPartitionCursorsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListPartitionCursorsRequest)` (message)
  * `[ListPartitionCursorsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListPartitionCursorsResponse)` (message)
  * `[ListReservationTopicsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationTopicsRequest)` (message)
  * `[ListReservationTopicsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationTopicsResponse)` (message)
  * `[ListReservationsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationsRequest)` (message)
  * `[ListReservationsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationsResponse)` (message)
  * `[ListSubscriptionsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListSubscriptionsRequest)` (message)
  * `[ListSubscriptionsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListSubscriptionsResponse)` (message)
  * `[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicSubscriptionsRequest)` (message)
  * `[ListTopicSubscriptionsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicSubscriptionsResponse)` (message)
  * `[ListTopicsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicsRequest)` (message)
  * `[ListTopicsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicsResponse)` (message)
  * `[MessagePublishRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessagePublishRequest)` (message)
  * `[MessagePublishResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessagePublishResponse)` (message)
  * `[MessagePublishResponse.CursorRange](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessagePublishResponse.CursorRange)` (message)
  * `[MessageResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessageResponse)` (message)
  * `[OpenKafkaStreamRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.OpenKafkaStreamRequest)` (message)
  * `[OpenKafkaStreamResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.OpenKafkaStreamResponse)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.OperationMetadata)` (message)
  * `[PartitionAssignment](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignment)` (message)
  * `[PartitionAssignmentAck](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignmentAck)` (message)
  * `[PartitionAssignmentRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignmentRequest)` (message)
  * `[PartitionCursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionCursor)` (message)
  * `[PubSubMessage](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PubSubMessage)` (message)
  * `[PublishRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PublishRequest)` (message)
  * `[PublishResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PublishResponse)` (message)
  * `[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)` (message)
  * `[SeekRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekRequest)` (message)
  * `[SeekRequest.NamedTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekRequest.NamedTarget)` (enum)
  * `[SeekResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekResponse)` (message)
  * `[SeekSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekSubscriptionRequest)` (message)
  * `[SeekSubscriptionRequest.NamedTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekSubscriptionRequest.NamedTarget)` (enum)
  * `[SeekSubscriptionResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekSubscriptionResponse)` (message)
  * `[SequencedCommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SequencedCommitCursorRequest)` (message)
  * `[SequencedCommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SequencedCommitCursorResponse)` (message)
  * `[SequencedMessage](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SequencedMessage)` (message)
  * `[StreamingCommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.StreamingCommitCursorRequest)` (message)
  * `[StreamingCommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.StreamingCommitCursorResponse)` (message)
  * `[SubscribeRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SubscribeRequest)` (message)
  * `[SubscribeResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SubscribeResponse)` (message)
  * `[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)` (message)
  * `[Subscription.DeliveryConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription.DeliveryConfig)` (message)
  * `[Subscription.DeliveryConfig.DeliveryRequirement](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription.DeliveryConfig.DeliveryRequirement)` (enum)
  * `[TimeTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.TimeTarget)` (message)
  * `[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)` (message)
  * `[Topic.PartitionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.PartitionConfig)` (message)
  * `[Topic.PartitionConfig.Capacity](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.PartitionConfig.Capacity)` (message)
  * `[Topic.ReservationConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.ReservationConfig)` (message)
  * `[Topic.RetentionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.RetentionConfig)` (message)
  * `[TopicPartitions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.TopicPartitions)` (message)
  * `[UpdateReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.UpdateReservationRequest)` (message)
  * `[UpdateSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.UpdateSubscriptionRequest)` (message)
  * `[UpdateTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.UpdateTopicRequest)` (message)



## AdminService

The service that a client application uses to manage topics and subscriptions, such creating, listing, and deleting topics and subscriptions.

CreateReservation  
---  
` rpc CreateReservation(`[CreateReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CreateReservationRequest)`) returns (`[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)`) ` Creates a new reservation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateSubscription  
---  
` rpc CreateSubscription(`[CreateSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CreateSubscriptionRequest)`) returns (`[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)`) ` Creates a new subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateTopic  
---  
` rpc CreateTopic(`[CreateTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CreateTopicRequest)`) returns (`[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)`) ` Creates a new topic.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteReservation  
---  
` rpc DeleteReservation(`[DeleteReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.DeleteReservationRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified reservation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteSubscription  
---  
` rpc DeleteSubscription(`[DeleteSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.DeleteSubscriptionRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteTopic  
---  
` rpc DeleteTopic(`[DeleteTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.DeleteTopicRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified topic.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetReservation  
---  
` rpc GetReservation(`[GetReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetReservationRequest)`) returns (`[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)`) ` Returns the reservation configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetSubscription  
---  
` rpc GetSubscription(`[GetSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetSubscriptionRequest)`) returns (`[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)`) ` Returns the subscription configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetTopic  
---  
` rpc GetTopic(`[GetTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetTopicRequest)`) returns (`[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)`) ` Returns the topic configuration.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetTopicPartitions  
---  
` rpc GetTopicPartitions(`[GetTopicPartitionsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.GetTopicPartitionsRequest)`) returns (`[TopicPartitions](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.TopicPartitions)`) ` Returns the partition information for the requested topic.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListReservationTopics  
---  
` rpc ListReservationTopics(`[ListReservationTopicsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationTopicsRequest)`) returns (`[ListReservationTopicsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationTopicsResponse)`) ` Lists the topics attached to the specified reservation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListReservations  
---  
` rpc ListReservations(`[ListReservationsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationsRequest)`) returns (`[ListReservationsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListReservationsResponse)`) ` Returns the list of reservations for the given project.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListSubscriptions  
---  
` rpc ListSubscriptions(`[ListSubscriptionsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListSubscriptionsRequest)`) returns (`[ListSubscriptionsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListSubscriptionsResponse)`) ` Returns the list of subscriptions for the given project.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListTopicSubscriptions  
---  
` rpc ListTopicSubscriptions(`[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicSubscriptionsRequest)`) returns (`[ListTopicSubscriptionsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicSubscriptionsResponse)`) ` Lists the subscriptions attached to the specified topic.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListTopics  
---  
` rpc ListTopics(`[ListTopicsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicsRequest)`) returns (`[ListTopicsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListTopicsResponse)`) ` Returns the list of topics for the given project.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
SeekSubscription  
---  
` rpc SeekSubscription(`[SeekSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekSubscriptionRequest)`) returns (`[Operation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Performs an out-of-band seek for a subscription to a specified target, which may be timestamps or named positions within the message backlog. Seek translates these targets to cursors for each partition and orchestrates subscribers to start consuming messages from these seek cursors.If an operation is returned, the seek has been registered and subscribers will eventually receive messages from the seek cursors (i.e. eventual consistency), as long as they are using a minimum supported client library version and not a system that tracks cursors independently of Pub/Sub Lite (e.g. Apache Beam, Dataflow, Spark). The seek operation will fail for unsupported clients.If clients would like to know when subscribers react to the seek (or not), they can poll the operation. The seek operation will succeed and complete once subscribers are ready to receive messages from the seek cursors for all partitions of the topic. This means that the seek operation will not complete until all subscribers come online.If the previous seek operation has not yet completed, it will be aborted and the new invocation of seek will supersede it.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateReservation  
---  
` rpc UpdateReservation(`[UpdateReservationRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.UpdateReservationRequest)`) returns (`[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)`) ` Updates properties of the specified reservation.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateSubscription  
---  
` rpc UpdateSubscription(`[UpdateSubscriptionRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.UpdateSubscriptionRequest)`) returns (`[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)`) ` Updates properties of the specified subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateTopic  
---  
` rpc UpdateTopic(`[UpdateTopicRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.UpdateTopicRequest)`) returns (`[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)`) ` Updates properties of the specified topic.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## CursorService

The service that a subscriber client application uses to manage committed cursors while receiving messsages. A cursor represents a subscriber's progress within a topic partition for a given subscription.

CommitCursor  
---  
` rpc CommitCursor(`[CommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CommitCursorRequest)`) returns (`[CommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.CommitCursorResponse)`) ` Updates the committed cursor.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListPartitionCursors  
---  
` rpc ListPartitionCursors(`[ListPartitionCursorsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListPartitionCursorsRequest)`) returns (`[ListPartitionCursorsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ListPartitionCursorsResponse)`) ` Returns all committed cursor information for a subscription.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
StreamingCommitCursor  
---  
` rpc StreamingCommitCursor(`[StreamingCommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.StreamingCommitCursorRequest)`) returns (`[StreamingCommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.StreamingCommitCursorResponse)`) ` Establishes a stream with the server for managing committed cursors.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## KafkaService

A service for pseudo-requests made while using the kafka wire protocol TCP stream.

This service is exposition only: calling it directly will have no effect and will not succeed.

OpenKafkaStream  
---  
` rpc OpenKafkaStream(`[OpenKafkaStreamRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.OpenKafkaStreamRequest)`) returns (`[OpenKafkaStreamResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.OpenKafkaStreamResponse)`) ` Request made when opening a new kafka stream. Calling this method directly has no effect.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## PartitionAssignmentService

The service that a subscriber client application uses to determine which partitions it should connect to.

AssignPartitions  
---  
` rpc AssignPartitions(`[PartitionAssignmentRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignmentRequest)`) returns (`[PartitionAssignment](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignment)`) ` Assign partitions for this client to handle for the specified subscription.The client must send an InitialPartitionAssignmentRequest first. The server will then send at most one unacknowledged PartitionAssignment outstanding on the stream at a time. The client should send a PartitionAssignmentAck after updating the partitions it is connected to to reflect the new assignment.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## PublisherService

The service that a publisher client application uses to publish messages to topics. Published messages are retained by the service for the duration of the retention period configured for the respective topic, and are delivered to subscriber clients upon request (via the `SubscriberService`).

Publish  
---  
` rpc Publish(`[PublishRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PublishRequest)`) returns (`[PublishResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PublishResponse)`) ` Establishes a stream with the server for publishing messages. Once the stream is initialized, the client publishes messages by sending publish requests on the stream. The server responds with a PublishResponse for each PublishRequest sent by the client, in the same order that the requests were sent. Note that multiple PublishRequests can be in flight simultaneously, but they will be processed by the server in the order that they are sent by the client on a given stream.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## SubscriberService

The service that a subscriber client application uses to receive messages from subscriptions.

Subscribe  
---  
` rpc Subscribe(`[SubscribeRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SubscribeRequest)`) returns (`[SubscribeResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SubscribeResponse)`) ` Establishes a stream with the server for receiving messages.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## TopicStatsService

This service allows users to get stats about messages in their topic.

ComputeHeadCursor  
---  
` rpc ComputeHeadCursor(`[ComputeHeadCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeHeadCursorRequest)`) returns (`[ComputeHeadCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeHeadCursorResponse)`) ` Compute the head cursor for the partition. The head cursor's offset is guaranteed to be less than or equal to all messages which have not yet been acknowledged as published, and greater than the offset of any message whose publish has already been acknowledged. It is zero if there have never been messages in the partition.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ComputeMessageStats  
---  
` rpc ComputeMessageStats(`[ComputeMessageStatsRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeMessageStatsRequest)`) returns (`[ComputeMessageStatsResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeMessageStatsResponse)`) ` Compute statistics about a range of messages in a given topic and partition.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ComputeTimeCursor  
---  
` rpc ComputeTimeCursor(`[ComputeTimeCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeTimeCursorRequest)`) returns (`[ComputeTimeCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ComputeTimeCursorResponse)`) ` Compute the corresponding cursor for a publish or event time in a topic partition.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## AttributeValues

The values associated with a key of an attribute.

Fields  
---  
`values[]` |  `bytes` The list of values associated with a key.  
  
## CommitCursorRequest

Request for CommitCursor.

Fields  
---  
`subscription` |  `string` The subscription for which to update the cursor. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `subscription`:

  * `pubsublite.subscriptions.setCursor`

  
`partition` |  `int64` The partition for which to update the cursor. Partitions are zero indexed, so `partition` must be in the range [0, topic.num_partitions).  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The new value for the committed cursor.  
  
## CommitCursorResponse

Response for CommitCursor.

## ComputeHeadCursorRequest

Compute the current head cursor for a partition.

Fields  
---  
`topic` |  `string` Required. The topic for which we should compute the head cursor. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `topic`:

  * `pubsublite.topics.computeHeadCursor`

  
`partition` |  `int64` Required. The partition for which we should compute the head cursor.  
  
## ComputeHeadCursorResponse

Response containing the head cursor for the requested topic and partition.

Fields  
---  
`head_cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The head cursor.  
  
## ComputeMessageStatsRequest

Compute statistics about a range of messages in a given topic and partition.

Fields  
---  
`topic` |  `string` Required. The topic for which we should compute message stats. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `topic`:

  * `pubsublite.topics.computeMessageStats`

  
`partition` |  `int64` Required. The partition for which we should compute message stats.  
`start_cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The inclusive start of the range.  
`end_cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The exclusive end of the range. The range is empty if end_cursor <= start_cursor. Specifying a start_cursor before the first message and an end_cursor after the last message will retrieve all messages.  
  
## ComputeMessageStatsResponse

Response containing stats for messages in the requested topic and partition.

Fields  
---  
`message_count` |  `int64` The count of messages.  
`message_bytes` |  `int64` The number of quota bytes accounted to these messages.  
`minimum_publish_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The minimum publish timestamp across these messages. Note that publish timestamps within a partition are not guaranteed to be non-decreasing. The timestamp will be unset if there are no messages.  
`minimum_event_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The minimum event timestamp across these messages. For the purposes of this computation, if a message does not have an event time, we use the publish time. The timestamp will be unset if there are no messages.  
  
## ComputeTimeCursorRequest

Compute the corresponding cursor for a publish or event time in a topic partition.

Fields  
---  
`topic` |  `string` Required. The topic for which we should compute the cursor. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `topic`:

  * `pubsublite.topics.computeTimeCursor`

  
`partition` |  `int64` Required. The partition for which we should compute the cursor.  
`target` |  ``[TimeTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.TimeTarget)`` Required. The target publish or event time. Specifying a future time will return an unset cursor.  
  
## ComputeTimeCursorResponse

Response containing the cursor corresponding to a publish or event time in a topic partition.

Fields  
---  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` If present, the cursor references the first message with time greater than or equal to the specified target time. If such a message cannot be found, the cursor will be unset (i.e. `cursor` is not present).  
  
## CreateReservationRequest

Request for CreateReservation.

Fields  
---  
`parent` |  `string` Required. The parent location in which to create the reservation. Structured like `projects/{project_number}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.reservations.create`

  
`reservation` |  ``[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)`` Required. Configuration of the reservation to create. Its `name` field is ignored.  
`reservation_id` |  `string` Required. The ID to use for the reservation, which will become the final component of the reservation's name.This value is structured like: `my-reservation-name`.  
  
## CreateSubscriptionRequest

Request for CreateSubscription.

Fields  
---  
`parent` |  `string` Required. The parent location in which to create the subscription. Structured like `projects/{project_number}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.subscriptions.create`

  
`subscription` |  ``[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)`` Required. Configuration of the subscription to create. Its `name` field is ignored. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `subscription`:

  * `pubsublite.topics.subscribe`

  
`subscription_id` |  `string` Required. The ID to use for the subscription, which will become the final component of the subscription's name.This value is structured like: `my-sub-name`.  
`skip_backlog` |  `bool` If true, the newly created subscription will only receive messages published after the subscription was created. Otherwise, the entire message backlog will be received on the subscription. Defaults to false.  
  
## CreateTopicRequest

Request for CreateTopic.

Fields  
---  
`parent` |  `string` Required. The parent location in which to create the topic. Structured like `projects/{project_number}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.topics.create`

  
`topic` |  ``[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)`` Required. Configuration of the topic to create. Its `name` field is ignored.  
`topic_id` |  `string` Required. The ID to use for the topic, which will become the final component of the topic's name.This value is structured like: `my-topic-name`.  
  
## Cursor

A cursor that describes the position of a message within a topic partition.

Fields  
---  
`offset` |  `int64` The offset of a message within a topic partition. Must be greater than or equal 0.  
  
## DeleteReservationRequest

Request for DeleteReservation.

Fields  
---  
`name` |  `string` Required. The name of the reservation to delete. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.reservations.delete`

  
  
## DeleteSubscriptionRequest

Request for DeleteSubscription.

Fields  
---  
`name` |  `string` Required. The name of the subscription to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.subscriptions.delete`

  
  
## DeleteTopicRequest

Request for DeleteTopic.

Fields  
---  
`name` |  `string` Required. The name of the topic to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.topics.delete`

  
  
## ExportConfig

Configuration for a Pub/Sub Lite subscription that writes messages to a destination. User subscriber clients must not connect to this subscription.

Fields  
---  
`desired_state` |  ``[State](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig.State)`` The desired state of this export. Setting this to values other than `ACTIVE` and `PAUSED` will result in an error.  
`current_state` |  ``[State](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig.State)`` Output only. The current state of the export, which may be different to the desired state due to errors. This field is output only.  
`dead_letter_topic` |  `string` Optional. The name of an optional Pub/Sub Lite topic to publish messages that can not be exported to the destination. For example, the message can not be published to the Pub/Sub service because it does not satisfy the constraints documented at <https://cloud.google.com/pubsub/docs/publisher>.Structured like: projects/{project_number}/locations/{location}/topics/{topic_id}. Must be within the same project and location as the subscription. The topic may be changed or removed.  
Union field `destination`. The destination to export to. Required. `destination` can be only one of the following:  
`pubsub_config` |  ``[PubSubConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig.PubSubConfig)`` Messages are automatically written from the Pub/Sub Lite topic associated with this subscription to a Pub/Sub topic.  
  
## PubSubConfig

Configuration for exporting to a Pub/Sub topic.

Fields  
---  
`topic` |  `string` The name of the Pub/Sub topic. Structured like: projects/{project_number}/topics/{topic_id}. The topic may be changed.  
  
## State

The desired export state.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`ACTIVE` | Messages are being exported.  
`PAUSED` | Exporting messages is suspended.  
`PERMISSION_DENIED` | Messages cannot be exported due to permission denied errors. Output only.  
`NOT_FOUND` | Messages cannot be exported due to missing resources. Output only.  
  
## FlowControlRequest

Request to grant tokens to the server, requesting delivery of messages when they become available.

Fields  
---  
`allowed_messages` |  `int64` The number of message tokens to grant. Must be greater than or equal to 0.  
`allowed_bytes` |  `int64` The number of byte tokens to grant. Must be greater than or equal to 0.  
  
## GetReservationRequest

Request for GetReservation.

Fields  
---  
`name` |  `string` Required. The name of the reservation whose configuration to return. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.reservations.get`

  
  
## GetSubscriptionRequest

Request for GetSubscription.

Fields  
---  
`name` |  `string` Required. The name of the subscription whose configuration to return. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.subscriptions.get`

  
  
## GetTopicPartitionsRequest

Request for GetTopicPartitions.

Fields  
---  
`name` |  `string` Required. The topic whose partition information to return. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.topics.getPartitions`

  
  
## GetTopicRequest

Request for GetTopic.

Fields  
---  
`name` |  `string` Required. The name of the topic whose configuration to return. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.topics.get`

  
  
## InitialCommitCursorRequest

The first streaming request that must be sent on a newly-opened stream. The client must wait for the response before sending subsequent requests on the stream.

Fields  
---  
`subscription` |  `string` The subscription for which to manage committed cursors. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `subscription`:

  * `pubsublite.subscriptions.setCursor`

  
`partition` |  `int64` The partition for which to manage committed cursors. Partitions are zero indexed, so `partition` must be in the range [0, topic.num_partitions).  
  
## InitialCommitCursorResponse

Response to an InitialCommitCursorRequest.

## InitialPartitionAssignmentRequest

The first request that must be sent on a newly-opened stream. The client must wait for the response before sending subsequent requests on the stream.

Fields  
---  
`subscription` |  `string` The subscription name. Structured like: projects//locations//subscriptions/ Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `subscription`:

  * `pubsublite.subscriptions.subscribe`

  
`client_id` |  `bytes` An opaque, unique client identifier. This field must be exactly 16 bytes long and is interpreted as an unsigned 128 bit integer. Other size values will be rejected and the stream will be failed with a non-retryable error.This field is large enough to fit a uuid from standard uuid algorithms like uuid1 or uuid4, which should be used to generate this number. The same identifier should be reused following disconnections with retryable stream errors.  
  
## InitialPublishRequest

The first request that must be sent on a newly-opened stream.

Fields  
---  
`topic` |  `string` The topic to which messages will be written. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `topic`:

  * `pubsublite.topics.publish`

  
`partition` |  `int64` The partition within the topic to which messages will be written. Partitions are zero indexed, so `partition` must be in the range [0, topic.num_partitions).  
`client_id` |  `bytes` Unique identifier for a publisher client. If set, enables publish idempotency within a publisher client session.The length of this field must be exactly 16 bytes long and should be populated with a 128 bit uuid, generated by standard uuid algorithms like uuid1 or uuid4. The same identifier should be reused following disconnections with retryable stream errors.  
  
## InitialPublishResponse

Response to an InitialPublishRequest.

## InitialSubscribeRequest

The first request that must be sent on a newly-opened stream. The client must wait for the response before sending subsequent requests on the stream.

Fields  
---  
`subscription` |  `string` The subscription from which to receive messages. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `subscription`:

  * `pubsublite.subscriptions.subscribe`

  
`partition` |  `int64` The partition from which to receive messages. Partitions are zero indexed, so `partition` must be in the range [0, topic.num_partitions).  
`initial_location` |  ``[SeekRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekRequest)`` Optional. Initial target location within the message backlog. If not set, messages will be delivered from the commit cursor for the given subscription and partition.  
  
## InitialSubscribeResponse

Response to an InitialSubscribeRequest.

Fields  
---  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The cursor from which the subscriber will start receiving messages once flow control tokens become available.  
  
## ListPartitionCursorsRequest

Request for ListPartitionCursors.

Fields  
---  
`parent` |  `string` Required. The subscription for which to retrieve cursors. Structured like `projects/{project_number}/locations/{location}/subscriptions/{subscription_id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.subscriptions.getCursor`

  
`page_size` |  `int32` The maximum number of cursors to return. The service may return fewer than this value. If unset or zero, all cursors for the parent will be returned.  
`page_token` |  `string` A page token, received from a previous `ListPartitionCursors` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListPartitionCursors` must match the call that provided the page token.  
  
## ListPartitionCursorsResponse

Response for ListPartitionCursors

Fields  
---  
`partition_cursors[]` |  ``[PartitionCursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionCursor)`` The partition cursors from this request.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListReservationTopicsRequest

Request for ListReservationTopics.

Fields  
---  
`name` |  `string` Required. The name of the reservation whose topics to list. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.reservations.listTopics`

  
`page_size` |  `int32` The maximum number of topics to return. The service may return fewer than this value. If unset or zero, all topics for the given reservation will be returned.  
`page_token` |  `string` A page token, received from a previous `ListReservationTopics` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListReservationTopics` must match the call that provided the page token.  
  
## ListReservationTopicsResponse

Response for ListReservationTopics.

Fields  
---  
`topics[]` |  `string` The names of topics attached to the reservation. The order of the topics is unspecified.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results.  
  
## ListReservationsRequest

Request for ListReservations.

Fields  
---  
`parent` |  `string` Required. The parent whose reservations are to be listed. Structured like `projects/{project_number}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.reservations.list`

  
`page_size` |  `int32` The maximum number of reservations to return. The service may return fewer than this value. If unset or zero, all reservations for the parent will be returned.  
`page_token` |  `string` A page token, received from a previous `ListReservations` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListReservations` must match the call that provided the page token.  
  
## ListReservationsResponse

Response for ListReservations.

Fields  
---  
`reservations[]` |  ``[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)`` The list of reservation in the requested parent. The order of the reservations is unspecified.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results.  
  
## ListSubscriptionsRequest

Request for ListSubscriptions.

Fields  
---  
`parent` |  `string` Required. The parent whose subscriptions are to be listed. Structured like `projects/{project_number}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.subscriptions.list`

  
`page_size` |  `int32` The maximum number of subscriptions to return. The service may return fewer than this value. If unset or zero, all subscriptions for the parent will be returned.  
`page_token` |  `string` A page token, received from a previous `ListSubscriptions` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListSubscriptions` must match the call that provided the page token.  
  
## ListSubscriptionsResponse

Response for ListSubscriptions.

Fields  
---  
`subscriptions[]` |  ``[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)`` The list of subscriptions in the requested parent. The order of the subscriptions is unspecified.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results.  
  
## ListTopicSubscriptionsRequest

Request for ListTopicSubscriptions.

Fields  
---  
`name` |  `string` Required. The name of the topic whose subscriptions to list. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.topics.listSubscriptions`

  
`page_size` |  `int32` The maximum number of subscriptions to return. The service may return fewer than this value. If unset or zero, all subscriptions for the given topic will be returned.  
`page_token` |  `string` A page token, received from a previous `ListTopicSubscriptions` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListTopicSubscriptions` must match the call that provided the page token.  
  
## ListTopicSubscriptionsResponse

Response for ListTopicSubscriptions.

Fields  
---  
`subscriptions[]` |  `string` The names of subscriptions attached to the topic. The order of the subscriptions is unspecified.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results.  
  
## ListTopicsRequest

Request for ListTopics.

Fields  
---  
`parent` |  `string` Required. The parent whose topics are to be listed. Structured like `projects/{project_number}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.topics.list`

  
`page_size` |  `int32` The maximum number of topics to return. The service may return fewer than this value. If unset or zero, all topics for the parent will be returned.  
`page_token` |  `string` A page token, received from a previous `ListTopics` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListTopics` must match the call that provided the page token.  
  
## ListTopicsResponse

Response for ListTopics.

Fields  
---  
`topics[]` |  ``[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)`` The list of topic in the requested parent. The order of the topics is unspecified.  
`next_page_token` |  `string` A token that can be sent as `page_token` to retrieve the next page of results. If this field is omitted, there are no more results.  
  
## MessagePublishRequest

Request to publish messages to the topic.

Fields  
---  
`messages[]` |  ``[PubSubMessage](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PubSubMessage)`` The messages to publish.  
`first_sequence_number` |  `int64` The sequence number corresponding to the first message in `messages`. Messages within a batch are ordered and the sequence numbers of all subsequent messages in the batch are assumed to be incremental.Sequence numbers are assigned at the message level and the first message published in a publisher client session must have a sequence number of 0. All messages must have contiguous sequence numbers, which uniquely identify the messages accepted by the publisher client. Since messages are ordered, the client only needs to specify the sequence number of the first message in a published batch. The server deduplicates messages with the same sequence number from the same publisher `client_id`.  
  
## MessagePublishResponse

Response to a MessagePublishRequest.

Fields  
---  
`start_cursor  
**(deprecated)**` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` This item is deprecated!DEPRECATED: Superseded by cursor_ranges.The cursor of the first published message in the batch. The cursors for any remaining messages in the batch are guaranteed to be sequential.  
`cursor_ranges[]` |  ``[CursorRange](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessagePublishResponse.CursorRange)`` Cursors for messages published in the batch. There will exist multiple ranges when cursors are not contiguous within the batch.The cursor ranges may not account for all messages in the batch when publish idempotency is enabled. A missing range indicates that cursors could not be determined for messages within the range, as they were deduplicated and the necessary data was not available at publish time. These messages will have offsets when received by a subscriber.  
  
## CursorRange

Cursors for a subrange of published messages.

Fields  
---  
`start_cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The cursor of the message at the start index. The cursors for remaining messages up to the end index (exclusive) are sequential.  
`start_index` |  `int32` Index of the message in the published batch that corresponds to the start cursor. Inclusive.  
`end_index` |  `int32` Index of the last message in this range. Exclusive.  
  
## MessageResponse

Response containing a list of messages. Upon delivering a MessageResponse to the client, the server: * Updates the stream's delivery cursor to one greater than the cursor of the last message in the list. * Subtracts the total number of bytes and messages from the tokens available to the server.

Fields  
---  
`messages[]` |  ``[SequencedMessage](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SequencedMessage)`` Messages from the topic partition.  
  
## OpenKafkaStreamRequest

Request for OpenKafkaStream.

Fields  
---  
`parent` |  `string` Required. The parent path specified as `projects/{project_id}/locations/{location_id}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `pubsublite.locations.openKafkaStream`

  
  
## OpenKafkaStreamResponse

Response for OpenKafkaStream.

## OperationMetadata

Metadata for long running operations.

Fields  
---  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the operation was created.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the operation finished running. Not set if the operation has not completed.  
`target` |  `string` Resource path for the target of the operation. For example, targets of seeks are subscription resources, structured like: projects/{project_number}/locations/{location}/subscriptions/{subscription_id}  
`verb` |  `string` Name of the verb executed by the operation.  
  
## PartitionAssignment

PartitionAssignments should not race with acknowledgements. There should be exactly one unacknowledged PartitionAssignment at a time. If not, the client must break the stream.

Fields  
---  
`partitions[]` |  `int64` The list of partition numbers this subscriber is assigned to.  
  
## PartitionAssignmentAck

Acknowledge receipt and handling of the previous assignment. If not sent within a short period after receiving the assignment, partitions may remain unassigned for a period of time until the client is known to be inactive, after which time the server will break the stream.

## PartitionAssignmentRequest

A request on the PartitionAssignment stream.

Fields  
---  
Union field `request`. The type of request this is. `request` can be only one of the following:  
`initial` |  ``[InitialPartitionAssignmentRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialPartitionAssignmentRequest)`` Initial request on the stream.  
`ack` |  ``[PartitionAssignmentAck](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PartitionAssignmentAck)`` Acknowledgement of a partition assignment.  
  
## PartitionCursor

A pair of a Cursor and the partition it is for.

Fields  
---  
`partition` |  `int64` The partition this is for.  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The value of the cursor.  
  
## PubSubMessage

A message that is published by publishers and delivered to subscribers.

Fields  
---  
`key` |  `bytes` The key used for routing messages to partitions or for compaction (e.g., keep the last N messages per key). If the key is empty, the message is routed to an arbitrary partition.  
`data` |  `bytes` The payload of the message.  
`attributes` |  `map<string, `[AttributeValues](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.AttributeValues)`>` Optional attributes that can be used for message metadata/headers.  
`event_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` An optional, user-specified event time.  
  
## PublishRequest

Request sent from the client to the server on a stream.

Fields  
---  
Union field `request_type`. The type of request this is. `request_type` can be only one of the following:  
`initial_request` |  ``[InitialPublishRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialPublishRequest)`` Initial request on the stream.  
`message_publish_request` |  ``[MessagePublishRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessagePublishRequest)`` Request to publish messages.  
  
## PublishResponse

Response to a PublishRequest.

Fields  
---  
Union field `response_type`. The type of response this is. `response_type` can be only one of the following:  
`initial_response` |  ``[InitialPublishResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialPublishResponse)`` Initial response on the stream.  
`message_response` |  ``[MessagePublishResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessagePublishResponse)`` Response to publishing messages.  
  
## Reservation

Metadata about a reservation resource.

Fields  
---  
`name` |  `string` The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id}  
`throughput_capacity` |  `int64` The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages.Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually.  
  
## SeekRequest

Request to update the stream's delivery cursor based on the given target. Resets the server available tokens to 0. SeekRequests past head result in stream breakage.

SeekRequests may not be sent while another SeekRequest is outstanding (i.e., has not received a SeekResponse) on the same stream.

Fields  
---  
Union field `target`. The target to seek to. Must be set. `target` can be only one of the following:  
`named_target` |  ``[NamedTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekRequest.NamedTarget)`` A named target.  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` A target corresponding to the cursor, pointing to anywhere in the topic partition.  
  
## NamedTarget

A special target in the partition that takes no other parameters.

Enums  
---  
`NAMED_TARGET_UNSPECIFIED` | Default value. This value is unused.  
`HEAD` | A target corresponding to the most recently published message in the partition.  
`COMMITTED_CURSOR` | A target corresponding to the committed cursor for the given subscription and topic partition.  
  
## SeekResponse

Response to a SeekRequest.

Fields  
---  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The new delivery cursor for the current stream.  
  
## SeekSubscriptionRequest

Request for SeekSubscription.

Fields  
---  
`name` |  `string` Required. The name of the subscription to seek. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.subscriptions.seek`

  
Union field `target`. The target to seek to. Must be set. `target` can be only one of the following:  
`named_target` |  ``[NamedTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekSubscriptionRequest.NamedTarget)`` Seek to a named position with respect to the message backlog.  
`time_target` |  ``[TimeTarget](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.TimeTarget)`` Seek to the first message whose publish or event time is greater than or equal to the specified query time. If no such message can be located, will seek to the end of the message backlog.  
  
## NamedTarget

A named position with respect to the message backlog.

Enums  
---  
`NAMED_TARGET_UNSPECIFIED` | Unspecified named target. Do not use.  
`TAIL` | Seek to the oldest retained message.  
`HEAD` | Seek past all recently published messages, skipping the entire message backlog.  
  
## SeekSubscriptionResponse

Response for SeekSubscription long running operation.

## SequencedCommitCursorRequest

Streaming request to update the committed cursor. Subsequent SequencedCommitCursorRequests override outstanding ones.

Fields  
---  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The new value for the committed cursor.  
  
## SequencedCommitCursorResponse

Response to a SequencedCommitCursorRequest.

Fields  
---  
`acknowledged_commits` |  `int64` The number of outstanding SequencedCommitCursorRequests acknowledged by this response. Note that SequencedCommitCursorRequests are acknowledged in the order that they are received.  
  
## SequencedMessage

A message that has been stored and sequenced by the Pub/Sub Lite system.

Fields  
---  
`cursor` |  ``[Cursor](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Cursor)`` The position of a message within the partition where it is stored.  
`publish_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time when the message was received by the server when it was first published.  
`message` |  ``[PubSubMessage](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.PubSubMessage)`` The user message.  
`size_bytes` |  `int64` The size in bytes of this message for flow control and quota purposes.  
  
## StreamingCommitCursorRequest

A request sent from the client to the server on a stream.

Fields  
---  
Union field `request`. The type of request this is. `request` can be only one of the following:  
`initial` |  ``[InitialCommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialCommitCursorRequest)`` Initial request on the stream.  
`commit` |  ``[SequencedCommitCursorRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SequencedCommitCursorRequest)`` Request to commit a new cursor value.  
  
## StreamingCommitCursorResponse

Response to a StreamingCommitCursorRequest.

Fields  
---  
Union field `request`. The type of request this is. `request` can be only one of the following:  
`initial` |  ``[InitialCommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialCommitCursorResponse)`` Initial response on the stream.  
`commit` |  ``[SequencedCommitCursorResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SequencedCommitCursorResponse)`` Response to committing a new cursor value.  
  
## SubscribeRequest

A request sent from the client to the server on a stream.

Fields  
---  
Union field `request`. The type of request this is. `request` can be only one of the following:  
`initial` |  ``[InitialSubscribeRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialSubscribeRequest)`` Initial request on the stream.  
`seek` |  ``[SeekRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekRequest)`` Request to update the stream's delivery cursor.  
`flow_control` |  ``[FlowControlRequest](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.FlowControlRequest)`` Request to grant tokens to the server,  
  
## SubscribeResponse

Response to SubscribeRequest.

Fields  
---  
Union field `response`. The type of response this is. `response` can be only one of the following:  
`initial` |  ``[InitialSubscribeResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.InitialSubscribeResponse)`` Initial response on the stream.  
`seek` |  ``[SeekResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.SeekResponse)`` Response to a Seek operation.  
`messages` |  ``[MessageResponse](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.MessageResponse)`` Response containing messages from the topic partition.  
  
## Subscription

Metadata about a subscription resource.

Fields  
---  
`name` |  `string` The name of the subscription. Structured like: projects/{project_number}/locations/{location}/subscriptions/{subscription_id}  
`topic` |  `string` The name of the topic this subscription is attached to. Structured like: projects/{project_number}/locations/{location}/topics/{topic_id}  
`delivery_config` |  ``[DeliveryConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription.DeliveryConfig)`` The settings for this subscription's message delivery.  
`export_config` |  ``[ExportConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.ExportConfig)`` If present, messages are automatically written from the Pub/Sub Lite topic associated with this subscription to a destination.  
  
## DeliveryConfig

The settings for a subscription's message delivery.

Fields  
---  
`delivery_requirement` |  ``[DeliveryRequirement](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription.DeliveryConfig.DeliveryRequirement)`` The DeliveryRequirement for this subscription.  
  
## DeliveryRequirement

When this subscription should send messages to subscribers relative to messages persistence in storage. For details, see [Creating Lite subscriptions](https://cloud.google.com/pubsub/lite/docs/subscriptions#creating_lite_subscriptions).

Enums  
---  
`DELIVERY_REQUIREMENT_UNSPECIFIED` | Default value. This value is unused.  
`DELIVER_IMMEDIATELY` | The server does not wait for a published message to be successfully written to storage before delivering it to subscribers.  
`DELIVER_AFTER_STORED` | The server will not deliver a published message to subscribers until the message has been successfully written to storage. This will result in higher end-to-end latency, but consistent delivery.  
  
## TimeTarget

A target publish or event time. Can be used for seeking to or retrieving the corresponding cursor.

Fields  
---  
Union field `time`. The type of message time to query. `time` can be only one of the following:  
`publish_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Request the cursor of the first message with publish time greater than or equal to `publish_time`. All messages thereafter are guaranteed to have publish times >= `publish_time`.  
`event_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Request the cursor of the first message with event time greater than or equal to `event_time`. If messages are missing an event time, the publish time is used as a fallback. As event times are user supplied, subsequent messages may have event times less than `event_time` and should be filtered by the client, if necessary.  
  
## Topic

Metadata about a topic resource.

Fields  
---  
`name` |  `string` The name of the topic. Structured like: projects/{project_number}/locations/{location}/topics/{topic_id}  
`partition_config` |  ``[PartitionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.PartitionConfig)`` The settings for this topic's partitions.  
`retention_config` |  ``[RetentionConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.RetentionConfig)`` The settings for this topic's message retention.  
`reservation_config` |  ``[ReservationConfig](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.ReservationConfig)`` The settings for this topic's Reservation usage.  
  
## PartitionConfig

The settings for a topic's partitions.

Fields  
---  
`count` |  `int64` The number of partitions in the topic. Must be at least 1.Once a topic has been created the number of partitions can be increased but not decreased. Message ordering is not guaranteed across a topic resize. For more information see <https://cloud.google.com/pubsub/lite/docs/topics#scaling_capacity>  
Union field `dimension`. The throughput dimension of this topic. `dimension` can be only one of the following:  
`scale  
**(deprecated)**` |  `int32` This item is deprecated!DEPRECATED: Use capacity instead which can express a superset of configurations.Every partition in the topic is allocated throughput equivalent to `scale` times the standard partition throughput (4 MiB/s). This is also reflected in the cost of this topic; a topic with `scale` of 2 and count of 10 is charged for 20 partitions. This value must be in the range [1,4].  
`capacity` |  ``[Capacity](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic.PartitionConfig.Capacity)`` The capacity configuration.  
  
## Capacity

The throughput capacity configuration for each partition.

Fields  
---  
`publish_mib_per_sec` |  `int32` Publish throughput capacity per partition in MiB/s. Must be >= 4 and <= 16.  
`subscribe_mib_per_sec` |  `int32` Subscribe throughput capacity per partition in MiB/s. Must be >= 4 and <= 32.  
  
## ReservationConfig

The settings for this topic's Reservation usage.

Fields  
---  
`throughput_reservation` |  `string` The Reservation to use for this topic's throughput capacity. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `throughputReservation`:

  * `pubsublite.reservations.attachTopic`

  
  
## RetentionConfig

The settings for a topic's message retention.

Fields  
---  
`per_partition_bytes` |  `int64` The provisioned storage, in bytes, per partition. If the number of bytes stored in any of the topic's partitions grows beyond this value, older messages will be dropped to make room for newer ones, regardless of the value of `period`.  
`period` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` How long a published message is retained. If unset, messages will be retained as long as the bytes retained for each partition is below `per_partition_bytes`.  
  
## TopicPartitions

Response for GetTopicPartitions.

Fields  
---  
`partition_count` |  `int64` The number of partitions in the topic.  
  
## UpdateReservationRequest

Request for UpdateReservation.

Fields  
---  
`reservation` |  ``[Reservation](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Reservation)`` Required. The reservation to update. Its `name` field must be populated. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `reservation`:

  * `pubsublite.reservations.update`

  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. A mask specifying the reservation fields to change.  
  
## UpdateSubscriptionRequest

Request for UpdateSubscription.

Fields  
---  
`subscription` |  ``[Subscription](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Subscription)`` Required. The subscription to update. Its `name` field must be populated. Topic field must not be populated. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `subscription`:

  * `pubsublite.subscriptions.update`

  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. A mask specifying the subscription fields to change.  
  
## UpdateTopicRequest

Request for UpdateTopic.

Fields  
---  
`topic` |  ``[Topic](https://docs.cloud.google.com/pubsub/lite/docs/reference/rpc/google.cloud.pubsublite.v1#google.cloud.pubsublite.v1.Topic)`` Required. The topic to update. Its `name` field must be populated. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `topic`:

  * `pubsublite.topics.update`

  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. A mask specifying the topic fields to change.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
