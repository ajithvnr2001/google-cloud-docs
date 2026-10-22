---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-create-topic-with-schema-revisions/
title: v1 Create and associate a schema when you create a topic (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:58.286462+00:00
---

# v1 Create and associate a schema when you create a topic (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-create-topic-with-schema-revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Create and associate a schema when you create a topic (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Create and associate a schema when you create a topic

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
    
    func createTopicWithSchemaRevisions(w io.Writer, projectID, topicID, schemaID, firstRevisionID, lastRevisionID string, encoding pubsub.[SchemaEncoding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaEncoding)) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// schemaID := "my-schema-id"
    	// firstRevisionID := "my-revision-id"
    	// lastRevisionID := "my-revision-id"
    	// encoding := pubsub.EncodingJSON
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	tc := &pubsub.TopicConfig{
    		SchemaSettings: &pubsub.SchemaSettings{
    			Schema:          fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    			FirstRevisionID: firstRevisionID,
    			LastRevisionID:  lastRevisionID,
    			Encoding:        encoding,
    		},
    	}
    	t, err := client.[CreateTopicWithConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_CreateTopicWithConfig)(ctx, topicID, tc)
    	if err != nil {
    		return fmt.Errorf("CreateTopicWithConfig: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic with schema revision: %#v\n", t)
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
