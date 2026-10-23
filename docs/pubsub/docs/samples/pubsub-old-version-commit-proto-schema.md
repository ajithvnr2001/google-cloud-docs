---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-commit-proto-schema/
title: v1 Commit a revision for a Protocol Buffer schema (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:05.883946+00:00
---

# v1 Commit a revision for a Protocol Buffer schema (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-commit-proto-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Commit a revision for a Protocol Buffer schema (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Commit a revision for a Protocol Buffer schema

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
    
    // commitProtoSchema commits a new proto schema revision to an existing schema.
    func commitProtoSchema(w io.Writer, projectID, schemaID, protoFile string) error {
    	// projectID := "my-project-id"
    	// schemaID := "my-schema"
    	// protoFile = "path/to/a/proto/schema/file(.proto)/formatted/in/protocol/buffers"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	// Read a proto file as a byte slice.
    	protoSource, err := os.ReadFile(protoFile)
    	if err != nil {
    		return fmt.Errorf("error reading from file: %s", protoFile)
    	}
    
    	config := pubsub.[SchemaConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaConfig){
    		Name:       fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    		Type:       pubsub.[SchemaProtocolBuffer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaTypeUnspecified_SchemaProtocolBuffer_SchemaAvro),
    		Definition: string(protoSource),
    	}
    	s, err := client.CommitSchema(ctx, schemaID, config)
    	if err != nil {
    		return fmt.Errorf("CommitSchema: %w", err)
    	}
    	fmt.Fprintf(w, "Committed a schema using a protobuf schema: %#v\n", s)
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
