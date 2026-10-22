---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-publisher-batch-settings/
title: v1 Publish with batching settings (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:44.737314+00:00
---

# v1 Publish with batching settings (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-publisher-batch-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Publish with batching settings (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Publish with batching settings

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strconv"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    )
    
    func publishWithSettings(w io.Writer, projectID, topicID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    	var results []*pubsub.[PublishResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_PublishResult)
    	var resultErrors []error
    	t := client.Topic(topicID)
    	t.PublishSettings.ByteThreshold = 5000
    	t.PublishSettings.CountThreshold = 10
    	t.PublishSettings.DelayThreshold = 100 * time.Millisecond
    
    	for i := 0; i < 10; i++ {
    		result := t.Publish(ctx, &pubsub.Message{
    			Data: []byte("Message " + strconv.Itoa(i)),
    		})
    		results = append(results, result)
    	}
    	// The Get method blocks until a server-generated ID or
    	// an error is returned for the published message.
    	for i, res := range results {
    		id, err := res.Get(ctx)
    		if err != nil {
    			resultErrors = append(resultErrors, err)
    			fmt.Fprintf(w, "Failed to publish: %v", err)
    			continue
    		}
    		fmt.Fprintf(w, "Published message %d; msg ID: %v\n", i, id)
    	}
    	if len(resultErrors) != 0 {
    		return fmt.Errorf("Get: %v", resultErrors[len(resultErrors)-1])
    	}
    	fmt.Fprintf(w, "Published messages with batch settings.")
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
