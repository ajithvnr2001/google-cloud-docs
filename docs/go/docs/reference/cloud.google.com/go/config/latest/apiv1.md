---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/
title: Infrastructure Manager API v1 - Package cloud.google.com/go/config/apiv1 (v1.14.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:57.413665+00:00
---

# Infrastructure Manager API v1 - Package cloud.google.com/go/config/apiv1 (v1.14.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Infrastructure Manager API v1 - Package cloud.google.com/go/config/apiv1 (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.2  1.2.1  1.1.2  1.0.5  0.4.0  0.3.0  0.2.2  0.1.4 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/config/apiv1). 

Package config is an auto-generated package for the Infrastructure Manager API. 

Creates and manages Google Cloud Platform resources and infrastructure. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/config/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := config.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &configpb.CreateDeploymentRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#CreateDeploymentRequest.
    }
    op, err := c.CreateDeployment(ctx, req)
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
    	ListDeployments              []gax.CallOption
    	GetDeployment                []gax.CallOption
    	CreateDeployment             []gax.CallOption
    	UpdateDeployment             []gax.CallOption
    	DeleteDeployment             []gax.CallOption
    	ListRevisions                []gax.CallOption
    	GetRevision                  []gax.CallOption
    	GetResource                  []gax.CallOption
    	ListResources                []gax.CallOption
    	ExportDeploymentStatefile    []gax.CallOption
    	ExportRevisionStatefile      []gax.CallOption
    	ImportStatefile              []gax.CallOption
    	DeleteStatefile              []gax.CallOption
    	LockDeployment               []gax.CallOption
    	UnlockDeployment             []gax.CallOption
    	ExportLockInfo               []gax.CallOption
    	CreatePreview                []gax.CallOption
    	GetPreview                   []gax.CallOption
    	ListPreviews                 []gax.CallOption
    	DeletePreview                []gax.CallOption
    	ExportPreviewResult          []gax.CallOption
    	ListTerraformVersions        []gax.CallOption
    	GetTerraformVersion          []gax.CallOption
    	ListResourceChanges          []gax.CallOption
    	GetResourceChange            []gax.CallOption
    	ListResourceDrifts           []gax.CallOption
    	GetResourceDrift             []gax.CallOption
    	GetAutoMigrationConfig       []gax.CallOption
    	UpdateAutoMigrationConfig    []gax.CallOption
    	GetDeploymentGroup           []gax.CallOption
    	CreateDeploymentGroup        []gax.CallOption
    	UpdateDeploymentGroup        []gax.CallOption
    	DeleteDeploymentGroup        []gax.CallOption
    	ListDeploymentGroups         []gax.CallOption
    	ProvisionDeploymentGroup     []gax.CallOption
    	DeprovisionDeploymentGroup   []gax.CallOption
    	GetDeploymentGroupRevision   []gax.CallOption
    	ListDeploymentGroupRevisions []gax.CallOption
    	GetLocation                  []gax.CallOption
    	ListLocations                []gax.CallOption
    	GetIamPolicy                 []gax.CallOption
    	SetIamPolicy                 []gax.CallOption
    	TestIamPermissions           []gax.CallOption
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

Client is a client for interacting with Infrastructure Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Infrastructure Manager is a managed service that automates the deployment and management of Google Cloud infrastructure resources.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new config client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Infrastructure Manager is a managed service that automates the deployment and management of Google Cloud infrastructure resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new config rest client.

Infrastructure Manager is a managed service that automates the deployment and management of Google Cloud infrastructure resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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

### func (*Client) CreateDeployment 
    
    
    func (c *Client) CreateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[CreateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_CreateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

CreateDeployment creates a Deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.CreateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#CreateDeploymentRequest.
    	}
    	op, err := c.CreateDeployment(ctx, req)
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
    

