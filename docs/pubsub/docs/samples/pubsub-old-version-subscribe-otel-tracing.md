---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-subscribe-otel-tracing/
title: v1 Create a subscriber application with OpenTelemetry enabled (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:53:07.171240+00:00
---

# v1 Create a subscriber application with OpenTelemetry enabled (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-subscribe-otel-tracing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Create a subscriber application with OpenTelemetry enabled (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Create a subscriber application with OpenTelemetry enabled

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync/atomic"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	texporter "github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace"
    	"go.opentelemetry.io/otel"
    	"go.opentelemetry.io/otel/sdk/resource"
    	sdktrace "go.opentelemetry.io/otel/sdk/trace"
    	semconv "go.opentelemetry.io/otel/semconv/v1.24.0"
    	"google.golang.org/api/option"
    )
    
    func subscribeOpenTelemetryTracing(w io.Writer, projectID, subID string, sampleRate float64) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	// sampleRate := "1.0"
    	ctx := context.Background()
    
    	exporter, err := texporter.New(texporter.WithProjectID(projectID),
    		// Disable spans created by the exporter.
    		texporter.WithTraceClientOptions(
    			[]option.ClientOption{option.WithTelemetryDisabled()},
    		),
    	)
    	if err != nil {
    		return fmt.Errorf("error instantiating exporter: %w", err)
    	}
    
    	resources := resource.NewWithAttributes(
    		semconv.SchemaURL,
    		semconv.ServiceNameKey.String("subscriber"),
    	)
    
    	// Instantiate a tracer provider with the following settings
    	tp := sdktrace.NewTracerProvider(
    		sdktrace.WithBatcher(exporter),
    		sdktrace.WithResource(resources),
    		sdktrace.WithSampler(
    			sdktrace.ParentBased(sdktrace.TraceIDRatioBased(sampleRate)),
    		),
    	)
    
    	defer tp.ForceFlush(ctx) // flushes any pending spans
    	otel.SetTracerProvider(tp)
    
    	// Create a new client with tracing enabled.
    	client, err := pubsub.[NewClientWithConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClientWithConfig)(ctx, projectID, &pubsub.[ClientConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_ClientConfig){
    		EnableOpenTelemetryTracing: true,
    	})
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub := client.Subscription(subID)
    
    	// Receive messages for 10 seconds, which simplifies testing.
    	// Comment this out in production, since `Receive` should
    	// be used as a long running operation.
    	ctx, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var received int32
    	err = sub.Receive(ctx, func(_ context.Context, msg *pubsub.Message) {
    		fmt.Fprintf(w, "Got message: %q\n", string(msg.Data))
    		atomic.AddInt32(&received, 1)
    		msg.Ack()
    	})
    	if err != nil {
    		return fmt.Errorf("sub.Receive: %w", err)
    	}
    	fmt.Fprintf(w, "Received %d messages\n", received)
    
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
