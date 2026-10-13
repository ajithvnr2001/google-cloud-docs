---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/
title: Vertex AI Search for commerce API v2 - Package cloud.google.com/go/retail/apiv2 (v1.36.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:10.071849+00:00
---

# Vertex AI Search for commerce API v2 - Package cloud.google.com/go/retail/apiv2 (v1.36.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Vertex AI Search for commerce API v2 - Package cloud.google.com/go/retail/apiv2 (v1.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.36.0 (latest)  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.1  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.4  1.18.1  1.17.5  1.16.2  1.15.1  1.14.4  1.13.1  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/retail/apiv2). 

Package retail is an auto-generated package for the Vertex AI Search for commerce API. 

AI Commerce Search API is made up of Search, Browse and Recommendations. These discovery AI solutions help you implement personalized search, browse and recommendations, based on machine learning models, across your websites and mobile applications. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/retail/apiv2@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := retail.NewAnalyticsClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &retailpb.ExportAnalyticsMetricsRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ExportAnalyticsMetricsRequest.
    }
    op, err := c.ExportAnalyticsMetrics(ctx, req)
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

The ctx passed to NewAnalyticsClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AddFulfillmentPlacesOperation
    
    
    type AddFulfillmentPlacesOperation struct {
    	// contains filtered or unexported fields
    }

AddFulfillmentPlacesOperation manages a long-running operation from AddFulfillmentPlaces.

### func (*AddFulfillmentPlacesOperation) Done 
    
    
    func (op *AddFulfillmentPlacesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*AddFulfillmentPlacesOperation) Metadata 
    
    
    func (op *AddFulfillmentPlacesOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddFulfillmentPlacesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddFulfillmentPlacesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*AddFulfillmentPlacesOperation) Name 
    
    
    func (op *AddFulfillmentPlacesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*AddFulfillmentPlacesOperation) Poll 
    
    
    func (op *AddFulfillmentPlacesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddFulfillmentPlacesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddFulfillmentPlacesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*AddFulfillmentPlacesOperation) Wait 
    
    
    func (op *AddFulfillmentPlacesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddFulfillmentPlacesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddFulfillmentPlacesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## AddLocalInventoriesOperation
    
    
    type AddLocalInventoriesOperation struct {
    	// contains filtered or unexported fields
    }

AddLocalInventoriesOperation manages a long-running operation from AddLocalInventories.

### func (*AddLocalInventoriesOperation) Done 
    
    
    func (op *AddLocalInventoriesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*AddLocalInventoriesOperation) Metadata 
    
    
    func (op *AddLocalInventoriesOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddLocalInventoriesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddLocalInventoriesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*AddLocalInventoriesOperation) Name 
    
    
    func (op *AddLocalInventoriesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*AddLocalInventoriesOperation) Poll 
    
    
    func (op *AddLocalInventoriesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddLocalInventoriesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddLocalInventoriesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*AddLocalInventoriesOperation) Wait 
    
    
    func (op *AddLocalInventoriesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddLocalInventoriesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddLocalInventoriesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## AnalyticsCallOptions
    
    
    type AnalyticsCallOptions struct {
    	ExportAnalyticsMetrics []gax.CallOption
    	GetOperation           []gax.CallOption
    	ListOperations         []gax.CallOption
    }

AnalyticsCallOptions contains the retry settings for each method of AnalyticsClient.

## AnalyticsClient
    
    
    type AnalyticsClient struct {
    
    	// The call options for this service.
    	CallOptions *AnalyticsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

AnalyticsClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing & accessing retail search business metric. Retail recommendation business metric is currently not available.

### func NewAnalyticsClient 
    
    
    func NewAnalyticsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AnalyticsClient, [error](https://pkg.go.dev/builtin#error))

NewAnalyticsClient creates a new analytics service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing & accessing retail search business metric. Retail recommendation business metric is currently not available.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewAnalyticsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_AnalyticsClient_NewAnalyticsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAnalyticsRESTClient 
    
    
    func NewAnalyticsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AnalyticsClient, [error](https://pkg.go.dev/builtin#error))

NewAnalyticsRESTClient creates a new analytics service rest client.

Service for managing & accessing retail search business metric. Retail recommendation business metric is currently not available.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewAnalyticsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_AnalyticsClient_NewAnalyticsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AnalyticsClient) Close 
    
    
    func (c *AnalyticsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AnalyticsClient) Connection (deprecated)
    
    
    func (c *AnalyticsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AnalyticsClient) ExportAnalyticsMetrics 
    
    
    func (c *AnalyticsClient) ExportAnalyticsMetrics(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ExportAnalyticsMetricsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ExportAnalyticsMetricsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportAnalyticsMetricsOperation, [error](https://pkg.go.dev/builtin#error))

ExportAnalyticsMetrics exports analytics metrics.

Operation.response is of type ExportAnalyticsMetricsResponse. Operation.metadata is of type ExportMetadata.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewAnalyticsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_AnalyticsClient_NewAnalyticsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ExportAnalyticsMetricsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ExportAnalyticsMetricsRequest.
    	}
    	op, err := c.ExportAnalyticsMetrics(ctx, req)
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
    

### func (*AnalyticsClient) ExportAnalyticsMetricsOperation 
    
    
    func (c *AnalyticsClient) ExportAnalyticsMetricsOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportAnalyticsMetricsOperation

ExportAnalyticsMetricsOperation returns a new ExportAnalyticsMetricsOperation from a given name. The name must be that of a previously created ExportAnalyticsMetricsOperation, possibly from a different process.

### func (*AnalyticsClient) GetOperation 
    
    
    func (c *AnalyticsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewAnalyticsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_AnalyticsClient_NewAnalyticsClient)(ctx)
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
    

### func (*AnalyticsClient) ListOperations 
    
    
    func (c *AnalyticsClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewAnalyticsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_AnalyticsClient_NewAnalyticsClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewAnalyticsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_AnalyticsClient_NewAnalyticsClient)(ctx)
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
    

## CatalogCallOptions
    
    
    type CatalogCallOptions struct {
    	ListCatalogs            []gax.CallOption
    	UpdateCatalog           []gax.CallOption
    	SetDefaultBranch        []gax.CallOption
    	GetDefaultBranch        []gax.CallOption
    	GetCompletionConfig     []gax.CallOption
    	UpdateCompletionConfig  []gax.CallOption
    	GetAttributesConfig     []gax.CallOption
    	UpdateAttributesConfig  []gax.CallOption
    	AddCatalogAttribute     []gax.CallOption
    	RemoveCatalogAttribute  []gax.CallOption
    	ReplaceCatalogAttribute []gax.CallOption
    	GetOperation            []gax.CallOption
    	ListOperations          []gax.CallOption
    }

CatalogCallOptions contains the retry settings for each method of CatalogClient.

## CatalogClient
    
    
    type CatalogClient struct {
    
    	// The call options for this service.
    	CallOptions *CatalogCallOptions
    	// contains filtered or unexported fields
    }

CatalogClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing catalog configuration.

### func NewCatalogClient 
    
    
    func NewCatalogClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CatalogClient, [error](https://pkg.go.dev/builtin#error))

NewCatalogClient creates a new catalog service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing catalog configuration.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCatalogRESTClient 
    
    
    func NewCatalogRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CatalogClient, [error](https://pkg.go.dev/builtin#error))

NewCatalogRESTClient creates a new catalog service rest client.

Service for managing catalog configuration.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CatalogClient) AddCatalogAttribute 
    
    
    func (c *CatalogClient) AddCatalogAttribute(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddCatalogAttributeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddCatalogAttributeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AttributesConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AttributesConfig), [error](https://pkg.go.dev/builtin#error))

AddCatalogAttribute adds the specified CatalogAttribute to the AttributesConfig.

If the CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.AddCatalogAttributeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#AddCatalogAttributeRequest.
    	}
    	resp, err := c.AddCatalogAttribute(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) Close 
    
    
    func (c *CatalogClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CatalogClient) Connection (deprecated)
    
    
    func (c *CatalogClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CatalogClient) GetAttributesConfig 
    
    
    func (c *CatalogClient) GetAttributesConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetAttributesConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetAttributesConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AttributesConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AttributesConfig), [error](https://pkg.go.dev/builtin#error))

GetAttributesConfig gets an AttributesConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetAttributesConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetAttributesConfigRequest.
    	}
    	resp, err := c.GetAttributesConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) GetCompletionConfig 
    
    
    func (c *CatalogClient) GetCompletionConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetCompletionConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetCompletionConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CompletionConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CompletionConfig), [error](https://pkg.go.dev/builtin#error))

GetCompletionConfig gets a CompletionConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetCompletionConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetCompletionConfigRequest.
    	}
    	resp, err := c.GetCompletionConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) GetDefaultBranch 
    
    
    func (c *CatalogClient) GetDefaultBranch(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetDefaultBranchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetDefaultBranchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetDefaultBranchResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetDefaultBranchResponse), [error](https://pkg.go.dev/builtin#error))

GetDefaultBranch get which branch is currently default branch set by CatalogService.SetDefaultBranch method under a specified parent catalog.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetDefaultBranchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetDefaultBranchRequest.
    	}
    	resp, err := c.GetDefaultBranch(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) GetOperation 
    
    
    func (c *CatalogClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
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
    

### func (*CatalogClient) ListCatalogs 
    
    
    func (c *CatalogClient) ListCatalogs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListCatalogsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListCatalogsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CatalogIterator

ListCatalogs lists all the Catalogs associated with the project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListCatalogsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListCatalogsRequest.
    	}
    	it := c.ListCatalogs(ctx, req)
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
    		_ = it.Response.(*retailpb.ListCatalogsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListCatalogsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListCatalogsRequest.
    	}
    	for resp, err := range c.ListCatalogs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CatalogClient) ListOperations 
    
    
    func (c *CatalogClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
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
    

### func (*CatalogClient) RemoveCatalogAttribute 
    
    
    func (c *CatalogClient) RemoveCatalogAttribute(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveCatalogAttributeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveCatalogAttributeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AttributesConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AttributesConfig), [error](https://pkg.go.dev/builtin#error))

RemoveCatalogAttribute removes the specified CatalogAttribute from the AttributesConfig.

If the CatalogAttribute to remove does not exist, a NOT_FOUND error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.RemoveCatalogAttributeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#RemoveCatalogAttributeRequest.
    	}
    	resp, err := c.RemoveCatalogAttribute(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) ReplaceCatalogAttribute 
    
    
    func (c *CatalogClient) ReplaceCatalogAttribute(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ReplaceCatalogAttributeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ReplaceCatalogAttributeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AttributesConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AttributesConfig), [error](https://pkg.go.dev/builtin#error))

ReplaceCatalogAttribute replaces the specified CatalogAttribute in the AttributesConfig by updating the catalog attribute with the same CatalogAttribute.key.

If the CatalogAttribute to replace does not exist, a NOT_FOUND error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ReplaceCatalogAttributeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ReplaceCatalogAttributeRequest.
    	}
    	resp, err := c.ReplaceCatalogAttribute(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) SetDefaultBranch 
    
    
    func (c *CatalogClient) SetDefaultBranch(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SetDefaultBranchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SetDefaultBranchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

SetDefaultBranch set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using “default_branch” to the actual branch id set as default.

For example, if projects/_/locations/_ /catalogs/_/branches/1 is set as default, setting SearchRequest.branch to projects/_ /locations/_/catalogs/_ /branches/default_branch is equivalent to setting SearchRequest.branch to projects/_/locations/_ /catalogs/*/branches/1.

Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using projects/_/locations/_ /catalogs/*/branches/default_branch as SearchRequest.branch to route the traffic to this staging branch.

CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one.

More specifically:
    
    
    PredictionService will only return product IDs from branch {newBranch}.
    
    SearchService will only return product IDs from branch {newBranch}
    (if branch is not explicitly set).
    
    UserEventService will only join events with products from branch
    {newBranch}.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.SetDefaultBranchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#SetDefaultBranchRequest.
    	}
    	err = c.SetDefaultBranch(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CatalogClient) UpdateAttributesConfig 
    
    
    func (c *CatalogClient) UpdateAttributesConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateAttributesConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateAttributesConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AttributesConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AttributesConfig), [error](https://pkg.go.dev/builtin#error))

UpdateAttributesConfig updates the AttributesConfig.

The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateAttributesConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateAttributesConfigRequest.
    	}
    	resp, err := c.UpdateAttributesConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) UpdateCatalog 
    
    
    func (c *CatalogClient) UpdateCatalog(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateCatalogRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateCatalogRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Catalog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Catalog), [error](https://pkg.go.dev/builtin#error))

UpdateCatalog updates the Catalogs.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateCatalogRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateCatalogRequest.
    	}
    	resp, err := c.UpdateCatalog(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CatalogClient) UpdateCompletionConfig 
    
    
    func (c *CatalogClient) UpdateCompletionConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateCompletionConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateCompletionConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CompletionConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CompletionConfig), [error](https://pkg.go.dev/builtin#error))

UpdateCompletionConfig updates the CompletionConfigs.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateCompletionConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateCompletionConfigRequest.
    	}
    	resp, err := c.UpdateCompletionConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CatalogIterator
    
    
    type CatalogIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*retailpb.Catalog, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CatalogIterator manages a stream of *retailpb.Catalog.

