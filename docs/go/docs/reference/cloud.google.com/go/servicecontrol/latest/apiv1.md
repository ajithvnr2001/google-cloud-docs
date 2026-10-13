---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/
title: Service Control API v1 - Package cloud.google.com/go/servicecontrol/apiv1 (v1.20.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:46.451639+00:00
---

# Service Control API v1 - Package cloud.google.com/go/servicecontrol/apiv1 (v1.20.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Service Control API v1 - Package cloud.google.com/go/servicecontrol/apiv1 (v1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.6  1.13.7  1.12.5  1.11.2  1.10.0  1.9.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/servicecontrol/apiv1). 

Package servicecontrol is an auto-generated package for the Service Control API. 

Provides admission control and telemetry reporting for services integrated with Service Infrastructure. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/servicecontrol/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := servicecontrol.NewQuotaControllerClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &servicecontrolpb.AllocateQuotaRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb#AllocateQuotaRequest.
    }
    resp, err := c.AllocateQuota(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewQuotaControllerClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## QuotaControllerCallOptions
    
    
    type QuotaControllerCallOptions struct {
    	AllocateQuota []gax.CallOption
    }

QuotaControllerCallOptions contains the retry settings for each method of QuotaControllerClient.

## QuotaControllerClient
    
    
    type QuotaControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *QuotaControllerCallOptions
    	// contains filtered or unexported fields
    }

