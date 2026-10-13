---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/
title: CSS API v1 - Package cloud.google.com/go/shopping/css/apiv1 (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:54.253821+00:00
---

# CSS API v1 - Package cloud.google.com/go/shopping/css/apiv1 (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  CSS API v1 - Package cloud.google.com/go/shopping/css/apiv1 (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.25.0  0.24.1  0.23.0  0.22.0  0.21.0  0.20.0  0.19.1  0.18.1  0.17.1  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1  0.10.0  0.9.2  0.8.7  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1). 

Package css is an auto-generated package for the CSS API. 

Programmatically manage your Comparison Shopping Service (CSS) account data at scale.
    
    
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
    
    
    // go get cloud.google.com/go/shopping/css/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := css.NewAccountsClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &csspb.GetAccountRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#GetAccountRequest.
    }
    resp, err := c.GetAccount(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewAccountsClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AccountIterator
    
    
    type AccountIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*csspb.Account, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AccountIterator manages a stream of *csspb.Account.

### func (*AccountIterator) All 
    
    
    func (it *AccountIterator) All() iter.Seq2[*csspb.Account, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AccountIterator) Next 
    
    
    func (it *AccountIterator) Next() (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[Account](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_Account), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AccountIterator) PageInfo 
    
    
    func (it *AccountIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AccountLabelIterator
    
    
    type AccountLabelIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*csspb.AccountLabel, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AccountLabelIterator manages a stream of *csspb.AccountLabel.

### func (*AccountLabelIterator) All 
    
    
    func (it *AccountLabelIterator) All() iter.Seq2[*csspb.AccountLabel, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AccountLabelIterator) Next 
    
    
    func (it *AccountLabelIterator) Next() (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[AccountLabel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_AccountLabel), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AccountLabelIterator) PageInfo 
    
    
    func (it *AccountLabelIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AccountLabelsCallOptions
    
    
    type AccountLabelsCallOptions struct {
    	ListAccountLabels  []gax.CallOption
    	CreateAccountLabel []gax.CallOption
    	UpdateAccountLabel []gax.CallOption
    	DeleteAccountLabel []gax.CallOption
    }

AccountLabelsCallOptions contains the retry settings for each method of AccountLabelsClient.

## AccountLabelsClient
    
    
    type AccountLabelsClient struct {
    
    	// The call options for this service.
    	CallOptions *AccountLabelsCallOptions
    	// contains filtered or unexported fields
    }

AccountLabelsClient is a client for interacting with CSS API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Manages Merchant Center and CSS accounts labels.

### func NewAccountLabelsClient 
    
    
    func NewAccountLabelsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AccountLabelsClient, [error](https://pkg.go.dev/builtin#error))

NewAccountLabelsClient creates a new account labels service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Manages Merchant Center and CSS accounts labels.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAccountLabelsRESTClient 
    
    
    func NewAccountLabelsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AccountLabelsClient, [error](https://pkg.go.dev/builtin#error))

NewAccountLabelsRESTClient creates a new account labels service rest client.

Manages Merchant Center and CSS accounts labels.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AccountLabelsClient) Close 
    
    
    func (c *AccountLabelsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AccountLabelsClient) Connection (deprecated)
    
    
    func (c *AccountLabelsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AccountLabelsClient) CreateAccountLabel 
    
    
    func (c *AccountLabelsClient) CreateAccountLabel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[CreateAccountLabelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_CreateAccountLabelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[AccountLabel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_AccountLabel), [error](https://pkg.go.dev/builtin#error))

CreateAccountLabel creates a new label, not assigned to any account.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.CreateAccountLabelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#CreateAccountLabelRequest.
    	}
    	resp, err := c.CreateAccountLabel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AccountLabelsClient) DeleteAccountLabel 
    
    
    func (c *AccountLabelsClient) DeleteAccountLabel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[DeleteAccountLabelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_DeleteAccountLabelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteAccountLabel deletes a label and removes it from all accounts to which it was assigned.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.DeleteAccountLabelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#DeleteAccountLabelRequest.
    	}
    	err = c.DeleteAccountLabel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*AccountLabelsClient) ListAccountLabels 
    
    
    func (c *AccountLabelsClient) ListAccountLabels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[ListAccountLabelsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_ListAccountLabelsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AccountLabelIterator

ListAccountLabels lists the labels owned by an account.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListAccountLabelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListAccountLabelsRequest.
    	}
    	it := c.ListAccountLabels(ctx, req)
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
    		_ = it.Response.(*csspb.ListAccountLabelsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListAccountLabelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListAccountLabelsRequest.
    	}
    	for resp, err := range c.ListAccountLabels(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AccountLabelsClient) UpdateAccountLabel 
    
    
    func (c *AccountLabelsClient) UpdateAccountLabel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[UpdateAccountLabelRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_UpdateAccountLabelRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[AccountLabel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_AccountLabel), [error](https://pkg.go.dev/builtin#error))

UpdateAccountLabel updates a label.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountLabelsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountLabelsClient_NewAccountLabelsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.UpdateAccountLabelRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#UpdateAccountLabelRequest.
    	}
    	resp, err := c.UpdateAccountLabel(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## AccountsCallOptions
    
    
    type AccountsCallOptions struct {
    	ListChildAccounts []gax.CallOption
    	GetAccount        []gax.CallOption
    	UpdateLabels      []gax.CallOption
    }

AccountsCallOptions contains the retry settings for each method of AccountsClient.

## AccountsClient
    
    
    type AccountsClient struct {
    
    	// The call options for this service.
    	CallOptions *AccountsCallOptions
    	// contains filtered or unexported fields
    }

AccountsClient is a client for interacting with CSS API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for managing CSS/MC account information.

### func NewAccountsClient 
    
    
    func NewAccountsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AccountsClient, [error](https://pkg.go.dev/builtin#error))

NewAccountsClient creates a new accounts service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for managing CSS/MC account information.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountsClient_NewAccountsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewAccountsRESTClient 
    
    
    func NewAccountsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*AccountsClient, [error](https://pkg.go.dev/builtin#error))

NewAccountsRESTClient creates a new accounts service rest client.

Service for managing CSS/MC account information.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountsClient_NewAccountsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*AccountsClient) Close 
    
    
    func (c *AccountsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*AccountsClient) Connection (deprecated)
    
    
    func (c *AccountsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*AccountsClient) GetAccount 
    
    
    func (c *AccountsClient) GetAccount(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[GetAccountRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_GetAccountRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[Account](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_Account), [error](https://pkg.go.dev/builtin#error))

GetAccount retrieves a single CSS/MC account by ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountsClient_NewAccountsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.GetAccountRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#GetAccountRequest.
    	}
    	resp, err := c.GetAccount(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*AccountsClient) ListChildAccounts 
    
    
    func (c *AccountsClient) ListChildAccounts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[ListChildAccountsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_ListChildAccountsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AccountIterator

ListChildAccounts lists all the accounts under the specified CSS account ID, and optionally filters by label ID and account name.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountsClient_NewAccountsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListChildAccountsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListChildAccountsRequest.
    	}
    	it := c.ListChildAccounts(ctx, req)
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
    		_ = it.Response.(*csspb.ListChildAccountsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountsClient_NewAccountsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListChildAccountsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListChildAccountsRequest.
    	}
    	for resp, err := range c.ListChildAccounts(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*AccountsClient) UpdateLabels 
    
    
    func (c *AccountsClient) UpdateLabels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[UpdateAccountLabelsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_UpdateAccountLabelsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[Account](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_Account), [error](https://pkg.go.dev/builtin#error))

UpdateLabels updates labels assigned to CSS/MC accounts by a CSS domain.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewAccountsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_AccountsClient_NewAccountsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.UpdateAccountLabelsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#UpdateAccountLabelsRequest.
    	}
    	resp, err := c.UpdateLabels(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CssProductInputsCallOptions
    
    
    type CssProductInputsCallOptions struct {
    	InsertCssProductInput []gax.CallOption
    	UpdateCssProductInput []gax.CallOption
    	DeleteCssProductInput []gax.CallOption
    }

CssProductInputsCallOptions contains the retry settings for each method of CssProductInputsClient.

## CssProductInputsClient
    
    
    type CssProductInputsClient struct {
    
    	// The call options for this service.
    	CallOptions *CssProductInputsCallOptions
    	// contains filtered or unexported fields
    }

CssProductInputsClient is a client for interacting with CSS API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service to use CssProductInput resource. This service helps to insert/update/delete CSS Products.

### func NewCssProductInputsClient 
    
    
    func NewCssProductInputsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CssProductInputsClient, [error](https://pkg.go.dev/builtin#error))

NewCssProductInputsClient creates a new css product inputs service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service to use CssProductInput resource. This service helps to insert/update/delete CSS Products.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductInputsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductInputsClient_NewCssProductInputsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCssProductInputsRESTClient 
    
    
    func NewCssProductInputsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CssProductInputsClient, [error](https://pkg.go.dev/builtin#error))

NewCssProductInputsRESTClient creates a new css product inputs service rest client.

Service to use CssProductInput resource. This service helps to insert/update/delete CSS Products.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductInputsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductInputsClient_NewCssProductInputsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CssProductInputsClient) Close 
    
    
    func (c *CssProductInputsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CssProductInputsClient) Connection (deprecated)
    
    
    func (c *CssProductInputsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CssProductInputsClient) DeleteCssProductInput 
    
    
    func (c *CssProductInputsClient) DeleteCssProductInput(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[DeleteCssProductInputRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_DeleteCssProductInputRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteCssProductInput deletes a CSS Product input from your CSS Center account.

After a delete it may take several minutes until the input is no longer available.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductInputsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductInputsClient_NewCssProductInputsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.DeleteCssProductInputRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#DeleteCssProductInputRequest.
    	}
    	err = c.DeleteCssProductInput(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CssProductInputsClient) InsertCssProductInput 
    
    
    func (c *CssProductInputsClient) InsertCssProductInput(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[InsertCssProductInputRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_InsertCssProductInputRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[CssProductInput](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_CssProductInput), [error](https://pkg.go.dev/builtin#error))

InsertCssProductInput uploads a CssProductInput to your CSS Center account. If an input with the same contentLanguage, identity, feedLabel and feedId already exists, this method replaces that entry.

After inserting, updating, or deleting a CSS Product input, it may take several minutes before the processed CSS Product can be retrieved.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductInputsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductInputsClient_NewCssProductInputsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.InsertCssProductInputRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#InsertCssProductInputRequest.
    	}
    	resp, err := c.InsertCssProductInput(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CssProductInputsClient) UpdateCssProductInput 
    
    
    func (c *CssProductInputsClient) UpdateCssProductInput(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[UpdateCssProductInputRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_UpdateCssProductInputRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[CssProductInput](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_CssProductInput), [error](https://pkg.go.dev/builtin#error))

UpdateCssProductInput updates the existing Css Product input in your CSS Center account.

After inserting, updating, or deleting a CSS Product input, it may take several minutes before the processed Css Product can be retrieved.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductInputsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductInputsClient_NewCssProductInputsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.UpdateCssProductInputRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#UpdateCssProductInputRequest.
    	}
    	resp, err := c.UpdateCssProductInput(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CssProductIterator
    
    
    type CssProductIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*csspb.CssProduct, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CssProductIterator manages a stream of *csspb.CssProduct.

### func (*CssProductIterator) All 
    
    
    func (it *CssProductIterator) All() iter.Seq2[*csspb.CssProduct, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CssProductIterator) Next 
    
    
    func (it *CssProductIterator) Next() (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[CssProduct](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_CssProduct), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CssProductIterator) PageInfo 
    
    
    func (it *CssProductIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CssProductsCallOptions
    
    
    type CssProductsCallOptions struct {
    	GetCssProduct   []gax.CallOption
    	ListCssProducts []gax.CallOption
    }

CssProductsCallOptions contains the retry settings for each method of CssProductsClient.

## CssProductsClient
    
    
    type CssProductsClient struct {
    
    	// The call options for this service.
    	CallOptions *CssProductsCallOptions
    	// contains filtered or unexported fields
    }

CssProductsClient is a client for interacting with CSS API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for doing get and list on Css Products(a.k.a Aggregate Offers internally).

### func NewCssProductsClient 
    
    
    func NewCssProductsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CssProductsClient, [error](https://pkg.go.dev/builtin#error))

NewCssProductsClient creates a new css products service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for doing get and list on Css Products(a.k.a Aggregate Offers internally).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductsClient_NewCssProductsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCssProductsRESTClient 
    
    
    func NewCssProductsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CssProductsClient, [error](https://pkg.go.dev/builtin#error))

NewCssProductsRESTClient creates a new css products service rest client.

Service for doing get and list on Css Products(a.k.a Aggregate Offers internally).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductsClient_NewCssProductsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CssProductsClient) Close 
    
    
    func (c *CssProductsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CssProductsClient) Connection (deprecated)
    
    
    func (c *CssProductsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CssProductsClient) GetCssProduct 
    
    
    func (c *CssProductsClient) GetCssProduct(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[GetCssProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_GetCssProductRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[CssProduct](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_CssProduct), [error](https://pkg.go.dev/builtin#error))

GetCssProduct retrieves the processed CSS Product from your CSS Center account. After inserting, updating, or deleting a product input, it may take several minutes before the updated final product can be retrieved.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductsClient_NewCssProductsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.GetCssProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#GetCssProductRequest.
    	}
    	resp, err := c.GetCssProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CssProductsClient) ListCssProducts 
    
    
    func (c *CssProductsClient) ListCssProducts(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[ListCssProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_ListCssProductsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CssProductIterator

ListCssProducts lists the processed CSS Products in your CSS Center account. The response might contain fewer items than specified by pageSize. Rely on pageToken to determine if there are more items to be requested.

After inserting, updating, or deleting a CSS product input, it may take several minutes before the updated processed CSS product can be retrieved.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductsClient_NewCssProductsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListCssProductsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListCssProductsRequest.
    	}
    	it := c.ListCssProducts(ctx, req)
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
    		_ = it.Response.(*csspb.ListCssProductsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewCssProductsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_CssProductsClient_NewCssProductsClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListCssProductsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListCssProductsRequest.
    	}
    	for resp, err := range c.ListCssProducts(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## QuotaCallOptions
    
    
    type QuotaCallOptions struct {
    	ListQuotaGroups []gax.CallOption
    }

QuotaCallOptions contains the retry settings for each method of QuotaClient.

## QuotaClient
    
    
    type QuotaClient struct {
    
    	// The call options for this service.
    	CallOptions *QuotaCallOptions
    	// contains filtered or unexported fields
    }

QuotaClient is a client for interacting with CSS API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service to get method call quota information per CSS API method.

### func NewQuotaClient 
    
    
    func NewQuotaClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*QuotaClient, [error](https://pkg.go.dev/builtin#error))

NewQuotaClient creates a new quota service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service to get method call quota information per CSS API method.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewQuotaClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_QuotaClient_NewQuotaClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewQuotaRESTClient 
    
    
    func NewQuotaRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*QuotaClient, [error](https://pkg.go.dev/builtin#error))

NewQuotaRESTClient creates a new quota service rest client.

Service to get method call quota information per CSS API method.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewQuotaRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_QuotaClient_NewQuotaRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*QuotaClient) Close 
    
    
    func (c *QuotaClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*QuotaClient) Connection (deprecated)
    
    
    func (c *QuotaClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*QuotaClient) ListQuotaGroups 
    
    
    func (c *QuotaClient) ListQuotaGroups(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[ListQuotaGroupsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_ListQuotaGroupsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *QuotaGroupIterator

ListQuotaGroups lists the daily call quota and usage per group for your CSS Center account.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewQuotaClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_QuotaClient_NewQuotaClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListQuotaGroupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListQuotaGroupsRequest.
    	}
    	it := c.ListQuotaGroups(ctx, req)
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
    		_ = it.Response.(*csspb.ListQuotaGroupsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	css "cloud.google.com/go/shopping/css/apiv1"
    	csspb "cloud.google.com/go/shopping/css/apiv1/csspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := css.[NewQuotaClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1.html#cloud_google_com_go_shopping_css_apiv1_QuotaClient_NewQuotaClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &csspb.ListQuotaGroupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shopping/css/apiv1/csspb#ListQuotaGroupsRequest.
    	}
    	for resp, err := range c.ListQuotaGroups(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## QuotaGroupIterator
    
    
    type QuotaGroupIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*csspb.QuotaGroup, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

QuotaGroupIterator manages a stream of *csspb.QuotaGroup.

### func (*QuotaGroupIterator) All 
    
    
    func (it *QuotaGroupIterator) All() iter.Seq2[*csspb.QuotaGroup, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*QuotaGroupIterator) Next 
    
    
    func (it *QuotaGroupIterator) Next() (*[csspb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb).[QuotaGroup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/css/apiv1/csspb#cloud_google_com_go_shopping_css_apiv1_csspb_QuotaGroup), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*QuotaGroupIterator) PageInfo 
    
    
    func (it *QuotaGroupIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
