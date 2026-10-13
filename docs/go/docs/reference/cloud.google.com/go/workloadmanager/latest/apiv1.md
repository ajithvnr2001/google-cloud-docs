---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/
title: Workload Manager API v1 - Package cloud.google.com/go/workloadmanager/apiv1 (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:27.243062+00:00
---

# Workload Manager API v1 - Package cloud.google.com/go/workloadmanager/apiv1 (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Workload Manager API v1 - Package cloud.google.com/go/workloadmanager/apiv1 (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1). 

Package workloadmanager is an auto-generated package for the Workload Manager API. 

Workload Manager is a service that provides tooling for enterprise workloads to automate the deployment and validation of your workloads against best practices and recommendations. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/workloadmanager/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := workloadmanager.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &workloadmanagerpb.CreateEvaluationRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#CreateEvaluationRequest.
    }
    op, err := c.CreateEvaluation(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    
    resp, err := op.Wait(ctx)
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
    	ListEvaluations      []gax.CallOption
    	GetEvaluation        []gax.CallOption
    	CreateEvaluation     []gax.CallOption
    	UpdateEvaluation     []gax.CallOption
    	DeleteEvaluation     []gax.CallOption
    	ListExecutions       []gax.CallOption
    	GetExecution         []gax.CallOption
    	RunEvaluation        []gax.CallOption
    	DeleteExecution      []gax.CallOption
    	ListExecutionResults []gax.CallOption
    	ListRules            []gax.CallOption
    	ListScannedResources []gax.CallOption
    	GetLocation          []gax.CallOption
    	ListLocations        []gax.CallOption
    	CancelOperation      []gax.CallOption
    	DeleteOperation      []gax.CallOption
    	GetOperation         []gax.CallOption
    	ListOperations       []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Workload Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The Workload Manager provides various tools to deploy, validate and observe your workloads running on Google Cloud.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new workload manager client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The Workload Manager provides various tools to deploy, validate and observe your workloads running on Google Cloud.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new workload manager rest client.

The Workload Manager provides various tools to deploy, validate and observe your workloads running on Google Cloud.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) CancelOperation 
    
    
    func (c *Client) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) CreateEvaluation 
    
    
    func (c *Client) CreateEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[CreateEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_CreateEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateEvaluationOperation, [error](https://pkg.go.dev/builtin#error))

CreateEvaluation creates a new Evaluation in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.CreateEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#CreateEvaluationRequest.
    	}
    	op, err := c.CreateEvaluation(ctx, req)
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
    

### func (*Client) CreateEvaluationOperation 
    
    
    func (c *Client) CreateEvaluationOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateEvaluationOperation

CreateEvaluationOperation returns a new CreateEvaluationOperation from a given name. The name must be that of a previously created CreateEvaluationOperation, possibly from a different process.

### func (*Client) DeleteEvaluation 
    
    
    func (c *Client) DeleteEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[DeleteEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_DeleteEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteEvaluationOperation, [error](https://pkg.go.dev/builtin#error))

DeleteEvaluation deletes a single Evaluation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.DeleteEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#DeleteEvaluationRequest.
    	}
    	op, err := c.DeleteEvaluation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteEvaluationOperation 
    
    
    func (c *Client) DeleteEvaluationOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteEvaluationOperation

DeleteEvaluationOperation returns a new DeleteEvaluationOperation from a given name. The name must be that of a previously created DeleteEvaluationOperation, possibly from a different process.

### func (*Client) DeleteExecution 
    
    
    func (c *Client) DeleteExecution(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[DeleteExecutionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_DeleteExecutionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteExecutionOperation, [error](https://pkg.go.dev/builtin#error))

DeleteExecution deletes a single Execution.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.DeleteExecutionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#DeleteExecutionRequest.
    	}
    	op, err := c.DeleteExecution(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteExecutionOperation 
    
    
    func (c *Client) DeleteExecutionOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteExecutionOperation

DeleteExecutionOperation returns a new DeleteExecutionOperation from a given name. The name must be that of a previously created DeleteExecutionOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) GetEvaluation 
    
    
    func (c *Client) GetEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[GetEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_GetEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Evaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Evaluation), [error](https://pkg.go.dev/builtin#error))

GetEvaluation gets details of a single Evaluation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.GetEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#GetEvaluationRequest.
    	}
    	resp, err := c.GetEvaluation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetExecution 
    
    
    func (c *Client) GetExecution(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[GetExecutionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_GetExecutionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Execution](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Execution), [error](https://pkg.go.dev/builtin#error))

GetExecution gets details of a single Execution.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.GetExecutionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#GetExecutionRequest.
    	}
    	resp, err := c.GetExecution(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetLocation 
    
    
    func (c *Client) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.[GetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_GetLocation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetOperation 
    
    
    func (c *Client) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
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
    

### func (*Client) ListEvaluations 
    
    
    func (c *Client) ListEvaluations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ListEvaluationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ListEvaluationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EvaluationIterator

ListEvaluations lists Evaluations in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListEvaluationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListEvaluationsRequest.
    	}
    	it := c.ListEvaluations(ctx, req)
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
    		_ = it.Response.(*workloadmanagerpb.ListEvaluationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListEvaluationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListEvaluationsRequest.
    	}
    	for resp, err := range c.ListEvaluations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListExecutionResults 
    
    
    func (c *Client) ListExecutionResults(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ListExecutionResultsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ListExecutionResultsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ExecutionResultIterator

ListExecutionResults lists the result of a single evaluation.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListExecutionResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListExecutionResultsRequest.
    	}
    	it := c.ListExecutionResults(ctx, req)
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
    		_ = it.Response.(*workloadmanagerpb.ListExecutionResultsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListExecutionResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListExecutionResultsRequest.
    	}
    	for resp, err := range c.ListExecutionResults(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListExecutions 
    
    
    func (c *Client) ListExecutions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ListExecutionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ListExecutionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ExecutionIterator

ListExecutions lists Executions in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListExecutionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListExecutionsRequest.
    	}
    	it := c.ListExecutions(ctx, req)
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
    		_ = it.Response.(*workloadmanagerpb.ListExecutionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListExecutionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListExecutionsRequest.
    	}
    	for resp, err := range c.ListExecutions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListLocations 
    
    
    func (c *Client) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service. This method can be called in two ways:
    
    
    List all public locations: Use the path GET /v1/locations.
    
    List project-visible locations: Use the path
    GET /v1/projects/{project_id}/locations. This may include public
    locations as well as private or other locations specifically visible
    to the project.
    

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
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
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_ListLocations)(ctx, req)
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
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOperations 
    
    
    func (c *Client) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
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
    

### func (*Client) ListRules 
    
    
    func (c *Client) ListRules(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ListRulesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ListRulesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ListRulesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ListRulesResponse), [error](https://pkg.go.dev/builtin#error))

ListRules lists rules in a given project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListRulesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListRulesRequest.
    	}
    	resp, err := c.ListRules(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListScannedResources 
    
    
    func (c *Client) ListScannedResources(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ListScannedResourcesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ListScannedResourcesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ScannedResourceIterator

ListScannedResources list all scanned resources for a single Execution.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListScannedResourcesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListScannedResourcesRequest.
    	}
    	it := c.ListScannedResources(ctx, req)
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
    		_ = it.Response.(*workloadmanagerpb.ListScannedResourcesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.ListScannedResourcesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#ListScannedResourcesRequest.
    	}
    	for resp, err := range c.ListScannedResources(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) RunEvaluation 
    
    
    func (c *Client) RunEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[RunEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_RunEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RunEvaluationOperation, [error](https://pkg.go.dev/builtin#error))

RunEvaluation creates a new Execution in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.RunEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#RunEvaluationRequest.
    	}
    	op, err := c.RunEvaluation(ctx, req)
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
    

### func (*Client) RunEvaluationOperation 
    
    
    func (c *Client) RunEvaluationOperation(name [string](https://pkg.go.dev/builtin#string)) *RunEvaluationOperation

RunEvaluationOperation returns a new RunEvaluationOperation from a given name. The name must be that of a previously created RunEvaluationOperation, possibly from a different process.

### func (*Client) UpdateEvaluation 
    
    
    func (c *Client) UpdateEvaluation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[UpdateEvaluationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_UpdateEvaluationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateEvaluationOperation, [error](https://pkg.go.dev/builtin#error))

UpdateEvaluation updates the parameters of a single Evaluation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	workloadmanager "cloud.google.com/go/workloadmanager/apiv1"
    
    	workloadmanagerpb "cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workloadmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1.html#cloud_google_com_go_workloadmanager_apiv1_Client_Close)()
    
    	req := &workloadmanagerpb.UpdateEvaluationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workloadmanager/apiv1/workloadmanagerpb#UpdateEvaluationRequest.
    	}
    	op, err := c.UpdateEvaluation(ctx, req)
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
    

### func (*Client) UpdateEvaluationOperation 
    
    
    func (c *Client) UpdateEvaluationOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateEvaluationOperation

UpdateEvaluationOperation returns a new UpdateEvaluationOperation from a given name. The name must be that of a previously created UpdateEvaluationOperation, possibly from a different process.

## CreateEvaluationOperation
    
    
    type CreateEvaluationOperation struct {
    	// contains filtered or unexported fields
    }

CreateEvaluationOperation manages a long-running operation from CreateEvaluation.

### func (*CreateEvaluationOperation) Done 
    
    
    func (op *CreateEvaluationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateEvaluationOperation) Metadata 
    
    
    func (op *CreateEvaluationOperation) Metadata() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateEvaluationOperation) Name 
    
    
    func (op *CreateEvaluationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateEvaluationOperation) Poll 
    
    
    func (op *CreateEvaluationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Evaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Evaluation), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateEvaluationOperation) Wait 
    
    
    func (op *CreateEvaluationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Evaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Evaluation), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteEvaluationOperation
    
    
    type DeleteEvaluationOperation struct {
    	// contains filtered or unexported fields
    }

DeleteEvaluationOperation manages a long-running operation from DeleteEvaluation.

### func (*DeleteEvaluationOperation) Done 
    
    
    func (op *DeleteEvaluationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteEvaluationOperation) Metadata 
    
    
    func (op *DeleteEvaluationOperation) Metadata() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteEvaluationOperation) Name 
    
    
    func (op *DeleteEvaluationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteEvaluationOperation) Poll 
    
    
    func (op *DeleteEvaluationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteEvaluationOperation) Wait 
    
    
    func (op *DeleteEvaluationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteExecutionOperation
    
    
    type DeleteExecutionOperation struct {
    	// contains filtered or unexported fields
    }

DeleteExecutionOperation manages a long-running operation from DeleteExecution.

### func (*DeleteExecutionOperation) Done 
    
    
    func (op *DeleteExecutionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteExecutionOperation) Metadata 
    
    
    func (op *DeleteExecutionOperation) Metadata() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteExecutionOperation) Name 
    
    
    func (op *DeleteExecutionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteExecutionOperation) Poll 
    
    
    func (op *DeleteExecutionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteExecutionOperation) Wait 
    
    
    func (op *DeleteExecutionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EvaluationIterator
    
    
    type EvaluationIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*workloadmanagerpb.Evaluation, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EvaluationIterator manages a stream of *workloadmanagerpb.Evaluation.

### func (*EvaluationIterator) All 
    
    
    func (it *EvaluationIterator) All() iter.Seq2[*workloadmanagerpb.Evaluation, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EvaluationIterator) Next 
    
    
    func (it *EvaluationIterator) Next() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Evaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Evaluation), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EvaluationIterator) PageInfo 
    
    
    func (it *EvaluationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ExecutionIterator
    
    
    type ExecutionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*workloadmanagerpb.Execution, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ExecutionIterator manages a stream of *workloadmanagerpb.Execution.

### func (*ExecutionIterator) All 
    
    
    func (it *ExecutionIterator) All() iter.Seq2[*workloadmanagerpb.Execution, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ExecutionIterator) Next 
    
    
    func (it *ExecutionIterator) Next() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Execution](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Execution), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ExecutionIterator) PageInfo 
    
    
    func (it *ExecutionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ExecutionResultIterator
    
    
    type ExecutionResultIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*workloadmanagerpb.ExecutionResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ExecutionResultIterator manages a stream of *workloadmanagerpb.ExecutionResult.

### func (*ExecutionResultIterator) All 
    
    
    func (it *ExecutionResultIterator) All() iter.Seq2[*workloadmanagerpb.ExecutionResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ExecutionResultIterator) Next 
    
    
    func (it *ExecutionResultIterator) Next() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ExecutionResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ExecutionResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ExecutionResultIterator) PageInfo 
    
    
    func (it *ExecutionResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

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

## RunEvaluationOperation
    
    
    type RunEvaluationOperation struct {
    	// contains filtered or unexported fields
    }

RunEvaluationOperation manages a long-running operation from RunEvaluation.

### func (*RunEvaluationOperation) Done 
    
    
    func (op *RunEvaluationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RunEvaluationOperation) Metadata 
    
    
    func (op *RunEvaluationOperation) Metadata() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RunEvaluationOperation) Name 
    
    
    func (op *RunEvaluationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RunEvaluationOperation) Poll 
    
    
    func (op *RunEvaluationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Execution](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Execution), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RunEvaluationOperation) Wait 
    
    
    func (op *RunEvaluationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Execution](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Execution), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ScannedResourceIterator
    
    
    type ScannedResourceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*workloadmanagerpb.ScannedResource, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ScannedResourceIterator manages a stream of *workloadmanagerpb.ScannedResource.

### func (*ScannedResourceIterator) All 
    
    
    func (it *ScannedResourceIterator) All() iter.Seq2[*workloadmanagerpb.ScannedResource, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ScannedResourceIterator) Next 
    
    
    func (it *ScannedResourceIterator) Next() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[ScannedResource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_ScannedResource), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ScannedResourceIterator) PageInfo 
    
    
    func (it *ScannedResourceIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## UpdateEvaluationOperation
    
    
    type UpdateEvaluationOperation struct {
    	// contains filtered or unexported fields
    }

UpdateEvaluationOperation manages a long-running operation from UpdateEvaluation.

### func (*UpdateEvaluationOperation) Done 
    
    
    func (op *UpdateEvaluationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateEvaluationOperation) Metadata 
    
    
    func (op *UpdateEvaluationOperation) Metadata() (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateEvaluationOperation) Name 
    
    
    func (op *UpdateEvaluationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateEvaluationOperation) Poll 
    
    
    func (op *UpdateEvaluationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Evaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Evaluation), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateEvaluationOperation) Wait 
    
    
    func (op *UpdateEvaluationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[workloadmanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb).[Evaluation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workloadmanager/latest/apiv1/workloadmanagerpb#cloud_google_com_go_workloadmanager_apiv1_workloadmanagerpb_Evaluation), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
