---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/
title: BeyondCorp AppGateways API v1 - Package cloud.google.com/go/beyondcorp/appgateways/apiv1 (v1.10.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:10.293329+00:00
---

# BeyondCorp AppGateways API v1 - Package cloud.google.com/go/beyondcorp/appgateways/apiv1 (v1.10.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  BeyondCorp AppGateways API v1 - Package cloud.google.com/go/beyondcorp/appgateways/apiv1 (v1.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.0 (latest)  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.6  1.0.11  0.6.1  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1). 

Package appgateways is an auto-generated package for the BeyondCorp API. 

Chrome Enterprise Premium is a secure enterprise browsing solution that provides secure access to applications and resources, and offers integrated threat and data protection. It adds an extra layer of security to safeguard your Chrome browser environment, including Data Loss Prevention (DLP), real-time URL and file scanning, and Context-Aware Access for SaaS and web apps. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/beyondcorp/appgateways/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := appgateways.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &appgatewayspb.CreateAppGatewayRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb#CreateAppGatewayRequest.
    }
    op, err := c.CreateAppGateway(ctx, req)
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

## AppGatewayIterator
    
    
    type AppGatewayIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*appgatewayspb.AppGateway, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AppGatewayIterator manages a stream of *appgatewayspb.AppGateway.

