---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/
title: Bare Metal Solution API v2 - Package cloud.google.com/go/baremetalsolution/apiv2 (v1.11.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:06.937000+00:00
---

# Bare Metal Solution API v2 - Package cloud.google.com/go/baremetalsolution/apiv2 (v1.11.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Bare Metal Solution API v2 - Package cloud.google.com/go/baremetalsolution/apiv2 (v1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.6  1.2.11  1.1.1  1.0.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2). 

Package baremetalsolution is an auto-generated package for the Bare Metal Solution API. 

Provides ways to manage Bare Metal Solution hardware installed in a regional extension located near a Google Cloud data center. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/baremetalsolution/apiv2@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := baremetalsolution.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &baremetalsolutionpb.CreateNfsShareRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#CreateNfsShareRequest.
    }
    op, err := c.CreateNfsShare(ctx, req)
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
    	ListInstances                   []gax.CallOption
    	GetInstance                     []gax.CallOption
    	UpdateInstance                  []gax.CallOption
    	RenameInstance                  []gax.CallOption
    	ResetInstance                   []gax.CallOption
    	StartInstance                   []gax.CallOption
    	StopInstance                    []gax.CallOption
    	EnableInteractiveSerialConsole  []gax.CallOption
    	DisableInteractiveSerialConsole []gax.CallOption
    	DetachLun                       []gax.CallOption
    	ListSSHKeys                     []gax.CallOption
    	CreateSSHKey                    []gax.CallOption
    	DeleteSSHKey                    []gax.CallOption
    	ListVolumes                     []gax.CallOption
    	GetVolume                       []gax.CallOption
    	UpdateVolume                    []gax.CallOption
    	RenameVolume                    []gax.CallOption
    	EvictVolume                     []gax.CallOption
    	ResizeVolume                    []gax.CallOption
    	ListNetworks                    []gax.CallOption
    	ListNetworkUsage                []gax.CallOption
    	GetNetwork                      []gax.CallOption
    	UpdateNetwork                   []gax.CallOption
    	CreateVolumeSnapshot            []gax.CallOption
    	RestoreVolumeSnapshot           []gax.CallOption
    	DeleteVolumeSnapshot            []gax.CallOption
    	GetVolumeSnapshot               []gax.CallOption
    	ListVolumeSnapshots             []gax.CallOption
    	GetLun                          []gax.CallOption
    	ListLuns                        []gax.CallOption
    	EvictLun                        []gax.CallOption
    	GetNfsShare                     []gax.CallOption
    	ListNfsShares                   []gax.CallOption
    	UpdateNfsShare                  []gax.CallOption
    	CreateNfsShare                  []gax.CallOption
    	RenameNfsShare                  []gax.CallOption
    	DeleteNfsShare                  []gax.CallOption
    	ListProvisioningQuotas          []gax.CallOption
    	SubmitProvisioningConfig        []gax.CallOption
    	GetProvisioningConfig           []gax.CallOption
    	CreateProvisioningConfig        []gax.CallOption
    	UpdateProvisioningConfig        []gax.CallOption
    	RenameNetwork                   []gax.CallOption
    	ListOSImages                    []gax.CallOption
    	GetLocation                     []gax.CallOption
    	ListLocations                   []gax.CallOption
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

Client is a client for interacting with Bare Metal Solution API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Performs management operations on Bare Metal Solution servers.

The baremetalsolution.googleapis.com service provides management capabilities for Bare Metal Solution servers. To access the API methods, you must assign Bare Metal Solution IAM roles containing the desired permissions to your staff in your Google Cloud project. You must also enable the Bare Metal Solution API. Once enabled, the methods act upon specific servers in your Bare Metal Solution environment.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new bare metal solution client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Performs management operations on Bare Metal Solution servers.

The baremetalsolution.googleapis.com service provides management capabilities for Bare Metal Solution servers. To access the API methods, you must assign Bare Metal Solution IAM roles containing the desired permissions to your staff in your Google Cloud project. You must also enable the Bare Metal Solution API. Once enabled, the methods act upon specific servers in your Bare Metal Solution environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new bare metal solution rest client.

Performs management operations on Bare Metal Solution servers.

