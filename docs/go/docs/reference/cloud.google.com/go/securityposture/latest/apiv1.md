---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/
title: Security Posture API v1 - Package cloud.google.com/go/securityposture/apiv1 (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:27.413906+00:00
---

# Security Posture API v1 - Package cloud.google.com/go/securityposture/apiv1 (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Security Posture API v1 - Package cloud.google.com/go/securityposture/apiv1 (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.8 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1). 

Package securityposture is an auto-generated package for the Security Posture API. 

Security Posture is a comprehensive framework of policy sets that empowers organizations to define, assess early, deploy, and monitor their security measures in a unified way and helps simplify governance and reduces administrative toil. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/securityposture/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := securityposture.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &securityposturepb.CreatePostureRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#CreatePostureRequest.
    }
    op, err := c.CreatePosture(ctx, req)
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
    	ListPostures            []gax.CallOption
    	ListPostureRevisions    []gax.CallOption
    	GetPosture              []gax.CallOption
    	CreatePosture           []gax.CallOption
    	UpdatePosture           []gax.CallOption
    	DeletePosture           []gax.CallOption
    	ExtractPosture          []gax.CallOption
    	ListPostureDeployments  []gax.CallOption
    	GetPostureDeployment    []gax.CallOption
    	CreatePostureDeployment []gax.CallOption
    	UpdatePostureDeployment []gax.CallOption
    	DeletePostureDeployment []gax.CallOption
    	ListPostureTemplates    []gax.CallOption
    	GetPostureTemplate      []gax.CallOption
    	GetLocation             []gax.CallOption
    	ListLocations           []gax.CallOption
    	CancelOperation         []gax.CallOption
    	DeleteOperation         []gax.CallOption
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

Client is a client for interacting with Security Posture API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service describing handlers for resources.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new security posture client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service describing handlers for resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new security posture rest client.

Service describing handlers for resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
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
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
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

