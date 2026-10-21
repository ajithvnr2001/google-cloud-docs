---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-subscribe-avro-records/
title: v1 Receive messages of Avro schema type (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:53:11.390418+00:00
---

# v1 Receive messages of Avro schema type (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-subscribe-avro-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Receive messages of Avro schema type (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Receive messages of Avro schema type

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"sync"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"github.com/linkedin/goavro/v2"
    )
    
    func subscribeWithAvroSchema(w io.Writer, projectID, subID, avscFile string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// avscFile = "path/to/an/avro/schema/file(.avsc)/formatted/in/json"
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	avroSchema, err := os.ReadFile(avscFile)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile err: %w", err)
    	}
    	codec, err := goavro.NewCodec(string(avroSchema))
    	if err != nil {
    		return fmt.Errorf("goavro.NewCodec err: %w", err)
    	}
    
    	sub := client.Subscription(subID)
    	ctx2, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var mu sync.Mutex
    	sub.Receive(ctx2, func(ctx context.Context, msg *pubsub.Message) {
    		mu.Lock()
    		defer mu.Unlock()
    		encoding := msg.Attributes["googclient_schemaencoding"]
    
    		var state map[string]interface{}
    		if encoding == "BINARY" {
    			data, _, err := codec.NativeFromBinary(msg.Data)
    			if err != nil {
    				fmt.Fprintf(w, "codec.NativeFromBinary err: %v\n", err)
    				msg.Nack()
    				return
    			}
    			fmt.Fprintf(w, "Received a binary-encoded message:\n%#v\n", data)
    			state = data.(map[string]interface{})
    		} else if encoding == "JSON" {
    			data, _, err := codec.NativeFromTextual(msg.Data)
    			if err != nil {
    				fmt.Fprintf(w, "codec.NativeFromTextual err: %v\n", err)
    				msg.Nack()
    				return
    			}
    			fmt.Fprintf(w, "Received a JSON-encoded message:\n%#v\n", data)
    			state = data.(map[string]interface{})
    		} else {
    			fmt.Fprintf(w, "Unknown message type(%s), nacking\n", encoding)
    			msg.Nack()
    			return
    		}
    		fmt.Fprintf(w, "%s is abbreviated as %s\n", state["name"], state["post_abbr"])
    		msg.Ack()
    	})
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
