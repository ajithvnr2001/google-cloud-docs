---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/
title: Generative Language API v1beta - Package cloud.google.com/go/ai/generativelanguage/apiv1beta (v1.2.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:18.425150+00:00
---

# Generative Language API v1beta - Package cloud.google.com/go/ai/generativelanguage/apiv1beta (v1.2.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Generative Language API v1beta - Package cloud.google.com/go/ai/generativelanguage/apiv1beta (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1  0.10.2  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.4  0.2.0  0.1.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta). 

Package generativelanguage is an auto-generated package for the Generative Language API. 

The Gemini API allows developers to build generative AI applications using Gemini models. Gemini is our most capable model, built from the ground up to be multimodal. It can generalize and seamlessly understand, operate across, and combine different types of information including language, images, audio, video, and code. You can use the Gemini API for use cases like reasoning across text and images, content generation, dialogue agents, summarization and classification systems, and more.
    
    
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
    
    
    // go get cloud.google.com/go/ai/generativelanguage/apiv1beta@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := generativelanguage.NewCacheClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &generativelanguagepb.CreateCachedContentRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateCachedContentRequest.
    }
    resp, err := c.CreateCachedContent(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewCacheClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## CacheCallOptions
    
    
    type CacheCallOptions struct {
    	ListCachedContents  []gax.CallOption
    	CreateCachedContent []gax.CallOption
    	GetCachedContent    []gax.CallOption
    	UpdateCachedContent []gax.CallOption
    	DeleteCachedContent []gax.CallOption
    	CancelOperation     []gax.CallOption
    	DeleteOperation     []gax.CallOption
    	GetOperation        []gax.CallOption
    	ListOperations      []gax.CallOption
    }

CacheCallOptions contains the retry settings for each method of CacheClient.

## CacheClient
    
    
    type CacheClient struct {
    
    	// The call options for this service.
    	CallOptions *CacheCallOptions
    	// contains filtered or unexported fields
    }

CacheClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

API for managing cache of content (CachedContent resources) that can be used in GenerativeService requests. This way generate content requests can benefit from preprocessing work being done earlier, possibly lowering their computational cost. It is intended to be used with large contexts.

### func NewCacheClient 
    
    
    func NewCacheClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CacheClient, [error](https://pkg.go.dev/builtin#error))

NewCacheClient creates a new cache service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

API for managing cache of content (CachedContent resources) that can be used in GenerativeService requests. This way generate content requests can benefit from preprocessing work being done earlier, possibly lowering their computational cost. It is intended to be used with large contexts.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCacheRESTClient 
    
    
    func NewCacheRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CacheClient, [error](https://pkg.go.dev/builtin#error))

NewCacheRESTClient creates a new cache service rest client.

API for managing cache of content (CachedContent resources) that can be used in GenerativeService requests. This way generate content requests can benefit from preprocessing work being done earlier, possibly lowering their computational cost. It is intended to be used with large contexts.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CacheClient) CancelOperation 
    
    
    func (c *CacheClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CacheClient) Close 
    
    
    func (c *CacheClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CacheClient) Connection (deprecated)
    
    
    func (c *CacheClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CacheClient) CreateCachedContent 
    
    
    func (c *CacheClient) CreateCachedContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateCachedContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateCachedContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CachedContent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CachedContent), [error](https://pkg.go.dev/builtin#error))

CreateCachedContent creates CachedContent resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreateCachedContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateCachedContentRequest.
    	}
    	resp, err := c.CreateCachedContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CacheClient) DeleteCachedContent 
    
    
    func (c *CacheClient) DeleteCachedContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeleteCachedContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeleteCachedContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteCachedContent deletes CachedContent resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeleteCachedContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeleteCachedContentRequest.
    	}
    	err = c.DeleteCachedContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CacheClient) DeleteOperation 
    
    
    func (c *CacheClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CacheClient) GetCachedContent 
    
    
    func (c *CacheClient) GetCachedContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetCachedContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetCachedContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CachedContent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CachedContent), [error](https://pkg.go.dev/builtin#error))

GetCachedContent reads CachedContent resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetCachedContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetCachedContentRequest.
    	}
    	resp, err := c.GetCachedContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CacheClient) GetOperation 
    
    
    func (c *CacheClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CacheClient) ListCachedContents 
    
    
    func (c *CacheClient) ListCachedContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListCachedContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListCachedContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CachedContentIterator

