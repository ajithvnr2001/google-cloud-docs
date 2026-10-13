---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/
title: Cloud Quotas API v1beta - Package cloud.google.com/go/cloudquotas/apiv1beta (v1.13.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:08.043343+00:00
---

# Cloud Quotas API v1beta - Package cloud.google.com/go/cloudquotas/apiv1beta (v1.13.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Quotas API v1beta - Package cloud.google.com/go/cloudquotas/apiv1beta (v1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.4  1.2.1  1.1.2  1.0.4  0.2.1  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta). 

Package cloudquotas is an auto-generated package for the Cloud Quotas API. 

Cloud Quotas API provides Google Cloud service consumers with management and observability for resource usage, quotas, and restrictions of the services they consume.
    
    
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
    
    
    // go get cloud.google.com/go/cloudquotas/apiv1beta@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := cloudquotas.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &cloudquotaspb.CreateQuotaPreferenceRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#CreateQuotaPreferenceRequest.
    }
    resp, err := c.CreateQuotaPreference(ctx, req)
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
    	ListQuotaInfos        []gax.CallOption
    	GetQuotaInfo          []gax.CallOption
    	ListQuotaPreferences  []gax.CallOption
    	GetQuotaPreference    []gax.CallOption
    	CreateQuotaPreference []gax.CallOption
    	UpdateQuotaPreference []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Cloud Quotas API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.
    
    
    List/Get the metadata and current status of the quotas for a service.
    
    Create/Update quota preferencess that declare the preferred quota values.
    
    Check the status of a quota preference request.
    
    List/Get pending and historical quota preference.
    

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new cloud quotas client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.
    
    
    List/Get the metadata and current status of the quotas for a service.
    
    Create/Update quota preferencess that declare the preferred quota values.
    
    Check the status of a quota preference request.
    
    List/Get pending and historical quota preference.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new cloud quotas rest client.

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.
    
    
    List/Get the metadata and current status of the quotas for a service.
    
    Create/Update quota preferencess that declare the preferred quota values.
    
    Check the status of a quota preference request.
    
    List/Get pending and historical quota preference.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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

