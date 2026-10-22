---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-list-schemas/
title: v1 List schemas (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:48.320293+00:00
---

# v1 List schemas (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-list-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 List schemas (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) List schemas

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub"
    	"google.golang.org/api/iterator"
    )
    
    func listSchemas(w io.Writer, projectID string) ([]*pubsub.[SchemaConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaConfig), error) {
    	// projectID := "my-project-id"
    	ctx := context.Background()
    	client, err := pubsub.NewSchemaClient(ctx, projectID)
    	if err != nil {
    		return nil, fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    	defer client.Close()
    
    	var schemas []*pubsub.[SchemaConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaConfig)
    
    	schemaIter := client.[Schemas](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaClient_Schemas)(ctx, pubsub.[SchemaViewFull](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_SchemaViewUnspecified_SchemaViewBasic_SchemaViewFull))
    	for {
    		sc, err := schemaIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return nil, fmt.Errorf("schemaIter.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Got schema: %#v\n", sc)
    		schemas = append(schemas, sc)
    	}
    
    	fmt.Fprintf(w, "Got %d schemas", len(schemas))
    	return schemas, nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
