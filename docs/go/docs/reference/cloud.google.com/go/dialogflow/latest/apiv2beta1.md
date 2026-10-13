---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/
title: Dialogflow API v2beta1 - Package cloud.google.com/go/dialogflow/apiv2beta1 (v1.87.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:57.868061+00:00
---

# Dialogflow API v2beta1 - Package cloud.google.com/go/dialogflow/apiv2beta1 (v1.87.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Dialogflow API v2beta1 - Package cloud.google.com/go/dialogflow/apiv2beta1 (v1.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.87.0 (latest)  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.1  1.68.2  1.67.0  1.66.0  1.65.0  1.64.1  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.1  1.57.1  1.56.0  1.55.0  1.54.3  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.2  1.47.0  1.46.0  1.45.0  1.44.3  1.42.0  1.41.0  1.40.1  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.1  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1). 

Package dialogflow is an auto-generated package for the Dialogflow API. 

Builds conversational interfaces (for example, chatbots, and voice-powered apps and devices).
    
    
    NOTE: This package is in beta. It is not stable, and may be subject to changes.

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/dialogflow/apiv2beta1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := dialogflow.NewAgentsClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &dialogflowpb.DeleteAgentRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteAgentRequest.
    }
    err = c.DeleteAgent(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }

## Use of Context

The ctx passed to NewAgentsClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Agent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AgentIterator manages a stream of *dialogflowpb.Agent.

### func (*AgentIterator) All 
    
    
    func (it *AgentIterator) All() iter.Seq2[*dialogflowpb.Agent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AgentIterator) Next 
    
    
    func (it *AgentIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Agent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AgentIterator) PageInfo 
    
    
    func (it *AgentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AgentsCallOptions
    
    
    type AgentsCallOptions struct {
    	GetAgent            []gax.CallOption
    	SetAgent            []gax.CallOption
    	DeleteAgent         []gax.CallOption
    	SearchAgents        []gax.CallOption
    	TrainAgent          []gax.CallOption
    	ExportAgent         []gax.CallOption
    	ImportAgent         []gax.CallOption
    	RestoreAgent        []gax.CallOption
    	GetValidationResult []gax.CallOption
    	GetLocation         []gax.CallOption
    	ListLocations       []gax.CallOption
    	CancelOperation     []gax.CallOption
    	GetOperation        []gax.CallOption
    	ListOperations      []gax.CallOption
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewAgentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_AgentsClient_NewAgentsRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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

### func (*AgentsClient) DeleteAgent 
    
    
    func (c *AgentsClient) DeleteAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAgent deletes the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteAgentRequest.
    	}
    	err = c.DeleteAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AgentsClient) ExportAgent 
    
    
    func (c *AgentsClient) ExportAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ExportAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ExportAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportAgentOperation, [error](https://pkg.go.dev/builtin#error))

ExportAgent exports the specified agent to a ZIP file.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response:
    ExportAgentResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ExportAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ExportAgentRequest.
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
    
    
    func (c *AgentsClient) GetAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Agent), [error](https://pkg.go.dev/builtin#error))

GetAgent retrieves the specified agent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetAgentRequest.
    	}
    	resp, err := c.GetAgent(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) GetValidationResult 
    
    
    func (c *AgentsClient) GetValidationResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetValidationResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetValidationResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ValidationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ValidationResult), [error](https://pkg.go.dev/builtin#error))

GetValidationResult gets agent validation result. Agent validation is performed during training time and is updated automatically when training is completed.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetValidationResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetValidationResultRequest.
    	}
    	resp, err := c.GetValidationResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) ImportAgent 
    
    
    func (c *AgentsClient) ImportAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ImportAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ImportAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportAgentOperation, [error](https://pkg.go.dev/builtin#error))

ImportAgent imports the specified agent from a ZIP file.

Uploads new intents and entity types without deleting the existing ones. Intents and entity types with the same name are replaced with the new versions from ImportAgentRequest. After the import, the imported draft agent will be trained automatically (unless disabled in agent settings). However, once the import is done, training may not be completed yet. Please call TrainAgent and wait for the operation it returns in order to train explicitly.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

The operation only tracks when importing is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ImportAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ImportAgentRequest.
    	}
    	op, err := c.ImportAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AgentsClient) ImportAgentOperation 
    
    
    func (c *AgentsClient) ImportAgentOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportAgentOperation

ImportAgentOperation returns a new ImportAgentOperation from a given name. The name must be that of a previously created ImportAgentOperation, possibly from a different process.

