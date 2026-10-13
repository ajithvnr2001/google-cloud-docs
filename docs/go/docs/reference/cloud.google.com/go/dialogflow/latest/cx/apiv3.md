---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/
title: Dialogflow API v3 - Package cloud.google.com/go/dialogflow/cx/apiv3 (v1.87.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:12.326452+00:00
---

# Dialogflow API v3 - Package cloud.google.com/go/dialogflow/cx/apiv3 (v1.87.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Dialogflow API v3 - Package cloud.google.com/go/dialogflow/cx/apiv3 (v1.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.87.0 (latest)  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.1  1.68.2  1.67.0  1.66.0  1.65.0  1.64.1  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.1  1.57.1  1.56.0  1.55.0  1.54.3  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.2  1.47.0  1.46.0  1.45.0  1.44.3  1.42.0  1.41.0  1.40.1  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.1  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3). 

Package cx is an auto-generated package for the Dialogflow API. 

Builds conversational interfaces (for example, chatbots, and voice-powered apps and devices). 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/dialogflow/cx/apiv3@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := cx.NewPagesClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &cxpb.CreatePageRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreatePageRequest.
    }
    resp, err := c.CreatePage(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewPagesClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AgentIterator
    
    
    type AgentIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Agent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AgentIterator manages a stream of *cxpb.Agent.

### func (*AgentIterator) All 
    
    
    func (it *AgentIterator) All() iter.Seq2[*cxpb.Agent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AgentIterator) Next 
    
    
    func (it *AgentIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Agent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AgentIterator) PageInfo 
    
    
    func (it *AgentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AgentsCallOptions
    
    
    type AgentsCallOptions struct {
    	ListAgents               []gax.CallOption
    	GetAgent                 []gax.CallOption
    	CreateAgent              []gax.CallOption
    	UpdateAgent              []gax.CallOption
    	DeleteAgent              []gax.CallOption
    	ExportAgent              []gax.CallOption
    	RestoreAgent             []gax.CallOption
    	ValidateAgent            []gax.CallOption
    	GetAgentValidationResult []gax.CallOption
    	GetGenerativeSettings    []gax.CallOption
    	UpdateGenerativeSettings []gax.CallOption
    	GetLocation              []gax.CallOption
    	ListLocations            []gax.CallOption
    	CancelOperation          []gax.CallOption
    	GetOperation             []gax.CallOption
    	ListOperations           []gax.CallOption
    }

AgentsCallOptions contains the retry settings for each method of AgentsClient.

## AgentsClient
    
    
    type AgentsClient struct {
    
    	// The call options for this service.
    	CallOptions *AgentsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

AgentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Agents.

### func NewAgentsClient 
    
    
    func NewAgentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AgentsClient, [error](https://pkg.go.dev/builtin#error))

NewAgentsClient creates a new agents client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Agents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAgentsRESTClient 
    
    
    func NewAgentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AgentsClient, [error](https://pkg.go.dev/builtin#error))

NewAgentsRESTClient creates a new agents rest client.

Service for managing Agents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewAgentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_AgentsClient_NewAgentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AgentsClient) CancelOperation 
    
    
    func (c *AgentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AgentsClient) Close 
    
    
    func (c *AgentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AgentsClient) Connection (deprecated)
    
    
    func (c *AgentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AgentsClient) CreateAgent 
    
    
    func (c *AgentsClient) CreateAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Agent), [error](https://pkg.go.dev/builtin#error))

CreateAgent creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateAgentRequest.
    	}
    	resp, err := c.CreateAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) DeleteAgent 
    
    
    func (c *AgentsClient) DeleteAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAgent deletes the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteAgentRequest.
    	}
    	err = c.DeleteAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AgentsClient) ExportAgent 
    
    
    func (c *AgentsClient) ExportAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportAgentOperation, [error](https://pkg.go.dev/builtin#error))

ExportAgent exports the specified agent to a binary file.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response:
    ExportAgentResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ExportAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ExportAgentRequest.
    	}
    	op, err := c.ExportAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) ExportAgentOperation 
    
    
    func (c *AgentsClient) ExportAgentOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportAgentOperation

ExportAgentOperation returns a new ExportAgentOperation from a given name. The name must be that of a previously created ExportAgentOperation, possibly from a different process.

### func (*AgentsClient) GetAgent 
    
    
    func (c *AgentsClient) GetAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Agent), [error](https://pkg.go.dev/builtin#error))

GetAgent retrieves the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetAgentRequest.
    	}
    	resp, err := c.GetAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) GetAgentValidationResult 
    
    
    func (c *AgentsClient) GetAgentValidationResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetAgentValidationResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetAgentValidationResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[AgentValidationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_AgentValidationResult), [error](https://pkg.go.dev/builtin#error))

GetAgentValidationResult gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetAgentValidationResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetAgentValidationResultRequest.
    	}
    	resp, err := c.GetAgentValidationResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) GetGenerativeSettings 
    
    
    func (c *AgentsClient) GetGenerativeSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetGenerativeSettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetGenerativeSettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GenerativeSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GenerativeSettings), [error](https://pkg.go.dev/builtin#error))

GetGenerativeSettings gets the generative settings for the agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetGenerativeSettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetGenerativeSettingsRequest.
    	}
    	resp, err := c.GetGenerativeSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) GetLocation 
    
    
    func (c *AgentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) GetOperation 
    
    
    func (c *AgentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) ListAgents 
    
    
    func (c *AgentsClient) ListAgents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListAgentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListAgentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AgentIterator

ListAgents returns the list of all agents in the specified location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListAgentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListAgentsRequest.
    	}
    	it := c.ListAgents(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListAgentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListAgentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListAgentsRequest.
    	}
    	for resp, err := range c.ListAgents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AgentsClient) ListLocations 
    
    
    func (c *AgentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AgentsClient) ListOperations 
    
    
    func (c *AgentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AgentsClient) RestoreAgent 
    
    
    func (c *AgentsClient) RestoreAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RestoreAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RestoreAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestoreAgentOperation, [error](https://pkg.go.dev/builtin#error))

RestoreAgent restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train flows prior to sending them queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.RestoreAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#RestoreAgentRequest.
    	}
    	op, err := c.RestoreAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AgentsClient) RestoreAgentOperation 
    
    
    func (c *AgentsClient) RestoreAgentOperation(name [string](https://pkg.go.dev/builtin#string)) *RestoreAgentOperation

RestoreAgentOperation returns a new RestoreAgentOperation from a given name. The name must be that of a previously created RestoreAgentOperation, possibly from a different process.

### func (*AgentsClient) UpdateAgent 
    
    
    func (c *AgentsClient) UpdateAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Agent), [error](https://pkg.go.dev/builtin#error))

UpdateAgent updates the specified agent.

Note: You should always train flows prior to sending them queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateAgentRequest.
    	}
    	resp, err := c.UpdateAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) UpdateGenerativeSettings 
    
    
    func (c *AgentsClient) UpdateGenerativeSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateGenerativeSettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GenerativeSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GenerativeSettings), [error](https://pkg.go.dev/builtin#error))

UpdateGenerativeSettings updates the generative settings for the agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateGenerativeSettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateGenerativeSettingsRequest.
    	}
    	resp, err := c.UpdateGenerativeSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) ValidateAgent 
    
    
    func (c *AgentsClient) ValidateAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ValidateAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ValidateAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[AgentValidationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_AgentValidationResult), [error](https://pkg.go.dev/builtin#error))

ValidateAgent validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ValidateAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ValidateAgentRequest.
    	}
    	resp, err := c.ValidateAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## BatchRunTestCasesOperation
    
    
    type BatchRunTestCasesOperation struct {
    	// contains filtered or unexported fields
    }

BatchRunTestCasesOperation manages a long-running operation from BatchRunTestCases.

### func (*BatchRunTestCasesOperation) Done 
    
    
    func (op *BatchRunTestCasesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchRunTestCasesOperation) Metadata 
    
    
    func (op *BatchRunTestCasesOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[BatchRunTestCasesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_BatchRunTestCasesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchRunTestCasesOperation) Name 
    
    
    func (op *BatchRunTestCasesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchRunTestCasesOperation) Poll 
    
    
    func (op *BatchRunTestCasesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[BatchRunTestCasesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_BatchRunTestCasesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchRunTestCasesOperation) Wait 
    
    
    func (op *BatchRunTestCasesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[BatchRunTestCasesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_BatchRunTestCasesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ChangelogIterator
    
    
    type ChangelogIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Changelog, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ChangelogIterator manages a stream of *cxpb.Changelog.

### func (*ChangelogIterator) All 
    
    
    func (it *ChangelogIterator) All() iter.Seq2[*cxpb.Changelog, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ChangelogIterator) Next 
    
    
    func (it *ChangelogIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Changelog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Changelog), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ChangelogIterator) PageInfo 
    
    
    func (it *ChangelogIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ChangelogsCallOptions
    
    
    type ChangelogsCallOptions struct {
    	ListChangelogs  []gax.CallOption
    	GetChangelog    []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

ChangelogsCallOptions contains the retry settings for each method of ChangelogsClient.

## ChangelogsClient
    
    
    type ChangelogsClient struct {
    
    	// The call options for this service.
    	CallOptions *ChangelogsCallOptions
    	// contains filtered or unexported fields
    }

ChangelogsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Changelogs.

### func NewChangelogsClient 
    
    
    func NewChangelogsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ChangelogsClient, [error](https://pkg.go.dev/builtin#error))

NewChangelogsClient creates a new changelogs client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Changelogs.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewChangelogsRESTClient 
    
    
    func NewChangelogsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ChangelogsClient, [error](https://pkg.go.dev/builtin#error))

NewChangelogsRESTClient creates a new changelogs rest client.

Service for managing Changelogs.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewChangelogsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_ChangelogsClient_NewChangelogsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ChangelogsClient) CancelOperation 
    
    
    func (c *ChangelogsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ChangelogsClient) Close 
    
    
    func (c *ChangelogsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ChangelogsClient) Connection (deprecated)
    
    
    func (c *ChangelogsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ChangelogsClient) GetChangelog 
    
    
    func (c *ChangelogsClient) GetChangelog(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetChangelogRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetChangelogRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Changelog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Changelog), [error](https://pkg.go.dev/builtin#error))

GetChangelog retrieves the specified Changelog.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetChangelogRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetChangelogRequest.
    	}
    	resp, err := c.GetChangelog(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ChangelogsClient) GetLocation 
    
    
    func (c *ChangelogsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ChangelogsClient) GetOperation 
    
    
    func (c *ChangelogsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ChangelogsClient) ListChangelogs 
    
    
    func (c *ChangelogsClient) ListChangelogs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListChangelogsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListChangelogsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ChangelogIterator

ListChangelogs returns the list of Changelogs.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListChangelogsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListChangelogsRequest.
    	}
    	it := c.ListChangelogs(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListChangelogsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListChangelogsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListChangelogsRequest.
    	}
    	for resp, err := range c.ListChangelogs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ChangelogsClient) ListLocations 
    
    
    func (c *ChangelogsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ChangelogsClient) ListOperations 
    
    
    func (c *ChangelogsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewChangelogsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## ContinuousTestResultIterator
    
    
    type ContinuousTestResultIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.ContinuousTestResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ContinuousTestResultIterator manages a stream of *cxpb.ContinuousTestResult.

### func (*ContinuousTestResultIterator) All 
    
    
    func (it *ContinuousTestResultIterator) All() iter.Seq2[*cxpb.ContinuousTestResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ContinuousTestResultIterator) Next 
    
    
    func (it *ContinuousTestResultIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ContinuousTestResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ContinuousTestResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ContinuousTestResultIterator) PageInfo 
    
    
    func (it *ContinuousTestResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CreateEnvironmentOperation
    
    
    type CreateEnvironmentOperation struct {
    	// contains filtered or unexported fields
    }

CreateEnvironmentOperation manages a long-running operation from CreateEnvironment.

### func (*CreateEnvironmentOperation) Done 
    
    
    func (op *CreateEnvironmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateEnvironmentOperation) Metadata 
    
    
    func (op *CreateEnvironmentOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateEnvironmentOperation) Name 
    
    
    func (op *CreateEnvironmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateEnvironmentOperation) Poll 
    
    
    func (op *CreateEnvironmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Environment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateEnvironmentOperation) Wait 
    
    
    func (op *CreateEnvironmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Environment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateVersionOperation
    
    
    type CreateVersionOperation struct {
    	// contains filtered or unexported fields
    }

CreateVersionOperation manages a long-running operation from CreateVersion.

### func (*CreateVersionOperation) Done 
    
    
    func (op *CreateVersionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateVersionOperation) Metadata 
    
    
    func (op *CreateVersionOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateVersionOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateVersionOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateVersionOperation) Name 
    
    
    func (op *CreateVersionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateVersionOperation) Poll 
    
    
    func (op *CreateVersionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Version), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateVersionOperation) Wait 
    
    
    func (op *CreateVersionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Version), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeployFlowOperation
    
    
    type DeployFlowOperation struct {
    	// contains filtered or unexported fields
    }

DeployFlowOperation manages a long-running operation from DeployFlow.

### func (*DeployFlowOperation) Done 
    
    
    func (op *DeployFlowOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeployFlowOperation) Metadata 
    
    
    func (op *DeployFlowOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeployFlowMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeployFlowMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeployFlowOperation) Name 
    
    
    func (op *DeployFlowOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeployFlowOperation) Poll 
    
    
    func (op *DeployFlowOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeployFlowResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeployFlowResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeployFlowOperation) Wait 
    
    
    func (op *DeployFlowOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeployFlowResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeployFlowResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeploymentIterator
    
    
    type DeploymentIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Deployment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DeploymentIterator manages a stream of *cxpb.Deployment.

### func (*DeploymentIterator) All 
    
    
    func (it *DeploymentIterator) All() iter.Seq2[*cxpb.Deployment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DeploymentIterator) Next 
    
    
    func (it *DeploymentIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DeploymentIterator) PageInfo 
    
    
    func (it *DeploymentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DeploymentsCallOptions
    
    
    type DeploymentsCallOptions struct {
    	ListDeployments []gax.CallOption
    	GetDeployment   []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

DeploymentsCallOptions contains the retry settings for each method of DeploymentsClient.

## DeploymentsClient
    
    
    type DeploymentsClient struct {
    
    	// The call options for this service.
    	CallOptions *DeploymentsCallOptions
    	// contains filtered or unexported fields
    }

DeploymentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Deployments.

### func NewDeploymentsClient 
    
    
    func NewDeploymentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DeploymentsClient, [error](https://pkg.go.dev/builtin#error))

NewDeploymentsClient creates a new deployments client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Deployments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewDeploymentsRESTClient 
    
    
    func NewDeploymentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DeploymentsClient, [error](https://pkg.go.dev/builtin#error))

NewDeploymentsRESTClient creates a new deployments rest client.

Service for managing Deployments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewDeploymentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_DeploymentsClient_NewDeploymentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*DeploymentsClient) CancelOperation 
    
    
    func (c *DeploymentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DeploymentsClient) Close 
    
    
    func (c *DeploymentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*DeploymentsClient) Connection (deprecated)
    
    
    func (c *DeploymentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*DeploymentsClient) GetDeployment 
    
    
    func (c *DeploymentsClient) GetDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Deployment), [error](https://pkg.go.dev/builtin#error))

GetDeployment retrieves the specified Deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetDeploymentRequest.
    	}
    	resp, err := c.GetDeployment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DeploymentsClient) GetLocation 
    
    
    func (c *DeploymentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DeploymentsClient) GetOperation 
    
    
    func (c *DeploymentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DeploymentsClient) ListDeployments 
    
    
    func (c *DeploymentsClient) ListDeployments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListDeploymentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListDeploymentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DeploymentIterator

ListDeployments returns the list of all deployments in the specified Environment.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListDeploymentsRequest.
    	}
    	it := c.ListDeployments(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListDeploymentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListDeploymentsRequest.
    	}
    	for resp, err := range c.ListDeployments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DeploymentsClient) ListLocations 
    
    
    func (c *DeploymentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DeploymentsClient) ListOperations 
    
    
    func (c *DeploymentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewDeploymentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## EntityTypeIterator
    
    
    type EntityTypeIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.EntityType, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EntityTypeIterator manages a stream of *cxpb.EntityType.

### func (*EntityTypeIterator) All 
    
    
    func (it *EntityTypeIterator) All() iter.Seq2[*cxpb.EntityType, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EntityTypeIterator) Next 
    
    
    func (it *EntityTypeIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_EntityType), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EntityTypeIterator) PageInfo 
    
    
    func (it *EntityTypeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## EntityTypesCallOptions
    
    
    type EntityTypesCallOptions struct {
    	GetEntityType     []gax.CallOption
    	CreateEntityType  []gax.CallOption
    	UpdateEntityType  []gax.CallOption
    	DeleteEntityType  []gax.CallOption
    	ListEntityTypes   []gax.CallOption
    	ExportEntityTypes []gax.CallOption
    	ImportEntityTypes []gax.CallOption
    	GetLocation       []gax.CallOption
    	ListLocations     []gax.CallOption
    	CancelOperation   []gax.CallOption
    	GetOperation      []gax.CallOption
    	ListOperations    []gax.CallOption
    }

EntityTypesCallOptions contains the retry settings for each method of EntityTypesClient.

## EntityTypesClient
    
    
    type EntityTypesClient struct {
    
    	// The call options for this service.
    	CallOptions *EntityTypesCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

EntityTypesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing EntityTypes.

### func NewEntityTypesClient 
    
    
    func NewEntityTypesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*EntityTypesClient, [error](https://pkg.go.dev/builtin#error))

NewEntityTypesClient creates a new entity types client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing EntityTypes.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewEntityTypesRESTClient 
    
    
    func NewEntityTypesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*EntityTypesClient, [error](https://pkg.go.dev/builtin#error))

NewEntityTypesRESTClient creates a new entity types rest client.

Service for managing EntityTypes.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewEntityTypesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_EntityTypesClient_NewEntityTypesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*EntityTypesClient) CancelOperation 
    
    
    func (c *EntityTypesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) Close 
    
    
    func (c *EntityTypesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*EntityTypesClient) Connection (deprecated)
    
    
    func (c *EntityTypesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*EntityTypesClient) CreateEntityType 
    
    
    func (c *EntityTypesClient) CreateEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_EntityType), [error](https://pkg.go.dev/builtin#error))

CreateEntityType creates an entity type in the specified agent.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateEntityTypeRequest.
    	}
    	resp, err := c.CreateEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) DeleteEntityType 
    
    
    func (c *EntityTypesClient) DeleteEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteEntityType deletes the specified entity type.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteEntityTypeRequest.
    	}
    	err = c.DeleteEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) ExportEntityTypes 
    
    
    func (c *EntityTypesClient) ExportEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportEntityTypesOperation, [error](https://pkg.go.dev/builtin#error))

ExportEntityTypes exports the selected entity types.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ExportEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ExportEntityTypesRequest.
    	}
    	op, err := c.ExportEntityTypes(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) ExportEntityTypesOperation 
    
    
    func (c *EntityTypesClient) ExportEntityTypesOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportEntityTypesOperation

ExportEntityTypesOperation returns a new ExportEntityTypesOperation from a given name. The name must be that of a previously created ExportEntityTypesOperation, possibly from a different process.

### func (*EntityTypesClient) GetEntityType 
    
    
    func (c *EntityTypesClient) GetEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_EntityType), [error](https://pkg.go.dev/builtin#error))

GetEntityType retrieves the specified entity type.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetEntityTypeRequest.
    	}
    	resp, err := c.GetEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) GetLocation 
    
    
    func (c *EntityTypesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) GetOperation 
    
    
    func (c *EntityTypesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) ImportEntityTypes 
    
    
    func (c *EntityTypesClient) ImportEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportEntityTypesOperation, [error](https://pkg.go.dev/builtin#error))

ImportEntityTypes imports the specified entitytypes into the agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ImportEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ImportEntityTypesRequest.
    	}
    	op, err := c.ImportEntityTypes(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) ImportEntityTypesOperation 
    
    
    func (c *EntityTypesClient) ImportEntityTypesOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportEntityTypesOperation

ImportEntityTypesOperation returns a new ImportEntityTypesOperation from a given name. The name must be that of a previously created ImportEntityTypesOperation, possibly from a different process.

### func (*EntityTypesClient) ListEntityTypes 
    
    
    func (c *EntityTypesClient) ListEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EntityTypeIterator

ListEntityTypes returns the list of all entity types in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListEntityTypesRequest.
    	}
    	it := c.ListEntityTypes(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListEntityTypesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListEntityTypesRequest.
    	}
    	for resp, err := range c.ListEntityTypes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EntityTypesClient) ListLocations 
    
    
    func (c *EntityTypesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EntityTypesClient) ListOperations 
    
    
    func (c *EntityTypesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EntityTypesClient) UpdateEntityType 
    
    
    func (c *EntityTypesClient) UpdateEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_EntityType), [error](https://pkg.go.dev/builtin#error))

UpdateEntityType updates the specified entity type.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateEntityTypeRequest.
    	}
    	resp, err := c.UpdateEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## EnvironmentIterator
    
    
    type EnvironmentIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Environment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EnvironmentIterator manages a stream of *cxpb.Environment.

