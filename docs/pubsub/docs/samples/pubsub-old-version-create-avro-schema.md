---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-create-avro-schema/
title: v1 Create Avro-typed schema (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:53.355653+00:00
---

# v1 Create Avro-typed schema (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-create-avro-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Create Avro-typed schema (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Create Avro-typed schema

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	"cloud.google.com/go/pubsub"
    )
    
    // createAvroSchema creates a schema resource from a JSON-formatted Avro schema file.
    func createAvroSchema(w io.Writer, projectID, schemaID, avscFile string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	// avscFile = "path/to/an/avro/schema/file(.avsc)/formatted/in/json"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	avscSource, err := os.ReadFile(avscFile)
    	if err != nil {
    		return fmt.Errorf("error reading from file: %s", avscFile)
    	}
    
    	config := pubsub.[SchemaConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaConfig){
    		Type:       pubsub.[SchemaAvro](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaTypeUnspecified_SchemaProtocolBuffer_SchemaAvro),
    		Definition: string(avscSource),
    	}
    	s, err := client.CreateSchema(ctx, schemaID, config)
    	if err != nil {
    		return fmt.Errorf("CreateSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Schema created: %#v\n", s)
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
