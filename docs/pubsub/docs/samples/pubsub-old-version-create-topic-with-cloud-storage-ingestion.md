---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-create-topic-with-cloud-storage-ingestion/
title: v1 Create topic with Cloud Storage ingestion (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:53:08.771130+00:00
---

# v1 Create topic with Cloud Storage ingestion (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-create-topic-with-cloud-storage-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Create topic with Cloud Storage ingestion (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Create topic with Cloud Storage ingestion

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
    )
    
    func createTopicWithCloudStorageIngestion(w io.Writer, projectID, topicID, bucket, matchGlob, minimumObjectCreateTime string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// bucket := "my-bucket"
    	// matchGlob := "**.txt"
    	// minimumObjectCreateTime := "2006-01-02T15:04:05Z"
    
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	minCreateTime, err := time.Parse(time.RFC3339, minimumObjectCreateTime)
    	if err != nil {
    		return err
    	}
    
    	cfg := &pubsub.TopicConfig{
    		IngestionDataSourceSettings: &pubsub.IngestionDataSourceSettings{
    			Source: &pubsub.[IngestionDataSourceCloudStorage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_IngestionDataSourceCloudStorage){
    				Bucket: bucket,
    				// Alternatively, can be Avro or PubSubAvro formats. See
    				InputFormat: &pubsub.[IngestionDataSourceCloudStorageTextFormat](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_IngestionDataSourceCloudStorageTextFormat){
    					Delimiter: ",",
    				},
    				MatchGlob:               matchGlob,
    				MinimumObjectCreateTime: minCreateTime,
    			},
    		},
    	}
    	t, err := client.[CreateTopicWithConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_CreateTopicWithConfig)(ctx, topicID, cfg)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Cloud storage topic created: %v\n", t)
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