### func (*EnvironmentIterator) All 
    
    
    func (it *EnvironmentIterator) All() iter.Seq2[*cxpb.Environment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EnvironmentIterator) Next 
    
    
    func (it *EnvironmentIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Environment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EnvironmentIterator) PageInfo 
    
    
    func (it *EnvironmentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## EnvironmentsCallOptions
    
    
    type EnvironmentsCallOptions struct {
    	ListEnvironments          []gax.CallOption
    	GetEnvironment            []gax.CallOption
    	CreateEnvironment         []gax.CallOption
    	UpdateEnvironment         []gax.CallOption
    	DeleteEnvironment         []gax.CallOption
    	LookupEnvironmentHistory  []gax.CallOption
    	RunContinuousTest         []gax.CallOption
    	ListContinuousTestResults []gax.CallOption
    	DeployFlow                []gax.CallOption
    	GetLocation               []gax.CallOption
    	ListLocations             []gax.CallOption
    	CancelOperation           []gax.CallOption
    	GetOperation              []gax.CallOption
    	ListOperations            []gax.CallOption
    }

EnvironmentsCallOptions contains the retry settings for each method of EnvironmentsClient.

## EnvironmentsClient
    
    
    type EnvironmentsClient struct {
    
    	// The call options for this service.
    	CallOptions *EnvironmentsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

EnvironmentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Environments.

### func NewEnvironmentsClient 
    
    
    func NewEnvironmentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*EnvironmentsClient, [error](https://pkg.go.dev/builtin#error))

NewEnvironmentsClient creates a new environments client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Environments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewEnvironmentsRESTClient 
    
    
    func NewEnvironmentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*EnvironmentsClient, [error](https://pkg.go.dev/builtin#error))

NewEnvironmentsRESTClient creates a new environments rest client.

Service for managing Environments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewEnvironmentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_EnvironmentsClient_NewEnvironmentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*EnvironmentsClient) CancelOperation 
    
    
    func (c *EnvironmentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EnvironmentsClient) Close 
    
    
    func (c *EnvironmentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*EnvironmentsClient) Connection (deprecated)
    
    
    func (c *EnvironmentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*EnvironmentsClient) CreateEnvironment 
    
    
    func (c *EnvironmentsClient) CreateEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateEnvironmentOperation, [error](https://pkg.go.dev/builtin#error))

CreateEnvironment creates an Environment in the specified Agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: Environment
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateEnvironmentRequest.
    	}
    	op, err := c.CreateEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) CreateEnvironmentOperation 
    
    
    func (c *EnvironmentsClient) CreateEnvironmentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateEnvironmentOperation

CreateEnvironmentOperation returns a new CreateEnvironmentOperation from a given name. The name must be that of a previously created CreateEnvironmentOperation, possibly from a different process.

### func (*EnvironmentsClient) DeleteEnvironment 
    
    
    func (c *EnvironmentsClient) DeleteEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteEnvironment deletes the specified Environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteEnvironmentRequest.
    	}
    	err = c.DeleteEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EnvironmentsClient) DeployFlow 
    
    
    func (c *EnvironmentsClient) DeployFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeployFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeployFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeployFlowOperation, [error](https://pkg.go.dev/builtin#error))

DeployFlow deploys a flow to the specified Environment.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    DeployFlowMetadata
    
    response:
    DeployFlowResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeployFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeployFlowRequest.
    	}
    	op, err := c.DeployFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) DeployFlowOperation 
    
    
    func (c *EnvironmentsClient) DeployFlowOperation(name [string](https://pkg.go.dev/builtin#string)) *DeployFlowOperation

DeployFlowOperation returns a new DeployFlowOperation from a given name. The name must be that of a previously created DeployFlowOperation, possibly from a different process.

### func (*EnvironmentsClient) GetEnvironment 
    
    
    func (c *EnvironmentsClient) GetEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Environment), [error](https://pkg.go.dev/builtin#error))

GetEnvironment retrieves the specified Environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetEnvironmentRequest.
    	}
    	resp, err := c.GetEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) GetLocation 
    
    
    func (c *EnvironmentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) GetOperation 
    
    
    func (c *EnvironmentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) ListContinuousTestResults 
    
    
    func (c *EnvironmentsClient) ListContinuousTestResults(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListContinuousTestResultsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListContinuousTestResultsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ContinuousTestResultIterator

ListContinuousTestResults fetches a list of continuous test results for a given environment.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListContinuousTestResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListContinuousTestResultsRequest.
    	}
    	it := c.ListContinuousTestResults(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListContinuousTestResultsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListContinuousTestResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListContinuousTestResultsRequest.
    	}
    	for resp, err := range c.ListContinuousTestResults(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) ListEnvironments 
    
    
    func (c *EnvironmentsClient) ListEnvironments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListEnvironmentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListEnvironmentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EnvironmentIterator

