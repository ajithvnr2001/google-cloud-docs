---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/go-runtime/
title: The Go Runtime \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:28.864151+00:00
---

# The Go Runtime  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/go-runtime/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The Go Runtime

## Overview

Your Cloud Run function runs in an environment consisting of an operating system version plus add-on packages, language support, and the Functions Framework library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime.

For information about runtimes in general, and to learn which Ubuntu version each Go runtime uses, see the [Cloud Run functions execution environment](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#go).

## Select your runtime

Cloud Run functions supports several versions of Go, listed on the [Runtime support](https://docs.cloud.google.com/functions/1stgendocs/runtime-support#go) page. You can select the preferred Go runtime for your function during deployment.

If you're using the Google Cloud CLI, specify the runtime by using the `--runtime` parameter with the Go runtime of your choice. For example:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --runtime go121 FLAGS...

`FLAGS...` refers to arguments passed during the first deployment of your function. For more information regarding required and optional arguments, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/deploy#basics).

## Function preparation

You can write a function on your local machine and upload it. To prepare your local machine for Go development, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

To get started quickly with Go on Cloud Run functions, see the [Quickstart](https://docs.cloud.google.com/functions/1stgendocs/create-deploy-gcloud-1st-gen).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Writing Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/writing#structuring_source_code) for more information.

## Specifying dependencies

Cloud Run functions in Go must provide all of their dependencies either with Go modules and a `go.mod` file, or with a `vendor` directory. For more information, see [Specifying dependencies in Go](https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-go).

## Environment variables

Your Go runtime automatically sets certain environment variables for your function to use as needed. For details, see [Using Environment Variables](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var#newer_runtimes).

## `Context` type

[Go's `context` package](https://golang.org/pkg/context/) defines the `Context` type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes.

The following Cloud Run functions code shows an example of context access by a Pub/Sub client:
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
    	functions.CloudEvent("HelloPubSub", helloPubSub)
    }
    
    // MessagePublishedData contains the full Pub/Sub message
    // See the documentation for more details:
    // https://cloud.google.com/eventarc/docs/cloudevents#pubsub
    type MessagePublishedData struct {
    	Message PubSubMessage
    }
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // helloPubSub consumes a CloudEvent message and extracts the Pub/Sub message.
    func helloPubSub(ctx context.Context, e event.Event) error {
    	var msg MessagePublishedData
    	if err := e.DataAs(&msg); err != nil {
    		return fmt.Errorf("event.DataAs: %w", err)
    	}
    
    	name := string(msg.Message.Data) // Automatically decoded from base64.
    	if name == "" {
    		name = "World"
    	}
    	log.Printf("Hello, %s!", name)
    	return nil
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