### func (*AppGatewayIterator) All 
    
    
    func (it *AppGatewayIterator) All() iter.Seq2[*appgatewayspb.AppGateway, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AppGatewayIterator) Next 
    
    
    func (it *AppGatewayIterator) Next() (*[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[AppGateway](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_AppGateway), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AppGatewayIterator) PageInfo 
    
    
    func (it *AppGatewayIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CallOptions
    
    
    type CallOptions struct {
    	ListAppGateways    []gax.CallOption
    	GetAppGateway      []gax.CallOption
    	CreateAppGateway   []gax.CallOption
    	DeleteAppGateway   []gax.CallOption
    	GetLocation        []gax.CallOption
    	ListLocations      []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client (deprecated)
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

Client is a client for interacting with BeyondCorp API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

API Overview:

The beyondcorp.googleapis.com service implements the Google Cloud BeyondCorp API.

Data Model:

The AppGatewaysService exposes the following resources:
    
    
    AppGateways, named as follows:
    projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id}.
    

The AppGatewaysService service provides methods to manage (create/read/update/delete) BeyondCorp AppGateways.

Deprecated: App Connector is deprecated and creation of new App Connector resources is no longer permitted. Use Security Gateway instead.

Deprecated: AppGatewaysService may be removed in a future version.

### func NewClient (deprecated)
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new app gateways service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

API Overview:

The beyondcorp.googleapis.com service implements the Google Cloud BeyondCorp API.

Data Model:

The AppGatewaysService exposes the following resources:
    
    
    AppGateways, named as follows:
    projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id}.
    

The AppGatewaysService service provides methods to manage (create/read/update/delete) BeyondCorp AppGateways.

Deprecated: App Connector is deprecated and creation of new App Connector resources is no longer permitted. Use Security Gateway instead.

Deprecated: AppGatewaysService may be removed in a future version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) CancelOperation (deprecated)
    
    
    func (c *Client) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) Close (deprecated)
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) CreateAppGateway (deprecated)
    
    
    func (c *Client) CreateAppGateway(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[CreateAppGatewayRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_CreateAppGatewayRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateAppGatewayOperation, [error](https://pkg.go.dev/builtin#error))

CreateAppGateway creates a new AppGateway in a given project and location.

Deprecated: CreateAppGateway may be removed in a future version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    	appgatewayspb "cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &appgatewayspb.CreateAppGatewayRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb#CreateAppGatewayRequest.
    	}
    	op, err := c.CreateAppGateway(ctx, req)
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
    

### func (*Client) CreateAppGatewayOperation (deprecated)
    
    
    func (c *Client) CreateAppGatewayOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateAppGatewayOperation

CreateAppGatewayOperation returns a new CreateAppGatewayOperation from a given name. The name must be that of a previously created CreateAppGatewayOperation, possibly from a different process.

### func (*Client) DeleteAppGateway (deprecated)
    
    
    func (c *Client) DeleteAppGateway(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[DeleteAppGatewayRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_DeleteAppGatewayRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteAppGatewayOperation, [error](https://pkg.go.dev/builtin#error))

DeleteAppGateway deletes a single AppGateway.

Deprecated: DeleteAppGateway may be removed in a future version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    	appgatewayspb "cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &appgatewayspb.DeleteAppGatewayRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb#DeleteAppGatewayRequest.
    	}
    	op, err := c.DeleteAppGateway(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteAppGatewayOperation (deprecated)
    
    
    func (c *Client) DeleteAppGatewayOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteAppGatewayOperation

DeleteAppGatewayOperation returns a new DeleteAppGatewayOperation from a given name. The name must be that of a previously created DeleteAppGatewayOperation, possibly from a different process.

### func (*Client) DeleteOperation (deprecated)
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) GetAppGateway (deprecated)
    
    
    func (c *Client) GetAppGateway(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[GetAppGatewayRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_GetAppGatewayRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[AppGateway](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_AppGateway), [error](https://pkg.go.dev/builtin#error))

GetAppGateway gets details of a single AppGateway.

Deprecated: GetAppGateway may be removed in a future version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    	appgatewayspb "cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &appgatewayspb.GetAppGatewayRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb#GetAppGatewayRequest.
    	}
    	resp, err := c.GetAppGateway(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetIamPolicy (deprecated)
    
    
    func (c *Client) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &iampb.[GetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest.
    	}
    	resp, err := c.GetIamPolicy(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetLocation (deprecated)
    
    
    func (c *Client) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.[GetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_GetLocation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetOperation (deprecated)
    
    
    func (c *Client) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
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
    

### func (*Client) ListAppGateways (deprecated)
    
    
    func (c *Client) ListAppGateways(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[ListAppGatewaysRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_ListAppGatewaysRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AppGatewayIterator

ListAppGateways lists AppGateways in a given project and location.

Deprecated: ListAppGateways may be removed in a future version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    	appgatewayspb "cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &appgatewayspb.ListAppGatewaysRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb#ListAppGatewaysRequest.
    	}
    	it := c.ListAppGateways(ctx, req)
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
    		_ = it.Response.(*appgatewayspb.ListAppGatewaysResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    	appgatewayspb "cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &appgatewayspb.ListAppGatewaysRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/beyondcorp/appgateways/apiv1/appgatewayspb#ListAppGatewaysRequest.
    	}
    	for resp, err := range c.ListAppGateways(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListLocations (deprecated)
    
    
    func (c *Client) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
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
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_ListLocations)(ctx, req)
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
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOperations (deprecated)
    
    
    func (c *Client) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
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
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
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
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
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
    

### func (*Client) SetIamPolicy (deprecated)
    
    
    func (c *Client) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &iampb.[SetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest.
    	}
    	resp, err := c.SetIamPolicy(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) TestIamPermissions (deprecated)
    
    
    func (c *Client) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	appgateways "cloud.google.com/go/beyondcorp/appgateways/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := appgateways.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1.html#cloud_google_com_go_beyondcorp_appgateways_apiv1_Client_Close)()
    
    	req := &iampb.[TestIamPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest.
    	}
    	resp, err := c.TestIamPermissions(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CreateAppGatewayOperation
    
    
    type CreateAppGatewayOperation struct {
    	// contains filtered or unexported fields
    }

CreateAppGatewayOperation manages a long-running operation from CreateAppGateway.

### func (*CreateAppGatewayOperation) Done 
    
    
    func (op *CreateAppGatewayOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateAppGatewayOperation) Metadata 
    
    
    func (op *CreateAppGatewayOperation) Metadata() (*[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[AppGatewayOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_AppGatewayOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateAppGatewayOperation) Name 
    
    
    func (op *CreateAppGatewayOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateAppGatewayOperation) Poll 
    
    
    func (op *CreateAppGatewayOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[AppGateway](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_AppGateway), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateAppGatewayOperation) Wait 
    
    
    func (op *CreateAppGatewayOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[AppGateway](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_AppGateway), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteAppGatewayOperation
    
    
    type DeleteAppGatewayOperation struct {
    	// contains filtered or unexported fields
    }

DeleteAppGatewayOperation manages a long-running operation from DeleteAppGateway.

### func (*DeleteAppGatewayOperation) Done 
    
    
    func (op *DeleteAppGatewayOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteAppGatewayOperation) Metadata 
    
    
    func (op *DeleteAppGatewayOperation) Metadata() (*[appgatewayspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb).[AppGatewayOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/beyondcorp/latest/appgateways/apiv1/appgatewayspb#cloud_google_com_go_beyondcorp_appgateways_apiv1_appgatewayspb_AppGatewayOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteAppGatewayOperation) Name 
    
    
    func (op *DeleteAppGatewayOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteAppGatewayOperation) Poll 
    
    
    func (op *DeleteAppGatewayOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteAppGatewayOperation) Wait 
    
    
    func (op *DeleteAppGatewayOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
