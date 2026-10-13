---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/
title: Eventarc API v1 - Package cloud.google.com/go/eventarc/apiv1 (v1.26.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:38.895610+00:00
---

# Eventarc API v1 - Package cloud.google.com/go/eventarc/apiv1 (v1.26.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Eventarc API v1 - Package cloud.google.com/go/eventarc/apiv1 (v1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.1  1.15.5  1.14.2  1.13.11  1.12.1  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1). 

Package eventarc is an auto-generated package for the Eventarc API. 

Build event-driven applications on Google Cloud Platform. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/eventarc/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := eventarc.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &eventarcpb.CreateChannelRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateChannelRequest.
    }
    op, err := c.CreateChannel(ctx, req)
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
    	GetTrigger                []gax.CallOption
    	ListTriggers              []gax.CallOption
    	CreateTrigger             []gax.CallOption
    	UpdateTrigger             []gax.CallOption
    	DeleteTrigger             []gax.CallOption
    	GetChannel                []gax.CallOption
    	ListChannels              []gax.CallOption
    	CreateChannel             []gax.CallOption
    	UpdateChannel             []gax.CallOption
    	DeleteChannel             []gax.CallOption
    	GetProvider               []gax.CallOption
    	ListProviders             []gax.CallOption
    	GetChannelConnection      []gax.CallOption
    	ListChannelConnections    []gax.CallOption
    	CreateChannelConnection   []gax.CallOption
    	DeleteChannelConnection   []gax.CallOption
    	GetGoogleChannelConfig    []gax.CallOption
    	UpdateGoogleChannelConfig []gax.CallOption
    	GetMessageBus             []gax.CallOption
    	ListMessageBuses          []gax.CallOption
    	ListMessageBusEnrollments []gax.CallOption
    	CreateMessageBus          []gax.CallOption
    	UpdateMessageBus          []gax.CallOption
    	DeleteMessageBus          []gax.CallOption
    	GetEnrollment             []gax.CallOption
    	ListEnrollments           []gax.CallOption
    	CreateEnrollment          []gax.CallOption
    	UpdateEnrollment          []gax.CallOption
    	DeleteEnrollment          []gax.CallOption
    	GetPipeline               []gax.CallOption
    	ListPipelines             []gax.CallOption
    	CreatePipeline            []gax.CallOption
    	UpdatePipeline            []gax.CallOption
    	DeletePipeline            []gax.CallOption
    	GetGoogleApiSource        []gax.CallOption
    	ListGoogleApiSources      []gax.CallOption
    	CreateGoogleApiSource     []gax.CallOption
    	UpdateGoogleApiSource     []gax.CallOption
    	DeleteGoogleApiSource     []gax.CallOption
    	GetLocation               []gax.CallOption
    	ListLocations             []gax.CallOption
    	GetIamPolicy              []gax.CallOption
    	SetIamPolicy              []gax.CallOption
    	TestIamPermissions        []gax.CallOption
    	CancelOperation           []gax.CallOption
    	DeleteOperation           []gax.CallOption
    	GetOperation              []gax.CallOption
    	ListOperations            []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## ChannelConnectionIterator
    
    
    type ChannelConnectionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.ChannelConnection, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ChannelConnectionIterator manages a stream of *eventarcpb.ChannelConnection.