QuotaControllerClient is a client for interacting with Service Control API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Google Quota Control API (at <https://cloud.google.com/service-control/overview>)

Allows clients to allocate and release quota against a managed service (at <https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService>).

### func NewQuotaControllerClient 
    
    
    func NewQuotaControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*QuotaControllerClient, [error](https://pkg.go.dev/builtin#error))

NewQuotaControllerClient creates a new quota controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Google Quota Control API (at <https://cloud.google.com/service-control/overview>)

Allows clients to allocate and release quota against a managed service (at <https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.NewQuotaControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewQuotaControllerRESTClient 
    
    
    func NewQuotaControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*QuotaControllerClient, [error](https://pkg.go.dev/builtin#error))

NewQuotaControllerRESTClient creates a new quota controller rest client.

Google Quota Control API (at <https://cloud.google.com/service-control/overview>)

Allows clients to allocate and release quota against a managed service (at <https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.[NewQuotaControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1.html#cloud_google_com_go_servicecontrol_apiv1_QuotaControllerClient_NewQuotaControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*QuotaControllerClient) AllocateQuota 
    
    
    func (c *QuotaControllerClient) AllocateQuota(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[servicecontrolpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb).[AllocateQuotaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb#cloud_google_com_go_servicecontrol_apiv1_servicecontrolpb_AllocateQuotaRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[servicecontrolpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb).[AllocateQuotaResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb#cloud_google_com_go_servicecontrol_apiv1_servicecontrolpb_AllocateQuotaResponse), [error](https://pkg.go.dev/builtin#error))

AllocateQuota attempts to allocate quota for the specified consumer. It should be called before the operation is executed.

This method requires the servicemanagement.services.quota permission on the specified service. For more information, see Cloud IAM (at <https://cloud.google.com/iam>).

NOTE: The client must fail-open on server errors INTERNAL, UNKNOWN, DEADLINE_EXCEEDED, and UNAVAILABLE. To ensure system reliability, the server may inject these errors to prohibit any hard dependency on the quota functionality.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    	servicecontrolpb "cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.NewQuotaControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &servicecontrolpb.AllocateQuotaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb#AllocateQuotaRequest.
    	}
    	resp, err := c.AllocateQuota(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*QuotaControllerClient) Close 
    
    
    func (c *QuotaControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*QuotaControllerClient) Connection (deprecated)
    
    
    func (c *QuotaControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

## ServiceControllerCallOptions
    
    
    type ServiceControllerCallOptions struct {
    	Check  []gax.CallOption
    	Report []gax.CallOption
    }

ServiceControllerCallOptions contains the retry settings for each method of ServiceControllerClient.

## ServiceControllerClient
    
    
    type ServiceControllerClient struct {
    
    	// The call options for this service.
    	CallOptions *ServiceControllerCallOptions
    	// contains filtered or unexported fields
    }

ServiceControllerClient is a client for interacting with Service Control API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Google Service Control API (at <https://cloud.google.com/service-control/overview>)

Lets clients check and report operations against a managed service (at <https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService>).

### func NewServiceControllerClient 
    
    
    func NewServiceControllerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ServiceControllerClient, [error](https://pkg.go.dev/builtin#error))

NewServiceControllerClient creates a new service controller client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Google Service Control API (at <https://cloud.google.com/service-control/overview>)

Lets clients check and report operations against a managed service (at <https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.NewServiceControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewServiceControllerRESTClient 
    
    
    func NewServiceControllerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ServiceControllerClient, [error](https://pkg.go.dev/builtin#error))

NewServiceControllerRESTClient creates a new service controller rest client.

Google Service Control API (at <https://cloud.google.com/service-control/overview>)

Lets clients check and report operations against a managed service (at <https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.[NewServiceControllerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1.html#cloud_google_com_go_servicecontrol_apiv1_ServiceControllerClient_NewServiceControllerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ServiceControllerClient) Check 
    
    
    func (c *ServiceControllerClient) Check(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[servicecontrolpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb).[CheckRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb#cloud_google_com_go_servicecontrol_apiv1_servicecontrolpb_CheckRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[servicecontrolpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb).[CheckResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb#cloud_google_com_go_servicecontrol_apiv1_servicecontrolpb_CheckResponse), [error](https://pkg.go.dev/builtin#error))

Check checks whether an operation on a service should be allowed to proceed based on the configuration of the service and related policies. It must be called before the operation is executed.

If feasible, the client should cache the check results and reuse them for 60 seconds. In case of any server errors, the client should rely on the cached results for much longer time to avoid outage. WARNING: There is general 60s delay for the configuration and policy propagation, therefore callers MUST NOT depend on the Check method having the latest policy information.

NOTE: the CheckRequest has the size limit (wire-format byte size) of 1MB.

This method requires the servicemanagement.services.check permission on the specified service. For more information, see Cloud IAM (at <https://cloud.google.com/iam>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    	servicecontrolpb "cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.NewServiceControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &servicecontrolpb.CheckRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb#CheckRequest.
    	}
    	resp, err := c.Check(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ServiceControllerClient) Close 
    
    
    func (c *ServiceControllerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ServiceControllerClient) Connection (deprecated)
    
    
    func (c *ServiceControllerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ServiceControllerClient) Report 
    
    
    func (c *ServiceControllerClient) Report(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[servicecontrolpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb).[ReportRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb#cloud_google_com_go_servicecontrol_apiv1_servicecontrolpb_ReportRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[servicecontrolpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb).[ReportResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicecontrol/latest/apiv1/servicecontrolpb#cloud_google_com_go_servicecontrol_apiv1_servicecontrolpb_ReportResponse), [error](https://pkg.go.dev/builtin#error))

Report reports operation results to Google Service Control, such as logs and metrics. It should be called after an operation is completed.

If feasible, the client should aggregate reporting data for up to 5 seconds to reduce API traffic. Limiting aggregation to 5 seconds is to reduce data loss during client crashes. Clients should carefully choose the aggregation time window to avoid data loss risk more than 0.01% for business and compliance reasons.

NOTE: the ReportRequest has the size limit (wire-format byte size) of 1MB.

This method requires the servicemanagement.services.report permission on the specified service. For more information, see Google Cloud IAM (at <https://cloud.google.com/iam>).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	servicecontrol "cloud.google.com/go/servicecontrol/apiv1"
    	servicecontrolpb "cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := servicecontrol.NewServiceControllerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &servicecontrolpb.ReportRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/servicecontrol/apiv1/servicecontrolpb#ReportRequest.
    	}
    	resp, err := c.Report(ctx, req)
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
