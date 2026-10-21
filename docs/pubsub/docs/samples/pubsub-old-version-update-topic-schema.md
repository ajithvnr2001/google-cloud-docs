---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-update-topic-schema/
title: v1 Update the topic schema (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:53:14.147890+00:00
---

# v1 Update the topic schema (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-update-topic-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Update the topic schema (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Update the topic schema

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub"
    )
    
    func updateTopicSchema(w io.Writer, projectID, topicID, firstRevisionID, lastRevisionID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// firstRevisionID := "my-revision-id"
    	// lastRevisionID := "my-revision-id"
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	t := client.Topic(topicID)
    
    	// This updates the first / last revision ID for the topic's schema.
    	// To clear the schema entirely, use a zero valued (empty) SchemaSettings.
    	tc := pubsub.TopicConfigToUpdate{
    		SchemaSettings: &pubsub.SchemaSettings{
    			FirstRevisionID: firstRevisionID,
    			LastRevisionID:  lastRevisionID,
    		},
    	}
    
    	gotTopicCfg, err := t.Update(ctx, tc)
    	if err != nil {
    		fmt.Fprintf(w, "topic.Update err: %v\n", gotTopicCfg)
    		return err
    	}
    	fmt.Fprintf(w, "Updated topic with schema: %#v\n", gotTopicCfg)
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