### func (*Client) CreateQuotaPreference 
    
    
    func (c *Client) CreateQuotaPreference(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_CreateQuotaPreferenceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaPreference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaPreference), [error](https://pkg.go.dev/builtin#error))

CreateQuotaPreference creates a new QuotaPreference that declares the desired value for a quota.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.CreateQuotaPreferenceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#CreateQuotaPreferenceRequest.
    	}
    	resp, err := c.CreateQuotaPreference(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetQuotaInfo 
    
    
    func (c *Client) GetQuotaInfo(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[GetQuotaInfoRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_GetQuotaInfoRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaInfo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaInfo), [error](https://pkg.go.dev/builtin#error))

GetQuotaInfo retrieve the QuotaInfo of a quota for a project, folder or organization.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.GetQuotaInfoRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#GetQuotaInfoRequest.
    	}
    	resp, err := c.GetQuotaInfo(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetQuotaPreference 
    
    
    func (c *Client) GetQuotaPreference(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[GetQuotaPreferenceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_GetQuotaPreferenceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaPreference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaPreference), [error](https://pkg.go.dev/builtin#error))

GetQuotaPreference gets details of a single QuotaPreference.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.GetQuotaPreferenceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#GetQuotaPreferenceRequest.
    	}
    	resp, err := c.GetQuotaPreference(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListQuotaInfos 
    
    
    func (c *Client) ListQuotaInfos(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[ListQuotaInfosRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_ListQuotaInfosRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *QuotaInfoIterator

ListQuotaInfos lists QuotaInfos of all quotas for a given project, folder or organization.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.ListQuotaInfosRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#ListQuotaInfosRequest.
    	}
    	it := c.ListQuotaInfos(ctx, req)
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
    		_ = it.Response.(*cloudquotaspb.ListQuotaInfosResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.ListQuotaInfosRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#ListQuotaInfosRequest.
    	}
    	for resp, err := range c.ListQuotaInfos(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListQuotaPreferences 
    
    
    func (c *Client) ListQuotaPreferences(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[ListQuotaPreferencesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_ListQuotaPreferencesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *QuotaPreferenceIterator

ListQuotaPreferences lists QuotaPreferences in a given project, folder or organization.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.ListQuotaPreferencesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#ListQuotaPreferencesRequest.
    	}
    	it := c.ListQuotaPreferences(ctx, req)
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
    		_ = it.Response.(*cloudquotaspb.ListQuotaPreferencesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.ListQuotaPreferencesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#ListQuotaPreferencesRequest.
    	}
    	for resp, err := range c.ListQuotaPreferences(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) UpdateQuotaPreference 
    
    
    func (c *Client) UpdateQuotaPreference(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_UpdateQuotaPreferenceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaPreference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaPreference), [error](https://pkg.go.dev/builtin#error))

UpdateQuotaPreference updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.UpdateQuotaPreferenceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#UpdateQuotaPreferenceRequest.
    	}
    	resp, err := c.UpdateQuotaPreference(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## QuotaAdjusterSettingsManagerCallOptions
    
    
    type QuotaAdjusterSettingsManagerCallOptions struct {
    	UpdateQuotaAdjusterSettings []gax.CallOption
    	GetQuotaAdjusterSettings    []gax.CallOption
    }

QuotaAdjusterSettingsManagerCallOptions contains the retry settings for each method of QuotaAdjusterSettingsManagerClient.

## QuotaAdjusterSettingsManagerClient
    
    
    type QuotaAdjusterSettingsManagerClient struct {
    
    	// The call options for this service.
    	CallOptions *QuotaAdjusterSettingsManagerCallOptions
    	// contains filtered or unexported fields
    }

QuotaAdjusterSettingsManagerClient is a client for interacting with Cloud Quotas API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The Quotas Adjuster Settings API is an infrastructure service for Google Cloud that lets service consumers view and update their quota adjuster settings.
    
    
    Update quota adjuster settings.
    
    Get the name of the configurations.
    

### func NewQuotaAdjusterSettingsManagerClient 
    
    
    func NewQuotaAdjusterSettingsManagerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*QuotaAdjusterSettingsManagerClient, [error](https://pkg.go.dev/builtin#error))

NewQuotaAdjusterSettingsManagerClient creates a new quota adjuster settings manager client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The Quotas Adjuster Settings API is an infrastructure service for Google Cloud that lets service consumers view and update their quota adjuster settings.
    
    
    Update quota adjuster settings.
    
    Get the name of the configurations.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.NewQuotaAdjusterSettingsManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewQuotaAdjusterSettingsManagerRESTClient 
    
    
    func NewQuotaAdjusterSettingsManagerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*QuotaAdjusterSettingsManagerClient, [error](https://pkg.go.dev/builtin#error))

NewQuotaAdjusterSettingsManagerRESTClient creates a new quota adjuster settings manager rest client.

The Quotas Adjuster Settings API is an infrastructure service for Google Cloud that lets service consumers view and update their quota adjuster settings.
    
    
    Update quota adjuster settings.
    
    Get the name of the configurations.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewQuotaAdjusterSettingsManagerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta.html#cloud_google_com_go_cloudquotas_apiv1beta_QuotaAdjusterSettingsManagerClient_NewQuotaAdjusterSettingsManagerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*QuotaAdjusterSettingsManagerClient) Close 
    
    
    func (c *QuotaAdjusterSettingsManagerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*QuotaAdjusterSettingsManagerClient) Connection (deprecated)
    
    
    func (c *QuotaAdjusterSettingsManagerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*QuotaAdjusterSettingsManagerClient) GetQuotaAdjusterSettings 
    
    
    func (c *QuotaAdjusterSettingsManagerClient) GetQuotaAdjusterSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_GetQuotaAdjusterSettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaAdjusterSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaAdjusterSettings), [error](https://pkg.go.dev/builtin#error))

GetQuotaAdjusterSettings gets the QuotaAdjusterSettings for the specified resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.NewQuotaAdjusterSettingsManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.GetQuotaAdjusterSettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#GetQuotaAdjusterSettingsRequest.
    	}
    	resp, err := c.GetQuotaAdjusterSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*QuotaAdjusterSettingsManagerClient) UpdateQuotaAdjusterSettings 
    
    
    func (c *QuotaAdjusterSettingsManagerClient) UpdateQuotaAdjusterSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_UpdateQuotaAdjusterSettingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaAdjusterSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaAdjusterSettings), [error](https://pkg.go.dev/builtin#error))

UpdateQuotaAdjusterSettings updates the QuotaAdjusterSettings for the specified resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1beta"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.NewQuotaAdjusterSettingsManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.UpdateQuotaAdjusterSettingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb#UpdateQuotaAdjusterSettingsRequest.
    	}
    	resp, err := c.UpdateQuotaAdjusterSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## QuotaInfoIterator
    
    
    type QuotaInfoIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cloudquotaspb.QuotaInfo, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

QuotaInfoIterator manages a stream of *cloudquotaspb.QuotaInfo.

### func (*QuotaInfoIterator) All 
    
    
    func (it *QuotaInfoIterator) All() iter.Seq2[*cloudquotaspb.QuotaInfo, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*QuotaInfoIterator) Next 
    
    
    func (it *QuotaInfoIterator) Next() (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaInfo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaInfo), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*QuotaInfoIterator) PageInfo 
    
    
    func (it *QuotaInfoIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## QuotaPreferenceIterator
    
    
    type QuotaPreferenceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cloudquotaspb.QuotaPreference, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

QuotaPreferenceIterator manages a stream of *cloudquotaspb.QuotaPreference.

### func (*QuotaPreferenceIterator) All 
    
    
    func (it *QuotaPreferenceIterator) All() iter.Seq2[*cloudquotaspb.QuotaPreference, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*QuotaPreferenceIterator) Next 
    
    
    func (it *QuotaPreferenceIterator) Next() (*[cloudquotaspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb).[QuotaPreference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1beta/cloudquotaspb#cloud_google_com_go_cloudquotas_apiv1beta_cloudquotaspb_QuotaPreference), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*QuotaPreferenceIterator) PageInfo 
    
    
    func (it *QuotaPreferenceIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
