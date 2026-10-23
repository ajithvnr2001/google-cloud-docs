---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-publisher-flow-control/
title: v1 Publish messages with flow control settings (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:48.898553+00:00
---

# v1 Publish messages with flow control settings (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-publisher-flow-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Publish messages with flow control settings (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Publish messages with flow control settings

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strconv"
    	"sync"
    	"sync/atomic"
    
    	"cloud.google.com/go/pubsub"
    )
    
    func publishWithFlowControlSettings(w io.Writer, projectID, topicID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	t := client.Topic(topicID)
    	t.PublishSettings.[FlowControlSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_FlowControlSettings) = pubsub.[FlowControlSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_FlowControlSettings){
    		MaxOutstandingMessages: 100,                     // default 1000
    		MaxOutstandingBytes:    10 * 1024 * 1024,        // default 0 (unlimited)
    		LimitExceededBehavior:  pubsub.[FlowControlBlock](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_FlowControlIgnore_FlowControlBlock_FlowControlSignalError), // default Ignore, other options: Block and SignalError
    	}
    
    	var wg sync.WaitGroup
    	var totalErrors uint64
    
    	numMsgs := 1000
    	// Rapidly publishing 1000 messages in a loop may be constrained by flow control.
    	for i := 0; i < numMsgs; i++ {
    		wg.Add(1)
    		result := t.Publish(ctx, &pubsub.Message{
    			Data: []byte("message #" + strconv.Itoa(i)),
    		})
    		go func(i int, res *pubsub.[PublishResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_PublishResult)) {
    			fmt.Fprintf(w, "Publishing message %d\n", i)
    			defer wg.Done()
    			// The Get method blocks until a server-generated ID or
    			// an error is returned for the published message.
    			_, err := res.Get(ctx)
    			if err != nil {
    				// Error handling code can be added here.
    				fmt.Fprintf(w, "Failed to publish: %v", err)
    				atomic.AddUint64(&totalErrors, 1)
    				return
    			}
    		}(i, result)
    	}
    
    	wg.Wait()
    
    	if totalErrors > 0 {
    		return fmt.Errorf("%d of %d messages did not publish successfully", totalErrors, numMsgs)
    	}
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
