---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/
title: Storage Transfer API v1 - Package cloud.google.com/go/storagetransfer/apiv1 (v1.20.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:45.972519+00:00
---

# Storage Transfer API v1 - Package cloud.google.com/go/storagetransfer/apiv1 (v1.20.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Storage Transfer API v1 - Package cloud.google.com/go/storagetransfer/apiv1 (v1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.1  1.12.4  1.11.2  1.10.11  1.9.1  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1). 

Package storagetransfer is an auto-generated package for the Storage Transfer API. 

Transfers data from external data sources to a Google Cloud Storage bucket or between Google Cloud Storage buckets. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/storagetransfer/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := storagetransfer.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &storagetransferpb.CreateAgentPoolRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#CreateAgentPoolRequest.
    }
    resp, err := c.CreateAgentPool(ctx, req)
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

## AgentPoolIterator
    
    
    type AgentPoolIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*storagetransferpb.AgentPool, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AgentPoolIterator manages a stream of *storagetransferpb.AgentPool.

### func (*AgentPoolIterator) All 
    
    
    func (it *AgentPoolIterator) All() iter.Seq2[*storagetransferpb.AgentPool, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AgentPoolIterator) Next 
    
    
    func (it *AgentPoolIterator) Next() (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[AgentPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_AgentPool), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AgentPoolIterator) PageInfo 
    
    
    func (it *AgentPoolIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CallOptions
    
    
    type CallOptions struct {
    	GetGoogleServiceAccount []gax.CallOption
    	CreateTransferJob       []gax.CallOption
    	UpdateTransferJob       []gax.CallOption
    	GetTransferJob          []gax.CallOption
    	ListTransferJobs        []gax.CallOption
    	PauseTransferOperation  []gax.CallOption
    	ResumeTransferOperation []gax.CallOption
    	RunTransferJob          []gax.CallOption
    	DeleteTransferJob       []gax.CallOption
    	CreateAgentPool         []gax.CallOption
    	UpdateAgentPool         []gax.CallOption
    	GetAgentPool            []gax.CallOption
    	ListAgentPools          []gax.CallOption
    	DeleteAgentPool         []gax.CallOption
    	CancelOperation         []gax.CallOption
    	GetOperation            []gax.CallOption
    	ListOperations          []gax.CallOption
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

Client is a client for interacting with Storage Transfer API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Storage Transfer Service and its protos. Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new storage transfer service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Storage Transfer Service and its protos. Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new storage transfer service rest client.

Storage Transfer Service and its protos. Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) CancelOperation 
    
    
    func (c *Client) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation cancels a transfer. Use the transferOperations.get method to check if the cancellation succeeded or if the operation completed despite the cancel request.

When you cancel an operation, the currently running transfer is interrupted. For recurring transfer jobs, the next instance of the transfer job will still run. For example, if your job is configured to run every day at 1pm and you cancel Monday’s operation at 1:05pm, Monday’s transfer will stop. However, a transfer job will still be attempted on Tuesday.

This applies only to currently running operations. If an operation is not currently running, cancel does nothing.

When you cancel a job, the next job computes a delta of files and may repair any inconsistent state. For instance, if you run a job every day, and today’s job found 10 new files and transferred five files before you canceled the job, tomorrow’s transfer operation will compute a new delta with the five files that were not copied today plus any new files discovered tomorrow.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
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

### func (*Client) CreateAgentPool 
    
    
    func (c *Client) CreateAgentPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[CreateAgentPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_CreateAgentPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[AgentPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_AgentPool), [error](https://pkg.go.dev/builtin#error))

CreateAgentPool creates an agent pool resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.CreateAgentPoolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#CreateAgentPoolRequest.
    	}
    	resp, err := c.CreateAgentPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateTransferJob 
    
    
    func (c *Client) CreateTransferJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[CreateTransferJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_CreateTransferJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[TransferJob](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob), [error](https://pkg.go.dev/builtin#error))

CreateTransferJob creates a transfer job that runs periodically.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.CreateTransferJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#CreateTransferJobRequest.
    	}
    	resp, err := c.CreateTransferJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) DeleteAgentPool 
    
    
    func (c *Client) DeleteAgentPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[DeleteAgentPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_DeleteAgentPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAgentPool deletes an agent pool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.DeleteAgentPoolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#DeleteAgentPoolRequest.
    	}
    	err = c.DeleteAgentPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteTransferJob 
    
    
    func (c *Client) DeleteTransferJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[DeleteTransferJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_DeleteTransferJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteTransferJob deletes a transfer job. Deleting a transfer job sets its status to DELETED.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.DeleteTransferJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#DeleteTransferJobRequest.
    	}
    	err = c.DeleteTransferJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) GetAgentPool 
    
    
    func (c *Client) GetAgentPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[GetAgentPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_GetAgentPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[AgentPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_AgentPool), [error](https://pkg.go.dev/builtin#error))

GetAgentPool gets an agent pool.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.GetAgentPoolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#GetAgentPoolRequest.
    	}
    	resp, err := c.GetAgentPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGoogleServiceAccount 
    
    
    func (c *Client) GetGoogleServiceAccount(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[GetGoogleServiceAccountRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_GetGoogleServiceAccountRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[GoogleServiceAccount](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_GoogleServiceAccount), [error](https://pkg.go.dev/builtin#error))

GetGoogleServiceAccount returns the Google service account that is used by Storage Transfer Service to access buckets in the project where transfers run or in other projects. Each Google service account is associated with one Google Cloud project. Users should add this service account to the Google Cloud Storage bucket ACLs to grant access to Storage Transfer Service. This service account is created and owned by Storage Transfer Service and can only be used by Storage Transfer Service.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.GetGoogleServiceAccountRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#GetGoogleServiceAccountRequest.
    	}
    	resp, err := c.GetGoogleServiceAccount(ctx, req)
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
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
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
    

### func (*Client) GetTransferJob 
    
    
    func (c *Client) GetTransferJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[GetTransferJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_GetTransferJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[TransferJob](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob), [error](https://pkg.go.dev/builtin#error))

GetTransferJob gets a transfer job.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.GetTransferJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#GetTransferJobRequest.
    	}
    	resp, err := c.GetTransferJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListAgentPools 
    
    
    func (c *Client) ListAgentPools(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[ListAgentPoolsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_ListAgentPoolsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AgentPoolIterator

ListAgentPools lists agent pools.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.ListAgentPoolsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#ListAgentPoolsRequest.
    	}
    	it := c.ListAgentPools(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Done) {
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
    		_ = it.Response.(*storagetransferpb.ListAgentPoolsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.ListAgentPoolsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#ListAgentPoolsRequest.
    	}
    	for resp, err := range c.ListAgentPools(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOperations 
    
    
    func (c *Client) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations lists transfer operations. Operations are ordered by their creation time in reverse chronological order.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.ListOperations(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Done) {
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
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
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
    

### func (*Client) ListTransferJobs 
    
    
    func (c *Client) ListTransferJobs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[ListTransferJobsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_ListTransferJobsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TransferJobIterator

ListTransferJobs lists transfer jobs.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.ListTransferJobsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#ListTransferJobsRequest.
    	}
    	it := c.ListTransferJobs(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Done) {
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
    		_ = it.Response.(*storagetransferpb.ListTransferJobsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.ListTransferJobsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#ListTransferJobsRequest.
    	}
    	for resp, err := range c.ListTransferJobs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) PauseTransferOperation 
    
    
    func (c *Client) PauseTransferOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[PauseTransferOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_PauseTransferOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

PauseTransferOperation pauses a transfer operation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.PauseTransferOperationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#PauseTransferOperationRequest.
    	}
    	err = c.PauseTransferOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) ResumeTransferOperation 
    
    
    func (c *Client) ResumeTransferOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[ResumeTransferOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_ResumeTransferOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

ResumeTransferOperation resumes a transfer operation that is paused.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.ResumeTransferOperationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#ResumeTransferOperationRequest.
    	}
    	err = c.ResumeTransferOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) RunTransferJob 
    
    
    func (c *Client) RunTransferJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[RunTransferJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_RunTransferJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RunTransferJobOperation, [error](https://pkg.go.dev/builtin#error))

RunTransferJob starts a new operation for the specified transfer job. A TransferJob has a maximum of one active TransferOperation. If this method is called while a TransferOperation is active, an error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.RunTransferJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#RunTransferJobRequest.
    	}
    	op, err := c.RunTransferJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_RunTransferJobOperation_Wait)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) RunTransferJobOperation 
    
    
    func (c *Client) RunTransferJobOperation(name [string](https://pkg.go.dev/builtin#string)) *RunTransferJobOperation

RunTransferJobOperation returns a new RunTransferJobOperation from a given name. The name must be that of a previously created RunTransferJobOperation, possibly from a different process.

### func (*Client) UpdateAgentPool 
    
    
    func (c *Client) UpdateAgentPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[UpdateAgentPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_UpdateAgentPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[AgentPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_AgentPool), [error](https://pkg.go.dev/builtin#error))

UpdateAgentPool updates an existing agent pool resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.UpdateAgentPoolRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#UpdateAgentPoolRequest.
    	}
    	resp, err := c.UpdateAgentPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateTransferJob 
    
    
    func (c *Client) UpdateTransferJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[UpdateTransferJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_UpdateTransferJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[TransferJob](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob), [error](https://pkg.go.dev/builtin#error))

UpdateTransferJob updates a transfer job. Updating a job’s transfer spec does not affect transfer operations that are running already.

Note: The job’s status field can be modified using this RPC (for example, to set a job’s status to DELETED, DISABLED, or ENABLED).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	storagetransfer "cloud.google.com/go/storagetransfer/apiv1"
    
    	storagetransferpb "cloud.google.com/go/storagetransfer/apiv1/storagetransferpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := storagetransfer.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1.html#cloud_google_com_go_storagetransfer_apiv1_Client_Close)()
    
    	req := &storagetransferpb.UpdateTransferJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/storagetransfer/apiv1/storagetransferpb#UpdateTransferJobRequest.
    	}
    	resp, err := c.UpdateTransferJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

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

## RunTransferJobOperation
    
    
    type RunTransferJobOperation struct {
    	// contains filtered or unexported fields
    }

RunTransferJobOperation manages a long-running operation from RunTransferJob.

### func (*RunTransferJobOperation) Done 
    
    
    func (op *RunTransferJobOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RunTransferJobOperation) Metadata 
    
    
    func (op *RunTransferJobOperation) Metadata() (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[TransferOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferOperation), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RunTransferJobOperation) Name 
    
    
    func (op *RunTransferJobOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RunTransferJobOperation) Poll 
    
    
    func (op *RunTransferJobOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RunTransferJobOperation) Wait 
    
    
    func (op *RunTransferJobOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## TransferJobIterator
    
    
    type TransferJobIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*storagetransferpb.TransferJob, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TransferJobIterator manages a stream of *storagetransferpb.TransferJob.

### func (*TransferJobIterator) All 
    
    
    func (it *TransferJobIterator) All() iter.Seq2[*storagetransferpb.TransferJob, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TransferJobIterator) Next 
    
    
    func (it *TransferJobIterator) Next() (*[storagetransferpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb).[TransferJob](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storagetransfer/latest/apiv1/storagetransferpb#cloud_google_com_go_storagetransfer_apiv1_storagetransferpb_TransferJob), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TransferJobIterator) PageInfo 
    
    
    func (it *TransferJobIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
