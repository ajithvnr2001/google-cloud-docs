---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-subscriber-exactly-once/
title: v1 Subscribe with exactly once delivery (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:23.953181+00:00
---

# v1 Subscribe with exactly once delivery (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-subscriber-exactly-once/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Subscribe with exactly once delivery (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Subscribe with exactly once delivery

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"google.golang.org/api/option"
    )
    
    // receiveMessagesWithExactlyOnceDeliveryEnabled instantiates a subscriber client.
    // This differs from regular subscribing since you must call msg.AckWithResult()
    // or msg.NackWithResult() instead of the regular Ack/Nack methods.
    // When exactly once delivery is enabled on the subscription, the message is
    // guaranteed to not be delivered again if the ack result succeeds.
    func receiveMessagesWithExactlyOnceDeliveryEnabled(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    
    	// Pub/Sub's exactly once delivery guarantee only applies when subscribers connect to the service in the same region.
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID, option.WithEndpoint("us-west1-pubsub.googleapis.com:443"))
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub := client.Subscription(subID)
    	// Set MinExtensionPeriod high to avoid any unintentional
    	// acknowledgment expirations (e.g. due to network events).
    	// This can lead to high tail latency in case of client crashes.
    	sub.ReceiveSettings.MinExtensionPeriod = 600 * time.Second
    
    	// Receive messages for 10 seconds, which simplifies testing.
    	// Comment this out in production, since `Receive` should
    	// be used as a long running operation.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    	err = sub.Receive(ctx, func(ctx context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got message: %q\n", string(msg.Data))
    		r := msg.AckWithResult()
    		// Block until the result is returned and a pubsub.AcknowledgeStatus
    		// is returned for the acked message.
    		status, err := r.Get(ctx)
    		if err != nil {
    			fmt.Fprintf(w, "MessageID: %s failed when calling result.Get: %v", msg.ID, err)
    		}
    
    		switch status {
    		case pubsub.[AcknowledgeStatusSuccess](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_AcknowledgeStatusSuccess_AcknowledgeStatusPermissionDenied_AcknowledgeStatusFailedPrecondition_AcknowledgeStatusInvalidAckID_AcknowledgeStatusOther):
    			fmt.Fprintf(w, "Message successfully acked: %s", msg.ID)
    		case pubsub.[AcknowledgeStatusInvalidAckID](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_AcknowledgeStatusSuccess_AcknowledgeStatusPermissionDenied_AcknowledgeStatusFailedPrecondition_AcknowledgeStatusInvalidAckID_AcknowledgeStatusOther):
    			fmt.Fprintf(w, "Message failed to ack with response of Invalid. ID: %s", msg.ID)
    		case pubsub.[AcknowledgeStatusPermissionDenied](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_AcknowledgeStatusSuccess_AcknowledgeStatusPermissionDenied_AcknowledgeStatusFailedPrecondition_AcknowledgeStatusInvalidAckID_AcknowledgeStatusOther):
    			fmt.Fprintf(w, "Message failed to ack with response of Permission Denied. ID: %s", msg.ID)
    		case pubsub.[AcknowledgeStatusFailedPrecondition](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_AcknowledgeStatusSuccess_AcknowledgeStatusPermissionDenied_AcknowledgeStatusFailedPrecondition_AcknowledgeStatusInvalidAckID_AcknowledgeStatusOther):
    			fmt.Fprintf(w, "Message failed to ack with response of Failed Precondition. ID: %s", msg.ID)
    		case pubsub.[AcknowledgeStatusOther](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_AcknowledgeStatusSuccess_AcknowledgeStatusPermissionDenied_AcknowledgeStatusFailedPrecondition_AcknowledgeStatusInvalidAckID_AcknowledgeStatusOther):
    			fmt.Fprintf(w, "Message failed to ack with response of Other. ID: %s", msg.ID)
    		default:
    		}
    	})
    	if err != nil {
    		return fmt.Errorf("got err from sub.Receive: %w", err)
    	}
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
