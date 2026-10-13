---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/
title: Cloud Build API v1 - Package cloud.google.com/go/cloudbuild/apiv1 (v1.34.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:37.014247+00:00
---

# Cloud Build API v1 - Package cloud.google.com/go/cloudbuild/apiv1 (v1.34.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Build API v1 - Package cloud.google.com/go/cloudbuild/apiv1 (v1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.3  1.21.0  1.20.0  1.19.2  1.18.1  1.17.1  1.16.6  1.15.1  1.14.3  1.13.0  1.12.0  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/cloudbuild/apiv1). 

Creates and manages builds on Google Cloud Platform. 

## Use of Context

The ctx passed to NewClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method. 

For information about setting deadlines, reusing contexts, and more please visit godoc.org/cloud.google.com/go. 

Deprecated: Please use cloud.google.com/go/cloudbuild/apiv1/v2.

## Functions 

### func DefaultAuthScopes (deprecated)
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## BuildIterator (deprecated)
    
    
    type BuildIterator struct {
    
    	// InternalFetch is for use by the Google Cloud Libraries only.
    	// It is not part of the stable interface of this package.
    	//
    	// InternalFetch returns results from a single call to the underlying RPC.
    	// The number of results is no greater than pageSize.
    	// If there are no more results, nextPageToken is empty and err is nil.
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*cloudbuildpb.Build, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

BuildIterator manages a stream of *cloudbuildpb.Build.

### func (*BuildIterator) Next (deprecated)
    
    
    func (it *BuildIterator) Next() (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[Build](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_Build), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*BuildIterator) PageInfo (deprecated)
    
    
    func (it *BuildIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the google.golang.org/api/iterator package for details.

## CallOptions (deprecated)
    
    
    type CallOptions struct {
    	CreateBuild        []gax.CallOption
    	GetBuild           []gax.CallOption
    	ListBuilds         []gax.CallOption
    	CancelBuild        []gax.CallOption
    	CreateBuildTrigger []gax.CallOption
    	GetBuildTrigger    []gax.CallOption
    	ListBuildTriggers  []gax.CallOption
    	DeleteBuildTrigger []gax.CallOption
    	UpdateBuildTrigger []gax.CallOption
    	RunBuildTrigger    []gax.CallOption
    	RetryBuild         []gax.CallOption
    	CreateWorkerPool   []gax.CallOption
    	GetWorkerPool      []gax.CallOption
    	DeleteWorkerPool   []gax.CallOption
    	UpdateWorkerPool   []gax.CallOption
    	ListWorkerPools    []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client (deprecated)
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Cloud Build API.

Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

### func NewClient (deprecated)
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new cloud build client.

Creates and manages builds on Google Cloud Platform.

The main concept used by this API is a Build, which describes the location of the source to build, how to build the source, and where to store the built artifacts, if any.

A user can list previously-requested builds or get builds by their ID to determine the status of the build.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) CancelBuild (deprecated)
    
    
    func (c *Client) CancelBuild(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[CancelBuildRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_CancelBuildRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[Build](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_Build), [error](https://pkg.go.dev/builtin#error))

CancelBuild cancels a build in progress.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.CancelBuildRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.CancelBuild(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) Close (deprecated)
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. The user should invoke this when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns the client's connection to the API service.

### func (*Client) CreateBuild (deprecated)
    
    
    func (c *Client) CreateBuild(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[CreateBuildRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_CreateBuildRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))

CreateBuild starts a build with the specified configuration.

This method returns a long-running Operation, which includes the build ID. Pass the build ID to GetBuild to determine the build status (such as SUCCESS or FAILURE).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.CreateBuildRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.CreateBuild(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateBuildTrigger (deprecated)
    
    
    func (c *Client) CreateBuildTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[CreateBuildTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_CreateBuildTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[BuildTrigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_BuildTrigger), [error](https://pkg.go.dev/builtin#error))

CreateBuildTrigger creates a new BuildTrigger.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.CreateBuildTriggerRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.CreateBuildTrigger(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateWorkerPool (deprecated)
    
    
    func (c *Client) CreateWorkerPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[CreateWorkerPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_CreateWorkerPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateWorkerPoolOperation, [error](https://pkg.go.dev/builtin#error))

CreateWorkerPool creates a WorkerPool to run the builds, and returns the new worker pool.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.CreateWorkerPoolRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.CreateWorkerPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateWorkerPoolOperation (deprecated)
    
    
    func (c *Client) CreateWorkerPoolOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateWorkerPoolOperation

CreateWorkerPoolOperation returns a new CreateWorkerPoolOperation from a given name. The name must be that of a previously created CreateWorkerPoolOperation, possibly from a different process.

### func (*Client) DeleteBuildTrigger (deprecated)
    
    
    func (c *Client) DeleteBuildTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[DeleteBuildTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_DeleteBuildTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteBuildTrigger deletes a BuildTrigger by its project ID and trigger ID.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.DeleteBuildTriggerRequest{
    		// TODO: Fill request struct fields.
    	}
    	err = c.DeleteBuildTrigger(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteWorkerPool (deprecated)
    
    
    func (c *Client) DeleteWorkerPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[DeleteWorkerPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_DeleteWorkerPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteWorkerPool deletes a WorkerPool by its project ID and WorkerPool name.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.DeleteWorkerPoolRequest{
    		// TODO: Fill request struct fields.
    	}
    	err = c.DeleteWorkerPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) GetBuild (deprecated)
    
    
    func (c *Client) GetBuild(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[GetBuildRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_GetBuildRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[Build](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_Build), [error](https://pkg.go.dev/builtin#error))

GetBuild returns information about a previously requested build.

The Build that is returned includes its status (such as SUCCESS, FAILURE, or WORKING), and timing information.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.GetBuildRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.GetBuild(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetBuildTrigger (deprecated)
    
    
    func (c *Client) GetBuildTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[GetBuildTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_GetBuildTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[BuildTrigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_BuildTrigger), [error](https://pkg.go.dev/builtin#error))

GetBuildTrigger returns information about a BuildTrigger.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.GetBuildTriggerRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.GetBuildTrigger(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetWorkerPool (deprecated)
    
    
    func (c *Client) GetWorkerPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[GetWorkerPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_GetWorkerPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[WorkerPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_WorkerPool), [error](https://pkg.go.dev/builtin#error))

GetWorkerPool returns information about a WorkerPool.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.GetWorkerPoolRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.GetWorkerPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListBuildTriggers (deprecated)
    
    
    func (c *Client) ListBuildTriggers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[ListBuildTriggersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_ListBuildTriggersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[ListBuildTriggersResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_ListBuildTriggersResponse), [error](https://pkg.go.dev/builtin#error))

ListBuildTriggers lists existing BuildTriggers.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.ListBuildTriggersRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.ListBuildTriggers(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListBuilds (deprecated)
    
    
    func (c *Client) ListBuilds(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[ListBuildsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_ListBuildsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *BuildIterator

ListBuilds lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.ListBuildsRequest{
    		// TODO: Fill request struct fields.
    	}
    	it := c.ListBuilds(ctx, req)
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
    	}
    }
    

### func (*Client) ListWorkerPools (deprecated)
    
    
    func (c *Client) ListWorkerPools(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[ListWorkerPoolsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_ListWorkerPoolsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[ListWorkerPoolsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_ListWorkerPoolsResponse), [error](https://pkg.go.dev/builtin#error))

ListWorkerPools list project's WorkerPools.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.ListWorkerPoolsRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.ListWorkerPools(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RetryBuild (deprecated)
    
    
    func (c *Client) RetryBuild(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[RetryBuildRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_RetryBuildRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))

RetryBuild creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:
    
    
    Triggered builds resolve to a precise revision; therefore a retry of a
    triggered build will result in a build that uses the same revision.
    

For non-triggered builds that specify RepoSource:
    
    
    If the original build built from the tip of a branch, the retried build
    will build from the tip of that branch, which may not be the same revision
    as the original build.
    
    If the original build specified a commit sha or revision ID, the retried
    build will use the identical source.
    

For builds that specify StorageSource:
    
    
    If the original build pulled source from Google Cloud Storage without
    specifying the generation of the object, the new build will use the current
    object, which may be different from the original build source.
    
    If the original build pulled source from Cloud Storage and specified the
    generation of the object, the new build will attempt to use the same
    object, which may or may not be available depending on the bucket's
    lifecycle management settings.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.RetryBuildRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.RetryBuild(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RunBuildTrigger (deprecated)
    
    
    func (c *Client) RunBuildTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[RunBuildTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_RunBuildTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*longrunningpb.Operation, [error](https://pkg.go.dev/builtin#error))

RunBuildTrigger runs a BuildTrigger at a particular source revision.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.RunBuildTriggerRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.RunBuildTrigger(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateBuildTrigger (deprecated)
    
    
    func (c *Client) UpdateBuildTrigger(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[UpdateBuildTriggerRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_UpdateBuildTriggerRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[BuildTrigger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_BuildTrigger), [error](https://pkg.go.dev/builtin#error))

UpdateBuildTrigger updates a BuildTrigger by its project ID and trigger ID.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.UpdateBuildTriggerRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.UpdateBuildTrigger(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateWorkerPool (deprecated)
    
    
    func (c *Client) UpdateWorkerPool(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[UpdateWorkerPoolRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_UpdateWorkerPoolRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateWorkerPoolOperation, [error](https://pkg.go.dev/builtin#error))

UpdateWorkerPool update a WorkerPool.

This API is experimental.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	cloudbuild "cloud.google.com/go/cloudbuild/apiv1"
    	"cloud.google.com/go/cloudbuild/apiv1/v2/cloudbuildpb"
    )
    
    func main() {
    	ctx := context.Background()
    	c, err := cloudbuild.NewClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	req := &cloudbuildpb.UpdateWorkerPoolRequest{
    		// TODO: Fill request struct fields.
    	}
    	resp, err := c.UpdateWorkerPool(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateWorkerPoolOperation (deprecated)
    
    
    func (c *Client) UpdateWorkerPoolOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateWorkerPoolOperation

UpdateWorkerPoolOperation returns a new UpdateWorkerPoolOperation from a given name. The name must be that of a previously created UpdateWorkerPoolOperation, possibly from a different process.

## CreateWorkerPoolOperation (deprecated)
    
    
    type CreateWorkerPoolOperation struct {
    	// contains filtered or unexported fields
    }

CreateWorkerPoolOperation manages a long-running operation from CreateWorkerPool.

### func (*CreateWorkerPoolOperation) Done (deprecated)
    
    
    func (op *CreateWorkerPoolOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateWorkerPoolOperation) Metadata (deprecated)
    
    
    func (op *CreateWorkerPoolOperation) Metadata() (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[CreateWorkerPoolOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_CreateWorkerPoolOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateWorkerPoolOperation) Name (deprecated)
    
    
    func (op *CreateWorkerPoolOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateWorkerPoolOperation) Poll (deprecated)
    
    
    func (op *CreateWorkerPoolOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[WorkerPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_WorkerPool), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateWorkerPoolOperation) Wait (deprecated)
    
    
    func (op *CreateWorkerPoolOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[WorkerPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_WorkerPool), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateWorkerPoolOperation (deprecated)
    
    
    type UpdateWorkerPoolOperation struct {
    	// contains filtered or unexported fields
    }

UpdateWorkerPoolOperation manages a long-running operation from UpdateWorkerPool.

### func (*UpdateWorkerPoolOperation) Done (deprecated)
    
    
    func (op *UpdateWorkerPoolOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateWorkerPoolOperation) Metadata (deprecated)
    
    
    func (op *UpdateWorkerPoolOperation) Metadata() (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[UpdateWorkerPoolOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_UpdateWorkerPoolOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateWorkerPoolOperation) Name (deprecated)
    
    
    func (op *UpdateWorkerPoolOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateWorkerPoolOperation) Poll (deprecated)
    
    
    func (op *UpdateWorkerPoolOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[WorkerPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_WorkerPool), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateWorkerPoolOperation) Wait (deprecated)
    
    
    func (op *UpdateWorkerPoolOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[cloudbuildpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb).[WorkerPool](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudbuild/latest/apiv1/v2/cloudbuildpb#cloud_google_com_go_cloudbuild_apiv1_v2_cloudbuildpb_WorkerPool), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
