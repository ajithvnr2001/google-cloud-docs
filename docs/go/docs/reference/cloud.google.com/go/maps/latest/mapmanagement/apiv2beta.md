---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/
title: Map Management API v2beta - Package cloud.google.com/go/maps/mapmanagement/apiv2beta (v1.43.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:30.658562+00:00
---

# Map Management API v2beta - Package cloud.google.com/go/maps/mapmanagement/apiv2beta (v1.43.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Map Management API v2beta - Package cloud.google.com/go/maps/mapmanagement/apiv2beta (v1.43.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.43.0 (latest)  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.1  1.20.4  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.0  1.12.1  1.11.7  1.10.0  1.9.0  1.8.0  1.7.3  1.6.4  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.0  0.5.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta). 

Package mapmanagement is an auto-generated package for the Map Management API. 

The Map Management API is a RESTful service that accepts HTTP requests for map styling data through a variety of methods. It returns formatted configuration data about map styling resources so that you can programmatically manage your Cloud-based map styles.
    
    
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
    
    
    // go get cloud.google.com/go/maps/mapmanagement/apiv2beta@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := mapmanagement.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &mapmanagementpb.CreateMapConfigRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#CreateMapConfigRequest.
    }
    resp, err := c.CreateMapConfig(ctx, req)
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
    	CreateMapConfig        []gax.CallOption
    	GetMapConfig           []gax.CallOption
    	ListMapConfigs         []gax.CallOption
    	UpdateMapConfig        []gax.CallOption
    	DeleteMapConfig        []gax.CallOption
    	CreateStyleConfig      []gax.CallOption
    	GetStyleConfig         []gax.CallOption
    	ListStyleConfigs       []gax.CallOption
    	UpdateStyleConfig      []gax.CallOption
    	DeleteStyleConfig      []gax.CallOption
    	CreateMapContextConfig []gax.CallOption
    	GetMapContextConfig    []gax.CallOption
    	ListMapContextConfigs  []gax.CallOption
    	UpdateMapContextConfig []gax.CallOption
    	DeleteMapContextConfig []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Map Management API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The Map Management API uses your inputs to create and manage Google Cloud based styling resources for Google Maps.

Using this API, you can can create and manage MapConfigs (Map IDs), StyleConfigs (JSON-based styling), and MapContextConfigs (associations between styles, datasets, and map variants).

This API offers features through three channels:
    
    
    v2alpha: Experimental features.
    
    v2beta: Preview features, recommended for early adoption.
    
    v2: General Availability (GA) features.
    

Capabilities described here are generally available across both the v2alpha and v2beta endpoints.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new map management client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The Map Management API uses your inputs to create and manage Google Cloud based styling resources for Google Maps.

Using this API, you can can create and manage MapConfigs (Map IDs), StyleConfigs (JSON-based styling), and MapContextConfigs (associations between styles, datasets, and map variants).

This API offers features through three channels:
    
    
    v2alpha: Experimental features.
    
    v2beta: Preview features, recommended for early adoption.
    
    v2: General Availability (GA) features.
    

Capabilities described here are generally available across both the v2alpha and v2beta endpoints.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new map management rest client.

The Map Management API uses your inputs to create and manage Google Cloud based styling resources for Google Maps.

Using this API, you can can create and manage MapConfigs (Map IDs), StyleConfigs (JSON-based styling), and MapContextConfigs (associations between styles, datasets, and map variants).

This API offers features through three channels:
    
    
    v2alpha: Experimental features.
    
    v2beta: Preview features, recommended for early adoption.
    
    v2: General Availability (GA) features.
    

Capabilities described here are generally available across both the v2alpha and v2beta endpoints.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
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