### func (*Client) CreatePosture 
    
    
    func (c *Client) CreatePosture(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[CreatePostureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_CreatePostureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreatePostureOperation, [error](https://pkg.go.dev/builtin#error))

CreatePosture creates a new Posture resource. If a Posture with the specified name already exists in the specified organization and location, the long running operation returns a ALREADY_EXISTS error.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.CreatePostureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#CreatePostureRequest.
    	}
    	op, err := c.CreatePosture(ctx, req)
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
    

### func (*Client) CreatePostureDeployment 
    
    
    func (c *Client) CreatePostureDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[CreatePostureDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_CreatePostureDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreatePostureDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

CreatePostureDeployment creates a new PostureDeployment in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.CreatePostureDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#CreatePostureDeploymentRequest.
    	}
    	op, err := c.CreatePostureDeployment(ctx, req)
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
    

### func (*Client) CreatePostureDeploymentOperation 
    
    
    func (c *Client) CreatePostureDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreatePostureDeploymentOperation

CreatePostureDeploymentOperation returns a new CreatePostureDeploymentOperation from a given name. The name must be that of a previously created CreatePostureDeploymentOperation, possibly from a different process.

### func (*Client) CreatePostureOperation 
    
    
    func (c *Client) CreatePostureOperation(name [string](https://pkg.go.dev/builtin#string)) *CreatePostureOperation

CreatePostureOperation returns a new CreatePostureOperation from a given name. The name must be that of a previously created CreatePostureOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeletePosture 
    
    
    func (c *Client) DeletePosture(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[DeletePostureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_DeletePostureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeletePostureOperation, [error](https://pkg.go.dev/builtin#error))

DeletePosture deletes all the revisions of a resource. A posture can only be deleted when none of the revisions are deployed to any workload.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.DeletePostureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#DeletePostureRequest.
    	}
    	op, err := c.DeletePosture(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeletePostureDeployment 
    
    
    func (c *Client) DeletePostureDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[DeletePostureDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_DeletePostureDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeletePostureDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

DeletePostureDeployment deletes a single PostureDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.DeletePostureDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#DeletePostureDeploymentRequest.
    	}
    	op, err := c.DeletePostureDeployment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeletePostureDeploymentOperation 
    
    
    func (c *Client) DeletePostureDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *DeletePostureDeploymentOperation

DeletePostureDeploymentOperation returns a new DeletePostureDeploymentOperation from a given name. The name must be that of a previously created DeletePostureDeploymentOperation, possibly from a different process.

### func (*Client) DeletePostureOperation 
    
    
    func (c *Client) DeletePostureOperation(name [string](https://pkg.go.dev/builtin#string)) *DeletePostureOperation

DeletePostureOperation returns a new DeletePostureOperation from a given name. The name must be that of a previously created DeletePostureOperation, possibly from a different process.

### func (*Client) ExtractPosture 
    
    
    func (c *Client) ExtractPosture(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[ExtractPostureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_ExtractPostureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExtractPostureOperation, [error](https://pkg.go.dev/builtin#error))

ExtractPosture extracts existing policies on a workload as a posture. If a Posture on the given workload already exists, the long running operation returns a ALREADY_EXISTS error.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ExtractPostureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ExtractPostureRequest.
    	}
    	op, err := c.ExtractPosture(ctx, req)
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
    

### func (*Client) ExtractPostureOperation 
    
    
    func (c *Client) ExtractPostureOperation(name [string](https://pkg.go.dev/builtin#string)) *ExtractPostureOperation

ExtractPostureOperation returns a new ExtractPostureOperation from a given name. The name must be that of a previously created ExtractPostureOperation, possibly from a different process.

### func (*Client) GetLocation 
    
    
    func (c *Client) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.[GetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_GetLocation)(ctx, req)
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
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
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
    

### func (*Client) GetPosture 
    
    
    func (c *Client) GetPosture(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[GetPostureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_GetPostureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

GetPosture gets a posture in a given organization and location. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the Posture name does not exist. In case revision_id is not provided then the latest Posture revision by UpdateTime is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.GetPostureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#GetPostureRequest.
    	}
    	resp, err := c.GetPosture(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetPostureDeployment 
    
    
    func (c *Client) GetPostureDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[GetPostureDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_GetPostureDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureDeployment), [error](https://pkg.go.dev/builtin#error))

GetPostureDeployment gets details of a single PostureDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.GetPostureDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#GetPostureDeploymentRequest.
    	}
    	resp, err := c.GetPostureDeployment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetPostureTemplate 
    
    
    func (c *Client) GetPostureTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[GetPostureTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_GetPostureTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureTemplate), [error](https://pkg.go.dev/builtin#error))

GetPostureTemplate gets a PostureTemplate. User must provide revision_id to retrieve a specific revision of the resource. NOT_FOUND error is returned if the revision_id or the PostureTemplate name does not exist. In case revision_id is not provided then the PostureTemplate with latest revision_id is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.GetPostureTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#GetPostureTemplateRequest.
    	}
    	resp, err := c.GetPostureTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListLocations 
    
    
    func (c *Client) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
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
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_ListLocations)(ctx, req)
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
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_ListLocations)(ctx, req).All() {
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
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
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
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
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
    

### func (*Client) ListPostureDeployments 
    
    
    func (c *Client) ListPostureDeployments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[ListPostureDeploymentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_ListPostureDeploymentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PostureDeploymentIterator

ListPostureDeployments postureDeployments Lists PostureDeployments in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPostureDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPostureDeploymentsRequest.
    	}
    	it := c.ListPostureDeployments(ctx, req)
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
    		_ = it.Response.(*securityposturepb.ListPostureDeploymentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPostureDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPostureDeploymentsRequest.
    	}
    	for resp, err := range c.ListPostureDeployments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListPostureRevisions 
    
    
    func (c *Client) ListPostureRevisions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[ListPostureRevisionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_ListPostureRevisionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PostureIterator

ListPostureRevisions lists revisions of a Posture in a given organization and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPostureRevisionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPostureRevisionsRequest.
    	}
    	it := c.ListPostureRevisions(ctx, req)
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
    		_ = it.Response.(*securityposturepb.ListPostureRevisionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPostureRevisionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPostureRevisionsRequest.
    	}
    	for resp, err := range c.ListPostureRevisions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListPostureTemplates 
    
    
    func (c *Client) ListPostureTemplates(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[ListPostureTemplatesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_ListPostureTemplatesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PostureTemplateIterator

ListPostureTemplates postureTemplates Lists all the PostureTemplates available to the user.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPostureTemplatesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPostureTemplatesRequest.
    	}
    	it := c.ListPostureTemplates(ctx, req)
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
    		_ = it.Response.(*securityposturepb.ListPostureTemplatesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPostureTemplatesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPostureTemplatesRequest.
    	}
    	for resp, err := range c.ListPostureTemplates(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListPostures 
    
    
    func (c *Client) ListPostures(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[ListPosturesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_ListPosturesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PostureIterator

ListPostures (– This option restricts the visibility of the API to only projects that will (– be labeled as PREVIEW or GOOGLE_INTERNAL by the service. (– option (google.api.api_visibility).restriction = “PREVIEW,GOOGLE_INTERNAL”; Postures Lists Postures in a given organization and location. In case a posture has multiple revisions, the latest revision as per UpdateTime will be returned.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPosturesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPosturesRequest.
    	}
    	it := c.ListPostures(ctx, req)
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
    		_ = it.Response.(*securityposturepb.ListPosturesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.ListPosturesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#ListPosturesRequest.
    	}
    	for resp, err := range c.ListPostures(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) UpdatePosture 
    
    
    func (c *Client) UpdatePosture(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[UpdatePostureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_UpdatePostureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdatePostureOperation, [error](https://pkg.go.dev/builtin#error))

UpdatePosture updates an existing Posture. A new revision of the posture will be created if the revision to be updated is currently deployed on a workload. Returns a google.rpc.Status with google.rpc.Code.NOT_FOUND if the Posture does not exist. Returns a google.rpc.Status with google.rpc.Code.ABORTED if the etag supplied in the request does not match the persisted etag of the Posture. Updatable fields are state, description and policy_sets. State update operation cannot be clubbed with update of description and policy_sets. An ACTIVE posture can be updated to both DRAFT or DEPRECATED states. Postures in DRAFT or DEPRECATED states can only be updated to ACTIVE state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.UpdatePostureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#UpdatePostureRequest.
    	}
    	op, err := c.UpdatePosture(ctx, req)
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
    

### func (*Client) UpdatePostureDeployment 
    
    
    func (c *Client) UpdatePostureDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[UpdatePostureDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_UpdatePostureDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdatePostureDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

UpdatePostureDeployment updates the parameters of a single PostureDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	securityposture "cloud.google.com/go/securityposture/apiv1"
    
    	securityposturepb "cloud.google.com/go/securityposture/apiv1/securityposturepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := securityposture.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1.html#cloud_google_com_go_securityposture_apiv1_Client_Close)()
    
    	req := &securityposturepb.UpdatePostureDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/securityposture/apiv1/securityposturepb#UpdatePostureDeploymentRequest.
    	}
    	op, err := c.UpdatePostureDeployment(ctx, req)
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
    

### func (*Client) UpdatePostureDeploymentOperation 
    
    
    func (c *Client) UpdatePostureDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdatePostureDeploymentOperation

UpdatePostureDeploymentOperation returns a new UpdatePostureDeploymentOperation from a given name. The name must be that of a previously created UpdatePostureDeploymentOperation, possibly from a different process.

### func (*Client) UpdatePostureOperation 
    
    
    func (c *Client) UpdatePostureOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdatePostureOperation

UpdatePostureOperation returns a new UpdatePostureOperation from a given name. The name must be that of a previously created UpdatePostureOperation, possibly from a different process.

## CreatePostureDeploymentOperation
    
    
    type CreatePostureDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

CreatePostureDeploymentOperation manages a long-running operation from CreatePostureDeployment.

### func (*CreatePostureDeploymentOperation) Done 
    
    
    func (op *CreatePostureDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreatePostureDeploymentOperation) Metadata 
    
    
    func (op *CreatePostureDeploymentOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreatePostureDeploymentOperation) Name 
    
    
    func (op *CreatePostureDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreatePostureDeploymentOperation) Poll 
    
    
    func (op *CreatePostureDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureDeployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreatePostureDeploymentOperation) Wait 
    
    
    func (op *CreatePostureDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureDeployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreatePostureOperation
    
    
    type CreatePostureOperation struct {
    	// contains filtered or unexported fields
    }

CreatePostureOperation manages a long-running operation from CreatePosture.

### func (*CreatePostureOperation) Done 
    
    
    func (op *CreatePostureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreatePostureOperation) Metadata 
    
    
    func (op *CreatePostureOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreatePostureOperation) Name 
    
    
    func (op *CreatePostureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreatePostureOperation) Poll 
    
    
    func (op *CreatePostureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreatePostureOperation) Wait 
    
    
    func (op *CreatePostureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeletePostureDeploymentOperation
    
    
    type DeletePostureDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

DeletePostureDeploymentOperation manages a long-running operation from DeletePostureDeployment.

### func (*DeletePostureDeploymentOperation) Done 
    
    
    func (op *DeletePostureDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeletePostureDeploymentOperation) Metadata 
    
    
    func (op *DeletePostureDeploymentOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeletePostureDeploymentOperation) Name 
    
    
    func (op *DeletePostureDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeletePostureDeploymentOperation) Poll 
    
    
    func (op *DeletePostureDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeletePostureDeploymentOperation) Wait 
    
    
    func (op *DeletePostureDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeletePostureOperation
    
    
    type DeletePostureOperation struct {
    	// contains filtered or unexported fields
    }

DeletePostureOperation manages a long-running operation from DeletePosture.

### func (*DeletePostureOperation) Done 
    
    
    func (op *DeletePostureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeletePostureOperation) Metadata 
    
    
    func (op *DeletePostureOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeletePostureOperation) Name 
    
    
    func (op *DeletePostureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeletePostureOperation) Poll 
    
    
    func (op *DeletePostureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeletePostureOperation) Wait 
    
    
    func (op *DeletePostureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExtractPostureOperation
    
    
    type ExtractPostureOperation struct {
    	// contains filtered or unexported fields
    }

ExtractPostureOperation manages a long-running operation from ExtractPosture.

### func (*ExtractPostureOperation) Done 
    
    
    func (op *ExtractPostureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExtractPostureOperation) Metadata 
    
    
    func (op *ExtractPostureOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExtractPostureOperation) Name 
    
    
    func (op *ExtractPostureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExtractPostureOperation) Poll 
    
    
    func (op *ExtractPostureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExtractPostureOperation) Wait 
    
    
    func (op *ExtractPostureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

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

## PostureDeploymentIterator
    
    
    type PostureDeploymentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*securityposturepb.PostureDeployment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PostureDeploymentIterator manages a stream of *securityposturepb.PostureDeployment.

### func (*PostureDeploymentIterator) All 
    
    
    func (it *PostureDeploymentIterator) All() iter.Seq2[*securityposturepb.PostureDeployment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PostureDeploymentIterator) Next 
    
    
    func (it *PostureDeploymentIterator) Next() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureDeployment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PostureDeploymentIterator) PageInfo 
    
    
    func (it *PostureDeploymentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PostureIterator
    
    
    type PostureIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*securityposturepb.Posture, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PostureIterator manages a stream of *securityposturepb.Posture.

### func (*PostureIterator) All 
    
    
    func (it *PostureIterator) All() iter.Seq2[*securityposturepb.Posture, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PostureIterator) Next 
    
    
    func (it *PostureIterator) Next() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PostureIterator) PageInfo 
    
    
    func (it *PostureIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PostureTemplateIterator
    
    
    type PostureTemplateIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*securityposturepb.PostureTemplate, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PostureTemplateIterator manages a stream of *securityposturepb.PostureTemplate.

### func (*PostureTemplateIterator) All 
    
    
    func (it *PostureTemplateIterator) All() iter.Seq2[*securityposturepb.PostureTemplate, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PostureTemplateIterator) Next 
    
    
    func (it *PostureTemplateIterator) Next() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureTemplate), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PostureTemplateIterator) PageInfo 
    
    
    func (it *PostureTemplateIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## UpdatePostureDeploymentOperation
    
    
    type UpdatePostureDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

UpdatePostureDeploymentOperation manages a long-running operation from UpdatePostureDeployment.

### func (*UpdatePostureDeploymentOperation) Done 
    
    
    func (op *UpdatePostureDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdatePostureDeploymentOperation) Metadata 
    
    
    func (op *UpdatePostureDeploymentOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdatePostureDeploymentOperation) Name 
    
    
    func (op *UpdatePostureDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdatePostureDeploymentOperation) Poll 
    
    
    func (op *UpdatePostureDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureDeployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdatePostureDeploymentOperation) Wait 
    
    
    func (op *UpdatePostureDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[PostureDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_PostureDeployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdatePostureOperation
    
    
    type UpdatePostureOperation struct {
    	// contains filtered or unexported fields
    }

UpdatePostureOperation manages a long-running operation from UpdatePosture.

### func (*UpdatePostureOperation) Done 
    
    
    func (op *UpdatePostureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdatePostureOperation) Metadata 
    
    
    func (op *UpdatePostureOperation) Metadata() (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdatePostureOperation) Name 
    
    
    func (op *UpdatePostureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdatePostureOperation) Poll 
    
    
    func (op *UpdatePostureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdatePostureOperation) Wait 
    
    
    func (op *UpdatePostureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[securityposturepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb).[Posture](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securityposture/latest/apiv1/securityposturepb#cloud_google_com_go_securityposture_apiv1_securityposturepb_Posture), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
