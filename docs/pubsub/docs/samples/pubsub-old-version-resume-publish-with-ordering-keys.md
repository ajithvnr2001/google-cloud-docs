---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-resume-publish-with-ordering-keys/
title: v1 Resume publishing with ordering keys (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:39.320194+00:00
---

# v1 Resume publishing with ordering keys (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-resume-publish-with-ordering-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Resume publishing with ordering keys (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Resume publishing with ordering keys

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub"
    	"google.golang.org/api/option"
    )
    
    func resumePublishWithOrderingKey(w io.Writer, projectID, topicID string) {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    
    	// Pub/Sub's ordered delivery guarantee only applies when publishes for an ordering key are in the same region
    	// For list of locational endpoints for Pub/Sub, see https://cloud.google.com/pubsub/docs/reference/service_apis_overview#list_of_locational_endpoints
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID,
    		option.WithEndpoint("us-east1-pubsub.googleapis.com:443"))
    	if err != nil {
    		fmt.Fprintf(w, "pubsub.NewClient: %v", err)
    		return
    	}
    	defer client.Close()
    
    	t := client.Topic(topicID)
    	t.EnableMessageOrdering = true
    	key := "some-ordering-key"
    
    	res := t.Publish(ctx, &pubsub.Message{
    		Data:        []byte("some-message"),
    		OrderingKey: key,
    	})
    	_, err = res.Get(ctx)
    	if err != nil {
    		// Error handling code can be added here.
    		fmt.Printf("Failed to publish: %s\n", err)
    
    		// Resume publish on an ordering key that has had unrecoverable errors.
    		// After such an error publishes with this ordering key will fail
    		// until this method is called.
    		t.[ResumePublish](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Topic_ResumePublish)(key)
    	}
    
    	fmt.Fprint(w, "Published a message with ordering key successfully\n")
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
