---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/
title: Access Approval API v1 - Package cloud.google.com/go/accessapproval/apiv1 (v1.14.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:01.589777+00:00
---

# Access Approval API v1 - Package cloud.google.com/go/accessapproval/apiv1 (v1.14.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Access Approval API v1 - Package cloud.google.com/go/accessapproval/apiv1 (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.8  1.7.12  1.6.1  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1). 

Package accessapproval is an auto-generated package for the Access Approval API. 

An API for controlling access to data by Google personnel. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/accessapproval/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := accessapproval.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &accessapprovalpb.ApproveApprovalRequestMessage{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#ApproveApprovalRequestMessage.
    }
    resp, err := c.ApproveApprovalRequest(ctx, req)
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

## ApprovalRequestIterator
    
    
    type ApprovalRequestIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*accessapprovalpb.ApprovalRequest, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ApprovalRequestIterator manages a stream of *accessapprovalpb.ApprovalRequest.

### func (*ApprovalRequestIterator) All 
    
    
    func (it *ApprovalRequestIterator) All() iter.Seq2[*accessapprovalpb.ApprovalRequest, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ApprovalRequestIterator) Next 
    
    
    func (it *ApprovalRequestIterator) Next() (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ApprovalRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ApprovalRequest), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ApprovalRequestIterator) PageInfo 
    
    
    func (it *ApprovalRequestIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CallOptions
    
    
    type CallOptions struct {
    	ListApprovalRequests            []gax.CallOption
    	GetApprovalRequest              []gax.CallOption
    	ApproveApprovalRequest          []gax.CallOption
    	DismissApprovalRequest          []gax.CallOption
    	InvalidateApprovalRequest       []gax.CallOption
    	GetAccessApprovalSettings       []gax.CallOption
    	UpdateAccessApprovalSettings    []gax.CallOption
    	DeleteAccessApprovalSettings    []gax.CallOption
    	GetAccessApprovalServiceAccount []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Access Approval API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

This API allows a customer to manage accesses to cloud resources by Google personnel. It defines the following resource model:
    
    
    The API has a collection of
    ApprovalRequest
    resources, named approvalRequests/{approval_request}
    
    The API has top-level settings per Project/Folder/Organization, named
    accessApprovalSettings
    

The service also periodically emails a list of recipients, defined at the Project/Folder/Organization level in the accessApprovalSettings, when there is a pending ApprovalRequest for them to act on. The ApprovalRequests can also optionally be published to a Pub/Sub topic owned by the customer (contact support if you would like to enable Pub/Sub notifications).

ApprovalRequests can be approved or dismissed. Google personnel can only access the indicated resource or resources if the request is approved (subject to some exclusions: <https://cloud.google.com/access-approval/docs/overview#exclusions> (at <https://cloud.google.com/access-approval/docs/overview#exclusions>)).

Note: Using Access Approval functionality will mean that Google may not be able to meet the SLAs for your chosen products, as any support response times may be dramatically increased. As such the SLAs do not apply to any service disruption to the extent impacted by Customer’s use of Access Approval. Do not enable Access Approval for projects where you may require high service availability and rapid response by Google Cloud Support.

After a request is approved or dismissed, no further action may be taken on it. Requests with the requested_expiration in the past or with no activity for 14 days are considered dismissed. When an approval expires, the request is considered dismissed.

If a request is not approved or dismissed, we call it pending.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new access approval client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

This API allows a customer to manage accesses to cloud resources by Google personnel. It defines the following resource model:
    
    
    The API has a collection of
    ApprovalRequest
    resources, named approvalRequests/{approval_request}
    
    The API has top-level settings per Project/Folder/Organization, named
    accessApprovalSettings
    

The service also periodically emails a list of recipients, defined at the Project/Folder/Organization level in the accessApprovalSettings, when there is a pending ApprovalRequest for them to act on. The ApprovalRequests can also optionally be published to a Pub/Sub topic owned by the customer (contact support if you would like to enable Pub/Sub notifications).

ApprovalRequests can be approved or dismissed. Google personnel can only access the indicated resource or resources if the request is approved (subject to some exclusions: <https://cloud.google.com/access-approval/docs/overview#exclusions> (at <https://cloud.google.com/access-approval/docs/overview#exclusions>)).

Note: Using Access Approval functionality will mean that Google may not be able to meet the SLAs for your chosen products, as any support response times may be dramatically increased. As such the SLAs do not apply to any service disruption to the extent impacted by Customer’s use of Access Approval. Do not enable Access Approval for projects where you may require high service availability and rapid response by Google Cloud Support.

After a request is approved or dismissed, no further action may be taken on it. Requests with the requested_expiration in the past or with no activity for 14 days are considered dismissed. When an approval expires, the request is considered dismissed.

If a request is not approved or dismissed, we call it pending.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new access approval rest client.

This API allows a customer to manage accesses to cloud resources by Google personnel. It defines the following resource model:
    
    
    The API has a collection of
    ApprovalRequest
    resources, named approvalRequests/{approval_request}
    
    The API has top-level settings per Project/Folder/Organization, named
    accessApprovalSettings
    

The service also periodically emails a list of recipients, defined at the Project/Folder/Organization level in the accessApprovalSettings, when there is a pending ApprovalRequest for them to act on. The ApprovalRequests can also optionally be published to a Pub/Sub topic owned by the customer (contact support if you would like to enable Pub/Sub notifications).

ApprovalRequests can be approved or dismissed. Google personnel can only access the indicated resource or resources if the request is approved (subject to some exclusions: <https://cloud.google.com/access-approval/docs/overview#exclusions> (at <https://cloud.google.com/access-approval/docs/overview#exclusions>)).

Note: Using Access Approval functionality will mean that Google may not be able to meet the SLAs for your chosen products, as any support response times may be dramatically increased. As such the SLAs do not apply to any service disruption to the extent impacted by Customer’s use of Access Approval. Do not enable Access Approval for projects where you may require high service availability and rapid response by Google Cloud Support.

After a request is approved or dismissed, no further action may be taken on it. Requests with the requested_expiration in the past or with no activity for 14 days are considered dismissed. When an approval expires, the request is considered dismissed.

If a request is not approved or dismissed, we call it pending.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) ApproveApprovalRequest 
    
    
    func (c *Client) ApproveApprovalRequest(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ApproveApprovalRequestMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ApproveApprovalRequestMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ApprovalRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ApprovalRequest), [error](https://pkg.go.dev/builtin#error))

ApproveApprovalRequest approves a request and returns the updated ApprovalRequest.

Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.ApproveApprovalRequestMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#ApproveApprovalRequestMessage.
    	}
    	resp, err := c.ApproveApprovalRequest(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) DeleteAccessApprovalSettings 
    
    
    func (c *Client) DeleteAccessApprovalSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[DeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_DeleteAccessApprovalSettingsMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAccessApprovalSettings deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.DeleteAccessApprovalSettingsMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#DeleteAccessApprovalSettingsMessage.
    	}
    	err = c.DeleteAccessApprovalSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DismissApprovalRequest 
    
    
    func (c *Client) DismissApprovalRequest(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[DismissApprovalRequestMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_DismissApprovalRequestMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ApprovalRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ApprovalRequest), [error](https://pkg.go.dev/builtin#error))

DismissApprovalRequest dismisses a request. Returns the updated ApprovalRequest.

NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether.

Returns NOT_FOUND if the request does not exist.

Returns FAILED_PRECONDITION if the request exists but is not in a pending state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.DismissApprovalRequestMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#DismissApprovalRequestMessage.
    	}
    	resp, err := c.DismissApprovalRequest(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetAccessApprovalServiceAccount 
    
    
    func (c *Client) GetAccessApprovalServiceAccount(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[GetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_GetAccessApprovalServiceAccountMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[AccessApprovalServiceAccount](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_AccessApprovalServiceAccount), [error](https://pkg.go.dev/builtin#error))

GetAccessApprovalServiceAccount retrieves the service account that is used by Access Approval to access KMS keys for signing approved approval requests.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.GetAccessApprovalServiceAccountMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#GetAccessApprovalServiceAccountMessage.
    	}
    	resp, err := c.GetAccessApprovalServiceAccount(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetAccessApprovalSettings 
    
    
    func (c *Client) GetAccessApprovalSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[GetAccessApprovalSettingsMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_GetAccessApprovalSettingsMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[AccessApprovalSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_AccessApprovalSettings), [error](https://pkg.go.dev/builtin#error))

GetAccessApprovalSettings gets the settings associated with a project, folder, or organization.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.GetAccessApprovalSettingsMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#GetAccessApprovalSettingsMessage.
    	}
    	resp, err := c.GetAccessApprovalSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetApprovalRequest 
    
    
    func (c *Client) GetApprovalRequest(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[GetApprovalRequestMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_GetApprovalRequestMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ApprovalRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ApprovalRequest), [error](https://pkg.go.dev/builtin#error))

GetApprovalRequest gets an approval request. Returns NOT_FOUND if the request does not exist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.GetApprovalRequestMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#GetApprovalRequestMessage.
    	}
    	resp, err := c.GetApprovalRequest(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) InvalidateApprovalRequest 
    
    
    func (c *Client) InvalidateApprovalRequest(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[InvalidateApprovalRequestMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_InvalidateApprovalRequestMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ApprovalRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ApprovalRequest), [error](https://pkg.go.dev/builtin#error))

InvalidateApprovalRequest invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest.

NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval.

Returns FAILED_PRECONDITION if the request exists but is not in an approved state.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.InvalidateApprovalRequestMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#InvalidateApprovalRequestMessage.
    	}
    	resp, err := c.InvalidateApprovalRequest(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListApprovalRequests 
    
    
    func (c *Client) ListApprovalRequests(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[ListApprovalRequestsMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_ListApprovalRequestsMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ApprovalRequestIterator

ListApprovalRequests lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.ListApprovalRequestsMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#ListApprovalRequestsMessage.
    	}
    	it := c.ListApprovalRequests(ctx, req)
    	for {
    		resp, err := it.[Next](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_ApprovalRequestIterator_Next)()
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
    		_ = it.Response.(*accessapprovalpb.ListApprovalRequestsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.ListApprovalRequestsMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#ListApprovalRequestsMessage.
    	}
    	for resp, err := range c.ListApprovalRequests(ctx, req).[All](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_ApprovalRequestIterator_All)() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) UpdateAccessApprovalSettings 
    
    
    func (c *Client) UpdateAccessApprovalSettings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[UpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_UpdateAccessApprovalSettingsMessage), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[accessapprovalpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb).[AccessApprovalSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1/accessapprovalpb#cloud_google_com_go_accessapproval_apiv1_accessapprovalpb_AccessApprovalSettings), [error](https://pkg.go.dev/builtin#error))

UpdateAccessApprovalSettings updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	accessapproval "cloud.google.com/go/accessapproval/apiv1"
    	accessapprovalpb "cloud.google.com/go/accessapproval/apiv1/accessapprovalpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := accessapproval.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/accessapproval/latest/apiv1.html#cloud_google_com_go_accessapproval_apiv1_Client_Close)()
    
    	req := &accessapprovalpb.UpdateAccessApprovalSettingsMessage{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/accessapproval/apiv1/accessapprovalpb#UpdateAccessApprovalSettingsMessage.
    	}
    	resp, err := c.UpdateAccessApprovalSettings(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