ListEnvironments returns the list of all environments in the specified Agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListEnvironmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListEnvironmentsRequest.
    	}
    	it := c.ListEnvironments(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListEnvironmentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListEnvironmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListEnvironmentsRequest.
    	}
    	for resp, err := range c.ListEnvironments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) ListLocations 
    
    
    func (c *EnvironmentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) ListOperations 
    
    
    func (c *EnvironmentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) LookupEnvironmentHistory 
    
    
    func (c *EnvironmentsClient) LookupEnvironmentHistory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[LookupEnvironmentHistoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_LookupEnvironmentHistoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EnvironmentIterator

LookupEnvironmentHistory looks up the history of the specified Environment.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.LookupEnvironmentHistoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#LookupEnvironmentHistoryRequest.
    	}
    	it := c.LookupEnvironmentHistory(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.LookupEnvironmentHistoryResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.LookupEnvironmentHistoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#LookupEnvironmentHistoryRequest.
    	}
    	for resp, err := range c.LookupEnvironmentHistory(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) RunContinuousTest 
    
    
    func (c *EnvironmentsClient) RunContinuousTest(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunContinuousTestRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunContinuousTestRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RunContinuousTestOperation, [error](https://pkg.go.dev/builtin#error))

RunContinuousTest kicks off a continuous test under the specified Environment.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    RunContinuousTestMetadata
    
    response:
    RunContinuousTestResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.RunContinuousTestRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#RunContinuousTestRequest.
    	}
    	op, err := c.RunContinuousTest(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) RunContinuousTestOperation 
    
    
    func (c *EnvironmentsClient) RunContinuousTestOperation(name [string](https://pkg.go.dev/builtin#string)) *RunContinuousTestOperation

RunContinuousTestOperation returns a new RunContinuousTestOperation from a given name. The name must be that of a previously created RunContinuousTestOperation, possibly from a different process.

### func (*EnvironmentsClient) UpdateEnvironment 
    
    
    func (c *EnvironmentsClient) UpdateEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateEnvironmentOperation, [error](https://pkg.go.dev/builtin#error))

UpdateEnvironment updates the specified Environment.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: Environment
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateEnvironmentRequest.
    	}
    	op, err := c.UpdateEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) UpdateEnvironmentOperation 
    
    
    func (c *EnvironmentsClient) UpdateEnvironmentOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateEnvironmentOperation

UpdateEnvironmentOperation returns a new UpdateEnvironmentOperation from a given name. The name must be that of a previously created UpdateEnvironmentOperation, possibly from a different process.

## ExampleIterator
    
    
    type ExampleIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Example, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ExampleIterator manages a stream of *cxpb.Example.

### func (*ExampleIterator) All 
    
    
    func (it *ExampleIterator) All() iter.Seq2[*cxpb.Example, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ExampleIterator) Next 
    
    
    func (it *ExampleIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Example](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Example), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ExampleIterator) PageInfo 
    
    
    func (it *ExampleIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ExamplesCallOptions
    
    
    type ExamplesCallOptions struct {
    	CreateExample   []gax.CallOption
    	DeleteExample   []gax.CallOption
    	ListExamples    []gax.CallOption
    	GetExample      []gax.CallOption
    	UpdateExample   []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

ExamplesCallOptions contains the retry settings for each method of ExamplesClient.

## ExamplesClient
    
    
    type ExamplesClient struct {
    
    	// The call options for this service.
    	CallOptions *ExamplesCallOptions
    	// contains filtered or unexported fields
    }

ExamplesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Examples.

### func NewExamplesClient 
    
    
    func NewExamplesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ExamplesClient, [error](https://pkg.go.dev/builtin#error))

NewExamplesClient creates a new examples client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Examples.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewExamplesRESTClient 
    
    
    func NewExamplesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ExamplesClient, [error](https://pkg.go.dev/builtin#error))

NewExamplesRESTClient creates a new examples rest client.

Service for managing Examples.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewExamplesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_ExamplesClient_NewExamplesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ExamplesClient) CancelOperation 
    
    
    func (c *ExamplesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ExamplesClient) Close 
    
    
    func (c *ExamplesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ExamplesClient) Connection (deprecated)
    
    
    func (c *ExamplesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ExamplesClient) CreateExample 
    
    
    func (c *ExamplesClient) CreateExample(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateExampleRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateExampleRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Example](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Example), [error](https://pkg.go.dev/builtin#error))

CreateExample creates an example in the specified playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateExampleRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateExampleRequest.
    	}
    	resp, err := c.CreateExample(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExamplesClient) DeleteExample 
    
    
    func (c *ExamplesClient) DeleteExample(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteExampleRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteExampleRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteExample deletes the specified example.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteExampleRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteExampleRequest.
    	}
    	err = c.DeleteExample(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ExamplesClient) GetExample 
    
    
    func (c *ExamplesClient) GetExample(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetExampleRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetExampleRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Example](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Example), [error](https://pkg.go.dev/builtin#error))

GetExample retrieves the specified example.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetExampleRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetExampleRequest.
    	}
    	resp, err := c.GetExample(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExamplesClient) GetLocation 
    
    
    func (c *ExamplesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExamplesClient) GetOperation 
    
    
    func (c *ExamplesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExamplesClient) ListExamples 
    
    
    func (c *ExamplesClient) ListExamples(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListExamplesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListExamplesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ExampleIterator

ListExamples returns a list of examples in the specified playbook.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListExamplesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListExamplesRequest.
    	}
    	it := c.ListExamples(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListExamplesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListExamplesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListExamplesRequest.
    	}
    	for resp, err := range c.ListExamples(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ExamplesClient) ListLocations 
    
    
    func (c *ExamplesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ExamplesClient) ListOperations 
    
    
    func (c *ExamplesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ExamplesClient) UpdateExample 
    
    
    func (c *ExamplesClient) UpdateExample(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateExampleRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateExampleRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Example](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Example), [error](https://pkg.go.dev/builtin#error))

UpdateExample update the specified example.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExamplesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateExampleRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateExampleRequest.
    	}
    	resp, err := c.UpdateExample(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ExperimentIterator
    
    
    type ExperimentIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Experiment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ExperimentIterator manages a stream of *cxpb.Experiment.

### func (*ExperimentIterator) All 
    
    
    func (it *ExperimentIterator) All() iter.Seq2[*cxpb.Experiment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ExperimentIterator) Next 
    
    
    func (it *ExperimentIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Experiment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Experiment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ExperimentIterator) PageInfo 
    
    
    func (it *ExperimentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ExperimentsCallOptions
    
    
    type ExperimentsCallOptions struct {
    	ListExperiments  []gax.CallOption
    	GetExperiment    []gax.CallOption
    	CreateExperiment []gax.CallOption
    	UpdateExperiment []gax.CallOption
    	DeleteExperiment []gax.CallOption
    	StartExperiment  []gax.CallOption
    	StopExperiment   []gax.CallOption
    	GetLocation      []gax.CallOption
    	ListLocations    []gax.CallOption
    	CancelOperation  []gax.CallOption
    	GetOperation     []gax.CallOption
    	ListOperations   []gax.CallOption
    }

ExperimentsCallOptions contains the retry settings for each method of ExperimentsClient.

## ExperimentsClient
    
    
    type ExperimentsClient struct {
    
    	// The call options for this service.
    	CallOptions *ExperimentsCallOptions
    	// contains filtered or unexported fields
    }

ExperimentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Experiments.

### func NewExperimentsClient 
    
    
    func NewExperimentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ExperimentsClient, [error](https://pkg.go.dev/builtin#error))

NewExperimentsClient creates a new experiments client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Experiments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewExperimentsRESTClient 
    
    
    func NewExperimentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ExperimentsClient, [error](https://pkg.go.dev/builtin#error))

NewExperimentsRESTClient creates a new experiments rest client.

Service for managing Experiments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewExperimentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_ExperimentsClient_NewExperimentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ExperimentsClient) CancelOperation 
    
    
    func (c *ExperimentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ExperimentsClient) Close 
    
    
    func (c *ExperimentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ExperimentsClient) Connection (deprecated)
    
    
    func (c *ExperimentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ExperimentsClient) CreateExperiment 
    
    
    func (c *ExperimentsClient) CreateExperiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateExperimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateExperimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Experiment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Experiment), [error](https://pkg.go.dev/builtin#error))

CreateExperiment creates an Experiment in the specified Environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateExperimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateExperimentRequest.
    	}
    	resp, err := c.CreateExperiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExperimentsClient) DeleteExperiment 
    
    
    func (c *ExperimentsClient) DeleteExperiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteExperimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteExperimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteExperiment deletes the specified Experiment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteExperimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteExperimentRequest.
    	}
    	err = c.DeleteExperiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ExperimentsClient) GetExperiment 
    
    
    func (c *ExperimentsClient) GetExperiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetExperimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetExperimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Experiment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Experiment), [error](https://pkg.go.dev/builtin#error))

GetExperiment retrieves the specified Experiment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetExperimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetExperimentRequest.
    	}
    	resp, err := c.GetExperiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExperimentsClient) GetLocation 
    
    
    func (c *ExperimentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExperimentsClient) GetOperation 
    
    
    func (c *ExperimentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExperimentsClient) ListExperiments 
    
    
    func (c *ExperimentsClient) ListExperiments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListExperimentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListExperimentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ExperimentIterator

ListExperiments returns the list of all experiments in the specified Environment.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListExperimentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListExperimentsRequest.
    	}
    	it := c.ListExperiments(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListExperimentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListExperimentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListExperimentsRequest.
    	}
    	for resp, err := range c.ListExperiments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ExperimentsClient) ListLocations 
    
    
    func (c *ExperimentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ExperimentsClient) ListOperations 
    
    
    func (c *ExperimentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ExperimentsClient) StartExperiment 
    
    
    func (c *ExperimentsClient) StartExperiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[StartExperimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_StartExperimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Experiment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Experiment), [error](https://pkg.go.dev/builtin#error))

StartExperiment starts the specified Experiment. This rpc only changes the state of experiment from PENDING to RUNNING.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.StartExperimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#StartExperimentRequest.
    	}
    	resp, err := c.StartExperiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExperimentsClient) StopExperiment 
    
    
    func (c *ExperimentsClient) StopExperiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[StopExperimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_StopExperimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Experiment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Experiment), [error](https://pkg.go.dev/builtin#error))

StopExperiment stops the specified Experiment. This rpc only changes the state of experiment from RUNNING to DONE.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.StopExperimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#StopExperimentRequest.
    	}
    	resp, err := c.StopExperiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ExperimentsClient) UpdateExperiment 
    
    
    func (c *ExperimentsClient) UpdateExperiment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateExperimentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateExperimentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Experiment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Experiment), [error](https://pkg.go.dev/builtin#error))

UpdateExperiment updates the specified Experiment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewExperimentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateExperimentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateExperimentRequest.
    	}
    	resp, err := c.UpdateExperiment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ExportAgentOperation
    
    
    type ExportAgentOperation struct {
    	// contains filtered or unexported fields
    }

ExportAgentOperation manages a long-running operation from ExportAgent.

### func (*ExportAgentOperation) Done 
    
    
    func (op *ExportAgentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportAgentOperation) Metadata 
    
    
    func (op *ExportAgentOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportAgentOperation) Name 
    
    
    func (op *ExportAgentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportAgentOperation) Poll 
    
    
    func (op *ExportAgentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportAgentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportAgentResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportAgentOperation) Wait 
    
    
    func (op *ExportAgentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportAgentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportAgentResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportEntityTypesOperation
    
    
    type ExportEntityTypesOperation struct {
    	// contains filtered or unexported fields
    }

ExportEntityTypesOperation manages a long-running operation from ExportEntityTypes.

### func (*ExportEntityTypesOperation) Done 
    
    
    func (op *ExportEntityTypesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportEntityTypesOperation) Metadata 
    
    
    func (op *ExportEntityTypesOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportEntityTypesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportEntityTypesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportEntityTypesOperation) Name 
    
    
    func (op *ExportEntityTypesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportEntityTypesOperation) Poll 
    
    
    func (op *ExportEntityTypesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportEntityTypesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportEntityTypesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportEntityTypesOperation) Wait 
    
    
    func (op *ExportEntityTypesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportEntityTypesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportEntityTypesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportFlowOperation
    
    
    type ExportFlowOperation struct {
    	// contains filtered or unexported fields
    }

ExportFlowOperation manages a long-running operation from ExportFlow.

### func (*ExportFlowOperation) Done 
    
    
    func (op *ExportFlowOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportFlowOperation) Metadata 
    
    
    func (op *ExportFlowOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportFlowOperation) Name 
    
    
    func (op *ExportFlowOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportFlowOperation) Poll 
    
    
    func (op *ExportFlowOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportFlowResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportFlowResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportFlowOperation) Wait 
    
    
    func (op *ExportFlowOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportFlowResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportFlowResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportIntentsOperation
    
    
    type ExportIntentsOperation struct {
    	// contains filtered or unexported fields
    }

ExportIntentsOperation manages a long-running operation from ExportIntents.

### func (*ExportIntentsOperation) Done 
    
    
    func (op *ExportIntentsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportIntentsOperation) Metadata 
    
    
    func (op *ExportIntentsOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportIntentsMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportIntentsMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportIntentsOperation) Name 
    
    
    func (op *ExportIntentsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportIntentsOperation) Poll 
    
    
    func (op *ExportIntentsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportIntentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportIntentsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportIntentsOperation) Wait 
    
    
    func (op *ExportIntentsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportIntentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportIntentsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportPlaybookOperation
    
    
    type ExportPlaybookOperation struct {
    	// contains filtered or unexported fields
    }

ExportPlaybookOperation manages a long-running operation from ExportPlaybook.

### func (*ExportPlaybookOperation) Done 
    
    
    func (op *ExportPlaybookOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportPlaybookOperation) Metadata 
    
    
    func (op *ExportPlaybookOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportPlaybookOperation) Name 
    
    
    func (op *ExportPlaybookOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportPlaybookOperation) Poll 
    
    
    func (op *ExportPlaybookOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportPlaybookResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportPlaybookResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportPlaybookOperation) Wait 
    
    
    func (op *ExportPlaybookOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportPlaybookResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportPlaybookResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportTestCasesOperation
    
    
    type ExportTestCasesOperation struct {
    	// contains filtered or unexported fields
    }

ExportTestCasesOperation manages a long-running operation from ExportTestCases.

### func (*ExportTestCasesOperation) Done 
    
    
    func (op *ExportTestCasesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportTestCasesOperation) Metadata 
    
    
    func (op *ExportTestCasesOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportTestCasesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportTestCasesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportTestCasesOperation) Name 
    
    
    func (op *ExportTestCasesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportTestCasesOperation) Poll 
    
    
    func (op *ExportTestCasesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportTestCasesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportTestCasesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportTestCasesOperation) Wait 
    
    
    func (op *ExportTestCasesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportTestCasesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportTestCasesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## FlowIterator
    
    
    type FlowIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Flow, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

FlowIterator manages a stream of *cxpb.Flow.

### func (*FlowIterator) All 
    
    
    func (it *FlowIterator) All() iter.Seq2[*cxpb.Flow, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*FlowIterator) Next 
    
    
    func (it *FlowIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Flow](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Flow), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*FlowIterator) PageInfo 
    
    
    func (it *FlowIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## FlowsCallOptions
    
    
    type FlowsCallOptions struct {
    	CreateFlow              []gax.CallOption
    	DeleteFlow              []gax.CallOption
    	ListFlows               []gax.CallOption
    	GetFlow                 []gax.CallOption
    	UpdateFlow              []gax.CallOption
    	TrainFlow               []gax.CallOption
    	ValidateFlow            []gax.CallOption
    	GetFlowValidationResult []gax.CallOption
    	ImportFlow              []gax.CallOption
    	ExportFlow              []gax.CallOption
    	GetLocation             []gax.CallOption
    	ListLocations           []gax.CallOption
    	CancelOperation         []gax.CallOption
    	GetOperation            []gax.CallOption
    	ListOperations          []gax.CallOption
    }

FlowsCallOptions contains the retry settings for each method of FlowsClient.

## FlowsClient
    
    
    type FlowsClient struct {
    
    	// The call options for this service.
    	CallOptions *FlowsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

FlowsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Flows.

### func NewFlowsClient 
    
    
    func NewFlowsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FlowsClient, [error](https://pkg.go.dev/builtin#error))

NewFlowsClient creates a new flows client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Flows.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewFlowsRESTClient 
    
    
    func NewFlowsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FlowsClient, [error](https://pkg.go.dev/builtin#error))

NewFlowsRESTClient creates a new flows rest client.

Service for managing Flows.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewFlowsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_FlowsClient_NewFlowsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*FlowsClient) CancelOperation 
    
    
    func (c *FlowsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FlowsClient) Close 
    
    
    func (c *FlowsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*FlowsClient) Connection (deprecated)
    
    
    func (c *FlowsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*FlowsClient) CreateFlow 
    
    
    func (c *FlowsClient) CreateFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Flow](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Flow), [error](https://pkg.go.dev/builtin#error))

CreateFlow creates a flow in the specified agent.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateFlowRequest.
    	}
    	resp, err := c.CreateFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) DeleteFlow 
    
    
    func (c *FlowsClient) DeleteFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteFlow deletes a specified flow.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteFlowRequest.
    	}
    	err = c.DeleteFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FlowsClient) ExportFlow 
    
    
    func (c *FlowsClient) ExportFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportFlowOperation, [error](https://pkg.go.dev/builtin#error))

ExportFlow exports the specified flow to a binary file.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response:
    ExportFlowResponse
    

Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ExportFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ExportFlowRequest.
    	}
    	op, err := c.ExportFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) ExportFlowOperation 
    
    
    func (c *FlowsClient) ExportFlowOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportFlowOperation

ExportFlowOperation returns a new ExportFlowOperation from a given name. The name must be that of a previously created ExportFlowOperation, possibly from a different process.

### func (*FlowsClient) GetFlow 
    
    
    func (c *FlowsClient) GetFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Flow](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Flow), [error](https://pkg.go.dev/builtin#error))

GetFlow retrieves the specified flow.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetFlowRequest.
    	}
    	resp, err := c.GetFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) GetFlowValidationResult 
    
    
    func (c *FlowsClient) GetFlowValidationResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetFlowValidationResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetFlowValidationResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[FlowValidationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_FlowValidationResult), [error](https://pkg.go.dev/builtin#error))

GetFlowValidationResult gets the latest flow validation result. Flow validation is performed when ValidateFlow is called.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetFlowValidationResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetFlowValidationResultRequest.
    	}
    	resp, err := c.GetFlowValidationResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) GetLocation 
    
    
    func (c *FlowsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) GetOperation 
    
    
    func (c *FlowsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) ImportFlow 
    
    
    func (c *FlowsClient) ImportFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportFlowOperation, [error](https://pkg.go.dev/builtin#error))

ImportFlow imports the specified flow to the specified agent from a binary file.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response:
    ImportFlowResponse
    

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ImportFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ImportFlowRequest.
    	}
    	op, err := c.ImportFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) ImportFlowOperation 
    
    
    func (c *FlowsClient) ImportFlowOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportFlowOperation

