---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/pstest/
title: Cloud PubSub - Package cloud.google.com/go/pubsub/pstest (v1.51.1) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:02.988451+00:00
---

# Cloud PubSub - Package cloud.google.com/go/pubsub/pstest (v1.51.1)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/pstest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud PubSub - Package cloud.google.com/go/pubsub/pstest (v1.51.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.51.1 (latest)  1.51.0  1.50.4  1.49.0  1.48.1  1.47.0  1.46.0  1.45.3  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.2  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.1  1.26.0  1.25.1  1.24.0  1.23.1  1.22.2  1.21.1  1.20.0  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.2  1.11.0  1.10.3  1.9.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/pubsub/pstest). 

Package pstest provides a fake Cloud PubSub service for testing. It implements a simplified form of the service, suitable for unit tests. It may behave differently from the actual service in ways in which the service is non-deterministic or unspecified: timing, delivery order, etc. 

This package is EXPERIMENTAL and is subject to change without notice. 

See the example for usage.

## Functions 

### func ResetMinAckDeadline 
    
    
    func ResetMinAckDeadline()

ResetMinAckDeadline resets the minack deadline to the default.

### func SetMinAckDeadline 
    
    
    func SetMinAckDeadline(n [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))

SetMinAckDeadline changes the minack deadline to n. Must be greater than or equal to 1 second. Remember to reset this value to the default after your test changes it. Example usage:
    
    
    pstest.SetMinAckDeadlineSecs(1)
    defer pstest.ResetMinAckDeadlineSecs()
    