### func (*Client) CreateDeploymentGroup 
    
    
    func (c *Client) CreateDeploymentGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[CreateDeploymentGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_CreateDeploymentGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateDeploymentGroupOperation, [error](https://pkg.go.dev/builtin#error))

CreateDeploymentGroup creates a DeploymentGroup The newly created DeploymentGroup will be in the CREATING state and can be retrieved via Get and List calls.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.CreateDeploymentGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#CreateDeploymentGroupRequest.
    	}
    	op, err := c.CreateDeploymentGroup(ctx, req)
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
    

### func (*Client) CreateDeploymentGroupOperation 
    
    
    func (c *Client) CreateDeploymentGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateDeploymentGroupOperation

CreateDeploymentGroupOperation returns a new CreateDeploymentGroupOperation from a given name. The name must be that of a previously created CreateDeploymentGroupOperation, possibly from a different process.

### func (*Client) CreateDeploymentOperation 
    
    
    func (c *Client) CreateDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateDeploymentOperation

CreateDeploymentOperation returns a new CreateDeploymentOperation from a given name. The name must be that of a previously created CreateDeploymentOperation, possibly from a different process.

### func (*Client) CreatePreview 
    
    
    func (c *Client) CreatePreview(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[CreatePreviewRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_CreatePreviewRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreatePreviewOperation, [error](https://pkg.go.dev/builtin#error))

CreatePreview creates a Preview.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.CreatePreviewRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#CreatePreviewRequest.
    	}
    	op, err := c.CreatePreview(ctx, req)
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
    

### func (*Client) CreatePreviewOperation 
    
    
    func (c *Client) CreatePreviewOperation(name [string](https://pkg.go.dev/builtin#string)) *CreatePreviewOperation

CreatePreviewOperation returns a new CreatePreviewOperation from a given name. The name must be that of a previously created CreatePreviewOperation, possibly from a different process.

### func (*Client) DeleteDeployment 
    
    
    func (c *Client) DeleteDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeleteDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeleteDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

DeleteDeployment deletes a Deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.DeleteDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#DeleteDeploymentRequest.
    	}
    	op, err := c.DeleteDeployment(ctx, req)
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
    

### func (*Client) DeleteDeploymentGroup 
    
    
    func (c *Client) DeleteDeploymentGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeleteDeploymentGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeleteDeploymentGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteDeploymentGroupOperation, [error](https://pkg.go.dev/builtin#error))

DeleteDeploymentGroup deletes a DeploymentGroup

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.DeleteDeploymentGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#DeleteDeploymentGroupRequest.
    	}
    	op, err := c.DeleteDeploymentGroup(ctx, req)
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
    

### func (*Client) DeleteDeploymentGroupOperation 
    
    
    func (c *Client) DeleteDeploymentGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteDeploymentGroupOperation

DeleteDeploymentGroupOperation returns a new DeleteDeploymentGroupOperation from a given name. The name must be that of a previously created DeleteDeploymentGroupOperation, possibly from a different process.

### func (*Client) DeleteDeploymentOperation 
    
    
    func (c *Client) DeleteDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteDeploymentOperation

DeleteDeploymentOperation returns a new DeleteDeploymentOperation from a given name. The name must be that of a previously created DeleteDeploymentOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeletePreview 
    
    
    func (c *Client) DeletePreview(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeletePreviewRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeletePreviewRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeletePreviewOperation, [error](https://pkg.go.dev/builtin#error))

DeletePreview deletes a Preview.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.DeletePreviewRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#DeletePreviewRequest.
    	}
    	op, err := c.DeletePreview(ctx, req)
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
    

### func (*Client) DeletePreviewOperation 
    
    
    func (c *Client) DeletePreviewOperation(name [string](https://pkg.go.dev/builtin#string)) *DeletePreviewOperation

DeletePreviewOperation returns a new DeletePreviewOperation from a given name. The name must be that of a previously created DeletePreviewOperation, possibly from a different process.

### func (*Client) DeleteStatefile 
    
    
    func (c *Client) DeleteStatefile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeleteStatefileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeleteStatefileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteStatefile deletes Terraform state file in a given deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.DeleteStatefileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#DeleteStatefileRequest.
    	}
    	err = c.DeleteStatefile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeprovisionDeploymentGroup 
    
    
    func (c *Client) DeprovisionDeploymentGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeprovisionDeploymentGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeprovisionDeploymentGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeprovisionDeploymentGroupOperation, [error](https://pkg.go.dev/builtin#error))

DeprovisionDeploymentGroup deprovisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the last successful DeploymentGroupRevision but are no longer included in the current DeploymentGroup definition (e.g., following an UpdateDeploymentGroup call), along with their actuated resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.DeprovisionDeploymentGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#DeprovisionDeploymentGroupRequest.
    	}
    	op, err := c.DeprovisionDeploymentGroup(ctx, req)
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
    

### func (*Client) DeprovisionDeploymentGroupOperation 
    
    
    func (c *Client) DeprovisionDeploymentGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *DeprovisionDeploymentGroupOperation

DeprovisionDeploymentGroupOperation returns a new DeprovisionDeploymentGroupOperation from a given name. The name must be that of a previously created DeprovisionDeploymentGroupOperation, possibly from a different process.

### func (*Client) ExportDeploymentStatefile 
    
    
    func (c *Client) ExportDeploymentStatefile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ExportDeploymentStatefileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ExportDeploymentStatefileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Statefile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Statefile), [error](https://pkg.go.dev/builtin#error))

ExportDeploymentStatefile exports Terraform state file from a given deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ExportDeploymentStatefileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ExportDeploymentStatefileRequest.
    	}
    	resp, err := c.ExportDeploymentStatefile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ExportLockInfo 
    
    
    func (c *Client) ExportLockInfo(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ExportLockInfoRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ExportLockInfoRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[LockInfo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_LockInfo), [error](https://pkg.go.dev/builtin#error))

ExportLockInfo exports the lock info on a locked deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ExportLockInfoRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ExportLockInfoRequest.
    	}
    	resp, err := c.ExportLockInfo(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ExportPreviewResult 
    
    
    func (c *Client) ExportPreviewResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ExportPreviewResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ExportPreviewResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ExportPreviewResultResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ExportPreviewResultResponse), [error](https://pkg.go.dev/builtin#error))

ExportPreviewResult export Preview results.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ExportPreviewResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ExportPreviewResultRequest.
    	}
    	resp, err := c.ExportPreviewResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ExportRevisionStatefile 
    
    
    func (c *Client) ExportRevisionStatefile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ExportRevisionStatefileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ExportRevisionStatefileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Statefile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Statefile), [error](https://pkg.go.dev/builtin#error))

ExportRevisionStatefile exports Terraform state file from a given revision.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ExportRevisionStatefileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ExportRevisionStatefileRequest.
    	}
    	resp, err := c.ExportRevisionStatefile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetAutoMigrationConfig 
    
    
    func (c *Client) GetAutoMigrationConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetAutoMigrationConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetAutoMigrationConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[AutoMigrationConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_AutoMigrationConfig), [error](https://pkg.go.dev/builtin#error))

GetAutoMigrationConfig get the AutoMigrationConfig for a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetAutoMigrationConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetAutoMigrationConfigRequest.
    	}
    	resp, err := c.GetAutoMigrationConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetDeployment 
    
    
    func (c *Client) GetDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

GetDeployment gets details about a Deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetDeploymentRequest.
    	}
    	resp, err := c.GetDeployment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetDeploymentGroup 
    
    
    func (c *Client) GetDeploymentGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetDeploymentGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetDeploymentGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

GetDeploymentGroup get a DeploymentGroup for a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetDeploymentGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetDeploymentGroupRequest.
    	}
    	resp, err := c.GetDeploymentGroup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetDeploymentGroupRevision 
    
    
    func (c *Client) GetDeploymentGroupRevision(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetDeploymentGroupRevisionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetDeploymentGroupRevisionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroupRevision](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroupRevision), [error](https://pkg.go.dev/builtin#error))

GetDeploymentGroupRevision gets details about a DeploymentGroupRevision.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetDeploymentGroupRevisionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetDeploymentGroupRevisionRequest.
    	}
    	resp, err := c.GetDeploymentGroupRevision(ctx, req)
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.[GetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_GetLocation)(ctx, req)
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    

### func (*Client) GetPreview 
    
    
    func (c *Client) GetPreview(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetPreviewRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetPreviewRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Preview](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Preview), [error](https://pkg.go.dev/builtin#error))

GetPreview gets details about a Preview.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetPreviewRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetPreviewRequest.
    	}
    	resp, err := c.GetPreview(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetResource 
    
    
    func (c *Client) GetResource(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetResourceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetResourceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Resource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Resource), [error](https://pkg.go.dev/builtin#error))

GetResource gets details about a Resource deployed by Infra Manager.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetResourceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetResourceRequest.
    	}
    	resp, err := c.GetResource(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetResourceChange 
    
    
    func (c *Client) GetResourceChange(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetResourceChangeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetResourceChangeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ResourceChange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ResourceChange), [error](https://pkg.go.dev/builtin#error))

GetResourceChange get a ResourceChange for a given preview.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetResourceChangeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetResourceChangeRequest.
    	}
    	resp, err := c.GetResourceChange(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetResourceDrift 
    
    
    func (c *Client) GetResourceDrift(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetResourceDriftRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetResourceDriftRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ResourceDrift](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ResourceDrift), [error](https://pkg.go.dev/builtin#error))

GetResourceDrift get a ResourceDrift for a given preview.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetResourceDriftRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetResourceDriftRequest.
    	}
    	resp, err := c.GetResourceDrift(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetRevision 
    
    
    func (c *Client) GetRevision(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetRevisionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetRevisionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Revision](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Revision), [error](https://pkg.go.dev/builtin#error))

GetRevision gets details about a Revision.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetRevisionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetRevisionRequest.
    	}
    	resp, err := c.GetRevision(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetTerraformVersion 
    
    
    func (c *Client) GetTerraformVersion(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[GetTerraformVersionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_GetTerraformVersionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[TerraformVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_TerraformVersion), [error](https://pkg.go.dev/builtin#error))

GetTerraformVersion gets details about a TerraformVersion.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.GetTerraformVersionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#GetTerraformVersionRequest.
    	}
    	resp, err := c.GetTerraformVersion(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ImportStatefile 
    
    
    func (c *Client) ImportStatefile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ImportStatefileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ImportStatefileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Statefile](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Statefile), [error](https://pkg.go.dev/builtin#error))

ImportStatefile imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ImportStatefileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ImportStatefileRequest.
    	}
    	resp, err := c.ImportStatefile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListDeploymentGroupRevisions 
    
    
    func (c *Client) ListDeploymentGroupRevisions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListDeploymentGroupRevisionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListDeploymentGroupRevisionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DeploymentGroupRevisionIterator

ListDeploymentGroupRevisions lists DeploymentGroupRevisions in a given DeploymentGroup.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListDeploymentGroupRevisionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListDeploymentGroupRevisionsRequest.
    	}
    	it := c.ListDeploymentGroupRevisions(ctx, req)
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
    		_ = it.Response.(*configpb.ListDeploymentGroupRevisionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListDeploymentGroupRevisionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListDeploymentGroupRevisionsRequest.
    	}
    	for resp, err := range c.ListDeploymentGroupRevisions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDeploymentGroups 
    
    
    func (c *Client) ListDeploymentGroups(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListDeploymentGroupsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListDeploymentGroupsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DeploymentGroupIterator

ListDeploymentGroups list DeploymentGroups for a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListDeploymentGroupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListDeploymentGroupsRequest.
    	}
    	it := c.ListDeploymentGroups(ctx, req)
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
    		_ = it.Response.(*configpb.ListDeploymentGroupsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListDeploymentGroupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListDeploymentGroupsRequest.
    	}
    	for resp, err := range c.ListDeploymentGroups(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDeployments 
    
    
    func (c *Client) ListDeployments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListDeploymentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListDeploymentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DeploymentIterator

ListDeployments lists Deployments in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListDeploymentsRequest.
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
    		_ = it.Response.(*configpb.ListDeploymentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListDeploymentsRequest.
    	}
    	for resp, err := range c.ListDeployments(ctx, req).All() {
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

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
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
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_ListLocations)(ctx, req)
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_ListLocations)(ctx, req).All() {
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
    
    	config "cloud.google.com/go/config/apiv1"
    
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
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    

### func (*Client) ListPreviews 
    
    
    func (c *Client) ListPreviews(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListPreviewsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListPreviewsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PreviewIterator

ListPreviews lists Previews in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListPreviewsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListPreviewsRequest.
    	}
    	it := c.ListPreviews(ctx, req)
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
    		_ = it.Response.(*configpb.ListPreviewsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListPreviewsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListPreviewsRequest.
    	}
    	for resp, err := range c.ListPreviews(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListResourceChanges 
    
    
    func (c *Client) ListResourceChanges(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListResourceChangesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListResourceChangesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ResourceChangeIterator

ListResourceChanges lists ResourceChanges for a given preview.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListResourceChangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListResourceChangesRequest.
    	}
    	it := c.ListResourceChanges(ctx, req)
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
    		_ = it.Response.(*configpb.ListResourceChangesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListResourceChangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListResourceChangesRequest.
    	}
    	for resp, err := range c.ListResourceChanges(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListResourceDrifts 
    
    
    func (c *Client) ListResourceDrifts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListResourceDriftsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListResourceDriftsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ResourceDriftIterator

ListResourceDrifts list ResourceDrifts for a given preview.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListResourceDriftsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListResourceDriftsRequest.
    	}
    	it := c.ListResourceDrifts(ctx, req)
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
    		_ = it.Response.(*configpb.ListResourceDriftsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListResourceDriftsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListResourceDriftsRequest.
    	}
    	for resp, err := range c.ListResourceDrifts(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListResources 
    
    
    func (c *Client) ListResources(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListResourcesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListResourcesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ResourceIterator

ListResources lists Resources in a given revision.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListResourcesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListResourcesRequest.
    	}
    	it := c.ListResources(ctx, req)
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
    		_ = it.Response.(*configpb.ListResourcesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListResourcesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListResourcesRequest.
    	}
    	for resp, err := range c.ListResources(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListRevisions 
    
    
    func (c *Client) ListRevisions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListRevisionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListRevisionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *RevisionIterator

ListRevisions lists Revisions of a deployment.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListRevisionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListRevisionsRequest.
    	}
    	it := c.ListRevisions(ctx, req)
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
    		_ = it.Response.(*configpb.ListRevisionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListRevisionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListRevisionsRequest.
    	}
    	for resp, err := range c.ListRevisions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListTerraformVersions 
    
    
    func (c *Client) ListTerraformVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ListTerraformVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ListTerraformVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TerraformVersionIterator

ListTerraformVersions lists TerraformVersions in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListTerraformVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListTerraformVersionsRequest.
    	}
    	it := c.ListTerraformVersions(ctx, req)
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
    		_ = it.Response.(*configpb.ListTerraformVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ListTerraformVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ListTerraformVersionsRequest.
    	}
    	for resp, err := range c.ListTerraformVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) LockDeployment 
    
    
    func (c *Client) LockDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[LockDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_LockDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*LockDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

LockDeployment locks a deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.LockDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#LockDeploymentRequest.
    	}
    	op, err := c.LockDeployment(ctx, req)
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
    

### func (*Client) LockDeploymentOperation 
    
    
    func (c *Client) LockDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *LockDeploymentOperation

LockDeploymentOperation returns a new LockDeploymentOperation from a given name. The name must be that of a previously created LockDeploymentOperation, possibly from a different process.

### func (*Client) ProvisionDeploymentGroup 
    
    
    func (c *Client) ProvisionDeploymentGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ProvisionDeploymentGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ProvisionDeploymentGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ProvisionDeploymentGroupOperation, [error](https://pkg.go.dev/builtin#error))

ProvisionDeploymentGroup provisions a deployment group.

NOTE: As a first step of this operation, Infra Manager will automatically delete any Deployments that were part of the last successful DeploymentGroupRevision but are no longer included in the current DeploymentGroup definition (e.g., following an UpdateDeploymentGroup call), along with their actuated resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.ProvisionDeploymentGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#ProvisionDeploymentGroupRequest.
    	}
    	op, err := c.ProvisionDeploymentGroup(ctx, req)
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
    

### func (*Client) ProvisionDeploymentGroupOperation 
    
    
    func (c *Client) ProvisionDeploymentGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *ProvisionDeploymentGroupOperation

ProvisionDeploymentGroupOperation returns a new ProvisionDeploymentGroupOperation from a given name. The name must be that of a previously created ProvisionDeploymentGroupOperation, possibly from a different process.

### func (*Client) SetIamPolicy 
    
    
    func (c *Client) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    
    	config "cloud.google.com/go/config/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
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
    

### func (*Client) UnlockDeployment 
    
    
    func (c *Client) UnlockDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[UnlockDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_UnlockDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UnlockDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

UnlockDeployment unlocks a locked deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.UnlockDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#UnlockDeploymentRequest.
    	}
    	op, err := c.UnlockDeployment(ctx, req)
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
    

### func (*Client) UnlockDeploymentOperation 
    
    
    func (c *Client) UnlockDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *UnlockDeploymentOperation

UnlockDeploymentOperation returns a new UnlockDeploymentOperation from a given name. The name must be that of a previously created UnlockDeploymentOperation, possibly from a different process.

### func (*Client) UpdateAutoMigrationConfig 
    
    
    func (c *Client) UpdateAutoMigrationConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[UpdateAutoMigrationConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_UpdateAutoMigrationConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateAutoMigrationConfigOperation, [error](https://pkg.go.dev/builtin#error))

UpdateAutoMigrationConfig updates the AutoMigrationConfig for a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.UpdateAutoMigrationConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#UpdateAutoMigrationConfigRequest.
    	}
    	op, err := c.UpdateAutoMigrationConfig(ctx, req)
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
    

### func (*Client) UpdateAutoMigrationConfigOperation 
    
    
    func (c *Client) UpdateAutoMigrationConfigOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateAutoMigrationConfigOperation

UpdateAutoMigrationConfigOperation returns a new UpdateAutoMigrationConfigOperation from a given name. The name must be that of a previously created UpdateAutoMigrationConfigOperation, possibly from a different process.

### func (*Client) UpdateDeployment 
    
    
    func (c *Client) UpdateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[UpdateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_UpdateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

UpdateDeployment updates a Deployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.UpdateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#UpdateDeploymentRequest.
    	}
    	op, err := c.UpdateDeployment(ctx, req)
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
    

### func (*Client) UpdateDeploymentGroup 
    
    
    func (c *Client) UpdateDeploymentGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[UpdateDeploymentGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_UpdateDeploymentGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateDeploymentGroupOperation, [error](https://pkg.go.dev/builtin#error))

UpdateDeploymentGroup updates a DeploymentGroup

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	config "cloud.google.com/go/config/apiv1"
    	configpb "cloud.google.com/go/config/apiv1/configpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := config.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1.html#cloud_google_com_go_config_apiv1_Client_Close)()
    
    	req := &configpb.UpdateDeploymentGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/config/apiv1/configpb#UpdateDeploymentGroupRequest.
    	}
    	op, err := c.UpdateDeploymentGroup(ctx, req)
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
    

### func (*Client) UpdateDeploymentGroupOperation 
    
    
    func (c *Client) UpdateDeploymentGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateDeploymentGroupOperation

UpdateDeploymentGroupOperation returns a new UpdateDeploymentGroupOperation from a given name. The name must be that of a previously created UpdateDeploymentGroupOperation, possibly from a different process.

### func (*Client) UpdateDeploymentOperation 
    
    
    func (c *Client) UpdateDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateDeploymentOperation

UpdateDeploymentOperation returns a new UpdateDeploymentOperation from a given name. The name must be that of a previously created UpdateDeploymentOperation, possibly from a different process.

## CreateDeploymentGroupOperation
    
    
    type CreateDeploymentGroupOperation struct {
    	// contains filtered or unexported fields
    }

CreateDeploymentGroupOperation manages a long-running operation from CreateDeploymentGroup.

### func (*CreateDeploymentGroupOperation) Done 
    
    
    func (op *CreateDeploymentGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateDeploymentGroupOperation) Metadata 
    
    
    func (op *CreateDeploymentGroupOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateDeploymentGroupOperation) Name 
    
    
    func (op *CreateDeploymentGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateDeploymentGroupOperation) Poll 
    
    
    func (op *CreateDeploymentGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateDeploymentGroupOperation) Wait 
    
    
    func (op *CreateDeploymentGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateDeploymentOperation
    
    
    type CreateDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

CreateDeploymentOperation manages a long-running operation from CreateDeployment.

### func (*CreateDeploymentOperation) Done 
    
    
    func (op *CreateDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateDeploymentOperation) Metadata 
    
    
    func (op *CreateDeploymentOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateDeploymentOperation) Name 
    
    
    func (op *CreateDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateDeploymentOperation) Poll 
    
    
    func (op *CreateDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateDeploymentOperation) Wait 
    
    
    func (op *CreateDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreatePreviewOperation
    
    
    type CreatePreviewOperation struct {
    	// contains filtered or unexported fields
    }

CreatePreviewOperation manages a long-running operation from CreatePreview.

### func (*CreatePreviewOperation) Done 
    
    
    func (op *CreatePreviewOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreatePreviewOperation) Metadata 
    
    
    func (op *CreatePreviewOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreatePreviewOperation) Name 
    
    
    func (op *CreatePreviewOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreatePreviewOperation) Poll 
    
    
    func (op *CreatePreviewOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Preview](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Preview), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreatePreviewOperation) Wait 
    
    
    func (op *CreatePreviewOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Preview](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Preview), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteDeploymentGroupOperation
    
    
    type DeleteDeploymentGroupOperation struct {
    	// contains filtered or unexported fields
    }

DeleteDeploymentGroupOperation manages a long-running operation from DeleteDeploymentGroup.

### func (*DeleteDeploymentGroupOperation) Done 
    
    
    func (op *DeleteDeploymentGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteDeploymentGroupOperation) Metadata 
    
    
    func (op *DeleteDeploymentGroupOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteDeploymentGroupOperation) Name 
    
    
    func (op *DeleteDeploymentGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteDeploymentGroupOperation) Poll 
    
    
    func (op *DeleteDeploymentGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteDeploymentGroupOperation) Wait 
    
    
    func (op *DeleteDeploymentGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteDeploymentOperation
    
    
    type DeleteDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

DeleteDeploymentOperation manages a long-running operation from DeleteDeployment.

### func (*DeleteDeploymentOperation) Done 
    
    
    func (op *DeleteDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteDeploymentOperation) Metadata 
    
    
    func (op *DeleteDeploymentOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteDeploymentOperation) Name 
    
    
    func (op *DeleteDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteDeploymentOperation) Poll 
    
    
    func (op *DeleteDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteDeploymentOperation) Wait 
    
    
    func (op *DeleteDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeletePreviewOperation
    
    
    type DeletePreviewOperation struct {
    	// contains filtered or unexported fields
    }

DeletePreviewOperation manages a long-running operation from DeletePreview.

### func (*DeletePreviewOperation) Done 
    
    
    func (op *DeletePreviewOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeletePreviewOperation) Metadata 
    
    
    func (op *DeletePreviewOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeletePreviewOperation) Name 
    
    
    func (op *DeletePreviewOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeletePreviewOperation) Poll 
    
    
    func (op *DeletePreviewOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Preview](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Preview), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeletePreviewOperation) Wait 
    
    
    func (op *DeletePreviewOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Preview](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Preview), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeploymentGroupIterator
    
    
    type DeploymentGroupIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.DeploymentGroup, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DeploymentGroupIterator manages a stream of *configpb.DeploymentGroup.

### func (*DeploymentGroupIterator) All 
    
    
    func (it *DeploymentGroupIterator) All() iter.Seq2[*configpb.DeploymentGroup, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DeploymentGroupIterator) Next 
    
    
    func (it *DeploymentGroupIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DeploymentGroupIterator) PageInfo 
    
    
    func (it *DeploymentGroupIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DeploymentGroupRevisionIterator
    
    
    type DeploymentGroupRevisionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.DeploymentGroupRevision, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DeploymentGroupRevisionIterator manages a stream of *configpb.DeploymentGroupRevision.

### func (*DeploymentGroupRevisionIterator) All 
    
    
    func (it *DeploymentGroupRevisionIterator) All() iter.Seq2[*configpb.DeploymentGroupRevision, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DeploymentGroupRevisionIterator) Next 
    
    
    func (it *DeploymentGroupRevisionIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroupRevision](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroupRevision), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DeploymentGroupRevisionIterator) PageInfo 
    
    
    func (it *DeploymentGroupRevisionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.Deployment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DeploymentIterator manages a stream of *configpb.Deployment.

### func (*DeploymentIterator) All 
    
    
    func (it *DeploymentIterator) All() iter.Seq2[*configpb.Deployment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DeploymentIterator) Next 
    
    
    func (it *DeploymentIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DeploymentIterator) PageInfo 
    
    
    func (it *DeploymentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DeprovisionDeploymentGroupOperation
    
    
    type DeprovisionDeploymentGroupOperation struct {
    	// contains filtered or unexported fields
    }

DeprovisionDeploymentGroupOperation manages a long-running operation from DeprovisionDeploymentGroup.

### func (*DeprovisionDeploymentGroupOperation) Done 
    
    
    func (op *DeprovisionDeploymentGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeprovisionDeploymentGroupOperation) Metadata 
    
    
    func (op *DeprovisionDeploymentGroupOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeprovisionDeploymentGroupOperation) Name 
    
    
    func (op *DeprovisionDeploymentGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeprovisionDeploymentGroupOperation) Poll 
    
    
    func (op *DeprovisionDeploymentGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeprovisionDeploymentGroupOperation) Wait 
    
    
    func (op *DeprovisionDeploymentGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

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

## LockDeploymentOperation
    
    
    type LockDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

LockDeploymentOperation manages a long-running operation from LockDeployment.

### func (*LockDeploymentOperation) Done 
    
    
    func (op *LockDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*LockDeploymentOperation) Metadata 
    
    
    func (op *LockDeploymentOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*LockDeploymentOperation) Name 
    
    
    func (op *LockDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*LockDeploymentOperation) Poll 
    
    
    func (op *LockDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*LockDeploymentOperation) Wait 
    
    
    func (op *LockDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

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

## PreviewIterator
    
    
    type PreviewIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.Preview, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PreviewIterator manages a stream of *configpb.Preview.

### func (*PreviewIterator) All 
    
    
    func (it *PreviewIterator) All() iter.Seq2[*configpb.Preview, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PreviewIterator) Next 
    
    
    func (it *PreviewIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Preview](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Preview), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PreviewIterator) PageInfo 
    
    
    func (it *PreviewIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ProvisionDeploymentGroupOperation
    
    
    type ProvisionDeploymentGroupOperation struct {
    	// contains filtered or unexported fields
    }

ProvisionDeploymentGroupOperation manages a long-running operation from ProvisionDeploymentGroup.

### func (*ProvisionDeploymentGroupOperation) Done 
    
    
    func (op *ProvisionDeploymentGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ProvisionDeploymentGroupOperation) Metadata 
    
    
    func (op *ProvisionDeploymentGroupOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ProvisionDeploymentGroupOperation) Name 
    
    
    func (op *ProvisionDeploymentGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ProvisionDeploymentGroupOperation) Poll 
    
    
    func (op *ProvisionDeploymentGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ProvisionDeploymentGroupOperation) Wait 
    
    
    func (op *ProvisionDeploymentGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ResourceChangeIterator
    
    
    type ResourceChangeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.ResourceChange, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ResourceChangeIterator manages a stream of *configpb.ResourceChange.

### func (*ResourceChangeIterator) All 
    
    
    func (it *ResourceChangeIterator) All() iter.Seq2[*configpb.ResourceChange, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ResourceChangeIterator) Next 
    
    
    func (it *ResourceChangeIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ResourceChange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ResourceChange), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ResourceChangeIterator) PageInfo 
    
    
    func (it *ResourceChangeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ResourceDriftIterator
    
    
    type ResourceDriftIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.ResourceDrift, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ResourceDriftIterator manages a stream of *configpb.ResourceDrift.

### func (*ResourceDriftIterator) All 
    
    
    func (it *ResourceDriftIterator) All() iter.Seq2[*configpb.ResourceDrift, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ResourceDriftIterator) Next 
    
    
    func (it *ResourceDriftIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[ResourceDrift](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_ResourceDrift), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ResourceDriftIterator) PageInfo 
    
    
    func (it *ResourceDriftIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ResourceIterator
    
    
    type ResourceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.Resource, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ResourceIterator manages a stream of *configpb.Resource.

### func (*ResourceIterator) All 
    
    
    func (it *ResourceIterator) All() iter.Seq2[*configpb.Resource, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ResourceIterator) Next 
    
    
    func (it *ResourceIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Resource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Resource), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ResourceIterator) PageInfo 
    
    
    func (it *ResourceIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## RevisionIterator
    
    
    type RevisionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.Revision, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

RevisionIterator manages a stream of *configpb.Revision.

### func (*RevisionIterator) All 
    
    
    func (it *RevisionIterator) All() iter.Seq2[*configpb.Revision, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*RevisionIterator) Next 
    
    
    func (it *RevisionIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Revision](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Revision), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*RevisionIterator) PageInfo 
    
    
    func (it *RevisionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TerraformVersionIterator
    
    
    type TerraformVersionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*configpb.TerraformVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TerraformVersionIterator manages a stream of *configpb.TerraformVersion.

### func (*TerraformVersionIterator) All 
    
    
    func (it *TerraformVersionIterator) All() iter.Seq2[*configpb.TerraformVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TerraformVersionIterator) Next 
    
    
    func (it *TerraformVersionIterator) Next() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[TerraformVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_TerraformVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TerraformVersionIterator) PageInfo 
    
    
    func (it *TerraformVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## UnlockDeploymentOperation
    
    
    type UnlockDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

UnlockDeploymentOperation manages a long-running operation from UnlockDeployment.

### func (*UnlockDeploymentOperation) Done 
    
    
    func (op *UnlockDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UnlockDeploymentOperation) Metadata 
    
    
    func (op *UnlockDeploymentOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UnlockDeploymentOperation) Name 
    
    
    func (op *UnlockDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UnlockDeploymentOperation) Poll 
    
    
    func (op *UnlockDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UnlockDeploymentOperation) Wait 
    
    
    func (op *UnlockDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateAutoMigrationConfigOperation
    
    
    type UpdateAutoMigrationConfigOperation struct {
    	// contains filtered or unexported fields
    }

UpdateAutoMigrationConfigOperation manages a long-running operation from UpdateAutoMigrationConfig.

### func (*UpdateAutoMigrationConfigOperation) Done 
    
    
    func (op *UpdateAutoMigrationConfigOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateAutoMigrationConfigOperation) Metadata 
    
    
    func (op *UpdateAutoMigrationConfigOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateAutoMigrationConfigOperation) Name 
    
    
    func (op *UpdateAutoMigrationConfigOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateAutoMigrationConfigOperation) Poll 
    
    
    func (op *UpdateAutoMigrationConfigOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[AutoMigrationConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_AutoMigrationConfig), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateAutoMigrationConfigOperation) Wait 
    
    
    func (op *UpdateAutoMigrationConfigOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[AutoMigrationConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_AutoMigrationConfig), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateDeploymentGroupOperation
    
    
    type UpdateDeploymentGroupOperation struct {
    	// contains filtered or unexported fields
    }

UpdateDeploymentGroupOperation manages a long-running operation from UpdateDeploymentGroup.

### func (*UpdateDeploymentGroupOperation) Done 
    
    
    func (op *UpdateDeploymentGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateDeploymentGroupOperation) Metadata 
    
    
    func (op *UpdateDeploymentGroupOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateDeploymentGroupOperation) Name 
    
    
    func (op *UpdateDeploymentGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateDeploymentGroupOperation) Poll 
    
    
    func (op *UpdateDeploymentGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateDeploymentGroupOperation) Wait 
    
    
    func (op *UpdateDeploymentGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[DeploymentGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_DeploymentGroup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateDeploymentOperation
    
    
    type UpdateDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

UpdateDeploymentOperation manages a long-running operation from UpdateDeployment.

### func (*UpdateDeploymentOperation) Done 
    
    
    func (op *UpdateDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateDeploymentOperation) Metadata 
    
    
    func (op *UpdateDeploymentOperation) Metadata() (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateDeploymentOperation) Name 
    
    
    func (op *UpdateDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateDeploymentOperation) Poll 
    
    
    func (op *UpdateDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateDeploymentOperation) Wait 
    
    
    func (op *UpdateDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[configpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb).[Deployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/config/latest/apiv1/configpb#cloud_google_com_go_config_apiv1_configpb_Deployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
