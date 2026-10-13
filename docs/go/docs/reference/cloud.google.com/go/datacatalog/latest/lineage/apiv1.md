---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/
title: Data Lineage API v1 - Package cloud.google.com/go/datacatalog/lineage/apiv1 (v1.34.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:47.773480+00:00
---

# Data Lineage API v1 - Package cloud.google.com/go/datacatalog/lineage/apiv1 (v1.34.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Data Lineage API v1 - Package cloud.google.com/go/datacatalog/lineage/apiv1 (v1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.1  1.25.2  1.24.5  1.23.0  1.22.2  1.21.1  1.20.5  1.19.3  1.18.3  1.17.0  1.16.0  1.15.0  1.14.1  1.13.1  1.12.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1). 

Package lineage is an auto-generated package for the Data Lineage API. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/datacatalog/lineage/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := lineage.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &lineagepb.BatchSearchLinkProcessesRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#BatchSearchLinkProcessesRequest.
    }
    it := c.BatchSearchLinkProcesses(ctx, req)
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
        _ = it.Response.(*lineagepb.BatchSearchLinkProcessesResponse)
    }

## Use of Context

The ctx passed to NewClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## CallOptions
    
    
    type CallOptions struct {
    	ProcessOpenLineageRunEvent []gax.CallOption
    	CreateProcess              []gax.CallOption
    	UpdateProcess              []gax.CallOption
    	GetProcess                 []gax.CallOption
    	ListProcesses              []gax.CallOption
    	DeleteProcess              []gax.CallOption
    	CreateRun                  []gax.CallOption
    	UpdateRun                  []gax.CallOption
    	GetRun                     []gax.CallOption
    	ListRuns                   []gax.CallOption
    	DeleteRun                  []gax.CallOption
    	CreateLineageEvent         []gax.CallOption
    	GetLineageEvent            []gax.CallOption
    	ListLineageEvents          []gax.CallOption
    	DeleteLineageEvent         []gax.CallOption
    	SearchLinks                []gax.CallOption
    	BatchSearchLinkProcesses   []gax.CallOption
    	SearchLineageStreaming     []gax.CallOption
    	CancelOperation            []gax.CallOption
    	DeleteOperation            []gax.CallOption
    	GetOperation               []gax.CallOption
    	ListOperations             []gax.CallOption
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

Client is a client for interacting with Data Lineage API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Lineage is used to track data flows between assets over time. You can create LineageEvents to record lineage between multiple sources and a single target, for example, when table data is based on data from multiple tables.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new lineage client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Lineage is used to track data flows between assets over time. You can create LineageEvents to record lineage between multiple sources and a single target, for example, when table data is based on data from multiple tables.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new lineage rest client.

Lineage is used to track data flows between assets over time. You can create LineageEvents to record lineage between multiple sources and a single target, for example, when table data is based on data from multiple tables.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) BatchSearchLinkProcesses 
    
    
    func (c *Client) BatchSearchLinkProcesses(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_BatchSearchLinkProcessesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProcessLinksIterator

BatchSearchLinkProcesses retrieve information about LineageProcesses associated with specific links. LineageProcesses are transformation pipelines that result in data flowing from source to target assets. Links between assets represent this operation.

If you have specific link names, you can use this method to verify which LineageProcesses contribute to creating those links. See the SearchLinks method for more information on how to retrieve link name.

You can retrieve the LineageProcess information in every project where you have the datalineage.events.get permission. The project provided in the URL is used for Billing and Quota.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.BatchSearchLinkProcessesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#BatchSearchLinkProcessesRequest.
    	}
    	it := c.BatchSearchLinkProcesses(ctx, req)
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
    		_ = it.Response.(*lineagepb.BatchSearchLinkProcessesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.BatchSearchLinkProcessesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#BatchSearchLinkProcessesRequest.
    	}
    	for resp, err := range c.BatchSearchLinkProcesses(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) CancelOperation 
    
    
    func (c *Client) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
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

