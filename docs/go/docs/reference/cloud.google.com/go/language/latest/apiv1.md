---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/
title: Cloud Natural Language API v1 - Package cloud.google.com/go/language/apiv1 (v1.19.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:42.544141+00:00
---

# Cloud Natural Language API v1 - Package cloud.google.com/go/language/apiv1 (v1.19.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Natural Language API v1 - Package cloud.google.com/go/language/apiv1 (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.0  1.17.0  1.16.0  1.15.0  1.14.6  1.13.1  1.12.9  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/language/apiv1). 

Package language is an auto-generated package for the Cloud Natural Language API. 

Provides natural language understanding technologies, such as sentiment analysis, entity recognition, entity sentiment analysis, and other text annotations, to developers. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/language/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := language.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &languagepb.AnalyzeEntitiesRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#AnalyzeEntitiesRequest.
    }
    resp, err := c.AnalyzeEntities(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## CallOptions
    
    
    type CallOptions struct {
    	AnalyzeSentiment       []gax.CallOption
    	AnalyzeEntities        []gax.CallOption
    	AnalyzeEntitySentiment []gax.CallOption
    	AnalyzeSyntax          []gax.CallOption
    	ClassifyText           []gax.CallOption
    	ModerateText           []gax.CallOption
    	AnnotateText           []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Cloud Natural Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Provides text analysis operations such as sentiment analysis and entity recognition.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new language service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Provides text analysis operations such as sentiment analysis and entity recognition.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new language service rest client.

Provides text analysis operations such as sentiment analysis and entity recognition.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) AnalyzeEntities 
    
    
    func (c *Client) AnalyzeEntities(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeEntitiesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeEntitiesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeEntitiesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeEntitiesResponse), [error](https://pkg.go.dev/builtin#error))

AnalyzeEntities finds named entities (currently proper names and common nouns) in the text along with entity types, salience, mentions for each entity, and other properties.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.AnalyzeEntitiesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#AnalyzeEntitiesRequest.
    	}
    	resp, err := c.AnalyzeEntities(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) AnalyzeEntitySentiment 
    
    
    func (c *Client) AnalyzeEntitySentiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeEntitySentimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeEntitySentimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeEntitySentimentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeEntitySentimentResponse), [error](https://pkg.go.dev/builtin#error))

AnalyzeEntitySentiment finds entities, similar to AnalyzeEntities in the text and analyzes sentiment associated with each entity and its mentions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.AnalyzeEntitySentimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#AnalyzeEntitySentimentRequest.
    	}
    	resp, err := c.AnalyzeEntitySentiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) AnalyzeSentiment 
    
    
    func (c *Client) AnalyzeSentiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeSentimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeSentimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeSentimentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeSentimentResponse), [error](https://pkg.go.dev/builtin#error))

AnalyzeSentiment analyzes the sentiment of the provided text.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.AnalyzeSentimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#AnalyzeSentimentRequest.
    	}
    	resp, err := c.AnalyzeSentiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) AnalyzeSyntax 
    
    
    func (c *Client) AnalyzeSyntax(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeSyntaxRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeSyntaxRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnalyzeSyntaxResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnalyzeSyntaxResponse), [error](https://pkg.go.dev/builtin#error))

AnalyzeSyntax analyzes the syntax of the text and provides sentence boundaries and tokenization along with part of speech tags, dependency trees, and other properties.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.AnalyzeSyntaxRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#AnalyzeSyntaxRequest.
    	}
    	resp, err := c.AnalyzeSyntax(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) AnnotateText 
    
    
    func (c *Client) AnnotateText(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnnotateTextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnnotateTextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[AnnotateTextResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_AnnotateTextResponse), [error](https://pkg.go.dev/builtin#error))

AnnotateText a convenience method that provides all the features that analyzeSentiment, analyzeEntities, and analyzeSyntax provide in one call.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.AnnotateTextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#AnnotateTextRequest.
    	}
    	resp, err := c.AnnotateText(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ClassifyText 
    
    
    func (c *Client) ClassifyText(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[ClassifyTextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_ClassifyTextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[ClassifyTextResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_ClassifyTextResponse), [error](https://pkg.go.dev/builtin#error))

ClassifyText classifies a document into categories.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.ClassifyTextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#ClassifyTextRequest.
    	}
    	resp, err := c.ClassifyText(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) ModerateText 
    
    
    func (c *Client) ModerateText(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[ModerateTextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_ModerateTextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[languagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb).[ModerateTextResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb#cloud_google_com_go_language_apiv1_languagepb_ModerateTextResponse), [error](https://pkg.go.dev/builtin#error))

ModerateText moderates a document for harmful and sensitive categories.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	language "cloud.google.com/go/language/apiv1"
    	languagepb "cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	req := &languagepb.ModerateTextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/language/apiv1/languagepb#ModerateTextRequest.
    	}
    	resp, err := c.ModerateText(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
