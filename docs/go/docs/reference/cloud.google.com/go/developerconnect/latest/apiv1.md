---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/
title: Developer Connect API v1 - Package cloud.google.com/go/developerconnect/apiv1 (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:46.678098+00:00
---

# Developer Connect API v1 - Package cloud.google.com/go/developerconnect/apiv1 (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Developer Connect API v1 - Package cloud.google.com/go/developerconnect/apiv1 (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.3  0.2.2  0.1.4 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1). 

Package developerconnect is an auto-generated package for the Developer Connect API. 

## Connect third-party source code management to Google

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/developerconnect/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := developerconnect.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &developerconnectpb.CreateAccountConnectorRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#CreateAccountConnectorRequest.
    }
    op, err := c.CreateAccountConnector(ctx, req)
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

## AccountConnectorIterator
    
    
    type AccountConnectorIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.AccountConnector, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AccountConnectorIterator manages a stream of *developerconnectpb.AccountConnector.

### func (*AccountConnectorIterator) All 
    
    
    func (it *AccountConnectorIterator) All() iter.Seq2[*developerconnectpb.AccountConnector, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AccountConnectorIterator) Next 
    
    
    func (it *AccountConnectorIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[AccountConnector](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_AccountConnector), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AccountConnectorIterator) PageInfo 
    
    
    func (it *AccountConnectorIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CallOptions
    
    
    type CallOptions struct {
    	ListConnections              []gax.CallOption
    	GetConnection                []gax.CallOption
    	CreateConnection             []gax.CallOption
    	UpdateConnection             []gax.CallOption
    	DeleteConnection             []gax.CallOption
    	CreateGitRepositoryLink      []gax.CallOption
    	DeleteGitRepositoryLink      []gax.CallOption
    	ListGitRepositoryLinks       []gax.CallOption
    	GetGitRepositoryLink         []gax.CallOption
    	FetchReadWriteToken          []gax.CallOption
    	FetchReadToken               []gax.CallOption
    	FetchLinkableGitRepositories []gax.CallOption
    	FetchGitHubInstallations     []gax.CallOption
    	FetchGitRefs                 []gax.CallOption
    	ListAccountConnectors        []gax.CallOption
    	GetAccountConnector          []gax.CallOption
    	CreateAccountConnector       []gax.CallOption
    	UpdateAccountConnector       []gax.CallOption
    	DeleteAccountConnector       []gax.CallOption
    	FetchAccessToken             []gax.CallOption
    	ListUsers                    []gax.CallOption
    	DeleteUser                   []gax.CallOption
    	FetchSelf                    []gax.CallOption
    	DeleteSelf                   []gax.CallOption
    	StartOAuth                   []gax.CallOption
    	FinishOAuth                  []gax.CallOption
    	GetLocation                  []gax.CallOption
    	ListLocations                []gax.CallOption
    	CancelOperation              []gax.CallOption
    	DeleteOperation              []gax.CallOption
    	GetOperation                 []gax.CallOption
    	ListOperations               []gax.CallOption
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

Client is a client for interacting with Developer Connect API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service describing handlers for resources

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new developer connect client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service describing handlers for resources

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new developer connect rest client.

Service describing handlers for resources

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) CreateAccountConnector 
    
    
    func (c *Client) CreateAccountConnector(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[CreateAccountConnectorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_CreateAccountConnectorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateAccountConnectorOperation, [error](https://pkg.go.dev/builtin#error))

CreateAccountConnector creates a new AccountConnector in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.CreateAccountConnectorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#CreateAccountConnectorRequest.
    	}
    	op, err := c.CreateAccountConnector(ctx, req)
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
    

### func (*Client) CreateAccountConnectorOperation 
    
    
    func (c *Client) CreateAccountConnectorOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateAccountConnectorOperation

CreateAccountConnectorOperation returns a new CreateAccountConnectorOperation from a given name. The name must be that of a previously created CreateAccountConnectorOperation, possibly from a different process.

### func (*Client) CreateConnection 
    
    
    func (c *Client) CreateConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[CreateConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_CreateConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateConnectionOperation, [error](https://pkg.go.dev/builtin#error))

CreateConnection creates a new Connection in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.CreateConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#CreateConnectionRequest.
    	}
    	op, err := c.CreateConnection(ctx, req)
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
    

### func (*Client) CreateConnectionOperation 
    
    
    func (c *Client) CreateConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateConnectionOperation

CreateConnectionOperation returns a new CreateConnectionOperation from a given name. The name must be that of a previously created CreateConnectionOperation, possibly from a different process.

### func (*Client) CreateGitRepositoryLink 
    
    
    func (c *Client) CreateGitRepositoryLink(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[CreateGitRepositoryLinkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_CreateGitRepositoryLinkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateGitRepositoryLinkOperation, [error](https://pkg.go.dev/builtin#error))

CreateGitRepositoryLink creates a GitRepositoryLink. Upon linking a Git Repository, Developer Connect will configure the Git Repository to send webhook events to Developer Connect. Connections that use Firebase GitHub Application will have events forwarded to the Firebase service. Connections that use Gemini Code Assist will have events forwarded to Gemini Code Assist service. All other Connections will have events forwarded to Cloud Build.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.CreateGitRepositoryLinkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#CreateGitRepositoryLinkRequest.
    	}
    	op, err := c.CreateGitRepositoryLink(ctx, req)
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
    

### func (*Client) CreateGitRepositoryLinkOperation 
    
    
    func (c *Client) CreateGitRepositoryLinkOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateGitRepositoryLinkOperation

CreateGitRepositoryLinkOperation returns a new CreateGitRepositoryLinkOperation from a given name. The name must be that of a previously created CreateGitRepositoryLinkOperation, possibly from a different process.

### func (*Client) DeleteAccountConnector 
    
    
    func (c *Client) DeleteAccountConnector(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeleteAccountConnectorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeleteAccountConnectorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteAccountConnectorOperation, [error](https://pkg.go.dev/builtin#error))

DeleteAccountConnector deletes a single AccountConnector.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.DeleteAccountConnectorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#DeleteAccountConnectorRequest.
    	}
    	op, err := c.DeleteAccountConnector(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteAccountConnectorOperation 
    
    
    func (c *Client) DeleteAccountConnectorOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteAccountConnectorOperation

DeleteAccountConnectorOperation returns a new DeleteAccountConnectorOperation from a given name. The name must be that of a previously created DeleteAccountConnectorOperation, possibly from a different process.

### func (*Client) DeleteConnection 
    
    
    func (c *Client) DeleteConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeleteConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeleteConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteConnectionOperation, [error](https://pkg.go.dev/builtin#error))

DeleteConnection deletes a single Connection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.DeleteConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#DeleteConnectionRequest.
    	}
    	op, err := c.DeleteConnection(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteConnectionOperation 
    
    
    func (c *Client) DeleteConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteConnectionOperation

DeleteConnectionOperation returns a new DeleteConnectionOperation from a given name. The name must be that of a previously created DeleteConnectionOperation, possibly from a different process.

### func (*Client) DeleteGitRepositoryLink 
    
    
    func (c *Client) DeleteGitRepositoryLink(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeleteGitRepositoryLinkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeleteGitRepositoryLinkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteGitRepositoryLinkOperation, [error](https://pkg.go.dev/builtin#error))

DeleteGitRepositoryLink deletes a single GitRepositoryLink.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.DeleteGitRepositoryLinkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#DeleteGitRepositoryLinkRequest.
    	}
    	op, err := c.DeleteGitRepositoryLink(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteGitRepositoryLinkOperation 
    
    
    func (c *Client) DeleteGitRepositoryLinkOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteGitRepositoryLinkOperation

DeleteGitRepositoryLinkOperation returns a new DeleteGitRepositoryLinkOperation from a given name. The name must be that of a previously created DeleteGitRepositoryLinkOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteSelf 
    
    
    func (c *Client) DeleteSelf(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeleteSelfRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeleteSelfRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteSelfOperation, [error](https://pkg.go.dev/builtin#error))

DeleteSelf delete the User based on the user credentials.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.DeleteSelfRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#DeleteSelfRequest.
    	}
    	op, err := c.DeleteSelf(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteSelfOperation 
    
    
    func (c *Client) DeleteSelfOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteSelfOperation

DeleteSelfOperation returns a new DeleteSelfOperation from a given name. The name must be that of a previously created DeleteSelfOperation, possibly from a different process.

### func (*Client) DeleteUser 
    
    
    func (c *Client) DeleteUser(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeleteUserRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeleteUserRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteUserOperation, [error](https://pkg.go.dev/builtin#error))

DeleteUser deletes a single User.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.DeleteUserRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#DeleteUserRequest.
    	}
    	op, err := c.DeleteUser(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteUserOperation 
    
    
    func (c *Client) DeleteUserOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteUserOperation

DeleteUserOperation returns a new DeleteUserOperation from a given name. The name must be that of a previously created DeleteUserOperation, possibly from a different process.

### func (*Client) FetchAccessToken 
    
    
    func (c *Client) FetchAccessToken(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchAccessTokenRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchAccessTokenRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchAccessTokenResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchAccessTokenResponse), [error](https://pkg.go.dev/builtin#error))

FetchAccessToken fetches OAuth access token based on end user credentials.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchAccessTokenRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchAccessTokenRequest.
    	}
    	resp, err := c.FetchAccessToken(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchGitHubInstallations 
    
    
    func (c *Client) FetchGitHubInstallations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchGitHubInstallationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchGitHubInstallationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchGitHubInstallationsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchGitHubInstallationsResponse), [error](https://pkg.go.dev/builtin#error))

FetchGitHubInstallations fetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection. For github.com (at <http://github.com>), only installations accessible to the authorizer token are returned. For GitHub Enterprise, all installations are returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchGitHubInstallationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchGitHubInstallationsRequest.
    	}
    	resp, err := c.FetchGitHubInstallations(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchGitRefs 
    
    
    func (c *Client) FetchGitRefs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchGitRefsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchGitRefsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *StringIterator

FetchGitRefs fetch the list of branches or tags for a given repository.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchGitRefsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchGitRefsRequest.
    	}
    	it := c.FetchGitRefs(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.FetchGitRefsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchGitRefsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchGitRefsRequest.
    	}
    	for resp, err := range c.FetchGitRefs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) FetchLinkableGitRepositories 
    
    
    func (c *Client) FetchLinkableGitRepositories(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchLinkableGitRepositoriesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchLinkableGitRepositoriesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LinkableGitRepositoryIterator

FetchLinkableGitRepositories fetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchLinkableGitRepositoriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchLinkableGitRepositoriesRequest.
    	}
    	it := c.FetchLinkableGitRepositories(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.FetchLinkableGitRepositoriesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchLinkableGitRepositoriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchLinkableGitRepositoriesRequest.
    	}
    	for resp, err := range c.FetchLinkableGitRepositories(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) FetchReadToken 
    
    
    func (c *Client) FetchReadToken(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchReadTokenRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchReadTokenRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchReadTokenResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchReadTokenResponse), [error](https://pkg.go.dev/builtin#error))

FetchReadToken fetches read token of a given gitRepositoryLink.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchReadTokenRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchReadTokenRequest.
    	}
    	resp, err := c.FetchReadToken(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchReadWriteToken 
    
    
    func (c *Client) FetchReadWriteToken(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchReadWriteTokenRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchReadWriteTokenRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchReadWriteTokenResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchReadWriteTokenResponse), [error](https://pkg.go.dev/builtin#error))

FetchReadWriteToken fetches read/write token of a given gitRepositoryLink.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchReadWriteTokenRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchReadWriteTokenRequest.
    	}
    	resp, err := c.FetchReadWriteToken(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchSelf 
    
    
    func (c *Client) FetchSelf(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FetchSelfRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FetchSelfRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[User](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_User), [error](https://pkg.go.dev/builtin#error))

FetchSelf fetch the User based on the user credentials.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FetchSelfRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FetchSelfRequest.
    	}
    	resp, err := c.FetchSelf(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FinishOAuth 
    
    
    func (c *Client) FinishOAuth(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FinishOAuthRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FinishOAuthRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[FinishOAuthResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_FinishOAuthResponse), [error](https://pkg.go.dev/builtin#error))

FinishOAuth finishes OAuth flow for an account connector.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.FinishOAuthRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#FinishOAuthRequest.
    	}
    	resp, err := c.FinishOAuth(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetAccountConnector 
    
    
    func (c *Client) GetAccountConnector(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GetAccountConnectorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GetAccountConnectorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[AccountConnector](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_AccountConnector), [error](https://pkg.go.dev/builtin#error))

GetAccountConnector gets details of a single AccountConnector.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.GetAccountConnectorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#GetAccountConnectorRequest.
    	}
    	resp, err := c.GetAccountConnector(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetConnection 
    
    
    func (c *Client) GetConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GetConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GetConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[Connection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_Connection), [error](https://pkg.go.dev/builtin#error))

GetConnection gets details of a single Connection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.GetConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#GetConnectionRequest.
    	}
    	resp, err := c.GetConnection(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGitRepositoryLink 
    
    
    func (c *Client) GetGitRepositoryLink(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GetGitRepositoryLinkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GetGitRepositoryLinkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GitRepositoryLink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GitRepositoryLink), [error](https://pkg.go.dev/builtin#error))

GetGitRepositoryLink gets details of a single GitRepositoryLink.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.GetGitRepositoryLinkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#GetGitRepositoryLinkRequest.
    	}
    	resp, err := c.GetGitRepositoryLink(ctx, req)
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    

### func (*Client) GetOperation 
    
    
    func (c *Client) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    

### func (*Client) ListAccountConnectors 
    
    
    func (c *Client) ListAccountConnectors(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[ListAccountConnectorsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_ListAccountConnectorsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AccountConnectorIterator

ListAccountConnectors lists AccountConnectors in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListAccountConnectorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListAccountConnectorsRequest.
    	}
    	it := c.ListAccountConnectors(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.ListAccountConnectorsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListAccountConnectorsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListAccountConnectorsRequest.
    	}
    	for resp, err := range c.ListAccountConnectors(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListConnections 
    
    
    func (c *Client) ListConnections(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[ListConnectionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_ListConnectionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ConnectionIterator

ListConnections lists Connections in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListConnectionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListConnectionsRequest.
    	}
    	it := c.ListConnections(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.ListConnectionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListConnectionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListConnectionsRequest.
    	}
    	for resp, err := range c.ListConnections(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGitRepositoryLinks 
    
    
    func (c *Client) ListGitRepositoryLinks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[ListGitRepositoryLinksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_ListGitRepositoryLinksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GitRepositoryLinkIterator

ListGitRepositoryLinks lists GitRepositoryLinks in a given project, location, and connection.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListGitRepositoryLinksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListGitRepositoryLinksRequest.
    	}
    	it := c.ListGitRepositoryLinks(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.ListGitRepositoryLinksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListGitRepositoryLinksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListGitRepositoryLinksRequest.
    	}
    	for resp, err := range c.ListGitRepositoryLinks(ctx, req).All() {
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
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
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    

### func (*Client) ListOperations 
    
    
    func (c *Client) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
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
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
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
    

### func (*Client) ListUsers 
    
    
    func (c *Client) ListUsers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[ListUsersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_ListUsersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *UserIterator

ListUsers lists Users in a given project, location, and account_connector.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListUsersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListUsersRequest.
    	}
    	it := c.ListUsers(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.ListUsersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListUsersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListUsersRequest.
    	}
    	for resp, err := range c.ListUsers(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) StartOAuth 
    
    
    func (c *Client) StartOAuth(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[StartOAuthRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_StartOAuthRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[StartOAuthResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_StartOAuthResponse), [error](https://pkg.go.dev/builtin#error))

StartOAuth starts OAuth flow for an account connector.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.StartOAuthRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#StartOAuthRequest.
    	}
    	resp, err := c.StartOAuth(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateAccountConnector 
    
    
    func (c *Client) UpdateAccountConnector(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[UpdateAccountConnectorRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_UpdateAccountConnectorRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateAccountConnectorOperation, [error](https://pkg.go.dev/builtin#error))

UpdateAccountConnector updates the parameters of a single AccountConnector.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.UpdateAccountConnectorRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#UpdateAccountConnectorRequest.
    	}
    	op, err := c.UpdateAccountConnector(ctx, req)
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
    

### func (*Client) UpdateAccountConnectorOperation 
    
    
    func (c *Client) UpdateAccountConnectorOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateAccountConnectorOperation

UpdateAccountConnectorOperation returns a new UpdateAccountConnectorOperation from a given name. The name must be that of a previously created UpdateAccountConnectorOperation, possibly from a different process.

### func (*Client) UpdateConnection 
    
    
    func (c *Client) UpdateConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[UpdateConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_UpdateConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateConnectionOperation, [error](https://pkg.go.dev/builtin#error))

UpdateConnection updates the parameters of a single Connection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.UpdateConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#UpdateConnectionRequest.
    	}
    	op, err := c.UpdateConnection(ctx, req)
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
    

### func (*Client) UpdateConnectionOperation 
    
    
    func (c *Client) UpdateConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateConnectionOperation

UpdateConnectionOperation returns a new UpdateConnectionOperation from a given name. The name must be that of a previously created UpdateConnectionOperation, possibly from a different process.

## ConnectionIterator
    
    
    type ConnectionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.Connection, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ConnectionIterator manages a stream of *developerconnectpb.Connection.

### func (*ConnectionIterator) All 
    
    
    func (it *ConnectionIterator) All() iter.Seq2[*developerconnectpb.Connection, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ConnectionIterator) Next 
    
    
    func (it *ConnectionIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[Connection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_Connection), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ConnectionIterator) PageInfo 
    
    
    func (it *ConnectionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CreateAccountConnectorOperation
    
    
    type CreateAccountConnectorOperation struct {
    	// contains filtered or unexported fields
    }

CreateAccountConnectorOperation manages a long-running operation from CreateAccountConnector.

### func (*CreateAccountConnectorOperation) Done 
    
    
    func (op *CreateAccountConnectorOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateAccountConnectorOperation) Metadata 
    
    
    func (op *CreateAccountConnectorOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateAccountConnectorOperation) Name 
    
    
    func (op *CreateAccountConnectorOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateAccountConnectorOperation) Poll 
    
    
    func (op *CreateAccountConnectorOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[AccountConnector](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_AccountConnector), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateAccountConnectorOperation) Wait 
    
    
    func (op *CreateAccountConnectorOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[AccountConnector](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_AccountConnector), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateConnectionOperation
    
    
    type CreateConnectionOperation struct {
    	// contains filtered or unexported fields
    }

CreateConnectionOperation manages a long-running operation from CreateConnection.

### func (*CreateConnectionOperation) Done 
    
    
    func (op *CreateConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateConnectionOperation) Metadata 
    
    
    func (op *CreateConnectionOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateConnectionOperation) Name 
    
    
    func (op *CreateConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateConnectionOperation) Poll 
    
    
    func (op *CreateConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[Connection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_Connection), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateConnectionOperation) Wait 
    
    
    func (op *CreateConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[Connection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_Connection), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateGitRepositoryLinkOperation
    
    
    type CreateGitRepositoryLinkOperation struct {
    	// contains filtered or unexported fields
    }

CreateGitRepositoryLinkOperation manages a long-running operation from CreateGitRepositoryLink.

### func (*CreateGitRepositoryLinkOperation) Done 
    
    
    func (op *CreateGitRepositoryLinkOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateGitRepositoryLinkOperation) Metadata 
    
    
    func (op *CreateGitRepositoryLinkOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateGitRepositoryLinkOperation) Name 
    
    
    func (op *CreateGitRepositoryLinkOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateGitRepositoryLinkOperation) Poll 
    
    
    func (op *CreateGitRepositoryLinkOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GitRepositoryLink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GitRepositoryLink), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateGitRepositoryLinkOperation) Wait 
    
    
    func (op *CreateGitRepositoryLinkOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GitRepositoryLink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GitRepositoryLink), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateInsightsConfigOperation
    
    
    type CreateInsightsConfigOperation struct {
    	// contains filtered or unexported fields
    }

CreateInsightsConfigOperation manages a long-running operation from CreateInsightsConfig.

### func (*CreateInsightsConfigOperation) Done 
    
    
    func (op *CreateInsightsConfigOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateInsightsConfigOperation) Metadata 
    
    
    func (op *CreateInsightsConfigOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateInsightsConfigOperation) Name 
    
    
    func (op *CreateInsightsConfigOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateInsightsConfigOperation) Poll 
    
    
    func (op *CreateInsightsConfigOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[InsightsConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_InsightsConfig), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateInsightsConfigOperation) Wait 
    
    
    func (op *CreateInsightsConfigOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[InsightsConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_InsightsConfig), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteAccountConnectorOperation
    
    
    type DeleteAccountConnectorOperation struct {
    	// contains filtered or unexported fields
    }

DeleteAccountConnectorOperation manages a long-running operation from DeleteAccountConnector.

### func (*DeleteAccountConnectorOperation) Done 
    
    
    func (op *DeleteAccountConnectorOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteAccountConnectorOperation) Metadata 
    
    
    func (op *DeleteAccountConnectorOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteAccountConnectorOperation) Name 
    
    
    func (op *DeleteAccountConnectorOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteAccountConnectorOperation) Poll 
    
    
    func (op *DeleteAccountConnectorOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteAccountConnectorOperation) Wait 
    
    
    func (op *DeleteAccountConnectorOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteConnectionOperation
    
    
    type DeleteConnectionOperation struct {
    	// contains filtered or unexported fields
    }

DeleteConnectionOperation manages a long-running operation from DeleteConnection.

### func (*DeleteConnectionOperation) Done 
    
    
    func (op *DeleteConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteConnectionOperation) Metadata 
    
    
    func (op *DeleteConnectionOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteConnectionOperation) Name 
    
    
    func (op *DeleteConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteConnectionOperation) Poll 
    
    
    func (op *DeleteConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteConnectionOperation) Wait 
    
    
    func (op *DeleteConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteGitRepositoryLinkOperation
    
    
    type DeleteGitRepositoryLinkOperation struct {
    	// contains filtered or unexported fields
    }

DeleteGitRepositoryLinkOperation manages a long-running operation from DeleteGitRepositoryLink.

### func (*DeleteGitRepositoryLinkOperation) Done 
    
    
    func (op *DeleteGitRepositoryLinkOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteGitRepositoryLinkOperation) Metadata 
    
    
    func (op *DeleteGitRepositoryLinkOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteGitRepositoryLinkOperation) Name 
    
    
    func (op *DeleteGitRepositoryLinkOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteGitRepositoryLinkOperation) Poll 
    
    
    func (op *DeleteGitRepositoryLinkOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteGitRepositoryLinkOperation) Wait 
    
    
    func (op *DeleteGitRepositoryLinkOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteInsightsConfigOperation
    
    
    type DeleteInsightsConfigOperation struct {
    	// contains filtered or unexported fields
    }

DeleteInsightsConfigOperation manages a long-running operation from DeleteInsightsConfig.

### func (*DeleteInsightsConfigOperation) Done 
    
    
    func (op *DeleteInsightsConfigOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteInsightsConfigOperation) Metadata 
    
    
    func (op *DeleteInsightsConfigOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteInsightsConfigOperation) Name 
    
    
    func (op *DeleteInsightsConfigOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteInsightsConfigOperation) Poll 
    
    
    func (op *DeleteInsightsConfigOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteInsightsConfigOperation) Wait 
    
    
    func (op *DeleteInsightsConfigOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteSelfOperation
    
    
    type DeleteSelfOperation struct {
    	// contains filtered or unexported fields
    }

DeleteSelfOperation manages a long-running operation from DeleteSelf.

### func (*DeleteSelfOperation) Done 
    
    
    func (op *DeleteSelfOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteSelfOperation) Metadata 
    
    
    func (op *DeleteSelfOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteSelfOperation) Name 
    
    
    func (op *DeleteSelfOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteSelfOperation) Poll 
    
    
    func (op *DeleteSelfOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteSelfOperation) Wait 
    
    
    func (op *DeleteSelfOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteUserOperation
    
    
    type DeleteUserOperation struct {
    	// contains filtered or unexported fields
    }

DeleteUserOperation manages a long-running operation from DeleteUser.

### func (*DeleteUserOperation) Done 
    
    
    func (op *DeleteUserOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteUserOperation) Metadata 
    
    
    func (op *DeleteUserOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteUserOperation) Name 
    
    
    func (op *DeleteUserOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteUserOperation) Poll 
    
    
    func (op *DeleteUserOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteUserOperation) Wait 
    
    
    func (op *DeleteUserOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeploymentEventIterator
    
    
    type DeploymentEventIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.DeploymentEvent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DeploymentEventIterator manages a stream of *developerconnectpb.DeploymentEvent.

### func (*DeploymentEventIterator) All 
    
    
    func (it *DeploymentEventIterator) All() iter.Seq2[*developerconnectpb.DeploymentEvent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DeploymentEventIterator) Next 
    
    
    func (it *DeploymentEventIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeploymentEvent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeploymentEvent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DeploymentEventIterator) PageInfo 
    
    
    func (it *DeploymentEventIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GitRepositoryLinkIterator
    
    
    type GitRepositoryLinkIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.GitRepositoryLink, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GitRepositoryLinkIterator manages a stream of *developerconnectpb.GitRepositoryLink.

### func (*GitRepositoryLinkIterator) All 
    
    
    func (it *GitRepositoryLinkIterator) All() iter.Seq2[*developerconnectpb.GitRepositoryLink, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GitRepositoryLinkIterator) Next 
    
    
    func (it *GitRepositoryLinkIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GitRepositoryLink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GitRepositoryLink), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GitRepositoryLinkIterator) PageInfo 
    
    
    func (it *GitRepositoryLinkIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## InsightsConfigCallOptions
    
    
    type InsightsConfigCallOptions struct {
    	ListInsightsConfigs  []gax.CallOption
    	CreateInsightsConfig []gax.CallOption
    	GetInsightsConfig    []gax.CallOption
    	UpdateInsightsConfig []gax.CallOption
    	DeleteInsightsConfig []gax.CallOption
    	GetDeploymentEvent   []gax.CallOption
    	ListDeploymentEvents []gax.CallOption
    	GetLocation          []gax.CallOption
    	ListLocations        []gax.CallOption
    	CancelOperation      []gax.CallOption
    	DeleteOperation      []gax.CallOption
    	GetOperation         []gax.CallOption
    	ListOperations       []gax.CallOption
    }

InsightsConfigCallOptions contains the retry settings for each method of InsightsConfigClient.

## InsightsConfigClient
    
    
    type InsightsConfigClient struct {
    
    	// The call options for this service.
    	CallOptions *InsightsConfigCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

InsightsConfigClient is a client for interacting with Developer Connect API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Creates and manages InsightsConfigs.

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them. A user can create an InsightsConfig, list previously-requested InsightsConfigs or get InsightsConfigs by their ID to determine the status of the InsightsConfig.

### func NewInsightsConfigClient 
    
    
    func NewInsightsConfigClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*InsightsConfigClient, [error](https://pkg.go.dev/builtin#error))

NewInsightsConfigClient creates a new insights config service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Creates and manages InsightsConfigs.

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them. A user can create an InsightsConfig, list previously-requested InsightsConfigs or get InsightsConfigs by their ID to determine the status of the InsightsConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewInsightsConfigRESTClient 
    
    
    func NewInsightsConfigRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*InsightsConfigClient, [error](https://pkg.go.dev/builtin#error))

NewInsightsConfigRESTClient creates a new insights config service rest client.

Creates and manages InsightsConfigs.

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them. A user can create an InsightsConfig, list previously-requested InsightsConfigs or get InsightsConfigs by their ID to determine the status of the InsightsConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*InsightsConfigClient) CancelOperation 
    
    
    func (c *InsightsConfigClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    

### func (*InsightsConfigClient) Close 
    
    
    func (c *InsightsConfigClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*InsightsConfigClient) Connection (deprecated)
    
    
    func (c *InsightsConfigClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*InsightsConfigClient) CreateInsightsConfig 
    
    
    func (c *InsightsConfigClient) CreateInsightsConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[CreateInsightsConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_CreateInsightsConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateInsightsConfigOperation, [error](https://pkg.go.dev/builtin#error))

CreateInsightsConfig creates a new InsightsConfig in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.CreateInsightsConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#CreateInsightsConfigRequest.
    	}
    	op, err := c.CreateInsightsConfig(ctx, req)
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
    

### func (*InsightsConfigClient) CreateInsightsConfigOperation 
    
    
    func (c *InsightsConfigClient) CreateInsightsConfigOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateInsightsConfigOperation

CreateInsightsConfigOperation returns a new CreateInsightsConfigOperation from a given name. The name must be that of a previously created CreateInsightsConfigOperation, possibly from a different process.

### func (*InsightsConfigClient) DeleteInsightsConfig 
    
    
    func (c *InsightsConfigClient) DeleteInsightsConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeleteInsightsConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeleteInsightsConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteInsightsConfigOperation, [error](https://pkg.go.dev/builtin#error))

DeleteInsightsConfig deletes a single Insight.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.DeleteInsightsConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#DeleteInsightsConfigRequest.
    	}
    	op, err := c.DeleteInsightsConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*InsightsConfigClient) DeleteInsightsConfigOperation 
    
    
    func (c *InsightsConfigClient) DeleteInsightsConfigOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteInsightsConfigOperation

DeleteInsightsConfigOperation returns a new DeleteInsightsConfigOperation from a given name. The name must be that of a previously created DeleteInsightsConfigOperation, possibly from a different process.

### func (*InsightsConfigClient) DeleteOperation 
    
    
    func (c *InsightsConfigClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*InsightsConfigClient) GetDeploymentEvent 
    
    
    func (c *InsightsConfigClient) GetDeploymentEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GetDeploymentEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GetDeploymentEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[DeploymentEvent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_DeploymentEvent), [error](https://pkg.go.dev/builtin#error))

GetDeploymentEvent gets a single Deployment Event.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.GetDeploymentEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#GetDeploymentEventRequest.
    	}
    	resp, err := c.GetDeploymentEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*InsightsConfigClient) GetInsightsConfig 
    
    
    func (c *InsightsConfigClient) GetInsightsConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[GetInsightsConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_GetInsightsConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[InsightsConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_InsightsConfig), [error](https://pkg.go.dev/builtin#error))

GetInsightsConfig gets details of a single Insight.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.GetInsightsConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#GetInsightsConfigRequest.
    	}
    	resp, err := c.GetInsightsConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*InsightsConfigClient) GetLocation 
    
    
    func (c *InsightsConfigClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    

### func (*InsightsConfigClient) GetOperation 
    
    
    func (c *InsightsConfigClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    

### func (*InsightsConfigClient) ListDeploymentEvents 
    
    
    func (c *InsightsConfigClient) ListDeploymentEvents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[ListDeploymentEventsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_ListDeploymentEventsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DeploymentEventIterator

ListDeploymentEvents lists Deployment Events in a given insights config.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListDeploymentEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListDeploymentEventsRequest.
    	}
    	it := c.ListDeploymentEvents(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.ListDeploymentEventsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListDeploymentEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListDeploymentEventsRequest.
    	}
    	for resp, err := range c.ListDeploymentEvents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*InsightsConfigClient) ListInsightsConfigs 
    
    
    func (c *InsightsConfigClient) ListInsightsConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[ListInsightsConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_ListInsightsConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *InsightsConfigIterator

ListInsightsConfigs lists InsightsConfigs in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListInsightsConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListInsightsConfigsRequest.
    	}
    	it := c.ListInsightsConfigs(ctx, req)
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
    		_ = it.Response.(*developerconnectpb.ListInsightsConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.ListInsightsConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#ListInsightsConfigsRequest.
    	}
    	for resp, err := range c.ListInsightsConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*InsightsConfigClient) ListLocations 
    
    
    func (c *InsightsConfigClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
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
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    

### func (*InsightsConfigClient) ListOperations 
    
    
    func (c *InsightsConfigClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
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
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
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
    

### func (*InsightsConfigClient) UpdateInsightsConfig 
    
    
    func (c *InsightsConfigClient) UpdateInsightsConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[UpdateInsightsConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_UpdateInsightsConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateInsightsConfigOperation, [error](https://pkg.go.dev/builtin#error))

UpdateInsightsConfig updates the parameters of a single InsightsConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	developerconnect "cloud.google.com/go/developerconnect/apiv1"
    	developerconnectpb "cloud.google.com/go/developerconnect/apiv1/developerconnectpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := developerconnect.[NewInsightsConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1.html#cloud_google_com_go_developerconnect_apiv1_InsightsConfigClient_NewInsightsConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &developerconnectpb.UpdateInsightsConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/developerconnect/apiv1/developerconnectpb#UpdateInsightsConfigRequest.
    	}
    	op, err := c.UpdateInsightsConfig(ctx, req)
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
    

### func (*InsightsConfigClient) UpdateInsightsConfigOperation 
    
    
    func (c *InsightsConfigClient) UpdateInsightsConfigOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateInsightsConfigOperation

UpdateInsightsConfigOperation returns a new UpdateInsightsConfigOperation from a given name. The name must be that of a previously created UpdateInsightsConfigOperation, possibly from a different process.

## InsightsConfigIterator
    
    
    type InsightsConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.InsightsConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

InsightsConfigIterator manages a stream of *developerconnectpb.InsightsConfig.

### func (*InsightsConfigIterator) All 
    
    
    func (it *InsightsConfigIterator) All() iter.Seq2[*developerconnectpb.InsightsConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*InsightsConfigIterator) Next 
    
    
    func (it *InsightsConfigIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[InsightsConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_InsightsConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*InsightsConfigIterator) PageInfo 
    
    
    func (it *InsightsConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## LinkableGitRepositoryIterator
    
    
    type LinkableGitRepositoryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.LinkableGitRepository, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

LinkableGitRepositoryIterator manages a stream of *developerconnectpb.LinkableGitRepository.

### func (*LinkableGitRepositoryIterator) All 
    
    
    func (it *LinkableGitRepositoryIterator) All() iter.Seq2[*developerconnectpb.LinkableGitRepository, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*LinkableGitRepositoryIterator) Next 
    
    
    func (it *LinkableGitRepositoryIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[LinkableGitRepository](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_LinkableGitRepository), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*LinkableGitRepositoryIterator) PageInfo 
    
    
    func (it *LinkableGitRepositoryIterator) PageInfo() *iterator.PageInfo

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

## UpdateAccountConnectorOperation
    
    
    type UpdateAccountConnectorOperation struct {
    	// contains filtered or unexported fields
    }

UpdateAccountConnectorOperation manages a long-running operation from UpdateAccountConnector.

### func (*UpdateAccountConnectorOperation) Done 
    
    
    func (op *UpdateAccountConnectorOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateAccountConnectorOperation) Metadata 
    
    
    func (op *UpdateAccountConnectorOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateAccountConnectorOperation) Name 
    
    
    func (op *UpdateAccountConnectorOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateAccountConnectorOperation) Poll 
    
    
    func (op *UpdateAccountConnectorOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[AccountConnector](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_AccountConnector), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateAccountConnectorOperation) Wait 
    
    
    func (op *UpdateAccountConnectorOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[AccountConnector](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_AccountConnector), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateConnectionOperation
    
    
    type UpdateConnectionOperation struct {
    	// contains filtered or unexported fields
    }

UpdateConnectionOperation manages a long-running operation from UpdateConnection.

### func (*UpdateConnectionOperation) Done 
    
    
    func (op *UpdateConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateConnectionOperation) Metadata 
    
    
    func (op *UpdateConnectionOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateConnectionOperation) Name 
    
    
    func (op *UpdateConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateConnectionOperation) Poll 
    
    
    func (op *UpdateConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[Connection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_Connection), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateConnectionOperation) Wait 
    
    
    func (op *UpdateConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[Connection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_Connection), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateInsightsConfigOperation
    
    
    type UpdateInsightsConfigOperation struct {
    	// contains filtered or unexported fields
    }

UpdateInsightsConfigOperation manages a long-running operation from UpdateInsightsConfig.

### func (*UpdateInsightsConfigOperation) Done 
    
    
    func (op *UpdateInsightsConfigOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateInsightsConfigOperation) Metadata 
    
    
    func (op *UpdateInsightsConfigOperation) Metadata() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateInsightsConfigOperation) Name 
    
    
    func (op *UpdateInsightsConfigOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateInsightsConfigOperation) Poll 
    
    
    func (op *UpdateInsightsConfigOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[InsightsConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_InsightsConfig), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateInsightsConfigOperation) Wait 
    
    
    func (op *UpdateInsightsConfigOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[InsightsConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_InsightsConfig), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UserIterator
    
    
    type UserIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*developerconnectpb.User, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

UserIterator manages a stream of *developerconnectpb.User.

### func (*UserIterator) All 
    
    
    func (it *UserIterator) All() iter.Seq2[*developerconnectpb.User, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*UserIterator) Next 
    
    
    func (it *UserIterator) Next() (*[developerconnectpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb).[User](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/developerconnect/latest/apiv1/developerconnectpb#cloud_google_com_go_developerconnect_apiv1_developerconnectpb_User), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*UserIterator) PageInfo 
    
    
    func (it *UserIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