ImportFlowOperation returns a new ImportFlowOperation from a given name. The name must be that of a previously created ImportFlowOperation, possibly from a different process.

### func (*FlowsClient) ListFlows 
    
    
    func (c *FlowsClient) ListFlows(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListFlowsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListFlowsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *FlowIterator

ListFlows returns the list of all flows in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListFlowsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListFlowsRequest.
    	}
    	it := c.ListFlows(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListFlowsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListFlowsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListFlowsRequest.
    	}
    	for resp, err := range c.ListFlows(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FlowsClient) ListLocations 
    
    
    func (c *FlowsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FlowsClient) ListOperations 
    
    
    func (c *FlowsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FlowsClient) TrainFlow 
    
    
    func (c *FlowsClient) TrainFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TrainFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TrainFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*TrainFlowOperation, [error](https://pkg.go.dev/builtin#error))

TrainFlow trains the specified flow. Note that only the flow in ‘draft’ environment is trained.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.TrainFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#TrainFlowRequest.
    	}
    	op, err := c.TrainFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FlowsClient) TrainFlowOperation 
    
    
    func (c *FlowsClient) TrainFlowOperation(name [string](https://pkg.go.dev/builtin#string)) *TrainFlowOperation

TrainFlowOperation returns a new TrainFlowOperation from a given name. The name must be that of a previously created TrainFlowOperation, possibly from a different process.

### func (*FlowsClient) UpdateFlow 
    
    
    func (c *FlowsClient) UpdateFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Flow](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Flow), [error](https://pkg.go.dev/builtin#error))

UpdateFlow updates the specified flow.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateFlowRequest.
    	}
    	resp, err := c.UpdateFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FlowsClient) ValidateFlow 
    
    
    func (c *FlowsClient) ValidateFlow(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ValidateFlowRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ValidateFlowRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[FlowValidationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_FlowValidationResult), [error](https://pkg.go.dev/builtin#error))

ValidateFlow validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewFlowsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ValidateFlowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ValidateFlowRequest.
    	}
    	resp, err := c.ValidateFlow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## GeneratorIterator
    
    
    type GeneratorIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Generator, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GeneratorIterator manages a stream of *cxpb.Generator.

### func (*GeneratorIterator) All 
    
    
    func (it *GeneratorIterator) All() iter.Seq2[*cxpb.Generator, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GeneratorIterator) Next 
    
    
    func (it *GeneratorIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Generator), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GeneratorIterator) PageInfo 
    
    
    func (it *GeneratorIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GeneratorsCallOptions
    
    
    type GeneratorsCallOptions struct {
    	ListGenerators  []gax.CallOption
    	GetGenerator    []gax.CallOption
    	CreateGenerator []gax.CallOption
    	UpdateGenerator []gax.CallOption
    	DeleteGenerator []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

GeneratorsCallOptions contains the retry settings for each method of GeneratorsClient.

## GeneratorsClient
    
    
    type GeneratorsClient struct {
    
    	// The call options for this service.
    	CallOptions *GeneratorsCallOptions
    	// contains filtered or unexported fields
    }

GeneratorsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Generators

### func NewGeneratorsClient 
    
    
    func NewGeneratorsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GeneratorsClient, [error](https://pkg.go.dev/builtin#error))

NewGeneratorsClient creates a new generators client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Generators

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewGeneratorsRESTClient 
    
    
    func NewGeneratorsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GeneratorsClient, [error](https://pkg.go.dev/builtin#error))

NewGeneratorsRESTClient creates a new generators rest client.

Service for managing Generators

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewGeneratorsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_GeneratorsClient_NewGeneratorsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*GeneratorsClient) CancelOperation 
    
    
    func (c *GeneratorsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GeneratorsClient) Close 
    
    
    func (c *GeneratorsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*GeneratorsClient) Connection (deprecated)
    
    
    func (c *GeneratorsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*GeneratorsClient) CreateGenerator 
    
    
    func (c *GeneratorsClient) CreateGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Generator), [error](https://pkg.go.dev/builtin#error))

CreateGenerator creates a generator in the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateGeneratorRequest.
    	}
    	resp, err := c.CreateGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorsClient) DeleteGenerator 
    
    
    func (c *GeneratorsClient) DeleteGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteGenerator deletes the specified generators.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteGeneratorRequest.
    	}
    	err = c.DeleteGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GeneratorsClient) GetGenerator 
    
    
    func (c *GeneratorsClient) GetGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Generator), [error](https://pkg.go.dev/builtin#error))

GetGenerator retrieves the specified generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetGeneratorRequest.
    	}
    	resp, err := c.GetGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorsClient) GetLocation 
    
    
    func (c *GeneratorsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorsClient) GetOperation 
    
    
    func (c *GeneratorsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorsClient) ListGenerators 
    
    
    func (c *GeneratorsClient) ListGenerators(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListGeneratorsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListGeneratorsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GeneratorIterator

ListGenerators returns the list of all generators in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListGeneratorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListGeneratorsRequest.
    	}
    	it := c.ListGenerators(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListGeneratorsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListGeneratorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListGeneratorsRequest.
    	}
    	for resp, err := range c.ListGenerators(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GeneratorsClient) ListLocations 
    
    
    func (c *GeneratorsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GeneratorsClient) ListOperations 
    
    
    func (c *GeneratorsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GeneratorsClient) UpdateGenerator 
    
    
    func (c *GeneratorsClient) UpdateGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Generator), [error](https://pkg.go.dev/builtin#error))

UpdateGenerator update the specified generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateGeneratorRequest.
    	}
    	resp, err := c.UpdateGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ImportEntityTypesOperation
    
    
    type ImportEntityTypesOperation struct {
    	// contains filtered or unexported fields
    }

ImportEntityTypesOperation manages a long-running operation from ImportEntityTypes.

### func (*ImportEntityTypesOperation) Done 
    
    
    func (op *ImportEntityTypesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportEntityTypesOperation) Metadata 
    
    
    func (op *ImportEntityTypesOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportEntityTypesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportEntityTypesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportEntityTypesOperation) Name 
    
    
    func (op *ImportEntityTypesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportEntityTypesOperation) Poll 
    
    
    func (op *ImportEntityTypesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportEntityTypesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportEntityTypesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportEntityTypesOperation) Wait 
    
    
    func (op *ImportEntityTypesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportEntityTypesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportEntityTypesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportFlowOperation
    
    
    type ImportFlowOperation struct {
    	// contains filtered or unexported fields
    }

ImportFlowOperation manages a long-running operation from ImportFlow.

### func (*ImportFlowOperation) Done 
    
    
    func (op *ImportFlowOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportFlowOperation) Metadata 
    
    
    func (op *ImportFlowOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportFlowOperation) Name 
    
    
    func (op *ImportFlowOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportFlowOperation) Poll 
    
    
    func (op *ImportFlowOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportFlowResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportFlowResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportFlowOperation) Wait 
    
    
    func (op *ImportFlowOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportFlowResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportFlowResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportIntentsOperation
    
    
    type ImportIntentsOperation struct {
    	// contains filtered or unexported fields
    }

ImportIntentsOperation manages a long-running operation from ImportIntents.

### func (*ImportIntentsOperation) Done 
    
    
    func (op *ImportIntentsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportIntentsOperation) Metadata 
    
    
    func (op *ImportIntentsOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportIntentsMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportIntentsMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportIntentsOperation) Name 
    
    
    func (op *ImportIntentsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportIntentsOperation) Poll 
    
    
    func (op *ImportIntentsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportIntentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportIntentsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportIntentsOperation) Wait 
    
    
    func (op *ImportIntentsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportIntentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportIntentsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportPlaybookOperation
    
    
    type ImportPlaybookOperation struct {
    	// contains filtered or unexported fields
    }

ImportPlaybookOperation manages a long-running operation from ImportPlaybook.

### func (*ImportPlaybookOperation) Done 
    
    
    func (op *ImportPlaybookOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportPlaybookOperation) Metadata 
    
    
    func (op *ImportPlaybookOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportPlaybookOperation) Name 
    
    
    func (op *ImportPlaybookOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportPlaybookOperation) Poll 
    
    
    func (op *ImportPlaybookOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportPlaybookResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportPlaybookResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportPlaybookOperation) Wait 
    
    
    func (op *ImportPlaybookOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportPlaybookResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportPlaybookResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportTestCasesOperation
    
    
    type ImportTestCasesOperation struct {
    	// contains filtered or unexported fields
    }

ImportTestCasesOperation manages a long-running operation from ImportTestCases.

### func (*ImportTestCasesOperation) Done 
    
    
    func (op *ImportTestCasesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportTestCasesOperation) Metadata 
    
    
    func (op *ImportTestCasesOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportTestCasesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportTestCasesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportTestCasesOperation) Name 
    
    
    func (op *ImportTestCasesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportTestCasesOperation) Poll 
    
    
    func (op *ImportTestCasesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportTestCasesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportTestCasesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportTestCasesOperation) Wait 
    
    
    func (op *ImportTestCasesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportTestCasesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportTestCasesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## IntentIterator
    
    
    type IntentIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Intent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

IntentIterator manages a stream of *cxpb.Intent.

### func (*IntentIterator) All 
    
    
    func (it *IntentIterator) All() iter.Seq2[*cxpb.Intent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*IntentIterator) Next 
    
    
    func (it *IntentIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Intent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*IntentIterator) PageInfo 
    
    
    func (it *IntentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## IntentsCallOptions
    
    
    type IntentsCallOptions struct {
    	ListIntents     []gax.CallOption
    	GetIntent       []gax.CallOption
    	CreateIntent    []gax.CallOption
    	UpdateIntent    []gax.CallOption
    	DeleteIntent    []gax.CallOption
    	ImportIntents   []gax.CallOption
    	ExportIntents   []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

IntentsCallOptions contains the retry settings for each method of IntentsClient.

## IntentsClient
    
    
    type IntentsClient struct {
    
    	// The call options for this service.
    	CallOptions *IntentsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

IntentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Intents.

### func NewIntentsClient 
    
    
    func NewIntentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*IntentsClient, [error](https://pkg.go.dev/builtin#error))

NewIntentsClient creates a new intents client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Intents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewIntentsRESTClient 
    
    
    func NewIntentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*IntentsClient, [error](https://pkg.go.dev/builtin#error))

NewIntentsRESTClient creates a new intents rest client.

Service for managing Intents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewIntentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_IntentsClient_NewIntentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*IntentsClient) CancelOperation 
    
    
    func (c *IntentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*IntentsClient) Close 
    
    
    func (c *IntentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*IntentsClient) Connection (deprecated)
    
    
    func (c *IntentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*IntentsClient) CreateIntent 
    
    
    func (c *IntentsClient) CreateIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Intent), [error](https://pkg.go.dev/builtin#error))

CreateIntent creates an intent in the specified agent.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateIntentRequest.
    	}
    	resp, err := c.CreateIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) DeleteIntent 
    
    
    func (c *IntentsClient) DeleteIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteIntent deletes the specified intent.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteIntentRequest.
    	}
    	err = c.DeleteIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*IntentsClient) ExportIntents 
    
    
    func (c *IntentsClient) ExportIntents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportIntentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportIntentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportIntentsOperation, [error](https://pkg.go.dev/builtin#error))

ExportIntents exports the selected intents.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    ExportIntentsMetadata
    
    response:
    ExportIntentsResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ExportIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ExportIntentsRequest.
    	}
    	op, err := c.ExportIntents(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) ExportIntentsOperation 
    
    
    func (c *IntentsClient) ExportIntentsOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportIntentsOperation

ExportIntentsOperation returns a new ExportIntentsOperation from a given name. The name must be that of a previously created ExportIntentsOperation, possibly from a different process.

### func (*IntentsClient) GetIntent 
    
    
    func (c *IntentsClient) GetIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Intent), [error](https://pkg.go.dev/builtin#error))

GetIntent retrieves the specified intent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetIntentRequest.
    	}
    	resp, err := c.GetIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) GetLocation 
    
    
    func (c *IntentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) GetOperation 
    
    
    func (c *IntentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) ImportIntents 
    
    
    func (c *IntentsClient) ImportIntents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportIntentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportIntentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportIntentsOperation, [error](https://pkg.go.dev/builtin#error))

ImportIntents imports the specified intents into the agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    ImportIntentsMetadata
    
    response:
    ImportIntentsResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ImportIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ImportIntentsRequest.
    	}
    	op, err := c.ImportIntents(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) ImportIntentsOperation 
    
    
    func (c *IntentsClient) ImportIntentsOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportIntentsOperation

ImportIntentsOperation returns a new ImportIntentsOperation from a given name. The name must be that of a previously created ImportIntentsOperation, possibly from a different process.

### func (*IntentsClient) ListIntents 
    
    
    func (c *IntentsClient) ListIntents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListIntentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListIntentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *IntentIterator

ListIntents returns the list of all intents in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListIntentsRequest.
    	}
    	it := c.ListIntents(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListIntentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListIntentsRequest.
    	}
    	for resp, err := range c.ListIntents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*IntentsClient) ListLocations 
    
    
    func (c *IntentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*IntentsClient) ListOperations 
    
    
    func (c *IntentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*IntentsClient) UpdateIntent 
    
    
    func (c *IntentsClient) UpdateIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Intent), [error](https://pkg.go.dev/builtin#error))

UpdateIntent updates the specified intent.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateIntentRequest.
    	}
    	resp, err := c.UpdateIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## LoadVersionOperation
    
    
    type LoadVersionOperation struct {
    	// contains filtered or unexported fields
    }

LoadVersionOperation manages a long-running operation from LoadVersion.