ListCachedContents lists CachedContents.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListCachedContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListCachedContentsRequest.
    	}
    	it := c.ListCachedContents(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListCachedContentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListCachedContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListCachedContentsRequest.
    	}
    	for resp, err := range c.ListCachedContents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CacheClient) ListOperations 
    
    
    func (c *CacheClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CacheClient) SetGoogleClientInfo 
    
    
    func (c *CacheClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

### func (*CacheClient) UpdateCachedContent 
    
    
    func (c *CacheClient) UpdateCachedContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[UpdateCachedContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_UpdateCachedContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CachedContent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CachedContent), [error](https://pkg.go.dev/builtin#error))

UpdateCachedContent updates CachedContent resource (only expiration is updatable).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewCacheClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_CacheClient_NewCacheClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.UpdateCachedContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#UpdateCachedContentRequest.
    	}
    	resp, err := c.UpdateCachedContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CachedContentIterator
    
    
    type CachedContentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.CachedContent, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CachedContentIterator manages a stream of *generativelanguagepb.CachedContent.

### func (*CachedContentIterator) All 
    
    
    func (it *CachedContentIterator) All() iter.Seq2[*generativelanguagepb.CachedContent, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CachedContentIterator) Next 
    
    
    func (it *CachedContentIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CachedContent](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CachedContent), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CachedContentIterator) PageInfo 
    
    
    func (it *CachedContentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ChunkIterator
    
    
    type ChunkIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.Chunk, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ChunkIterator manages a stream of *generativelanguagepb.Chunk.

### func (*ChunkIterator) All 
    
    
    func (it *ChunkIterator) All() iter.Seq2[*generativelanguagepb.Chunk, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ChunkIterator) Next 
    
    
    func (it *ChunkIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Chunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Chunk), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ChunkIterator) PageInfo 
    
    
    func (it *ChunkIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CorpusIterator
    
    
    type CorpusIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.Corpus, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CorpusIterator manages a stream of *generativelanguagepb.Corpus.

### func (*CorpusIterator) All 
    
    
    func (it *CorpusIterator) All() iter.Seq2[*generativelanguagepb.Corpus, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CorpusIterator) Next 
    
    
    func (it *CorpusIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Corpus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Corpus), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CorpusIterator) PageInfo 
    
    
    func (it *CorpusIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CreateTunedModelOperation
    
    
    type CreateTunedModelOperation struct {
    	// contains filtered or unexported fields
    }

CreateTunedModelOperation manages a long-running operation from CreateTunedModel.

### func (*CreateTunedModelOperation) Done 
    
    
    func (op *CreateTunedModelOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateTunedModelOperation) Metadata 
    
    
    func (op *CreateTunedModelOperation) Metadata() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateTunedModelMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateTunedModelMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateTunedModelOperation) Name 
    
    
    func (op *CreateTunedModelOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateTunedModelOperation) Poll 
    
    
    func (op *CreateTunedModelOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TunedModel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TunedModel), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateTunedModelOperation) Wait 
    
    
    func (op *CreateTunedModelOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TunedModel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TunedModel), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DiscussCallOptions
    
    
    type DiscussCallOptions struct {
    	GenerateMessage    []gax.CallOption
    	CountMessageTokens []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

DiscussCallOptions contains the retry settings for each method of DiscussClient.

## DiscussClient
    
    
    type DiscussClient struct {
    
    	// The call options for this service.
    	CallOptions *DiscussCallOptions
    	// contains filtered or unexported fields
    }

DiscussClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

An API for using Generative Language Models (GLMs) in dialog applications.

Also known as large language models (LLMs), this API provides models that are trained for multi-turn dialog.

### func NewDiscussClient 
    
    
    func NewDiscussClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DiscussClient, [error](https://pkg.go.dev/builtin#error))

NewDiscussClient creates a new discuss service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

An API for using Generative Language Models (GLMs) in dialog applications.

Also known as large language models (LLMs), this API provides models that are trained for multi-turn dialog.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewDiscussRESTClient 
    
    
    func NewDiscussRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DiscussClient, [error](https://pkg.go.dev/builtin#error))

NewDiscussRESTClient creates a new discuss service rest client.

An API for using Generative Language Models (GLMs) in dialog applications.

Also known as large language models (LLMs), this API provides models that are trained for multi-turn dialog.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussRESTClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*DiscussClient) CancelOperation 
    
    
    func (c *DiscussClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DiscussClient) Close 
    
    
    func (c *DiscussClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*DiscussClient) Connection (deprecated)
    
    
    func (c *DiscussClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*DiscussClient) CountMessageTokens 
    
    
    func (c *DiscussClient) CountMessageTokens(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CountMessageTokensRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CountMessageTokensRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CountMessageTokensResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CountMessageTokensResponse), [error](https://pkg.go.dev/builtin#error))

CountMessageTokens runs a model’s tokenizer on a string and returns the token count.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CountMessageTokensRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CountMessageTokensRequest.
    	}
    	resp, err := c.CountMessageTokens(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DiscussClient) DeleteOperation 
    
    
    func (c *DiscussClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DiscussClient) GenerateMessage 
    
    
    func (c *DiscussClient) GenerateMessage(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateMessageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateMessageRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateMessageResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateMessageResponse), [error](https://pkg.go.dev/builtin#error))

GenerateMessage generates a response from the model given an input MessagePrompt.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GenerateMessageRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GenerateMessageRequest.
    	}
    	resp, err := c.GenerateMessage(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DiscussClient) GetOperation 
    
    
    func (c *DiscussClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DiscussClient) ListOperations 
    
    
    func (c *DiscussClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewDiscussClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DiscussClient) SetGoogleClientInfo 
    
    
    func (c *DiscussClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

## DocumentIterator
    
    
    type DocumentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.Document, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DocumentIterator manages a stream of *generativelanguagepb.Document.

### func (*DocumentIterator) All 
    
    
    func (it *DocumentIterator) All() iter.Seq2[*generativelanguagepb.Document, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DocumentIterator) Next 
    
    
    func (it *DocumentIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Document), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DocumentIterator) PageInfo 
    
    
    func (it *DocumentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## FileCallOptions
    
    
    type FileCallOptions struct {
    	CreateFile      []gax.CallOption
    	ListFiles       []gax.CallOption
    	GetFile         []gax.CallOption
    	DeleteFile      []gax.CallOption
    	DownloadFile    []gax.CallOption
    	CancelOperation []gax.CallOption
    	DeleteOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

FileCallOptions contains the retry settings for each method of FileClient.

## FileClient
    
    
    type FileClient struct {
    
    	// The call options for this service.
    	CallOptions *FileCallOptions
    	// contains filtered or unexported fields
    }

FileClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

An API for uploading and managing files.

### func NewFileClient 
    
    
    func NewFileClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FileClient, [error](https://pkg.go.dev/builtin#error))

NewFileClient creates a new file service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

An API for uploading and managing files.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewFileRESTClient 
    
    
    func NewFileRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FileClient, [error](https://pkg.go.dev/builtin#error))

NewFileRESTClient creates a new file service rest client.

An API for uploading and managing files.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*FileClient) CancelOperation 
    
    
    func (c *FileClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FileClient) Close 
    
    
    func (c *FileClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*FileClient) Connection (deprecated)
    
    
    func (c *FileClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*FileClient) CreateFile 
    
    
    func (c *FileClient) CreateFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateFileResponse), [error](https://pkg.go.dev/builtin#error))

CreateFile creates a File.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreateFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateFileRequest.
    	}
    	resp, err := c.CreateFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FileClient) DeleteFile 
    
    
    func (c *FileClient) DeleteFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeleteFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeleteFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteFile deletes the File.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeleteFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeleteFileRequest.
    	}
    	err = c.DeleteFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FileClient) DeleteOperation 
    
    
    func (c *FileClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*FileClient) DownloadFile 
    
    
    func (c *FileClient) DownloadFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DownloadFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DownloadFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DownloadFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DownloadFileResponse), [error](https://pkg.go.dev/builtin#error))

DownloadFile download the File.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DownloadFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DownloadFileRequest.
    	}
    	resp, err := c.DownloadFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FileClient) GetFile 
    
    
    func (c *FileClient) GetFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[File](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_File), [error](https://pkg.go.dev/builtin#error))

GetFile gets the metadata for the given File.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetFileRequest.
    	}
    	resp, err := c.GetFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FileClient) GetOperation 
    
    
    func (c *FileClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FileClient) ListFiles 
    
    
    func (c *FileClient) ListFiles(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListFilesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListFilesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *FileIterator

ListFiles lists the metadata for Files owned by the requesting project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListFilesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListFilesRequest.
    	}
    	it := c.ListFiles(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListFilesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListFilesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListFilesRequest.
    	}
    	for resp, err := range c.ListFiles(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FileClient) ListOperations 
    
    
    func (c *FileClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewFileClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_FileClient_NewFileClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FileClient) SetGoogleClientInfo 
    
    
    func (c *FileClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

## FileIterator
    
    
    type FileIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.File, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

FileIterator manages a stream of *generativelanguagepb.File.

### func (*FileIterator) All 
    
    
    func (it *FileIterator) All() iter.Seq2[*generativelanguagepb.File, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*FileIterator) Next 
    
    
    func (it *FileIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[File](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_File), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*FileIterator) PageInfo 
    
    
    func (it *FileIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GenerativeCallOptions
    
    
    type GenerativeCallOptions struct {
    	GenerateContent       []gax.CallOption
    	GenerateAnswer        []gax.CallOption
    	StreamGenerateContent []gax.CallOption
    	EmbedContent          []gax.CallOption
    	BatchEmbedContents    []gax.CallOption
    	CountTokens           []gax.CallOption
    	BidiGenerateContent   []gax.CallOption
    	CancelOperation       []gax.CallOption
    	DeleteOperation       []gax.CallOption
    	GetOperation          []gax.CallOption
    	ListOperations        []gax.CallOption
    }

GenerativeCallOptions contains the retry settings for each method of GenerativeClient.

## GenerativeClient
    
    
    type GenerativeClient struct {
    
    	// The call options for this service.
    	CallOptions *GenerativeCallOptions
    	// contains filtered or unexported fields
    }

GenerativeClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

API for using Large Models that generate multimodal content and have additional capabilities beyond text generation.

### func NewGenerativeClient 
    
    
    func NewGenerativeClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GenerativeClient, [error](https://pkg.go.dev/builtin#error))

NewGenerativeClient creates a new generative service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

API for using Large Models that generate multimodal content and have additional capabilities beyond text generation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewGenerativeRESTClient 
    
    
    func NewGenerativeRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*GenerativeClient, [error](https://pkg.go.dev/builtin#error))

NewGenerativeRESTClient creates a new generative service rest client.

API for using Large Models that generate multimodal content and have additional capabilities beyond text generation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*GenerativeClient) BatchEmbedContents 
    
    
    func (c *GenerativeClient) BatchEmbedContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchEmbedContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchEmbedContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchEmbedContentsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchEmbedContentsResponse), [error](https://pkg.go.dev/builtin#error))

BatchEmbedContents generates multiple embedding vectors from the input Content which consists of a batch of strings represented as EmbedContentRequest objects.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.BatchEmbedContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#BatchEmbedContentsRequest.
    	}
    	resp, err := c.BatchEmbedContents(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeClient) BidiGenerateContent 
    
    
    func (c *GenerativeClient) BidiGenerateContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerativeService_BidiGenerateContentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerativeService_BidiGenerateContentClient), [error](https://pkg.go.dev/builtin#error))

BidiGenerateContent low-Latency bidirectional streaming API that supports audio and video streaming inputs can produce multimodal output streams (audio and text).

This method is not supported for the REST transport.

#### Example
    
    
    package main
    
    import (
    	"context"
    	"io"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    	stream, err := c.BidiGenerateContent(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	go func() {
    		reqs := []*generativelanguagepb.BidiGenerateContentClientMessage{
    			// TODO: Create requests.
    		}
    		for _, req := range reqs {
    			if err := stream.Send(req); err != nil {
    				// TODO: Handle error.
    			}
    		}
    		stream.CloseSend()
    	}()
    	for {
    		resp, err := stream.Recv()
    		if err == io.EOF {
    			break
    		}
    		if err != nil {
    			// TODO: handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GenerativeClient) CancelOperation 
    
    
    func (c *GenerativeClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GenerativeClient) Close 
    
    
    func (c *GenerativeClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*GenerativeClient) Connection (deprecated)
    
    
    func (c *GenerativeClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*GenerativeClient) CountTokens 
    
    
    func (c *GenerativeClient) CountTokens(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CountTokensRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CountTokensRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CountTokensResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CountTokensResponse), [error](https://pkg.go.dev/builtin#error))

CountTokens runs a model’s tokenizer on input Content and returns the token count. Refer to the tokens guide (at <https://ai.google.dev/gemini-api/docs/tokens>) to learn more about tokens.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CountTokensRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CountTokensRequest.
    	}
    	resp, err := c.CountTokens(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeClient) DeleteOperation 
    
    
    func (c *GenerativeClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*GenerativeClient) EmbedContent 
    
    
    func (c *GenerativeClient) EmbedContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[EmbedContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_EmbedContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[EmbedContentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_EmbedContentResponse), [error](https://pkg.go.dev/builtin#error))

EmbedContent generates a text embedding vector from the input Content using the specified Gemini Embedding model (at <https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.EmbedContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#EmbedContentRequest.
    	}
    	resp, err := c.EmbedContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeClient) GenerateAnswer 
    
    
    func (c *GenerativeClient) GenerateAnswer(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateAnswerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateAnswerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateAnswerResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateAnswerResponse), [error](https://pkg.go.dev/builtin#error))

GenerateAnswer generates a grounded answer from the model given an input GenerateAnswerRequest.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GenerateAnswerRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GenerateAnswerRequest.
    	}
    	resp, err := c.GenerateAnswer(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeClient) GenerateContent 
    
    
    func (c *GenerativeClient) GenerateContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateContentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateContentResponse), [error](https://pkg.go.dev/builtin#error))

GenerateContent generates a model response given an input GenerateContentRequest. Refer to the text generation guide (at <https://ai.google.dev/gemini-api/docs/text-generation>) for detailed usage information. Input capabilities differ between models, including tuned models. Refer to the model guide (at <https://ai.google.dev/gemini-api/docs/models/gemini>) and tuning guide (at <https://ai.google.dev/gemini-api/docs/model-tuning>) for details.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GenerateContentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GenerateContentRequest.
    	}
    	resp, err := c.GenerateContent(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeClient) GetOperation 
    
    
    func (c *GenerativeClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*GenerativeClient) ListOperations 
    
    
    func (c *GenerativeClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewGenerativeClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_GenerativeClient_NewGenerativeClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*GenerativeClient) SetGoogleClientInfo 
    
    
    func (c *GenerativeClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

### func (*GenerativeClient) StreamGenerateContent 
    
    
    func (c *GenerativeClient) StreamGenerateContent(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateContentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateContentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) ([generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerativeService_StreamGenerateContentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerativeService_StreamGenerateContentClient), [error](https://pkg.go.dev/builtin#error))

StreamGenerateContent generates a streamed response (at <https://ai.google.dev/gemini-api/docs/text-generation?lang=python#generate-a-text-stream>) from the model given an input GenerateContentRequest.

## ModelCallOptions
    
    
    type ModelCallOptions struct {
    	GetModel         []gax.CallOption
    	ListModels       []gax.CallOption
    	GetTunedModel    []gax.CallOption
    	ListTunedModels  []gax.CallOption
    	CreateTunedModel []gax.CallOption
    	UpdateTunedModel []gax.CallOption
    	DeleteTunedModel []gax.CallOption
    	CancelOperation  []gax.CallOption
    	DeleteOperation  []gax.CallOption
    	GetOperation     []gax.CallOption
    	ListOperations   []gax.CallOption
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

ModelClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Provides methods for getting metadata information about Generative Models.

### func NewModelClient 
    
    
    func NewModelClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ModelClient, [error](https://pkg.go.dev/builtin#error))

NewModelClient creates a new model service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Provides methods for getting metadata information about Generative Models.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
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

Provides methods for getting metadata information about Generative Models.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelRESTClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ModelClient) CancelOperation 
    
    
    func (c *ModelClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ModelClient) Close 
    
    
    func (c *ModelClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ModelClient) Connection (deprecated)
    
    
    func (c *ModelClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ModelClient) CreateTunedModel 
    
    
    func (c *ModelClient) CreateTunedModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateTunedModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateTunedModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateTunedModelOperation, [error](https://pkg.go.dev/builtin#error))

CreateTunedModel creates a tuned model. Check intermediate tuning progress (if any) through the [google.longrunning.Operations] service.

Access status and results through the Operations service. Example: GET /v1/tunedModels/az2mb0bpw6i/operations/000-111-222

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreateTunedModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateTunedModelRequest.
    	}
    	op, err := c.CreateTunedModel(ctx, req)
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
    

### func (*ModelClient) CreateTunedModelOperation 
    
    
    func (c *ModelClient) CreateTunedModelOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateTunedModelOperation

CreateTunedModelOperation returns a new CreateTunedModelOperation from a given name. The name must be that of a previously created CreateTunedModelOperation, possibly from a different process.

### func (*ModelClient) DeleteOperation 
    
    
    func (c *ModelClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ModelClient) DeleteTunedModel 
    
    
    func (c *ModelClient) DeleteTunedModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeleteTunedModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeleteTunedModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteTunedModel deletes a tuned model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeleteTunedModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeleteTunedModelRequest.
    	}
    	err = c.DeleteTunedModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ModelClient) GetModel 
    
    
    func (c *ModelClient) GetModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Model), [error](https://pkg.go.dev/builtin#error))

GetModel gets information about a specific Model such as its version number, token limits, parameters (at <https://ai.google.dev/gemini-api/docs/models/generative-models#model-parameters>) and other metadata. Refer to the Gemini models guide (at <https://ai.google.dev/gemini-api/docs/models/gemini>) for detailed model information.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetModelRequest.
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ModelClient) GetTunedModel 
    
    
    func (c *ModelClient) GetTunedModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetTunedModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetTunedModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TunedModel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TunedModel), [error](https://pkg.go.dev/builtin#error))

GetTunedModel gets information about a specific TunedModel.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetTunedModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetTunedModelRequest.
    	}
    	resp, err := c.GetTunedModel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ModelClient) ListModels 
    
    
    func (c *ModelClient) ListModels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListModelsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListModelsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ModelIterator

ListModels lists the Models (at <https://ai.google.dev/gemini-api/docs/models/gemini>) available through the Gemini API.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListModelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListModelsRequest.
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
    		_ = it.Response.(*generativelanguagepb.ListModelsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListModelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListModelsRequest.
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ModelClient) ListTunedModels 
    
    
    func (c *ModelClient) ListTunedModels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListTunedModelsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListTunedModelsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TunedModelIterator

ListTunedModels lists created tuned models.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListTunedModelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListTunedModelsRequest.
    	}
    	it := c.ListTunedModels(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListTunedModelsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListTunedModelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListTunedModelsRequest.
    	}
    	for resp, err := range c.ListTunedModels(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ModelClient) SetGoogleClientInfo 
    
    
    func (c *ModelClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

### func (*ModelClient) UpdateTunedModel 
    
    
    func (c *ModelClient) UpdateTunedModel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[UpdateTunedModelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_UpdateTunedModelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TunedModel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TunedModel), [error](https://pkg.go.dev/builtin#error))

UpdateTunedModel updates a tuned model.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewModelClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.UpdateTunedModelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#UpdateTunedModelRequest.
    	}
    	resp, err := c.UpdateTunedModel(ctx, req)
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.Model, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ModelIterator manages a stream of *generativelanguagepb.Model.

### func (*ModelIterator) All 
    
    
    func (it *ModelIterator) All() iter.Seq2[*generativelanguagepb.Model, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ModelIterator) Next 
    
    
    func (it *ModelIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Model](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Model), [error](https://pkg.go.dev/builtin#error))

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

## PermissionCallOptions
    
    
    type PermissionCallOptions struct {
    	CreatePermission  []gax.CallOption
    	GetPermission     []gax.CallOption
    	ListPermissions   []gax.CallOption
    	UpdatePermission  []gax.CallOption
    	DeletePermission  []gax.CallOption
    	TransferOwnership []gax.CallOption
    	CancelOperation   []gax.CallOption
    	DeleteOperation   []gax.CallOption
    	GetOperation      []gax.CallOption
    	ListOperations    []gax.CallOption
    }

PermissionCallOptions contains the retry settings for each method of PermissionClient.

## PermissionClient
    
    
    type PermissionClient struct {
    
    	// The call options for this service.
    	CallOptions *PermissionCallOptions
    	// contains filtered or unexported fields
    }

PermissionClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Provides methods for managing permissions to PaLM API resources.

### func NewPermissionClient 
    
    
    func NewPermissionClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PermissionClient, [error](https://pkg.go.dev/builtin#error))

NewPermissionClient creates a new permission service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Provides methods for managing permissions to PaLM API resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewPermissionRESTClient 
    
    
    func NewPermissionRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PermissionClient, [error](https://pkg.go.dev/builtin#error))

NewPermissionRESTClient creates a new permission service rest client.

Provides methods for managing permissions to PaLM API resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*PermissionClient) CancelOperation 
    
    
    func (c *PermissionClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PermissionClient) Close 
    
    
    func (c *PermissionClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*PermissionClient) Connection (deprecated)
    
    
    func (c *PermissionClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*PermissionClient) CreatePermission 
    
    
    func (c *PermissionClient) CreatePermission(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreatePermissionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreatePermissionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Permission](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Permission), [error](https://pkg.go.dev/builtin#error))

CreatePermission create a permission to a specific resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreatePermissionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreatePermissionRequest.
    	}
    	resp, err := c.CreatePermission(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PermissionClient) DeleteOperation 
    
    
    func (c *PermissionClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PermissionClient) DeletePermission 
    
    
    func (c *PermissionClient) DeletePermission(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeletePermissionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeletePermissionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeletePermission deletes the permission.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeletePermissionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeletePermissionRequest.
    	}
    	err = c.DeletePermission(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PermissionClient) GetOperation 
    
    
    func (c *PermissionClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PermissionClient) GetPermission 
    
    
    func (c *PermissionClient) GetPermission(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetPermissionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetPermissionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Permission](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Permission), [error](https://pkg.go.dev/builtin#error))

GetPermission gets information about a specific Permission.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetPermissionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetPermissionRequest.
    	}
    	resp, err := c.GetPermission(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PermissionClient) ListOperations 
    
    
    func (c *PermissionClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PermissionClient) ListPermissions 
    
    
    func (c *PermissionClient) ListPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PermissionIterator

ListPermissions lists permissions for the specific resource.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListPermissionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListPermissionsRequest.
    	}
    	it := c.ListPermissions(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListPermissionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListPermissionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListPermissionsRequest.
    	}
    	for resp, err := range c.ListPermissions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PermissionClient) SetGoogleClientInfo 
    
    
    func (c *PermissionClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

### func (*PermissionClient) TransferOwnership 
    
    
    func (c *PermissionClient) TransferOwnership(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TransferOwnershipRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TransferOwnershipRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TransferOwnershipResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TransferOwnershipResponse), [error](https://pkg.go.dev/builtin#error))

TransferOwnership transfers ownership of the tuned model. This is the only way to change ownership of the tuned model. The current owner will be downgraded to writer role.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.TransferOwnershipRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#TransferOwnershipRequest.
    	}
    	resp, err := c.TransferOwnership(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PermissionClient) UpdatePermission 
    
    
    func (c *PermissionClient) UpdatePermission(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[UpdatePermissionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_UpdatePermissionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Permission](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Permission), [error](https://pkg.go.dev/builtin#error))

UpdatePermission updates the permission.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPermissionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PermissionClient_NewPermissionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.UpdatePermissionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#UpdatePermissionRequest.
    	}
    	resp, err := c.UpdatePermission(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## PermissionIterator
    
    
    type PermissionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.Permission, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PermissionIterator manages a stream of *generativelanguagepb.Permission.

### func (*PermissionIterator) All 
    
    
    func (it *PermissionIterator) All() iter.Seq2[*generativelanguagepb.Permission, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PermissionIterator) Next 
    
    
    func (it *PermissionIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Permission](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Permission), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PermissionIterator) PageInfo 
    
    
    func (it *PermissionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## PredictLongRunningOperation
    
    
    type PredictLongRunningOperation struct {
    	// contains filtered or unexported fields
    }

PredictLongRunningOperation manages a long-running operation from PredictLongRunning.

### func (*PredictLongRunningOperation) Done 
    
    
    func (op *PredictLongRunningOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*PredictLongRunningOperation) Metadata 
    
    
    func (op *PredictLongRunningOperation) Metadata() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[PredictLongRunningMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_PredictLongRunningMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*PredictLongRunningOperation) Name 
    
    
    func (op *PredictLongRunningOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*PredictLongRunningOperation) Poll 
    
    
    func (op *PredictLongRunningOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[PredictLongRunningResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_PredictLongRunningResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*PredictLongRunningOperation) Wait 
    
    
    func (op *PredictLongRunningOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[PredictLongRunningResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_PredictLongRunningResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## PredictionCallOptions
    
    
    type PredictionCallOptions struct {
    	Predict            []gax.CallOption
    	PredictLongRunning []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

PredictionCallOptions contains the retry settings for each method of PredictionClient.

## PredictionClient
    
    
    type PredictionClient struct {
    
    	// The call options for this service.
    	CallOptions *PredictionCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

PredictionClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

A service for online predictions and explanations.

### func NewPredictionClient 
    
    
    func NewPredictionClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*PredictionClient, [error](https://pkg.go.dev/builtin#error))

NewPredictionClient creates a new prediction service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

A service for online predictions and explanations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
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

A service for online predictions and explanations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*PredictionClient) CancelOperation 
    
    
    func (c *PredictionClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PredictionClient) Close 
    
    
    func (c *PredictionClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*PredictionClient) Connection (deprecated)
    
    
    func (c *PredictionClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*PredictionClient) DeleteOperation 
    
    
    func (c *PredictionClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*PredictionClient) GetOperation 
    
    
    func (c *PredictionClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*PredictionClient) Predict 
    
    
    func (c *PredictionClient) Predict(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[PredictRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_PredictRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[PredictResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_PredictResponse), [error](https://pkg.go.dev/builtin#error))

Predict performs a prediction request.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.PredictRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#PredictRequest.
    	}
    	resp, err := c.Predict(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*PredictionClient) PredictLongRunning 
    
    
    func (c *PredictionClient) PredictLongRunning(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[PredictLongRunningRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_PredictLongRunningRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*PredictLongRunningOperation, [error](https://pkg.go.dev/builtin#error))

PredictLongRunning same as Predict but returns an LRO.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewPredictionClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_PredictionClient_NewPredictionClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.PredictLongRunningRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#PredictLongRunningRequest.
    	}
    	op, err := c.PredictLongRunning(ctx, req)
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
    

### func (*PredictionClient) PredictLongRunningOperation 
    
    
    func (c *PredictionClient) PredictLongRunningOperation(name [string](https://pkg.go.dev/builtin#string)) *PredictLongRunningOperation

PredictLongRunningOperation returns a new PredictLongRunningOperation from a given name. The name must be that of a previously created PredictLongRunningOperation, possibly from a different process.

### func (*PredictionClient) SetGoogleClientInfo 
    
    
    func (c *PredictionClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

## RetrieverCallOptions
    
    
    type RetrieverCallOptions struct {
    	CreateCorpus      []gax.CallOption
    	GetCorpus         []gax.CallOption
    	UpdateCorpus      []gax.CallOption
    	DeleteCorpus      []gax.CallOption
    	ListCorpora       []gax.CallOption
    	QueryCorpus       []gax.CallOption
    	CreateDocument    []gax.CallOption
    	GetDocument       []gax.CallOption
    	UpdateDocument    []gax.CallOption
    	DeleteDocument    []gax.CallOption
    	ListDocuments     []gax.CallOption
    	QueryDocument     []gax.CallOption
    	CreateChunk       []gax.CallOption
    	BatchCreateChunks []gax.CallOption
    	GetChunk          []gax.CallOption
    	UpdateChunk       []gax.CallOption
    	BatchUpdateChunks []gax.CallOption
    	DeleteChunk       []gax.CallOption
    	BatchDeleteChunks []gax.CallOption
    	ListChunks        []gax.CallOption
    	CancelOperation   []gax.CallOption
    	DeleteOperation   []gax.CallOption
    	GetOperation      []gax.CallOption
    	ListOperations    []gax.CallOption
    }

RetrieverCallOptions contains the retry settings for each method of RetrieverClient.

## RetrieverClient
    
    
    type RetrieverClient struct {
    
    	// The call options for this service.
    	CallOptions *RetrieverCallOptions
    	// contains filtered or unexported fields
    }

RetrieverClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

An API for semantic search over a corpus of user uploaded content.

### func NewRetrieverClient 
    
    
    func NewRetrieverClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*RetrieverClient, [error](https://pkg.go.dev/builtin#error))

NewRetrieverClient creates a new retriever service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

An API for semantic search over a corpus of user uploaded content.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRetrieverRESTClient 
    
    
    func NewRetrieverRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*RetrieverClient, [error](https://pkg.go.dev/builtin#error))

NewRetrieverRESTClient creates a new retriever service rest client.

An API for semantic search over a corpus of user uploaded content.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*RetrieverClient) BatchCreateChunks 
    
    
    func (c *RetrieverClient) BatchCreateChunks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchCreateChunksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchCreateChunksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchCreateChunksResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchCreateChunksResponse), [error](https://pkg.go.dev/builtin#error))

BatchCreateChunks batch create Chunks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.BatchCreateChunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#BatchCreateChunksRequest.
    	}
    	resp, err := c.BatchCreateChunks(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) BatchDeleteChunks 
    
    
    func (c *RetrieverClient) BatchDeleteChunks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchDeleteChunksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchDeleteChunksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

BatchDeleteChunks batch delete Chunks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.BatchDeleteChunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#BatchDeleteChunksRequest.
    	}
    	err = c.BatchDeleteChunks(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*RetrieverClient) BatchUpdateChunks 
    
    
    func (c *RetrieverClient) BatchUpdateChunks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchUpdateChunksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchUpdateChunksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchUpdateChunksResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchUpdateChunksResponse), [error](https://pkg.go.dev/builtin#error))

BatchUpdateChunks batch update Chunks.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.BatchUpdateChunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#BatchUpdateChunksRequest.
    	}
    	resp, err := c.BatchUpdateChunks(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) CancelOperation 
    
    
    func (c *RetrieverClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*RetrieverClient) Close 
    
    
    func (c *RetrieverClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*RetrieverClient) Connection (deprecated)
    
    
    func (c *RetrieverClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*RetrieverClient) CreateChunk 
    
    
    func (c *RetrieverClient) CreateChunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateChunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateChunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Chunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Chunk), [error](https://pkg.go.dev/builtin#error))

CreateChunk creates a Chunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreateChunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateChunkRequest.
    	}
    	resp, err := c.CreateChunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) CreateCorpus 
    
    
    func (c *RetrieverClient) CreateCorpus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateCorpusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateCorpusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Corpus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Corpus), [error](https://pkg.go.dev/builtin#error))

CreateCorpus creates an empty Corpus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreateCorpusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateCorpusRequest.
    	}
    	resp, err := c.CreateCorpus(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) CreateDocument 
    
    
    func (c *RetrieverClient) CreateDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CreateDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CreateDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Document), [error](https://pkg.go.dev/builtin#error))

CreateDocument creates an empty Document.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CreateDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CreateDocumentRequest.
    	}
    	resp, err := c.CreateDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) DeleteChunk 
    
    
    func (c *RetrieverClient) DeleteChunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeleteChunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeleteChunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteChunk deletes a Chunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeleteChunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeleteChunkRequest.
    	}
    	err = c.DeleteChunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*RetrieverClient) DeleteCorpus 
    
    
    func (c *RetrieverClient) DeleteCorpus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeleteCorpusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeleteCorpusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteCorpus deletes a Corpus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeleteCorpusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeleteCorpusRequest.
    	}
    	err = c.DeleteCorpus(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*RetrieverClient) DeleteDocument 
    
    
    func (c *RetrieverClient) DeleteDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[DeleteDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_DeleteDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteDocument deletes a Document.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.DeleteDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#DeleteDocumentRequest.
    	}
    	err = c.DeleteDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*RetrieverClient) DeleteOperation 
    
    
    func (c *RetrieverClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*RetrieverClient) GetChunk 
    
    
    func (c *RetrieverClient) GetChunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetChunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetChunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Chunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Chunk), [error](https://pkg.go.dev/builtin#error))

GetChunk gets information about a specific Chunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetChunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetChunkRequest.
    	}
    	resp, err := c.GetChunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) GetCorpus 
    
    
    func (c *RetrieverClient) GetCorpus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetCorpusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetCorpusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Corpus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Corpus), [error](https://pkg.go.dev/builtin#error))

GetCorpus gets information about a specific Corpus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetCorpusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetCorpusRequest.
    	}
    	resp, err := c.GetCorpus(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) GetDocument 
    
    
    func (c *RetrieverClient) GetDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GetDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GetDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Document), [error](https://pkg.go.dev/builtin#error))

GetDocument gets information about a specific Document.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GetDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GetDocumentRequest.
    	}
    	resp, err := c.GetDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) GetOperation 
    
    
    func (c *RetrieverClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) ListChunks 
    
    
    func (c *RetrieverClient) ListChunks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListChunksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListChunksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ChunkIterator

ListChunks lists all Chunks in a Document.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListChunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListChunksRequest.
    	}
    	it := c.ListChunks(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListChunksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListChunksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListChunksRequest.
    	}
    	for resp, err := range c.ListChunks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*RetrieverClient) ListCorpora 
    
    
    func (c *RetrieverClient) ListCorpora(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListCorporaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListCorporaRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CorpusIterator

ListCorpora lists all Corpora owned by the user.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListCorporaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListCorporaRequest.
    	}
    	it := c.ListCorpora(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListCorporaResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListCorporaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListCorporaRequest.
    	}
    	for resp, err := range c.ListCorpora(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*RetrieverClient) ListDocuments 
    
    
    func (c *RetrieverClient) ListDocuments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[ListDocumentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_ListDocumentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DocumentIterator

ListDocuments lists all Documents in a Corpus.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListDocumentsRequest.
    	}
    	it := c.ListDocuments(ctx, req)
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
    		_ = it.Response.(*generativelanguagepb.ListDocumentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.ListDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#ListDocumentsRequest.
    	}
    	for resp, err := range c.ListDocuments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*RetrieverClient) ListOperations 
    
    
    func (c *RetrieverClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*RetrieverClient) QueryCorpus 
    
    
    func (c *RetrieverClient) QueryCorpus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[QueryCorpusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_QueryCorpusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[QueryCorpusResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_QueryCorpusResponse), [error](https://pkg.go.dev/builtin#error))

QueryCorpus performs semantic search over a Corpus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.QueryCorpusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#QueryCorpusRequest.
    	}
    	resp, err := c.QueryCorpus(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) QueryDocument 
    
    
    func (c *RetrieverClient) QueryDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[QueryDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_QueryDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[QueryDocumentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_QueryDocumentResponse), [error](https://pkg.go.dev/builtin#error))

QueryDocument performs semantic search over a Document.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.QueryDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#QueryDocumentRequest.
    	}
    	resp, err := c.QueryDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) SetGoogleClientInfo 
    
    
    func (c *RetrieverClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

### func (*RetrieverClient) UpdateChunk 
    
    
    func (c *RetrieverClient) UpdateChunk(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[UpdateChunkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_UpdateChunkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Chunk](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Chunk), [error](https://pkg.go.dev/builtin#error))

UpdateChunk updates a Chunk.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.UpdateChunkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#UpdateChunkRequest.
    	}
    	resp, err := c.UpdateChunk(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) UpdateCorpus 
    
    
    func (c *RetrieverClient) UpdateCorpus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[UpdateCorpusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_UpdateCorpusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Corpus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Corpus), [error](https://pkg.go.dev/builtin#error))

UpdateCorpus updates a Corpus.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.UpdateCorpusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#UpdateCorpusRequest.
    	}
    	resp, err := c.UpdateCorpus(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*RetrieverClient) UpdateDocument 
    
    
    func (c *RetrieverClient) UpdateDocument(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[UpdateDocumentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_UpdateDocumentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[Document](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_Document), [error](https://pkg.go.dev/builtin#error))

UpdateDocument updates a Document.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.[NewRetrieverClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta.html#cloud_google_com_go_ai_generativelanguage_apiv1beta_RetrieverClient_NewRetrieverClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.UpdateDocumentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#UpdateDocumentRequest.
    	}
    	resp, err := c.UpdateDocument(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## TextCallOptions
    
    
    type TextCallOptions struct {
    	GenerateText    []gax.CallOption
    	EmbedText       []gax.CallOption
    	BatchEmbedText  []gax.CallOption
    	CountTextTokens []gax.CallOption
    	CancelOperation []gax.CallOption
    	DeleteOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

TextCallOptions contains the retry settings for each method of TextClient.

## TextClient
    
    
    type TextClient struct {
    
    	// The call options for this service.
    	CallOptions *TextCallOptions
    	// contains filtered or unexported fields
    }

TextClient is a client for interacting with Generative Language API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

API for using Generative Language Models (GLMs) trained to generate text.

Also known as Large Language Models (LLM)s, these generate text given an input prompt from the user.

### func NewTextClient 
    
    
    func NewTextClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TextClient, [error](https://pkg.go.dev/builtin#error))

NewTextClient creates a new text service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

API for using Generative Language Models (GLMs) trained to generate text.

Also known as Large Language Models (LLM)s, these generate text given an input prompt from the user.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTextRESTClient 
    
    
    func NewTextRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TextClient, [error](https://pkg.go.dev/builtin#error))

NewTextRESTClient creates a new text service rest client.

API for using Generative Language Models (GLMs) trained to generate text.

Also known as Large Language Models (LLM)s, these generate text given an input prompt from the user.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextRESTClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TextClient) BatchEmbedText 
    
    
    func (c *TextClient) BatchEmbedText(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchEmbedTextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchEmbedTextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[BatchEmbedTextResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_BatchEmbedTextResponse), [error](https://pkg.go.dev/builtin#error))

BatchEmbedText generates multiple embeddings from the model given input text in a synchronous call.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.BatchEmbedTextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#BatchEmbedTextRequest.
    	}
    	resp, err := c.BatchEmbedText(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TextClient) CancelOperation 
    
    
    func (c *TextClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.[CancelOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_CancelOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TextClient) Close 
    
    
    func (c *TextClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TextClient) Connection (deprecated)
    
    
    func (c *TextClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TextClient) CountTextTokens 
    
    
    func (c *TextClient) CountTextTokens(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CountTextTokensRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CountTextTokensRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[CountTextTokensResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_CountTextTokensResponse), [error](https://pkg.go.dev/builtin#error))

CountTextTokens runs a model’s tokenizer on a text and returns the token count.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.CountTextTokensRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#CountTextTokensRequest.
    	}
    	resp, err := c.CountTextTokens(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TextClient) DeleteOperation 
    
    
    func (c *TextClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.[DeleteOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_DeleteOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TextClient) EmbedText 
    
    
    func (c *TextClient) EmbedText(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[EmbedTextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_EmbedTextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[EmbedTextResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_EmbedTextResponse), [error](https://pkg.go.dev/builtin#error))

EmbedText generates an embedding from the model given an input message.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.EmbedTextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#EmbedTextRequest.
    	}
    	resp, err := c.EmbedText(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TextClient) GenerateText 
    
    
    func (c *TextClient) GenerateText(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateTextRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateTextRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[GenerateTextResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_GenerateTextResponse), [error](https://pkg.go.dev/builtin#error))

GenerateText generates a response from the model given an input message.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	generativelanguagepb "cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &generativelanguagepb.GenerateTextRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb#GenerateTextRequest.
    	}
    	resp, err := c.GenerateText(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TextClient) GetOperation 
    
    
    func (c *TextClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[GetOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_GetOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest.
    	}
    	resp, err := c.[GetOperation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_GetOperation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TextClient) ListOperations 
    
    
    func (c *TextClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    
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
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	it := c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req)
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
    
    	generativelanguage "cloud.google.com/go/ai/generativelanguage/apiv1beta"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := generativelanguage.NewTextClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &longrunningpb.[ListOperationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_ListOperationsRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest.
    	}
    	for resp, err := range c.[ListOperations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_UnimplementedOperationsServer_ListOperations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TextClient) SetGoogleClientInfo 
    
    
    func (c *TextClient) SetGoogleClientInfo(keyval [string](https://pkg.go.dev/builtin#string))

SetGoogleClientInfo sets the name and version of the application in the `x-goog-api-client` header passed on each request. Intended for use by Google-written clients.

SetGoogleClientInfo is not concurrency-safe and should only be invoked sequentially before concurrent operations begin.

## TunedModelIterator
    
    
    type TunedModelIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*generativelanguagepb.TunedModel, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TunedModelIterator manages a stream of *generativelanguagepb.TunedModel.

### func (*TunedModelIterator) All 
    
    
    func (it *TunedModelIterator) All() iter.Seq2[*generativelanguagepb.TunedModel, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TunedModelIterator) Next 
    
    
    func (it *TunedModelIterator) Next() (*[generativelanguagepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb).[TunedModel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/ai/latest/generativelanguage/apiv1beta/generativelanguagepb#cloud_google_com_go_ai_generativelanguage_apiv1beta_generativelanguagepb_TunedModel), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TunedModelIterator) PageInfo 
    
    
    func (it *TunedModelIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