The baremetalsolution.googleapis.com service provides management capabilities for Bare Metal Solution servers. To access the API methods, you must assign Bare Metal Solution IAM roles containing the desired permissions to your staff in your Google Cloud project. You must also enable the Bare Metal Solution API. Once enabled, the methods act upon specific servers in your Bare Metal Solution environment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) CreateNfsShare 
    
    
    func (c *Client) CreateNfsShare(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[CreateNfsShareRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_CreateNfsShareRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateNfsShareOperation, [error](https://pkg.go.dev/builtin#error))

CreateNfsShare create an NFS share.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.CreateNfsShareRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#CreateNfsShareRequest.
    	}
    	op, err := c.CreateNfsShare(ctx, req)
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
    

### func (*Client) CreateNfsShareOperation 
    
    
    func (c *Client) CreateNfsShareOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateNfsShareOperation

CreateNfsShareOperation returns a new CreateNfsShareOperation from a given name. The name must be that of a previously created CreateNfsShareOperation, possibly from a different process.

### func (*Client) CreateProvisioningConfig 
    
    
    func (c *Client) CreateProvisioningConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[CreateProvisioningConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_CreateProvisioningConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ProvisioningConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ProvisioningConfig), [error](https://pkg.go.dev/builtin#error))

CreateProvisioningConfig create new ProvisioningConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.CreateProvisioningConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#CreateProvisioningConfigRequest.
    	}
    	resp, err := c.CreateProvisioningConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateSSHKey 
    
    
    func (c *Client) CreateSSHKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[CreateSSHKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_CreateSSHKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[SSHKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_SSHKey), [error](https://pkg.go.dev/builtin#error))

CreateSSHKey register a public SSH key in the specified project for use with the interactive serial console feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.CreateSSHKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#CreateSSHKeyRequest.
    	}
    	resp, err := c.CreateSSHKey(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateVolumeSnapshot 
    
    
    func (c *Client) CreateVolumeSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[CreateVolumeSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_CreateVolumeSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[VolumeSnapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_VolumeSnapshot), [error](https://pkg.go.dev/builtin#error))

CreateVolumeSnapshot takes a snapshot of a boot volume. Returns INVALID_ARGUMENT if called for a non-boot volume.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.CreateVolumeSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#CreateVolumeSnapshotRequest.
    	}
    	resp, err := c.CreateVolumeSnapshot(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) DeleteNfsShare 
    
    
    func (c *Client) DeleteNfsShare(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DeleteNfsShareRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DeleteNfsShareRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteNfsShareOperation, [error](https://pkg.go.dev/builtin#error))

DeleteNfsShare delete an NFS share. The underlying volume is automatically deleted.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.DeleteNfsShareRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#DeleteNfsShareRequest.
    	}
    	op, err := c.DeleteNfsShare(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteNfsShareOperation 
    
    
    func (c *Client) DeleteNfsShareOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteNfsShareOperation

DeleteNfsShareOperation returns a new DeleteNfsShareOperation from a given name. The name must be that of a previously created DeleteNfsShareOperation, possibly from a different process.

### func (*Client) DeleteSSHKey 
    
    
    func (c *Client) DeleteSSHKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DeleteSSHKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DeleteSSHKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteSSHKey deletes a public SSH key registered in the specified project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.DeleteSSHKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#DeleteSSHKeyRequest.
    	}
    	err = c.DeleteSSHKey(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteVolumeSnapshot 
    
    
    func (c *Client) DeleteVolumeSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DeleteVolumeSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DeleteVolumeSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteVolumeSnapshot deletes a volume snapshot. Returns INVALID_ARGUMENT if called for a non-boot volume.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.DeleteVolumeSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#DeleteVolumeSnapshotRequest.
    	}
    	err = c.DeleteVolumeSnapshot(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DetachLun 
    
    
    func (c *Client) DetachLun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DetachLunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DetachLunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DetachLunOperation, [error](https://pkg.go.dev/builtin#error))

DetachLun detach LUN from Instance.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.DetachLunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#DetachLunRequest.
    	}
    	op, err := c.DetachLun(ctx, req)
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
    

### func (*Client) DetachLunOperation 
    
    
    func (c *Client) DetachLunOperation(name [string](https://pkg.go.dev/builtin#string)) *DetachLunOperation

DetachLunOperation returns a new DetachLunOperation from a given name. The name must be that of a previously created DetachLunOperation, possibly from a different process.

### func (*Client) DisableInteractiveSerialConsole 
    
    
    func (c *Client) DisableInteractiveSerialConsole(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DisableInteractiveSerialConsoleRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DisableInteractiveSerialConsoleRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DisableInteractiveSerialConsoleOperation, [error](https://pkg.go.dev/builtin#error))

DisableInteractiveSerialConsole disable the interactive serial console feature on an instance.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.DisableInteractiveSerialConsoleRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#DisableInteractiveSerialConsoleRequest.
    	}
    	op, err := c.DisableInteractiveSerialConsole(ctx, req)
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
    

### func (*Client) DisableInteractiveSerialConsoleOperation 
    
    
    func (c *Client) DisableInteractiveSerialConsoleOperation(name [string](https://pkg.go.dev/builtin#string)) *DisableInteractiveSerialConsoleOperation

DisableInteractiveSerialConsoleOperation returns a new DisableInteractiveSerialConsoleOperation from a given name. The name must be that of a previously created DisableInteractiveSerialConsoleOperation, possibly from a different process.

### func (*Client) EnableInteractiveSerialConsole 
    
    
    func (c *Client) EnableInteractiveSerialConsole(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[EnableInteractiveSerialConsoleRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_EnableInteractiveSerialConsoleRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*EnableInteractiveSerialConsoleOperation, [error](https://pkg.go.dev/builtin#error))

EnableInteractiveSerialConsole enable the interactive serial console feature on an instance.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.EnableInteractiveSerialConsoleRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#EnableInteractiveSerialConsoleRequest.
    	}
    	op, err := c.EnableInteractiveSerialConsole(ctx, req)
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
    

### func (*Client) EnableInteractiveSerialConsoleOperation 
    
    
    func (c *Client) EnableInteractiveSerialConsoleOperation(name [string](https://pkg.go.dev/builtin#string)) *EnableInteractiveSerialConsoleOperation

EnableInteractiveSerialConsoleOperation returns a new EnableInteractiveSerialConsoleOperation from a given name. The name must be that of a previously created EnableInteractiveSerialConsoleOperation, possibly from a different process.

### func (*Client) EvictLun 
    
    
    func (c *Client) EvictLun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[EvictLunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_EvictLunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*EvictLunOperation, [error](https://pkg.go.dev/builtin#error))

EvictLun skips lun’s cooloff and deletes it now. Lun must be in cooloff state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.EvictLunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#EvictLunRequest.
    	}
    	op, err := c.EvictLun(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) EvictLunOperation 
    
    
    func (c *Client) EvictLunOperation(name [string](https://pkg.go.dev/builtin#string)) *EvictLunOperation

EvictLunOperation returns a new EvictLunOperation from a given name. The name must be that of a previously created EvictLunOperation, possibly from a different process.

### func (*Client) EvictVolume 
    
    
    func (c *Client) EvictVolume(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[EvictVolumeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_EvictVolumeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*EvictVolumeOperation, [error](https://pkg.go.dev/builtin#error))

EvictVolume skips volume’s cooloff and deletes it now. Volume must be in cooloff state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.EvictVolumeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#EvictVolumeRequest.
    	}
    	op, err := c.EvictVolume(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) EvictVolumeOperation 
    
    
    func (c *Client) EvictVolumeOperation(name [string](https://pkg.go.dev/builtin#string)) *EvictVolumeOperation

EvictVolumeOperation returns a new EvictVolumeOperation from a given name. The name must be that of a previously created EvictVolumeOperation, possibly from a different process.

### func (*Client) GetInstance 
    
    
    func (c *Client) GetInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

GetInstance get details about a single server.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetInstanceRequest.
    	}
    	resp, err := c.GetInstance(ctx, req)
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
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
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
    

### func (*Client) GetLun 
    
    
    func (c *Client) GetLun(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetLunRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetLunRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Lun](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Lun), [error](https://pkg.go.dev/builtin#error))

GetLun get details of a single storage logical unit number(LUN).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetLunRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetLunRequest.
    	}
    	resp, err := c.GetLun(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetNetwork 
    
    
    func (c *Client) GetNetwork(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetNetworkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetNetworkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Network](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Network), [error](https://pkg.go.dev/builtin#error))

GetNetwork get details of a single network.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetNetworkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetNetworkRequest.
    	}
    	resp, err := c.GetNetwork(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetNfsShare 
    
    
    func (c *Client) GetNfsShare(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetNfsShareRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetNfsShareRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

GetNfsShare get details of a single NFS share.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetNfsShareRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetNfsShareRequest.
    	}
    	resp, err := c.GetNfsShare(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetProvisioningConfig 
    
    
    func (c *Client) GetProvisioningConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetProvisioningConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetProvisioningConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ProvisioningConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ProvisioningConfig), [error](https://pkg.go.dev/builtin#error))

GetProvisioningConfig get ProvisioningConfig by name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetProvisioningConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetProvisioningConfigRequest.
    	}
    	resp, err := c.GetProvisioningConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetVolume 
    
    
    func (c *Client) GetVolume(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetVolumeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetVolumeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

GetVolume get details of a single storage volume.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetVolumeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetVolumeRequest.
    	}
    	resp, err := c.GetVolume(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetVolumeSnapshot 
    
    
    func (c *Client) GetVolumeSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[GetVolumeSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_GetVolumeSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[VolumeSnapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_VolumeSnapshot), [error](https://pkg.go.dev/builtin#error))

GetVolumeSnapshot returns the specified snapshot resource. Returns INVALID_ARGUMENT if called for a non-boot volume.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.GetVolumeSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#GetVolumeSnapshotRequest.
    	}
    	resp, err := c.GetVolumeSnapshot(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListInstances 
    
    
    func (c *Client) ListInstances(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListInstancesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListInstancesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *InstanceIterator

ListInstances list servers in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListInstancesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListInstancesRequest.
    	}
    	it := c.ListInstances(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListInstancesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListInstancesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListInstancesRequest.
    	}
    	for resp, err := range c.ListInstances(ctx, req).All() {
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
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
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
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_ListLocations)(ctx, req)
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
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListLuns 
    
    
    func (c *Client) ListLuns(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListLunsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListLunsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LunIterator

ListLuns list storage volume luns for given storage volume.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListLunsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListLunsRequest.
    	}
    	it := c.ListLuns(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListLunsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListLunsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListLunsRequest.
    	}
    	for resp, err := range c.ListLuns(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListNetworkUsage 
    
    
    func (c *Client) ListNetworkUsage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListNetworkUsageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListNetworkUsageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListNetworkUsageResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListNetworkUsageResponse), [error](https://pkg.go.dev/builtin#error))

ListNetworkUsage list all Networks (and used IPs for each Network) in the vendor account associated with the specified project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListNetworkUsageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListNetworkUsageRequest.
    	}
    	resp, err := c.ListNetworkUsage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListNetworks 
    
    
    func (c *Client) ListNetworks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListNetworksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListNetworksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *NetworkIterator

ListNetworks list network in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListNetworksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListNetworksRequest.
    	}
    	it := c.ListNetworks(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListNetworksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListNetworksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListNetworksRequest.
    	}
    	for resp, err := range c.ListNetworks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListNfsShares 
    
    
    func (c *Client) ListNfsShares(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListNfsSharesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListNfsSharesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *NfsShareIterator

ListNfsShares list NFS shares.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListNfsSharesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListNfsSharesRequest.
    	}
    	it := c.ListNfsShares(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListNfsSharesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListNfsSharesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListNfsSharesRequest.
    	}
    	for resp, err := range c.ListNfsShares(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOSImages 
    
    
    func (c *Client) ListOSImages(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListOSImagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListOSImagesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OSImageIterator

ListOSImages retrieves the list of OS images which are currently approved.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListOSImagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListOSImagesRequest.
    	}
    	it := c.ListOSImages(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListOSImagesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListOSImagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListOSImagesRequest.
    	}
    	for resp, err := range c.ListOSImages(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListProvisioningQuotas 
    
    
    func (c *Client) ListProvisioningQuotas(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListProvisioningQuotasRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListProvisioningQuotasRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProvisioningQuotaIterator

ListProvisioningQuotas list the budget details to provision resources on a given project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListProvisioningQuotasRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListProvisioningQuotasRequest.
    	}
    	it := c.ListProvisioningQuotas(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListProvisioningQuotasResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListProvisioningQuotasRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListProvisioningQuotasRequest.
    	}
    	for resp, err := range c.ListProvisioningQuotas(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListSSHKeys 
    
    
    func (c *Client) ListSSHKeys(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListSSHKeysRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListSSHKeysRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SSHKeyIterator

ListSSHKeys lists the public SSH keys registered for the specified project. These SSH keys are used only for the interactive serial console feature.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListSSHKeysRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListSSHKeysRequest.
    	}
    	it := c.ListSSHKeys(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListSSHKeysResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListSSHKeysRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListSSHKeysRequest.
    	}
    	for resp, err := range c.ListSSHKeys(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListVolumeSnapshots 
    
    
    func (c *Client) ListVolumeSnapshots(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListVolumeSnapshotsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListVolumeSnapshotsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *VolumeSnapshotIterator

ListVolumeSnapshots retrieves the list of snapshots for the specified volume. Returns a response with an empty list of snapshots if called for a non-boot volume.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListVolumeSnapshotsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListVolumeSnapshotsRequest.
    	}
    	it := c.ListVolumeSnapshots(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListVolumeSnapshotsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListVolumeSnapshotsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListVolumeSnapshotsRequest.
    	}
    	for resp, err := range c.ListVolumeSnapshots(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListVolumes 
    
    
    func (c *Client) ListVolumes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ListVolumesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ListVolumesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *VolumeIterator

ListVolumes list storage volumes in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListVolumesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListVolumesRequest.
    	}
    	it := c.ListVolumes(ctx, req)
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
    		_ = it.Response.(*baremetalsolutionpb.ListVolumesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ListVolumesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ListVolumesRequest.
    	}
    	for resp, err := range c.ListVolumes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) RenameInstance 
    
    
    func (c *Client) RenameInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[RenameInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_RenameInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

RenameInstance renameInstance sets a new name for an instance. Use with caution, previous names become immediately invalidated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.RenameInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#RenameInstanceRequest.
    	}
    	resp, err := c.RenameInstance(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RenameNetwork 
    
    
    func (c *Client) RenameNetwork(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[RenameNetworkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_RenameNetworkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Network](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Network), [error](https://pkg.go.dev/builtin#error))

RenameNetwork renameNetwork sets a new name for a network. Use with caution, previous names become immediately invalidated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.RenameNetworkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#RenameNetworkRequest.
    	}
    	resp, err := c.RenameNetwork(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RenameNfsShare 
    
    
    func (c *Client) RenameNfsShare(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[RenameNfsShareRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_RenameNfsShareRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

RenameNfsShare renameNfsShare sets a new name for an nfsshare. Use with caution, previous names become immediately invalidated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.RenameNfsShareRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#RenameNfsShareRequest.
    	}
    	resp, err := c.RenameNfsShare(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RenameVolume 
    
    
    func (c *Client) RenameVolume(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[RenameVolumeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_RenameVolumeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

RenameVolume renameVolume sets a new name for a volume. Use with caution, previous names become immediately invalidated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.RenameVolumeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#RenameVolumeRequest.
    	}
    	resp, err := c.RenameVolume(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ResetInstance 
    
    
    func (c *Client) ResetInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ResetInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ResetInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ResetInstanceOperation, [error](https://pkg.go.dev/builtin#error))

ResetInstance perform an ungraceful, hard reset on a server. Equivalent to shutting the power off and then turning it back on.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ResetInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ResetInstanceRequest.
    	}
    	op, err := c.ResetInstance(ctx, req)
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
    

### func (*Client) ResetInstanceOperation 
    
    
    func (c *Client) ResetInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *ResetInstanceOperation

ResetInstanceOperation returns a new ResetInstanceOperation from a given name. The name must be that of a previously created ResetInstanceOperation, possibly from a different process.

### func (*Client) ResizeVolume 
    
    
    func (c *Client) ResizeVolume(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ResizeVolumeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ResizeVolumeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ResizeVolumeOperation, [error](https://pkg.go.dev/builtin#error))

ResizeVolume emergency Volume resize.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.ResizeVolumeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#ResizeVolumeRequest.
    	}
    	op, err := c.ResizeVolume(ctx, req)
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
    

### func (*Client) ResizeVolumeOperation 
    
    
    func (c *Client) ResizeVolumeOperation(name [string](https://pkg.go.dev/builtin#string)) *ResizeVolumeOperation

ResizeVolumeOperation returns a new ResizeVolumeOperation from a given name. The name must be that of a previously created ResizeVolumeOperation, possibly from a different process.

### func (*Client) RestoreVolumeSnapshot 
    
    
    func (c *Client) RestoreVolumeSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[RestoreVolumeSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_RestoreVolumeSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestoreVolumeSnapshotOperation, [error](https://pkg.go.dev/builtin#error))

RestoreVolumeSnapshot uses the specified snapshot to restore its parent volume. Returns INVALID_ARGUMENT if called for a non-boot volume.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.RestoreVolumeSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#RestoreVolumeSnapshotRequest.
    	}
    	op, err := c.RestoreVolumeSnapshot(ctx, req)
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
    

### func (*Client) RestoreVolumeSnapshotOperation 
    
    
    func (c *Client) RestoreVolumeSnapshotOperation(name [string](https://pkg.go.dev/builtin#string)) *RestoreVolumeSnapshotOperation

RestoreVolumeSnapshotOperation returns a new RestoreVolumeSnapshotOperation from a given name. The name must be that of a previously created RestoreVolumeSnapshotOperation, possibly from a different process.

### func (*Client) StartInstance 
    
    
    func (c *Client) StartInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[StartInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_StartInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StartInstanceOperation, [error](https://pkg.go.dev/builtin#error))

StartInstance starts a server that was shutdown.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.StartInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#StartInstanceRequest.
    	}
    	op, err := c.StartInstance(ctx, req)
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
    

### func (*Client) StartInstanceOperation 
    
    
    func (c *Client) StartInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *StartInstanceOperation

StartInstanceOperation returns a new StartInstanceOperation from a given name. The name must be that of a previously created StartInstanceOperation, possibly from a different process.

### func (*Client) StopInstance 
    
    
    func (c *Client) StopInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[StopInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_StopInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StopInstanceOperation, [error](https://pkg.go.dev/builtin#error))

StopInstance stop a running server.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.StopInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#StopInstanceRequest.
    	}
    	op, err := c.StopInstance(ctx, req)
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
    

### func (*Client) StopInstanceOperation 
    
    
    func (c *Client) StopInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *StopInstanceOperation

StopInstanceOperation returns a new StopInstanceOperation from a given name. The name must be that of a previously created StopInstanceOperation, possibly from a different process.

### func (*Client) SubmitProvisioningConfig 
    
    
    func (c *Client) SubmitProvisioningConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[SubmitProvisioningConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_SubmitProvisioningConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[SubmitProvisioningConfigResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_SubmitProvisioningConfigResponse), [error](https://pkg.go.dev/builtin#error))

SubmitProvisioningConfig submit a provisiong configuration for a given project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.SubmitProvisioningConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#SubmitProvisioningConfigRequest.
    	}
    	resp, err := c.SubmitProvisioningConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateInstance 
    
    
    func (c *Client) UpdateInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[UpdateInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_UpdateInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateInstanceOperation, [error](https://pkg.go.dev/builtin#error))

UpdateInstance update details of a single server.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.UpdateInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#UpdateInstanceRequest.
    	}
    	op, err := c.UpdateInstance(ctx, req)
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
    

### func (*Client) UpdateInstanceOperation 
    
    
    func (c *Client) UpdateInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateInstanceOperation

UpdateInstanceOperation returns a new UpdateInstanceOperation from a given name. The name must be that of a previously created UpdateInstanceOperation, possibly from a different process.

### func (*Client) UpdateNetwork 
    
    
    func (c *Client) UpdateNetwork(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[UpdateNetworkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_UpdateNetworkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateNetworkOperation, [error](https://pkg.go.dev/builtin#error))

UpdateNetwork update details of a single network.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.UpdateNetworkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#UpdateNetworkRequest.
    	}
    	op, err := c.UpdateNetwork(ctx, req)
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
    

### func (*Client) UpdateNetworkOperation 
    
    
    func (c *Client) UpdateNetworkOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateNetworkOperation

UpdateNetworkOperation returns a new UpdateNetworkOperation from a given name. The name must be that of a previously created UpdateNetworkOperation, possibly from a different process.

### func (*Client) UpdateNfsShare 
    
    
    func (c *Client) UpdateNfsShare(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[UpdateNfsShareRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_UpdateNfsShareRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateNfsShareOperation, [error](https://pkg.go.dev/builtin#error))

UpdateNfsShare update details of a single NFS share.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.UpdateNfsShareRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#UpdateNfsShareRequest.
    	}
    	op, err := c.UpdateNfsShare(ctx, req)
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
    

### func (*Client) UpdateNfsShareOperation 
    
    
    func (c *Client) UpdateNfsShareOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateNfsShareOperation

UpdateNfsShareOperation returns a new UpdateNfsShareOperation from a given name. The name must be that of a previously created UpdateNfsShareOperation, possibly from a different process.

### func (*Client) UpdateProvisioningConfig 
    
    
    func (c *Client) UpdateProvisioningConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[UpdateProvisioningConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_UpdateProvisioningConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ProvisioningConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ProvisioningConfig), [error](https://pkg.go.dev/builtin#error))

UpdateProvisioningConfig update existing ProvisioningConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.UpdateProvisioningConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#UpdateProvisioningConfigRequest.
    	}
    	resp, err := c.UpdateProvisioningConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateVolume 
    
    
    func (c *Client) UpdateVolume(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[UpdateVolumeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_UpdateVolumeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateVolumeOperation, [error](https://pkg.go.dev/builtin#error))

UpdateVolume update details of a single storage volume.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	baremetalsolution "cloud.google.com/go/baremetalsolution/apiv2"
    	baremetalsolutionpb "cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := baremetalsolution.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2.html#cloud_google_com_go_baremetalsolution_apiv2_Client_Close)()
    
    	req := &baremetalsolutionpb.UpdateVolumeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb#UpdateVolumeRequest.
    	}
    	op, err := c.UpdateVolume(ctx, req)
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
    

### func (*Client) UpdateVolumeOperation 
    
    
    func (c *Client) UpdateVolumeOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateVolumeOperation

UpdateVolumeOperation returns a new UpdateVolumeOperation from a given name. The name must be that of a previously created UpdateVolumeOperation, possibly from a different process.

## CreateNfsShareOperation
    
    
    type CreateNfsShareOperation struct {
    	// contains filtered or unexported fields
    }

CreateNfsShareOperation manages a long-running operation from CreateNfsShare.

### func (*CreateNfsShareOperation) Done 
    
    
    func (op *CreateNfsShareOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateNfsShareOperation) Metadata 
    
    
    func (op *CreateNfsShareOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateNfsShareOperation) Name 
    
    
    func (op *CreateNfsShareOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateNfsShareOperation) Poll 
    
    
    func (op *CreateNfsShareOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateNfsShareOperation) Wait 
    
    
    func (op *CreateNfsShareOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteNfsShareOperation
    
    
    type DeleteNfsShareOperation struct {
    	// contains filtered or unexported fields
    }

DeleteNfsShareOperation manages a long-running operation from DeleteNfsShare.

### func (*DeleteNfsShareOperation) Done 
    
    
    func (op *DeleteNfsShareOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteNfsShareOperation) Metadata 
    
    
    func (op *DeleteNfsShareOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteNfsShareOperation) Name 
    
    
    func (op *DeleteNfsShareOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteNfsShareOperation) Poll 
    
    
    func (op *DeleteNfsShareOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteNfsShareOperation) Wait 
    
    
    func (op *DeleteNfsShareOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DetachLunOperation
    
    
    type DetachLunOperation struct {
    	// contains filtered or unexported fields
    }

DetachLunOperation manages a long-running operation from DetachLun.

### func (*DetachLunOperation) Done 
    
    
    func (op *DetachLunOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DetachLunOperation) Metadata 
    
    
    func (op *DetachLunOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DetachLunOperation) Name 
    
    
    func (op *DetachLunOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DetachLunOperation) Poll 
    
    
    func (op *DetachLunOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DetachLunOperation) Wait 
    
    
    func (op *DetachLunOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DisableInteractiveSerialConsoleOperation
    
    
    type DisableInteractiveSerialConsoleOperation struct {
    	// contains filtered or unexported fields
    }

DisableInteractiveSerialConsoleOperation manages a long-running operation from DisableInteractiveSerialConsole.

### func (*DisableInteractiveSerialConsoleOperation) Done 
    
    
    func (op *DisableInteractiveSerialConsoleOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DisableInteractiveSerialConsoleOperation) Metadata 
    
    
    func (op *DisableInteractiveSerialConsoleOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DisableInteractiveSerialConsoleOperation) Name 
    
    
    func (op *DisableInteractiveSerialConsoleOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DisableInteractiveSerialConsoleOperation) Poll 
    
    
    func (op *DisableInteractiveSerialConsoleOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DisableInteractiveSerialConsoleResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DisableInteractiveSerialConsoleResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DisableInteractiveSerialConsoleOperation) Wait 
    
    
    func (op *DisableInteractiveSerialConsoleOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[DisableInteractiveSerialConsoleResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_DisableInteractiveSerialConsoleResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EnableInteractiveSerialConsoleOperation
    
    
    type EnableInteractiveSerialConsoleOperation struct {
    	// contains filtered or unexported fields
    }

EnableInteractiveSerialConsoleOperation manages a long-running operation from EnableInteractiveSerialConsole.

### func (*EnableInteractiveSerialConsoleOperation) Done 
    
    
    func (op *EnableInteractiveSerialConsoleOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*EnableInteractiveSerialConsoleOperation) Metadata 
    
    
    func (op *EnableInteractiveSerialConsoleOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*EnableInteractiveSerialConsoleOperation) Name 
    
    
    func (op *EnableInteractiveSerialConsoleOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*EnableInteractiveSerialConsoleOperation) Poll 
    
    
    func (op *EnableInteractiveSerialConsoleOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[EnableInteractiveSerialConsoleResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_EnableInteractiveSerialConsoleResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*EnableInteractiveSerialConsoleOperation) Wait 
    
    
    func (op *EnableInteractiveSerialConsoleOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[EnableInteractiveSerialConsoleResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_EnableInteractiveSerialConsoleResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EvictLunOperation
    
    
    type EvictLunOperation struct {
    	// contains filtered or unexported fields
    }

EvictLunOperation manages a long-running operation from EvictLun.

### func (*EvictLunOperation) Done 
    
    
    func (op *EvictLunOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*EvictLunOperation) Metadata 
    
    
    func (op *EvictLunOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*EvictLunOperation) Name 
    
    
    func (op *EvictLunOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*EvictLunOperation) Poll 
    
    
    func (op *EvictLunOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*EvictLunOperation) Wait 
    
    
    func (op *EvictLunOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EvictVolumeOperation
    
    
    type EvictVolumeOperation struct {
    	// contains filtered or unexported fields
    }

EvictVolumeOperation manages a long-running operation from EvictVolume.

### func (*EvictVolumeOperation) Done 
    
    
    func (op *EvictVolumeOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*EvictVolumeOperation) Metadata 
    
    
    func (op *EvictVolumeOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*EvictVolumeOperation) Name 
    
    
    func (op *EvictVolumeOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*EvictVolumeOperation) Poll 
    
    
    func (op *EvictVolumeOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*EvictVolumeOperation) Wait 
    
    
    func (op *EvictVolumeOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## InstanceIterator
    
    
    type InstanceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.Instance, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

InstanceIterator manages a stream of *baremetalsolutionpb.Instance.

### func (*InstanceIterator) All 
    
    
    func (it *InstanceIterator) All() iter.Seq2[*baremetalsolutionpb.Instance, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*InstanceIterator) Next 
    
    
    func (it *InstanceIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*InstanceIterator) PageInfo 
    
    
    func (it *InstanceIterator) PageInfo() *iterator.PageInfo

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

## LunIterator
    
    
    type LunIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.Lun, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

LunIterator manages a stream of *baremetalsolutionpb.Lun.

### func (*LunIterator) All 
    
    
    func (it *LunIterator) All() iter.Seq2[*baremetalsolutionpb.Lun, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*LunIterator) Next 
    
    
    func (it *LunIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Lun](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Lun), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*LunIterator) PageInfo 
    
    
    func (it *LunIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## NetworkIterator
    
    
    type NetworkIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.Network, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

NetworkIterator manages a stream of *baremetalsolutionpb.Network.

### func (*NetworkIterator) All 
    
    
    func (it *NetworkIterator) All() iter.Seq2[*baremetalsolutionpb.Network, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*NetworkIterator) Next 
    
    
    func (it *NetworkIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Network](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Network), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*NetworkIterator) PageInfo 
    
    
    func (it *NetworkIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## NfsShareIterator
    
    
    type NfsShareIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.NfsShare, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

NfsShareIterator manages a stream of *baremetalsolutionpb.NfsShare.

### func (*NfsShareIterator) All 
    
    
    func (it *NfsShareIterator) All() iter.Seq2[*baremetalsolutionpb.NfsShare, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*NfsShareIterator) Next 
    
    
    func (it *NfsShareIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*NfsShareIterator) PageInfo 
    
    
    func (it *NfsShareIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## OSImageIterator
    
    
    type OSImageIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.OSImage, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

OSImageIterator manages a stream of *baremetalsolutionpb.OSImage.

### func (*OSImageIterator) All 
    
    
    func (it *OSImageIterator) All() iter.Seq2[*baremetalsolutionpb.OSImage, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*OSImageIterator) Next 
    
    
    func (it *OSImageIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OSImage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OSImage), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*OSImageIterator) PageInfo 
    
    
    func (it *OSImageIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ProvisioningQuotaIterator
    
    
    type ProvisioningQuotaIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.ProvisioningQuota, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ProvisioningQuotaIterator manages a stream of *baremetalsolutionpb.ProvisioningQuota.

### func (*ProvisioningQuotaIterator) All 
    
    
    func (it *ProvisioningQuotaIterator) All() iter.Seq2[*baremetalsolutionpb.ProvisioningQuota, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ProvisioningQuotaIterator) Next 
    
    
    func (it *ProvisioningQuotaIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ProvisioningQuota](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ProvisioningQuota), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ProvisioningQuotaIterator) PageInfo 
    
    
    func (it *ProvisioningQuotaIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ResetInstanceOperation
    
    
    type ResetInstanceOperation struct {
    	// contains filtered or unexported fields
    }

ResetInstanceOperation manages a long-running operation from ResetInstance.

### func (*ResetInstanceOperation) Done 
    
    
    func (op *ResetInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ResetInstanceOperation) Metadata 
    
    
    func (op *ResetInstanceOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ResetInstanceOperation) Name 
    
    
    func (op *ResetInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ResetInstanceOperation) Poll 
    
    
    func (op *ResetInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ResetInstanceResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ResetInstanceResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ResetInstanceOperation) Wait 
    
    
    func (op *ResetInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[ResetInstanceResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_ResetInstanceResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ResizeVolumeOperation
    
    
    type ResizeVolumeOperation struct {
    	// contains filtered or unexported fields
    }

ResizeVolumeOperation manages a long-running operation from ResizeVolume.

### func (*ResizeVolumeOperation) Done 
    
    
    func (op *ResizeVolumeOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ResizeVolumeOperation) Metadata 
    
    
    func (op *ResizeVolumeOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ResizeVolumeOperation) Name 
    
    
    func (op *ResizeVolumeOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ResizeVolumeOperation) Poll 
    
    
    func (op *ResizeVolumeOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ResizeVolumeOperation) Wait 
    
    
    func (op *ResizeVolumeOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RestoreVolumeSnapshotOperation
    
    
    type RestoreVolumeSnapshotOperation struct {
    	// contains filtered or unexported fields
    }

RestoreVolumeSnapshotOperation manages a long-running operation from RestoreVolumeSnapshot.

### func (*RestoreVolumeSnapshotOperation) Done 
    
    
    func (op *RestoreVolumeSnapshotOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RestoreVolumeSnapshotOperation) Metadata 
    
    
    func (op *RestoreVolumeSnapshotOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RestoreVolumeSnapshotOperation) Name 
    
    
    func (op *RestoreVolumeSnapshotOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RestoreVolumeSnapshotOperation) Poll 
    
    
    func (op *RestoreVolumeSnapshotOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[VolumeSnapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_VolumeSnapshot), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RestoreVolumeSnapshotOperation) Wait 
    
    
    func (op *RestoreVolumeSnapshotOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[VolumeSnapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_VolumeSnapshot), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SSHKeyIterator
    
    
    type SSHKeyIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.SSHKey, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SSHKeyIterator manages a stream of *baremetalsolutionpb.SSHKey.

### func (*SSHKeyIterator) All 
    
    
    func (it *SSHKeyIterator) All() iter.Seq2[*baremetalsolutionpb.SSHKey, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SSHKeyIterator) Next 
    
    
    func (it *SSHKeyIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[SSHKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_SSHKey), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SSHKeyIterator) PageInfo 
    
    
    func (it *SSHKeyIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## StartInstanceOperation
    
    
    type StartInstanceOperation struct {
    	// contains filtered or unexported fields
    }

StartInstanceOperation manages a long-running operation from StartInstance.

### func (*StartInstanceOperation) Done 
    
    
    func (op *StartInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StartInstanceOperation) Metadata 
    
    
    func (op *StartInstanceOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StartInstanceOperation) Name 
    
    
    func (op *StartInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StartInstanceOperation) Poll 
    
    
    func (op *StartInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[StartInstanceResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_StartInstanceResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StartInstanceOperation) Wait 
    
    
    func (op *StartInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[StartInstanceResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_StartInstanceResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StopInstanceOperation
    
    
    type StopInstanceOperation struct {
    	// contains filtered or unexported fields
    }

StopInstanceOperation manages a long-running operation from StopInstance.

### func (*StopInstanceOperation) Done 
    
    
    func (op *StopInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StopInstanceOperation) Metadata 
    
    
    func (op *StopInstanceOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StopInstanceOperation) Name 
    
    
    func (op *StopInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StopInstanceOperation) Poll 
    
    
    func (op *StopInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[StopInstanceResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_StopInstanceResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StopInstanceOperation) Wait 
    
    
    func (op *StopInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[StopInstanceResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_StopInstanceResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateInstanceOperation
    
    
    type UpdateInstanceOperation struct {
    	// contains filtered or unexported fields
    }

UpdateInstanceOperation manages a long-running operation from UpdateInstance.

### func (*UpdateInstanceOperation) Done 
    
    
    func (op *UpdateInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateInstanceOperation) Metadata 
    
    
    func (op *UpdateInstanceOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateInstanceOperation) Name 
    
    
    func (op *UpdateInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateInstanceOperation) Poll 
    
    
    func (op *UpdateInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateInstanceOperation) Wait 
    
    
    func (op *UpdateInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateNetworkOperation
    
    
    type UpdateNetworkOperation struct {
    	// contains filtered or unexported fields
    }

UpdateNetworkOperation manages a long-running operation from UpdateNetwork.

### func (*UpdateNetworkOperation) Done 
    
    
    func (op *UpdateNetworkOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateNetworkOperation) Metadata 
    
    
    func (op *UpdateNetworkOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateNetworkOperation) Name 
    
    
    func (op *UpdateNetworkOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateNetworkOperation) Poll 
    
    
    func (op *UpdateNetworkOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Network](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Network), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateNetworkOperation) Wait 
    
    
    func (op *UpdateNetworkOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Network](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Network), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateNfsShareOperation
    
    
    type UpdateNfsShareOperation struct {
    	// contains filtered or unexported fields
    }

UpdateNfsShareOperation manages a long-running operation from UpdateNfsShare.

### func (*UpdateNfsShareOperation) Done 
    
    
    func (op *UpdateNfsShareOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateNfsShareOperation) Metadata 
    
    
    func (op *UpdateNfsShareOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateNfsShareOperation) Name 
    
    
    func (op *UpdateNfsShareOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateNfsShareOperation) Poll 
    
    
    func (op *UpdateNfsShareOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateNfsShareOperation) Wait 
    
    
    func (op *UpdateNfsShareOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[NfsShare](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_NfsShare), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateVolumeOperation
    
    
    type UpdateVolumeOperation struct {
    	// contains filtered or unexported fields
    }

UpdateVolumeOperation manages a long-running operation from UpdateVolume.

### func (*UpdateVolumeOperation) Done 
    
    
    func (op *UpdateVolumeOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateVolumeOperation) Metadata 
    
    
    func (op *UpdateVolumeOperation) Metadata() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateVolumeOperation) Name 
    
    
    func (op *UpdateVolumeOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateVolumeOperation) Poll 
    
    
    func (op *UpdateVolumeOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateVolumeOperation) Wait 
    
    
    func (op *UpdateVolumeOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## VolumeIterator
    
    
    type VolumeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.Volume, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

VolumeIterator manages a stream of *baremetalsolutionpb.Volume.

### func (*VolumeIterator) All 
    
    
    func (it *VolumeIterator) All() iter.Seq2[*baremetalsolutionpb.Volume, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*VolumeIterator) Next 
    
    
    func (it *VolumeIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[Volume](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_Volume), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*VolumeIterator) PageInfo 
    
    
    func (it *VolumeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## VolumeSnapshotIterator
    
    
    type VolumeSnapshotIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*baremetalsolutionpb.VolumeSnapshot, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

VolumeSnapshotIterator manages a stream of *baremetalsolutionpb.VolumeSnapshot.

### func (*VolumeSnapshotIterator) All 
    
    
    func (it *VolumeSnapshotIterator) All() iter.Seq2[*baremetalsolutionpb.VolumeSnapshot, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*VolumeSnapshotIterator) Next 
    
    
    func (it *VolumeSnapshotIterator) Next() (*[baremetalsolutionpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb).[VolumeSnapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/baremetalsolution/latest/apiv2/baremetalsolutionpb#cloud_google_com_go_baremetalsolution_apiv2_baremetalsolutionpb_VolumeSnapshot), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*VolumeSnapshotIterator) PageInfo 
    
    
    func (it *VolumeSnapshotIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