### func (*LoadVersionOperation) Done 
    
    
    func (op *LoadVersionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*LoadVersionOperation) Metadata 
    
    
    func (op *LoadVersionOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*LoadVersionOperation) Name 
    
    
    func (op *LoadVersionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*LoadVersionOperation) Poll 
    
    
    func (op *LoadVersionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*LoadVersionOperation) Wait 
    
    
    func (op *LoadVersionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## LocationIterator
    
    
    type LocationIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*locationpb.Location, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

LocationIterator manages a stream of *locationpb.Location.

### func (*LocationIterator) All 
    
    
    func (it *LocationIterator) All() iter.Seq2[*locationpb.Location, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*LocationIterator) Next 
    
    
    func (it *LocationIterator) Next() (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*LocationIterator) PageInfo 
    
    
    func (it *LocationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## OperationIterator
    
    
    type OperationIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*longrunningpb.Operation, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

OperationIterator manages a stream of *longrunningpb.Operation.

### func (*OperationIterator) All 
    
    
    func (it *OperationIterator) All() iter.Seq2[*longrunningpb.Operation, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*OperationIterator) Next 
    
    
    func (it *OperationIterator) Next() (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*OperationIterator) PageInfo 
    
    
    func (it *OperationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PageIterator
    
    
    type PageIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Page, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PageIterator manages a stream of *cxpb.Page.

### func (*PageIterator) All 
    
    
    func (it *PageIterator) All() iter.Seq2[*cxpb.Page, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PageIterator) Next 
    
    
    func (it *PageIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Page](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Page), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PageIterator) PageInfo 
    
    
    func (it *PageIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PagesCallOptions
    
    
    type PagesCallOptions struct {
    	ListPages       []gax.CallOption
    	GetPage         []gax.CallOption
    	CreatePage      []gax.CallOption
    	UpdatePage      []gax.CallOption
    	DeletePage      []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

PagesCallOptions contains the retry settings for each method of PagesClient.

## PagesClient
    
    
    type PagesClient struct {
    
    	// The call options for this service.
    	CallOptions *PagesCallOptions
    	// contains filtered or unexported fields
    }

PagesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing [Pages][google.cloud.dialogflow.cx.v3.Page (at <http://google.cloud.dialogflow.cx.v3.Page>)].

### func NewPagesClient 
    
    
    func NewPagesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PagesClient, [error](https://pkg.go.dev/builtin#error))

NewPagesClient creates a new pages client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing [Pages][google.cloud.dialogflow.cx.v3.Page (at <http://google.cloud.dialogflow.cx.v3.Page>)].

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewPagesRESTClient 
    
    
    func NewPagesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PagesClient, [error](https://pkg.go.dev/builtin#error))

NewPagesRESTClient creates a new pages rest client.

Service for managing [Pages][google.cloud.dialogflow.cx.v3.Page (at <http://google.cloud.dialogflow.cx.v3.Page>)].

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewPagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_PagesClient_NewPagesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*PagesClient) CancelOperation 
    
    
    func (c *PagesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PagesClient) Close 
    
    
    func (c *PagesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*PagesClient) Connection (deprecated)
    
    
    func (c *PagesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*PagesClient) CreatePage 
    
    
    func (c *PagesClient) CreatePage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreatePageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreatePageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Page](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Page), [error](https://pkg.go.dev/builtin#error))

CreatePage creates a page in the specified flow.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreatePageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreatePageRequest.
    	}
    	resp, err := c.CreatePage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PagesClient) DeletePage 
    
    
    func (c *PagesClient) DeletePage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeletePageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeletePageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeletePage deletes the specified page.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeletePageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeletePageRequest.
    	}
    	err = c.DeletePage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PagesClient) GetLocation 
    
    
    func (c *PagesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PagesClient) GetOperation 
    
    
    func (c *PagesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PagesClient) GetPage 
    
    
    func (c *PagesClient) GetPage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetPageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetPageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Page](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Page), [error](https://pkg.go.dev/builtin#error))

GetPage retrieves the specified page.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetPageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetPageRequest.
    	}
    	resp, err := c.GetPage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PagesClient) ListLocations 
    
    
    func (c *PagesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PagesClient) ListOperations 
    
    
    func (c *PagesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PagesClient) ListPages 
    
    
    func (c *PagesClient) ListPages(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListPagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListPagesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PageIterator

ListPages returns the list of all pages in the specified flow.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListPagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListPagesRequest.
    	}
    	it := c.ListPages(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListPagesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListPagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListPagesRequest.
    	}
    	for resp, err := range c.ListPages(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PagesClient) UpdatePage 
    
    
    func (c *PagesClient) UpdatePage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdatePageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdatePageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Page](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Page), [error](https://pkg.go.dev/builtin#error))

UpdatePage updates the specified page.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPagesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdatePageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdatePageRequest.
    	}
    	resp, err := c.UpdatePage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## PlaybookIterator
    
    
    type PlaybookIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Playbook, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PlaybookIterator manages a stream of *cxpb.Playbook.

### func (*PlaybookIterator) All 
    
    
    func (it *PlaybookIterator) All() iter.Seq2[*cxpb.Playbook, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PlaybookIterator) Next 
    
    
    func (it *PlaybookIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Playbook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Playbook), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PlaybookIterator) PageInfo 
    
    
    func (it *PlaybookIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PlaybookVersionIterator
    
    
    type PlaybookVersionIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.PlaybookVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PlaybookVersionIterator manages a stream of *cxpb.PlaybookVersion.

### func (*PlaybookVersionIterator) All 
    
    
    func (it *PlaybookVersionIterator) All() iter.Seq2[*cxpb.PlaybookVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PlaybookVersionIterator) Next 
    
    
    func (it *PlaybookVersionIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[PlaybookVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_PlaybookVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PlaybookVersionIterator) PageInfo 
    
    
    func (it *PlaybookVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PlaybooksCallOptions
    
    
    type PlaybooksCallOptions struct {
    	CreatePlaybook         []gax.CallOption
    	DeletePlaybook         []gax.CallOption
    	ListPlaybooks          []gax.CallOption
    	GetPlaybook            []gax.CallOption
    	ExportPlaybook         []gax.CallOption
    	ImportPlaybook         []gax.CallOption
    	UpdatePlaybook         []gax.CallOption
    	CreatePlaybookVersion  []gax.CallOption
    	GetPlaybookVersion     []gax.CallOption
    	RestorePlaybookVersion []gax.CallOption
    	ListPlaybookVersions   []gax.CallOption
    	DeletePlaybookVersion  []gax.CallOption
    	GetLocation            []gax.CallOption
    	ListLocations          []gax.CallOption
    	CancelOperation        []gax.CallOption
    	GetOperation           []gax.CallOption
    	ListOperations         []gax.CallOption
    }

PlaybooksCallOptions contains the retry settings for each method of PlaybooksClient.

## PlaybooksClient
    
    
    type PlaybooksClient struct {
    
    	// The call options for this service.
    	CallOptions *PlaybooksCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

PlaybooksClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Playbooks.

### func NewPlaybooksClient 
    
    
    func NewPlaybooksClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PlaybooksClient, [error](https://pkg.go.dev/builtin#error))

NewPlaybooksClient creates a new playbooks client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Playbooks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewPlaybooksRESTClient 
    
    
    func NewPlaybooksRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PlaybooksClient, [error](https://pkg.go.dev/builtin#error))

NewPlaybooksRESTClient creates a new playbooks rest client.

Service for managing Playbooks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewPlaybooksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_PlaybooksClient_NewPlaybooksRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*PlaybooksClient) CancelOperation 
    
    
    func (c *PlaybooksClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PlaybooksClient) Close 
    
    
    func (c *PlaybooksClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*PlaybooksClient) Connection (deprecated)
    
    
    func (c *PlaybooksClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*PlaybooksClient) CreatePlaybook 
    
    
    func (c *PlaybooksClient) CreatePlaybook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreatePlaybookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreatePlaybookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Playbook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Playbook), [error](https://pkg.go.dev/builtin#error))

CreatePlaybook creates a playbook in a specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreatePlaybookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreatePlaybookRequest.
    	}
    	resp, err := c.CreatePlaybook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) CreatePlaybookVersion 
    
    
    func (c *PlaybooksClient) CreatePlaybookVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreatePlaybookVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreatePlaybookVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[PlaybookVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_PlaybookVersion), [error](https://pkg.go.dev/builtin#error))

CreatePlaybookVersion creates a version for the specified Playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreatePlaybookVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreatePlaybookVersionRequest.
    	}
    	resp, err := c.CreatePlaybookVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) DeletePlaybook 
    
    
    func (c *PlaybooksClient) DeletePlaybook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeletePlaybookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeletePlaybookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeletePlaybook deletes a specified playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeletePlaybookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeletePlaybookRequest.
    	}
    	err = c.DeletePlaybook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PlaybooksClient) DeletePlaybookVersion 
    
    
    func (c *PlaybooksClient) DeletePlaybookVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeletePlaybookVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeletePlaybookVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeletePlaybookVersion deletes the specified version of the Playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeletePlaybookVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeletePlaybookVersionRequest.
    	}
    	err = c.DeletePlaybookVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PlaybooksClient) ExportPlaybook 
    
    
    func (c *PlaybooksClient) ExportPlaybook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportPlaybookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportPlaybookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportPlaybookOperation, [error](https://pkg.go.dev/builtin#error))

ExportPlaybook exports the specified playbook to a binary file.

Note that resources (e.g. examples, tools) that the playbook references will also be exported.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ExportPlaybookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ExportPlaybookRequest.
    	}
    	op, err := c.ExportPlaybook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) ExportPlaybookOperation 
    
    
    func (c *PlaybooksClient) ExportPlaybookOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportPlaybookOperation

ExportPlaybookOperation returns a new ExportPlaybookOperation from a given name. The name must be that of a previously created ExportPlaybookOperation, possibly from a different process.

### func (*PlaybooksClient) GetLocation 
    
    
    func (c *PlaybooksClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) GetOperation 
    
    
    func (c *PlaybooksClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) GetPlaybook 
    
    
    func (c *PlaybooksClient) GetPlaybook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetPlaybookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetPlaybookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Playbook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Playbook), [error](https://pkg.go.dev/builtin#error))

GetPlaybook retrieves the specified Playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetPlaybookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetPlaybookRequest.
    	}
    	resp, err := c.GetPlaybook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) GetPlaybookVersion 
    
    
    func (c *PlaybooksClient) GetPlaybookVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetPlaybookVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetPlaybookVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[PlaybookVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_PlaybookVersion), [error](https://pkg.go.dev/builtin#error))

GetPlaybookVersion retrieves the specified version of the Playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetPlaybookVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetPlaybookVersionRequest.
    	}
    	resp, err := c.GetPlaybookVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) ImportPlaybook 
    
    
    func (c *PlaybooksClient) ImportPlaybook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportPlaybookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportPlaybookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportPlaybookOperation, [error](https://pkg.go.dev/builtin#error))

ImportPlaybook imports the specified playbook to the specified agent from a binary file.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ImportPlaybookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ImportPlaybookRequest.
    	}
    	op, err := c.ImportPlaybook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) ImportPlaybookOperation 
    
    
    func (c *PlaybooksClient) ImportPlaybookOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportPlaybookOperation

ImportPlaybookOperation returns a new ImportPlaybookOperation from a given name. The name must be that of a previously created ImportPlaybookOperation, possibly from a different process.

### func (*PlaybooksClient) ListLocations 
    
    
    func (c *PlaybooksClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PlaybooksClient) ListOperations 
    
    
    func (c *PlaybooksClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PlaybooksClient) ListPlaybookVersions 
    
    
    func (c *PlaybooksClient) ListPlaybookVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListPlaybookVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListPlaybookVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PlaybookVersionIterator

ListPlaybookVersions lists versions for the specified Playbook.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListPlaybookVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListPlaybookVersionsRequest.
    	}
    	it := c.ListPlaybookVersions(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListPlaybookVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListPlaybookVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListPlaybookVersionsRequest.
    	}
    	for resp, err := range c.ListPlaybookVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PlaybooksClient) ListPlaybooks 
    
    
    func (c *PlaybooksClient) ListPlaybooks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListPlaybooksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListPlaybooksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PlaybookIterator

ListPlaybooks returns a list of playbooks in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListPlaybooksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListPlaybooksRequest.
    	}
    	it := c.ListPlaybooks(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListPlaybooksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListPlaybooksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListPlaybooksRequest.
    	}
    	for resp, err := range c.ListPlaybooks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PlaybooksClient) RestorePlaybookVersion 
    
    
    func (c *PlaybooksClient) RestorePlaybookVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RestorePlaybookVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RestorePlaybookVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RestorePlaybookVersionResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RestorePlaybookVersionResponse), [error](https://pkg.go.dev/builtin#error))

RestorePlaybookVersion retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.RestorePlaybookVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#RestorePlaybookVersionRequest.
    	}
    	resp, err := c.RestorePlaybookVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PlaybooksClient) UpdatePlaybook 
    
    
    func (c *PlaybooksClient) UpdatePlaybook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdatePlaybookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdatePlaybookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Playbook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Playbook), [error](https://pkg.go.dev/builtin#error))

UpdatePlaybook updates the specified Playbook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewPlaybooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdatePlaybookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdatePlaybookRequest.
    	}
    	resp, err := c.UpdatePlaybook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## RestoreAgentOperation
    
    
    type RestoreAgentOperation struct {
    	// contains filtered or unexported fields
    }

RestoreAgentOperation manages a long-running operation from RestoreAgent.

