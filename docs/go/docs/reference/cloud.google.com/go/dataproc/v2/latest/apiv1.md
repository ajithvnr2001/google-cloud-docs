---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/
title: Cloud Dataproc API v1 - Package cloud.google.com/go/dataproc/v2/apiv1 (v2.26.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:34.582449+00:00
---

# Cloud Dataproc API v1 - Package cloud.google.com/go/dataproc/v2/apiv1 (v2.26.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Dataproc API v1 - Package cloud.google.com/go/dataproc/v2/apiv1 (v2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.1  2.13.0  2.12.0  2.11.2  2.10.1  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.2  2.3.0  2.2.3  2.0.2 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1). 

Package dataproc is an auto-generated package for the Cloud Dataproc API. 

Manages Hadoop-based clusters and jobs on Google Cloud Platform. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/dataproc/v2/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := dataproc.NewAutoscalingPolicyClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &dataprocpb.CreateAutoscalingPolicyRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateAutoscalingPolicyRequest.
    }
    resp, err := c.CreateAutoscalingPolicy(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewAutoscalingPolicyClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AutoscalingPolicyCallOptions
    
    
    type AutoscalingPolicyCallOptions struct {
    	CreateAutoscalingPolicy []gax.CallOption
    	UpdateAutoscalingPolicy []gax.CallOption
    	GetAutoscalingPolicy    []gax.CallOption
    	ListAutoscalingPolicies []gax.CallOption
    	DeleteAutoscalingPolicy []gax.CallOption
    	GetIamPolicy            []gax.CallOption
    	SetIamPolicy            []gax.CallOption
    	TestIamPermissions      []gax.CallOption
    	CancelOperation         []gax.CallOption
    	DeleteOperation         []gax.CallOption
    	GetOperation            []gax.CallOption
    	ListOperations          []gax.CallOption
    }

AutoscalingPolicyCallOptions contains the retry settings for each method of AutoscalingPolicyClient.

## AutoscalingPolicyClient
    
    
    type AutoscalingPolicyClient struct {
    
    	// The call options for this service.
    	CallOptions *AutoscalingPolicyCallOptions
    	// contains filtered or unexported fields
    }

AutoscalingPolicyClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The API interface for managing autoscaling policies in the Dataproc API.

### func NewAutoscalingPolicyClient 
    
    
    func NewAutoscalingPolicyClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AutoscalingPolicyClient, [error](https://pkg.go.dev/builtin#error))

NewAutoscalingPolicyClient creates a new autoscaling policy service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The API interface for managing autoscaling policies in the Dataproc API.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAutoscalingPolicyRESTClient 
    
    
    func NewAutoscalingPolicyRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AutoscalingPolicyClient, [error](https://pkg.go.dev/builtin#error))

NewAutoscalingPolicyRESTClient creates a new autoscaling policy service rest client.

The API interface for managing autoscaling policies in the Dataproc API.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AutoscalingPolicyClient) CancelOperation 
    
    
    func (c *AutoscalingPolicyClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
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
    

### func (*AutoscalingPolicyClient) Close 
    
    
    func (c *AutoscalingPolicyClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AutoscalingPolicyClient) Connection (deprecated)
    
    
    func (c *AutoscalingPolicyClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AutoscalingPolicyClient) CreateAutoscalingPolicy 
    
    
    func (c *AutoscalingPolicyClient) CreateAutoscalingPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateAutoscalingPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateAutoscalingPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[AutoscalingPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_AutoscalingPolicy), [error](https://pkg.go.dev/builtin#error))

CreateAutoscalingPolicy creates new autoscaling policy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateAutoscalingPolicyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateAutoscalingPolicyRequest.
    	}
    	resp, err := c.CreateAutoscalingPolicy(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AutoscalingPolicyClient) DeleteAutoscalingPolicy 
    
    
    func (c *AutoscalingPolicyClient) DeleteAutoscalingPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteAutoscalingPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteAutoscalingPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAutoscalingPolicy deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteAutoscalingPolicyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteAutoscalingPolicyRequest.
    	}
    	err = c.DeleteAutoscalingPolicy(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AutoscalingPolicyClient) DeleteOperation 
    
    
    func (c *AutoscalingPolicyClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
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
    

### func (*AutoscalingPolicyClient) GetAutoscalingPolicy 
    
    
    func (c *AutoscalingPolicyClient) GetAutoscalingPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetAutoscalingPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetAutoscalingPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[AutoscalingPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_AutoscalingPolicy), [error](https://pkg.go.dev/builtin#error))

GetAutoscalingPolicy retrieves autoscaling policy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetAutoscalingPolicyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetAutoscalingPolicyRequest.
    	}
    	resp, err := c.GetAutoscalingPolicy(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AutoscalingPolicyClient) GetIamPolicy 
    
    
    func (c *AutoscalingPolicyClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*AutoscalingPolicyClient) GetOperation 
    
    
    func (c *AutoscalingPolicyClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
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
    

### func (*AutoscalingPolicyClient) ListAutoscalingPolicies 
    
    
    func (c *AutoscalingPolicyClient) ListAutoscalingPolicies(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListAutoscalingPoliciesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListAutoscalingPoliciesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AutoscalingPolicyIterator

ListAutoscalingPolicies lists autoscaling policies in the project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListAutoscalingPoliciesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListAutoscalingPoliciesRequest.
    	}
    	it := c.ListAutoscalingPolicies(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListAutoscalingPoliciesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListAutoscalingPoliciesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListAutoscalingPoliciesRequest.
    	}
    	for resp, err := range c.ListAutoscalingPolicies(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AutoscalingPolicyClient) ListOperations 
    
    
    func (c *AutoscalingPolicyClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
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
    

### func (*AutoscalingPolicyClient) SetIamPolicy 
    
    
    func (c *AutoscalingPolicyClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*AutoscalingPolicyClient) TestIamPermissions 
    
    
    func (c *AutoscalingPolicyClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*AutoscalingPolicyClient) UpdateAutoscalingPolicy 
    
    
    func (c *AutoscalingPolicyClient) UpdateAutoscalingPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[UpdateAutoscalingPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_UpdateAutoscalingPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[AutoscalingPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_AutoscalingPolicy), [error](https://pkg.go.dev/builtin#error))

UpdateAutoscalingPolicy updates (replaces) autoscaling policy.

Disabled check for update_mask, because all updates will be full replacements.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewAutoscalingPolicyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_AutoscalingPolicyClient_NewAutoscalingPolicyClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.UpdateAutoscalingPolicyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#UpdateAutoscalingPolicyRequest.
    	}
    	resp, err := c.UpdateAutoscalingPolicy(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## AutoscalingPolicyIterator
    
    
    type AutoscalingPolicyIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.AutoscalingPolicy, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AutoscalingPolicyIterator manages a stream of *dataprocpb.AutoscalingPolicy.

### func (*AutoscalingPolicyIterator) All 
    
    
    func (it *AutoscalingPolicyIterator) All() iter.Seq2[*dataprocpb.AutoscalingPolicy, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AutoscalingPolicyIterator) Next 
    
    
    func (it *AutoscalingPolicyIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[AutoscalingPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_AutoscalingPolicy), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AutoscalingPolicyIterator) PageInfo 
    
    
    func (it *AutoscalingPolicyIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## BatchControllerCallOptions
    
    
    type BatchControllerCallOptions struct {
    	CreateBatch        []gax.CallOption
    	GetBatch           []gax.CallOption
    	ListBatches        []gax.CallOption
    	DeleteBatch        []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

BatchControllerCallOptions contains the retry settings for each method of BatchControllerClient.

## BatchControllerClient
    
    
    type BatchControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *BatchControllerCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

BatchControllerClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The BatchController provides methods to manage batch workloads.

### func NewBatchControllerClient 
    
    
    func NewBatchControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*BatchControllerClient, [error](https://pkg.go.dev/builtin#error))

NewBatchControllerClient creates a new batch controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The BatchController provides methods to manage batch workloads.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewBatchControllerRESTClient 
    
    
    func NewBatchControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*BatchControllerClient, [error](https://pkg.go.dev/builtin#error))

NewBatchControllerRESTClient creates a new batch controller rest client.

The BatchController provides methods to manage batch workloads.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewBatchControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_BatchControllerClient_NewBatchControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*BatchControllerClient) CancelOperation 
    
    
    func (c *BatchControllerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
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
    

### func (*BatchControllerClient) Close 
    
    
    func (c *BatchControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*BatchControllerClient) Connection (deprecated)
    
    
    func (c *BatchControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*BatchControllerClient) CreateBatch 
    
    
    func (c *BatchControllerClient) CreateBatch(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateBatchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateBatchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateBatchOperation, [error](https://pkg.go.dev/builtin#error))

CreateBatch creates a batch workload that executes asynchronously.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateBatchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateBatchRequest.
    	}
    	op, err := c.CreateBatch(ctx, req)
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
    

### func (*BatchControllerClient) CreateBatchOperation 
    
    
    func (c *BatchControllerClient) CreateBatchOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateBatchOperation

CreateBatchOperation returns a new CreateBatchOperation from a given name. The name must be that of a previously created CreateBatchOperation, possibly from a different process.

### func (*BatchControllerClient) DeleteBatch 
    
    
    func (c *BatchControllerClient) DeleteBatch(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteBatchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteBatchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteBatch deletes the batch workload resource. If the batch is not in a CANCELLED, SUCCEEDED or FAILED [State][google.cloud.dataproc.v1.Batch.State], the delete operation fails and the response returns FAILED_PRECONDITION.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteBatchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteBatchRequest.
    	}
    	err = c.DeleteBatch(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*BatchControllerClient) DeleteOperation 
    
    
    func (c *BatchControllerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
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
    

### func (*BatchControllerClient) GetBatch 
    
    
    func (c *BatchControllerClient) GetBatch(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetBatchRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetBatchRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Batch), [error](https://pkg.go.dev/builtin#error))

GetBatch gets the batch workload resource representation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetBatchRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetBatchRequest.
    	}
    	resp, err := c.GetBatch(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*BatchControllerClient) GetIamPolicy 
    
    
    func (c *BatchControllerClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*BatchControllerClient) GetOperation 
    
    
    func (c *BatchControllerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
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
    

### func (*BatchControllerClient) ListBatches 
    
    
    func (c *BatchControllerClient) ListBatches(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListBatchesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListBatchesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *BatchIterator

ListBatches lists batch workloads.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListBatchesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListBatchesRequest.
    	}
    	it := c.ListBatches(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListBatchesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListBatchesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListBatchesRequest.
    	}
    	for resp, err := range c.ListBatches(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*BatchControllerClient) ListOperations 
    
    
    func (c *BatchControllerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.NewBatchControllerClient(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
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
    

### func (*BatchControllerClient) SetIamPolicy 
    
    
    func (c *BatchControllerClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*BatchControllerClient) TestIamPermissions 
    
    
    func (c *BatchControllerClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewBatchControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

## BatchIterator
    
    
    type BatchIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.Batch, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

BatchIterator manages a stream of *dataprocpb.Batch.

### func (*BatchIterator) All 
    
    
    func (it *BatchIterator) All() iter.Seq2[*dataprocpb.Batch, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*BatchIterator) Next 
    
    
    func (it *BatchIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Batch), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*BatchIterator) PageInfo 
    
    
    func (it *BatchIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ClusterControllerCallOptions
    
    
    type ClusterControllerCallOptions struct {
    	CreateCluster      []gax.CallOption
    	UpdateCluster      []gax.CallOption
    	StopCluster        []gax.CallOption
    	StartCluster       []gax.CallOption
    	DeleteCluster      []gax.CallOption
    	GetCluster         []gax.CallOption
    	ListClusters       []gax.CallOption
    	DiagnoseCluster    []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

ClusterControllerCallOptions contains the retry settings for each method of ClusterControllerClient.

## ClusterControllerClient
    
    
    type ClusterControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *ClusterControllerCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

ClusterControllerClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The ClusterControllerService provides methods to manage clusters of Compute Engine instances.

### func NewClusterControllerClient 
    
    
    func NewClusterControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ClusterControllerClient, [error](https://pkg.go.dev/builtin#error))

NewClusterControllerClient creates a new cluster controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The ClusterControllerService provides methods to manage clusters of Compute Engine instances.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewClusterControllerRESTClient 
    
    
    func NewClusterControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ClusterControllerClient, [error](https://pkg.go.dev/builtin#error))

NewClusterControllerRESTClient creates a new cluster controller rest client.

The ClusterControllerService provides methods to manage clusters of Compute Engine instances.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewClusterControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_ClusterControllerClient_NewClusterControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ClusterControllerClient) CancelOperation 
    
    
    func (c *ClusterControllerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
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
    

### func (*ClusterControllerClient) Close 
    
    
    func (c *ClusterControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ClusterControllerClient) Connection (deprecated)
    
    
    func (c *ClusterControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ClusterControllerClient) CreateCluster 
    
    
    func (c *ClusterControllerClient) CreateCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateClusterOperation, [error](https://pkg.go.dev/builtin#error))

CreateCluster creates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateClusterRequest.
    	}
    	op, err := c.CreateCluster(ctx, req)
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
    

### func (*ClusterControllerClient) CreateClusterOperation 
    
    
    func (c *ClusterControllerClient) CreateClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateClusterOperation

CreateClusterOperation returns a new CreateClusterOperation from a given name. The name must be that of a previously created CreateClusterOperation, possibly from a different process.

### func (*ClusterControllerClient) DeleteCluster 
    
    
    func (c *ClusterControllerClient) DeleteCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteClusterOperation, [error](https://pkg.go.dev/builtin#error))

DeleteCluster deletes a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteClusterRequest.
    	}
    	op, err := c.DeleteCluster(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*ClusterControllerClient) DeleteClusterOperation 
    
    
    func (c *ClusterControllerClient) DeleteClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteClusterOperation

DeleteClusterOperation returns a new DeleteClusterOperation from a given name. The name must be that of a previously created DeleteClusterOperation, possibly from a different process.

### func (*ClusterControllerClient) DeleteOperation 
    
    
    func (c *ClusterControllerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
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
    

### func (*ClusterControllerClient) DiagnoseCluster 
    
    
    func (c *ClusterControllerClient) DiagnoseCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DiagnoseClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DiagnoseClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DiagnoseClusterOperation, [error](https://pkg.go.dev/builtin#error))

DiagnoseCluster gets cluster diagnostic information. The returned Operation.metadata will be ClusterOperationMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>). After the operation completes, Operation.response contains DiagnoseClusterResults (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#diagnoseclusterresults>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DiagnoseClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DiagnoseClusterRequest.
    	}
    	op, err := c.DiagnoseCluster(ctx, req)
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
    

### func (*ClusterControllerClient) DiagnoseClusterOperation 
    
    
    func (c *ClusterControllerClient) DiagnoseClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *DiagnoseClusterOperation

DiagnoseClusterOperation returns a new DiagnoseClusterOperation from a given name. The name must be that of a previously created DiagnoseClusterOperation, possibly from a different process.

### func (*ClusterControllerClient) GetCluster 
    
    
    func (c *ClusterControllerClient) GetCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

GetCluster gets the resource representation for a cluster in a project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetClusterRequest.
    	}
    	resp, err := c.GetCluster(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ClusterControllerClient) GetIamPolicy 
    
    
    func (c *ClusterControllerClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*ClusterControllerClient) GetOperation 
    
    
    func (c *ClusterControllerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
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
    

### func (*ClusterControllerClient) ListClusters 
    
    
    func (c *ClusterControllerClient) ListClusters(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListClustersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListClustersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ClusterIterator

ListClusters lists all regions/{region}/clusters in a project alphabetically.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListClustersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListClustersRequest.
    	}
    	it := c.ListClusters(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListClustersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListClustersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListClustersRequest.
    	}
    	for resp, err := range c.ListClusters(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ClusterControllerClient) ListOperations 
    
    
    func (c *ClusterControllerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.NewClusterControllerClient(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
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
    

### func (*ClusterControllerClient) SetIamPolicy 
    
    
    func (c *ClusterControllerClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*ClusterControllerClient) StartCluster 
    
    
    func (c *ClusterControllerClient) StartCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[StartClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_StartClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StartClusterOperation, [error](https://pkg.go.dev/builtin#error))

StartCluster starts a cluster in a project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.StartClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#StartClusterRequest.
    	}
    	op, err := c.StartCluster(ctx, req)
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
    

### func (*ClusterControllerClient) StartClusterOperation 
    
    
    func (c *ClusterControllerClient) StartClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *StartClusterOperation

StartClusterOperation returns a new StartClusterOperation from a given name. The name must be that of a previously created StartClusterOperation, possibly from a different process.

### func (*ClusterControllerClient) StopCluster 
    
    
    func (c *ClusterControllerClient) StopCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[StopClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_StopClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StopClusterOperation, [error](https://pkg.go.dev/builtin#error))

StopCluster stops a cluster in a project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.StopClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#StopClusterRequest.
    	}
    	op, err := c.StopCluster(ctx, req)
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
    

### func (*ClusterControllerClient) StopClusterOperation 
    
    
    func (c *ClusterControllerClient) StopClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *StopClusterOperation

StopClusterOperation returns a new StopClusterOperation from a given name. The name must be that of a previously created StopClusterOperation, possibly from a different process.

### func (*ClusterControllerClient) TestIamPermissions 
    
    
    func (c *ClusterControllerClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*ClusterControllerClient) UpdateCluster 
    
    
    func (c *ClusterControllerClient) UpdateCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[UpdateClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_UpdateClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateClusterOperation, [error](https://pkg.go.dev/builtin#error))

UpdateCluster updates a cluster in a project. The returned Operation.metadata will be ClusterOperationMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#clusteroperationmetadata>). The cluster must be in a [RUNNING][google.cloud.dataproc.v1.ClusterStatus.State] state or an error is returned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewClusterControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.UpdateClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#UpdateClusterRequest.
    	}
    	op, err := c.UpdateCluster(ctx, req)
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
    

### func (*ClusterControllerClient) UpdateClusterOperation 
    
    
    func (c *ClusterControllerClient) UpdateClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateClusterOperation

UpdateClusterOperation returns a new UpdateClusterOperation from a given name. The name must be that of a previously created UpdateClusterOperation, possibly from a different process.

## ClusterIterator
    
    
    type ClusterIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.Cluster, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ClusterIterator manages a stream of *dataprocpb.Cluster.

### func (*ClusterIterator) All 
    
    
    func (it *ClusterIterator) All() iter.Seq2[*dataprocpb.Cluster, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ClusterIterator) Next 
    
    
    func (it *ClusterIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ClusterIterator) PageInfo 
    
    
    func (it *ClusterIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CreateBatchOperation
    
    
    type CreateBatchOperation struct {
    	// contains filtered or unexported fields
    }

CreateBatchOperation manages a long-running operation from CreateBatch.

### func (*CreateBatchOperation) Done 
    
    
    func (op *CreateBatchOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateBatchOperation) Metadata 
    
    
    func (op *CreateBatchOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[BatchOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_BatchOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateBatchOperation) Name 
    
    
    func (op *CreateBatchOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateBatchOperation) Poll 
    
    
    func (op *CreateBatchOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Batch), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateBatchOperation) Wait 
    
    
    func (op *CreateBatchOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Batch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Batch), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateClusterOperation
    
    
    type CreateClusterOperation struct {
    	// contains filtered or unexported fields
    }

CreateClusterOperation manages a long-running operation from CreateCluster.

### func (*CreateClusterOperation) Delete 
    
    
    func (op *CreateClusterOperation) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

### func (*CreateClusterOperation) Done 
    
    
    func (op *CreateClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateClusterOperation) Metadata 
    
    
    func (op *CreateClusterOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ClusterOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ClusterOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateClusterOperation) Name 
    
    
    func (op *CreateClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateClusterOperation) Poll 
    
    
    func (op *CreateClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateClusterOperation) Wait 
    
    
    func (op *CreateClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateNodeGroupOperation
    
    
    type CreateNodeGroupOperation struct {
    	// contains filtered or unexported fields
    }

CreateNodeGroupOperation manages a long-running operation from CreateNodeGroup.

### func (*CreateNodeGroupOperation) Done 
    
    
    func (op *CreateNodeGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateNodeGroupOperation) Metadata 
    
    
    func (op *CreateNodeGroupOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroupOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroupOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateNodeGroupOperation) Name 
    
    
    func (op *CreateNodeGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateNodeGroupOperation) Poll 
    
    
    func (op *CreateNodeGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateNodeGroupOperation) Wait 
    
    
    func (op *CreateNodeGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateSessionOperation
    
    
    type CreateSessionOperation struct {
    	// contains filtered or unexported fields
    }

CreateSessionOperation manages a long-running operation from CreateSession.

### func (*CreateSessionOperation) Done 
    
    
    func (op *CreateSessionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateSessionOperation) Metadata 
    
    
    func (op *CreateSessionOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateSessionOperation) Name 
    
    
    func (op *CreateSessionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateSessionOperation) Poll 
    
    
    func (op *CreateSessionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateSessionOperation) Wait 
    
    
    func (op *CreateSessionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteClusterOperation
    
    
    type DeleteClusterOperation struct {
    	// contains filtered or unexported fields
    }

DeleteClusterOperation manages a long-running operation from DeleteCluster.

### func (*DeleteClusterOperation) Delete 
    
    
    func (op *DeleteClusterOperation) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

### func (*DeleteClusterOperation) Done 
    
    
    func (op *DeleteClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteClusterOperation) Metadata 
    
    
    func (op *DeleteClusterOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ClusterOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ClusterOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteClusterOperation) Name 
    
    
    func (op *DeleteClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteClusterOperation) Poll 
    
    
    func (op *DeleteClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteClusterOperation) Wait 
    
    
    func (op *DeleteClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteSessionOperation
    
    
    type DeleteSessionOperation struct {
    	// contains filtered or unexported fields
    }

DeleteSessionOperation manages a long-running operation from DeleteSession.

### func (*DeleteSessionOperation) Done 
    
    
    func (op *DeleteSessionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteSessionOperation) Metadata 
    
    
    func (op *DeleteSessionOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteSessionOperation) Name 
    
    
    func (op *DeleteSessionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteSessionOperation) Poll 
    
    
    func (op *DeleteSessionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteSessionOperation) Wait 
    
    
    func (op *DeleteSessionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DiagnoseClusterOperation
    
    
    type DiagnoseClusterOperation struct {
    	// contains filtered or unexported fields
    }

DiagnoseClusterOperation manages a long-running operation from DiagnoseCluster.

### func (*DiagnoseClusterOperation) Delete 
    
    
    func (op *DiagnoseClusterOperation) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

### func (*DiagnoseClusterOperation) Done 
    
    
    func (op *DiagnoseClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DiagnoseClusterOperation) Metadata 
    
    
    func (op *DiagnoseClusterOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ClusterOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ClusterOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DiagnoseClusterOperation) Name 
    
    
    func (op *DiagnoseClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DiagnoseClusterOperation) Poll 
    
    
    func (op *DiagnoseClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DiagnoseClusterResults](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DiagnoseClusterResults), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DiagnoseClusterOperation) Wait 
    
    
    func (op *DiagnoseClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DiagnoseClusterResults](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DiagnoseClusterResults), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## InstantiateInlineWorkflowTemplateOperation
    
    
    type InstantiateInlineWorkflowTemplateOperation struct {
    	// contains filtered or unexported fields
    }

InstantiateInlineWorkflowTemplateOperation manages a long-running operation from InstantiateInlineWorkflowTemplate.

### func (*InstantiateInlineWorkflowTemplateOperation) Cancel 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Cancel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Cancel starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use Poll or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, op.Poll returns an error with code Canceled.

### func (*InstantiateInlineWorkflowTemplateOperation) Delete 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

### func (*InstantiateInlineWorkflowTemplateOperation) Done 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*InstantiateInlineWorkflowTemplateOperation) Metadata 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[WorkflowMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_WorkflowMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*InstantiateInlineWorkflowTemplateOperation) Name 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*InstantiateInlineWorkflowTemplateOperation) Poll 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*InstantiateInlineWorkflowTemplateOperation) Wait 
    
    
    func (op *InstantiateInlineWorkflowTemplateOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## InstantiateWorkflowTemplateOperation
    
    
    type InstantiateWorkflowTemplateOperation struct {
    	// contains filtered or unexported fields
    }

InstantiateWorkflowTemplateOperation manages a long-running operation from InstantiateWorkflowTemplate.

### func (*InstantiateWorkflowTemplateOperation) Cancel 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Cancel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Cancel starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use Poll or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, op.Poll returns an error with code Canceled.

### func (*InstantiateWorkflowTemplateOperation) Delete 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

### func (*InstantiateWorkflowTemplateOperation) Done 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*InstantiateWorkflowTemplateOperation) Metadata 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[WorkflowMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_WorkflowMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*InstantiateWorkflowTemplateOperation) Name 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*InstantiateWorkflowTemplateOperation) Poll 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*InstantiateWorkflowTemplateOperation) Wait 
    
    
    func (op *InstantiateWorkflowTemplateOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## JobControllerCallOptions
    
    
    type JobControllerCallOptions struct {
    	SubmitJob            []gax.CallOption
    	SubmitJobAsOperation []gax.CallOption
    	GetJob               []gax.CallOption
    	ListJobs             []gax.CallOption
    	UpdateJob            []gax.CallOption
    	CancelJob            []gax.CallOption
    	DeleteJob            []gax.CallOption
    	GetIamPolicy         []gax.CallOption
    	SetIamPolicy         []gax.CallOption
    	TestIamPermissions   []gax.CallOption
    	CancelOperation      []gax.CallOption
    	DeleteOperation      []gax.CallOption
    	GetOperation         []gax.CallOption
    	ListOperations       []gax.CallOption
    }

JobControllerCallOptions contains the retry settings for each method of JobControllerClient.

## JobControllerClient
    
    
    type JobControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *JobControllerCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

JobControllerClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The JobController provides methods to manage jobs.

### func NewJobControllerClient 
    
    
    func NewJobControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*JobControllerClient, [error](https://pkg.go.dev/builtin#error))

NewJobControllerClient creates a new job controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The JobController provides methods to manage jobs.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewJobControllerRESTClient 
    
    
    func NewJobControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*JobControllerClient, [error](https://pkg.go.dev/builtin#error))

NewJobControllerRESTClient creates a new job controller rest client.

The JobController provides methods to manage jobs.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewJobControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_JobControllerClient_NewJobControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*JobControllerClient) CancelJob 
    
    
    func (c *JobControllerClient) CancelJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CancelJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CancelJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

CancelJob starts a job cancellation request. To access the job resource after cancellation, call regions/{region}/jobs.list (at <https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/list>) or regions/{region}/jobs.get (at <https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/get>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CancelJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CancelJobRequest.
    	}
    	resp, err := c.CancelJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*JobControllerClient) CancelOperation 
    
    
    func (c *JobControllerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
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
    

### func (*JobControllerClient) Close 
    
    
    func (c *JobControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*JobControllerClient) Connection (deprecated)
    
    
    func (c *JobControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*JobControllerClient) DeleteJob 
    
    
    func (c *JobControllerClient) DeleteJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteJob deletes the job from the project. If the job is active, the delete fails, and the response returns FAILED_PRECONDITION.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteJobRequest.
    	}
    	err = c.DeleteJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*JobControllerClient) DeleteOperation 
    
    
    func (c *JobControllerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
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
    

### func (*JobControllerClient) GetIamPolicy 
    
    
    func (c *JobControllerClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*JobControllerClient) GetJob 
    
    
    func (c *JobControllerClient) GetJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

GetJob gets the resource representation for a job in a project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetJobRequest.
    	}
    	resp, err := c.GetJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*JobControllerClient) GetOperation 
    
    
    func (c *JobControllerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
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
    

### func (*JobControllerClient) ListJobs 
    
    
    func (c *JobControllerClient) ListJobs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListJobsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListJobsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *JobIterator

ListJobs lists regions/{region}/jobs in a project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListJobsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListJobsRequest.
    	}
    	it := c.ListJobs(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListJobsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListJobsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListJobsRequest.
    	}
    	for resp, err := range c.ListJobs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*JobControllerClient) ListOperations 
    
    
    func (c *JobControllerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.NewJobControllerClient(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
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
    

### func (*JobControllerClient) SetIamPolicy 
    
    
    func (c *JobControllerClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*JobControllerClient) SubmitJob 
    
    
    func (c *JobControllerClient) SubmitJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SubmitJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SubmitJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

SubmitJob submits a job to a cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.SubmitJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#SubmitJobRequest.
    	}
    	resp, err := c.SubmitJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*JobControllerClient) SubmitJobAsOperation 
    
    
    func (c *JobControllerClient) SubmitJobAsOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SubmitJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SubmitJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*SubmitJobAsOperationOperation, [error](https://pkg.go.dev/builtin#error))

SubmitJobAsOperation submits job to a cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.SubmitJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#SubmitJobRequest.
    	}
    	op, err := c.SubmitJobAsOperation(ctx, req)
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
    

### func (*JobControllerClient) SubmitJobAsOperationOperation 
    
    
    func (c *JobControllerClient) SubmitJobAsOperationOperation(name [string](https://pkg.go.dev/builtin#string)) *SubmitJobAsOperationOperation

SubmitJobAsOperationOperation returns a new SubmitJobAsOperationOperation from a given name. The name must be that of a previously created SubmitJobAsOperationOperation, possibly from a different process.

### func (*JobControllerClient) TestIamPermissions 
    
    
    func (c *JobControllerClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*JobControllerClient) UpdateJob 
    
    
    func (c *JobControllerClient) UpdateJob(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[UpdateJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_UpdateJobRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

UpdateJob updates a job in a project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewJobControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.UpdateJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#UpdateJobRequest.
    	}
    	resp, err := c.UpdateJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## JobIterator
    
    
    type JobIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.Job, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

JobIterator manages a stream of *dataprocpb.Job.

### func (*JobIterator) All 
    
    
    func (it *JobIterator) All() iter.Seq2[*dataprocpb.Job, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*JobIterator) Next 
    
    
    func (it *JobIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*JobIterator) PageInfo 
    
    
    func (it *JobIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## NodeGroupControllerCallOptions
    
    
    type NodeGroupControllerCallOptions struct {
    	CreateNodeGroup    []gax.CallOption
    	ResizeNodeGroup    []gax.CallOption
    	GetNodeGroup       []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

NodeGroupControllerCallOptions contains the retry settings for each method of NodeGroupControllerClient.

## NodeGroupControllerClient
    
    
    type NodeGroupControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *NodeGroupControllerCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

NodeGroupControllerClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The NodeGroupControllerService provides methods to manage node groups of Compute Engine managed instances.

### func NewNodeGroupControllerClient 
    
    
    func NewNodeGroupControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*NodeGroupControllerClient, [error](https://pkg.go.dev/builtin#error))

NewNodeGroupControllerClient creates a new node group controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The NodeGroupControllerService provides methods to manage node groups of Compute Engine managed instances.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewNodeGroupControllerRESTClient 
    
    
    func NewNodeGroupControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*NodeGroupControllerClient, [error](https://pkg.go.dev/builtin#error))

NewNodeGroupControllerRESTClient creates a new node group controller rest client.

The NodeGroupControllerService provides methods to manage node groups of Compute Engine managed instances.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewNodeGroupControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_NodeGroupControllerClient_NewNodeGroupControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*NodeGroupControllerClient) CancelOperation 
    
    
    func (c *NodeGroupControllerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
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
    

### func (*NodeGroupControllerClient) Close 
    
    
    func (c *NodeGroupControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*NodeGroupControllerClient) Connection (deprecated)
    
    
    func (c *NodeGroupControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*NodeGroupControllerClient) CreateNodeGroup 
    
    
    func (c *NodeGroupControllerClient) CreateNodeGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateNodeGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateNodeGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateNodeGroupOperation, [error](https://pkg.go.dev/builtin#error))

CreateNodeGroup creates a node group in a cluster. The returned Operation.metadata is NodeGroupOperationMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#nodegroupoperationmetadata>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateNodeGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateNodeGroupRequest.
    	}
    	op, err := c.CreateNodeGroup(ctx, req)
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
    

### func (*NodeGroupControllerClient) CreateNodeGroupOperation 
    
    
    func (c *NodeGroupControllerClient) CreateNodeGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateNodeGroupOperation

CreateNodeGroupOperation returns a new CreateNodeGroupOperation from a given name. The name must be that of a previously created CreateNodeGroupOperation, possibly from a different process.

### func (*NodeGroupControllerClient) DeleteOperation 
    
    
    func (c *NodeGroupControllerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
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
    

### func (*NodeGroupControllerClient) GetIamPolicy 
    
    
    func (c *NodeGroupControllerClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*NodeGroupControllerClient) GetNodeGroup 
    
    
    func (c *NodeGroupControllerClient) GetNodeGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetNodeGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetNodeGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroup), [error](https://pkg.go.dev/builtin#error))

GetNodeGroup gets the resource representation for a node group in a cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetNodeGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetNodeGroupRequest.
    	}
    	resp, err := c.GetNodeGroup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*NodeGroupControllerClient) GetOperation 
    
    
    func (c *NodeGroupControllerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
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
    

### func (*NodeGroupControllerClient) ListOperations 
    
    
    func (c *NodeGroupControllerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
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
    

### func (*NodeGroupControllerClient) ResizeNodeGroup 
    
    
    func (c *NodeGroupControllerClient) ResizeNodeGroup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ResizeNodeGroupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ResizeNodeGroupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ResizeNodeGroupOperation, [error](https://pkg.go.dev/builtin#error))

ResizeNodeGroup resizes a node group in a cluster. The returned Operation.metadata is NodeGroupOperationMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#nodegroupoperationmetadata>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ResizeNodeGroupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ResizeNodeGroupRequest.
    	}
    	op, err := c.ResizeNodeGroup(ctx, req)
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
    

### func (*NodeGroupControllerClient) ResizeNodeGroupOperation 
    
    
    func (c *NodeGroupControllerClient) ResizeNodeGroupOperation(name [string](https://pkg.go.dev/builtin#string)) *ResizeNodeGroupOperation

ResizeNodeGroupOperation returns a new ResizeNodeGroupOperation from a given name. The name must be that of a previously created ResizeNodeGroupOperation, possibly from a different process.

### func (*NodeGroupControllerClient) SetIamPolicy 
    
    
    func (c *NodeGroupControllerClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*NodeGroupControllerClient) TestIamPermissions 
    
    
    func (c *NodeGroupControllerClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewNodeGroupControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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

## ResizeNodeGroupOperation
    
    
    type ResizeNodeGroupOperation struct {
    	// contains filtered or unexported fields
    }

ResizeNodeGroupOperation manages a long-running operation from ResizeNodeGroup.

### func (*ResizeNodeGroupOperation) Done 
    
    
    func (op *ResizeNodeGroupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ResizeNodeGroupOperation) Metadata 
    
    
    func (op *ResizeNodeGroupOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroupOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroupOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ResizeNodeGroupOperation) Name 
    
    
    func (op *ResizeNodeGroupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ResizeNodeGroupOperation) Poll 
    
    
    func (op *ResizeNodeGroupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ResizeNodeGroupOperation) Wait 
    
    
    func (op *ResizeNodeGroupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[NodeGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_NodeGroup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SessionControllerCallOptions
    
    
    type SessionControllerCallOptions struct {
    	CreateSession      []gax.CallOption
    	GetSession         []gax.CallOption
    	ListSessions       []gax.CallOption
    	TerminateSession   []gax.CallOption
    	DeleteSession      []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

SessionControllerCallOptions contains the retry settings for each method of SessionControllerClient.

## SessionControllerClient
    
    
    type SessionControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *SessionControllerCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

SessionControllerClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The SessionController provides methods to manage interactive sessions.

### func NewSessionControllerClient 
    
    
    func NewSessionControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionControllerClient, [error](https://pkg.go.dev/builtin#error))

NewSessionControllerClient creates a new session controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The SessionController provides methods to manage interactive sessions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSessionControllerRESTClient 
    
    
    func NewSessionControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionControllerClient, [error](https://pkg.go.dev/builtin#error))

NewSessionControllerRESTClient creates a new session controller rest client.

The SessionController provides methods to manage interactive sessions.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewSessionControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_SessionControllerClient_NewSessionControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SessionControllerClient) CancelOperation 
    
    
    func (c *SessionControllerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
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
    

### func (*SessionControllerClient) Close 
    
    
    func (c *SessionControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SessionControllerClient) Connection (deprecated)
    
    
    func (c *SessionControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SessionControllerClient) CreateSession 
    
    
    func (c *SessionControllerClient) CreateSession(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateSessionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateSessionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateSessionOperation, [error](https://pkg.go.dev/builtin#error))

CreateSession create an interactive session asynchronously.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateSessionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateSessionRequest.
    	}
    	op, err := c.CreateSession(ctx, req)
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
    

### func (*SessionControllerClient) CreateSessionOperation 
    
    
    func (c *SessionControllerClient) CreateSessionOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateSessionOperation

CreateSessionOperation returns a new CreateSessionOperation from a given name. The name must be that of a previously created CreateSessionOperation, possibly from a different process.

### func (*SessionControllerClient) DeleteOperation 
    
    
    func (c *SessionControllerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
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
    

### func (*SessionControllerClient) DeleteSession 
    
    
    func (c *SessionControllerClient) DeleteSession(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteSessionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteSessionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteSessionOperation, [error](https://pkg.go.dev/builtin#error))

DeleteSession deletes the interactive session resource. If the session is not in terminal state, it is terminated, and then deleted.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteSessionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteSessionRequest.
    	}
    	op, err := c.DeleteSession(ctx, req)
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
    

### func (*SessionControllerClient) DeleteSessionOperation 
    
    
    func (c *SessionControllerClient) DeleteSessionOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteSessionOperation

DeleteSessionOperation returns a new DeleteSessionOperation from a given name. The name must be that of a previously created DeleteSessionOperation, possibly from a different process.

### func (*SessionControllerClient) GetIamPolicy 
    
    
    func (c *SessionControllerClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*SessionControllerClient) GetOperation 
    
    
    func (c *SessionControllerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
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
    

### func (*SessionControllerClient) GetSession 
    
    
    func (c *SessionControllerClient) GetSession(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetSessionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetSessionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

GetSession gets the resource representation for an interactive session.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetSessionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetSessionRequest.
    	}
    	resp, err := c.GetSession(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionControllerClient) ListOperations 
    
    
    func (c *SessionControllerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.NewSessionControllerClient(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
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
    

### func (*SessionControllerClient) ListSessions 
    
    
    func (c *SessionControllerClient) ListSessions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListSessionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListSessionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SessionIterator

ListSessions lists interactive sessions.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListSessionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListSessionsRequest.
    	}
    	it := c.ListSessions(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListSessionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListSessionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListSessionsRequest.
    	}
    	for resp, err := range c.ListSessions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionControllerClient) SetIamPolicy 
    
    
    func (c *SessionControllerClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*SessionControllerClient) TerminateSession 
    
    
    func (c *SessionControllerClient) TerminateSession(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[TerminateSessionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_TerminateSessionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*TerminateSessionOperation, [error](https://pkg.go.dev/builtin#error))

TerminateSession terminates the interactive session.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.TerminateSessionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#TerminateSessionRequest.
    	}
    	op, err := c.TerminateSession(ctx, req)
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
    

### func (*SessionControllerClient) TerminateSessionOperation 
    
    
    func (c *SessionControllerClient) TerminateSessionOperation(name [string](https://pkg.go.dev/builtin#string)) *TerminateSessionOperation

TerminateSessionOperation returns a new TerminateSessionOperation from a given name. The name must be that of a previously created TerminateSessionOperation, possibly from a different process.

### func (*SessionControllerClient) TestIamPermissions 
    
    
    func (c *SessionControllerClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

## SessionIterator
    
    
    type SessionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.Session, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SessionIterator manages a stream of *dataprocpb.Session.

### func (*SessionIterator) All 
    
    
    func (it *SessionIterator) All() iter.Seq2[*dataprocpb.Session, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SessionIterator) Next 
    
    
    func (it *SessionIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SessionIterator) PageInfo 
    
    
    func (it *SessionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SessionTemplateControllerCallOptions
    
    
    type SessionTemplateControllerCallOptions struct {
    	CreateSessionTemplate []gax.CallOption
    	UpdateSessionTemplate []gax.CallOption
    	GetSessionTemplate    []gax.CallOption
    	ListSessionTemplates  []gax.CallOption
    	DeleteSessionTemplate []gax.CallOption
    	GetIamPolicy          []gax.CallOption
    	SetIamPolicy          []gax.CallOption
    	TestIamPermissions    []gax.CallOption
    	CancelOperation       []gax.CallOption
    	DeleteOperation       []gax.CallOption
    	GetOperation          []gax.CallOption
    	ListOperations        []gax.CallOption
    }

SessionTemplateControllerCallOptions contains the retry settings for each method of SessionTemplateControllerClient.

## SessionTemplateControllerClient
    
    
    type SessionTemplateControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *SessionTemplateControllerCallOptions
    	// contains filtered or unexported fields
    }

SessionTemplateControllerClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The SessionTemplateController provides methods to manage session templates.

### func NewSessionTemplateControllerClient 
    
    
    func NewSessionTemplateControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionTemplateControllerClient, [error](https://pkg.go.dev/builtin#error))

NewSessionTemplateControllerClient creates a new session template controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The SessionTemplateController provides methods to manage session templates.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewSessionTemplateControllerRESTClient 
    
    
    func NewSessionTemplateControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*SessionTemplateControllerClient, [error](https://pkg.go.dev/builtin#error))

NewSessionTemplateControllerRESTClient creates a new session template controller rest client.

The SessionTemplateController provides methods to manage session templates.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewSessionTemplateControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_SessionTemplateControllerClient_NewSessionTemplateControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*SessionTemplateControllerClient) CancelOperation 
    
    
    func (c *SessionTemplateControllerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
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
    

### func (*SessionTemplateControllerClient) Close 
    
    
    func (c *SessionTemplateControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*SessionTemplateControllerClient) Connection (deprecated)
    
    
    func (c *SessionTemplateControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*SessionTemplateControllerClient) CreateSessionTemplate 
    
    
    func (c *SessionTemplateControllerClient) CreateSessionTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateSessionTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateSessionTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionTemplate), [error](https://pkg.go.dev/builtin#error))

CreateSessionTemplate create a session template synchronously.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateSessionTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateSessionTemplateRequest.
    	}
    	resp, err := c.CreateSessionTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionTemplateControllerClient) DeleteOperation 
    
    
    func (c *SessionTemplateControllerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
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
    

### func (*SessionTemplateControllerClient) DeleteSessionTemplate 
    
    
    func (c *SessionTemplateControllerClient) DeleteSessionTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteSessionTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteSessionTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteSessionTemplate deletes a session template.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteSessionTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteSessionTemplateRequest.
    	}
    	err = c.DeleteSessionTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*SessionTemplateControllerClient) GetIamPolicy 
    
    
    func (c *SessionTemplateControllerClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*SessionTemplateControllerClient) GetOperation 
    
    
    func (c *SessionTemplateControllerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
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
    

### func (*SessionTemplateControllerClient) GetSessionTemplate 
    
    
    func (c *SessionTemplateControllerClient) GetSessionTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetSessionTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetSessionTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionTemplate), [error](https://pkg.go.dev/builtin#error))

GetSessionTemplate gets the resource representation for a session template.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetSessionTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetSessionTemplateRequest.
    	}
    	resp, err := c.GetSessionTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*SessionTemplateControllerClient) ListOperations 
    
    
    func (c *SessionTemplateControllerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
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
    

### func (*SessionTemplateControllerClient) ListSessionTemplates 
    
    
    func (c *SessionTemplateControllerClient) ListSessionTemplates(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListSessionTemplatesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListSessionTemplatesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SessionTemplateIterator

ListSessionTemplates lists session templates.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListSessionTemplatesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListSessionTemplatesRequest.
    	}
    	it := c.ListSessionTemplates(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListSessionTemplatesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListSessionTemplatesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListSessionTemplatesRequest.
    	}
    	for resp, err := range c.ListSessionTemplates(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*SessionTemplateControllerClient) SetIamPolicy 
    
    
    func (c *SessionTemplateControllerClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*SessionTemplateControllerClient) TestIamPermissions 
    
    
    func (c *SessionTemplateControllerClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*SessionTemplateControllerClient) UpdateSessionTemplate 
    
    
    func (c *SessionTemplateControllerClient) UpdateSessionTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[UpdateSessionTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_UpdateSessionTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionTemplate), [error](https://pkg.go.dev/builtin#error))

UpdateSessionTemplate updates the session template synchronously.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.NewSessionTemplateControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.UpdateSessionTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#UpdateSessionTemplateRequest.
    	}
    	resp, err := c.UpdateSessionTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## SessionTemplateIterator
    
    
    type SessionTemplateIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.SessionTemplate, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SessionTemplateIterator manages a stream of *dataprocpb.SessionTemplate.

### func (*SessionTemplateIterator) All 
    
    
    func (it *SessionTemplateIterator) All() iter.Seq2[*dataprocpb.SessionTemplate, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SessionTemplateIterator) Next 
    
    
    func (it *SessionTemplateIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionTemplate), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SessionTemplateIterator) PageInfo 
    
    
    func (it *SessionTemplateIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## StartClusterOperation
    
    
    type StartClusterOperation struct {
    	// contains filtered or unexported fields
    }

StartClusterOperation manages a long-running operation from StartCluster.

### func (*StartClusterOperation) Done 
    
    
    func (op *StartClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StartClusterOperation) Metadata 
    
    
    func (op *StartClusterOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ClusterOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ClusterOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StartClusterOperation) Name 
    
    
    func (op *StartClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StartClusterOperation) Poll 
    
    
    func (op *StartClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StartClusterOperation) Wait 
    
    
    func (op *StartClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StopClusterOperation
    
    
    type StopClusterOperation struct {
    	// contains filtered or unexported fields
    }

StopClusterOperation manages a long-running operation from StopCluster.

### func (*StopClusterOperation) Done 
    
    
    func (op *StopClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StopClusterOperation) Metadata 
    
    
    func (op *StopClusterOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ClusterOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ClusterOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StopClusterOperation) Name 
    
    
    func (op *StopClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StopClusterOperation) Poll 
    
    
    func (op *StopClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StopClusterOperation) Wait 
    
    
    func (op *StopClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SubmitJobAsOperationOperation
    
    
    type SubmitJobAsOperationOperation struct {
    	// contains filtered or unexported fields
    }

SubmitJobAsOperationOperation manages a long-running operation from SubmitJobAsOperation.

### func (*SubmitJobAsOperationOperation) Done 
    
    
    func (op *SubmitJobAsOperationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*SubmitJobAsOperationOperation) Metadata 
    
    
    func (op *SubmitJobAsOperationOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[JobMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_JobMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*SubmitJobAsOperationOperation) Name 
    
    
    func (op *SubmitJobAsOperationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*SubmitJobAsOperationOperation) Poll 
    
    
    func (op *SubmitJobAsOperationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*SubmitJobAsOperationOperation) Wait 
    
    
    func (op *SubmitJobAsOperationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Job), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## TerminateSessionOperation
    
    
    type TerminateSessionOperation struct {
    	// contains filtered or unexported fields
    }

TerminateSessionOperation manages a long-running operation from TerminateSession.

### func (*TerminateSessionOperation) Done 
    
    
    func (op *TerminateSessionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*TerminateSessionOperation) Metadata 
    
    
    func (op *TerminateSessionOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[SessionOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_SessionOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*TerminateSessionOperation) Name 
    
    
    func (op *TerminateSessionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*TerminateSessionOperation) Poll 
    
    
    func (op *TerminateSessionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*TerminateSessionOperation) Wait 
    
    
    func (op *TerminateSessionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Session](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Session), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateClusterOperation
    
    
    type UpdateClusterOperation struct {
    	// contains filtered or unexported fields
    }

UpdateClusterOperation manages a long-running operation from UpdateCluster.

### func (*UpdateClusterOperation) Delete 
    
    
    func (op *UpdateClusterOperation) Delete(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

### func (*UpdateClusterOperation) Done 
    
    
    func (op *UpdateClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateClusterOperation) Metadata 
    
    
    func (op *UpdateClusterOperation) Metadata() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ClusterOperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ClusterOperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateClusterOperation) Name 
    
    
    func (op *UpdateClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateClusterOperation) Poll 
    
    
    func (op *UpdateClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateClusterOperation) Wait 
    
    
    func (op *UpdateClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[Cluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_Cluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## WorkflowTemplateCallOptions
    
    
    type WorkflowTemplateCallOptions struct {
    	CreateWorkflowTemplate            []gax.CallOption
    	GetWorkflowTemplate               []gax.CallOption
    	InstantiateWorkflowTemplate       []gax.CallOption
    	InstantiateInlineWorkflowTemplate []gax.CallOption
    	UpdateWorkflowTemplate            []gax.CallOption
    	ListWorkflowTemplates             []gax.CallOption
    	DeleteWorkflowTemplate            []gax.CallOption
    	GetIamPolicy                      []gax.CallOption
    	SetIamPolicy                      []gax.CallOption
    	TestIamPermissions                []gax.CallOption
    	CancelOperation                   []gax.CallOption
    	DeleteOperation                   []gax.CallOption
    	GetOperation                      []gax.CallOption
    	ListOperations                    []gax.CallOption
    }

WorkflowTemplateCallOptions contains the retry settings for each method of WorkflowTemplateClient.

## WorkflowTemplateClient
    
    
    type WorkflowTemplateClient struct {
    
    	// The call options for this service.
    	CallOptions *WorkflowTemplateCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

WorkflowTemplateClient is a client for interacting with Cloud Dataproc API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The API interface for managing Workflow Templates in the Dataproc API.

### func NewWorkflowTemplateClient 
    
    
    func NewWorkflowTemplateClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*WorkflowTemplateClient, [error](https://pkg.go.dev/builtin#error))

NewWorkflowTemplateClient creates a new workflow template service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

The API interface for managing Workflow Templates in the Dataproc API.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewWorkflowTemplateRESTClient 
    
    
    func NewWorkflowTemplateRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*WorkflowTemplateClient, [error](https://pkg.go.dev/builtin#error))

NewWorkflowTemplateRESTClient creates a new workflow template service rest client.

The API interface for managing Workflow Templates in the Dataproc API.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*WorkflowTemplateClient) CancelOperation 
    
    
    func (c *WorkflowTemplateClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
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
    

### func (*WorkflowTemplateClient) Close 
    
    
    func (c *WorkflowTemplateClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*WorkflowTemplateClient) Connection (deprecated)
    
    
    func (c *WorkflowTemplateClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*WorkflowTemplateClient) CreateWorkflowTemplate 
    
    
    func (c *WorkflowTemplateClient) CreateWorkflowTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[CreateWorkflowTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_CreateWorkflowTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[WorkflowTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_WorkflowTemplate), [error](https://pkg.go.dev/builtin#error))

CreateWorkflowTemplate creates new workflow template.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.CreateWorkflowTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#CreateWorkflowTemplateRequest.
    	}
    	resp, err := c.CreateWorkflowTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*WorkflowTemplateClient) DeleteOperation 
    
    
    func (c *WorkflowTemplateClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
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
    

### func (*WorkflowTemplateClient) DeleteWorkflowTemplate 
    
    
    func (c *WorkflowTemplateClient) DeleteWorkflowTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[DeleteWorkflowTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_DeleteWorkflowTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteWorkflowTemplate deletes a workflow template. It does not cancel in-progress workflows.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.DeleteWorkflowTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#DeleteWorkflowTemplateRequest.
    	}
    	err = c.DeleteWorkflowTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*WorkflowTemplateClient) GetIamPolicy 
    
    
    func (c *WorkflowTemplateClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*WorkflowTemplateClient) GetOperation 
    
    
    func (c *WorkflowTemplateClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
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
    

### func (*WorkflowTemplateClient) GetWorkflowTemplate 
    
    
    func (c *WorkflowTemplateClient) GetWorkflowTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[GetWorkflowTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_GetWorkflowTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[WorkflowTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_WorkflowTemplate), [error](https://pkg.go.dev/builtin#error))

GetWorkflowTemplate retrieves the latest workflow template.

Can retrieve previously instantiated template by specifying optional version parameter.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.GetWorkflowTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#GetWorkflowTemplateRequest.
    	}
    	resp, err := c.GetWorkflowTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*WorkflowTemplateClient) InstantiateInlineWorkflowTemplate 
    
    
    func (c *WorkflowTemplateClient) InstantiateInlineWorkflowTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[InstantiateInlineWorkflowTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_InstantiateInlineWorkflowTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*InstantiateInlineWorkflowTemplateOperation, [error](https://pkg.go.dev/builtin#error))

InstantiateInlineWorkflowTemplate instantiates a template and begins execution.

This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be WorkflowMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata>). Also see Using WorkflowMetadata (at <https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata>).

On successful completion, Operation.response will be Empty.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.InstantiateInlineWorkflowTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#InstantiateInlineWorkflowTemplateRequest.
    	}
    	op, err := c.InstantiateInlineWorkflowTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*WorkflowTemplateClient) InstantiateInlineWorkflowTemplateOperation 
    
    
    func (c *WorkflowTemplateClient) InstantiateInlineWorkflowTemplateOperation(name [string](https://pkg.go.dev/builtin#string)) *InstantiateInlineWorkflowTemplateOperation

InstantiateInlineWorkflowTemplateOperation returns a new InstantiateInlineWorkflowTemplateOperation from a given name. The name must be that of a previously created InstantiateInlineWorkflowTemplateOperation, possibly from a different process.

### func (*WorkflowTemplateClient) InstantiateWorkflowTemplate 
    
    
    func (c *WorkflowTemplateClient) InstantiateWorkflowTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[InstantiateWorkflowTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_InstantiateWorkflowTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*InstantiateWorkflowTemplateOperation, [error](https://pkg.go.dev/builtin#error))

InstantiateWorkflowTemplate instantiates a template and begins execution.

The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.

The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.

The Operation.metadata will be WorkflowMetadata (at <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata>). Also see Using WorkflowMetadata (at <https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata>).

On successful completion, Operation.response will be Empty.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.InstantiateWorkflowTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#InstantiateWorkflowTemplateRequest.
    	}
    	op, err := c.InstantiateWorkflowTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*WorkflowTemplateClient) InstantiateWorkflowTemplateOperation 
    
    
    func (c *WorkflowTemplateClient) InstantiateWorkflowTemplateOperation(name [string](https://pkg.go.dev/builtin#string)) *InstantiateWorkflowTemplateOperation

InstantiateWorkflowTemplateOperation returns a new InstantiateWorkflowTemplateOperation from a given name. The name must be that of a previously created InstantiateWorkflowTemplateOperation, possibly from a different process.

### func (*WorkflowTemplateClient) ListOperations 
    
    
    func (c *WorkflowTemplateClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
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
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
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
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
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
    

### func (*WorkflowTemplateClient) ListWorkflowTemplates 
    
    
    func (c *WorkflowTemplateClient) ListWorkflowTemplates(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[ListWorkflowTemplatesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_ListWorkflowTemplatesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *WorkflowTemplateIterator

ListWorkflowTemplates lists workflows that match the specified filter in the request.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListWorkflowTemplatesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListWorkflowTemplatesRequest.
    	}
    	it := c.ListWorkflowTemplates(ctx, req)
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
    		_ = it.Response.(*dataprocpb.ListWorkflowTemplatesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.ListWorkflowTemplatesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#ListWorkflowTemplatesRequest.
    	}
    	for resp, err := range c.ListWorkflowTemplates(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*WorkflowTemplateClient) SetIamPolicy 
    
    
    func (c *WorkflowTemplateClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*WorkflowTemplateClient) TestIamPermissions 
    
    
    func (c *WorkflowTemplateClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
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
    

### func (*WorkflowTemplateClient) UpdateWorkflowTemplate 
    
    
    func (c *WorkflowTemplateClient) UpdateWorkflowTemplate(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[UpdateWorkflowTemplateRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_UpdateWorkflowTemplateRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[WorkflowTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_WorkflowTemplate), [error](https://pkg.go.dev/builtin#error))

UpdateWorkflowTemplate updates (replaces) workflow template. The updated template must contain version that matches the current server version.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataproc "cloud.google.com/go/dataproc/v2/apiv1"
    	dataprocpb "cloud.google.com/go/dataproc/v2/apiv1/dataprocpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataproc.[NewWorkflowTemplateClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1.html#cloud_google_com_go_dataproc_v2_apiv1_WorkflowTemplateClient_NewWorkflowTemplateClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataprocpb.UpdateWorkflowTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataproc/v2/apiv1/dataprocpb#UpdateWorkflowTemplateRequest.
    	}
    	resp, err := c.UpdateWorkflowTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## WorkflowTemplateIterator
    
    
    type WorkflowTemplateIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataprocpb.WorkflowTemplate, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

WorkflowTemplateIterator manages a stream of *dataprocpb.WorkflowTemplate.

### func (*WorkflowTemplateIterator) All 
    
    
    func (it *WorkflowTemplateIterator) All() iter.Seq2[*dataprocpb.WorkflowTemplate, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*WorkflowTemplateIterator) Next 
    
    
    func (it *WorkflowTemplateIterator) Next() (*[dataprocpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb).[WorkflowTemplate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataproc/v2/latest/apiv1/dataprocpb#cloud_google_com_go_dataproc_v2_apiv1_dataprocpb_WorkflowTemplate), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*WorkflowTemplateIterator) PageInfo 
    
    
    func (it *WorkflowTemplateIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
