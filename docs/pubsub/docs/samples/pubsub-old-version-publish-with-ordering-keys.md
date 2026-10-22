---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-publish-with-ordering-keys/
title: v1 Publish with ordering keys (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:42.471477+00:00
---

# v1 Publish with ordering keys (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-publish-with-ordering-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Publish with ordering keys (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Publish with ordering keys

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync"
    	"sync/atomic"
    
    	"cloud.google.com/go/pubsub"
    	"google.golang.org/api/option"
    )
    
    func publishWithOrderingKey(w io.Writer, projectID, topicID string) {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    
    	// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering key are in the same region.
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID,
    		option.WithEndpoint("us-east1-pubsub.googleapis.com:443"))
    	if err != nil {
    		fmt.Fprintf(w, "pubsub.NewClient: %v", err)
    		return
    	}
    	defer client.Close()
    
    	var wg sync.WaitGroup
    	var totalErrors uint64
    	t := client.Topic(topicID)
    	t.EnableMessageOrdering = true
    
    	messages := []struct {
    		message     string
    		orderingKey string
    	}{
    		{
    			message:     "message1",
    			orderingKey: "key1",
    		},
    		{
    			message:     "message2",
    			orderingKey: "key2",
    		},
    		{
    			message:     "message3",
    			orderingKey: "key1",
    		},
    		{
    			message:     "message4",
    			orderingKey: "key2",
    		},
    	}
    
    	for _, m := range messages {
    		res := t.Publish(ctx, &pubsub.Message{
    			Data:        []byte(m.message),
    			OrderingKey: m.orderingKey,
    		})
    
    		wg.Add(1)
    		go func(res *pubsub.[PublishResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_PublishResult)) {
    			defer wg.Done()
    			// The Get method blocks until a server-generated ID or
    			// an error is returned for the published message.
    			_, err := res.Get(ctx)
    			if err != nil {
    				// Error handling code can be added here.
    				fmt.Printf("Failed to publish: %s\n", err)
    				atomic.AddUint64(&totalErrors, 1)
    				return
    			}
    		}(res)
    	}
    
    	wg.Wait()
    
    	if totalErrors > 0 {
    		fmt.Fprintf(w, "%d of 4 messages did not publish successfully", totalErrors)
    		return
    	}
    
    	fmt.Fprint(w, "Published 4 messages with ordering keys successfully\n")
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