### func (*RestoreAgentOperation) Done 
    
    
    func (op *RestoreAgentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RestoreAgentOperation) Metadata 
    
    
    func (op *RestoreAgentOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RestoreAgentOperation) Name 
    
    
    func (op *RestoreAgentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RestoreAgentOperation) Poll 
    
    
    func (op *RestoreAgentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RestoreAgentOperation) Wait 
    
    
    func (op *RestoreAgentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RunContinuousTestOperation
    
    
    type RunContinuousTestOperation struct {
    	// contains filtered or unexported fields
    }

RunContinuousTestOperation manages a long-running operation from RunContinuousTest.

### func (*RunContinuousTestOperation) Done 
    
    
    func (op *RunContinuousTestOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RunContinuousTestOperation) Metadata 
    
    
    func (op *RunContinuousTestOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunContinuousTestMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunContinuousTestMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RunContinuousTestOperation) Name 
    
    
    func (op *RunContinuousTestOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RunContinuousTestOperation) Poll 
    
    
    func (op *RunContinuousTestOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunContinuousTestResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunContinuousTestResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RunContinuousTestOperation) Wait 
    
    
    func (op *RunContinuousTestOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunContinuousTestResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunContinuousTestResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RunTestCaseOperation
    
    
    type RunTestCaseOperation struct {
    	// contains filtered or unexported fields
    }

RunTestCaseOperation manages a long-running operation from RunTestCase.

### func (*RunTestCaseOperation) Done 
    
    
    func (op *RunTestCaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RunTestCaseOperation) Metadata 
    
    
    func (op *RunTestCaseOperation) Metadata() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunTestCaseMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunTestCaseMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RunTestCaseOperation) Name 
    
    
    func (op *RunTestCaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RunTestCaseOperation) Poll 
    
    
    func (op *RunTestCaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunTestCaseResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunTestCaseResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RunTestCaseOperation) Wait 
    
    
    func (op *RunTestCaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunTestCaseResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunTestCaseResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SecuritySettingsCallOptions
    
    
    type SecuritySettingsCallOptions struct {
    	CreateSecuritySettings []gax.CallOption
    	GetSecuritySettings    []gax.CallOption
    	UpdateSecuritySettings []gax.CallOption
    	ListSecuritySettings   []gax.CallOption
    	DeleteSecuritySettings []gax.CallOption
    	GetLocation            []gax.CallOption
    	ListLocations          []gax.CallOption
    	CancelOperation        []gax.CallOption
    	GetOperation           []gax.CallOption
    	ListOperations         []gax.CallOption
    }

SecuritySettingsCallOptions contains the retry settings for each method of SecuritySettingsClient.

## SecuritySettingsClient
    
    
    type SecuritySettingsClient struct {
    
    	// The call options for this service.
    	CallOptions *SecuritySettingsCallOptions
    	// contains filtered or unexported fields
    }

SecuritySettingsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing security settings for Dialogflow.

### func NewSecuritySettingsClient 
    
    
    func NewSecuritySettingsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SecuritySettingsClient, [error](https://pkg.go.dev/builtin#error))

NewSecuritySettingsClient creates a new security settings service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing security settings for Dialogflow.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSecuritySettingsRESTClient 
    
    
    func NewSecuritySettingsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SecuritySettingsClient, [error](https://pkg.go.dev/builtin#error))

NewSecuritySettingsRESTClient creates a new security settings service rest client.

Service for managing security settings for Dialogflow.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SecuritySettingsClient) CancelOperation 
    
    
    func (c *SecuritySettingsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SecuritySettingsClient) Close 
    
    
    func (c *SecuritySettingsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SecuritySettingsClient) Connection (deprecated)
    
    
    func (c *SecuritySettingsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SecuritySettingsClient) CreateSecuritySettings 
    
    
    func (c *SecuritySettingsClient) CreateSecuritySettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateSecuritySettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateSecuritySettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SecuritySettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SecuritySettings), [error](https://pkg.go.dev/builtin#error))

CreateSecuritySettings create security settings in the specified location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateSecuritySettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateSecuritySettingsRequest.
    	}
    	resp, err := c.CreateSecuritySettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SecuritySettingsClient) DeleteSecuritySettings 
    
    
    func (c *SecuritySettingsClient) DeleteSecuritySettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteSecuritySettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteSecuritySettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteSecuritySettings deletes the specified SecuritySettings.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteSecuritySettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteSecuritySettingsRequest.
    	}
    	err = c.DeleteSecuritySettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SecuritySettingsClient) GetLocation 
    
    
    func (c *SecuritySettingsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SecuritySettingsClient) GetOperation 
    
    
    func (c *SecuritySettingsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SecuritySettingsClient) GetSecuritySettings 
    
    
    func (c *SecuritySettingsClient) GetSecuritySettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetSecuritySettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetSecuritySettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SecuritySettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SecuritySettings), [error](https://pkg.go.dev/builtin#error))

GetSecuritySettings retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetSecuritySettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetSecuritySettingsRequest.
    	}
    	resp, err := c.GetSecuritySettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SecuritySettingsClient) ListLocations 
    
    
    func (c *SecuritySettingsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SecuritySettingsClient) ListOperations 
    
    
    func (c *SecuritySettingsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SecuritySettingsClient) ListSecuritySettings 
    
    
    func (c *SecuritySettingsClient) ListSecuritySettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListSecuritySettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListSecuritySettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SecuritySettingsIterator

ListSecuritySettings returns the list of all security settings in the specified location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListSecuritySettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListSecuritySettingsRequest.
    	}
    	it := c.ListSecuritySettings(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListSecuritySettingsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListSecuritySettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListSecuritySettingsRequest.
    	}
    	for resp, err := range c.ListSecuritySettings(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SecuritySettingsClient) UpdateSecuritySettings 
    
    
    func (c *SecuritySettingsClient) UpdateSecuritySettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateSecuritySettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SecuritySettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SecuritySettings), [error](https://pkg.go.dev/builtin#error))

UpdateSecuritySettings updates the specified SecuritySettings.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSecuritySettingsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SecuritySettingsClient_NewSecuritySettingsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateSecuritySettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateSecuritySettingsRequest.
    	}
    	resp, err := c.UpdateSecuritySettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## SecuritySettingsIterator
    
    
    type SecuritySettingsIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.SecuritySettings, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SecuritySettingsIterator manages a stream of *cxpb.SecuritySettings.

### func (*SecuritySettingsIterator) All 
    
    
    func (it *SecuritySettingsIterator) All() iter.Seq2[*cxpb.SecuritySettings, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SecuritySettingsIterator) Next 
    
    
    func (it *SecuritySettingsIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SecuritySettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SecuritySettings), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SecuritySettingsIterator) PageInfo 
    
    
    func (it *SecuritySettingsIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SessionEntityTypeIterator
    
    
    type SessionEntityTypeIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.SessionEntityType, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SessionEntityTypeIterator manages a stream of *cxpb.SessionEntityType.

### func (*SessionEntityTypeIterator) All 
    
    
    func (it *SessionEntityTypeIterator) All() iter.Seq2[*cxpb.SessionEntityType, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SessionEntityTypeIterator) Next 
    
    
    func (it *SessionEntityTypeIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SessionEntityTypeIterator) PageInfo 
    
    
    func (it *SessionEntityTypeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SessionEntityTypesCallOptions
    
    
    type SessionEntityTypesCallOptions struct {
    	ListSessionEntityTypes  []gax.CallOption
    	GetSessionEntityType    []gax.CallOption
    	CreateSessionEntityType []gax.CallOption
    	UpdateSessionEntityType []gax.CallOption
    	DeleteSessionEntityType []gax.CallOption
    	GetLocation             []gax.CallOption
    	ListLocations           []gax.CallOption
    	CancelOperation         []gax.CallOption
    	GetOperation            []gax.CallOption
    	ListOperations          []gax.CallOption
    }

SessionEntityTypesCallOptions contains the retry settings for each method of SessionEntityTypesClient.

## SessionEntityTypesClient
    
    
    type SessionEntityTypesClient struct {
    
    	// The call options for this service.
    	CallOptions *SessionEntityTypesCallOptions
    	// contains filtered or unexported fields
    }

SessionEntityTypesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing SessionEntityTypes.

### func NewSessionEntityTypesClient 
    
    
    func NewSessionEntityTypesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionEntityTypesClient, [error](https://pkg.go.dev/builtin#error))

NewSessionEntityTypesClient creates a new session entity types client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing SessionEntityTypes.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSessionEntityTypesRESTClient 
    
    
    func NewSessionEntityTypesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionEntityTypesClient, [error](https://pkg.go.dev/builtin#error))

NewSessionEntityTypesRESTClient creates a new session entity types rest client.

Service for managing SessionEntityTypes.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSessionEntityTypesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SessionEntityTypesClient_NewSessionEntityTypesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SessionEntityTypesClient) CancelOperation 
    
    
    func (c *SessionEntityTypesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SessionEntityTypesClient) Close 
    
    
    func (c *SessionEntityTypesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SessionEntityTypesClient) Connection (deprecated)
    
    
    func (c *SessionEntityTypesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SessionEntityTypesClient) CreateSessionEntityType 
    
    
    func (c *SessionEntityTypesClient) CreateSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

CreateSessionEntityType creates a session entity type.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateSessionEntityTypeRequest.
    	}
    	resp, err := c.CreateSessionEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionEntityTypesClient) DeleteSessionEntityType 
    
    
    func (c *SessionEntityTypesClient) DeleteSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteSessionEntityType deletes the specified session entity type.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteSessionEntityTypeRequest.
    	}
    	err = c.DeleteSessionEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SessionEntityTypesClient) GetLocation 
    
    
    func (c *SessionEntityTypesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionEntityTypesClient) GetOperation 
    
    
    func (c *SessionEntityTypesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionEntityTypesClient) GetSessionEntityType 
    
    
    func (c *SessionEntityTypesClient) GetSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

GetSessionEntityType retrieves the specified session entity type.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetSessionEntityTypeRequest.
    	}
    	resp, err := c.GetSessionEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionEntityTypesClient) ListLocations 
    
    
    func (c *SessionEntityTypesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionEntityTypesClient) ListOperations 
    
    
    func (c *SessionEntityTypesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionEntityTypesClient) ListSessionEntityTypes 
    
    
    func (c *SessionEntityTypesClient) ListSessionEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListSessionEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListSessionEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SessionEntityTypeIterator

ListSessionEntityTypes returns the list of all session entity types in the specified session.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListSessionEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListSessionEntityTypesRequest.
    	}
    	it := c.ListSessionEntityTypes(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListSessionEntityTypesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListSessionEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListSessionEntityTypesRequest.
    	}
    	for resp, err := range c.ListSessionEntityTypes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionEntityTypesClient) UpdateSessionEntityType 
    
    
    func (c *SessionEntityTypesClient) UpdateSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

UpdateSessionEntityType updates the specified session entity type.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateSessionEntityTypeRequest.
    	}
    	resp, err := c.UpdateSessionEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## SessionsCallOptions
    
    
    type SessionsCallOptions struct {
    	DetectIntent                []gax.CallOption
    	ServerStreamingDetectIntent []gax.CallOption
    	StreamingDetectIntent       []gax.CallOption
    	MatchIntent                 []gax.CallOption
    	FulfillIntent               []gax.CallOption
    	SubmitAnswerFeedback        []gax.CallOption
    	GetLocation                 []gax.CallOption
    	ListLocations               []gax.CallOption
    	CancelOperation             []gax.CallOption
    	GetOperation                []gax.CallOption
    	ListOperations              []gax.CallOption
    }

SessionsCallOptions contains the retry settings for each method of SessionsClient.

## SessionsClient
    
    
    type SessionsClient struct {
    
    	// The call options for this service.
    	CallOptions *SessionsCallOptions
    	// contains filtered or unexported fields
    }

SessionsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

A session represents an interaction with a user. You retrieve user input and pass it to the DetectIntent method to determine user intent and respond.