### func (*AgentsClient) ListLocations 
    
    
    func (c *AgentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewAgentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AgentsClient) RestoreAgent 
    
    
    func (c *AgentsClient) RestoreAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[RestoreAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_RestoreAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestoreAgentOperation, [error](https://pkg.go.dev/builtin#error))

RestoreAgent restores the specified agent from a ZIP file.

Replaces the current agent version with a new one. All the intents and entity types in the older version are deleted. After the restore, the restored draft agent will be trained automatically (unless disabled in agent settings). However, once the restore is done, training may not be completed yet. Please call TrainAgent and wait for the operation it returns in order to train explicitly.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

The operation only tracks when restoring is complete, not when it is done training.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.RestoreAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#RestoreAgentRequest.
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

### func (*AgentsClient) SearchAgents 
    
    
    func (c *AgentsClient) SearchAgents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SearchAgentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SearchAgentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AgentIterator

SearchAgents returns the list of agents. Since there is at most one conversational agent per project, this method is useful primarily for listing all agents across projects the caller has access to. One can achieve that with a wildcard project collection id “-”. Refer to List Sub-Collections (at <https://cloud.google.com/apis/design/design_patterns#list_sub-collections>).

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SearchAgentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SearchAgentsRequest.
    	}
    	it := c.SearchAgents(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.SearchAgentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SearchAgentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SearchAgentsRequest.
    	}
    	for resp, err := range c.SearchAgents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AgentsClient) SetAgent 
    
    
    func (c *AgentsClient) SetAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SetAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SetAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Agent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Agent), [error](https://pkg.go.dev/builtin#error))

SetAgent creates/updates the specified agent.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SetAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SetAgentRequest.
    	}
    	resp, err := c.SetAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AgentsClient) TrainAgent 
    
    
    func (c *AgentsClient) TrainAgent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[TrainAgentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_TrainAgentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*TrainAgentOperation, [error](https://pkg.go.dev/builtin#error))

TrainAgent trains the specified agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAgentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.TrainAgentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#TrainAgentRequest.
    	}
    	op, err := c.TrainAgent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AgentsClient) TrainAgentOperation 
    
    
    func (c *AgentsClient) TrainAgentOperation(name [string](https://pkg.go.dev/builtin#string)) *TrainAgentOperation

TrainAgentOperation returns a new TrainAgentOperation from a given name. The name must be that of a previously created TrainAgentOperation, possibly from a different process.

## AnswerRecordIterator
    
    
    type AnswerRecordIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.AnswerRecord, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AnswerRecordIterator manages a stream of *dialogflowpb.AnswerRecord.

### func (*AnswerRecordIterator) All 
    
    
    func (it *AnswerRecordIterator) All() iter.Seq2[*dialogflowpb.AnswerRecord, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AnswerRecordIterator) Next 
    
    
    func (it *AnswerRecordIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[AnswerRecord](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_AnswerRecord), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AnswerRecordIterator) PageInfo 
    
    
    func (it *AnswerRecordIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AnswerRecordsCallOptions
    
    
    type AnswerRecordsCallOptions struct {
    	GetAnswerRecord    []gax.CallOption
    	ListAnswerRecords  []gax.CallOption
    	UpdateAnswerRecord []gax.CallOption
    	GetLocation        []gax.CallOption
    	ListLocations      []gax.CallOption
    	CancelOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

AnswerRecordsCallOptions contains the retry settings for each method of AnswerRecordsClient.

## AnswerRecordsClient
    
    
    type AnswerRecordsClient struct {
    
    	// The call options for this service.
    	CallOptions *AnswerRecordsCallOptions
    	// contains filtered or unexported fields
    }

AnswerRecordsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing AnswerRecords.

### func NewAnswerRecordsClient 
    
    
    func NewAnswerRecordsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AnswerRecordsClient, [error](https://pkg.go.dev/builtin#error))

NewAnswerRecordsClient creates a new answer records client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing AnswerRecords.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAnswerRecordsRESTClient 
    
    
    func NewAnswerRecordsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AnswerRecordsClient, [error](https://pkg.go.dev/builtin#error))

NewAnswerRecordsRESTClient creates a new answer records rest client.

Service for managing AnswerRecords.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewAnswerRecordsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_AnswerRecordsClient_NewAnswerRecordsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AnswerRecordsClient) CancelOperation 
    
    
    func (c *AnswerRecordsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AnswerRecordsClient) Close 
    
    
    func (c *AnswerRecordsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AnswerRecordsClient) Connection (deprecated)
    
    
    func (c *AnswerRecordsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AnswerRecordsClient) GetAnswerRecord (deprecated)
    
    
    func (c *AnswerRecordsClient) GetAnswerRecord(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetAnswerRecordRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetAnswerRecordRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[AnswerRecord](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_AnswerRecord), [error](https://pkg.go.dev/builtin#error))

GetAnswerRecord deprecated. Retrieves a specific answer record.

Deprecated: GetAnswerRecord may be removed in a future version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetAnswerRecordRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetAnswerRecordRequest.
    	}
    	resp, err := c.GetAnswerRecord(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnswerRecordsClient) GetLocation 
    
    
    func (c *AnswerRecordsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
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
    

### func (*AnswerRecordsClient) GetOperation 
    
    
    func (c *AnswerRecordsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnswerRecordsClient) ListAnswerRecords 
    
    
    func (c *AnswerRecordsClient) ListAnswerRecords(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListAnswerRecordsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListAnswerRecordsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AnswerRecordIterator

ListAnswerRecords returns the list of all answer records in the specified project in reverse chronological order.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListAnswerRecordsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListAnswerRecordsRequest.
    	}
    	it := c.ListAnswerRecords(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListAnswerRecordsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListAnswerRecordsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListAnswerRecordsRequest.
    	}
    	for resp, err := range c.ListAnswerRecords(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AnswerRecordsClient) ListLocations 
    
    
    func (c *AnswerRecordsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
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
    

### func (*AnswerRecordsClient) ListOperations 
    
    
    func (c *AnswerRecordsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AnswerRecordsClient) UpdateAnswerRecord 
    
    
    func (c *AnswerRecordsClient) UpdateAnswerRecord(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateAnswerRecordRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateAnswerRecordRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[AnswerRecord](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_AnswerRecord), [error](https://pkg.go.dev/builtin#error))

UpdateAnswerRecord updates the specified answer record.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewAnswerRecordsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateAnswerRecordRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateAnswerRecordRequest.
    	}
    	resp, err := c.UpdateAnswerRecord(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## BatchCreateEntitiesOperation
    
    
    type BatchCreateEntitiesOperation struct {
    	// contains filtered or unexported fields
    }

BatchCreateEntitiesOperation manages a long-running operation from BatchCreateEntities.

### func (*BatchCreateEntitiesOperation) Done 
    
    
    func (op *BatchCreateEntitiesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchCreateEntitiesOperation) Metadata 
    
    
    func (op *BatchCreateEntitiesOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchCreateEntitiesOperation) Name 
    
    
    func (op *BatchCreateEntitiesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchCreateEntitiesOperation) Poll 
    
    
    func (op *BatchCreateEntitiesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchCreateEntitiesOperation) Wait 
    
    
    func (op *BatchCreateEntitiesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## BatchDeleteEntitiesOperation
    
    
    type BatchDeleteEntitiesOperation struct {
    	// contains filtered or unexported fields
    }

BatchDeleteEntitiesOperation manages a long-running operation from BatchDeleteEntities.

### func (*BatchDeleteEntitiesOperation) Done 
    
    
    func (op *BatchDeleteEntitiesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchDeleteEntitiesOperation) Metadata 
    
    
    func (op *BatchDeleteEntitiesOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchDeleteEntitiesOperation) Name 
    
    
    func (op *BatchDeleteEntitiesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchDeleteEntitiesOperation) Poll 
    
    
    func (op *BatchDeleteEntitiesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchDeleteEntitiesOperation) Wait 
    
    
    func (op *BatchDeleteEntitiesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## BatchDeleteEntityTypesOperation
    
    
    type BatchDeleteEntityTypesOperation struct {
    	// contains filtered or unexported fields
    }

BatchDeleteEntityTypesOperation manages a long-running operation from BatchDeleteEntityTypes.

### func (*BatchDeleteEntityTypesOperation) Done 
    
    
    func (op *BatchDeleteEntityTypesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchDeleteEntityTypesOperation) Metadata 
    
    
    func (op *BatchDeleteEntityTypesOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchDeleteEntityTypesOperation) Name 
    
    
    func (op *BatchDeleteEntityTypesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchDeleteEntityTypesOperation) Poll 
    
    
    func (op *BatchDeleteEntityTypesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchDeleteEntityTypesOperation) Wait 
    
    
    func (op *BatchDeleteEntityTypesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## BatchDeleteIntentsOperation
    
    
    type BatchDeleteIntentsOperation struct {
    	// contains filtered or unexported fields
    }

BatchDeleteIntentsOperation manages a long-running operation from BatchDeleteIntents.

### func (*BatchDeleteIntentsOperation) Done 
    
    
    func (op *BatchDeleteIntentsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchDeleteIntentsOperation) Metadata 
    
    
    func (op *BatchDeleteIntentsOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchDeleteIntentsOperation) Name 
    
    
    func (op *BatchDeleteIntentsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchDeleteIntentsOperation) Poll 
    
    
    func (op *BatchDeleteIntentsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchDeleteIntentsOperation) Wait 
    
    
    func (op *BatchDeleteIntentsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## BatchUpdateEntitiesOperation
    
    
    type BatchUpdateEntitiesOperation struct {
    	// contains filtered or unexported fields
    }

BatchUpdateEntitiesOperation manages a long-running operation from BatchUpdateEntities.

### func (*BatchUpdateEntitiesOperation) Done 
    
    
    func (op *BatchUpdateEntitiesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchUpdateEntitiesOperation) Metadata 
    
    
    func (op *BatchUpdateEntitiesOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchUpdateEntitiesOperation) Name 
    
    
    func (op *BatchUpdateEntitiesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchUpdateEntitiesOperation) Poll 
    
    
    func (op *BatchUpdateEntitiesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchUpdateEntitiesOperation) Wait 
    
    
    func (op *BatchUpdateEntitiesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## BatchUpdateEntityTypesOperation
    
    
    type BatchUpdateEntityTypesOperation struct {
    	// contains filtered or unexported fields
    }

BatchUpdateEntityTypesOperation manages a long-running operation from BatchUpdateEntityTypes.

### func (*BatchUpdateEntityTypesOperation) Done 
    
    
    func (op *BatchUpdateEntityTypesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchUpdateEntityTypesOperation) Metadata 
    
    
    func (op *BatchUpdateEntityTypesOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchUpdateEntityTypesOperation) Name 
    
    
    func (op *BatchUpdateEntityTypesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchUpdateEntityTypesOperation) Poll 
    
    
    func (op *BatchUpdateEntityTypesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateEntityTypesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateEntityTypesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchUpdateEntityTypesOperation) Wait 
    
    
    func (op *BatchUpdateEntityTypesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateEntityTypesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateEntityTypesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## BatchUpdateIntentsOperation
    
    
    type BatchUpdateIntentsOperation struct {
    	// contains filtered or unexported fields
    }

BatchUpdateIntentsOperation manages a long-running operation from BatchUpdateIntents.

### func (*BatchUpdateIntentsOperation) Done 
    
    
    func (op *BatchUpdateIntentsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*BatchUpdateIntentsOperation) Metadata 
    
    
    func (op *BatchUpdateIntentsOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*BatchUpdateIntentsOperation) Name 
    
    
    func (op *BatchUpdateIntentsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*BatchUpdateIntentsOperation) Poll 
    
    
    func (op *BatchUpdateIntentsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateIntentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateIntentsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*BatchUpdateIntentsOperation) Wait 
    
    
    func (op *BatchUpdateIntentsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateIntentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateIntentsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ClearSuggestionFeatureConfigOperation
    
    
    type ClearSuggestionFeatureConfigOperation struct {
    	// contains filtered or unexported fields
    }

ClearSuggestionFeatureConfigOperation manages a long-running operation from ClearSuggestionFeatureConfig.

### func (*ClearSuggestionFeatureConfigOperation) Done 
    
    
    func (op *ClearSuggestionFeatureConfigOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ClearSuggestionFeatureConfigOperation) Metadata 
    
    
    func (op *ClearSuggestionFeatureConfigOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ClearSuggestionFeatureConfigOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ClearSuggestionFeatureConfigOperation) Name 
    
    
    func (op *ClearSuggestionFeatureConfigOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ClearSuggestionFeatureConfigOperation) Poll 
    
    
    func (op *ClearSuggestionFeatureConfigOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ClearSuggestionFeatureConfigOperation) Wait 
    
    
    func (op *ClearSuggestionFeatureConfigOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ContextIterator
    
    
    type ContextIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Context, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ContextIterator manages a stream of *dialogflowpb.Context.

### func (*ContextIterator) All 
    
    
    func (it *ContextIterator) All() iter.Seq2[*dialogflowpb.Context, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ContextIterator) Next 
    
    
    func (it *ContextIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Context](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Context), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ContextIterator) PageInfo 
    
    
    func (it *ContextIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ContextsCallOptions
    
    
    type ContextsCallOptions struct {
    	ListContexts      []gax.CallOption
    	GetContext        []gax.CallOption
    	CreateContext     []gax.CallOption
    	UpdateContext     []gax.CallOption
    	DeleteContext     []gax.CallOption
    	DeleteAllContexts []gax.CallOption
    	GetLocation       []gax.CallOption
    	ListLocations     []gax.CallOption
    	CancelOperation   []gax.CallOption
    	GetOperation      []gax.CallOption
    	ListOperations    []gax.CallOption
    }

ContextsCallOptions contains the retry settings for each method of ContextsClient.

## ContextsClient
    
    
    type ContextsClient struct {
    
    	// The call options for this service.
    	CallOptions *ContextsCallOptions
    	// contains filtered or unexported fields
    }

ContextsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Contexts.

### func NewContextsClient 
    
    
    func NewContextsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ContextsClient, [error](https://pkg.go.dev/builtin#error))

NewContextsClient creates a new contexts client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Contexts.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewContextsRESTClient 
    
    
    func NewContextsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ContextsClient, [error](https://pkg.go.dev/builtin#error))

NewContextsRESTClient creates a new contexts rest client.

Service for managing Contexts.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewContextsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_ContextsClient_NewContextsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ContextsClient) CancelOperation 
    
    
    func (c *ContextsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ContextsClient) Close 
    
    
    func (c *ContextsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ContextsClient) Connection (deprecated)
    
    
    func (c *ContextsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ContextsClient) CreateContext 
    
    
    func (c *ContextsClient) CreateContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateContextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateContextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Context](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Context), [error](https://pkg.go.dev/builtin#error))

CreateContext creates a context.

If the specified context already exists, overrides the context.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateContextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateContextRequest.
    	}
    	resp, err := c.CreateContext(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ContextsClient) DeleteAllContexts 
    
    
    func (c *ContextsClient) DeleteAllContexts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteAllContextsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteAllContextsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAllContexts deletes all active contexts in the specified session.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteAllContextsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteAllContextsRequest.
    	}
    	err = c.DeleteAllContexts(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ContextsClient) DeleteContext 
    
    
    func (c *ContextsClient) DeleteContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteContextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteContextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteContext deletes the specified context.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteContextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteContextRequest.
    	}
    	err = c.DeleteContext(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ContextsClient) GetContext 
    
    
    func (c *ContextsClient) GetContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetContextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetContextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Context](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Context), [error](https://pkg.go.dev/builtin#error))

GetContext retrieves the specified context.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetContextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetContextRequest.
    	}
    	resp, err := c.GetContext(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ContextsClient) GetLocation 
    
    
    func (c *ContextsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
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
    

### func (*ContextsClient) GetOperation 
    
    
    func (c *ContextsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ContextsClient) ListContexts 
    
    
    func (c *ContextsClient) ListContexts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListContextsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListContextsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ContextIterator

ListContexts returns the list of all contexts in the specified session.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListContextsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListContextsRequest.
    	}
    	it := c.ListContexts(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListContextsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListContextsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListContextsRequest.
    	}
    	for resp, err := range c.ListContexts(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ContextsClient) ListLocations 
    
    
    func (c *ContextsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewContextsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
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
    

### func (*ContextsClient) ListOperations 
    
    
    func (c *ContextsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ContextsClient) UpdateContext 
    
    
    func (c *ContextsClient) UpdateContext(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateContextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateContextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Context](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Context), [error](https://pkg.go.dev/builtin#error))

UpdateContext updates the specified context.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewContextsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateContextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateContextRequest.
    	}
    	resp, err := c.UpdateContext(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ConversationIterator
    
    
    type ConversationIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Conversation, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ConversationIterator manages a stream of *dialogflowpb.Conversation.

### func (*ConversationIterator) All 
    
    
    func (it *ConversationIterator) All() iter.Seq2[*dialogflowpb.Conversation, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ConversationIterator) Next 
    
    
    func (it *ConversationIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Conversation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Conversation), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ConversationIterator) PageInfo 
    
    
    func (it *ConversationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ConversationProfileIterator
    
    
    type ConversationProfileIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.ConversationProfile, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ConversationProfileIterator manages a stream of *dialogflowpb.ConversationProfile.

### func (*ConversationProfileIterator) All 
    
    
    func (it *ConversationProfileIterator) All() iter.Seq2[*dialogflowpb.ConversationProfile, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ConversationProfileIterator) Next 
    
    
    func (it *ConversationProfileIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ConversationProfileIterator) PageInfo 
    
    
    func (it *ConversationProfileIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ConversationProfilesCallOptions
    
    
    type ConversationProfilesCallOptions struct {
    	ListConversationProfiles     []gax.CallOption
    	GetConversationProfile       []gax.CallOption
    	CreateConversationProfile    []gax.CallOption
    	UpdateConversationProfile    []gax.CallOption
    	DeleteConversationProfile    []gax.CallOption
    	SetSuggestionFeatureConfig   []gax.CallOption
    	ClearSuggestionFeatureConfig []gax.CallOption
    	GetLocation                  []gax.CallOption
    	ListLocations                []gax.CallOption
    	CancelOperation              []gax.CallOption
    	GetOperation                 []gax.CallOption
    	ListOperations               []gax.CallOption
    }

ConversationProfilesCallOptions contains the retry settings for each method of ConversationProfilesClient.

## ConversationProfilesClient
    
    
    type ConversationProfilesClient struct {
    
    	// The call options for this service.
    	CallOptions *ConversationProfilesCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

ConversationProfilesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing ConversationProfiles.

### func NewConversationProfilesClient 
    
    
    func NewConversationProfilesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ConversationProfilesClient, [error](https://pkg.go.dev/builtin#error))

NewConversationProfilesClient creates a new conversation profiles client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing ConversationProfiles.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewConversationProfilesRESTClient 
    
    
    func NewConversationProfilesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ConversationProfilesClient, [error](https://pkg.go.dev/builtin#error))

NewConversationProfilesRESTClient creates a new conversation profiles rest client.

Service for managing ConversationProfiles.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewConversationProfilesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_ConversationProfilesClient_NewConversationProfilesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ConversationProfilesClient) CancelOperation 
    
    
    func (c *ConversationProfilesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ConversationProfilesClient) ClearSuggestionFeatureConfig 
    
    
    func (c *ConversationProfilesClient) ClearSuggestionFeatureConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ClearSuggestionFeatureConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ClearSuggestionFeatureConfigOperation, [error](https://pkg.go.dev/builtin#error))

ClearSuggestionFeatureConfig clears a suggestion feature from a conversation profile for the given participant role.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    ClearSuggestionFeatureConfigOperationMetadata
    
    response:
    ConversationProfile
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ClearSuggestionFeatureConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ClearSuggestionFeatureConfigRequest.
    	}
    	op, err := c.ClearSuggestionFeatureConfig(ctx, req)
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
    

### func (*ConversationProfilesClient) ClearSuggestionFeatureConfigOperation 
    
    
    func (c *ConversationProfilesClient) ClearSuggestionFeatureConfigOperation(name [string](https://pkg.go.dev/builtin#string)) *ClearSuggestionFeatureConfigOperation

ClearSuggestionFeatureConfigOperation returns a new ClearSuggestionFeatureConfigOperation from a given name. The name must be that of a previously created ClearSuggestionFeatureConfigOperation, possibly from a different process.

### func (*ConversationProfilesClient) Close 
    
    
    func (c *ConversationProfilesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ConversationProfilesClient) Connection (deprecated)
    
    
    func (c *ConversationProfilesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ConversationProfilesClient) CreateConversationProfile 
    
    
    func (c *ConversationProfilesClient) CreateConversationProfile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateConversationProfileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateConversationProfileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

CreateConversationProfile creates a conversation profile in the specified project.

ConversationProfile.CreateTime and ConversationProfile.UpdateTime aren’t populated in the response. You can retrieve them via GetConversationProfile API.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateConversationProfileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateConversationProfileRequest.
    	}
    	resp, err := c.CreateConversationProfile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationProfilesClient) DeleteConversationProfile 
    
    
    func (c *ConversationProfilesClient) DeleteConversationProfile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteConversationProfileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteConversationProfileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteConversationProfile deletes the specified conversation profile.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteConversationProfileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteConversationProfileRequest.
    	}
    	err = c.DeleteConversationProfile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ConversationProfilesClient) GetConversationProfile 
    
    
    func (c *ConversationProfilesClient) GetConversationProfile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetConversationProfileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetConversationProfileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

GetConversationProfile retrieves the specified conversation profile.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetConversationProfileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetConversationProfileRequest.
    	}
    	resp, err := c.GetConversationProfile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationProfilesClient) GetLocation 
    
    
    func (c *ConversationProfilesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
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
    

### func (*ConversationProfilesClient) GetOperation 
    
    
    func (c *ConversationProfilesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationProfilesClient) ListConversationProfiles 
    
    
    func (c *ConversationProfilesClient) ListConversationProfiles(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListConversationProfilesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListConversationProfilesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ConversationProfileIterator

ListConversationProfiles returns the list of all conversation profiles in the specified project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListConversationProfilesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListConversationProfilesRequest.
    	}
    	it := c.ListConversationProfiles(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListConversationProfilesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListConversationProfilesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListConversationProfilesRequest.
    	}
    	for resp, err := range c.ListConversationProfiles(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ConversationProfilesClient) ListLocations 
    
    
    func (c *ConversationProfilesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
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
    

### func (*ConversationProfilesClient) ListOperations 
    
    
    func (c *ConversationProfilesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ConversationProfilesClient) SetSuggestionFeatureConfig 
    
    
    func (c *ConversationProfilesClient) SetSuggestionFeatureConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SetSuggestionFeatureConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*SetSuggestionFeatureConfigOperation, [error](https://pkg.go.dev/builtin#error))

SetSuggestionFeatureConfig adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    SetSuggestionFeatureConfigOperationMetadata
    
    response:
    ConversationProfile
    

If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SetSuggestionFeatureConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SetSuggestionFeatureConfigRequest.
    	}
    	op, err := c.SetSuggestionFeatureConfig(ctx, req)
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
    

### func (*ConversationProfilesClient) SetSuggestionFeatureConfigOperation 
    
    
    func (c *ConversationProfilesClient) SetSuggestionFeatureConfigOperation(name [string](https://pkg.go.dev/builtin#string)) *SetSuggestionFeatureConfigOperation

SetSuggestionFeatureConfigOperation returns a new SetSuggestionFeatureConfigOperation from a given name. The name must be that of a previously created SetSuggestionFeatureConfigOperation, possibly from a different process.

### func (*ConversationProfilesClient) UpdateConversationProfile 
    
    
    func (c *ConversationProfilesClient) UpdateConversationProfile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateConversationProfileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateConversationProfileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

UpdateConversationProfile updates the specified conversation profile.

ConversationProfile.CreateTime and ConversationProfile.UpdateTime aren’t populated in the response. You can retrieve them via GetConversationProfile API.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationProfilesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateConversationProfileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateConversationProfileRequest.
    	}
    	resp, err := c.UpdateConversationProfile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ConversationsCallOptions
    
    
    type ConversationsCallOptions struct {
    	CreateConversation          []gax.CallOption
    	ListConversations           []gax.CallOption
    	GetConversation             []gax.CallOption
    	CompleteConversation        []gax.CallOption
    	IngestContextReferences     []gax.CallOption
    	BatchCreateMessages         []gax.CallOption
    	ListMessages                []gax.CallOption
    	SuggestConversationSummary  []gax.CallOption
    	GenerateStatelessSummary    []gax.CallOption
    	GenerateStatelessSuggestion []gax.CallOption
    	SearchKnowledge             []gax.CallOption
    	GenerateSuggestions         []gax.CallOption
    	GetLocation                 []gax.CallOption
    	ListLocations               []gax.CallOption
    	CancelOperation             []gax.CallOption
    	GetOperation                []gax.CallOption
    	ListOperations              []gax.CallOption
    }

ConversationsCallOptions contains the retry settings for each method of ConversationsClient.

## ConversationsClient
    
    
    type ConversationsClient struct {
    
    	// The call options for this service.
    	CallOptions *ConversationsCallOptions
    	// contains filtered or unexported fields
    }

ConversationsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Conversations.

### func NewConversationsClient 
    
    
    func NewConversationsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ConversationsClient, [error](https://pkg.go.dev/builtin#error))

NewConversationsClient creates a new conversations client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Conversations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewConversationsRESTClient 
    
    
    func NewConversationsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ConversationsClient, [error](https://pkg.go.dev/builtin#error))

NewConversationsRESTClient creates a new conversations rest client.

Service for managing Conversations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewConversationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_ConversationsClient_NewConversationsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ConversationsClient) BatchCreateMessages 
    
    
    func (c *ConversationsClient) BatchCreateMessages(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchCreateMessagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchCreateMessagesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchCreateMessagesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchCreateMessagesResponse), [error](https://pkg.go.dev/builtin#error))

BatchCreateMessages batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchCreateMessagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchCreateMessagesRequest.
    	}
    	resp, err := c.BatchCreateMessages(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) CancelOperation 
    
    
    func (c *ConversationsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ConversationsClient) Close 
    
    
    func (c *ConversationsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ConversationsClient) CompleteConversation 
    
    
    func (c *ConversationsClient) CompleteConversation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CompleteConversationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CompleteConversationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Conversation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Conversation), [error](https://pkg.go.dev/builtin#error))

CompleteConversation completes the specified conversation. Finished conversations are purged from the database after 30 days.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CompleteConversationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CompleteConversationRequest.
    	}
    	resp, err := c.CompleteConversation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) Connection (deprecated)
    
    
    func (c *ConversationsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ConversationsClient) CreateConversation 
    
    
    func (c *ConversationsClient) CreateConversation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateConversationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateConversationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Conversation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Conversation), [error](https://pkg.go.dev/builtin#error))

CreateConversation creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there’s no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from Automated Agent Stage, otherwise, it will start from Assist Stage. And during Automated Agent Stage, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateConversationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateConversationRequest.
    	}
    	resp, err := c.CreateConversation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) GenerateStatelessSuggestion 
    
    
    func (c *ConversationsClient) GenerateStatelessSuggestion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GenerateStatelessSuggestionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GenerateStatelessSuggestionResponse), [error](https://pkg.go.dev/builtin#error))

GenerateStatelessSuggestion generates and returns a suggestion for a conversation that does not have a resource created for it.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GenerateStatelessSuggestionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GenerateStatelessSuggestionRequest.
    	}
    	resp, err := c.GenerateStatelessSuggestion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) GenerateStatelessSummary 
    
    
    func (c *ConversationsClient) GenerateStatelessSummary(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GenerateStatelessSummaryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GenerateStatelessSummaryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GenerateStatelessSummaryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GenerateStatelessSummaryResponse), [error](https://pkg.go.dev/builtin#error))

GenerateStatelessSummary generates and returns a summary for a conversation that does not have a resource created for it.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GenerateStatelessSummaryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GenerateStatelessSummaryRequest.
    	}
    	resp, err := c.GenerateStatelessSummary(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) GenerateSuggestions 
    
    
    func (c *ConversationsClient) GenerateSuggestions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GenerateSuggestionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GenerateSuggestionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GenerateSuggestionsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GenerateSuggestionsResponse), [error](https://pkg.go.dev/builtin#error))

GenerateSuggestions generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GenerateSuggestionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GenerateSuggestionsRequest.
    	}
    	resp, err := c.GenerateSuggestions(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) GetConversation 
    
    
    func (c *ConversationsClient) GetConversation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetConversationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetConversationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Conversation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Conversation), [error](https://pkg.go.dev/builtin#error))

GetConversation retrieves the specific conversation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetConversationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetConversationRequest.
    	}
    	resp, err := c.GetConversation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) GetLocation 
    
    
    func (c *ConversationsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
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
    

### func (*ConversationsClient) GetOperation 
    
    
    func (c *ConversationsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) IngestContextReferences 
    
    
    func (c *ConversationsClient) IngestContextReferences(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[IngestContextReferencesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_IngestContextReferencesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[IngestContextReferencesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_IngestContextReferencesResponse), [error](https://pkg.go.dev/builtin#error))

IngestContextReferences data ingestion API. Ingests context references for an existing conversation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.IngestContextReferencesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#IngestContextReferencesRequest.
    	}
    	resp, err := c.IngestContextReferences(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) ListConversations 
    
    
    func (c *ConversationsClient) ListConversations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListConversationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListConversationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ConversationIterator

ListConversations returns the list of all conversations in the specified project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListConversationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListConversationsRequest.
    	}
    	it := c.ListConversations(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListConversationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListConversationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListConversationsRequest.
    	}
    	for resp, err := range c.ListConversations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ConversationsClient) ListLocations 
    
    
    func (c *ConversationsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewConversationsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
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
    

### func (*ConversationsClient) ListMessages 
    
    
    func (c *ConversationsClient) ListMessages(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListMessagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListMessagesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *MessageIterator

ListMessages lists messages that belong to a given conversation. messages are ordered by create_time in descending order. To fetch updates without duplication, send request with filter create_time_epoch_microseconds > [first item's create_time of previous request] and empty page_token.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListMessagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListMessagesRequest.
    	}
    	it := c.ListMessages(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListMessagesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListMessagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListMessagesRequest.
    	}
    	for resp, err := range c.ListMessages(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ConversationsClient) ListOperations 
    
    
    func (c *ConversationsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ConversationsClient) SearchKnowledge 
    
    
    func (c *ConversationsClient) SearchKnowledge(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SearchKnowledgeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SearchKnowledgeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SearchKnowledgeResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SearchKnowledgeResponse), [error](https://pkg.go.dev/builtin#error))

SearchKnowledge get answers for the given query based on knowledge documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SearchKnowledgeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SearchKnowledgeRequest.
    	}
    	resp, err := c.SearchKnowledge(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ConversationsClient) SuggestConversationSummary 
    
    
    func (c *ConversationsClient) SuggestConversationSummary(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestConversationSummaryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestConversationSummaryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestConversationSummaryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestConversationSummaryResponse), [error](https://pkg.go.dev/builtin#error))

SuggestConversationSummary suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewConversationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SuggestConversationSummaryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SuggestConversationSummaryRequest.
    	}
    	resp, err := c.SuggestConversationSummary(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CreateDocumentOperation
    
    
    type CreateDocumentOperation struct {
    	// contains filtered or unexported fields
    }

CreateDocumentOperation manages a long-running operation from CreateDocument.

### func (*CreateDocumentOperation) Done 
    
    
    func (op *CreateDocumentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateDocumentOperation) Metadata 
    
    
    func (op *CreateDocumentOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateDocumentOperation) Name 
    
    
    func (op *CreateDocumentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateDocumentOperation) Poll 
    
    
    func (op *CreateDocumentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateDocumentOperation) Wait 
    
    
    func (op *CreateDocumentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateGeneratorEvaluationOperation
    
    
    type CreateGeneratorEvaluationOperation struct {
    	// contains filtered or unexported fields
    }

CreateGeneratorEvaluationOperation manages a long-running operation from CreateGeneratorEvaluation.

### func (*CreateGeneratorEvaluationOperation) Done 
    
    
    func (op *CreateGeneratorEvaluationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateGeneratorEvaluationOperation) Metadata 
    
    
    func (op *CreateGeneratorEvaluationOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GeneratorEvaluationOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateGeneratorEvaluationOperation) Name 
    
    
    func (op *CreateGeneratorEvaluationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateGeneratorEvaluationOperation) Poll 
    
    
    func (op *CreateGeneratorEvaluationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GeneratorEvaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GeneratorEvaluation), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateGeneratorEvaluationOperation) Wait 
    
    
    func (op *CreateGeneratorEvaluationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GeneratorEvaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GeneratorEvaluation), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteDocumentOperation
    
    
    type DeleteDocumentOperation struct {
    	// contains filtered or unexported fields
    }

DeleteDocumentOperation manages a long-running operation from DeleteDocument.

### func (*DeleteDocumentOperation) Done 
    
    
    func (op *DeleteDocumentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteDocumentOperation) Metadata 
    
    
    func (op *DeleteDocumentOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteDocumentOperation) Name 
    
    
    func (op *DeleteDocumentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteDocumentOperation) Poll 
    
    
    func (op *DeleteDocumentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteDocumentOperation) Wait 
    
    
    func (op *DeleteDocumentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DocumentIterator
    
    
    type DocumentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Document, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DocumentIterator manages a stream of *dialogflowpb.Document.

### func (*DocumentIterator) All 
    
    
    func (it *DocumentIterator) All() iter.Seq2[*dialogflowpb.Document, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DocumentIterator) Next 
    
    
    func (it *DocumentIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DocumentIterator) PageInfo 
    
    
    func (it *DocumentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DocumentsCallOptions
    
    
    type DocumentsCallOptions struct {
    	ListDocuments   []gax.CallOption
    	GetDocument     []gax.CallOption
    	CreateDocument  []gax.CallOption
    	ImportDocuments []gax.CallOption
    	DeleteDocument  []gax.CallOption
    	UpdateDocument  []gax.CallOption
    	ReloadDocument  []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

DocumentsCallOptions contains the retry settings for each method of DocumentsClient.

## DocumentsClient
    
    
    type DocumentsClient struct {
    
    	// The call options for this service.
    	CallOptions *DocumentsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

DocumentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing knowledge Documents.

### func NewDocumentsClient 
    
    
    func NewDocumentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DocumentsClient, [error](https://pkg.go.dev/builtin#error))

NewDocumentsClient creates a new documents client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing knowledge Documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewDocumentsRESTClient 
    
    
    func NewDocumentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DocumentsClient, [error](https://pkg.go.dev/builtin#error))

NewDocumentsRESTClient creates a new documents rest client.

Service for managing knowledge Documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewDocumentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_DocumentsClient_NewDocumentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*DocumentsClient) CancelOperation 
    
    
    func (c *DocumentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DocumentsClient) Close 
    
    
    func (c *DocumentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*DocumentsClient) Connection (deprecated)
    
    
    func (c *DocumentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*DocumentsClient) CreateDocument 
    
    
    func (c *DocumentsClient) CreateDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateDocumentOperation, [error](https://pkg.go.dev/builtin#error))

CreateDocument creates a new document.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    KnowledgeOperationMetadata
    
    response: Document
    

Note: The projects.agent.knowledgeBases.documents resource is deprecated; only use projects.knowledgeBases.documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateDocumentRequest.
    	}
    	op, err := c.CreateDocument(ctx, req)
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
    

### func (*DocumentsClient) CreateDocumentOperation 
    
    
    func (c *DocumentsClient) CreateDocumentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateDocumentOperation

CreateDocumentOperation returns a new CreateDocumentOperation from a given name. The name must be that of a previously created CreateDocumentOperation, possibly from a different process.

### func (*DocumentsClient) DeleteDocument 
    
    
    func (c *DocumentsClient) DeleteDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteDocumentOperation, [error](https://pkg.go.dev/builtin#error))

DeleteDocument deletes the specified document.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    KnowledgeOperationMetadata
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: The projects.agent.knowledgeBases.documents resource is deprecated; only use projects.knowledgeBases.documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteDocumentRequest.
    	}
    	op, err := c.DeleteDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DocumentsClient) DeleteDocumentOperation 
    
    
    func (c *DocumentsClient) DeleteDocumentOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteDocumentOperation

DeleteDocumentOperation returns a new DeleteDocumentOperation from a given name. The name must be that of a previously created DeleteDocumentOperation, possibly from a different process.

### func (*DocumentsClient) GetDocument 
    
    
    func (c *DocumentsClient) GetDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

GetDocument retrieves the specified document.

Note: The projects.agent.knowledgeBases.documents resource is deprecated; only use projects.knowledgeBases.documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetDocumentRequest.
    	}
    	resp, err := c.GetDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DocumentsClient) GetLocation 
    
    
    func (c *DocumentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
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
    

### func (*DocumentsClient) GetOperation 
    
    
    func (c *DocumentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DocumentsClient) ImportDocuments 
    
    
    func (c *DocumentsClient) ImportDocuments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ImportDocumentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ImportDocumentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportDocumentsOperation, [error](https://pkg.go.dev/builtin#error))

ImportDocuments create documents by importing data from external sources. Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    KnowledgeOperationMetadata
    
    response:
    ImportDocumentsResponse
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ImportDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ImportDocumentsRequest.
    	}
    	op, err := c.ImportDocuments(ctx, req)
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
    

### func (*DocumentsClient) ImportDocumentsOperation 
    
    
    func (c *DocumentsClient) ImportDocumentsOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportDocumentsOperation

ImportDocumentsOperation returns a new ImportDocumentsOperation from a given name. The name must be that of a previously created ImportDocumentsOperation, possibly from a different process.

### func (*DocumentsClient) ListDocuments 
    
    
    func (c *DocumentsClient) ListDocuments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListDocumentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListDocumentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DocumentIterator

ListDocuments returns the list of all documents of the knowledge base.

Note: The projects.agent.knowledgeBases.documents resource is deprecated; only use projects.knowledgeBases.documents.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListDocumentsRequest.
    	}
    	it := c.ListDocuments(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListDocumentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListDocumentsRequest.
    	}
    	for resp, err := range c.ListDocuments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DocumentsClient) ListLocations 
    
    
    func (c *DocumentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewDocumentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
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
    

### func (*DocumentsClient) ListOperations 
    
    
    func (c *DocumentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DocumentsClient) ReloadDocument 
    
    
    func (c *DocumentsClient) ReloadDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ReloadDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ReloadDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ReloadDocumentOperation, [error](https://pkg.go.dev/builtin#error))

ReloadDocument reloads the specified document from its specified source, content_uri or content. The previously loaded content of the document will be deleted. Note: Even when the content of the document has not changed, there still may be side effects because of internal implementation changes. Note: If the document source is Google Cloud Storage URI, its metadata will be replaced with the custom metadata from Google Cloud Storage if the import_gcs_custom_metadata field is set to true in the request.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    KnowledgeOperationMetadata
    
    response: Document
    

Note: The projects.agent.knowledgeBases.documents resource is deprecated; only use projects.knowledgeBases.documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ReloadDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ReloadDocumentRequest.
    	}
    	op, err := c.ReloadDocument(ctx, req)
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
    

### func (*DocumentsClient) ReloadDocumentOperation 
    
    
    func (c *DocumentsClient) ReloadDocumentOperation(name [string](https://pkg.go.dev/builtin#string)) *ReloadDocumentOperation

ReloadDocumentOperation returns a new ReloadDocumentOperation from a given name. The name must be that of a previously created ReloadDocumentOperation, possibly from a different process.

### func (*DocumentsClient) UpdateDocument 
    
    
    func (c *DocumentsClient) UpdateDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateDocumentOperation, [error](https://pkg.go.dev/builtin#error))

UpdateDocument updates the specified document.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation>). The returned Operation type has the following method-specific fields:
    
    
    metadata:
    KnowledgeOperationMetadata
    
    response: Document
    

Note: The projects.agent.knowledgeBases.documents resource is deprecated; only use projects.knowledgeBases.documents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewDocumentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateDocumentRequest.
    	}
    	op, err := c.UpdateDocument(ctx, req)
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
    

### func (*DocumentsClient) UpdateDocumentOperation 
    
    
    func (c *DocumentsClient) UpdateDocumentOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateDocumentOperation

UpdateDocumentOperation returns a new UpdateDocumentOperation from a given name. The name must be that of a previously created UpdateDocumentOperation, possibly from a different process.

## EncryptionSpecCallOptions
    
    
    type EncryptionSpecCallOptions struct {
    	GetEncryptionSpec        []gax.CallOption
    	InitializeEncryptionSpec []gax.CallOption
    	GetLocation              []gax.CallOption
    	ListLocations            []gax.CallOption
    	CancelOperation          []gax.CallOption
    	GetOperation             []gax.CallOption
    	ListOperations           []gax.CallOption
    }

EncryptionSpecCallOptions contains the retry settings for each method of EncryptionSpecClient.

## EncryptionSpecClient
    
    
    type EncryptionSpecClient struct {
    
    	// The call options for this service.
    	CallOptions *EncryptionSpecCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

EncryptionSpecClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Manages encryption spec settings for Dialogflow and Agent Assist.

### func NewEncryptionSpecClient 
    
    
    func NewEncryptionSpecClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*EncryptionSpecClient, [error](https://pkg.go.dev/builtin#error))

NewEncryptionSpecClient creates a new encryption spec service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Manages encryption spec settings for Dialogflow and Agent Assist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewEncryptionSpecRESTClient 
    
    
    func NewEncryptionSpecRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*EncryptionSpecClient, [error](https://pkg.go.dev/builtin#error))

NewEncryptionSpecRESTClient creates a new encryption spec service rest client.

Manages encryption spec settings for Dialogflow and Agent Assist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*EncryptionSpecClient) CancelOperation 
    
    
    func (c *EncryptionSpecClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EncryptionSpecClient) Close 
    
    
    func (c *EncryptionSpecClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*EncryptionSpecClient) Connection (deprecated)
    
    
    func (c *EncryptionSpecClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*EncryptionSpecClient) GetEncryptionSpec 
    
    
    func (c *EncryptionSpecClient) GetEncryptionSpec(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetEncryptionSpecRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetEncryptionSpecRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[EncryptionSpec](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_EncryptionSpec), [error](https://pkg.go.dev/builtin#error))

GetEncryptionSpec gets location-level encryption key specification.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetEncryptionSpecRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetEncryptionSpecRequest.
    	}
    	resp, err := c.GetEncryptionSpec(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EncryptionSpecClient) GetLocation 
    
    
    func (c *EncryptionSpecClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
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
    

### func (*EncryptionSpecClient) GetOperation 
    
    
    func (c *EncryptionSpecClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EncryptionSpecClient) InitializeEncryptionSpec 
    
    
    func (c *EncryptionSpecClient) InitializeEncryptionSpec(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[InitializeEncryptionSpecRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_InitializeEncryptionSpecRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*InitializeEncryptionSpecOperation, [error](https://pkg.go.dev/builtin#error))

InitializeEncryptionSpec initializes a location-level encryption key specification. An error will be thrown if the location has resources already created before the initialization. Once the encryption specification is initialized at a location, it is immutable and all newly created resources under the location will be encrypted with the existing specification.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.InitializeEncryptionSpecRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#InitializeEncryptionSpecRequest.
    	}
    	op, err := c.InitializeEncryptionSpec(ctx, req)
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
    

### func (*EncryptionSpecClient) InitializeEncryptionSpecOperation 
    
    
    func (c *EncryptionSpecClient) InitializeEncryptionSpecOperation(name [string](https://pkg.go.dev/builtin#string)) *InitializeEncryptionSpecOperation

InitializeEncryptionSpecOperation returns a new InitializeEncryptionSpecOperation from a given name. The name must be that of a previously created InitializeEncryptionSpecOperation, possibly from a different process.

### func (*EncryptionSpecClient) ListLocations 
    
    
    func (c *EncryptionSpecClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
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
    

### func (*EncryptionSpecClient) ListOperations 
    
    
    func (c *EncryptionSpecClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEncryptionSpecClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EncryptionSpecClient_NewEncryptionSpecClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.EntityType, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EntityTypeIterator manages a stream of *dialogflowpb.EntityType.

### func (*EntityTypeIterator) All 
    
    
    func (it *EntityTypeIterator) All() iter.Seq2[*dialogflowpb.EntityType, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EntityTypeIterator) Next 
    
    
    func (it *EntityTypeIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_EntityType), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EntityTypeIterator) PageInfo 
    
    
    func (it *EntityTypeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## EntityTypesCallOptions
    
    
    type EntityTypesCallOptions struct {
    	ListEntityTypes        []gax.CallOption
    	GetEntityType          []gax.CallOption
    	CreateEntityType       []gax.CallOption
    	UpdateEntityType       []gax.CallOption
    	DeleteEntityType       []gax.CallOption
    	BatchUpdateEntityTypes []gax.CallOption
    	BatchDeleteEntityTypes []gax.CallOption
    	BatchCreateEntities    []gax.CallOption
    	BatchUpdateEntities    []gax.CallOption
    	BatchDeleteEntities    []gax.CallOption
    	GetLocation            []gax.CallOption
    	ListLocations          []gax.CallOption
    	CancelOperation        []gax.CallOption
    	GetOperation           []gax.CallOption
    	ListOperations         []gax.CallOption
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEntityTypesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EntityTypesClient_NewEntityTypesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*EntityTypesClient) BatchCreateEntities 
    
    
    func (c *EntityTypesClient) BatchCreateEntities(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchCreateEntitiesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchCreateEntitiesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchCreateEntitiesOperation, [error](https://pkg.go.dev/builtin#error))

BatchCreateEntities creates multiple new entities in the specified entity type.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchCreateEntitiesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchCreateEntitiesRequest.
    	}
    	op, err := c.BatchCreateEntities(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) BatchCreateEntitiesOperation 
    
    
    func (c *EntityTypesClient) BatchCreateEntitiesOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchCreateEntitiesOperation

BatchCreateEntitiesOperation returns a new BatchCreateEntitiesOperation from a given name. The name must be that of a previously created BatchCreateEntitiesOperation, possibly from a different process.

### func (*EntityTypesClient) BatchDeleteEntities 
    
    
    func (c *EntityTypesClient) BatchDeleteEntities(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchDeleteEntitiesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchDeleteEntitiesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchDeleteEntitiesOperation, [error](https://pkg.go.dev/builtin#error))

BatchDeleteEntities deletes entities in the specified entity type.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchDeleteEntitiesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchDeleteEntitiesRequest.
    	}
    	op, err := c.BatchDeleteEntities(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) BatchDeleteEntitiesOperation 
    
    
    func (c *EntityTypesClient) BatchDeleteEntitiesOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchDeleteEntitiesOperation

BatchDeleteEntitiesOperation returns a new BatchDeleteEntitiesOperation from a given name. The name must be that of a previously created BatchDeleteEntitiesOperation, possibly from a different process.

### func (*EntityTypesClient) BatchDeleteEntityTypes 
    
    
    func (c *EntityTypesClient) BatchDeleteEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchDeleteEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchDeleteEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchDeleteEntityTypesOperation, [error](https://pkg.go.dev/builtin#error))

BatchDeleteEntityTypes deletes entity types in the specified agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchDeleteEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchDeleteEntityTypesRequest.
    	}
    	op, err := c.BatchDeleteEntityTypes(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) BatchDeleteEntityTypesOperation 
    
    
    func (c *EntityTypesClient) BatchDeleteEntityTypesOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchDeleteEntityTypesOperation

BatchDeleteEntityTypesOperation returns a new BatchDeleteEntityTypesOperation from a given name. The name must be that of a previously created BatchDeleteEntityTypesOperation, possibly from a different process.

### func (*EntityTypesClient) BatchUpdateEntities 
    
    
    func (c *EntityTypesClient) BatchUpdateEntities(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateEntitiesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateEntitiesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchUpdateEntitiesOperation, [error](https://pkg.go.dev/builtin#error))

BatchUpdateEntities updates or creates multiple entities in the specified entity type. This method does not affect entities in the entity type that aren’t explicitly specified in the request.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchUpdateEntitiesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchUpdateEntitiesRequest.
    	}
    	op, err := c.BatchUpdateEntities(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) BatchUpdateEntitiesOperation 
    
    
    func (c *EntityTypesClient) BatchUpdateEntitiesOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchUpdateEntitiesOperation

BatchUpdateEntitiesOperation returns a new BatchUpdateEntitiesOperation from a given name. The name must be that of a previously created BatchUpdateEntitiesOperation, possibly from a different process.

### func (*EntityTypesClient) BatchUpdateEntityTypes 
    
    
    func (c *EntityTypesClient) BatchUpdateEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchUpdateEntityTypesOperation, [error](https://pkg.go.dev/builtin#error))

BatchUpdateEntityTypes updates/Creates multiple entity types in the specified agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response:
    BatchUpdateEntityTypesResponse
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchUpdateEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchUpdateEntityTypesRequest.
    	}
    	op, err := c.BatchUpdateEntityTypes(ctx, req)
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
    

### func (*EntityTypesClient) BatchUpdateEntityTypesOperation 
    
    
    func (c *EntityTypesClient) BatchUpdateEntityTypesOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchUpdateEntityTypesOperation

BatchUpdateEntityTypesOperation returns a new BatchUpdateEntityTypesOperation from a given name. The name must be that of a previously created BatchUpdateEntityTypesOperation, possibly from a different process.

### func (*EntityTypesClient) CancelOperation 
    
    
    func (c *EntityTypesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *EntityTypesClient) CreateEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_EntityType), [error](https://pkg.go.dev/builtin#error))

CreateEntityType creates an entity type in the specified agent.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateEntityTypeRequest.
    	}
    	resp, err := c.CreateEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) DeleteEntityType 
    
    
    func (c *EntityTypesClient) DeleteEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteEntityType deletes the specified entity type.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteEntityTypeRequest.
    	}
    	err = c.DeleteEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EntityTypesClient) GetEntityType 
    
    
    func (c *EntityTypesClient) GetEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_EntityType), [error](https://pkg.go.dev/builtin#error))

GetEntityType retrieves the specified entity type.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetEntityTypeRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EntityTypesClient) ListEntityTypes 
    
    
    func (c *EntityTypesClient) ListEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EntityTypeIterator

ListEntityTypes returns the list of all entity types in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListEntityTypesRequest.
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
    		_ = it.Response.(*dialogflowpb.ListEntityTypesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListEntityTypesRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EntityTypesClient) UpdateEntityType 
    
    
    func (c *EntityTypesClient) UpdateEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[EntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_EntityType), [error](https://pkg.go.dev/builtin#error))

UpdateEntityType updates the specified entity type.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateEntityTypeRequest.
    	}
    	resp, err := c.UpdateEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## EnvironmentHistory_EntryIterator
    
    
    type EnvironmentHistory_EntryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.EnvironmentHistory_Entry, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EnvironmentHistory_EntryIterator manages a stream of *dialogflowpb.EnvironmentHistory_Entry.

### func (*EnvironmentHistory_EntryIterator) All 
    
    
    func (it *EnvironmentHistory_EntryIterator) All() iter.Seq2[*dialogflowpb.EnvironmentHistory_Entry, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EnvironmentHistory_EntryIterator) Next 
    
    
    func (it *EnvironmentHistory_EntryIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[EnvironmentHistory_Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_EnvironmentHistory_Entry), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EnvironmentHistory_EntryIterator) PageInfo 
    
    
    func (it *EnvironmentHistory_EntryIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Environment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EnvironmentIterator manages a stream of *dialogflowpb.Environment.

### func (*EnvironmentIterator) All 
    
    
    func (it *EnvironmentIterator) All() iter.Seq2[*dialogflowpb.Environment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EnvironmentIterator) Next 
    
    
    func (it *EnvironmentIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Environment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EnvironmentIterator) PageInfo 
    
    
    func (it *EnvironmentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## EnvironmentsCallOptions
    
    
    type EnvironmentsCallOptions struct {
    	ListEnvironments      []gax.CallOption
    	GetEnvironment        []gax.CallOption
    	CreateEnvironment     []gax.CallOption
    	UpdateEnvironment     []gax.CallOption
    	DeleteEnvironment     []gax.CallOption
    	GetEnvironmentHistory []gax.CallOption
    	GetLocation           []gax.CallOption
    	ListLocations         []gax.CallOption
    	CancelOperation       []gax.CallOption
    	GetOperation          []gax.CallOption
    	ListOperations        []gax.CallOption
    }

EnvironmentsCallOptions contains the retry settings for each method of EnvironmentsClient.

## EnvironmentsClient
    
    
    type EnvironmentsClient struct {
    
    	// The call options for this service.
    	CallOptions *EnvironmentsCallOptions
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewEnvironmentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_EnvironmentsClient_NewEnvironmentsRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *EnvironmentsClient) CreateEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Environment), [error](https://pkg.go.dev/builtin#error))

CreateEnvironment creates an agent environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateEnvironmentRequest.
    	}
    	resp, err := c.CreateEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) DeleteEnvironment 
    
    
    func (c *EnvironmentsClient) DeleteEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteEnvironment deletes the specified agent environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteEnvironmentRequest.
    	}
    	err = c.DeleteEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*EnvironmentsClient) GetEnvironment 
    
    
    func (c *EnvironmentsClient) GetEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Environment), [error](https://pkg.go.dev/builtin#error))

GetEnvironment retrieves the specified agent environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetEnvironmentRequest.
    	}
    	resp, err := c.GetEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) GetEnvironmentHistory 
    
    
    func (c *EnvironmentsClient) GetEnvironmentHistory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetEnvironmentHistoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetEnvironmentHistoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EnvironmentHistory_EntryIterator

GetEnvironmentHistory gets the history of the specified environment.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetEnvironmentHistoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetEnvironmentHistoryRequest.
    	}
    	it := c.GetEnvironmentHistory(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.EnvironmentHistory)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetEnvironmentHistoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetEnvironmentHistoryRequest.
    	}
    	for resp, err := range c.GetEnvironmentHistory(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) GetLocation 
    
    
    func (c *EnvironmentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*EnvironmentsClient) ListEnvironments 
    
    
    func (c *EnvironmentsClient) ListEnvironments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListEnvironmentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListEnvironmentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EnvironmentIterator

ListEnvironments returns the list of all non-draft environments of the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListEnvironmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListEnvironmentsRequest.
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
    		_ = it.Response.(*dialogflowpb.ListEnvironmentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListEnvironmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListEnvironmentsRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*EnvironmentsClient) UpdateEnvironment 
    
    
    func (c *EnvironmentsClient) UpdateEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Environment), [error](https://pkg.go.dev/builtin#error))

UpdateEnvironment updates the specified agent environment.

This method allows you to deploy new agent versions into the environment. When an environment is pointed to a new agent version by setting environment.agent_version, the environment is temporarily set to the LOADING state. During that time, the environment keeps on serving the previous version of the agent. After the new agent version is done loading, the environment is set back to the RUNNING state. You can use “-” as Environment ID in environment name to update version in “draft” environment. WARNING: this will negate all recent changes to draft and can’t be undone. You may want to save the draft to a version before calling this function.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewEnvironmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateEnvironmentRequest.
    	}
    	resp, err := c.UpdateEnvironment(ctx, req)
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
    
    
    func (op *ExportAgentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ExportAgentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ExportAgentResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportAgentOperation) Wait 
    
    
    func (op *ExportAgentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ExportAgentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ExportAgentResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## FulfillmentsCallOptions
    
    
    type FulfillmentsCallOptions struct {
    	GetFulfillment    []gax.CallOption
    	UpdateFulfillment []gax.CallOption
    	GetLocation       []gax.CallOption
    	ListLocations     []gax.CallOption
    	CancelOperation   []gax.CallOption
    	GetOperation      []gax.CallOption
    	ListOperations    []gax.CallOption
    }

FulfillmentsCallOptions contains the retry settings for each method of FulfillmentsClient.

## FulfillmentsClient
    
    
    type FulfillmentsClient struct {
    
    	// The call options for this service.
    	CallOptions *FulfillmentsCallOptions
    	// contains filtered or unexported fields
    }

FulfillmentsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Fulfillments.

### func NewFulfillmentsClient 
    
    
    func NewFulfillmentsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FulfillmentsClient, [error](https://pkg.go.dev/builtin#error))

NewFulfillmentsClient creates a new fulfillments client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Fulfillments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewFulfillmentsRESTClient 
    
    
    func NewFulfillmentsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FulfillmentsClient, [error](https://pkg.go.dev/builtin#error))

NewFulfillmentsRESTClient creates a new fulfillments rest client.

Service for managing Fulfillments.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewFulfillmentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_FulfillmentsClient_NewFulfillmentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*FulfillmentsClient) CancelOperation 
    
    
    func (c *FulfillmentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FulfillmentsClient) Close 
    
    
    func (c *FulfillmentsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*FulfillmentsClient) Connection (deprecated)
    
    
    func (c *FulfillmentsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*FulfillmentsClient) GetFulfillment 
    
    
    func (c *FulfillmentsClient) GetFulfillment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetFulfillmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetFulfillmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Fulfillment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Fulfillment), [error](https://pkg.go.dev/builtin#error))

GetFulfillment retrieves the fulfillment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetFulfillmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetFulfillmentRequest.
    	}
    	resp, err := c.GetFulfillment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FulfillmentsClient) GetLocation 
    
    
    func (c *FulfillmentsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
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
    

### func (*FulfillmentsClient) GetOperation 
    
    
    func (c *FulfillmentsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FulfillmentsClient) ListLocations 
    
    
    func (c *FulfillmentsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
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
    

### func (*FulfillmentsClient) ListOperations 
    
    
    func (c *FulfillmentsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FulfillmentsClient) UpdateFulfillment 
    
    
    func (c *FulfillmentsClient) UpdateFulfillment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateFulfillmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateFulfillmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Fulfillment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Fulfillment), [error](https://pkg.go.dev/builtin#error))

UpdateFulfillment updates the fulfillment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewFulfillmentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateFulfillmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateFulfillmentRequest.
    	}
    	resp, err := c.UpdateFulfillment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## GeneratorEvaluationIterator
    
    
    type GeneratorEvaluationIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.GeneratorEvaluation, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GeneratorEvaluationIterator manages a stream of *dialogflowpb.GeneratorEvaluation.

### func (*GeneratorEvaluationIterator) All 
    
    
    func (it *GeneratorEvaluationIterator) All() iter.Seq2[*dialogflowpb.GeneratorEvaluation, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GeneratorEvaluationIterator) Next 
    
    
    func (it *GeneratorEvaluationIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GeneratorEvaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GeneratorEvaluation), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GeneratorEvaluationIterator) PageInfo 
    
    
    func (it *GeneratorEvaluationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GeneratorEvaluationsCallOptions
    
    
    type GeneratorEvaluationsCallOptions struct {
    	CreateGeneratorEvaluation []gax.CallOption
    	GetGeneratorEvaluation    []gax.CallOption
    	ListGeneratorEvaluations  []gax.CallOption
    	DeleteGeneratorEvaluation []gax.CallOption
    	GetLocation               []gax.CallOption
    	ListLocations             []gax.CallOption
    	CancelOperation           []gax.CallOption
    	GetOperation              []gax.CallOption
    	ListOperations            []gax.CallOption
    }

GeneratorEvaluationsCallOptions contains the retry settings for each method of GeneratorEvaluationsClient.

## GeneratorEvaluationsClient
    
    
    type GeneratorEvaluationsClient struct {
    
    	// The call options for this service.
    	CallOptions *GeneratorEvaluationsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

GeneratorEvaluationsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing generator evaluations.

### func NewGeneratorEvaluationsClient 
    
    
    func NewGeneratorEvaluationsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GeneratorEvaluationsClient, [error](https://pkg.go.dev/builtin#error))

NewGeneratorEvaluationsClient creates a new generator evaluations client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing generator evaluations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewGeneratorEvaluationsRESTClient 
    
    
    func NewGeneratorEvaluationsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GeneratorEvaluationsClient, [error](https://pkg.go.dev/builtin#error))

NewGeneratorEvaluationsRESTClient creates a new generator evaluations rest client.

Service for managing generator evaluations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewGeneratorEvaluationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_GeneratorEvaluationsClient_NewGeneratorEvaluationsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*GeneratorEvaluationsClient) CancelOperation 
    
    
    func (c *GeneratorEvaluationsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GeneratorEvaluationsClient) Close 
    
    
    func (c *GeneratorEvaluationsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*GeneratorEvaluationsClient) Connection (deprecated)
    
    
    func (c *GeneratorEvaluationsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*GeneratorEvaluationsClient) CreateGeneratorEvaluation 
    
    
    func (c *GeneratorEvaluationsClient) CreateGeneratorEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateGeneratorEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateGeneratorEvaluationOperation, [error](https://pkg.go.dev/builtin#error))

CreateGeneratorEvaluation creates evaluation of a generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateGeneratorEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateGeneratorEvaluationRequest.
    	}
    	op, err := c.CreateGeneratorEvaluation(ctx, req)
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
    

### func (*GeneratorEvaluationsClient) CreateGeneratorEvaluationOperation 
    
    
    func (c *GeneratorEvaluationsClient) CreateGeneratorEvaluationOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateGeneratorEvaluationOperation

CreateGeneratorEvaluationOperation returns a new CreateGeneratorEvaluationOperation from a given name. The name must be that of a previously created CreateGeneratorEvaluationOperation, possibly from a different process.

### func (*GeneratorEvaluationsClient) DeleteGeneratorEvaluation 
    
    
    func (c *GeneratorEvaluationsClient) DeleteGeneratorEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteGeneratorEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteGeneratorEvaluation deletes an evaluation of generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteGeneratorEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteGeneratorEvaluationRequest.
    	}
    	err = c.DeleteGeneratorEvaluation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GeneratorEvaluationsClient) GetGeneratorEvaluation 
    
    
    func (c *GeneratorEvaluationsClient) GetGeneratorEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetGeneratorEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetGeneratorEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GeneratorEvaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GeneratorEvaluation), [error](https://pkg.go.dev/builtin#error))

GetGeneratorEvaluation gets an evaluation of generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetGeneratorEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetGeneratorEvaluationRequest.
    	}
    	resp, err := c.GetGeneratorEvaluation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorEvaluationsClient) GetLocation 
    
    
    func (c *GeneratorEvaluationsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
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
    

### func (*GeneratorEvaluationsClient) GetOperation 
    
    
    func (c *GeneratorEvaluationsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorEvaluationsClient) ListGeneratorEvaluations 
    
    
    func (c *GeneratorEvaluationsClient) ListGeneratorEvaluations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListGeneratorEvaluationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GeneratorEvaluationIterator

ListGeneratorEvaluations lists evaluations of generator.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListGeneratorEvaluationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListGeneratorEvaluationsRequest.
    	}
    	it := c.ListGeneratorEvaluations(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListGeneratorEvaluationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListGeneratorEvaluationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListGeneratorEvaluationsRequest.
    	}
    	for resp, err := range c.ListGeneratorEvaluations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GeneratorEvaluationsClient) ListLocations 
    
    
    func (c *GeneratorEvaluationsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
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
    

### func (*GeneratorEvaluationsClient) ListOperations 
    
    
    func (c *GeneratorEvaluationsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorEvaluationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Generator, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GeneratorIterator manages a stream of *dialogflowpb.Generator.

### func (*GeneratorIterator) All 
    
    
    func (it *GeneratorIterator) All() iter.Seq2[*dialogflowpb.Generator, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GeneratorIterator) Next 
    
    
    func (it *GeneratorIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Generator), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GeneratorIterator) PageInfo 
    
    
    func (it *GeneratorIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GeneratorsCallOptions
    
    
    type GeneratorsCallOptions struct {
    	CreateGenerator []gax.CallOption
    	GetGenerator    []gax.CallOption
    	ListGenerators  []gax.CallOption
    	DeleteGenerator []gax.CallOption
    	UpdateGenerator []gax.CallOption
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

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

### func NewGeneratorsClient 
    
    
    func NewGeneratorsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GeneratorsClient, [error](https://pkg.go.dev/builtin#error))

NewGeneratorsClient creates a new generators client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
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

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewGeneratorsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_GeneratorsClient_NewGeneratorsRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *GeneratorsClient) CreateGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Generator), [error](https://pkg.go.dev/builtin#error))

CreateGenerator creates a generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateGeneratorRequest.
    	}
    	resp, err := c.CreateGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorsClient) DeleteGenerator 
    
    
    func (c *GeneratorsClient) DeleteGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteGenerator deletes a generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteGeneratorRequest.
    	}
    	err = c.DeleteGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GeneratorsClient) GetGenerator 
    
    
    func (c *GeneratorsClient) GetGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Generator), [error](https://pkg.go.dev/builtin#error))

GetGenerator retrieves a generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetGeneratorRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GeneratorsClient) ListGenerators 
    
    
    func (c *GeneratorsClient) ListGenerators(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListGeneratorsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListGeneratorsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GeneratorIterator

ListGenerators lists generators.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListGeneratorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListGeneratorsRequest.
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
    		_ = it.Response.(*dialogflowpb.ListGeneratorsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListGeneratorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListGeneratorsRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewGeneratorsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GeneratorsClient) UpdateGenerator 
    
    
    func (c *GeneratorsClient) UpdateGenerator(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateGeneratorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateGeneratorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Generator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Generator), [error](https://pkg.go.dev/builtin#error))

UpdateGenerator updates a generator.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewGeneratorsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateGeneratorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateGeneratorRequest.
    	}
    	resp, err := c.UpdateGenerator(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ImportAgentOperation
    
    
    type ImportAgentOperation struct {
    	// contains filtered or unexported fields
    }

ImportAgentOperation manages a long-running operation from ImportAgent.

### func (*ImportAgentOperation) Done 
    
    
    func (op *ImportAgentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportAgentOperation) Metadata 
    
    
    func (op *ImportAgentOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportAgentOperation) Name 
    
    
    func (op *ImportAgentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportAgentOperation) Poll 
    
    
    func (op *ImportAgentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportAgentOperation) Wait 
    
    
    func (op *ImportAgentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportDocumentsOperation
    
    
    type ImportDocumentsOperation struct {
    	// contains filtered or unexported fields
    }

ImportDocumentsOperation manages a long-running operation from ImportDocuments.

### func (*ImportDocumentsOperation) Done 
    
    
    func (op *ImportDocumentsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportDocumentsOperation) Metadata 
    
    
    func (op *ImportDocumentsOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportDocumentsOperation) Name 
    
    
    func (op *ImportDocumentsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportDocumentsOperation) Poll 
    
    
    func (op *ImportDocumentsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ImportDocumentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ImportDocumentsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportDocumentsOperation) Wait 
    
    
    func (op *ImportDocumentsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ImportDocumentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ImportDocumentsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## InitializeEncryptionSpecOperation
    
    
    type InitializeEncryptionSpecOperation struct {
    	// contains filtered or unexported fields
    }

InitializeEncryptionSpecOperation manages a long-running operation from InitializeEncryptionSpec.

### func (*InitializeEncryptionSpecOperation) Done 
    
    
    func (op *InitializeEncryptionSpecOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*InitializeEncryptionSpecOperation) Metadata 
    
    
    func (op *InitializeEncryptionSpecOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[InitializeEncryptionSpecMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_InitializeEncryptionSpecMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*InitializeEncryptionSpecOperation) Name 
    
    
    func (op *InitializeEncryptionSpecOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*InitializeEncryptionSpecOperation) Poll 
    
    
    func (op *InitializeEncryptionSpecOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[InitializeEncryptionSpecResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_InitializeEncryptionSpecResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*InitializeEncryptionSpecOperation) Wait 
    
    
    func (op *InitializeEncryptionSpecOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[InitializeEncryptionSpecResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_InitializeEncryptionSpecResponse), [error](https://pkg.go.dev/builtin#error))

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Intent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

IntentIterator manages a stream of *dialogflowpb.Intent.

### func (*IntentIterator) All 
    
    
    func (it *IntentIterator) All() iter.Seq2[*dialogflowpb.Intent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*IntentIterator) Next 
    
    
    func (it *IntentIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Intent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*IntentIterator) PageInfo 
    
    
    func (it *IntentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## IntentsCallOptions
    
    
    type IntentsCallOptions struct {
    	ListIntents        []gax.CallOption
    	GetIntent          []gax.CallOption
    	CreateIntent       []gax.CallOption
    	UpdateIntent       []gax.CallOption
    	DeleteIntent       []gax.CallOption
    	BatchUpdateIntents []gax.CallOption
    	BatchDeleteIntents []gax.CallOption
    	GetLocation        []gax.CallOption
    	ListLocations      []gax.CallOption
    	CancelOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewIntentsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_IntentsClient_NewIntentsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*IntentsClient) BatchDeleteIntents 
    
    
    func (c *IntentsClient) BatchDeleteIntents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchDeleteIntentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchDeleteIntentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchDeleteIntentsOperation, [error](https://pkg.go.dev/builtin#error))

BatchDeleteIntents deletes intents in the specified agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response: An Empty
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchDeleteIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchDeleteIntentsRequest.
    	}
    	op, err := c.BatchDeleteIntents(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*IntentsClient) BatchDeleteIntentsOperation 
    
    
    func (c *IntentsClient) BatchDeleteIntentsOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchDeleteIntentsOperation

BatchDeleteIntentsOperation returns a new BatchDeleteIntentsOperation from a given name. The name must be that of a previously created BatchDeleteIntentsOperation, possibly from a different process.

### func (*IntentsClient) BatchUpdateIntents 
    
    
    func (c *IntentsClient) BatchUpdateIntents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[BatchUpdateIntentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_BatchUpdateIntentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*BatchUpdateIntentsOperation, [error](https://pkg.go.dev/builtin#error))

BatchUpdateIntents updates/Creates multiple intents in the specified agent.

This method is a long-running operation (at <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>). The returned Operation type has the following method-specific fields:
    
    
    metadata: An empty Struct
    message (at https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)
    
    response:
    BatchUpdateIntentsResponse
    

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.BatchUpdateIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#BatchUpdateIntentsRequest.
    	}
    	op, err := c.BatchUpdateIntents(ctx, req)
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
    

### func (*IntentsClient) BatchUpdateIntentsOperation 
    
    
    func (c *IntentsClient) BatchUpdateIntentsOperation(name [string](https://pkg.go.dev/builtin#string)) *BatchUpdateIntentsOperation

BatchUpdateIntentsOperation returns a new BatchUpdateIntentsOperation from a given name. The name must be that of a previously created BatchUpdateIntentsOperation, possibly from a different process.

### func (*IntentsClient) CancelOperation 
    
    
    func (c *IntentsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *IntentsClient) CreateIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Intent), [error](https://pkg.go.dev/builtin#error))

CreateIntent creates an intent in the specified agent.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateIntentRequest.
    	}
    	resp, err := c.CreateIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) DeleteIntent 
    
    
    func (c *IntentsClient) DeleteIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteIntent deletes the specified intent and its direct or indirect followup intents.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteIntentRequest.
    	}
    	err = c.DeleteIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*IntentsClient) GetIntent 
    
    
    func (c *IntentsClient) GetIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Intent), [error](https://pkg.go.dev/builtin#error))

GetIntent retrieves the specified intent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetIntentRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*IntentsClient) ListIntents 
    
    
    func (c *IntentsClient) ListIntents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListIntentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListIntentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *IntentIterator

ListIntents returns the list of all intents in the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListIntentsRequest.
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
    		_ = it.Response.(*dialogflowpb.ListIntentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListIntentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListIntentsRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewIntentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*IntentsClient) UpdateIntent 
    
    
    func (c *IntentsClient) UpdateIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Intent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Intent), [error](https://pkg.go.dev/builtin#error))

UpdateIntent updates the specified intent.

Note: You should always train an agent prior to sending it queries. See the training documentation (at <https://cloud.google.com/dialogflow/es/docs/training>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewIntentsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateIntentRequest.
    	}
    	resp, err := c.UpdateIntent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## KnowledgeBaseIterator
    
    
    type KnowledgeBaseIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.KnowledgeBase, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

KnowledgeBaseIterator manages a stream of *dialogflowpb.KnowledgeBase.

### func (*KnowledgeBaseIterator) All 
    
    
    func (it *KnowledgeBaseIterator) All() iter.Seq2[*dialogflowpb.KnowledgeBase, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*KnowledgeBaseIterator) Next 
    
    
    func (it *KnowledgeBaseIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeBase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeBase), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*KnowledgeBaseIterator) PageInfo 
    
    
    func (it *KnowledgeBaseIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## KnowledgeBasesCallOptions
    
    
    type KnowledgeBasesCallOptions struct {
    	ListKnowledgeBases  []gax.CallOption
    	GetKnowledgeBase    []gax.CallOption
    	CreateKnowledgeBase []gax.CallOption
    	DeleteKnowledgeBase []gax.CallOption
    	UpdateKnowledgeBase []gax.CallOption
    	GetLocation         []gax.CallOption
    	ListLocations       []gax.CallOption
    	CancelOperation     []gax.CallOption
    	GetOperation        []gax.CallOption
    	ListOperations      []gax.CallOption
    }

KnowledgeBasesCallOptions contains the retry settings for each method of KnowledgeBasesClient.

## KnowledgeBasesClient
    
    
    type KnowledgeBasesClient struct {
    
    	// The call options for this service.
    	CallOptions *KnowledgeBasesCallOptions
    	// contains filtered or unexported fields
    }

KnowledgeBasesClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing KnowledgeBases.

### func NewKnowledgeBasesClient 
    
    
    func NewKnowledgeBasesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*KnowledgeBasesClient, [error](https://pkg.go.dev/builtin#error))

NewKnowledgeBasesClient creates a new knowledge bases client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing KnowledgeBases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewKnowledgeBasesRESTClient 
    
    
    func NewKnowledgeBasesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*KnowledgeBasesClient, [error](https://pkg.go.dev/builtin#error))

NewKnowledgeBasesRESTClient creates a new knowledge bases rest client.

Service for managing KnowledgeBases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewKnowledgeBasesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_KnowledgeBasesClient_NewKnowledgeBasesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*KnowledgeBasesClient) CancelOperation 
    
    
    func (c *KnowledgeBasesClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*KnowledgeBasesClient) Close 
    
    
    func (c *KnowledgeBasesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*KnowledgeBasesClient) Connection (deprecated)
    
    
    func (c *KnowledgeBasesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*KnowledgeBasesClient) CreateKnowledgeBase 
    
    
    func (c *KnowledgeBasesClient) CreateKnowledgeBase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateKnowledgeBaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateKnowledgeBaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeBase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeBase), [error](https://pkg.go.dev/builtin#error))

CreateKnowledgeBase creates a knowledge base.

Note: The projects.agent.knowledgeBases resource is deprecated; only use projects.knowledgeBases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateKnowledgeBaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateKnowledgeBaseRequest.
    	}
    	resp, err := c.CreateKnowledgeBase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*KnowledgeBasesClient) DeleteKnowledgeBase 
    
    
    func (c *KnowledgeBasesClient) DeleteKnowledgeBase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteKnowledgeBaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteKnowledgeBase deletes the specified knowledge base.

Note: The projects.agent.knowledgeBases resource is deprecated; only use projects.knowledgeBases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteKnowledgeBaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteKnowledgeBaseRequest.
    	}
    	err = c.DeleteKnowledgeBase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*KnowledgeBasesClient) GetKnowledgeBase 
    
    
    func (c *KnowledgeBasesClient) GetKnowledgeBase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetKnowledgeBaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetKnowledgeBaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeBase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeBase), [error](https://pkg.go.dev/builtin#error))

GetKnowledgeBase retrieves the specified knowledge base.

Note: The projects.agent.knowledgeBases resource is deprecated; only use projects.knowledgeBases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetKnowledgeBaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetKnowledgeBaseRequest.
    	}
    	resp, err := c.GetKnowledgeBase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*KnowledgeBasesClient) GetLocation 
    
    
    func (c *KnowledgeBasesClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
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
    

### func (*KnowledgeBasesClient) GetOperation 
    
    
    func (c *KnowledgeBasesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*KnowledgeBasesClient) ListKnowledgeBases 
    
    
    func (c *KnowledgeBasesClient) ListKnowledgeBases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListKnowledgeBasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListKnowledgeBasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *KnowledgeBaseIterator

ListKnowledgeBases returns the list of all knowledge bases of the specified agent.

Note: The projects.agent.knowledgeBases resource is deprecated; only use projects.knowledgeBases.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListKnowledgeBasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListKnowledgeBasesRequest.
    	}
    	it := c.ListKnowledgeBases(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListKnowledgeBasesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListKnowledgeBasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListKnowledgeBasesRequest.
    	}
    	for resp, err := range c.ListKnowledgeBases(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*KnowledgeBasesClient) ListLocations 
    
    
    func (c *KnowledgeBasesClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
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
    

### func (*KnowledgeBasesClient) ListOperations 
    
    
    func (c *KnowledgeBasesClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*KnowledgeBasesClient) UpdateKnowledgeBase 
    
    
    func (c *KnowledgeBasesClient) UpdateKnowledgeBase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateKnowledgeBaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeBase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeBase), [error](https://pkg.go.dev/builtin#error))

UpdateKnowledgeBase updates the specified knowledge base.

Note: The projects.agent.knowledgeBases resource is deprecated; only use projects.knowledgeBases.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewKnowledgeBasesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateKnowledgeBaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateKnowledgeBaseRequest.
    	}
    	resp, err := c.UpdateKnowledgeBase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

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

## MessageIterator
    
    
    type MessageIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Message, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

MessageIterator manages a stream of *dialogflowpb.Message.

### func (*MessageIterator) All 
    
    
    func (it *MessageIterator) All() iter.Seq2[*dialogflowpb.Message, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*MessageIterator) Next 
    
    
    func (it *MessageIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Message](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Message), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*MessageIterator) PageInfo 
    
    
    func (it *MessageIterator) PageInfo() *iterator.PageInfo

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

## ParticipantIterator
    
    
    type ParticipantIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Participant, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ParticipantIterator manages a stream of *dialogflowpb.Participant.

### func (*ParticipantIterator) All 
    
    
    func (it *ParticipantIterator) All() iter.Seq2[*dialogflowpb.Participant, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ParticipantIterator) Next 
    
    
    func (it *ParticipantIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Participant](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Participant), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ParticipantIterator) PageInfo 
    
    
    func (it *ParticipantIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ParticipantsCallOptions
    
    
    type ParticipantsCallOptions struct {
    	CreateParticipant           []gax.CallOption
    	GetParticipant              []gax.CallOption
    	ListParticipants            []gax.CallOption
    	UpdateParticipant           []gax.CallOption
    	AnalyzeContent              []gax.CallOption
    	StreamingAnalyzeContent     []gax.CallOption
    	BidiStreamingAnalyzeContent []gax.CallOption
    	SuggestArticles             []gax.CallOption
    	SuggestFaqAnswers           []gax.CallOption
    	SuggestSmartReplies         []gax.CallOption
    	SuggestKnowledgeAssist      []gax.CallOption
    	ListSuggestions             []gax.CallOption
    	CompileSuggestion           []gax.CallOption
    	GetLocation                 []gax.CallOption
    	ListLocations               []gax.CallOption
    	CancelOperation             []gax.CallOption
    	GetOperation                []gax.CallOption
    	ListOperations              []gax.CallOption
    }

ParticipantsCallOptions contains the retry settings for each method of ParticipantsClient.

## ParticipantsClient
    
    
    type ParticipantsClient struct {
    
    	// The call options for this service.
    	CallOptions *ParticipantsCallOptions
    	// contains filtered or unexported fields
    }

ParticipantsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing Participants.

### func NewParticipantsClient 
    
    
    func NewParticipantsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ParticipantsClient, [error](https://pkg.go.dev/builtin#error))

NewParticipantsClient creates a new participants client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing Participants.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewParticipantsRESTClient 
    
    
    func NewParticipantsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ParticipantsClient, [error](https://pkg.go.dev/builtin#error))

NewParticipantsRESTClient creates a new participants rest client.

Service for managing Participants.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewParticipantsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_ParticipantsClient_NewParticipantsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ParticipantsClient) AnalyzeContent 
    
    
    func (c *ParticipantsClient) AnalyzeContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[AnalyzeContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_AnalyzeContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[AnalyzeContentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_AnalyzeContentResponse), [error](https://pkg.go.dev/builtin#error))

AnalyzeContent adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See Versions and environments (at <https://cloud.google.com/dialogflow/es/docs/agents-versions>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.AnalyzeContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#AnalyzeContentRequest.
    	}
    	resp, err := c.AnalyzeContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) BidiStreamingAnalyzeContent 
    
    
    func (c *ParticipantsClient) BidiStreamingAnalyzeContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Participants_BidiStreamingAnalyzeContentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Participants_BidiStreamingAnalyzeContentClient), [error](https://pkg.go.dev/builtin#error))

BidiStreamingAnalyzeContent bidirectional endless streaming version of StreamingAnalyzeContent.

This method is not supported for the REST transport.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"io"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    	stream, err := c.BidiStreamingAnalyzeContent(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	go func() {
    		reqs := []*dialogflowpb.BidiStreamingAnalyzeContentRequest{
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
    

### func (*ParticipantsClient) CancelOperation 
    
    
    func (c *ParticipantsClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ParticipantsClient) Close 
    
    
    func (c *ParticipantsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ParticipantsClient) CompileSuggestion (deprecated)
    
    
    func (c *ParticipantsClient) CompileSuggestion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CompileSuggestionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CompileSuggestionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CompileSuggestionResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CompileSuggestionResponse), [error](https://pkg.go.dev/builtin#error))

CompileSuggestion deprecated. use SuggestArticles and SuggestFaqAnswers instead.

Gets suggestions for a participant based on specific historical messages.

Note that ListSuggestions will only list the auto-generated suggestions, while CompileSuggestion will try to compile suggestion based on the provided conversation context in the real time.

Deprecated: CompileSuggestion may be removed in a future version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CompileSuggestionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CompileSuggestionRequest.
    	}
    	resp, err := c.CompileSuggestion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) Connection (deprecated)
    
    
    func (c *ParticipantsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ParticipantsClient) CreateParticipant 
    
    
    func (c *ParticipantsClient) CreateParticipant(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateParticipantRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateParticipantRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Participant](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Participant), [error](https://pkg.go.dev/builtin#error))

CreateParticipant creates a new participant in a conversation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateParticipantRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateParticipantRequest.
    	}
    	resp, err := c.CreateParticipant(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) GetLocation 
    
    
    func (c *ParticipantsClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
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
    

### func (*ParticipantsClient) GetOperation 
    
    
    func (c *ParticipantsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) GetParticipant 
    
    
    func (c *ParticipantsClient) GetParticipant(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetParticipantRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetParticipantRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Participant](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Participant), [error](https://pkg.go.dev/builtin#error))

GetParticipant retrieves a conversation participant.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetParticipantRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetParticipantRequest.
    	}
    	resp, err := c.GetParticipant(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) ListLocations 
    
    
    func (c *ParticipantsClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewParticipantsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
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
    

### func (*ParticipantsClient) ListOperations 
    
    
    func (c *ParticipantsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ParticipantsClient) ListParticipants 
    
    
    func (c *ParticipantsClient) ListParticipants(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListParticipantsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListParticipantsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ParticipantIterator

ListParticipants returns the list of all participants in the specified conversation.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListParticipantsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListParticipantsRequest.
    	}
    	it := c.ListParticipants(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListParticipantsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListParticipantsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListParticipantsRequest.
    	}
    	for resp, err := range c.ListParticipants(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ParticipantsClient) ListSuggestions (deprecated)
    
    
    func (c *ParticipantsClient) ListSuggestions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListSuggestionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListSuggestionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SuggestionIterator

ListSuggestions deprecated: Use inline suggestion, event based suggestion or Suggestion* API instead. See [HumanAgentAssistantConfig.name (at http://HumanAgentAssistantConfig.name)][google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.name (at <http://google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.name>)] for more details. Removal Date: 2020-09-01.

Retrieves suggestions for live agents.

This method should be used by human agent client software to fetch auto generated suggestions in real-time, while the conversation with an end user is in progress. The functionality is implemented in terms of the list pagination (at <https://cloud.google.com/apis/design/design_patterns#list_pagination>) design pattern. The client app should use the next_page_token field to fetch the next batch of suggestions. suggestions are sorted by create_time in descending order. To fetch latest suggestion, just set page_size to 1. To fetch new suggestions without duplication, send request with filter create_time_epoch_microseconds > [first item's create_time of previous request] and empty page_token.

Deprecated: ListSuggestions may be removed in a future version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListSuggestionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListSuggestionsRequest.
    	}
    	it := c.ListSuggestions(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListSuggestionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListSuggestionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListSuggestionsRequest.
    	}
    	for resp, err := range c.ListSuggestions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ParticipantsClient) StreamingAnalyzeContent 
    
    
    func (c *ParticipantsClient) StreamingAnalyzeContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Participants_StreamingAnalyzeContentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Participants_StreamingAnalyzeContentClient), [error](https://pkg.go.dev/builtin#error))

StreamingAnalyzeContent adds a text (e.g., chat) or audio (e.g., phone recording) message from a participant into the conversation. Note: This method is only available through the gRPC API (not REST).

The top-level message sent to the client by the server is StreamingAnalyzeContentResponse. Multiple response messages can be returned in order. The first one or more messages contain the recognition_result field. Each result represents a more complete transcript of what the user said. The next message contains the reply_text field, and potentially the reply_audio and/or the automated_agent_reply fields.

Note: Always use agent versions for production traffic sent to virtual agents. See Versions and environments (at <https://cloud.google.com/dialogflow/es/docs/agents-versions>).

This method is not supported for the REST transport.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"io"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    	stream, err := c.StreamingAnalyzeContent(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	go func() {
    		reqs := []*dialogflowpb.StreamingAnalyzeContentRequest{
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
    

### func (*ParticipantsClient) SuggestArticles 
    
    
    func (c *ParticipantsClient) SuggestArticles(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestArticlesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestArticlesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestArticlesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestArticlesResponse), [error](https://pkg.go.dev/builtin#error))

SuggestArticles gets suggested articles for a participant based on specific historical messages.

Note that ListSuggestions will only list the auto-generated suggestions, while CompileSuggestion will try to compile suggestion based on the provided conversation context in the real time.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SuggestArticlesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SuggestArticlesRequest.
    	}
    	resp, err := c.SuggestArticles(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) SuggestFaqAnswers 
    
    
    func (c *ParticipantsClient) SuggestFaqAnswers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestFaqAnswersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestFaqAnswersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestFaqAnswersResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestFaqAnswersResponse), [error](https://pkg.go.dev/builtin#error))

SuggestFaqAnswers gets suggested faq answers for a participant based on specific historical messages.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SuggestFaqAnswersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SuggestFaqAnswersRequest.
    	}
    	resp, err := c.SuggestFaqAnswers(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) SuggestKnowledgeAssist 
    
    
    func (c *ParticipantsClient) SuggestKnowledgeAssist(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestKnowledgeAssistRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestKnowledgeAssistResponse), [error](https://pkg.go.dev/builtin#error))

SuggestKnowledgeAssist gets knowledge assist suggestions based on historical messages.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SuggestKnowledgeAssistRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SuggestKnowledgeAssistRequest.
    	}
    	resp, err := c.SuggestKnowledgeAssist(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) SuggestSmartReplies 
    
    
    func (c *ParticipantsClient) SuggestSmartReplies(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestSmartRepliesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestSmartRepliesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SuggestSmartRepliesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SuggestSmartRepliesResponse), [error](https://pkg.go.dev/builtin#error))

SuggestSmartReplies gets smart replies for a participant based on specific historical messages.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.SuggestSmartRepliesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#SuggestSmartRepliesRequest.
    	}
    	resp, err := c.SuggestSmartReplies(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ParticipantsClient) UpdateParticipant 
    
    
    func (c *ParticipantsClient) UpdateParticipant(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateParticipantRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateParticipantRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Participant](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Participant), [error](https://pkg.go.dev/builtin#error))

UpdateParticipant updates the specified participant.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewParticipantsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateParticipantRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateParticipantRequest.
    	}
    	resp, err := c.UpdateParticipant(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## PhoneNumberIterator
    
    
    type PhoneNumberIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.PhoneNumber, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PhoneNumberIterator manages a stream of *dialogflowpb.PhoneNumber.

### func (*PhoneNumberIterator) All 
    
    
    func (it *PhoneNumberIterator) All() iter.Seq2[*dialogflowpb.PhoneNumber, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PhoneNumberIterator) Next 
    
    
    func (it *PhoneNumberIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[PhoneNumber](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_PhoneNumber), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PhoneNumberIterator) PageInfo 
    
    
    func (it *PhoneNumberIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PhoneNumbersCallOptions
    
    
    type PhoneNumbersCallOptions struct {
    	ListPhoneNumbers    []gax.CallOption
    	UpdatePhoneNumber   []gax.CallOption
    	DeletePhoneNumber   []gax.CallOption
    	UndeletePhoneNumber []gax.CallOption
    	GetLocation         []gax.CallOption
    	ListLocations       []gax.CallOption
    	CancelOperation     []gax.CallOption
    	GetOperation        []gax.CallOption
    	ListOperations      []gax.CallOption
    }

PhoneNumbersCallOptions contains the retry settings for each method of PhoneNumbersClient.

## PhoneNumbersClient
    
    
    type PhoneNumbersClient struct {
    
    	// The call options for this service.
    	CallOptions *PhoneNumbersCallOptions
    	// contains filtered or unexported fields
    }

PhoneNumbersClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing PhoneNumbers.

### func NewPhoneNumbersClient 
    
    
    func NewPhoneNumbersClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PhoneNumbersClient, [error](https://pkg.go.dev/builtin#error))

NewPhoneNumbersClient creates a new phone numbers client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing PhoneNumbers.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewPhoneNumbersRESTClient 
    
    
    func NewPhoneNumbersRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PhoneNumbersClient, [error](https://pkg.go.dev/builtin#error))

NewPhoneNumbersRESTClient creates a new phone numbers rest client.

Service for managing PhoneNumbers.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewPhoneNumbersRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_PhoneNumbersClient_NewPhoneNumbersRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*PhoneNumbersClient) CancelOperation 
    
    
    func (c *PhoneNumbersClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PhoneNumbersClient) Close 
    
    
    func (c *PhoneNumbersClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*PhoneNumbersClient) Connection (deprecated)
    
    
    func (c *PhoneNumbersClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*PhoneNumbersClient) DeletePhoneNumber 
    
    
    func (c *PhoneNumbersClient) DeletePhoneNumber(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeletePhoneNumberRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeletePhoneNumberRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[PhoneNumber](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_PhoneNumber), [error](https://pkg.go.dev/builtin#error))

DeletePhoneNumber requests deletion of a PhoneNumber. The PhoneNumber is moved into the DELETE_REQUESTED state immediately, and is deleted approximately 30 days later. This method may only be called on a PhoneNumber in the [ACTIVE][google.cloud.dialogflow.v2beta1.PhoneNumber.LifecycleState.ACTIVE (at <http://google.cloud.dialogflow.v2beta1.PhoneNumber.LifecycleState.ACTIVE>)] state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeletePhoneNumberRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeletePhoneNumberRequest.
    	}
    	resp, err := c.DeletePhoneNumber(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PhoneNumbersClient) GetLocation 
    
    
    func (c *PhoneNumbersClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
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
    

### func (*PhoneNumbersClient) GetOperation 
    
    
    func (c *PhoneNumbersClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PhoneNumbersClient) ListLocations 
    
    
    func (c *PhoneNumbersClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
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
    

### func (*PhoneNumbersClient) ListOperations 
    
    
    func (c *PhoneNumbersClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PhoneNumbersClient) ListPhoneNumbers 
    
    
    func (c *PhoneNumbersClient) ListPhoneNumbers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListPhoneNumbersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListPhoneNumbersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PhoneNumberIterator

ListPhoneNumbers returns the list of all phone numbers in the specified project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListPhoneNumbersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListPhoneNumbersRequest.
    	}
    	it := c.ListPhoneNumbers(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListPhoneNumbersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListPhoneNumbersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListPhoneNumbersRequest.
    	}
    	for resp, err := range c.ListPhoneNumbers(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PhoneNumbersClient) UndeletePhoneNumber 
    
    
    func (c *PhoneNumbersClient) UndeletePhoneNumber(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UndeletePhoneNumberRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UndeletePhoneNumberRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[PhoneNumber](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_PhoneNumber), [error](https://pkg.go.dev/builtin#error))

UndeletePhoneNumber cancels the deletion request for a PhoneNumber. This method may only be called on a PhoneNumber in the DELETE_REQUESTED state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UndeletePhoneNumberRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UndeletePhoneNumberRequest.
    	}
    	resp, err := c.UndeletePhoneNumber(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PhoneNumbersClient) UpdatePhoneNumber 
    
    
    func (c *PhoneNumbersClient) UpdatePhoneNumber(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdatePhoneNumberRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdatePhoneNumberRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[PhoneNumber](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_PhoneNumber), [error](https://pkg.go.dev/builtin#error))

UpdatePhoneNumber updates the specified PhoneNumber.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewPhoneNumbersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdatePhoneNumberRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdatePhoneNumberRequest.
    	}
    	resp, err := c.UpdatePhoneNumber(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ReloadDocumentOperation
    
    
    type ReloadDocumentOperation struct {
    	// contains filtered or unexported fields
    }

ReloadDocumentOperation manages a long-running operation from ReloadDocument.

### func (*ReloadDocumentOperation) Done 
    
    
    func (op *ReloadDocumentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ReloadDocumentOperation) Metadata 
    
    
    func (op *ReloadDocumentOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ReloadDocumentOperation) Name 
    
    
    func (op *ReloadDocumentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ReloadDocumentOperation) Poll 
    
    
    func (op *ReloadDocumentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ReloadDocumentOperation) Wait 
    
    
    func (op *ReloadDocumentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.SessionEntityType, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SessionEntityTypeIterator manages a stream of *dialogflowpb.SessionEntityType.

### func (*SessionEntityTypeIterator) All 
    
    
    func (it *SessionEntityTypeIterator) All() iter.Seq2[*dialogflowpb.SessionEntityType, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SessionEntityTypeIterator) Next 
    
    
    func (it *SessionEntityTypeIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewSessionEntityTypesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_SessionEntityTypesClient_NewSessionEntityTypesRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *SessionEntityTypesClient) CreateSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

CreateSessionEntityType creates a session entity type.

If the specified session entity type already exists, overrides the session entity type.

This method doesn’t work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateSessionEntityTypeRequest.
    	}
    	resp, err := c.CreateSessionEntityType(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionEntityTypesClient) DeleteSessionEntityType 
    
    
    func (c *SessionEntityTypesClient) DeleteSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteSessionEntityType deletes the specified session entity type.

This method doesn’t work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteSessionEntityTypeRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionEntityTypesClient) GetSessionEntityType 
    
    
    func (c *SessionEntityTypesClient) GetSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

GetSessionEntityType retrieves the specified session entity type.

This method doesn’t work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetSessionEntityTypeRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionEntityTypesClient) ListSessionEntityTypes 
    
    
    func (c *SessionEntityTypesClient) ListSessionEntityTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListSessionEntityTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListSessionEntityTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SessionEntityTypeIterator

ListSessionEntityTypes returns the list of all session entity types in the specified session.

This method doesn’t work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListSessionEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListSessionEntityTypesRequest.
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
    		_ = it.Response.(*dialogflowpb.ListSessionEntityTypesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListSessionEntityTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListSessionEntityTypesRequest.
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
    
    
    func (c *SessionEntityTypesClient) UpdateSessionEntityType(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateSessionEntityTypeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SessionEntityType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SessionEntityType), [error](https://pkg.go.dev/builtin#error))

UpdateSessionEntityType updates the specified session entity type.

This method doesn’t work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionEntityTypesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateSessionEntityTypeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateSessionEntityTypeRequest.
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
    	DetectIntent          []gax.CallOption
    	StreamingDetectIntent []gax.CallOption
    	GetLocation           []gax.CallOption
    	ListLocations         []gax.CallOption
    	CancelOperation       []gax.CallOption
    	GetOperation          []gax.CallOption
    	ListOperations        []gax.CallOption
    }

SessionsCallOptions contains the retry settings for each method of SessionsClient.

## SessionsClient
    
    
    type SessionsClient struct {
    
    	// The call options for this service.
    	CallOptions *SessionsCallOptions
    	// contains filtered or unexported fields
    }

SessionsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

A service used for session interactions.

For more information, see the API interactions guide (at <https://cloud.google.com/dialogflow/docs/api-overview>).

### func NewSessionsClient 
    
    
    func NewSessionsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionsClient, [error](https://pkg.go.dev/builtin#error))

NewSessionsClient creates a new sessions client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

A service used for session interactions.

For more information, see the API interactions guide (at <https://cloud.google.com/dialogflow/docs/api-overview>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
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

A service used for session interactions.

For more information, see the API interactions guide (at <https://cloud.google.com/dialogflow/docs/api-overview>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewSessionsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_SessionsClient_NewSessionsRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *SessionsClient) DetectIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DetectIntentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DetectIntentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DetectIntentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DetectIntentResponse), [error](https://pkg.go.dev/builtin#error))

DetectIntent processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause contexts and session entity types to be updated, which in turn might affect results of future queries.

If you might use Agent Assist (at <https://cloud.google.com/dialogflow/docs/#aa>) or other CCAI products now or in the future, consider using AnalyzeContent instead of DetectIntent. AnalyzeContent has additional functionality for Agent Assist and other CCAI products.

Note: Always use agent versions for production traffic. See Versions and environments (at <https://cloud.google.com/dialogflow/es/docs/agents-versions>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DetectIntentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DetectIntentRequest.
    	}
    	resp, err := c.DetectIntent(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewSessionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionsClient) StreamingDetectIntent 
    
    
    func (c *SessionsClient) StreamingDetectIntent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Sessions_StreamingDetectIntentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Sessions_StreamingDetectIntentClient), [error](https://pkg.go.dev/builtin#error))

StreamingDetectIntent processes a natural language query in audio format in a streaming fashion and returns structured, actionable data as a result. This method is only available via the gRPC API (not REST).

If you might use Agent Assist (at <https://cloud.google.com/dialogflow/docs/#aa>) or other CCAI products now or in the future, consider using StreamingAnalyzeContent instead of StreamingDetectIntent. StreamingAnalyzeContent has additional functionality for Agent Assist and other CCAI products.

Note: Always use agent versions for production traffic. See Versions and environments (at <https://cloud.google.com/dialogflow/es/docs/agents-versions>).

This method is not supported for the REST transport.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"io"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSessionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    	stream, err := c.StreamingDetectIntent(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	go func() {
    		reqs := []*dialogflowpb.StreamingDetectIntentRequest{
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
    

## SetSuggestionFeatureConfigOperation
    
    
    type SetSuggestionFeatureConfigOperation struct {
    	// contains filtered or unexported fields
    }

SetSuggestionFeatureConfigOperation manages a long-running operation from SetSuggestionFeatureConfig.

### func (*SetSuggestionFeatureConfigOperation) Done 
    
    
    func (op *SetSuggestionFeatureConfigOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*SetSuggestionFeatureConfigOperation) Metadata 
    
    
    func (op *SetSuggestionFeatureConfigOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SetSuggestionFeatureConfigOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*SetSuggestionFeatureConfigOperation) Name 
    
    
    func (op *SetSuggestionFeatureConfigOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*SetSuggestionFeatureConfigOperation) Poll 
    
    
    func (op *SetSuggestionFeatureConfigOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*SetSuggestionFeatureConfigOperation) Wait 
    
    
    func (op *SetSuggestionFeatureConfigOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ConversationProfile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ConversationProfile), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SipTrunkIterator
    
    
    type SipTrunkIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.SipTrunk, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SipTrunkIterator manages a stream of *dialogflowpb.SipTrunk.

### func (*SipTrunkIterator) All 
    
    
    func (it *SipTrunkIterator) All() iter.Seq2[*dialogflowpb.SipTrunk, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SipTrunkIterator) Next 
    
    
    func (it *SipTrunkIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SipTrunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SipTrunk), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SipTrunkIterator) PageInfo 
    
    
    func (it *SipTrunkIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SipTrunksCallOptions
    
    
    type SipTrunksCallOptions struct {
    	CreateSipTrunk  []gax.CallOption
    	DeleteSipTrunk  []gax.CallOption
    	ListSipTrunks   []gax.CallOption
    	GetSipTrunk     []gax.CallOption
    	UpdateSipTrunk  []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

SipTrunksCallOptions contains the retry settings for each method of SipTrunksClient.

## SipTrunksClient
    
    
    type SipTrunksClient struct {
    
    	// The call options for this service.
    	CallOptions *SipTrunksCallOptions
    	// contains filtered or unexported fields
    }

SipTrunksClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing SipTrunks.

### func NewSipTrunksClient 
    
    
    func NewSipTrunksClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SipTrunksClient, [error](https://pkg.go.dev/builtin#error))

NewSipTrunksClient creates a new sip trunks client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing SipTrunks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSipTrunksRESTClient 
    
    
    func NewSipTrunksRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SipTrunksClient, [error](https://pkg.go.dev/builtin#error))

NewSipTrunksRESTClient creates a new sip trunks rest client.

Service for managing SipTrunks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewSipTrunksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_SipTrunksClient_NewSipTrunksRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SipTrunksClient) CancelOperation 
    
    
    func (c *SipTrunksClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SipTrunksClient) Close 
    
    
    func (c *SipTrunksClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SipTrunksClient) Connection (deprecated)
    
    
    func (c *SipTrunksClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SipTrunksClient) CreateSipTrunk 
    
    
    func (c *SipTrunksClient) CreateSipTrunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateSipTrunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateSipTrunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SipTrunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SipTrunk), [error](https://pkg.go.dev/builtin#error))

CreateSipTrunk creates a SipTrunk for a specified location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateSipTrunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateSipTrunkRequest.
    	}
    	resp, err := c.CreateSipTrunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SipTrunksClient) DeleteSipTrunk 
    
    
    func (c *SipTrunksClient) DeleteSipTrunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteSipTrunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteSipTrunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteSipTrunk deletes a specified SipTrunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteSipTrunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteSipTrunkRequest.
    	}
    	err = c.DeleteSipTrunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SipTrunksClient) GetLocation 
    
    
    func (c *SipTrunksClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
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
    

### func (*SipTrunksClient) GetOperation 
    
    
    func (c *SipTrunksClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SipTrunksClient) GetSipTrunk 
    
    
    func (c *SipTrunksClient) GetSipTrunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetSipTrunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetSipTrunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SipTrunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SipTrunk), [error](https://pkg.go.dev/builtin#error))

GetSipTrunk retrieves the specified SipTrunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetSipTrunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetSipTrunkRequest.
    	}
    	resp, err := c.GetSipTrunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SipTrunksClient) ListLocations 
    
    
    func (c *SipTrunksClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewSipTrunksClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
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
    

### func (*SipTrunksClient) ListOperations 
    
    
    func (c *SipTrunksClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SipTrunksClient) ListSipTrunks 
    
    
    func (c *SipTrunksClient) ListSipTrunks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListSipTrunksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListSipTrunksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SipTrunkIterator

ListSipTrunks returns a list of SipTrunks in the specified location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListSipTrunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListSipTrunksRequest.
    	}
    	it := c.ListSipTrunks(ctx, req)
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
    		_ = it.Response.(*dialogflowpb.ListSipTrunksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListSipTrunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListSipTrunksRequest.
    	}
    	for resp, err := range c.ListSipTrunks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SipTrunksClient) UpdateSipTrunk 
    
    
    func (c *SipTrunksClient) UpdateSipTrunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateSipTrunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateSipTrunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[SipTrunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_SipTrunk), [error](https://pkg.go.dev/builtin#error))

UpdateSipTrunk updates the specified SipTrunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewSipTrunksClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateSipTrunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateSipTrunkRequest.
    	}
    	resp, err := c.UpdateSipTrunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## SuggestionIterator
    
    
    type SuggestionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Suggestion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SuggestionIterator manages a stream of *dialogflowpb.Suggestion.

### func (*SuggestionIterator) All 
    
    
    func (it *SuggestionIterator) All() iter.Seq2[*dialogflowpb.Suggestion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SuggestionIterator) Next 
    
    
    func (it *SuggestionIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Suggestion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Suggestion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SuggestionIterator) PageInfo 
    
    
    func (it *SuggestionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Tool, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ToolIterator manages a stream of *dialogflowpb.Tool.

### func (*ToolIterator) All 
    
    
    func (it *ToolIterator) All() iter.Seq2[*dialogflowpb.Tool, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ToolIterator) Next 
    
    
    func (it *ToolIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Tool), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ToolIterator) PageInfo 
    
    
    func (it *ToolIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ToolsCallOptions
    
    
    type ToolsCallOptions struct {
    	CreateTool      []gax.CallOption
    	GetTool         []gax.CallOption
    	ListTools       []gax.CallOption
    	DeleteTool      []gax.CallOption
    	UpdateTool      []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

ToolsCallOptions contains the retry settings for each method of ToolsClient.

## ToolsClient
    
    
    type ToolsClient struct {
    
    	// The call options for this service.
    	CallOptions *ToolsCallOptions
    	// contains filtered or unexported fields
    }

ToolsClient is a client for interacting with Dialogflow API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

### func NewToolsClient 
    
    
    func NewToolsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ToolsClient, [error](https://pkg.go.dev/builtin#error))

NewToolsClient creates a new tools client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
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

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewToolsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_ToolsClient_NewToolsRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
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
    
    
    func (c *ToolsClient) CreateTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Tool), [error](https://pkg.go.dev/builtin#error))

CreateTool creates a tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateToolRequest.
    	}
    	resp, err := c.CreateTool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) DeleteTool 
    
    
    func (c *ToolsClient) DeleteTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteTool deletes a tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteToolRequest.
    	}
    	err = c.DeleteTool(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ToolsClient) GetTool 
    
    
    func (c *ToolsClient) GetTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Tool), [error](https://pkg.go.dev/builtin#error))

GetTool retrieves a tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetToolRequest.
    	}
    	resp, err := c.GetTool(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewToolsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ToolsClient) ListTools 
    
    
    func (c *ToolsClient) ListTools(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListToolsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListToolsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ToolIterator

ListTools lists tools.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListToolsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListToolsRequest.
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
    		_ = it.Response.(*dialogflowpb.ListToolsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListToolsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListToolsRequest.
    	}
    	for resp, err := range c.ListTools(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ToolsClient) UpdateTool 
    
    
    func (c *ToolsClient) UpdateTool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateToolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateToolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Tool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Tool), [error](https://pkg.go.dev/builtin#error))

UpdateTool updates a tool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewToolsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateToolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateToolRequest.
    	}
    	resp, err := c.UpdateTool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## TrainAgentOperation
    
    
    type TrainAgentOperation struct {
    	// contains filtered or unexported fields
    }

TrainAgentOperation manages a long-running operation from TrainAgent.

### func (*TrainAgentOperation) Done 
    
    
    func (op *TrainAgentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*TrainAgentOperation) Metadata 
    
    
    func (op *TrainAgentOperation) Metadata() (*[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*TrainAgentOperation) Name 
    
    
    func (op *TrainAgentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*TrainAgentOperation) Poll 
    
    
    func (op *TrainAgentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*TrainAgentOperation) Wait 
    
    
    func (op *TrainAgentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateDocumentOperation
    
    
    type UpdateDocumentOperation struct {
    	// contains filtered or unexported fields
    }

UpdateDocumentOperation manages a long-running operation from UpdateDocument.

### func (*UpdateDocumentOperation) Done 
    
    
    func (op *UpdateDocumentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateDocumentOperation) Metadata 
    
    
    func (op *UpdateDocumentOperation) Metadata() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[KnowledgeOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_KnowledgeOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateDocumentOperation) Name 
    
    
    func (op *UpdateDocumentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateDocumentOperation) Poll 
    
    
    func (op *UpdateDocumentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateDocumentOperation) Wait 
    
    
    func (op *UpdateDocumentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Document), [error](https://pkg.go.dev/builtin#error))

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dialogflowpb.Version, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

VersionIterator manages a stream of *dialogflowpb.Version.

### func (*VersionIterator) All 
    
    
    func (it *VersionIterator) All() iter.Seq2[*dialogflowpb.Version, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*VersionIterator) Next 
    
    
    func (it *VersionIterator) Next() (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Version), [error](https://pkg.go.dev/builtin#error))

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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.[NewVersionsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1.html#cloud_google_com_go_dialogflow_apiv2beta1_VersionsClient_NewVersionsRESTClient)(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*VersionsClient) Close 
    
    
    func (c *VersionsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*VersionsClient) Connection (deprecated)
    
    
    func (c *VersionsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*VersionsClient) CreateVersion 
    
    
    func (c *VersionsClient) CreateVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[CreateVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_CreateVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Version), [error](https://pkg.go.dev/builtin#error))

CreateVersion creates an agent version.

The new version points to the agent instance in the “default” environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.CreateVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#CreateVersionRequest.
    	}
    	resp, err := c.CreateVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) DeleteVersion 
    
    
    func (c *VersionsClient) DeleteVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[DeleteVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_DeleteVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteVersion delete the specified agent version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.DeleteVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#DeleteVersionRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*VersionsClient) GetVersion 
    
    
    func (c *VersionsClient) GetVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[GetVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_GetVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Version), [error](https://pkg.go.dev/builtin#error))

GetVersion retrieves the specified agent version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.GetVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#GetVersionRequest.
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
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
    	c, err := dialogflow.NewVersionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
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
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*VersionsClient) ListVersions 
    
    
    func (c *VersionsClient) ListVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[ListVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_ListVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *VersionIterator

ListVersions returns the list of all versions of the specified agent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListVersionsRequest.
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
    		_ = it.Response.(*dialogflowpb.ListVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.ListVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#ListVersionsRequest.
    	}
    	for resp, err := range c.ListVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*VersionsClient) UpdateVersion 
    
    
    func (c *VersionsClient) UpdateVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[UpdateVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_UpdateVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dialogflowpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb).[Version](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/apiv2beta1/dialogflowpb#cloud_google_com_go_dialogflow_apiv2beta1_dialogflowpb_Version), [error](https://pkg.go.dev/builtin#error))

UpdateVersion updates the specified agent version.

Note that this method does not allow you to update the state of the agent the given version points to. It allows you to update only mutable properties of the version resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dialogflow "cloud.google.com/go/dialogflow/apiv2beta1"
    	dialogflowpb "cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dialogflow.NewVersionsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dialogflowpb.UpdateVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb#UpdateVersionRequest.
    	}
    	resp, err := c.UpdateVersion(ctx, req)
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
