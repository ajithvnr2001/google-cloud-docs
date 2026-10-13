---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/
title: Cloud Monitoring API v1 - Package cloud.google.com/go/monitoring/metricsscope/apiv1 (v1.31.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:57.799062+00:00
---

# Cloud Monitoring API v1 - Package cloud.google.com/go/monitoring/metricsscope/apiv1 (v1.31.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Monitoring API v1 - Package cloud.google.com/go/monitoring/metricsscope/apiv1 (v1.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.31.0 (latest)  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.3  1.23.0  1.22.1  1.21.2  1.20.4  1.19.0  1.18.2  1.17.1  1.16.3  1.15.1  1.14.0  1.13.1  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.3.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/monitoring/metricsscope/apiv1). 

Package metricsscope is an auto-generated package for the Cloud Monitoring API. 

Manages your Cloud Monitoring data and configurations. Most projects must be associated with a Workspace, with a few exceptions as noted on the individual method pages. The table entries below are presented in alphabetical order, not in order of common use. For explanations of the concepts found in the table entries, read the Cloud Monitoring documentation (at <https://cloud.google.com/monitoring/docs>). 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/monitoring/metricsscope/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := metricsscope.NewMetricsScopesClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &metricsscopepb.CreateMonitoredProjectRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb#CreateMonitoredProjectRequest.
    }
    op, err := c.CreateMonitoredProject(ctx, req)
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

The ctx passed to NewMetricsScopesClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## CreateMonitoredProjectOperation
    
    
    type CreateMonitoredProjectOperation struct {
    	// contains filtered or unexported fields
    }

CreateMonitoredProjectOperation manages a long-running operation from CreateMonitoredProject.

### func (*CreateMonitoredProjectOperation) Done 
    
    
    func (op *CreateMonitoredProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateMonitoredProjectOperation) Metadata 
    
    
    func (op *CreateMonitoredProjectOperation) Metadata() (*[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateMonitoredProjectOperation) Name 
    
    
    func (op *CreateMonitoredProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateMonitoredProjectOperation) Poll 
    
    
    func (op *CreateMonitoredProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[MonitoredProject](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_MonitoredProject), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateMonitoredProjectOperation) Wait 
    
    
    func (op *CreateMonitoredProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[MonitoredProject](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_MonitoredProject), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteMonitoredProjectOperation
    
    
    type DeleteMonitoredProjectOperation struct {
    	// contains filtered or unexported fields
    }

DeleteMonitoredProjectOperation manages a long-running operation from DeleteMonitoredProject.

### func (*DeleteMonitoredProjectOperation) Done 
    
    
    func (op *DeleteMonitoredProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteMonitoredProjectOperation) Metadata 
    
    
    func (op *DeleteMonitoredProjectOperation) Metadata() (*[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteMonitoredProjectOperation) Name 
    
    
    func (op *DeleteMonitoredProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteMonitoredProjectOperation) Poll 
    
    
    func (op *DeleteMonitoredProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteMonitoredProjectOperation) Wait 
    
    
    func (op *DeleteMonitoredProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## MetricsScopesCallOptions
    
    
    type MetricsScopesCallOptions struct {
    	GetMetricsScope                     []gax.CallOption
    	ListMetricsScopesByMonitoredProject []gax.CallOption
    	CreateMonitoredProject              []gax.CallOption
    	DeleteMonitoredProject              []gax.CallOption
    }

MetricsScopesCallOptions contains the retry settings for each method of MetricsScopesClient.

## MetricsScopesClient
    
    
    type MetricsScopesClient struct {
    
    	// The call options for this service.
    	CallOptions *MetricsScopesCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

MetricsScopesClient is a client for interacting with Cloud Monitoring API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Manages Cloud Monitoring Metrics Scopes, and the monitoring of Google Cloud projects and AWS accounts.

### func NewMetricsScopesClient 
    
    
    func NewMetricsScopesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*MetricsScopesClient, [error](https://pkg.go.dev/builtin#error))

NewMetricsScopesClient creates a new metrics scopes client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Manages Cloud Monitoring Metrics Scopes, and the monitoring of Google Cloud projects and AWS accounts.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metricsscope "cloud.google.com/go/monitoring/metricsscope/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metricsscope.NewMetricsScopesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1.html#cloud_google_com_go_monitoring_metricsscope_apiv1_MetricsScopesClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*MetricsScopesClient) Close 
    
    
    func (c *MetricsScopesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*MetricsScopesClient) Connection (deprecated)
    
    
    func (c *MetricsScopesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*MetricsScopesClient) CreateMonitoredProject 
    
    
    func (c *MetricsScopesClient) CreateMonitoredProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[CreateMonitoredProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_CreateMonitoredProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateMonitoredProjectOperation, [error](https://pkg.go.dev/builtin#error))

CreateMonitoredProject adds a MonitoredProject with the given project ID to the specified Metrics Scope.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metricsscope "cloud.google.com/go/monitoring/metricsscope/apiv1"
    	metricsscopepb "cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metricsscope.NewMetricsScopesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1.html#cloud_google_com_go_monitoring_metricsscope_apiv1_MetricsScopesClient_Close)()
    
    	req := &metricsscopepb.CreateMonitoredProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb#CreateMonitoredProjectRequest.
    	}
    	op, err := c.CreateMonitoredProject(ctx, req)
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
    

### func (*MetricsScopesClient) CreateMonitoredProjectOperation 
    
    
    func (c *MetricsScopesClient) CreateMonitoredProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateMonitoredProjectOperation

CreateMonitoredProjectOperation returns a new CreateMonitoredProjectOperation from a given name. The name must be that of a previously created CreateMonitoredProjectOperation, possibly from a different process.

### func (*MetricsScopesClient) DeleteMonitoredProject 
    
    
    func (c *MetricsScopesClient) DeleteMonitoredProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[DeleteMonitoredProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_DeleteMonitoredProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteMonitoredProjectOperation, [error](https://pkg.go.dev/builtin#error))

DeleteMonitoredProject deletes a MonitoredProject from the specified Metrics Scope.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metricsscope "cloud.google.com/go/monitoring/metricsscope/apiv1"
    	metricsscopepb "cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metricsscope.NewMetricsScopesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1.html#cloud_google_com_go_monitoring_metricsscope_apiv1_MetricsScopesClient_Close)()
    
    	req := &metricsscopepb.DeleteMonitoredProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb#DeleteMonitoredProjectRequest.
    	}
    	op, err := c.DeleteMonitoredProject(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*MetricsScopesClient) DeleteMonitoredProjectOperation 
    
    
    func (c *MetricsScopesClient) DeleteMonitoredProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteMonitoredProjectOperation

DeleteMonitoredProjectOperation returns a new DeleteMonitoredProjectOperation from a given name. The name must be that of a previously created DeleteMonitoredProjectOperation, possibly from a different process.

### func (*MetricsScopesClient) GetMetricsScope 
    
    
    func (c *MetricsScopesClient) GetMetricsScope(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[GetMetricsScopeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_GetMetricsScopeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[MetricsScope](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_MetricsScope), [error](https://pkg.go.dev/builtin#error))

GetMetricsScope returns a specific Metrics Scope.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metricsscope "cloud.google.com/go/monitoring/metricsscope/apiv1"
    	metricsscopepb "cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metricsscope.NewMetricsScopesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1.html#cloud_google_com_go_monitoring_metricsscope_apiv1_MetricsScopesClient_Close)()
    
    	req := &metricsscopepb.GetMetricsScopeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb#GetMetricsScopeRequest.
    	}
    	resp, err := c.GetMetricsScope(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetricsScopesClient) ListMetricsScopesByMonitoredProject 
    
    
    func (c *MetricsScopesClient) ListMetricsScopesByMonitoredProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[ListMetricsScopesByMonitoredProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_ListMetricsScopesByMonitoredProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metricsscopepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb).[ListMetricsScopesByMonitoredProjectResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1/metricsscopepb#cloud_google_com_go_monitoring_metricsscope_apiv1_metricsscopepb_ListMetricsScopesByMonitoredProjectResponse), [error](https://pkg.go.dev/builtin#error))

ListMetricsScopesByMonitoredProject returns a list of every Metrics Scope that a specific MonitoredProject has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metricsscope "cloud.google.com/go/monitoring/metricsscope/apiv1"
    	metricsscopepb "cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metricsscope.NewMetricsScopesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/metricsscope/apiv1.html#cloud_google_com_go_monitoring_metricsscope_apiv1_MetricsScopesClient_Close)()
    
    	req := &metricsscopepb.ListMetricsScopesByMonitoredProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/monitoring/metricsscope/apiv1/metricsscopepb#ListMetricsScopesByMonitoredProjectRequest.
    	}
    	resp, err := c.ListMetricsScopesByMonitoredProject(ctx, req)
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