### func (*Client) CreateLineageEvent 
    
    
    func (c *Client) CreateLineageEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[CreateLineageEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_CreateLineageEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[LineageEvent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_LineageEvent), [error](https://pkg.go.dev/builtin#error))

CreateLineageEvent creates a new lineage event.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.CreateLineageEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#CreateLineageEventRequest.
    	}
    	resp, err := c.CreateLineageEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateProcess 
    
    
    func (c *Client) CreateProcess(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[CreateProcessRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_CreateProcessRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Process](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Process), [error](https://pkg.go.dev/builtin#error))

CreateProcess creates a new process.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.CreateProcessRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#CreateProcessRequest.
    	}
    	resp, err := c.CreateProcess(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateRun 
    
    
    func (c *Client) CreateRun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[CreateRunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_CreateRunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Run](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Run), [error](https://pkg.go.dev/builtin#error))

CreateRun creates a new run.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.CreateRunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#CreateRunRequest.
    	}
    	resp, err := c.CreateRun(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) DeleteLineageEvent 
    
    
    func (c *Client) DeleteLineageEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[DeleteLineageEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_DeleteLineageEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteLineageEvent deletes the lineage event with the specified name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.DeleteLineageEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#DeleteLineageEventRequest.
    	}
    	err = c.DeleteLineageEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteProcess 
    
    
    func (c *Client) DeleteProcess(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[DeleteProcessRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_DeleteProcessRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteProcessOperation, [error](https://pkg.go.dev/builtin#error))

DeleteProcess deletes the process with the specified name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.DeleteProcessRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#DeleteProcessRequest.
    	}
    	op, err := c.DeleteProcess(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteProcessOperation 
    
    
    func (c *Client) DeleteProcessOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteProcessOperation

DeleteProcessOperation returns a new DeleteProcessOperation from a given name. The name must be that of a previously created DeleteProcessOperation, possibly from a different process.

### func (*Client) DeleteRun 
    
    
    func (c *Client) DeleteRun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[DeleteRunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_DeleteRunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteRunOperation, [error](https://pkg.go.dev/builtin#error))

DeleteRun deletes the run with the specified name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.DeleteRunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#DeleteRunRequest.
    	}
    	op, err := c.DeleteRun(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteRunOperation 
    
    
    func (c *Client) DeleteRunOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteRunOperation

DeleteRunOperation returns a new DeleteRunOperation from a given name. The name must be that of a previously created DeleteRunOperation, possibly from a different process.

### func (*Client) GetLineageEvent 
    
    
    func (c *Client) GetLineageEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[GetLineageEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_GetLineageEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[LineageEvent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_LineageEvent), [error](https://pkg.go.dev/builtin#error))

GetLineageEvent gets details of a specified lineage event.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.GetLineageEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#GetLineageEventRequest.
    	}
    	resp, err := c.GetLineageEvent(ctx, req)
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
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
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
    

### func (*Client) GetProcess 
    
    
    func (c *Client) GetProcess(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[GetProcessRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_GetProcessRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Process](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Process), [error](https://pkg.go.dev/builtin#error))

GetProcess gets the details of the specified process.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.GetProcessRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#GetProcessRequest.
    	}
    	resp, err := c.GetProcess(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetRun 
    
    
    func (c *Client) GetRun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[GetRunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_GetRunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Run](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Run), [error](https://pkg.go.dev/builtin#error))

GetRun gets the details of the specified run.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.GetRunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#GetRunRequest.
    	}
    	resp, err := c.GetRun(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListLineageEvents 
    
    
    func (c *Client) ListLineageEvents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[ListLineageEventsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_ListLineageEventsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LineageEventIterator

ListLineageEvents lists lineage events in the given project and location. The list order is not defined.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ListLineageEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ListLineageEventsRequest.
    	}
    	it := c.ListLineageEvents(ctx, req)
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
    		_ = it.Response.(*lineagepb.ListLineageEventsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ListLineageEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ListLineageEventsRequest.
    	}
    	for resp, err := range c.ListLineageEvents(ctx, req).All() {
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
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    
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
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
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
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
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
    

### func (*Client) ListProcesses 
    
    
    func (c *Client) ListProcesses(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[ListProcessesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_ListProcessesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProcessIterator

ListProcesses list processes in the given project and location. List order is descending by insertion time.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ListProcessesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ListProcessesRequest.
    	}
    	it := c.ListProcesses(ctx, req)
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
    		_ = it.Response.(*lineagepb.ListProcessesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ListProcessesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ListProcessesRequest.
    	}
    	for resp, err := range c.ListProcesses(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListRuns 
    
    
    func (c *Client) ListRuns(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[ListRunsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_ListRunsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *RunIterator

ListRuns lists runs in the given project and location. List order is descending by start_time.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ListRunsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ListRunsRequest.
    	}
    	it := c.ListRuns(ctx, req)
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
    		_ = it.Response.(*lineagepb.ListRunsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ListRunsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ListRunsRequest.
    	}
    	for resp, err := range c.ListRuns(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ProcessOpenLineageRunEvent 
    
    
    func (c *Client) ProcessOpenLineageRunEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_ProcessOpenLineageRunEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_ProcessOpenLineageRunEventResponse), [error](https://pkg.go.dev/builtin#error))

ProcessOpenLineageRunEvent creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json> (at <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.ProcessOpenLineageRunEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#ProcessOpenLineageRunEventRequest.
    	}
    	resp, err := c.ProcessOpenLineageRunEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) SearchLineageStreaming 
    
    
    func (c *Client) SearchLineageStreaming(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[SearchLineageStreamingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_SearchLineageStreamingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Lineage_SearchLineageStreamingClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Lineage_SearchLineageStreamingClient), [error](https://pkg.go.dev/builtin#error))

SearchLineageStreaming retrieves a streaming response of lineage links connected to the requested assets by performing a breadth-first search in the given direction. Links represent the data flow between source (upstream) and target (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them. This method retrieves links from all valid locations provided in the request. This method supports Column-Level Lineage (CLL) along with wildcard support to retrieve all CLL for an Entity FQN.

Following permissions are required to retrieve links:
    
    
    datalineage.events.get permission for the project where the link is
    stored for entity-level lineage.
    
    datalineage.events.getFields permission for the project where the link
    is stored for column-level lineage.
    

This method also returns processes that created the links if explicitly requested by setting max_process_per_link (at google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.limits.max_process_per_link) is non-zero and full process details are requested via links.processes.process in the FieldMask (at <https://developers.google.com/workspace/docs/api/how-tos/field-masks#read_with_a_field_mask>).

Permission required to retrieve processes:
    
    
    datalineage.processes.get permission for the project where the process
    is stored.
    

### func (*Client) SearchLinks 
    
    
    func (c *Client) SearchLinks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[SearchLinksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_SearchLinksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LinkIterator

SearchLinks retrieve a list of links connected to a specific asset. Links represent the data flow between source (upstream) and target (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them.

You can retrieve links in every project where you have the datalineage.events.get permission. The project provided in the URL is used for Billing and Quota.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.SearchLinksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#SearchLinksRequest.
    	}
    	it := c.SearchLinks(ctx, req)
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
    		_ = it.Response.(*lineagepb.SearchLinksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.SearchLinksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#SearchLinksRequest.
    	}
    	for resp, err := range c.SearchLinks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) UpdateProcess 
    
    
    func (c *Client) UpdateProcess(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[UpdateProcessRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_UpdateProcessRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Process](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Process), [error](https://pkg.go.dev/builtin#error))

UpdateProcess updates a process.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.UpdateProcessRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#UpdateProcessRequest.
    	}
    	resp, err := c.UpdateProcess(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateRun 
    
    
    func (c *Client) UpdateRun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[UpdateRunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_UpdateRunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Run](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Run), [error](https://pkg.go.dev/builtin#error))

UpdateRun updates a run.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	lineage "cloud.google.com/go/datacatalog/lineage/apiv1"
    	lineagepb "cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := lineage.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1.html#cloud_google_com_go_datacatalog_lineage_apiv1_Client_Close)()
    
    	req := &lineagepb.UpdateRunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/datacatalog/lineage/apiv1/lineagepb#UpdateRunRequest.
    	}
    	resp, err := c.UpdateRun(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## DeleteProcessOperation
    
    
    type DeleteProcessOperation struct {
    	// contains filtered or unexported fields
    }

DeleteProcessOperation manages a long-running operation from DeleteProcess.

### func (*DeleteProcessOperation) Done 
    
    
    func (op *DeleteProcessOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteProcessOperation) Metadata 
    
    
    func (op *DeleteProcessOperation) Metadata() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteProcessOperation) Name 
    
    
    func (op *DeleteProcessOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteProcessOperation) Poll 
    
    
    func (op *DeleteProcessOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteProcessOperation) Wait 
    
    
    func (op *DeleteProcessOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteRunOperation
    
    
    type DeleteRunOperation struct {
    	// contains filtered or unexported fields
    }

DeleteRunOperation manages a long-running operation from DeleteRun.

### func (*DeleteRunOperation) Done 
    
    
    func (op *DeleteRunOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteRunOperation) Metadata 
    
    
    func (op *DeleteRunOperation) Metadata() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteRunOperation) Name 
    
    
    func (op *DeleteRunOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteRunOperation) Poll 
    
    
    func (op *DeleteRunOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteRunOperation) Wait 
    
    
    func (op *DeleteRunOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## LineageEventIterator
    
    
    type LineageEventIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*lineagepb.LineageEvent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

LineageEventIterator manages a stream of *lineagepb.LineageEvent.

### func (*LineageEventIterator) All 
    
    
    func (it *LineageEventIterator) All() iter.Seq2[*lineagepb.LineageEvent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*LineageEventIterator) Next 
    
    
    func (it *LineageEventIterator) Next() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[LineageEvent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_LineageEvent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*LineageEventIterator) PageInfo 
    
    
    func (it *LineageEventIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## LinkIterator
    
    
    type LinkIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*lineagepb.Link, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

LinkIterator manages a stream of *lineagepb.Link.

### func (*LinkIterator) All 
    
    
    func (it *LinkIterator) All() iter.Seq2[*lineagepb.Link, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*LinkIterator) Next 
    
    
    func (it *LinkIterator) Next() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Link](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Link), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*LinkIterator) PageInfo 
    
    
    func (it *LinkIterator) PageInfo() *iterator.PageInfo

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

## ProcessIterator
    
    
    type ProcessIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*lineagepb.Process, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ProcessIterator manages a stream of *lineagepb.Process.

### func (*ProcessIterator) All 
    
    
    func (it *ProcessIterator) All() iter.Seq2[*lineagepb.Process, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ProcessIterator) Next 
    
    
    func (it *ProcessIterator) Next() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Process](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Process), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ProcessIterator) PageInfo 
    
    
    func (it *ProcessIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ProcessLinksIterator
    
    
    type ProcessLinksIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*lineagepb.ProcessLinks, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ProcessLinksIterator manages a stream of *lineagepb.ProcessLinks.

### func (*ProcessLinksIterator) All 
    
    
    func (it *ProcessLinksIterator) All() iter.Seq2[*lineagepb.ProcessLinks, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ProcessLinksIterator) Next 
    
    
    func (it *ProcessLinksIterator) Next() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[ProcessLinks](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_ProcessLinks), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ProcessLinksIterator) PageInfo 
    
    
    func (it *ProcessLinksIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## RunIterator
    
    
    type RunIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*lineagepb.Run, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

RunIterator manages a stream of *lineagepb.Run.

### func (*RunIterator) All 
    
    
    func (it *RunIterator) All() iter.Seq2[*lineagepb.Run, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*RunIterator) Next 
    
    
    func (it *RunIterator) Next() (*[lineagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb).[Run](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/datacatalog/latest/lineage/apiv1/lineagepb#cloud_google_com_go_datacatalog_lineage_apiv1_lineagepb_Run), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*RunIterator) PageInfo 
    
    
    func (it *RunIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
