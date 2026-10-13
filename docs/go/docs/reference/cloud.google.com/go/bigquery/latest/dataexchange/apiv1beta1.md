---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/
title: Analytics Hub API v1beta1 - Package cloud.google.com/go/bigquery/dataexchange/apiv1beta1 (v1.85.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:37.317615+00:00
---

# Analytics Hub API v1beta1 - Package cloud.google.com/go/bigquery/dataexchange/apiv1beta1 (v1.85.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Analytics Hub API v1beta1 - Package cloud.google.com/go/bigquery/dataexchange/apiv1beta1 (v1.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.85.0 (latest)  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.1  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.1  1.72.0  1.71.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.2  1.65.0  1.64.0  1.63.1  1.62.0  1.61.0  1.60.0  1.59.1  1.58.0  1.57.1  1.54.0  1.53.0  1.52.0  1.51.2  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.0  1.31.0  1.30.2  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1). 

Package dataexchange is an auto-generated package for the Analytics Hub API. 

Exchange data and analytics assets securely and efficiently.
    
    
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
    
    
    // go get cloud.google.com/go/bigquery/dataexchange/apiv1beta1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := dataexchange.NewAnalyticsHubClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &dataexchangepb.CreateDataExchangeRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#CreateDataExchangeRequest.
    }
    resp, err := c.CreateDataExchange(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewAnalyticsHubClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AnalyticsHubCallOptions
    
    
    type AnalyticsHubCallOptions struct {
    	ListDataExchanges    []gax.CallOption
    	ListOrgDataExchanges []gax.CallOption
    	GetDataExchange      []gax.CallOption
    	CreateDataExchange   []gax.CallOption
    	UpdateDataExchange   []gax.CallOption
    	DeleteDataExchange   []gax.CallOption
    	ListListings         []gax.CallOption
    	GetListing           []gax.CallOption
    	CreateListing        []gax.CallOption
    	UpdateListing        []gax.CallOption
    	DeleteListing        []gax.CallOption
    	SubscribeListing     []gax.CallOption
    	GetIamPolicy         []gax.CallOption
    	SetIamPolicy         []gax.CallOption
    	TestIamPermissions   []gax.CallOption
    	GetLocation          []gax.CallOption
    	ListLocations        []gax.CallOption
    }

AnalyticsHubCallOptions contains the retry settings for each method of AnalyticsHubClient.

## AnalyticsHubClient
    
    
    type AnalyticsHubClient struct {
    
    	// The call options for this service.
    	CallOptions *AnalyticsHubCallOptions
    	// contains filtered or unexported fields
    }

AnalyticsHubClient is a client for interacting with Analytics Hub API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The AnalyticsHubService API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

### func NewAnalyticsHubClient 
    
    
    func NewAnalyticsHubClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*AnalyticsHubClient, [error](https://pkg.go.dev/builtin#error))

NewAnalyticsHubClient creates a new analytics hub service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The AnalyticsHubService API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAnalyticsHubRESTClient 
    
    
    func NewAnalyticsHubRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*AnalyticsHubClient, [error](https://pkg.go.dev/builtin#error))

NewAnalyticsHubRESTClient creates a new analytics hub service rest client.

The AnalyticsHubService API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AnalyticsHubClient) Close 
    
    
    func (c *AnalyticsHubClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AnalyticsHubClient) Connection (deprecated)
    
    
    func (c *AnalyticsHubClient) Connection() *[grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConn](https://pkg.go.dev/google.golang.org/grpc#ClientConn)

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AnalyticsHubClient) CreateDataExchange 
    
    
    func (c *AnalyticsHubClient) CreateDataExchange(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[CreateDataExchangeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_CreateDataExchangeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[DataExchange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_DataExchange), [error](https://pkg.go.dev/builtin#error))

CreateDataExchange creates a new data exchange.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.CreateDataExchangeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#CreateDataExchangeRequest.
    	}
    	resp, err := c.CreateDataExchange(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) CreateListing 
    
    
    func (c *AnalyticsHubClient) CreateListing(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[CreateListingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_CreateListingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[Listing](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_Listing), [error](https://pkg.go.dev/builtin#error))

CreateListing creates a new listing.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.CreateListingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#CreateListingRequest.
    	}
    	resp, err := c.CreateListing(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) DeleteDataExchange 
    
    
    func (c *AnalyticsHubClient) DeleteDataExchange(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[DeleteDataExchangeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_DeleteDataExchangeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteDataExchange deletes an existing data exchange.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.DeleteDataExchangeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#DeleteDataExchangeRequest.
    	}
    	err = c.DeleteDataExchange(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AnalyticsHubClient) DeleteListing 
    
    
    func (c *AnalyticsHubClient) DeleteListing(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[DeleteListingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_DeleteListingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteListing deletes a listing.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.DeleteListingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#DeleteListingRequest.
    	}
    	err = c.DeleteListing(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AnalyticsHubClient) GetDataExchange 
    
    
    func (c *AnalyticsHubClient) GetDataExchange(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[GetDataExchangeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_GetDataExchangeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[DataExchange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_DataExchange), [error](https://pkg.go.dev/builtin#error))

GetDataExchange gets the details of a data exchange.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.GetDataExchangeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#GetDataExchangeRequest.
    	}
    	resp, err := c.GetDataExchange(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) GetIamPolicy 
    
    
    func (c *AnalyticsHubClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb).[GetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb).[Policy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb#cloud_google_com_go_iam_apiv1_iampb_Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the IAM policy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &iampb.[GetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest.
    	}
    	resp, err := c.[GetIamPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_GetIamPolicy)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) GetListing 
    
    
    func (c *AnalyticsHubClient) GetListing(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[GetListingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_GetListingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[Listing](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_Listing), [error](https://pkg.go.dev/builtin#error))

GetListing gets the details of a listing.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.GetListingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#GetListingRequest.
    	}
    	resp, err := c.GetListing(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) GetLocation 
    
    
    func (c *AnalyticsHubClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
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
    

### func (*AnalyticsHubClient) ListDataExchanges 
    
    
    func (c *AnalyticsHubClient) ListDataExchanges(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[ListDataExchangesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_ListDataExchangesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DataExchangeIterator

ListDataExchanges lists all data exchanges in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.ListDataExchangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#ListDataExchangesRequest.
    	}
    	it := c.ListDataExchanges(ctx, req)
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
    		_ = it.Response.(*dataexchangepb.ListDataExchangesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.ListDataExchangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#ListDataExchangesRequest.
    	}
    	for resp, err := range c.ListDataExchanges(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AnalyticsHubClient) ListListings 
    
    
    func (c *AnalyticsHubClient) ListListings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[ListListingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_ListListingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ListingIterator

ListListings lists all listings in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.ListListingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#ListListingsRequest.
    	}
    	it := c.ListListings(ctx, req)
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
    		_ = it.Response.(*dataexchangepb.ListListingsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.ListListingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#ListListingsRequest.
    	}
    	for resp, err := range c.ListListings(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AnalyticsHubClient) ListLocations 
    
    
    func (c *AnalyticsHubClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
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
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_ListLocations)(ctx, req)
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
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AnalyticsHubClient) ListOrgDataExchanges 
    
    
    func (c *AnalyticsHubClient) ListOrgDataExchanges(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[ListOrgDataExchangesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_ListOrgDataExchangesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DataExchangeIterator

ListOrgDataExchanges lists all data exchanges from projects in a given organization and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.ListOrgDataExchangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#ListOrgDataExchangesRequest.
    	}
    	it := c.ListOrgDataExchanges(ctx, req)
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
    		_ = it.Response.(*dataexchangepb.ListOrgDataExchangesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.ListOrgDataExchangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#ListOrgDataExchangesRequest.
    	}
    	for resp, err := range c.ListOrgDataExchanges(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AnalyticsHubClient) SetIamPolicy 
    
    
    func (c *AnalyticsHubClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb).[SetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb).[Policy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb#cloud_google_com_go_iam_apiv1_iampb_Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the IAM policy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &iampb.[SetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest.
    	}
    	resp, err := c.[SetIamPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_SetIamPolicy)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) SubscribeListing 
    
    
    func (c *AnalyticsHubClient) SubscribeListing(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[SubscribeListingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_SubscribeListingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[SubscribeListingResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_SubscribeListingResponse), [error](https://pkg.go.dev/builtin#error))

SubscribeListing subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber’s project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.SubscribeListingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#SubscribeListingRequest.
    	}
    	resp, err := c.SubscribeListing(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) TestIamPermissions 
    
    
    func (c *AnalyticsHubClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb).[TestIamPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb).[TestIamPermissionsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns the permissions that a caller has.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &iampb.[TestIamPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest.
    	}
    	resp, err := c.[TestIamPermissions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_TestIamPermissions)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) UpdateDataExchange 
    
    
    func (c *AnalyticsHubClient) UpdateDataExchange(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[UpdateDataExchangeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_UpdateDataExchangeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[DataExchange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_DataExchange), [error](https://pkg.go.dev/builtin#error))

UpdateDataExchange updates an existing data exchange.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.UpdateDataExchangeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#UpdateDataExchangeRequest.
    	}
    	resp, err := c.UpdateDataExchange(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AnalyticsHubClient) UpdateListing 
    
    
    func (c *AnalyticsHubClient) UpdateListing(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[UpdateListingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_UpdateListingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[Listing](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_Listing), [error](https://pkg.go.dev/builtin#error))

UpdateListing updates an existing listing.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataexchange "cloud.google.com/go/bigquery/dataexchange/apiv1beta1"
    	dataexchangepb "cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataexchange.[NewAnalyticsHubClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_NewAnalyticsHubClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1.html#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_AnalyticsHubClient_Close)()
    
    	req := &dataexchangepb.UpdateListingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/dataexchange/apiv1beta1/dataexchangepb#UpdateListingRequest.
    	}
    	resp, err := c.UpdateListing(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## DataExchangeIterator
    
    
    type DataExchangeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataexchangepb.DataExchange, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DataExchangeIterator manages a stream of *dataexchangepb.DataExchange.

### func (*DataExchangeIterator) All 
    
    
    func (it *DataExchangeIterator) All() iter.Seq2[*dataexchangepb.DataExchange, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DataExchangeIterator) Next 
    
    
    func (it *DataExchangeIterator) Next() (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[DataExchange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_DataExchange), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DataExchangeIterator) PageInfo 
    
    
    func (it *DataExchangeIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ListingIterator
    
    
    type ListingIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataexchangepb.Listing, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ListingIterator manages a stream of *dataexchangepb.Listing.

### func (*ListingIterator) All 
    
    
    func (it *ListingIterator) All() iter.Seq2[*dataexchangepb.Listing, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ListingIterator) Next 
    
    
    func (it *ListingIterator) Next() (*[dataexchangepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb).[Listing](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/dataexchange/apiv1beta1/dataexchangepb#cloud_google_com_go_bigquery_dataexchange_apiv1beta1_dataexchangepb_Listing), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ListingIterator) PageInfo 
    
    
    func (it *ListingIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

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
    
    
    func (it *LocationIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