### func (*ChannelConnectionIterator) All 
    
    
    func (it *ChannelConnectionIterator) All() iter.Seq2[*eventarcpb.ChannelConnection, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ChannelConnectionIterator) Next 
    
    
    func (it *ChannelConnectionIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ChannelConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ChannelConnection), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ChannelConnectionIterator) PageInfo 
    
    
    func (it *ChannelConnectionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ChannelIterator
    
    
    type ChannelIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.Channel, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ChannelIterator manages a stream of *eventarcpb.Channel.

### func (*ChannelIterator) All 
    
    
    func (it *ChannelIterator) All() iter.Seq2[*eventarcpb.Channel, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ChannelIterator) Next 
    
    
    func (it *ChannelIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ChannelIterator) PageInfo 
    
    
    func (it *ChannelIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

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

Client is a client for interacting with Eventarc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Eventarc allows users to subscribe to various events that are provided by Google Cloud services and forward them to supported destinations.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new eventarc client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Eventarc allows users to subscribe to various events that are provided by Google Cloud services and forward them to supported destinations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new eventarc rest client.

Eventarc allows users to subscribe to various events that are provided by Google Cloud services and forward them to supported destinations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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

### func (*Client) CreateChannel 
    
    
    func (c *Client) CreateChannel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreateChannelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreateChannelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateChannelOperation, [error](https://pkg.go.dev/builtin#error))

CreateChannel create a new channel in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreateChannelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateChannelRequest.
    	}
    	op, err := c.CreateChannel(ctx, req)
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
    

### func (*Client) CreateChannelConnection 
    
    
    func (c *Client) CreateChannelConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreateChannelConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreateChannelConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateChannelConnectionOperation, [error](https://pkg.go.dev/builtin#error))

CreateChannelConnection create a new ChannelConnection in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreateChannelConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateChannelConnectionRequest.
    	}
    	op, err := c.CreateChannelConnection(ctx, req)
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
    

### func (*Client) CreateChannelConnectionOperation 
    
    
    func (c *Client) CreateChannelConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateChannelConnectionOperation

CreateChannelConnectionOperation returns a new CreateChannelConnectionOperation from a given name. The name must be that of a previously created CreateChannelConnectionOperation, possibly from a different process.

### func (*Client) CreateChannelOperation 
    
    
    func (c *Client) CreateChannelOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateChannelOperation

CreateChannelOperation returns a new CreateChannelOperation from a given name. The name must be that of a previously created CreateChannelOperation, possibly from a different process.

### func (*Client) CreateEnrollment 
    
    
    func (c *Client) CreateEnrollment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreateEnrollmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreateEnrollmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateEnrollmentOperation, [error](https://pkg.go.dev/builtin#error))

CreateEnrollment create a new Enrollment in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreateEnrollmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateEnrollmentRequest.
    	}
    	op, err := c.CreateEnrollment(ctx, req)
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
    

### func (*Client) CreateEnrollmentOperation 
    
    
    func (c *Client) CreateEnrollmentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateEnrollmentOperation

CreateEnrollmentOperation returns a new CreateEnrollmentOperation from a given name. The name must be that of a previously created CreateEnrollmentOperation, possibly from a different process.

### func (*Client) CreateGoogleApiSource 
    
    
    func (c *Client) CreateGoogleApiSource(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreateGoogleApiSourceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreateGoogleApiSourceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateGoogleApiSourceOperation, [error](https://pkg.go.dev/builtin#error))

CreateGoogleApiSource create a new GoogleApiSource in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreateGoogleApiSourceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateGoogleApiSourceRequest.
    	}
    	op, err := c.CreateGoogleApiSource(ctx, req)
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
    

### func (*Client) CreateGoogleApiSourceOperation 
    
    
    func (c *Client) CreateGoogleApiSourceOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateGoogleApiSourceOperation

CreateGoogleApiSourceOperation returns a new CreateGoogleApiSourceOperation from a given name. The name must be that of a previously created CreateGoogleApiSourceOperation, possibly from a different process.

### func (*Client) CreateMessageBus 
    
    
    func (c *Client) CreateMessageBus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreateMessageBusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreateMessageBusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateMessageBusOperation, [error](https://pkg.go.dev/builtin#error))

CreateMessageBus create a new MessageBus in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreateMessageBusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateMessageBusRequest.
    	}
    	op, err := c.CreateMessageBus(ctx, req)
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
    

### func (*Client) CreateMessageBusOperation 
    
    
    func (c *Client) CreateMessageBusOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateMessageBusOperation

CreateMessageBusOperation returns a new CreateMessageBusOperation from a given name. The name must be that of a previously created CreateMessageBusOperation, possibly from a different process.

### func (*Client) CreatePipeline 
    
    
    func (c *Client) CreatePipeline(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreatePipelineRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreatePipelineRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreatePipelineOperation, [error](https://pkg.go.dev/builtin#error))

CreatePipeline create a new Pipeline in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreatePipelineRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreatePipelineRequest.
    	}
    	op, err := c.CreatePipeline(ctx, req)
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
    

### func (*Client) CreatePipelineOperation 
    
    
    func (c *Client) CreatePipelineOperation(name [string](https://pkg.go.dev/builtin#string)) *CreatePipelineOperation

CreatePipelineOperation returns a new CreatePipelineOperation from a given name. The name must be that of a previously created CreatePipelineOperation, possibly from a different process.

### func (*Client) CreateTrigger 
    
    
    func (c *Client) CreateTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[CreateTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_CreateTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateTriggerOperation, [error](https://pkg.go.dev/builtin#error))

CreateTrigger create a new trigger in a particular project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.CreateTriggerRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#CreateTriggerRequest.
    	}
    	op, err := c.CreateTrigger(ctx, req)
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
    

### func (*Client) CreateTriggerOperation 
    
    
    func (c *Client) CreateTriggerOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateTriggerOperation

CreateTriggerOperation returns a new CreateTriggerOperation from a given name. The name must be that of a previously created CreateTriggerOperation, possibly from a different process.

### func (*Client) DeleteChannel 
    
    
    func (c *Client) DeleteChannel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeleteChannelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeleteChannelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteChannelOperation, [error](https://pkg.go.dev/builtin#error))

DeleteChannel delete a single channel.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeleteChannelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeleteChannelRequest.
    	}
    	op, err := c.DeleteChannel(ctx, req)
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
    

### func (*Client) DeleteChannelConnection 
    
    
    func (c *Client) DeleteChannelConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeleteChannelConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeleteChannelConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteChannelConnectionOperation, [error](https://pkg.go.dev/builtin#error))

DeleteChannelConnection delete a single ChannelConnection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeleteChannelConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeleteChannelConnectionRequest.
    	}
    	op, err := c.DeleteChannelConnection(ctx, req)
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
    

### func (*Client) DeleteChannelConnectionOperation 
    
    
    func (c *Client) DeleteChannelConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteChannelConnectionOperation

DeleteChannelConnectionOperation returns a new DeleteChannelConnectionOperation from a given name. The name must be that of a previously created DeleteChannelConnectionOperation, possibly from a different process.

### func (*Client) DeleteChannelOperation 
    
    
    func (c *Client) DeleteChannelOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteChannelOperation

DeleteChannelOperation returns a new DeleteChannelOperation from a given name. The name must be that of a previously created DeleteChannelOperation, possibly from a different process.

### func (*Client) DeleteEnrollment 
    
    
    func (c *Client) DeleteEnrollment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeleteEnrollmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeleteEnrollmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteEnrollmentOperation, [error](https://pkg.go.dev/builtin#error))

DeleteEnrollment delete a single Enrollment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeleteEnrollmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeleteEnrollmentRequest.
    	}
    	op, err := c.DeleteEnrollment(ctx, req)
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
    

### func (*Client) DeleteEnrollmentOperation 
    
    
    func (c *Client) DeleteEnrollmentOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteEnrollmentOperation

DeleteEnrollmentOperation returns a new DeleteEnrollmentOperation from a given name. The name must be that of a previously created DeleteEnrollmentOperation, possibly from a different process.

### func (*Client) DeleteGoogleApiSource 
    
    
    func (c *Client) DeleteGoogleApiSource(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeleteGoogleApiSourceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeleteGoogleApiSourceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteGoogleApiSourceOperation, [error](https://pkg.go.dev/builtin#error))

DeleteGoogleApiSource delete a single GoogleApiSource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeleteGoogleApiSourceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeleteGoogleApiSourceRequest.
    	}
    	op, err := c.DeleteGoogleApiSource(ctx, req)
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
    

### func (*Client) DeleteGoogleApiSourceOperation 
    
    
    func (c *Client) DeleteGoogleApiSourceOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteGoogleApiSourceOperation

DeleteGoogleApiSourceOperation returns a new DeleteGoogleApiSourceOperation from a given name. The name must be that of a previously created DeleteGoogleApiSourceOperation, possibly from a different process.

### func (*Client) DeleteMessageBus 
    
    
    func (c *Client) DeleteMessageBus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeleteMessageBusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeleteMessageBusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteMessageBusOperation, [error](https://pkg.go.dev/builtin#error))

DeleteMessageBus delete a single message bus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeleteMessageBusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeleteMessageBusRequest.
    	}
    	op, err := c.DeleteMessageBus(ctx, req)
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
    

### func (*Client) DeleteMessageBusOperation 
    
    
    func (c *Client) DeleteMessageBusOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteMessageBusOperation

DeleteMessageBusOperation returns a new DeleteMessageBusOperation from a given name. The name must be that of a previously created DeleteMessageBusOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeletePipeline 
    
    
    func (c *Client) DeletePipeline(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeletePipelineRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeletePipelineRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeletePipelineOperation, [error](https://pkg.go.dev/builtin#error))

DeletePipeline delete a single pipeline.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeletePipelineRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeletePipelineRequest.
    	}
    	op, err := c.DeletePipeline(ctx, req)
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
    

### func (*Client) DeletePipelineOperation 
    
    
    func (c *Client) DeletePipelineOperation(name [string](https://pkg.go.dev/builtin#string)) *DeletePipelineOperation

DeletePipelineOperation returns a new DeletePipelineOperation from a given name. The name must be that of a previously created DeletePipelineOperation, possibly from a different process.

### func (*Client) DeleteTrigger 
    
    
    func (c *Client) DeleteTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[DeleteTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_DeleteTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteTriggerOperation, [error](https://pkg.go.dev/builtin#error))

DeleteTrigger delete a single trigger.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.DeleteTriggerRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#DeleteTriggerRequest.
    	}
    	op, err := c.DeleteTrigger(ctx, req)
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
    

### func (*Client) DeleteTriggerOperation 
    
    
    func (c *Client) DeleteTriggerOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteTriggerOperation

DeleteTriggerOperation returns a new DeleteTriggerOperation from a given name. The name must be that of a previously created DeleteTriggerOperation, possibly from a different process.

### func (*Client) GetChannel 
    
    
    func (c *Client) GetChannel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetChannelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetChannelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

GetChannel get a single Channel.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetChannelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetChannelRequest.
    	}
    	resp, err := c.GetChannel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetChannelConnection 
    
    
    func (c *Client) GetChannelConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetChannelConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetChannelConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ChannelConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ChannelConnection), [error](https://pkg.go.dev/builtin#error))

GetChannelConnection get a single ChannelConnection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetChannelConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetChannelConnectionRequest.
    	}
    	resp, err := c.GetChannelConnection(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetEnrollment 
    
    
    func (c *Client) GetEnrollment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetEnrollmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetEnrollmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

GetEnrollment get a single Enrollment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetEnrollmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetEnrollmentRequest.
    	}
    	resp, err := c.GetEnrollment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGoogleApiSource 
    
    
    func (c *Client) GetGoogleApiSource(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetGoogleApiSourceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetGoogleApiSourceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

GetGoogleApiSource get a single GoogleApiSource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetGoogleApiSourceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetGoogleApiSourceRequest.
    	}
    	resp, err := c.GetGoogleApiSource(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGoogleChannelConfig 
    
    
    func (c *Client) GetGoogleChannelConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetGoogleChannelConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetGoogleChannelConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleChannelConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleChannelConfig), [error](https://pkg.go.dev/builtin#error))

GetGoogleChannelConfig get a GoogleChannelConfig. The name of the GoogleChannelConfig in the response is ALWAYS coded with projectID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetGoogleChannelConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetGoogleChannelConfigRequest.
    	}
    	resp, err := c.GetGoogleChannelConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetIamPolicy 
    
    
    func (c *Client) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    

### func (*Client) GetLocation 
    
    
    func (c *Client) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    

### func (*Client) GetMessageBus 
    
    
    func (c *Client) GetMessageBus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetMessageBusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetMessageBusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

GetMessageBus get a single MessageBus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetMessageBusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetMessageBusRequest.
    	}
    	resp, err := c.GetMessageBus(ctx, req)
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
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    

### func (*Client) GetPipeline 
    
    
    func (c *Client) GetPipeline(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetPipelineRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetPipelineRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

GetPipeline get a single Pipeline.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetPipelineRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetPipelineRequest.
    	}
    	resp, err := c.GetPipeline(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetProvider 
    
    
    func (c *Client) GetProvider(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetProviderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetProviderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Provider](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Provider), [error](https://pkg.go.dev/builtin#error))

GetProvider get a single Provider.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetProviderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetProviderRequest.
    	}
    	resp, err := c.GetProvider(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetTrigger 
    
    
    func (c *Client) GetTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GetTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GetTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

GetTrigger get a single trigger.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.GetTriggerRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#GetTriggerRequest.
    	}
    	resp, err := c.GetTrigger(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListChannelConnections 
    
    
    func (c *Client) ListChannelConnections(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListChannelConnectionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListChannelConnectionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ChannelConnectionIterator

ListChannelConnections list channel connections.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListChannelConnectionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListChannelConnectionsRequest.
    	}
    	it := c.ListChannelConnections(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListChannelConnectionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListChannelConnectionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListChannelConnectionsRequest.
    	}
    	for resp, err := range c.ListChannelConnections(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListChannels 
    
    
    func (c *Client) ListChannels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListChannelsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListChannelsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ChannelIterator

ListChannels list channels.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListChannelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListChannelsRequest.
    	}
    	it := c.ListChannels(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListChannelsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListChannelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListChannelsRequest.
    	}
    	for resp, err := range c.ListChannels(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListEnrollments 
    
    
    func (c *Client) ListEnrollments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListEnrollmentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListEnrollmentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EnrollmentIterator

ListEnrollments list Enrollments.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListEnrollmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListEnrollmentsRequest.
    	}
    	it := c.ListEnrollments(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListEnrollmentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListEnrollmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListEnrollmentsRequest.
    	}
    	for resp, err := range c.ListEnrollments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoogleApiSources 
    
    
    func (c *Client) ListGoogleApiSources(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListGoogleApiSourcesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListGoogleApiSourcesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoogleApiSourceIterator

ListGoogleApiSources list GoogleApiSources.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListGoogleApiSourcesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListGoogleApiSourcesRequest.
    	}
    	it := c.ListGoogleApiSources(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListGoogleApiSourcesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListGoogleApiSourcesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListGoogleApiSourcesRequest.
    	}
    	for resp, err := range c.ListGoogleApiSources(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListLocations 
    
    
    func (c *Client) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
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
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_ListLocations)(ctx, req)
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
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListMessageBusEnrollments 
    
    
    func (c *Client) ListMessageBusEnrollments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListMessageBusEnrollmentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListMessageBusEnrollmentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *StringIterator

ListMessageBusEnrollments list message bus enrollments.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListMessageBusEnrollmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListMessageBusEnrollmentsRequest.
    	}
    	it := c.ListMessageBusEnrollments(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListMessageBusEnrollmentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListMessageBusEnrollmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListMessageBusEnrollmentsRequest.
    	}
    	for resp, err := range c.ListMessageBusEnrollments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListMessageBuses 
    
    
    func (c *Client) ListMessageBuses(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListMessageBusesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListMessageBusesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *MessageBusIterator

ListMessageBuses list message buses.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListMessageBusesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListMessageBusesRequest.
    	}
    	it := c.ListMessageBuses(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListMessageBusesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListMessageBusesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListMessageBusesRequest.
    	}
    	for resp, err := range c.ListMessageBuses(ctx, req).All() {
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
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
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
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    

### func (*Client) ListPipelines 
    
    
    func (c *Client) ListPipelines(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListPipelinesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListPipelinesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PipelineIterator

ListPipelines list pipelines.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListPipelinesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListPipelinesRequest.
    	}
    	it := c.ListPipelines(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListPipelinesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListPipelinesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListPipelinesRequest.
    	}
    	for resp, err := range c.ListPipelines(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListProviders 
    
    
    func (c *Client) ListProviders(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListProvidersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListProvidersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProviderIterator

ListProviders list providers.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListProvidersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListProvidersRequest.
    	}
    	it := c.ListProviders(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListProvidersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListProvidersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListProvidersRequest.
    	}
    	for resp, err := range c.ListProviders(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListTriggers 
    
    
    func (c *Client) ListTriggers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ListTriggersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ListTriggersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TriggerIterator

ListTriggers list triggers.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListTriggersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListTriggersRequest.
    	}
    	it := c.ListTriggers(ctx, req)
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
    		_ = it.Response.(*eventarcpb.ListTriggersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.ListTriggersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#ListTriggersRequest.
    	}
    	for resp, err := range c.ListTriggers(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) SetIamPolicy 
    
    
    func (c *Client) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    

### func (*Client) TestIamPermissions 
    
    
    func (c *Client) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
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
    

### func (*Client) UpdateChannel 
    
    
    func (c *Client) UpdateChannel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdateChannelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdateChannelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateChannelOperation, [error](https://pkg.go.dev/builtin#error))

UpdateChannel update a single channel.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdateChannelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdateChannelRequest.
    	}
    	op, err := c.UpdateChannel(ctx, req)
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
    

### func (*Client) UpdateChannelOperation 
    
    
    func (c *Client) UpdateChannelOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateChannelOperation

UpdateChannelOperation returns a new UpdateChannelOperation from a given name. The name must be that of a previously created UpdateChannelOperation, possibly from a different process.

### func (*Client) UpdateEnrollment 
    
    
    func (c *Client) UpdateEnrollment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdateEnrollmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdateEnrollmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateEnrollmentOperation, [error](https://pkg.go.dev/builtin#error))

UpdateEnrollment update a single Enrollment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdateEnrollmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdateEnrollmentRequest.
    	}
    	op, err := c.UpdateEnrollment(ctx, req)
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
    

### func (*Client) UpdateEnrollmentOperation 
    
    
    func (c *Client) UpdateEnrollmentOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateEnrollmentOperation

UpdateEnrollmentOperation returns a new UpdateEnrollmentOperation from a given name. The name must be that of a previously created UpdateEnrollmentOperation, possibly from a different process.

### func (*Client) UpdateGoogleApiSource 
    
    
    func (c *Client) UpdateGoogleApiSource(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdateGoogleApiSourceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdateGoogleApiSourceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateGoogleApiSourceOperation, [error](https://pkg.go.dev/builtin#error))

UpdateGoogleApiSource update a single GoogleApiSource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdateGoogleApiSourceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdateGoogleApiSourceRequest.
    	}
    	op, err := c.UpdateGoogleApiSource(ctx, req)
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
    

### func (*Client) UpdateGoogleApiSourceOperation 
    
    
    func (c *Client) UpdateGoogleApiSourceOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateGoogleApiSourceOperation

UpdateGoogleApiSourceOperation returns a new UpdateGoogleApiSourceOperation from a given name. The name must be that of a previously created UpdateGoogleApiSourceOperation, possibly from a different process.

### func (*Client) UpdateGoogleChannelConfig 
    
    
    func (c *Client) UpdateGoogleChannelConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdateGoogleChannelConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdateGoogleChannelConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleChannelConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleChannelConfig), [error](https://pkg.go.dev/builtin#error))

UpdateGoogleChannelConfig update a single GoogleChannelConfig

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdateGoogleChannelConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdateGoogleChannelConfigRequest.
    	}
    	resp, err := c.UpdateGoogleChannelConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateMessageBus 
    
    
    func (c *Client) UpdateMessageBus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdateMessageBusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdateMessageBusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateMessageBusOperation, [error](https://pkg.go.dev/builtin#error))

UpdateMessageBus update a single message bus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdateMessageBusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdateMessageBusRequest.
    	}
    	op, err := c.UpdateMessageBus(ctx, req)
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
    

### func (*Client) UpdateMessageBusOperation 
    
    
    func (c *Client) UpdateMessageBusOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateMessageBusOperation

UpdateMessageBusOperation returns a new UpdateMessageBusOperation from a given name. The name must be that of a previously created UpdateMessageBusOperation, possibly from a different process.

### func (*Client) UpdatePipeline 
    
    
    func (c *Client) UpdatePipeline(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdatePipelineRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdatePipelineRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdatePipelineOperation, [error](https://pkg.go.dev/builtin#error))

UpdatePipeline update a single pipeline.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdatePipelineRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdatePipelineRequest.
    	}
    	op, err := c.UpdatePipeline(ctx, req)
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
    

### func (*Client) UpdatePipelineOperation 
    
    
    func (c *Client) UpdatePipelineOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdatePipelineOperation

UpdatePipelineOperation returns a new UpdatePipelineOperation from a given name. The name must be that of a previously created UpdatePipelineOperation, possibly from a different process.

### func (*Client) UpdateTrigger 
    
    
    func (c *Client) UpdateTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[UpdateTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_UpdateTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateTriggerOperation, [error](https://pkg.go.dev/builtin#error))

UpdateTrigger update a single trigger.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	eventarc "cloud.google.com/go/eventarc/apiv1"
    	eventarcpb "cloud.google.com/go/eventarc/apiv1/eventarcpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := eventarc.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1.html#cloud_google_com_go_eventarc_apiv1_Client_Close)()
    
    	req := &eventarcpb.UpdateTriggerRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/eventarc/apiv1/eventarcpb#UpdateTriggerRequest.
    	}
    	op, err := c.UpdateTrigger(ctx, req)
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
    

### func (*Client) UpdateTriggerOperation 
    
    
    func (c *Client) UpdateTriggerOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateTriggerOperation

UpdateTriggerOperation returns a new UpdateTriggerOperation from a given name. The name must be that of a previously created UpdateTriggerOperation, possibly from a different process.

## CreateChannelConnectionOperation
    
    
    type CreateChannelConnectionOperation struct {
    	// contains filtered or unexported fields
    }

CreateChannelConnectionOperation manages a long-running operation from CreateChannelConnection.

### func (*CreateChannelConnectionOperation) Done 
    
    
    func (op *CreateChannelConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateChannelConnectionOperation) Metadata 
    
    
    func (op *CreateChannelConnectionOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateChannelConnectionOperation) Name 
    
    
    func (op *CreateChannelConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateChannelConnectionOperation) Poll 
    
    
    func (op *CreateChannelConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ChannelConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ChannelConnection), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateChannelConnectionOperation) Wait 
    
    
    func (op *CreateChannelConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ChannelConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ChannelConnection), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateChannelOperation
    
    
    type CreateChannelOperation struct {
    	// contains filtered or unexported fields
    }

CreateChannelOperation manages a long-running operation from CreateChannel.

### func (*CreateChannelOperation) Done 
    
    
    func (op *CreateChannelOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateChannelOperation) Metadata 
    
    
    func (op *CreateChannelOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateChannelOperation) Name 
    
    
    func (op *CreateChannelOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateChannelOperation) Poll 
    
    
    func (op *CreateChannelOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateChannelOperation) Wait 
    
    
    func (op *CreateChannelOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateEnrollmentOperation
    
    
    type CreateEnrollmentOperation struct {
    	// contains filtered or unexported fields
    }

CreateEnrollmentOperation manages a long-running operation from CreateEnrollment.

### func (*CreateEnrollmentOperation) Done 
    
    
    func (op *CreateEnrollmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateEnrollmentOperation) Metadata 
    
    
    func (op *CreateEnrollmentOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateEnrollmentOperation) Name 
    
    
    func (op *CreateEnrollmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateEnrollmentOperation) Poll 
    
    
    func (op *CreateEnrollmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateEnrollmentOperation) Wait 
    
    
    func (op *CreateEnrollmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateGoogleApiSourceOperation
    
    
    type CreateGoogleApiSourceOperation struct {
    	// contains filtered or unexported fields
    }

CreateGoogleApiSourceOperation manages a long-running operation from CreateGoogleApiSource.

### func (*CreateGoogleApiSourceOperation) Done 
    
    
    func (op *CreateGoogleApiSourceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateGoogleApiSourceOperation) Metadata 
    
    
    func (op *CreateGoogleApiSourceOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateGoogleApiSourceOperation) Name 
    
    
    func (op *CreateGoogleApiSourceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateGoogleApiSourceOperation) Poll 
    
    
    func (op *CreateGoogleApiSourceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateGoogleApiSourceOperation) Wait 
    
    
    func (op *CreateGoogleApiSourceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateMessageBusOperation
    
    
    type CreateMessageBusOperation struct {
    	// contains filtered or unexported fields
    }

CreateMessageBusOperation manages a long-running operation from CreateMessageBus.

### func (*CreateMessageBusOperation) Done 
    
    
    func (op *CreateMessageBusOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateMessageBusOperation) Metadata 
    
    
    func (op *CreateMessageBusOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateMessageBusOperation) Name 
    
    
    func (op *CreateMessageBusOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateMessageBusOperation) Poll 
    
    
    func (op *CreateMessageBusOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateMessageBusOperation) Wait 
    
    
    func (op *CreateMessageBusOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreatePipelineOperation
    
    
    type CreatePipelineOperation struct {
    	// contains filtered or unexported fields
    }

CreatePipelineOperation manages a long-running operation from CreatePipeline.

### func (*CreatePipelineOperation) Done 
    
    
    func (op *CreatePipelineOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreatePipelineOperation) Metadata 
    
    
    func (op *CreatePipelineOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreatePipelineOperation) Name 
    
    
    func (op *CreatePipelineOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreatePipelineOperation) Poll 
    
    
    func (op *CreatePipelineOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreatePipelineOperation) Wait 
    
    
    func (op *CreatePipelineOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateTriggerOperation
    
    
    type CreateTriggerOperation struct {
    	// contains filtered or unexported fields
    }

CreateTriggerOperation manages a long-running operation from CreateTrigger.

### func (*CreateTriggerOperation) Done 
    
    
    func (op *CreateTriggerOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateTriggerOperation) Metadata 
    
    
    func (op *CreateTriggerOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateTriggerOperation) Name 
    
    
    func (op *CreateTriggerOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateTriggerOperation) Poll 
    
    
    func (op *CreateTriggerOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateTriggerOperation) Wait 
    
    
    func (op *CreateTriggerOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteChannelConnectionOperation
    
    
    type DeleteChannelConnectionOperation struct {
    	// contains filtered or unexported fields
    }

DeleteChannelConnectionOperation manages a long-running operation from DeleteChannelConnection.

### func (*DeleteChannelConnectionOperation) Done 
    
    
    func (op *DeleteChannelConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteChannelConnectionOperation) Metadata 
    
    
    func (op *DeleteChannelConnectionOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteChannelConnectionOperation) Name 
    
    
    func (op *DeleteChannelConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteChannelConnectionOperation) Poll 
    
    
    func (op *DeleteChannelConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ChannelConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ChannelConnection), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteChannelConnectionOperation) Wait 
    
    
    func (op *DeleteChannelConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[ChannelConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_ChannelConnection), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteChannelOperation
    
    
    type DeleteChannelOperation struct {
    	// contains filtered or unexported fields
    }

DeleteChannelOperation manages a long-running operation from DeleteChannel.

### func (*DeleteChannelOperation) Done 
    
    
    func (op *DeleteChannelOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteChannelOperation) Metadata 
    
    
    func (op *DeleteChannelOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteChannelOperation) Name 
    
    
    func (op *DeleteChannelOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteChannelOperation) Poll 
    
    
    func (op *DeleteChannelOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteChannelOperation) Wait 
    
    
    func (op *DeleteChannelOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteEnrollmentOperation
    
    
    type DeleteEnrollmentOperation struct {
    	// contains filtered or unexported fields
    }

DeleteEnrollmentOperation manages a long-running operation from DeleteEnrollment.

### func (*DeleteEnrollmentOperation) Done 
    
    
    func (op *DeleteEnrollmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteEnrollmentOperation) Metadata 
    
    
    func (op *DeleteEnrollmentOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteEnrollmentOperation) Name 
    
    
    func (op *DeleteEnrollmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteEnrollmentOperation) Poll 
    
    
    func (op *DeleteEnrollmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteEnrollmentOperation) Wait 
    
    
    func (op *DeleteEnrollmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteGoogleApiSourceOperation
    
    
    type DeleteGoogleApiSourceOperation struct {
    	// contains filtered or unexported fields
    }

DeleteGoogleApiSourceOperation manages a long-running operation from DeleteGoogleApiSource.

### func (*DeleteGoogleApiSourceOperation) Done 
    
    
    func (op *DeleteGoogleApiSourceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteGoogleApiSourceOperation) Metadata 
    
    
    func (op *DeleteGoogleApiSourceOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteGoogleApiSourceOperation) Name 
    
    
    func (op *DeleteGoogleApiSourceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteGoogleApiSourceOperation) Poll 
    
    
    func (op *DeleteGoogleApiSourceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteGoogleApiSourceOperation) Wait 
    
    
    func (op *DeleteGoogleApiSourceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteMessageBusOperation
    
    
    type DeleteMessageBusOperation struct {
    	// contains filtered or unexported fields
    }

DeleteMessageBusOperation manages a long-running operation from DeleteMessageBus.

### func (*DeleteMessageBusOperation) Done 
    
    
    func (op *DeleteMessageBusOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteMessageBusOperation) Metadata 
    
    
    func (op *DeleteMessageBusOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteMessageBusOperation) Name 
    
    
    func (op *DeleteMessageBusOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteMessageBusOperation) Poll 
    
    
    func (op *DeleteMessageBusOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteMessageBusOperation) Wait 
    
    
    func (op *DeleteMessageBusOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeletePipelineOperation
    
    
    type DeletePipelineOperation struct {
    	// contains filtered or unexported fields
    }

DeletePipelineOperation manages a long-running operation from DeletePipeline.

### func (*DeletePipelineOperation) Done 
    
    
    func (op *DeletePipelineOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeletePipelineOperation) Metadata 
    
    
    func (op *DeletePipelineOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeletePipelineOperation) Name 
    
    
    func (op *DeletePipelineOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeletePipelineOperation) Poll 
    
    
    func (op *DeletePipelineOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeletePipelineOperation) Wait 
    
    
    func (op *DeletePipelineOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteTriggerOperation
    
    
    type DeleteTriggerOperation struct {
    	// contains filtered or unexported fields
    }

DeleteTriggerOperation manages a long-running operation from DeleteTrigger.

### func (*DeleteTriggerOperation) Done 
    
    
    func (op *DeleteTriggerOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteTriggerOperation) Metadata 
    
    
    func (op *DeleteTriggerOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteTriggerOperation) Name 
    
    
    func (op *DeleteTriggerOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteTriggerOperation) Poll 
    
    
    func (op *DeleteTriggerOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteTriggerOperation) Wait 
    
    
    func (op *DeleteTriggerOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EnrollmentIterator
    
    
    type EnrollmentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.Enrollment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EnrollmentIterator manages a stream of *eventarcpb.Enrollment.

### func (*EnrollmentIterator) All 
    
    
    func (it *EnrollmentIterator) All() iter.Seq2[*eventarcpb.Enrollment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EnrollmentIterator) Next 
    
    
    func (it *EnrollmentIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EnrollmentIterator) PageInfo 
    
    
    func (it *EnrollmentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoogleApiSourceIterator
    
    
    type GoogleApiSourceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.GoogleApiSource, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoogleApiSourceIterator manages a stream of *eventarcpb.GoogleApiSource.

### func (*GoogleApiSourceIterator) All 
    
    
    func (it *GoogleApiSourceIterator) All() iter.Seq2[*eventarcpb.GoogleApiSource, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoogleApiSourceIterator) Next 
    
    
    func (it *GoogleApiSourceIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoogleApiSourceIterator) PageInfo 
    
    
    func (it *GoogleApiSourceIterator) PageInfo() *iterator.PageInfo

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

## MessageBusIterator
    
    
    type MessageBusIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.MessageBus, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

MessageBusIterator manages a stream of *eventarcpb.MessageBus.

### func (*MessageBusIterator) All 
    
    
    func (it *MessageBusIterator) All() iter.Seq2[*eventarcpb.MessageBus, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*MessageBusIterator) Next 
    
    
    func (it *MessageBusIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*MessageBusIterator) PageInfo 
    
    
    func (it *MessageBusIterator) PageInfo() *iterator.PageInfo

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

## PipelineIterator
    
    
    type PipelineIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.Pipeline, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PipelineIterator manages a stream of *eventarcpb.Pipeline.

### func (*PipelineIterator) All 
    
    
    func (it *PipelineIterator) All() iter.Seq2[*eventarcpb.Pipeline, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PipelineIterator) Next 
    
    
    func (it *PipelineIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PipelineIterator) PageInfo 
    
    
    func (it *PipelineIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ProviderIterator
    
    
    type ProviderIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.Provider, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ProviderIterator manages a stream of *eventarcpb.Provider.

### func (*ProviderIterator) All 
    
    
    func (it *ProviderIterator) All() iter.Seq2[*eventarcpb.Provider, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ProviderIterator) Next 
    
    
    func (it *ProviderIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Provider](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Provider), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ProviderIterator) PageInfo 
    
    
    func (it *ProviderIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## StringIterator
    
    
    type StringIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results [][string](https://pkg.go.dev/builtin#string), nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

StringIterator manages a stream of string.

### func (*StringIterator) All 
    
    
    func (it *StringIterator) All() [iter](https://pkg.go.dev/iter).[Seq2[string, error]](https://pkg.go.dev/iter#Seq2\[string,%20error\])

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*StringIterator) Next 
    
    
    func (it *StringIterator) Next() ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*StringIterator) PageInfo 
    
    
    func (it *StringIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TriggerIterator
    
    
    type TriggerIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*eventarcpb.Trigger, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TriggerIterator manages a stream of *eventarcpb.Trigger.

### func (*TriggerIterator) All 
    
    
    func (it *TriggerIterator) All() iter.Seq2[*eventarcpb.Trigger, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TriggerIterator) Next 
    
    
    func (it *TriggerIterator) Next() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TriggerIterator) PageInfo 
    
    
    func (it *TriggerIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## UpdateChannelOperation
    
    
    type UpdateChannelOperation struct {
    	// contains filtered or unexported fields
    }

UpdateChannelOperation manages a long-running operation from UpdateChannel.

### func (*UpdateChannelOperation) Done 
    
    
    func (op *UpdateChannelOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateChannelOperation) Metadata 
    
    
    func (op *UpdateChannelOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateChannelOperation) Name 
    
    
    func (op *UpdateChannelOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateChannelOperation) Poll 
    
    
    func (op *UpdateChannelOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateChannelOperation) Wait 
    
    
    func (op *UpdateChannelOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Channel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Channel), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateEnrollmentOperation
    
    
    type UpdateEnrollmentOperation struct {
    	// contains filtered or unexported fields
    }

UpdateEnrollmentOperation manages a long-running operation from UpdateEnrollment.

### func (*UpdateEnrollmentOperation) Done 
    
    
    func (op *UpdateEnrollmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateEnrollmentOperation) Metadata 
    
    
    func (op *UpdateEnrollmentOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateEnrollmentOperation) Name 
    
    
    func (op *UpdateEnrollmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateEnrollmentOperation) Poll 
    
    
    func (op *UpdateEnrollmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateEnrollmentOperation) Wait 
    
    
    func (op *UpdateEnrollmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Enrollment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Enrollment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateGoogleApiSourceOperation
    
    
    type UpdateGoogleApiSourceOperation struct {
    	// contains filtered or unexported fields
    }

UpdateGoogleApiSourceOperation manages a long-running operation from UpdateGoogleApiSource.

### func (*UpdateGoogleApiSourceOperation) Done 
    
    
    func (op *UpdateGoogleApiSourceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateGoogleApiSourceOperation) Metadata 
    
    
    func (op *UpdateGoogleApiSourceOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateGoogleApiSourceOperation) Name 
    
    
    func (op *UpdateGoogleApiSourceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateGoogleApiSourceOperation) Poll 
    
    
    func (op *UpdateGoogleApiSourceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateGoogleApiSourceOperation) Wait 
    
    
    func (op *UpdateGoogleApiSourceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[GoogleApiSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_GoogleApiSource), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateMessageBusOperation
    
    
    type UpdateMessageBusOperation struct {
    	// contains filtered or unexported fields
    }

UpdateMessageBusOperation manages a long-running operation from UpdateMessageBus.

### func (*UpdateMessageBusOperation) Done 
    
    
    func (op *UpdateMessageBusOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateMessageBusOperation) Metadata 
    
    
    func (op *UpdateMessageBusOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateMessageBusOperation) Name 
    
    
    func (op *UpdateMessageBusOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateMessageBusOperation) Poll 
    
    
    func (op *UpdateMessageBusOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateMessageBusOperation) Wait 
    
    
    func (op *UpdateMessageBusOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[MessageBus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_MessageBus), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdatePipelineOperation
    
    
    type UpdatePipelineOperation struct {
    	// contains filtered or unexported fields
    }

UpdatePipelineOperation manages a long-running operation from UpdatePipeline.

### func (*UpdatePipelineOperation) Done 
    
    
    func (op *UpdatePipelineOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdatePipelineOperation) Metadata 
    
    
    func (op *UpdatePipelineOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdatePipelineOperation) Name 
    
    
    func (op *UpdatePipelineOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdatePipelineOperation) Poll 
    
    
    func (op *UpdatePipelineOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdatePipelineOperation) Wait 
    
    
    func (op *UpdatePipelineOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Pipeline](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Pipeline), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateTriggerOperation
    
    
    type UpdateTriggerOperation struct {
    	// contains filtered or unexported fields
    }

UpdateTriggerOperation manages a long-running operation from UpdateTrigger.

### func (*UpdateTriggerOperation) Done 
    
    
    func (op *UpdateTriggerOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateTriggerOperation) Metadata 
    
    
    func (op *UpdateTriggerOperation) Metadata() (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateTriggerOperation) Name 
    
    
    func (op *UpdateTriggerOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateTriggerOperation) Poll 
    
    
    func (op *UpdateTriggerOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateTriggerOperation) Wait 
    
    
    func (op *UpdateTriggerOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[eventarcpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb).[Trigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/eventarc/latest/apiv1/eventarcpb#cloud_google_com_go_eventarc_apiv1_eventarcpb_Trigger), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