### func (*Client) CreateMapConfig 
    
    
    func (c *Client) CreateMapConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[CreateMapConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_CreateMapConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapConfig), [error](https://pkg.go.dev/builtin#error))

CreateMapConfig creates a MapConfig in a project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.CreateMapConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#CreateMapConfigRequest.
    	}
    	resp, err := c.CreateMapConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateMapContextConfig 
    
    
    func (c *Client) CreateMapContextConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[CreateMapContextConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_CreateMapContextConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapContextConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapContextConfig), [error](https://pkg.go.dev/builtin#error))

CreateMapContextConfig creates a MapContextConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.CreateMapContextConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#CreateMapContextConfigRequest.
    	}
    	resp, err := c.CreateMapContextConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateStyleConfig 
    
    
    func (c *Client) CreateStyleConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[CreateStyleConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_CreateStyleConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[StyleConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_StyleConfig), [error](https://pkg.go.dev/builtin#error))

CreateStyleConfig creates a StyleConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.CreateStyleConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#CreateStyleConfigRequest.
    	}
    	resp, err := c.CreateStyleConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) DeleteMapConfig 
    
    
    func (c *Client) DeleteMapConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[DeleteMapConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_DeleteMapConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteMapConfig deletes a MapConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.DeleteMapConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#DeleteMapConfigRequest.
    	}
    	err = c.DeleteMapConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteMapContextConfig 
    
    
    func (c *Client) DeleteMapContextConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[DeleteMapContextConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_DeleteMapContextConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteMapContextConfig deletes a MapContextConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.DeleteMapContextConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#DeleteMapContextConfigRequest.
    	}
    	err = c.DeleteMapContextConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteStyleConfig 
    
    
    func (c *Client) DeleteStyleConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[DeleteStyleConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_DeleteStyleConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteStyleConfig deletes a StyleConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.DeleteStyleConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#DeleteStyleConfigRequest.
    	}
    	err = c.DeleteStyleConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) GetMapConfig 
    
    
    func (c *Client) GetMapConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[GetMapConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_GetMapConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapConfig), [error](https://pkg.go.dev/builtin#error))

GetMapConfig gets a MapConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.GetMapConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#GetMapConfigRequest.
    	}
    	resp, err := c.GetMapConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetMapContextConfig 
    
    
    func (c *Client) GetMapContextConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[GetMapContextConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_GetMapContextConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapContextConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapContextConfig), [error](https://pkg.go.dev/builtin#error))

GetMapContextConfig gets a MapContextConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.GetMapContextConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#GetMapContextConfigRequest.
    	}
    	resp, err := c.GetMapContextConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetStyleConfig 
    
    
    func (c *Client) GetStyleConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[GetStyleConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_GetStyleConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[StyleConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_StyleConfig), [error](https://pkg.go.dev/builtin#error))

GetStyleConfig gets a StyleConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.GetStyleConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#GetStyleConfigRequest.
    	}
    	resp, err := c.GetStyleConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListMapConfigs 
    
    
    func (c *Client) ListMapConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[ListMapConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_ListMapConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *MapConfigIterator

ListMapConfigs lists MapConfigs for a project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.ListMapConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#ListMapConfigsRequest.
    	}
    	it := c.ListMapConfigs(ctx, req)
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
    		_ = it.Response.(*mapmanagementpb.ListMapConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.ListMapConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#ListMapConfigsRequest.
    	}
    	for resp, err := range c.ListMapConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListMapContextConfigs 
    
    
    func (c *Client) ListMapContextConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[ListMapContextConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_ListMapContextConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *MapContextConfigIterator

ListMapContextConfigs lists MapContextConfigs.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.ListMapContextConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#ListMapContextConfigsRequest.
    	}
    	it := c.ListMapContextConfigs(ctx, req)
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
    		_ = it.Response.(*mapmanagementpb.ListMapContextConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.ListMapContextConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#ListMapContextConfigsRequest.
    	}
    	for resp, err := range c.ListMapContextConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListStyleConfigs 
    
    
    func (c *Client) ListStyleConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[ListStyleConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_ListStyleConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *StyleConfigIterator

ListStyleConfigs lists StyleConfigs.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.ListStyleConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#ListStyleConfigsRequest.
    	}
    	it := c.ListStyleConfigs(ctx, req)
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
    		_ = it.Response.(*mapmanagementpb.ListStyleConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.ListStyleConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#ListStyleConfigsRequest.
    	}
    	for resp, err := range c.ListStyleConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) UpdateMapConfig 
    
    
    func (c *Client) UpdateMapConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[UpdateMapConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_UpdateMapConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapConfig), [error](https://pkg.go.dev/builtin#error))

UpdateMapConfig updates a MapConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.UpdateMapConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#UpdateMapConfigRequest.
    	}
    	resp, err := c.UpdateMapConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateMapContextConfig 
    
    
    func (c *Client) UpdateMapContextConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[UpdateMapContextConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_UpdateMapContextConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapContextConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapContextConfig), [error](https://pkg.go.dev/builtin#error))

UpdateMapContextConfig updates a MapContextConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.UpdateMapContextConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#UpdateMapContextConfigRequest.
    	}
    	resp, err := c.UpdateMapContextConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateStyleConfig 
    
    
    func (c *Client) UpdateStyleConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[UpdateStyleConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_UpdateStyleConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[StyleConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_StyleConfig), [error](https://pkg.go.dev/builtin#error))

UpdateStyleConfig updates a StyleConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	mapmanagement "cloud.google.com/go/maps/mapmanagement/apiv2beta"
    	mapmanagementpb "cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := mapmanagement.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta.html#cloud_google_com_go_maps_mapmanagement_apiv2beta_Client_Close)()
    
    	req := &mapmanagementpb.UpdateStyleConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/maps/mapmanagement/apiv2beta/mapmanagementpb#UpdateStyleConfigRequest.
    	}
    	resp, err := c.UpdateStyleConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## MapConfigIterator
    
    
    type MapConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*mapmanagementpb.MapConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

MapConfigIterator manages a stream of *mapmanagementpb.MapConfig.

### func (*MapConfigIterator) All 
    
    
    func (it *MapConfigIterator) All() iter.Seq2[*mapmanagementpb.MapConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*MapConfigIterator) Next 
    
    
    func (it *MapConfigIterator) Next() (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*MapConfigIterator) PageInfo 
    
    
    func (it *MapConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## MapContextConfigIterator
    
    
    type MapContextConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*mapmanagementpb.MapContextConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

MapContextConfigIterator manages a stream of *mapmanagementpb.MapContextConfig.

### func (*MapContextConfigIterator) All 
    
    
    func (it *MapContextConfigIterator) All() iter.Seq2[*mapmanagementpb.MapContextConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*MapContextConfigIterator) Next 
    
    
    func (it *MapContextConfigIterator) Next() (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[MapContextConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_MapContextConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*MapContextConfigIterator) PageInfo 
    
    
    func (it *MapContextConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## StyleConfigIterator
    
    
    type StyleConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*mapmanagementpb.StyleConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

StyleConfigIterator manages a stream of *mapmanagementpb.StyleConfig.

### func (*StyleConfigIterator) All 
    
    
    func (it *StyleConfigIterator) All() iter.Seq2[*mapmanagementpb.StyleConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*StyleConfigIterator) Next 
    
    
    func (it *StyleConfigIterator) Next() (*[mapmanagementpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb).[StyleConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/maps/latest/mapmanagement/apiv2beta/mapmanagementpb#cloud_google_com_go_maps_mapmanagement_apiv2beta_mapmanagementpb_StyleConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*StyleConfigIterator) PageInfo 
    
    
    func (it *StyleConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