### func NewSessionsClient 
    
    
    func NewSessionsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionsClient, [error](https://pkg.go.dev/builtin#error))

NewSessionsClient creates a new sessions client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

A session represents an interaction with a user. You retrieve user input and pass it to the DetectIntent method to determine user intent and respond.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSessionsRESTClient 
    
    
    func NewSessionsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionsClient, [error](https://pkg.go.dev/builtin#error))

NewSessionsRESTClient creates a new sessions rest client.

A session represents an interaction with a user. You retrieve user input and pass it to the DetectIntent method to determine user intent and respond.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewSessionsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient_NewSessionsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SessionsClient) CancelOperation 
    
    
    func (c *SessionsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SessionsClient) Close 
    
    
    func (c *SessionsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SessionsClient) Connection (deprecated)
    
    
    func (c *SessionsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SessionsClient) DetectIntent 
    
    
    func (c *SessionsClient) DetectIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DetectIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DetectIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DetectIntentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DetectIntentResponse), [error](https://pkg.go.dev/builtin#error))

DetectIntent processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries.

Note: Always use agent versions for production traffic. See Versions and environments (at <https://cloud.google.com/dialogflow/cx/docs/concept/version>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DetectIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DetectIntentRequest.
    	}
    	resp, err := c.DetectIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionsClient) FulfillIntent 
    
    
    func (c *SessionsClient) FulfillIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[FulfillIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_FulfillIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[FulfillIntentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_FulfillIntentResponse), [error](https://pkg.go.dev/builtin#error))

FulfillIntent fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.FulfillIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#FulfillIntentRequest.
    	}
    	resp, err := c.FulfillIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionsClient) GetLocation 
    
    
    func (c *SessionsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionsClient) GetOperation 
    
    
    func (c *SessionsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionsClient) ListLocations 
    
    
    func (c *SessionsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionsClient) ListOperations 
    
    
    func (c *SessionsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionsClient) MatchIntent 
    
    
    func (c *SessionsClient) MatchIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[MatchIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_MatchIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[MatchIntentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_MatchIntentResponse), [error](https://pkg.go.dev/builtin#error))

MatchIntent returns preliminary intent match results, doesn’t change the session status.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.MatchIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#MatchIntentRequest.
    	}
    	resp, err := c.MatchIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionsClient) ServerStreamingDetectIntent 
    
    
    func (c *SessionsClient) ServerStreamingDetectIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DetectIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DetectIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Sessions_ServerStreamingDetectIntentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Sessions_ServerStreamingDetectIntentClient), [error](https://pkg.go.dev/builtin#error))

ServerStreamingDetectIntent processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send partial responses (at <https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response>) earlier in a single request.

### func (*SessionsClient) StreamingDetectIntent 
    
    
    func (c *SessionsClient) StreamingDetectIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Sessions_StreamingDetectIntentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Sessions_StreamingDetectIntentClient), [error](https://pkg.go.dev/builtin#error))

StreamingDetectIntent processes a natural language query in audio format in a streaming fashion and returns structured, actionable data as a result. This method is only available via the gRPC API (not REST).

Note: Always use agent versions for production traffic. See Versions and environments (at <https://cloud.google.com/dialogflow/cx/docs/concept/version>).

This method is not supported for the REST transport.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"io"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    	stream, err := c.StreamingDetectIntent(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	go func() {
    		reqs := []*cxpb.StreamingDetectIntentRequest{
    			// TODO: Create requests.
    		}
    		for _, req := range reqs {
    			if err := stream.Send(req); err != nil {
    				// TODO: Handle error.
    			}
    		}
    		stream.CloseSend()
    	}()
    	for {
    		resp, err := stream.Recv()
    		if err == io.EOF {
    			break
    		}
    		if err != nil {
    			// TODO: handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionsClient) SubmitAnswerFeedback 
    
    
    func (c *SessionsClient) SubmitAnswerFeedback(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[SubmitAnswerFeedbackRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_SubmitAnswerFeedbackRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[AnswerFeedback](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_AnswerFeedback), [error](https://pkg.go.dev/builtin#error))

SubmitAnswerFeedback updates the feedback received from the user for a single turn of the bot response.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.SubmitAnswerFeedbackRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#SubmitAnswerFeedbackRequest.
    	}
    	resp, err := c.SubmitAnswerFeedback(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## TestCaseIterator
    
    
    type TestCaseIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.TestCase, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TestCaseIterator manages a stream of *cxpb.TestCase.

### func (*TestCaseIterator) All 
    
    
    func (it *TestCaseIterator) All() iter.Seq2[*cxpb.TestCase, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TestCaseIterator) Next 
    
    
    func (it *TestCaseIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TestCase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TestCase), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TestCaseIterator) PageInfo 
    
    
    func (it *TestCaseIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TestCaseResultIterator
    
    
    type TestCaseResultIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.TestCaseResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TestCaseResultIterator manages a stream of *cxpb.TestCaseResult.

### func (*TestCaseResultIterator) All 
    
    
    func (it *TestCaseResultIterator) All() iter.Seq2[*cxpb.TestCaseResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TestCaseResultIterator) Next 
    
    
    func (it *TestCaseResultIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TestCaseResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TestCaseResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TestCaseResultIterator) PageInfo 
    
    
    func (it *TestCaseResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TestCasesCallOptions
    
    
    type TestCasesCallOptions struct {
    	ListTestCases        []gax.CallOption
    	BatchDeleteTestCases []gax.CallOption
    	GetTestCase          []gax.CallOption
    	CreateTestCase       []gax.CallOption
    	UpdateTestCase       []gax.CallOption
    	RunTestCase          []gax.CallOption
    	BatchRunTestCases    []gax.CallOption
    	CalculateCoverage    []gax.CallOption
    	ImportTestCases      []gax.CallOption
    	ExportTestCases      []gax.CallOption
    	ListTestCaseResults  []gax.CallOption
    	GetTestCaseResult    []gax.CallOption
    	GetLocation          []gax.CallOption
    	ListLocations        []gax.CallOption
    	CancelOperation      []gax.CallOption
    	GetOperation         []gax.CallOption
    	ListOperations       []gax.CallOption
    }

TestCasesCallOptions contains the retry settings for each method of TestCasesClient.

## TestCasesClient
    
    
    type TestCasesClient struct {
    
    	// The call options for this service.
    	CallOptions *TestCasesCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

TestCasesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing [Test Cases][google.cloud.dialogflow.cx.v3.TestCase] and [Test Case Results][google.cloud.dialogflow.cx.v3.TestCaseResult].

### func NewTestCasesClient 
    
    
    func NewTestCasesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TestCasesClient, [error](https://pkg.go.dev/builtin#error))

NewTestCasesClient creates a new test cases client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing [Test Cases][google.cloud.dialogflow.cx.v3.TestCase] and [Test Case Results][google.cloud.dialogflow.cx.v3.TestCaseResult].

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTestCasesRESTClient 
    
    
    func NewTestCasesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TestCasesClient, [error](https://pkg.go.dev/builtin#error))

NewTestCasesRESTClient creates a new test cases rest client.

Service for managing [Test Cases][google.cloud.dialogflow.cx.v3.TestCase] and [Test Case Results][google.cloud.dialogflow.cx.v3.TestCaseResult].

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewTestCasesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_TestCasesClient_NewTestCasesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TestCasesClient) BatchDeleteTestCases 
    
    
    func (c *TestCasesClient) BatchDeleteTestCases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[BatchDeleteTestCasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_BatchDeleteTestCasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

BatchDeleteTestCases batch deletes test cases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.BatchDeleteTestCasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#BatchDeleteTestCasesRequest.
    	}
    	err = c.BatchDeleteTestCases(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TestCasesClient) BatchRunTestCases 
    
    
    func (c *TestCasesClient) BatchRunTestCases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[BatchRunTestCasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_BatchRunTestCasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchRunTestCasesOperation, [error](https://pkg.go.dev/builtin#error))

BatchRunTestCases kicks off a batch run of test cases.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    BatchRunTestCasesMetadata
    
    response:
    BatchRunTestCasesResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.BatchRunTestCasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#BatchRunTestCasesRequest.
    	}
    	op, err := c.BatchRunTestCases(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) BatchRunTestCasesOperation 
    
    
    func (c *TestCasesClient) BatchRunTestCasesOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchRunTestCasesOperation

BatchRunTestCasesOperation returns a new BatchRunTestCasesOperation from a given name. The name must be that of a previously created BatchRunTestCasesOperation, possibly from a different process.

### func (*TestCasesClient) CalculateCoverage 
    
    
    func (c *TestCasesClient) CalculateCoverage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CalculateCoverageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CalculateCoverageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CalculateCoverageResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CalculateCoverageResponse), [error](https://pkg.go.dev/builtin#error))

CalculateCoverage calculates the test coverage for an agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CalculateCoverageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CalculateCoverageRequest.
    	}
    	resp, err := c.CalculateCoverage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) CancelOperation 
    
    
    func (c *TestCasesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TestCasesClient) Close 
    
    
    func (c *TestCasesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TestCasesClient) Connection (deprecated)
    
    
    func (c *TestCasesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TestCasesClient) CreateTestCase 
    
    
    func (c *TestCasesClient) CreateTestCase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateTestCaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateTestCaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TestCase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TestCase), [error](https://pkg.go.dev/builtin#error))

CreateTestCase creates a test case for the given agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateTestCaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateTestCaseRequest.
    	}
    	resp, err := c.CreateTestCase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) ExportTestCases 
    
    
    func (c *TestCasesClient) ExportTestCases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ExportTestCasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ExportTestCasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportTestCasesOperation, [error](https://pkg.go.dev/builtin#error))

ExportTestCases exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    ExportTestCasesMetadata
    
    response:
    ExportTestCasesResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ExportTestCasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ExportTestCasesRequest.
    	}
    	op, err := c.ExportTestCases(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) ExportTestCasesOperation 
    
    
    func (c *TestCasesClient) ExportTestCasesOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportTestCasesOperation

ExportTestCasesOperation returns a new ExportTestCasesOperation from a given name. The name must be that of a previously created ExportTestCasesOperation, possibly from a different process.

### func (*TestCasesClient) GetLocation 
    
    
    func (c *TestCasesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) GetOperation 
    
    
    func (c *TestCasesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) GetTestCase 
    
    
    func (c *TestCasesClient) GetTestCase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetTestCaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetTestCaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TestCase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TestCase), [error](https://pkg.go.dev/builtin#error))

GetTestCase gets a test case.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetTestCaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetTestCaseRequest.
    	}
    	resp, err := c.GetTestCase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) GetTestCaseResult 
    
    
    func (c *TestCasesClient) GetTestCaseResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetTestCaseResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetTestCaseResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TestCaseResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TestCaseResult), [error](https://pkg.go.dev/builtin#error))

GetTestCaseResult gets a test case result.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetTestCaseResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetTestCaseResultRequest.
    	}
    	resp, err := c.GetTestCaseResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) ImportTestCases 
    
    
    func (c *TestCasesClient) ImportTestCases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ImportTestCasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ImportTestCasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportTestCasesOperation, [error](https://pkg.go.dev/builtin#error))

ImportTestCases imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won’t overwrite any existing ones. The provided ID in the imported test case is neglected.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    ImportTestCasesMetadata
    
    response:
    ImportTestCasesResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ImportTestCasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ImportTestCasesRequest.
    	}
    	op, err := c.ImportTestCases(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) ImportTestCasesOperation 
    
    
    func (c *TestCasesClient) ImportTestCasesOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportTestCasesOperation

ImportTestCasesOperation returns a new ImportTestCasesOperation from a given name. The name must be that of a previously created ImportTestCasesOperation, possibly from a different process.

### func (*TestCasesClient) ListLocations 
    
    
    func (c *TestCasesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TestCasesClient) ListOperations 
    
    
    func (c *TestCasesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TestCasesClient) ListTestCaseResults 
    
    
    func (c *TestCasesClient) ListTestCaseResults(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListTestCaseResultsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListTestCaseResultsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TestCaseResultIterator

ListTestCaseResults fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListTestCaseResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListTestCaseResultsRequest.
    	}
    	it := c.ListTestCaseResults(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListTestCaseResultsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListTestCaseResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListTestCaseResultsRequest.
    	}
    	for resp, err := range c.ListTestCaseResults(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TestCasesClient) ListTestCases 
    
    
    func (c *TestCasesClient) ListTestCases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListTestCasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListTestCasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TestCaseIterator

ListTestCases fetches a list of test cases for a given agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListTestCasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListTestCasesRequest.
    	}
    	it := c.ListTestCases(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListTestCasesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListTestCasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListTestCasesRequest.
    	}
    	for resp, err := range c.ListTestCases(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TestCasesClient) RunTestCase 
    
    
    func (c *TestCasesClient) RunTestCase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RunTestCaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RunTestCaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RunTestCaseOperation, [error](https://pkg.go.dev/builtin#error))

RunTestCase kicks off a test case run.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    RunTestCaseMetadata
    
    response:
    RunTestCaseResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.RunTestCaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#RunTestCaseRequest.
    	}
    	op, err := c.RunTestCase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TestCasesClient) RunTestCaseOperation 
    
    
    func (c *TestCasesClient) RunTestCaseOperation(name [string](https://pkg.go.dev/builtin#string)) *RunTestCaseOperation

RunTestCaseOperation returns a new RunTestCaseOperation from a given name. The name must be that of a previously created RunTestCaseOperation, possibly from a different process.

### func (*TestCasesClient) UpdateTestCase 
    
    
    func (c *TestCasesClient) UpdateTestCase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateTestCaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateTestCaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TestCase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TestCase), [error](https://pkg.go.dev/builtin#error))

UpdateTestCase updates the specified test case.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTestCasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateTestCaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateTestCaseRequest.
    	}
    	resp, err := c.UpdateTestCase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ToolIterator
    
    
    type ToolIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Tool, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ToolIterator manages a stream of *cxpb.Tool.

### func (*ToolIterator) All 
    
    
    func (it *ToolIterator) All() iter.Seq2[*cxpb.Tool, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ToolIterator) Next 
    
    
    func (it *ToolIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Tool), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ToolIterator) PageInfo 
    
    
    func (it *ToolIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ToolVersionIterator
    
    
    type ToolVersionIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.ToolVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ToolVersionIterator manages a stream of *cxpb.ToolVersion.

### func (*ToolVersionIterator) All 
    
    
    func (it *ToolVersionIterator) All() iter.Seq2[*cxpb.ToolVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ToolVersionIterator) Next 
    
    
    func (it *ToolVersionIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ToolVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ToolVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ToolVersionIterator) PageInfo 
    
    
    func (it *ToolVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ToolsCallOptions
    
    
    type ToolsCallOptions struct {
    	CreateTool         []gax.CallOption
    	ListTools          []gax.CallOption
    	GetTool            []gax.CallOption
    	UpdateTool         []gax.CallOption
    	DeleteTool         []gax.CallOption
    	ListToolVersions   []gax.CallOption
    	CreateToolVersion  []gax.CallOption
    	GetToolVersion     []gax.CallOption
    	DeleteToolVersion  []gax.CallOption
    	RestoreToolVersion []gax.CallOption
    	GetLocation        []gax.CallOption
    	ListLocations      []gax.CallOption
    	CancelOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

ToolsCallOptions contains the retry settings for each method of ToolsClient.

## ToolsClient
    
    
    type ToolsClient struct {
    
    	// The call options for this service.
    	CallOptions *ToolsCallOptions
    	// contains filtered or unexported fields
    }

ToolsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Tools.

### func NewToolsClient 
    
    
    func NewToolsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ToolsClient, [error](https://pkg.go.dev/builtin#error))

NewToolsClient creates a new tools client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Tools.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewToolsRESTClient 
    
    
    func NewToolsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ToolsClient, [error](https://pkg.go.dev/builtin#error))

NewToolsRESTClient creates a new tools rest client.

Service for managing Tools.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewToolsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_ToolsClient_NewToolsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ToolsClient) CancelOperation 
    
    
    func (c *ToolsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ToolsClient) Close 
    
    
    func (c *ToolsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ToolsClient) Connection (deprecated)
    
    
    func (c *ToolsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ToolsClient) CreateTool 
    
    
    func (c *ToolsClient) CreateTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Tool), [error](https://pkg.go.dev/builtin#error))

CreateTool creates a Tool in the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateToolRequest.
    	}
    	resp, err := c.CreateTool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) CreateToolVersion 
    
    
    func (c *ToolsClient) CreateToolVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateToolVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateToolVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ToolVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ToolVersion), [error](https://pkg.go.dev/builtin#error))

CreateToolVersion creates a version for the specified Tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateToolVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateToolVersionRequest.
    	}
    	resp, err := c.CreateToolVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) DeleteTool 
    
    
    func (c *ToolsClient) DeleteTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteTool deletes a specified Tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteToolRequest.
    	}
    	err = c.DeleteTool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ToolsClient) DeleteToolVersion 
    
    
    func (c *ToolsClient) DeleteToolVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteToolVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteToolVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteToolVersion deletes the specified version of the Tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteToolVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteToolVersionRequest.
    	}
    	err = c.DeleteToolVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ToolsClient) GetLocation 
    
    
    func (c *ToolsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) GetOperation 
    
    
    func (c *ToolsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) GetTool 
    
    
    func (c *ToolsClient) GetTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Tool), [error](https://pkg.go.dev/builtin#error))

GetTool retrieves the specified Tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetToolRequest.
    	}
    	resp, err := c.GetTool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) GetToolVersion 
    
    
    func (c *ToolsClient) GetToolVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetToolVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetToolVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ToolVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ToolVersion), [error](https://pkg.go.dev/builtin#error))

GetToolVersion retrieves the specified version of the Tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetToolVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetToolVersionRequest.
    	}
    	resp, err := c.GetToolVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) ListLocations 
    
    
    func (c *ToolsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ToolsClient) ListOperations 
    
    
    func (c *ToolsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ToolsClient) ListToolVersions 
    
    
    func (c *ToolsClient) ListToolVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListToolVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListToolVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ToolVersionIterator

ListToolVersions list versions of the specified Tool.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListToolVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListToolVersionsRequest.
    	}
    	it := c.ListToolVersions(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListToolVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListToolVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListToolVersionsRequest.
    	}
    	for resp, err := range c.ListToolVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ToolsClient) ListTools 
    
    
    func (c *ToolsClient) ListTools(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListToolsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListToolsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ToolIterator

ListTools returns a list of Tools in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListToolsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListToolsRequest.
    	}
    	it := c.ListTools(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListToolsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListToolsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListToolsRequest.
    	}
    	for resp, err := range c.ListTools(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ToolsClient) RestoreToolVersion 
    
    
    func (c *ToolsClient) RestoreToolVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RestoreToolVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RestoreToolVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[RestoreToolVersionResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_RestoreToolVersionResponse), [error](https://pkg.go.dev/builtin#error))

RestoreToolVersion retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.RestoreToolVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#RestoreToolVersionRequest.
    	}
    	resp, err := c.RestoreToolVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) UpdateTool 
    
    
    func (c *ToolsClient) UpdateTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Tool), [error](https://pkg.go.dev/builtin#error))

UpdateTool update the specified Tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateToolRequest.
    	}
    	resp, err := c.UpdateTool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## TrainFlowOperation
    
    
    type TrainFlowOperation struct {
    	// contains filtered or unexported fields
    }

TrainFlowOperation manages a long-running operation from TrainFlow.