### func (*CatalogIterator) All 
    
    
    func (it *CatalogIterator) All() iter.Seq2[*retailpb.Catalog, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CatalogIterator) Next 
    
    
    func (it *CatalogIterator) Next() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Catalog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Catalog), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CatalogIterator) PageInfo 
    
    
    func (it *CatalogIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CompletionCallOptions
    
    
    type CompletionCallOptions struct {
    	CompleteQuery        []gax.CallOption
    	ImportCompletionData []gax.CallOption
    	GetOperation         []gax.CallOption
    	ListOperations       []gax.CallOption
    }

CompletionCallOptions contains the retry settings for each method of CompletionClient.

## CompletionClient
    
    
    type CompletionClient struct {
    
    	// The call options for this service.
    	CallOptions *CompletionCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

CompletionClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Autocomplete service for retail.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

### func NewCompletionClient 
    
    
    func NewCompletionClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CompletionClient, [error](https://pkg.go.dev/builtin#error))

NewCompletionClient creates a new completion service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Autocomplete service for retail.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCompletionRESTClient 
    
    
    func NewCompletionRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CompletionClient, [error](https://pkg.go.dev/builtin#error))

NewCompletionRESTClient creates a new completion service rest client.

Autocomplete service for retail.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CompletionClient) Close 
    
    
    func (c *CompletionClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CompletionClient) CompleteQuery 
    
    
    func (c *CompletionClient) CompleteQuery(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CompleteQueryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CompleteQueryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CompleteQueryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CompleteQueryResponse), [error](https://pkg.go.dev/builtin#error))

CompleteQuery completes the specified prefix with keyword suggestions.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.CompleteQueryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#CompleteQueryRequest.
    	}
    	resp, err := c.CompleteQuery(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CompletionClient) Connection (deprecated)
    
    
    func (c *CompletionClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CompletionClient) GetOperation 
    
    
    func (c *CompletionClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionClient)(ctx)
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
    

### func (*CompletionClient) ImportCompletionData 
    
    
    func (c *CompletionClient) ImportCompletionData(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportCompletionDataRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportCompletionDataRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportCompletionDataOperation, [error](https://pkg.go.dev/builtin#error))

ImportCompletionData bulk import of processed completion dataset.

Request processing is asynchronous. Partial updating is not supported.

The operation is successfully finished only after the imported suggestions are indexed successfully and ready for serving. The process takes hours.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ImportCompletionDataRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ImportCompletionDataRequest.
    	}
    	op, err := c.ImportCompletionData(ctx, req)
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
    

### func (*CompletionClient) ImportCompletionDataOperation 
    
    
    func (c *CompletionClient) ImportCompletionDataOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportCompletionDataOperation

ImportCompletionDataOperation returns a new ImportCompletionDataOperation from a given name. The name must be that of a previously created ImportCompletionDataOperation, possibly from a different process.

### func (*CompletionClient) ListOperations 
    
    
    func (c *CompletionClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewCompletionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_CompletionClient_NewCompletionClient)(ctx)
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
    

## ControlCallOptions
    
    
    type ControlCallOptions struct {
    	CreateControl  []gax.CallOption
    	DeleteControl  []gax.CallOption
    	UpdateControl  []gax.CallOption
    	GetControl     []gax.CallOption
    	ListControls   []gax.CallOption
    	GetOperation   []gax.CallOption
    	ListOperations []gax.CallOption
    }

ControlCallOptions contains the retry settings for each method of ControlClient.

## ControlClient
    
    
    type ControlClient struct {
    
    	// The call options for this service.
    	CallOptions *ControlCallOptions
    	// contains filtered or unexported fields
    }

ControlClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for modifying Control.

### func NewControlClient 
    
    
    func NewControlClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ControlClient, [error](https://pkg.go.dev/builtin#error))

NewControlClient creates a new control service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for modifying Control.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewControlRESTClient 
    
    
    func NewControlRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ControlClient, [error](https://pkg.go.dev/builtin#error))

NewControlRESTClient creates a new control service rest client.

Service for modifying Control.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ControlClient) Close 
    
    
    func (c *ControlClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ControlClient) Connection (deprecated)
    
    
    func (c *ControlClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ControlClient) CreateControl 
    
    
    func (c *ControlClient) CreateControl(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CreateControlRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CreateControlRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Control](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Control), [error](https://pkg.go.dev/builtin#error))

CreateControl creates a Control.

If the Control to create already exists, an ALREADY_EXISTS error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.CreateControlRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#CreateControlRequest.
    	}
    	resp, err := c.CreateControl(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ControlClient) DeleteControl 
    
    
    func (c *ControlClient) DeleteControl(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[DeleteControlRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_DeleteControlRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteControl deletes a Control.

If the Control to delete does not exist, a NOT_FOUND error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.DeleteControlRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#DeleteControlRequest.
    	}
    	err = c.DeleteControl(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ControlClient) GetControl 
    
    
    func (c *ControlClient) GetControl(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetControlRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetControlRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Control](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Control), [error](https://pkg.go.dev/builtin#error))

GetControl gets a Control.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetControlRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetControlRequest.
    	}
    	resp, err := c.GetControl(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ControlClient) GetOperation 
    
    
    func (c *ControlClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
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
    

### func (*ControlClient) ListControls 
    
    
    func (c *ControlClient) ListControls(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListControlsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListControlsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ControlIterator

ListControls lists all Controls by their parent Catalog.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListControlsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListControlsRequest.
    	}
    	it := c.ListControls(ctx, req)
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
    		_ = it.Response.(*retailpb.ListControlsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListControlsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListControlsRequest.
    	}
    	for resp, err := range c.ListControls(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ControlClient) ListOperations 
    
    
    func (c *ControlClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
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
    

### func (*ControlClient) UpdateControl 
    
    
    func (c *ControlClient) UpdateControl(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateControlRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateControlRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Control](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Control), [error](https://pkg.go.dev/builtin#error))

UpdateControl updates a Control.

Control cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the Control to update does not exist, a NOT_FOUND error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewControlClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ControlClient_NewControlClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateControlRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateControlRequest.
    	}
    	resp, err := c.UpdateControl(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ControlIterator
    
    
    type ControlIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*retailpb.Control, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ControlIterator manages a stream of *retailpb.Control.

### func (*ControlIterator) All 
    
    
    func (it *ControlIterator) All() iter.Seq2[*retailpb.Control, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ControlIterator) Next 
    
    
    func (it *ControlIterator) Next() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Control](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Control), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ControlIterator) PageInfo 
    
    
    func (it *ControlIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ConversationalSearchCallOptions
    
    
    type ConversationalSearchCallOptions struct {
    	ConversationalSearch []gax.CallOption
    	GetOperation         []gax.CallOption
    	ListOperations       []gax.CallOption
    }

ConversationalSearchCallOptions contains the retry settings for each method of ConversationalSearchClient.

## ConversationalSearchClient
    
    
    type ConversationalSearchClient struct {
    
    	// The call options for this service.
    	CallOptions *ConversationalSearchCallOptions
    	// contains filtered or unexported fields
    }

ConversationalSearchClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for retail conversational search.

This feature is only available for users who have Retail Conversational Search enabled. Enable Retail Conversational Search on Cloud Console before using this feature.

### func NewConversationalSearchClient 
    
    
    func NewConversationalSearchClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ConversationalSearchClient, [error](https://pkg.go.dev/builtin#error))

NewConversationalSearchClient creates a new conversational search service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for retail conversational search.

This feature is only available for users who have Retail Conversational Search enabled. Enable Retail Conversational Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewConversationalSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ConversationalSearchClient_NewConversationalSearchClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewConversationalSearchRESTClient 
    
    
    func NewConversationalSearchRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ConversationalSearchClient, [error](https://pkg.go.dev/builtin#error))

NewConversationalSearchRESTClient creates a new conversational search service rest client.

Service for retail conversational search.

This feature is only available for users who have Retail Conversational Search enabled. Enable Retail Conversational Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewConversationalSearchRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ConversationalSearchClient_NewConversationalSearchRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ConversationalSearchClient) Close 
    
    
    func (c *ConversationalSearchClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ConversationalSearchClient) Connection (deprecated)
    
    
    func (c *ConversationalSearchClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ConversationalSearchClient) ConversationalSearch 
    
    
    func (c *ConversationalSearchClient) ConversationalSearch(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ConversationalSearchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ConversationalSearchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ConversationalSearchService_ConversationalSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ConversationalSearchService_ConversationalSearchClient), [error](https://pkg.go.dev/builtin#error))

ConversationalSearch performs a conversational search.

This feature is only available for users who have Conversational Search enabled.

### func (*ConversationalSearchClient) GetOperation 
    
    
    func (c *ConversationalSearchClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewConversationalSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ConversationalSearchClient_NewConversationalSearchClient)(ctx)
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
    

### func (*ConversationalSearchClient) ListOperations 
    
    
    func (c *ConversationalSearchClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewConversationalSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ConversationalSearchClient_NewConversationalSearchClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewConversationalSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ConversationalSearchClient_NewConversationalSearchClient)(ctx)
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
    

## CreateModelOperation
    
    
    type CreateModelOperation struct {
    	// contains filtered or unexported fields
    }

CreateModelOperation manages a long-running operation from CreateModel.

### func (*CreateModelOperation) Done 
    
    
    func (op *CreateModelOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateModelOperation) Metadata 
    
    
    func (op *CreateModelOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CreateModelMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CreateModelMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateModelOperation) Name 
    
    
    func (op *CreateModelOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateModelOperation) Poll 
    
    
    func (op *CreateModelOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateModelOperation) Wait 
    
    
    func (op *CreateModelOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportAnalyticsMetricsOperation
    
    
    type ExportAnalyticsMetricsOperation struct {
    	// contains filtered or unexported fields
    }

ExportAnalyticsMetricsOperation manages a long-running operation from ExportAnalyticsMetrics.

### func (*ExportAnalyticsMetricsOperation) Done 
    
    
    func (op *ExportAnalyticsMetricsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportAnalyticsMetricsOperation) Metadata 
    
    
    func (op *ExportAnalyticsMetricsOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ExportMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ExportMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportAnalyticsMetricsOperation) Name 
    
    
    func (op *ExportAnalyticsMetricsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportAnalyticsMetricsOperation) Poll 
    
    
    func (op *ExportAnalyticsMetricsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ExportAnalyticsMetricsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ExportAnalyticsMetricsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportAnalyticsMetricsOperation) Wait 
    
    
    func (op *ExportAnalyticsMetricsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ExportAnalyticsMetricsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ExportAnalyticsMetricsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## GenerativeQuestionCallOptions
    
    
    type GenerativeQuestionCallOptions struct {
    	UpdateGenerativeQuestionsFeatureConfig []gax.CallOption
    	GetGenerativeQuestionsFeatureConfig    []gax.CallOption
    	ListGenerativeQuestionConfigs          []gax.CallOption
    	UpdateGenerativeQuestionConfig         []gax.CallOption
    	BatchUpdateGenerativeQuestionConfigs   []gax.CallOption
    	GetOperation                           []gax.CallOption
    	ListOperations                         []gax.CallOption
    }

GenerativeQuestionCallOptions contains the retry settings for each method of GenerativeQuestionClient.

## GenerativeQuestionClient
    
    
    type GenerativeQuestionClient struct {
    
    	// The call options for this service.
    	CallOptions *GenerativeQuestionCallOptions
    	// contains filtered or unexported fields
    }

GenerativeQuestionClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing LLM generated questions in search serving.

### func NewGenerativeQuestionClient 
    
    
    func NewGenerativeQuestionClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GenerativeQuestionClient, [error](https://pkg.go.dev/builtin#error))

NewGenerativeQuestionClient creates a new generative question service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing LLM generated questions in search serving.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewGenerativeQuestionRESTClient 
    
    
    func NewGenerativeQuestionRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GenerativeQuestionClient, [error](https://pkg.go.dev/builtin#error))

NewGenerativeQuestionRESTClient creates a new generative question service rest client.

Service for managing LLM generated questions in search serving.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*GenerativeQuestionClient) BatchUpdateGenerativeQuestionConfigs 
    
    
    func (c *GenerativeQuestionClient) BatchUpdateGenerativeQuestionConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_BatchUpdateGenerativeQuestionConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_BatchUpdateGenerativeQuestionConfigsResponse), [error](https://pkg.go.dev/builtin#error))

BatchUpdateGenerativeQuestionConfigs allows management of multiple questions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.BatchUpdateGenerativeQuestionConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#BatchUpdateGenerativeQuestionConfigsRequest.
    	}
    	resp, err := c.BatchUpdateGenerativeQuestionConfigs(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeQuestionClient) Close 
    
    
    func (c *GenerativeQuestionClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*GenerativeQuestionClient) Connection (deprecated)
    
    
    func (c *GenerativeQuestionClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*GenerativeQuestionClient) GetGenerativeQuestionsFeatureConfig 
    
    
    func (c *GenerativeQuestionClient) GetGenerativeQuestionsFeatureConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetGenerativeQuestionsFeatureConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GenerativeQuestionsFeatureConfig), [error](https://pkg.go.dev/builtin#error))

GetGenerativeQuestionsFeatureConfig manages overal generative question feature state – enables toggling feature on and off.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetGenerativeQuestionsFeatureConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetGenerativeQuestionsFeatureConfigRequest.
    	}
    	resp, err := c.GetGenerativeQuestionsFeatureConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeQuestionClient) GetOperation 
    
    
    func (c *GenerativeQuestionClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
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
    

### func (*GenerativeQuestionClient) ListGenerativeQuestionConfigs 
    
    
    func (c *GenerativeQuestionClient) ListGenerativeQuestionConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListGenerativeQuestionConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListGenerativeQuestionConfigsResponse), [error](https://pkg.go.dev/builtin#error))

ListGenerativeQuestionConfigs returns all questions for a given catalog.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListGenerativeQuestionConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListGenerativeQuestionConfigsRequest.
    	}
    	resp, err := c.ListGenerativeQuestionConfigs(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeQuestionClient) ListOperations 
    
    
    func (c *GenerativeQuestionClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
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
    

### func (*GenerativeQuestionClient) UpdateGenerativeQuestionConfig 
    
    
    func (c *GenerativeQuestionClient) UpdateGenerativeQuestionConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateGenerativeQuestionConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GenerativeQuestionConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GenerativeQuestionConfig), [error](https://pkg.go.dev/builtin#error))

UpdateGenerativeQuestionConfig allows management of individual questions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateGenerativeQuestionConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateGenerativeQuestionConfigRequest.
    	}
    	resp, err := c.UpdateGenerativeQuestionConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeQuestionClient) UpdateGenerativeQuestionsFeatureConfig 
    
    
    func (c *GenerativeQuestionClient) UpdateGenerativeQuestionsFeatureConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateGenerativeQuestionsFeatureConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GenerativeQuestionsFeatureConfig), [error](https://pkg.go.dev/builtin#error))

UpdateGenerativeQuestionsFeatureConfig manages overal generative question feature state – enables toggling feature on and off.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewGenerativeQuestionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_GenerativeQuestionClient_NewGenerativeQuestionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateGenerativeQuestionsFeatureConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateGenerativeQuestionsFeatureConfigRequest.
    	}
    	resp, err := c.UpdateGenerativeQuestionsFeatureConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ImportCompletionDataOperation
    
    
    type ImportCompletionDataOperation struct {
    	// contains filtered or unexported fields
    }

ImportCompletionDataOperation manages a long-running operation from ImportCompletionData.

### func (*ImportCompletionDataOperation) Done 
    
    
    func (op *ImportCompletionDataOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportCompletionDataOperation) Metadata 
    
    
    func (op *ImportCompletionDataOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportCompletionDataOperation) Name 
    
    
    func (op *ImportCompletionDataOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportCompletionDataOperation) Poll 
    
    
    func (op *ImportCompletionDataOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportCompletionDataResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportCompletionDataResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportCompletionDataOperation) Wait 
    
    
    func (op *ImportCompletionDataOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportCompletionDataResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportCompletionDataResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportProductsOperation
    
    
    type ImportProductsOperation struct {
    	// contains filtered or unexported fields
    }

ImportProductsOperation manages a long-running operation from ImportProducts.

### func (*ImportProductsOperation) Done 
    
    
    func (op *ImportProductsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportProductsOperation) Metadata 
    
    
    func (op *ImportProductsOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportProductsOperation) Name 
    
    
    func (op *ImportProductsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportProductsOperation) Poll 
    
    
    func (op *ImportProductsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportProductsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportProductsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportProductsOperation) Wait 
    
    
    func (op *ImportProductsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportProductsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportProductsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ImportUserEventsOperation
    
    
    type ImportUserEventsOperation struct {
    	// contains filtered or unexported fields
    }

ImportUserEventsOperation manages a long-running operation from ImportUserEvents.

### func (*ImportUserEventsOperation) Done 
    
    
    func (op *ImportUserEventsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ImportUserEventsOperation) Metadata 
    
    
    func (op *ImportUserEventsOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ImportUserEventsOperation) Name 
    
    
    func (op *ImportUserEventsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ImportUserEventsOperation) Poll 
    
    
    func (op *ImportUserEventsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportUserEventsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportUserEventsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ImportUserEventsOperation) Wait 
    
    
    func (op *ImportUserEventsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportUserEventsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportUserEventsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ModelCallOptions
    
    
    type ModelCallOptions struct {
    	CreateModel    []gax.CallOption
    	GetModel       []gax.CallOption
    	PauseModel     []gax.CallOption
    	ResumeModel    []gax.CallOption
    	DeleteModel    []gax.CallOption
    	ListModels     []gax.CallOption
    	UpdateModel    []gax.CallOption
    	TuneModel      []gax.CallOption
    	GetOperation   []gax.CallOption
    	ListOperations []gax.CallOption
    }

ModelCallOptions contains the retry settings for each method of ModelClient.

## ModelClient
    
    
    type ModelClient struct {
    
    	// The call options for this service.
    	CallOptions *ModelCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

ModelClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for performing CRUD operations on models. Recommendation models contain all the metadata necessary to generate a set of models for the Predict() API. A model is queried indirectly via a ServingConfig, which associates a model with a given Placement (e.g. Frequently Bought Together on Home Page).

This service allows you to do the following:
    
    
    Initiate training of a model.
    
    Pause training of an existing model.
    
    List all the available models along with their metadata.
    
    Control their tuning schedule.
    

### func NewModelClient 
    
    
    func NewModelClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ModelClient, [error](https://pkg.go.dev/builtin#error))

NewModelClient creates a new model service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for performing CRUD operations on models. Recommendation models contain all the metadata necessary to generate a set of models for the Predict() API. A model is queried indirectly via a ServingConfig, which associates a model with a given Placement (e.g. Frequently Bought Together on Home Page).

This service allows you to do the following:
    
    
    Initiate training of a model.
    
    Pause training of an existing model.
    
    List all the available models along with their metadata.
    
    Control their tuning schedule.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewModelRESTClient 
    
    
    func NewModelRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ModelClient, [error](https://pkg.go.dev/builtin#error))

NewModelRESTClient creates a new model service rest client.

Service for performing CRUD operations on models. Recommendation models contain all the metadata necessary to generate a set of models for the Predict() API. A model is queried indirectly via a ServingConfig, which associates a model with a given Placement (e.g. Frequently Bought Together on Home Page).

This service allows you to do the following:
    
    
    Initiate training of a model.
    
    Pause training of an existing model.
    
    List all the available models along with their metadata.
    
    Control their tuning schedule.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ModelClient) Close 
    
    
    func (c *ModelClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ModelClient) Connection (deprecated)
    
    
    func (c *ModelClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ModelClient) CreateModel 
    
    
    func (c *ModelClient) CreateModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CreateModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CreateModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateModelOperation, [error](https://pkg.go.dev/builtin#error))

CreateModel creates a new model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.CreateModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#CreateModelRequest.
    	}
    	op, err := c.CreateModel(ctx, req)
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
    

### func (*ModelClient) CreateModelOperation 
    
    
    func (c *ModelClient) CreateModelOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateModelOperation

CreateModelOperation returns a new CreateModelOperation from a given name. The name must be that of a previously created CreateModelOperation, possibly from a different process.

### func (*ModelClient) DeleteModel 
    
    
    func (c *ModelClient) DeleteModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[DeleteModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_DeleteModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteModel deletes an existing model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.DeleteModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#DeleteModelRequest.
    	}
    	err = c.DeleteModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ModelClient) GetModel 
    
    
    func (c *ModelClient) GetModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

GetModel gets a model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetModelRequest.
    	}
    	resp, err := c.GetModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ModelClient) GetOperation 
    
    
    func (c *ModelClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
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
    

### func (*ModelClient) ListModels 
    
    
    func (c *ModelClient) ListModels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListModelsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListModelsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ModelIterator

ListModels lists all the models linked to this event store.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListModelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListModelsRequest.
    	}
    	it := c.ListModels(ctx, req)
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
    		_ = it.Response.(*retailpb.ListModelsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListModelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListModelsRequest.
    	}
    	for resp, err := range c.ListModels(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ModelClient) ListOperations 
    
    
    func (c *ModelClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
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
    

### func (*ModelClient) PauseModel 
    
    
    func (c *ModelClient) PauseModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PauseModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PauseModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

PauseModel pauses the training of an existing model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.PauseModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#PauseModelRequest.
    	}
    	resp, err := c.PauseModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ModelClient) ResumeModel 
    
    
    func (c *ModelClient) ResumeModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ResumeModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ResumeModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

ResumeModel resumes the training of an existing model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ResumeModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ResumeModelRequest.
    	}
    	resp, err := c.ResumeModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ModelClient) TuneModel 
    
    
    func (c *ModelClient) TuneModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[TuneModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_TuneModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*TuneModelOperation, [error](https://pkg.go.dev/builtin#error))

TuneModel tunes an existing model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.TuneModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#TuneModelRequest.
    	}
    	op, err := c.TuneModel(ctx, req)
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
    

### func (*ModelClient) TuneModelOperation 
    
    
    func (c *ModelClient) TuneModelOperation(name [string](https://pkg.go.dev/builtin#string)) *TuneModelOperation

TuneModelOperation returns a new TuneModelOperation from a given name. The name must be that of a previously created TuneModelOperation, possibly from a different process.

### func (*ModelClient) UpdateModel 
    
    
    func (c *ModelClient) UpdateModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

UpdateModel update of model metadata. Only fields that currently can be updated are: filtering_option and periodic_tuning_state. If other values are provided, this API method ignores them.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewModelClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ModelClient_NewModelClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateModelRequest.
    	}
    	resp, err := c.UpdateModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ModelIterator
    
    
    type ModelIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*retailpb.Model, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ModelIterator manages a stream of *retailpb.Model.

### func (*ModelIterator) All 
    
    
    func (it *ModelIterator) All() iter.Seq2[*retailpb.Model, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ModelIterator) Next 
    
    
    func (it *ModelIterator) Next() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Model), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ModelIterator) PageInfo 
    
    
    func (it *ModelIterator) PageInfo() *iterator.PageInfo

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

## PredictionCallOptions
    
    
    type PredictionCallOptions struct {
    	Predict        []gax.CallOption
    	GetOperation   []gax.CallOption
    	ListOperations []gax.CallOption
    }

PredictionCallOptions contains the retry settings for each method of PredictionClient.

## PredictionClient
    
    
    type PredictionClient struct {
    
    	// The call options for this service.
    	CallOptions *PredictionCallOptions
    	// contains filtered or unexported fields
    }

PredictionClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for making recommendation prediction.

### func NewPredictionClient 
    
    
    func NewPredictionClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PredictionClient, [error](https://pkg.go.dev/builtin#error))

NewPredictionClient creates a new prediction service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for making recommendation prediction.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewPredictionRESTClient 
    
    
    func NewPredictionRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PredictionClient, [error](https://pkg.go.dev/builtin#error))

NewPredictionRESTClient creates a new prediction service rest client.

Service for making recommendation prediction.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewPredictionRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_PredictionClient_NewPredictionRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*PredictionClient) Close 
    
    
    func (c *PredictionClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*PredictionClient) Connection (deprecated)
    
    
    func (c *PredictionClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*PredictionClient) GetOperation 
    
    
    func (c *PredictionClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_PredictionClient_NewPredictionClient)(ctx)
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
    

### func (*PredictionClient) ListOperations 
    
    
    func (c *PredictionClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_PredictionClient_NewPredictionClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_PredictionClient_NewPredictionClient)(ctx)
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
    

### func (*PredictionClient) Predict 
    
    
    func (c *PredictionClient) Predict(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PredictRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PredictRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PredictResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PredictResponse), [error](https://pkg.go.dev/builtin#error))

Predict makes a recommendation prediction.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.PredictRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#PredictRequest.
    	}
    	resp, err := c.Predict(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ProductCallOptions
    
    
    type ProductCallOptions struct {
    	CreateProduct           []gax.CallOption
    	GetProduct              []gax.CallOption
    	ListProducts            []gax.CallOption
    	UpdateProduct           []gax.CallOption
    	DeleteProduct           []gax.CallOption
    	PurgeProducts           []gax.CallOption
    	ImportProducts          []gax.CallOption
    	SetInventory            []gax.CallOption
    	AddFulfillmentPlaces    []gax.CallOption
    	RemoveFulfillmentPlaces []gax.CallOption
    	AddLocalInventories     []gax.CallOption
    	RemoveLocalInventories  []gax.CallOption
    	GetOperation            []gax.CallOption
    	ListOperations          []gax.CallOption
    }

ProductCallOptions contains the retry settings for each method of ProductClient.

## ProductClient
    
    
    type ProductClient struct {
    
    	// The call options for this service.
    	CallOptions *ProductCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

ProductClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for ingesting Product information of the customer’s website.

### func NewProductClient 
    
    
    func NewProductClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ProductClient, [error](https://pkg.go.dev/builtin#error))

NewProductClient creates a new product service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for ingesting Product information of the customer’s website.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewProductRESTClient 
    
    
    func NewProductRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ProductClient, [error](https://pkg.go.dev/builtin#error))

NewProductRESTClient creates a new product service rest client.

Service for ingesting Product information of the customer’s website.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ProductClient) AddFulfillmentPlaces 
    
    
    func (c *ProductClient) AddFulfillmentPlaces(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddFulfillmentPlacesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddFulfillmentPlacesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*AddFulfillmentPlacesOperation, [error](https://pkg.go.dev/builtin#error))

AddFulfillmentPlaces we recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally adds place IDs to Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.AddFulfillmentPlacesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#AddFulfillmentPlacesRequest.
    	}
    	op, err := c.AddFulfillmentPlaces(ctx, req)
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
    

### func (*ProductClient) AddFulfillmentPlacesOperation 
    
    
    func (c *ProductClient) AddFulfillmentPlacesOperation(name [string](https://pkg.go.dev/builtin#string)) *AddFulfillmentPlacesOperation

AddFulfillmentPlacesOperation returns a new AddFulfillmentPlacesOperation from a given name. The name must be that of a previously created AddFulfillmentPlacesOperation, possibly from a different process.

### func (*ProductClient) AddLocalInventories 
    
    
    func (c *ProductClient) AddLocalInventories(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddLocalInventoriesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddLocalInventoriesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*AddLocalInventoriesOperation, [error](https://pkg.go.dev/builtin#error))

AddLocalInventories updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.AddLocalInventoriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#AddLocalInventoriesRequest.
    	}
    	op, err := c.AddLocalInventories(ctx, req)
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
    

### func (*ProductClient) AddLocalInventoriesOperation 
    
    
    func (c *ProductClient) AddLocalInventoriesOperation(name [string](https://pkg.go.dev/builtin#string)) *AddLocalInventoriesOperation

AddLocalInventoriesOperation returns a new AddLocalInventoriesOperation from a given name. The name must be that of a previously created AddLocalInventoriesOperation, possibly from a different process.

### func (*ProductClient) Close 
    
    
    func (c *ProductClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ProductClient) Connection (deprecated)
    
    
    func (c *ProductClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ProductClient) CreateProduct 
    
    
    func (c *ProductClient) CreateProduct(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CreateProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CreateProductRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Product), [error](https://pkg.go.dev/builtin#error))

CreateProduct creates a Product.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.CreateProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#CreateProductRequest.
    	}
    	resp, err := c.CreateProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ProductClient) DeleteProduct 
    
    
    func (c *ProductClient) DeleteProduct(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[DeleteProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_DeleteProductRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteProduct deletes a Product.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.DeleteProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#DeleteProductRequest.
    	}
    	err = c.DeleteProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ProductClient) GetOperation 
    
    
    func (c *ProductClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
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
    

### func (*ProductClient) GetProduct 
    
    
    func (c *ProductClient) GetProduct(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetProductRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Product), [error](https://pkg.go.dev/builtin#error))

GetProduct gets a Product.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetProductRequest.
    	}
    	resp, err := c.GetProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ProductClient) ImportProducts 
    
    
    func (c *ProductClient) ImportProducts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportProductsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportProductsOperation, [error](https://pkg.go.dev/builtin#error))

ImportProducts bulk import of multiple Products.

Request processing may be synchronous. Non-existing items are created.

Note that it is possible for a subset of the Products to be successfully updated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ImportProductsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ImportProductsRequest.
    	}
    	op, err := c.ImportProducts(ctx, req)
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
    

### func (*ProductClient) ImportProductsOperation 
    
    
    func (c *ProductClient) ImportProductsOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportProductsOperation

ImportProductsOperation returns a new ImportProductsOperation from a given name. The name must be that of a previously created ImportProductsOperation, possibly from a different process.

### func (*ProductClient) ListOperations 
    
    
    func (c *ProductClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
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
    

### func (*ProductClient) ListProducts 
    
    
    func (c *ProductClient) ListProducts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListProductsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProductIterator

ListProducts gets a list of Products.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListProductsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListProductsRequest.
    	}
    	it := c.ListProducts(ctx, req)
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
    		_ = it.Response.(*retailpb.ListProductsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListProductsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListProductsRequest.
    	}
    	for resp, err := range c.ListProducts(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ProductClient) PurgeProducts 
    
    
    func (c *ProductClient) PurgeProducts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeProductsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*PurgeProductsOperation, [error](https://pkg.go.dev/builtin#error))

PurgeProducts permanently deletes all selected Products under a branch.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts.

Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.PurgeProductsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#PurgeProductsRequest.
    	}
    	op, err := c.PurgeProducts(ctx, req)
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
    

### func (*ProductClient) PurgeProductsOperation 
    
    
    func (c *ProductClient) PurgeProductsOperation(name [string](https://pkg.go.dev/builtin#string)) *PurgeProductsOperation

PurgeProductsOperation returns a new PurgeProductsOperation from a given name. The name must be that of a previously created PurgeProductsOperation, possibly from a different process.

### func (*ProductClient) RemoveFulfillmentPlaces 
    
    
    func (c *ProductClient) RemoveFulfillmentPlaces(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveFulfillmentPlacesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveFulfillmentPlacesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RemoveFulfillmentPlacesOperation, [error](https://pkg.go.dev/builtin#error))

RemoveFulfillmentPlaces we recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data.

Incrementally removes place IDs from a Product.fulfillment_info.place_ids.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.RemoveFulfillmentPlacesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#RemoveFulfillmentPlacesRequest.
    	}
    	op, err := c.RemoveFulfillmentPlaces(ctx, req)
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
    

### func (*ProductClient) RemoveFulfillmentPlacesOperation 
    
    
    func (c *ProductClient) RemoveFulfillmentPlacesOperation(name [string](https://pkg.go.dev/builtin#string)) *RemoveFulfillmentPlacesOperation

RemoveFulfillmentPlacesOperation returns a new RemoveFulfillmentPlacesOperation from a given name. The name must be that of a previously created RemoveFulfillmentPlacesOperation, possibly from a different process.

### func (*ProductClient) RemoveLocalInventories 
    
    
    func (c *ProductClient) RemoveLocalInventories(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveLocalInventoriesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveLocalInventoriesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RemoveLocalInventoriesOperation, [error](https://pkg.go.dev/builtin#error))

RemoveLocalInventories remove local inventory information for a Product at a list of places at a removal timestamp.

This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories.

The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.RemoveLocalInventoriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#RemoveLocalInventoriesRequest.
    	}
    	op, err := c.RemoveLocalInventories(ctx, req)
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
    

### func (*ProductClient) RemoveLocalInventoriesOperation 
    
    
    func (c *ProductClient) RemoveLocalInventoriesOperation(name [string](https://pkg.go.dev/builtin#string)) *RemoveLocalInventoriesOperation

RemoveLocalInventoriesOperation returns a new RemoveLocalInventoriesOperation from a given name. The name must be that of a previously created RemoveLocalInventoriesOperation, possibly from a different process.

### func (*ProductClient) SetInventory 
    
    
    func (c *ProductClient) SetInventory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SetInventoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SetInventoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*SetInventoryOperation, [error](https://pkg.go.dev/builtin#error))

SetInventory updates inventory information for a Product while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts.

When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request.

If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used.

If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces.

The returned Operations is obsolete after one day, and the GetOperation API returns NOT_FOUND afterwards.

If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.SetInventoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#SetInventoryRequest.
    	}
    	op, err := c.SetInventory(ctx, req)
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
    

### func (*ProductClient) SetInventoryOperation 
    
    
    func (c *ProductClient) SetInventoryOperation(name [string](https://pkg.go.dev/builtin#string)) *SetInventoryOperation

SetInventoryOperation returns a new SetInventoryOperation from a given name. The name must be that of a previously created SetInventoryOperation, possibly from a different process.

### func (*ProductClient) UpdateProduct 
    
    
    func (c *ProductClient) UpdateProduct(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateProductRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Product), [error](https://pkg.go.dev/builtin#error))

UpdateProduct updates a Product.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ProductClient_NewProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateProductRequest.
    	}
    	resp, err := c.UpdateProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ProductIterator
    
    
    type ProductIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*retailpb.Product, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ProductIterator manages a stream of *retailpb.Product.

### func (*ProductIterator) All 
    
    
    func (it *ProductIterator) All() iter.Seq2[*retailpb.Product, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ProductIterator) Next 
    
    
    func (it *ProductIterator) Next() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_Product), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ProductIterator) PageInfo 
    
    
    func (it *ProductIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PurgeProductsOperation
    
    
    type PurgeProductsOperation struct {
    	// contains filtered or unexported fields
    }

PurgeProductsOperation manages a long-running operation from PurgeProducts.

### func (*PurgeProductsOperation) Done 
    
    
    func (op *PurgeProductsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*PurgeProductsOperation) Metadata 
    
    
    func (op *PurgeProductsOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeProductsMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeProductsMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*PurgeProductsOperation) Name 
    
    
    func (op *PurgeProductsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*PurgeProductsOperation) Poll 
    
    
    func (op *PurgeProductsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeProductsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeProductsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*PurgeProductsOperation) Wait 
    
    
    func (op *PurgeProductsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeProductsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeProductsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## PurgeUserEventsOperation
    
    
    type PurgeUserEventsOperation struct {
    	// contains filtered or unexported fields
    }

PurgeUserEventsOperation manages a long-running operation from PurgeUserEvents.

### func (*PurgeUserEventsOperation) Done 
    
    
    func (op *PurgeUserEventsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*PurgeUserEventsOperation) Metadata 
    
    
    func (op *PurgeUserEventsOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*PurgeUserEventsOperation) Name 
    
    
    func (op *PurgeUserEventsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*PurgeUserEventsOperation) Poll 
    
    
    func (op *PurgeUserEventsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeUserEventsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeUserEventsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*PurgeUserEventsOperation) Wait 
    
    
    func (op *PurgeUserEventsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeUserEventsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeUserEventsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RejoinUserEventsOperation
    
    
    type RejoinUserEventsOperation struct {
    	// contains filtered or unexported fields
    }

RejoinUserEventsOperation manages a long-running operation from RejoinUserEvents.

### func (*RejoinUserEventsOperation) Done 
    
    
    func (op *RejoinUserEventsOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RejoinUserEventsOperation) Metadata 
    
    
    func (op *RejoinUserEventsOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RejoinUserEventsMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RejoinUserEventsMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RejoinUserEventsOperation) Name 
    
    
    func (op *RejoinUserEventsOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RejoinUserEventsOperation) Poll 
    
    
    func (op *RejoinUserEventsOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RejoinUserEventsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RejoinUserEventsResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RejoinUserEventsOperation) Wait 
    
    
    func (op *RejoinUserEventsOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RejoinUserEventsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RejoinUserEventsResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RemoveFulfillmentPlacesOperation
    
    
    type RemoveFulfillmentPlacesOperation struct {
    	// contains filtered or unexported fields
    }

RemoveFulfillmentPlacesOperation manages a long-running operation from RemoveFulfillmentPlaces.

### func (*RemoveFulfillmentPlacesOperation) Done 
    
    
    func (op *RemoveFulfillmentPlacesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RemoveFulfillmentPlacesOperation) Metadata 
    
    
    func (op *RemoveFulfillmentPlacesOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveFulfillmentPlacesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveFulfillmentPlacesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RemoveFulfillmentPlacesOperation) Name 
    
    
    func (op *RemoveFulfillmentPlacesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RemoveFulfillmentPlacesOperation) Poll 
    
    
    func (op *RemoveFulfillmentPlacesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveFulfillmentPlacesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RemoveFulfillmentPlacesOperation) Wait 
    
    
    func (op *RemoveFulfillmentPlacesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveFulfillmentPlacesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveFulfillmentPlacesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RemoveLocalInventoriesOperation
    
    
    type RemoveLocalInventoriesOperation struct {
    	// contains filtered or unexported fields
    }

RemoveLocalInventoriesOperation manages a long-running operation from RemoveLocalInventories.

### func (*RemoveLocalInventoriesOperation) Done 
    
    
    func (op *RemoveLocalInventoriesOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RemoveLocalInventoriesOperation) Metadata 
    
    
    func (op *RemoveLocalInventoriesOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveLocalInventoriesMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveLocalInventoriesMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RemoveLocalInventoriesOperation) Name 
    
    
    func (op *RemoveLocalInventoriesOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RemoveLocalInventoriesOperation) Poll 
    
    
    func (op *RemoveLocalInventoriesOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveLocalInventoriesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveLocalInventoriesResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RemoveLocalInventoriesOperation) Wait 
    
    
    func (op *RemoveLocalInventoriesOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveLocalInventoriesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveLocalInventoriesResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SearchCallOptions
    
    
    type SearchCallOptions struct {
    	Search         []gax.CallOption
    	GetOperation   []gax.CallOption
    	ListOperations []gax.CallOption
    }

SearchCallOptions contains the retry settings for each method of SearchClient.

## SearchClient
    
    
    type SearchClient struct {
    
    	// The call options for this service.
    	CallOptions *SearchCallOptions
    	// contains filtered or unexported fields
    }

SearchClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

### func NewSearchClient 
    
    
    func NewSearchClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SearchClient, [error](https://pkg.go.dev/builtin#error))

NewSearchClient creates a new search service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSearchRESTClient 
    
    
    func NewSearchRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SearchClient, [error](https://pkg.go.dev/builtin#error))

NewSearchRESTClient creates a new search service rest client.

Service for search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SearchClient) Close 
    
    
    func (c *SearchClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SearchClient) Connection (deprecated)
    
    
    func (c *SearchClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SearchClient) GetOperation 
    
    
    func (c *SearchClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchClient)(ctx)
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
    

### func (*SearchClient) ListOperations 
    
    
    func (c *SearchClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchClient)(ctx)
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
    

### func (*SearchClient) Search 
    
    
    func (c *SearchClient) Search(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SearchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SearchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SearchResponse_SearchResultIterator

Search performs a search.

This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.SearchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#SearchRequest.
    	}
    	it := c.Search(ctx, req)
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
    		_ = it.Response.(*retailpb.SearchResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewSearchClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_SearchClient_NewSearchClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.SearchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#SearchRequest.
    	}
    	for resp, err := range c.Search(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## SearchResponse_SearchResultIterator
    
    
    type SearchResponse_SearchResultIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*retailpb.SearchResponse_SearchResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SearchResponse_SearchResultIterator manages a stream of *retailpb.SearchResponse_SearchResult.

### func (*SearchResponse_SearchResultIterator) All 
    
    
    func (it *SearchResponse_SearchResultIterator) All() iter.Seq2[*retailpb.SearchResponse_SearchResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SearchResponse_SearchResultIterator) Next 
    
    
    func (it *SearchResponse_SearchResultIterator) Next() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SearchResponse_SearchResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SearchResponse_SearchResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SearchResponse_SearchResultIterator) PageInfo 
    
    
    func (it *SearchResponse_SearchResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ServingConfigCallOptions
    
    
    type ServingConfigCallOptions struct {
    	CreateServingConfig []gax.CallOption
    	DeleteServingConfig []gax.CallOption
    	UpdateServingConfig []gax.CallOption
    	GetServingConfig    []gax.CallOption
    	ListServingConfigs  []gax.CallOption
    	AddControl          []gax.CallOption
    	RemoveControl       []gax.CallOption
    	GetOperation        []gax.CallOption
    	ListOperations      []gax.CallOption
    }

ServingConfigCallOptions contains the retry settings for each method of ServingConfigClient.

## ServingConfigClient
    
    
    type ServingConfigClient struct {
    
    	// The call options for this service.
    	CallOptions *ServingConfigCallOptions
    	// contains filtered or unexported fields
    }

ServingConfigClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for modifying ServingConfig.

### func NewServingConfigClient 
    
    
    func NewServingConfigClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ServingConfigClient, [error](https://pkg.go.dev/builtin#error))

NewServingConfigClient creates a new serving config service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for modifying ServingConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewServingConfigRESTClient 
    
    
    func NewServingConfigRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ServingConfigClient, [error](https://pkg.go.dev/builtin#error))

NewServingConfigRESTClient creates a new serving config service rest client.

Service for modifying ServingConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ServingConfigClient) AddControl 
    
    
    func (c *ServingConfigClient) AddControl(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[AddControlRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_AddControlRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ServingConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ServingConfig), [error](https://pkg.go.dev/builtin#error))

AddControl enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it’s a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.AddControlRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#AddControlRequest.
    	}
    	resp, err := c.AddControl(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ServingConfigClient) Close 
    
    
    func (c *ServingConfigClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ServingConfigClient) Connection (deprecated)
    
    
    func (c *ServingConfigClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ServingConfigClient) CreateServingConfig 
    
    
    func (c *ServingConfigClient) CreateServingConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CreateServingConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CreateServingConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ServingConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ServingConfig), [error](https://pkg.go.dev/builtin#error))

CreateServingConfig creates a ServingConfig.

A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.CreateServingConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#CreateServingConfigRequest.
    	}
    	resp, err := c.CreateServingConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ServingConfigClient) DeleteServingConfig 
    
    
    func (c *ServingConfigClient) DeleteServingConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[DeleteServingConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_DeleteServingConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteServingConfig deletes a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.DeleteServingConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#DeleteServingConfigRequest.
    	}
    	err = c.DeleteServingConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ServingConfigClient) GetOperation 
    
    
    func (c *ServingConfigClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
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
    

### func (*ServingConfigClient) GetServingConfig 
    
    
    func (c *ServingConfigClient) GetServingConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[GetServingConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_GetServingConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ServingConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ServingConfig), [error](https://pkg.go.dev/builtin#error))

GetServingConfig gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.GetServingConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#GetServingConfigRequest.
    	}
    	resp, err := c.GetServingConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ServingConfigClient) ListOperations 
    
    
    func (c *ServingConfigClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
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
    

### func (*ServingConfigClient) ListServingConfigs 
    
    
    func (c *ServingConfigClient) ListServingConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ListServingConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ListServingConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ServingConfigIterator

ListServingConfigs lists all ServingConfigs linked to this catalog.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListServingConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListServingConfigsRequest.
    	}
    	it := c.ListServingConfigs(ctx, req)
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
    		_ = it.Response.(*retailpb.ListServingConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ListServingConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ListServingConfigsRequest.
    	}
    	for resp, err := range c.ListServingConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ServingConfigClient) RemoveControl 
    
    
    func (c *ServingConfigClient) RemoveControl(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RemoveControlRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RemoveControlRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ServingConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ServingConfig), [error](https://pkg.go.dev/builtin#error))

RemoveControl disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.RemoveControlRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#RemoveControlRequest.
    	}
    	resp, err := c.RemoveControl(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ServingConfigClient) UpdateServingConfig 
    
    
    func (c *ServingConfigClient) UpdateServingConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UpdateServingConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UpdateServingConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ServingConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ServingConfig), [error](https://pkg.go.dev/builtin#error))

UpdateServingConfig updates a ServingConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewServingConfigClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_ServingConfigClient_NewServingConfigClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.UpdateServingConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#UpdateServingConfigRequest.
    	}
    	resp, err := c.UpdateServingConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## ServingConfigIterator
    
    
    type ServingConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*retailpb.ServingConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ServingConfigIterator manages a stream of *retailpb.ServingConfig.

### func (*ServingConfigIterator) All 
    
    
    func (it *ServingConfigIterator) All() iter.Seq2[*retailpb.ServingConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ServingConfigIterator) Next 
    
    
    func (it *ServingConfigIterator) Next() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ServingConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ServingConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ServingConfigIterator) PageInfo 
    
    
    func (it *ServingConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SetInventoryOperation
    
    
    type SetInventoryOperation struct {
    	// contains filtered or unexported fields
    }

SetInventoryOperation manages a long-running operation from SetInventory.

### func (*SetInventoryOperation) Done 
    
    
    func (op *SetInventoryOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*SetInventoryOperation) Metadata 
    
    
    func (op *SetInventoryOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SetInventoryMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SetInventoryMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*SetInventoryOperation) Name 
    
    
    func (op *SetInventoryOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*SetInventoryOperation) Poll 
    
    
    func (op *SetInventoryOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SetInventoryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SetInventoryResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*SetInventoryOperation) Wait 
    
    
    func (op *SetInventoryOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[SetInventoryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_SetInventoryResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## TuneModelOperation
    
    
    type TuneModelOperation struct {
    	// contains filtered or unexported fields
    }

TuneModelOperation manages a long-running operation from TuneModel.

### func (*TuneModelOperation) Done 
    
    
    func (op *TuneModelOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*TuneModelOperation) Metadata 
    
    
    func (op *TuneModelOperation) Metadata() (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[TuneModelMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_TuneModelMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*TuneModelOperation) Name 
    
    
    func (op *TuneModelOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*TuneModelOperation) Poll 
    
    
    func (op *TuneModelOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[TuneModelResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_TuneModelResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*TuneModelOperation) Wait 
    
    
    func (op *TuneModelOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[TuneModelResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_TuneModelResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UserEventCallOptions
    
    
    type UserEventCallOptions struct {
    	WriteUserEvent   []gax.CallOption
    	CollectUserEvent []gax.CallOption
    	PurgeUserEvents  []gax.CallOption
    	ImportUserEvents []gax.CallOption
    	RejoinUserEvents []gax.CallOption
    	GetOperation     []gax.CallOption
    	ListOperations   []gax.CallOption
    }

UserEventCallOptions contains the retry settings for each method of UserEventClient.

## UserEventClient
    
    
    type UserEventClient struct {
    
    	// The call options for this service.
    	CallOptions *UserEventCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

UserEventClient is a client for interacting with Vertex AI Search for commerce API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for ingesting end user actions on the customer website.

### func NewUserEventClient 
    
    
    func NewUserEventClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*UserEventClient, [error](https://pkg.go.dev/builtin#error))

NewUserEventClient creates a new user event service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for ingesting end user actions on the customer website.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewUserEventRESTClient 
    
    
    func NewUserEventRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*UserEventClient, [error](https://pkg.go.dev/builtin#error))

NewUserEventRESTClient creates a new user event service rest client.

Service for ingesting end user actions on the customer website.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*UserEventClient) Close 
    
    
    func (c *UserEventClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*UserEventClient) CollectUserEvent 
    
    
    func (c *UserEventClient) CollectUserEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[CollectUserEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_CollectUserEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[httpbodypb](https://pkg.go.dev/google.golang.org/genproto/googleapis/api/httpbody).[HttpBody](https://pkg.go.dev/google.golang.org/genproto/googleapis/api/httpbody#HttpBody), [error](https://pkg.go.dev/builtin#error))

CollectUserEvent writes a single user event from the browser.

For larger user event payload over 16 KB, the POST method should be used instead, otherwise a 400 Bad Request error is returned.

This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.CollectUserEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#CollectUserEventRequest.
    	}
    	resp, err := c.CollectUserEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*UserEventClient) Connection (deprecated)
    
    
    func (c *UserEventClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*UserEventClient) GetOperation 
    
    
    func (c *UserEventClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
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
    

### func (*UserEventClient) ImportUserEvents 
    
    
    func (c *UserEventClient) ImportUserEvents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[ImportUserEventsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_ImportUserEventsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ImportUserEventsOperation, [error](https://pkg.go.dev/builtin#error))

ImportUserEvents bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events.

Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.ImportUserEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#ImportUserEventsRequest.
    	}
    	op, err := c.ImportUserEvents(ctx, req)
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
    

### func (*UserEventClient) ImportUserEventsOperation 
    
    
    func (c *UserEventClient) ImportUserEventsOperation(name [string](https://pkg.go.dev/builtin#string)) *ImportUserEventsOperation

ImportUserEventsOperation returns a new ImportUserEventsOperation from a given name. The name must be that of a previously created ImportUserEventsOperation, possibly from a different process.

### func (*UserEventClient) ListOperations 
    
    
    func (c *UserEventClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	retail "cloud.google.com/go/retail/apiv2"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
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
    

### func (*UserEventClient) PurgeUserEvents 
    
    
    func (c *UserEventClient) PurgeUserEvents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[PurgeUserEventsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_PurgeUserEventsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*PurgeUserEventsOperation, [error](https://pkg.go.dev/builtin#error))

PurgeUserEvents deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.PurgeUserEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#PurgeUserEventsRequest.
    	}
    	op, err := c.PurgeUserEvents(ctx, req)
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
    

### func (*UserEventClient) PurgeUserEventsOperation 
    
    
    func (c *UserEventClient) PurgeUserEventsOperation(name [string](https://pkg.go.dev/builtin#string)) *PurgeUserEventsOperation

PurgeUserEventsOperation returns a new PurgeUserEventsOperation from a given name. The name must be that of a previously created PurgeUserEventsOperation, possibly from a different process.

### func (*UserEventClient) RejoinUserEvents 
    
    
    func (c *UserEventClient) RejoinUserEvents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[RejoinUserEventsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_RejoinUserEventsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RejoinUserEventsOperation, [error](https://pkg.go.dev/builtin#error))

RejoinUserEvents starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.RejoinUserEventsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#RejoinUserEventsRequest.
    	}
    	op, err := c.RejoinUserEvents(ctx, req)
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
    

### func (*UserEventClient) RejoinUserEventsOperation 
    
    
    func (c *UserEventClient) RejoinUserEventsOperation(name [string](https://pkg.go.dev/builtin#string)) *RejoinUserEventsOperation

RejoinUserEventsOperation returns a new RejoinUserEventsOperation from a given name. The name must be that of a previously created RejoinUserEventsOperation, possibly from a different process.

### func (*UserEventClient) WriteUserEvent 
    
    
    func (c *UserEventClient) WriteUserEvent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[WriteUserEventRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_WriteUserEventRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[retailpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb).[UserEvent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2/retailpb#cloud_google_com_go_retail_apiv2_retailpb_UserEvent), [error](https://pkg.go.dev/builtin#error))

WriteUserEvent writes a single user event.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	retail "cloud.google.com/go/retail/apiv2"
    
    	retailpb "cloud.google.com/go/retail/apiv2/retailpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := retail.[NewUserEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/retail/latest/apiv2.html#cloud_google_com_go_retail_apiv2_UserEventClient_NewUserEventClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &retailpb.WriteUserEventRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/retail/apiv2/retailpb#WriteUserEventRequest.
    	}
    	resp, err := c.WriteUserEvent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