### func ValidateFilter 
    
    
    func ValidateFilter(filter [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

ValidateFilter validates if the filter string is parsable.

## GServer
    
    
    type GServer struct {
    	pb.UnimplementedPublisherServer
    	pb.UnimplementedSubscriberServer
    	pb.UnimplementedSchemaServiceServer
    	// contains filtered or unexported fields
    }

GServer is the underlying service implementor. It is not intended to be used directly.

### func (*GServer) Acknowledge 
    
    
    func (s *GServer) Acknowledge(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[AcknowledgeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_AcknowledgeRequest)) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

Acknowledge marks the message as acknowleged.

### func (*GServer) CommitSchema 
    
    
    func (s *GServer) CommitSchema(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[CommitSchemaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_CommitSchemaRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Schema), [error](https://pkg.go.dev/builtin#error))

CommitSchema commits a new schema revision.

### func (*GServer) CreateSchema 
    
    
    func (s *GServer) CreateSchema(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[CreateSchemaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_CreateSchemaRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Schema), [error](https://pkg.go.dev/builtin#error))

CreateSchema creates a new schema.

### func (*GServer) CreateSubscription 
    
    
    func (s *GServer) CreateSubscription(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), ps *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Subscription](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Subscription)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Subscription](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Subscription), [error](https://pkg.go.dev/builtin#error))

CreateSubscription creates a Pub/Sub subscription.

### func (*GServer) CreateTopic 
    
    
    func (s *GServer) CreateTopic(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), t *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Topic](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Topic)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Topic](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Topic), [error](https://pkg.go.dev/builtin#error))

CreateTopic creates a topic.

### func (*GServer) DeleteSchema 
    
    
    func (s *GServer) DeleteSchema(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[DeleteSchemaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_DeleteSchemaRequest)) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

DeleteSchema deletes an existing schema.

### func (*GServer) DeleteSchemaRevision 
    
    
    func (s *GServer) DeleteSchemaRevision(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[DeleteSchemaRevisionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_DeleteSchemaRevisionRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Schema), [error](https://pkg.go.dev/builtin#error))

DeleteSchemaRevision deletes a schema revision.

### func (*GServer) DeleteSubscription 
    
    
    func (s *GServer) DeleteSubscription(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[DeleteSubscriptionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_DeleteSubscriptionRequest)) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

DeleteSubscription deletes the Pub/Sub subscription.

### func (*GServer) DeleteTopic 
    
    
    func (s *GServer) DeleteTopic(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[DeleteTopicRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_DeleteTopicRequest)) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

DeleteTopic deletes the topic.

### func (*GServer) DetachSubscription 
    
    
    func (s *GServer) DetachSubscription(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[DetachSubscriptionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_DetachSubscriptionRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[DetachSubscriptionResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_DetachSubscriptionResponse), [error](https://pkg.go.dev/builtin#error))

DetachSubscription detaches the subscription from the topic.

### func (*GServer) GetSchema 
    
    
    func (s *GServer) GetSchema(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[GetSchemaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_GetSchemaRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Schema), [error](https://pkg.go.dev/builtin#error))

GetSchema gets an existing schema details.

### func (*GServer) GetSubscription 
    
    
    func (s *GServer) GetSubscription(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[GetSubscriptionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_GetSubscriptionRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Subscription](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Subscription), [error](https://pkg.go.dev/builtin#error))

GetSubscription fetches an existing Pub/Sub subscription details.

### func (*GServer) GetTopic 
    
    
    func (s *GServer) GetTopic(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[GetTopicRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_GetTopicRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Topic](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Topic), [error](https://pkg.go.dev/builtin#error))

GetTopic gets a Pub/Sub topic.

### func (*GServer) ListSchemaRevisions 
    
    
    func (s *GServer) ListSchemaRevisions(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListSchemaRevisionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListSchemaRevisionsRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListSchemaRevisionsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListSchemaRevisionsResponse), [error](https://pkg.go.dev/builtin#error))

ListSchemaRevisions lists the schema revisions.

### func (*GServer) ListSchemas 
    
    
    func (s *GServer) ListSchemas(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListSchemasRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListSchemasRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListSchemasResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListSchemasResponse), [error](https://pkg.go.dev/builtin#error))

ListSchemas lists the available schemas in this server.

### func (*GServer) ListSubscriptions 
    
    
    func (s *GServer) ListSubscriptions(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListSubscriptionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListSubscriptionsRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListSubscriptionsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListSubscriptionsResponse), [error](https://pkg.go.dev/builtin#error))

ListSubscriptions lists the Pub/Sub subscriptions in this server.

### func (*GServer) ListTopicSubscriptions 
    
    
    func (s *GServer) ListTopicSubscriptions(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListTopicSubscriptionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListTopicSubscriptionsRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListTopicSubscriptionsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListTopicSubscriptionsResponse), [error](https://pkg.go.dev/builtin#error))

ListTopicSubscriptions lists the subscriptions associated with a topic.

### func (*GServer) ListTopics 
    
    
    func (s *GServer) ListTopics(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListTopicsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListTopicsRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ListTopicsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ListTopicsResponse), [error](https://pkg.go.dev/builtin#error))

ListTopics lists the topics in this server.

### func (*GServer) ModifyAckDeadline 
    
    
    func (s *GServer) ModifyAckDeadline(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ModifyAckDeadlineRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ModifyAckDeadlineRequest)) (*[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty), [error](https://pkg.go.dev/builtin#error))

ModifyAckDeadline modifies the ack deadline of the message.

### func (*GServer) Publish 
    
    
    func (s *GServer) Publish(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[PublishRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_PublishRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[PublishResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_PublishResponse), [error](https://pkg.go.dev/builtin#error))

Publish sends a message to the topic.

### func (*GServer) Pull 
    
    
    func (s *GServer) Pull(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[PullRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_PullRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[PullResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_PullResponse), [error](https://pkg.go.dev/builtin#error))

Pull returns a list of unacknowledged messages from a subscription.

### func (*GServer) RollbackSchema 
    
    
    func (s *GServer) RollbackSchema(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[RollbackSchemaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_RollbackSchemaRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Schema), [error](https://pkg.go.dev/builtin#error))

RollbackSchema rolls back the current schema to a previous revision by copying and creating a new revision.

### func (*GServer) Seek 
    
    
    func (s *GServer) Seek(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[SeekRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_SeekRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[SeekResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_SeekResponse), [error](https://pkg.go.dev/builtin#error))

Seek updates a subscription to a specific point in time or snapshot.

### func (*GServer) StreamingPull 
    
    
    func (s *GServer) StreamingPull(sps [pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Subscriber_StreamingPullServer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Subscriber_StreamingPullServer)) [error](https://pkg.go.dev/builtin#error)

StreamingPull return a stream to pull messages from a subscription.

### func (*GServer) UpdateSubscription 
    
    
    func (s *GServer) UpdateSubscription(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[UpdateSubscriptionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_UpdateSubscriptionRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Subscription](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Subscription), [error](https://pkg.go.dev/builtin#error))

UpdateSubscription updates an existing Pub/Sub subscription.

### func (*GServer) UpdateTopic 
    
    
    func (s *GServer) UpdateTopic(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[UpdateTopicRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_UpdateTopicRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[Topic](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_Topic), [error](https://pkg.go.dev/builtin#error))

UpdateTopic updates the Pub/Sub topic.

### func (*GServer) ValidateMessage 
    
    
    func (s *GServer) ValidateMessage(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ValidateMessageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ValidateMessageRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ValidateMessageResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ValidateMessageResponse), [error](https://pkg.go.dev/builtin#error))

ValidateMessage mocks the ValidateMessage call but only checks that the schema definition to validate the message against is not empty.

### func (*GServer) ValidateSchema 
    
    
    func (s *GServer) ValidateSchema(_ [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ValidateSchemaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ValidateSchemaRequest)) (*[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[ValidateSchemaResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_ValidateSchemaResponse), [error](https://pkg.go.dev/builtin#error))

ValidateSchema mocks the ValidateSchema call but only checks that the schema definition is not empty.

## Message
    
    
    type Message struct {
    	ID          [string](https://pkg.go.dev/builtin#string)
    	Data        [][byte](https://pkg.go.dev/builtin#byte)
    	Attributes  map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)
    	PublishTime time.Time
    	Deliveries  [int](https://pkg.go.dev/builtin#int)      // number of times delivery of the message was attempted
    	Acks        [int](https://pkg.go.dev/builtin#int)      // number of acks received from clients
    	Modacks     []Modack // modacks received by server for this message
    	OrderingKey [string](https://pkg.go.dev/builtin#string)
    	Topic       [string](https://pkg.go.dev/builtin#string)
    	// contains filtered or unexported fields
    }

A Message is a message that was published to the server.

## Modack
    
    
    type Modack struct {
    	AckID       [string](https://pkg.go.dev/builtin#string)
    	AckDeadline [int32](https://pkg.go.dev/builtin#int32)
    	ReceivedAt  time.Time
    }

Modack represents a modack sent to the server.

## Reactor
    
    
    type Reactor interface {
    	// React handles the message types and returns results.  If "handled" is false,
    	// then the test server will ignore the results and continue to the next reactor
    	// or the original handler.
    	React(_ interface{}) (handled [bool](https://pkg.go.dev/builtin#bool), ret interface{}, err [error](https://pkg.go.dev/builtin#error))
    }

Reactor is an interface to allow reaction function to a certain call.

## ReactorOptions
    
    
    type ReactorOptions map[[string](https://pkg.go.dev/builtin#string)][]Reactor

ReactorOptions is a map that Server uses to look up reactors. Key is the function name, value is array of reactor for the function.

## Server
    
    
    type Server struct {
    	Addr    [string](https://pkg.go.dev/builtin#string)  // The address that the server is listening on.
    	GServer GServer // Not intended to be used directly.
    	// contains filtered or unexported fields
    }

Server is a fake Pub/Sub server.

### func NewServer 
    
    
    func NewServer(opts ...ServerReactorOption) *Server

NewServer creates a new fake server running in the current process.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsub/pstest"
    	"google.golang.org/api/option"
    	"google.golang.org/grpc"
    	"google.golang.org/grpc/credentials/insecure"
    )
    
    func main() {
    	ctx := context.Background()
    	// Start a fake server running locally.
    	srv := pstest.NewServer()
    	defer srv.Close()
    	// Connect to the server without using TLS.
    	conn, err := grpc.Dial(srv.Addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer conn.Close()
    	// Use the connection when creating a pubsub client.
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, "project", option.WithGRPCConn(conn))
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	_ = client // TODO: Use the client.
    }
    

### func NewServerWithAddress 
    
    
    func NewServerWithAddress(address [string](https://pkg.go.dev/builtin#string), opts ...ServerReactorOption) *Server

NewServerWithAddress creates a new fake server running in the current process at the specified address (host and port).

### func NewServerWithCallback 
    
    
    func NewServerWithCallback(port [int](https://pkg.go.dev/builtin#int), callback func(*[grpc](https://pkg.go.dev/google.golang.org/grpc).[Server](https://pkg.go.dev/google.golang.org/grpc#Server)), opts ...ServerReactorOption) *Server

NewServerWithCallback creates new fake server running in the current process at the specified port. Before starting the server, the provided callback is called to allow caller to register additional fakes into grpc server.

### func NewServerWithPort 
    
    
    func NewServerWithPort(port [int](https://pkg.go.dev/builtin#int), opts ...ServerReactorOption) *Server

NewServerWithPort creates a new fake server running in the current process at the specified port.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsub/pstest"
    	"google.golang.org/api/option"
    	"google.golang.org/grpc"
    	"google.golang.org/grpc/credentials/insecure"
    )
    
    func main() {
    	ctx := context.Background()
    	// Start a fake server running locally at 9001.
    	srv := pstest.NewServerWithPort(9001)
    	defer srv.Close()
    	// Connect to the server without using TLS.
    	conn, err := grpc.Dial(srv.Addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer conn.Close()
    	// Use the connection when creating a pubsub client.
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, "project", option.WithGRPCConn(conn))
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer client.Close()
    	_ = client // TODO: Use the client.
    }
    

### func (*Server) AddPublishResponse 
    
    
    func (s *Server) AddPublishResponse(pbr *[pb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb).[PublishResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/apiv1/pubsubpb#cloud_google_com_go_pubsub_apiv1_pubsubpb_PublishResponse), err [error](https://pkg.go.dev/builtin#error))

AddPublishResponse adds a new publish response to the channel used for responding to publish requests.

### func (*Server) ClearMessages 
    
    
    func (s *Server) ClearMessages()

ClearMessages removes all published messages from internal containers.

### func (*Server) Close 
    
    
    func (s *Server) Close() [error](https://pkg.go.dev/builtin#error)

Close shuts down the server and releases all resources.

### func (*Server) Message 
    
    
    func (s *Server) Message(id [string](https://pkg.go.dev/builtin#string)) *Message

Message returns the message with the given ID, or nil if no message with that ID was published.

### func (*Server) Messages 
    
    
    func (s *Server) Messages() []*Message

Messages returns information about all messages ever published.

### func (*Server) Publish 
    
    
    func (s *Server) Publish(topic [string](https://pkg.go.dev/builtin#string), data [][byte](https://pkg.go.dev/builtin#byte), attrs map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)) [string](https://pkg.go.dev/builtin#string)

Publish behaves as if the Publish RPC was called with a message with the given data and attrs. It returns the ID of the message. The topic will be created if it doesn't exist.

Publish panics if there is an error, which is appropriate for testing.

### func (*Server) PublishOrdered 
    
    
    func (s *Server) PublishOrdered(topic [string](https://pkg.go.dev/builtin#string), data [][byte](https://pkg.go.dev/builtin#byte), attrs map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string), orderingKey [string](https://pkg.go.dev/builtin#string)) [string](https://pkg.go.dev/builtin#string)

PublishOrdered behaves as if the Publish RPC was called with a message with the given data, attrs and ordering key. It returns the ID of the message. The topic will be created if it doesn't exist.

PublishOrdered panics if there is an error, which is appropriate for testing.

### func (*Server) ResetPublishResponses 
    
    
    func (s *Server) ResetPublishResponses(size [int](https://pkg.go.dev/builtin#int))

ResetPublishResponses resets the buffered publishResponses channel with a new buffered channel with the given size.

### func (*Server) SetAutoPublishResponse 
    
    
    func (s *Server) SetAutoPublishResponse(autoPublishResponse [bool](https://pkg.go.dev/builtin#bool))

SetAutoPublishResponse controls whether to automatically respond to messages published or to use user-added responses from the publishResponses channel.

### func (*Server) SetStreamTimeout 
    
    
    func (s *Server) SetStreamTimeout(d [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))

SetStreamTimeout sets the amount of time a stream will be active before it shuts itself down. This mimics the real service's behavior of closing streams after 30 minutes. If SetStreamTimeout is never called or is passed zero, streams never shut down.

### func (*Server) SetTimeNowFunc 
    
    
    func (s *Server) SetTimeNowFunc(f func() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time))

SetTimeNowFunc registers f as a function to be used instead of time.Now for this server.

### func (*Server) Wait 
    
    
    func (s *Server) Wait()

Wait blocks until all server activity has completed.

## ServerReactorOption
    
    
    type ServerReactorOption struct {
    	FuncName [string](https://pkg.go.dev/builtin#string)
    	Reactor  Reactor
    }

ServerReactorOption is options passed to the server for reactor creation.

### func WithErrorInjection 
    
    
    func WithErrorInjection(funcName [string](https://pkg.go.dev/builtin#string), code [codes](https://pkg.go.dev/google.golang.org/grpc/codes).[Code](https://pkg.go.dev/google.golang.org/grpc/codes#Code), msg [string](https://pkg.go.dev/builtin#string)) ServerReactorOption

WithErrorInjection creates a ServerReactorOption that injects error with defined status code and message for a certain function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-20 UTC."],[],[]] 