### func (*TrainFlowOperation) Done 
    
    
    func (op *TrainFlowOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*TrainFlowOperation) Metadata 
    
    
    func (op *TrainFlowOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*TrainFlowOperation) Name 
    
    
    func (op *TrainFlowOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*TrainFlowOperation) Poll 
    
    
    func (op *TrainFlowOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*TrainFlowOperation) Wait 
    
    
    func (op *TrainFlowOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## TransitionRouteGroupIterator
    
    
    type TransitionRouteGroupIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.TransitionRouteGroup, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TransitionRouteGroupIterator manages a stream of *cxpb.TransitionRouteGroup.

### func (*TransitionRouteGroupIterator) All 
    
    
    func (it *TransitionRouteGroupIterator) All() iter.Seq2[*cxpb.TransitionRouteGroup, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TransitionRouteGroupIterator) Next 
    
    
    func (it *TransitionRouteGroupIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TransitionRouteGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TransitionRouteGroup), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TransitionRouteGroupIterator) PageInfo 
    
    
    func (it *TransitionRouteGroupIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TransitionRouteGroupsCallOptions
    
    
    type TransitionRouteGroupsCallOptions struct {
    	ListTransitionRouteGroups  []gax.CallOption
    	GetTransitionRouteGroup    []gax.CallOption
    	CreateTransitionRouteGroup []gax.CallOption
    	UpdateTransitionRouteGroup []gax.CallOption
    	DeleteTransitionRouteGroup []gax.CallOption
    	GetLocation                []gax.CallOption
    	ListLocations              []gax.CallOption
    	CancelOperation            []gax.CallOption
    	GetOperation               []gax.CallOption
    	ListOperations             []gax.CallOption
    }

TransitionRouteGroupsCallOptions contains the retry settings for each method of TransitionRouteGroupsClient.

## TransitionRouteGroupsClient
    
    
    type TransitionRouteGroupsClient struct {
    
    	// The call options for this service.
    	CallOptions *TransitionRouteGroupsCallOptions
    	// contains filtered or unexported fields
    }

TransitionRouteGroupsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing TransitionRouteGroups.

### func NewTransitionRouteGroupsClient 
    
    
    func NewTransitionRouteGroupsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TransitionRouteGroupsClient, [error](https://pkg.go.dev/builtin#error))

NewTransitionRouteGroupsClient creates a new transition route groups client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing TransitionRouteGroups.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTransitionRouteGroupsRESTClient 
    
    
    func NewTransitionRouteGroupsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TransitionRouteGroupsClient, [error](https://pkg.go.dev/builtin#error))

NewTransitionRouteGroupsRESTClient creates a new transition route groups rest client.

Service for managing TransitionRouteGroups.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewTransitionRouteGroupsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_TransitionRouteGroupsClient_NewTransitionRouteGroupsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TransitionRouteGroupsClient) CancelOperation 
    
    
    func (c *TransitionRouteGroupsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TransitionRouteGroupsClient) Close 
    
    
    func (c *TransitionRouteGroupsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TransitionRouteGroupsClient) Connection (deprecated)
    
    
    func (c *TransitionRouteGroupsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TransitionRouteGroupsClient) CreateTransitionRouteGroup 
    
    
    func (c *TransitionRouteGroupsClient) CreateTransitionRouteGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateTransitionRouteGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateTransitionRouteGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TransitionRouteGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TransitionRouteGroup), [error](https://pkg.go.dev/builtin#error))

CreateTransitionRouteGroup creates an TransitionRouteGroup in the specified flow.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateTransitionRouteGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateTransitionRouteGroupRequest.
    	}
    	resp, err := c.CreateTransitionRouteGroup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TransitionRouteGroupsClient) DeleteTransitionRouteGroup 
    
    
    func (c *TransitionRouteGroupsClient) DeleteTransitionRouteGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteTransitionRouteGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteTransitionRouteGroup deletes the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteTransitionRouteGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteTransitionRouteGroupRequest.
    	}
    	err = c.DeleteTransitionRouteGroup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TransitionRouteGroupsClient) GetLocation 
    
    
    func (c *TransitionRouteGroupsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TransitionRouteGroupsClient) GetOperation 
    
    
    func (c *TransitionRouteGroupsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TransitionRouteGroupsClient) GetTransitionRouteGroup 
    
    
    func (c *TransitionRouteGroupsClient) GetTransitionRouteGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetTransitionRouteGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetTransitionRouteGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TransitionRouteGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TransitionRouteGroup), [error](https://pkg.go.dev/builtin#error))

GetTransitionRouteGroup retrieves the specified TransitionRouteGroup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetTransitionRouteGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetTransitionRouteGroupRequest.
    	}
    	resp, err := c.GetTransitionRouteGroup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TransitionRouteGroupsClient) ListLocations 
    
    
    func (c *TransitionRouteGroupsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TransitionRouteGroupsClient) ListOperations 
    
    
    func (c *TransitionRouteGroupsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TransitionRouteGroupsClient) ListTransitionRouteGroups 
    
    
    func (c *TransitionRouteGroupsClient) ListTransitionRouteGroups(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListTransitionRouteGroupsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListTransitionRouteGroupsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TransitionRouteGroupIterator

ListTransitionRouteGroups returns the list of all transition route groups in the specified flow.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListTransitionRouteGroupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListTransitionRouteGroupsRequest.
    	}
    	it := c.ListTransitionRouteGroups(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListTransitionRouteGroupsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListTransitionRouteGroupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListTransitionRouteGroupsRequest.
    	}
    	for resp, err := range c.ListTransitionRouteGroups(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TransitionRouteGroupsClient) UpdateTransitionRouteGroup 
    
    
    func (c *TransitionRouteGroupsClient) UpdateTransitionRouteGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateTransitionRouteGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[TransitionRouteGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_TransitionRouteGroup), [error](https://pkg.go.dev/builtin#error))

UpdateTransitionRouteGroup updates the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/cx/docs/concept/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewTransitionRouteGroupsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateTransitionRouteGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateTransitionRouteGroupRequest.
    	}
    	resp, err := c.UpdateTransitionRouteGroup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## UpdateEnvironmentOperation
    
    
    type UpdateEnvironmentOperation struct {
    	// contains filtered or unexported fields
    }

UpdateEnvironmentOperation manages a long-running operation from UpdateEnvironment.

### func (*UpdateEnvironmentOperation) Done 
    
    
    func (op *UpdateEnvironmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateEnvironmentOperation) Metadata 
    
    
    func (op *UpdateEnvironmentOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateEnvironmentOperation) Name 
    
    
    func (op *UpdateEnvironmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateEnvironmentOperation) Poll 
    
    
    func (op *UpdateEnvironmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Environment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateEnvironmentOperation) Wait 
    
    
    func (op *UpdateEnvironmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Environment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## VersionIterator
    
    
    type VersionIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Version, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

VersionIterator manages a stream of *cxpb.Version.

### func (*VersionIterator) All 
    
    
    func (it *VersionIterator) All() iter.Seq2[*cxpb.Version, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*VersionIterator) Next 
    
    
    func (it *VersionIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Version), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*VersionIterator) PageInfo 
    
    
    func (it *VersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## VersionsCallOptions
    
    
    type VersionsCallOptions struct {
    	ListVersions    []gax.CallOption
    	GetVersion      []gax.CallOption
    	CreateVersion   []gax.CallOption
    	UpdateVersion   []gax.CallOption
    	DeleteVersion   []gax.CallOption
    	LoadVersion     []gax.CallOption
    	CompareVersions []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

VersionsCallOptions contains the retry settings for each method of VersionsClient.

## VersionsClient
    
    
    type VersionsClient struct {
    
    	// The call options for this service.
    	CallOptions *VersionsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

VersionsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Versions.

### func NewVersionsClient 
    
    
    func NewVersionsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*VersionsClient, [error](https://pkg.go.dev/builtin#error))

NewVersionsClient creates a new versions client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Versions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewVersionsRESTClient 
    
    
    func NewVersionsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*VersionsClient, [error](https://pkg.go.dev/builtin#error))

NewVersionsRESTClient creates a new versions rest client.

Service for managing Versions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewVersionsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_VersionsClient_NewVersionsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*VersionsClient) CancelOperation 
    
    
    func (c *VersionsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*VersionsClient) Close 
    
    
    func (c *VersionsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*VersionsClient) CompareVersions 
    
    
    func (c *VersionsClient) CompareVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CompareVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CompareVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CompareVersionsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CompareVersionsResponse), [error](https://pkg.go.dev/builtin#error))

CompareVersions compares the specified base version with target version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CompareVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CompareVersionsRequest.
    	}
    	resp, err := c.CompareVersions(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) Connection (deprecated)
    
    
    func (c *VersionsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*VersionsClient) CreateVersion 
    
    
    func (c *VersionsClient) CreateVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateVersionOperation, [error](https://pkg.go.dev/builtin#error))

CreateVersion creates a Version in the specified Flow.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    CreateVersionOperationMetadata
    
    response: Version
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateVersionRequest.
    	}
    	op, err := c.CreateVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) CreateVersionOperation 
    
    
    func (c *VersionsClient) CreateVersionOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateVersionOperation

CreateVersionOperation returns a new CreateVersionOperation from a given name. The name must be that of a previously created CreateVersionOperation, possibly from a different process.

### func (*VersionsClient) DeleteVersion 
    
    
    func (c *VersionsClient) DeleteVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteVersion deletes the specified Version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteVersionRequest.
    	}
    	err = c.DeleteVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*VersionsClient) GetLocation 
    
    
    func (c *VersionsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) GetOperation 
    
    
    func (c *VersionsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) GetVersion 
    
    
    func (c *VersionsClient) GetVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Version), [error](https://pkg.go.dev/builtin#error))

GetVersion retrieves the specified Version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetVersionRequest.
    	}
    	resp, err := c.GetVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) ListLocations 
    
    
    func (c *VersionsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*VersionsClient) ListOperations 
    
    
    func (c *VersionsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*VersionsClient) ListVersions 
    
    
    func (c *VersionsClient) ListVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *VersionIterator

ListVersions returns the list of all versions in the specified Flow.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListVersionsRequest.
    	}
    	it := c.ListVersions(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListVersionsRequest.
    	}
    	for resp, err := range c.ListVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*VersionsClient) LoadVersion 
    
    
    func (c *VersionsClient) LoadVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[LoadVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_LoadVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*LoadVersionOperation, [error](https://pkg.go.dev/builtin#error))

LoadVersion loads resources in the specified version to the draft flow.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.LoadVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#LoadVersionRequest.
    	}
    	op, err := c.LoadVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*VersionsClient) LoadVersionOperation 
    
    
    func (c *VersionsClient) LoadVersionOperation(name [string](https://pkg.go.dev/builtin#string)) *LoadVersionOperation

LoadVersionOperation returns a new LoadVersionOperation from a given name. The name must be that of a previously created LoadVersionOperation, possibly from a different process.

### func (*VersionsClient) UpdateVersion 
    
    
    func (c *VersionsClient) UpdateVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Version), [error](https://pkg.go.dev/builtin#error))

UpdateVersion updates the specified Version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateVersionRequest.
    	}
    	resp, err := c.UpdateVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## WebhookIterator
    
    
    type WebhookIterator struct {
    
    	// Response is the raw response for the current page.
    	// It must be cast to the RPC response type.
    	// Calling Next() or InternalFetch() updates this value.
    	Response interface{}
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cxpb.Webhook, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

WebhookIterator manages a stream of *cxpb.Webhook.

### func (*WebhookIterator) All 
    
    
    func (it *WebhookIterator) All() iter.Seq2[*cxpb.Webhook, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*WebhookIterator) Next 
    
    
    func (it *WebhookIterator) Next() (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Webhook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Webhook), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*WebhookIterator) PageInfo 
    
    
    func (it *WebhookIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## WebhooksCallOptions
    
    
    type WebhooksCallOptions struct {
    	ListWebhooks    []gax.CallOption
    	GetWebhook      []gax.CallOption
    	CreateWebhook   []gax.CallOption
    	UpdateWebhook   []gax.CallOption
    	DeleteWebhook   []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

WebhooksCallOptions contains the retry settings for each method of WebhooksClient.

## WebhooksClient
    
    
    type WebhooksClient struct {
    
    	// The call options for this service.
    	CallOptions *WebhooksCallOptions
    	// contains filtered or unexported fields
    }

WebhooksClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Webhooks.

### func NewWebhooksClient 
    
    
    func NewWebhooksClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*WebhooksClient, [error](https://pkg.go.dev/builtin#error))

NewWebhooksClient creates a new webhooks client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Webhooks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewWebhooksRESTClient 
    
    
    func NewWebhooksRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*WebhooksClient, [error](https://pkg.go.dev/builtin#error))

NewWebhooksRESTClient creates a new webhooks rest client.

Service for managing Webhooks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.[NewWebhooksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3.html#cloud_google_com_go_dialogflow_cx_apiv3_WebhooksClient_NewWebhooksRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*WebhooksClient) CancelOperation 
    
    
    func (c *WebhooksClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*WebhooksClient) Close 
    
    
    func (c *WebhooksClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*WebhooksClient) Connection (deprecated)
    
    
    func (c *WebhooksClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*WebhooksClient) CreateWebhook 
    
    
    func (c *WebhooksClient) CreateWebhook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[CreateWebhookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_CreateWebhookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Webhook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Webhook), [error](https://pkg.go.dev/builtin#error))

CreateWebhook creates a webhook in the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.CreateWebhookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#CreateWebhookRequest.
    	}
    	resp, err := c.CreateWebhook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*WebhooksClient) DeleteWebhook 
    
    
    func (c *WebhooksClient) DeleteWebhook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[DeleteWebhookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_DeleteWebhookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteWebhook deletes the specified webhook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.DeleteWebhookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#DeleteWebhookRequest.
    	}
    	err = c.DeleteWebhook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*WebhooksClient) GetLocation 
    
    
    func (c *WebhooksClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*WebhooksClient) GetOperation 
    
    
    func (c *WebhooksClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.GetOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*WebhooksClient) GetWebhook 
    
    
    func (c *WebhooksClient) GetWebhook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[GetWebhookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_GetWebhookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Webhook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Webhook), [error](https://pkg.go.dev/builtin#error))

GetWebhook retrieves the specified webhook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.GetWebhookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#GetWebhookRequest.
    	}
    	resp, err := c.GetWebhook(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*WebhooksClient) ListLocations 
    
    
    func (c *WebhooksClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	"google.golang.org/api/iterator"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*locationpb.ListLocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*WebhooksClient) ListOperations 
    
    
    func (c *WebhooksClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*longrunningpb.[ListOperationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsResponse))
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.ListOperations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*WebhooksClient) ListWebhooks 
    
    
    func (c *WebhooksClient) ListWebhooks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[ListWebhooksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_ListWebhooksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *WebhookIterator

ListWebhooks returns the list of all webhooks in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListWebhooksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListWebhooksRequest.
    	}
    	it := c.ListWebhooks(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cxpb.ListWebhooksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.ListWebhooksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#ListWebhooksRequest.
    	}
    	for resp, err := range c.ListWebhooks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*WebhooksClient) UpdateWebhook 
    
    
    func (c *WebhooksClient) UpdateWebhook(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[UpdateWebhookRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_UpdateWebhookRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cxpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb).[Webhook](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3/cxpb#cloud_google_com_go_dialogflow_cx_apiv3_cxpb_Webhook), [error](https://pkg.go.dev/builtin#error))

UpdateWebhook updates the specified webhook.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cx "cloud.google.com/go/dialogflow/cx/apiv3"
    	cxpb "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cx.NewWebhooksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cxpb.UpdateWebhookRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/cx/apiv3/cxpb#UpdateWebhookRequest.
    	}
    	resp, err := c.UpdateWebhook(ctx, req)
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
