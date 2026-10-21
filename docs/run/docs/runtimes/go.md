---
url: https://docs.cloud.google.com/run/docs/runtimes/go/
title: The Go runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:48.606217+00:00
---

# The Go runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The Go runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [Go Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-go) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for Go development, see [Set up a Go development environment](https://docs.cloud.google.com/go/docs/setup).

## Supported Go runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Go 1.27 | go127 | 
* google-24 (default)
* google-24-full
| 
* [google-24/go127](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/go127)
* [google-24-full/go127](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go127)
| Aug/Sept 2027 | Feb/March 2028  
Go 1.26 | go126 | 
* google-24 (default)
* google-24-full
| 
* [google-24/go126](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/go126)
* [google-24-full/go126](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/go126)
| Feb/March 2027 | Aug/Sept 2027  
Go 1.25 | go125 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go125](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go125)
* [google-22-full/go125](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go125)
| 2026-10-01 | 2027-04-01  
Go 1.24 | go124 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go124](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go124)
* [google-22-full/go124](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go124)
| 2026-09-02 | 2027-03-02  
Go 1.23   
| go123 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go123](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go123)
* [google-22-full/go123](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go123)
| 2026-02-21 | 2026-08-21  
Go 1.22 | go122 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go122](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go122)
* [google-22-full/go122](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go122)
| 2026-01-28 | 2026-07-28  
Go 1.21 | go121 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go121](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go121)
* [google-22-full/go121](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go121)
| 2025-09-03 | 2026-03-03  
Go 1.20 | go120 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go120)
* [google-22-full/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go120)
| 2024-05-01 | 2025-05-01  
Go 1.19 | go119 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go119](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go119)
* [google-22-full/go119](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go119)
| 2024-04-30 | 2025-01-30  
Go 1.18 | go118 | 
* google-22 (default)
* google-22-full
| 
* [google-22/go118](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/go118)
* [google-22-full/go120](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/go118)
| 2024-01-30 | 2025-01-30  
Go 1.16 | go116 |  google-18-full  |  [google-18-full/go116](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go116) | 2024-01-30 | 2025-01-30  
Go 1.13 | go113 |  google-18-full  |  [google-18-full/go113](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/go113) | 2024-01-30 | 2025-01-30  
Go 1.11 | go111 |  Decommissioned  |  Decommissioned  | 2020-08-05 | Feb 2021  
**Note:** Go's [release policy](https://go.dev/doc/devel/release#policy) states that each major Go release is supported until there are two newer major releases. Thus, depending on when newer versions of Go are made publicly available, key dates such as end of support, deprecation, and decommission might be postponed. 

## Select your runtime

You can select one of the supported Go runtimes for your function during deployment.

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [Go base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image go127
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a Go runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#go) for more information.

## Specify dependencies

Cloud Run functions in Go must provide all of their dependencies either with Go modules and a `go.mod` file, or with a `vendor` directory. For more information, see [Specify dependencies in Go](https://docs.cloud.google.com/run/docs/runtimes/go-dependencies).

## Environment variables

Your Go runtime automatically sets certain environment variables for your function to use as needed. For details, see [Configure environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables).

## `Context` type

[Go's `context` package](https://golang.org/pkg/context/) defines the `Context` type, which carries deadlines, cancellation signals, and other request-scoped values across API boundaries and between processes.

The following code shows an example of context access by a Pub/Sub client:
    
    
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
