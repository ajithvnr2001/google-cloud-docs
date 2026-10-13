---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/
title: BigLake API v1alpha1 - Package cloud.google.com/go/bigquery/biglake/apiv1alpha1 (v1.85.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:28.253432+00:00
---

# BigLake API v1alpha1 - Package cloud.google.com/go/bigquery/biglake/apiv1alpha1 (v1.85.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  BigLake API v1alpha1 - Package cloud.google.com/go/bigquery/biglake/apiv1alpha1 (v1.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.85.0 (latest)  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.1  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.1  1.72.0  1.71.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.2  1.65.0  1.64.0  1.63.1  1.62.0  1.61.0  1.60.0  1.59.1  1.58.0  1.57.1  1.54.0  1.53.0  1.52.0  1.51.2  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.0  1.31.0  1.30.2  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0 

**Alpha**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1). 

Package biglake is an auto-generated package for the BigLake API. 

The BigLake API provides access to BigLake Metastore, a serverless, fully managed, and highly available metastore for open-source data that can be used for querying Apache Iceberg tables in BigQuery.
    
    
    NOTE: This package is in alpha. It is not stable, and is likely to change.

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/bigquery/biglake/apiv1alpha1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := biglake.NewMetastoreClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &biglakepb.CheckLockRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#CheckLockRequest.
    }
    resp, err := c.CheckLock(ctx, req)
    if err != nil {
        // TODO: Handle error.
    }
    // TODO: Use resp.
    _ = resp

## Use of Context

The ctx passed to NewMetastoreClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*biglakepb.Catalog, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CatalogIterator manages a stream of *biglakepb.Catalog.

### func (*CatalogIterator) All 
    
    
    func (it *CatalogIterator) All() iter.Seq2[*biglakepb.Catalog, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CatalogIterator) Next 
    
    
    func (it *CatalogIterator) Next() (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Catalog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Catalog), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CatalogIterator) PageInfo 
    
    
    func (it *CatalogIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DatabaseIterator
    
    
    type DatabaseIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*biglakepb.Database, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DatabaseIterator manages a stream of *biglakepb.Database.

### func (*DatabaseIterator) All 
    
    
    func (it *DatabaseIterator) All() iter.Seq2[*biglakepb.Database, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DatabaseIterator) Next 
    
    
    func (it *DatabaseIterator) Next() (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Database), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DatabaseIterator) PageInfo 
    
    
    func (it *DatabaseIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## LockIterator
    
    
    type LockIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*biglakepb.Lock, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

LockIterator manages a stream of *biglakepb.Lock.

### func (*LockIterator) All 
    
    
    func (it *LockIterator) All() iter.Seq2[*biglakepb.Lock, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*LockIterator) Next 
    
    
    func (it *LockIterator) Next() (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Lock](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Lock), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*LockIterator) PageInfo 
    
    
    func (it *LockIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## MetastoreCallOptions
    
    
    type MetastoreCallOptions struct {
    	CreateCatalog  []gax.CallOption
    	DeleteCatalog  []gax.CallOption
    	GetCatalog     []gax.CallOption
    	ListCatalogs   []gax.CallOption
    	CreateDatabase []gax.CallOption
    	DeleteDatabase []gax.CallOption
    	UpdateDatabase []gax.CallOption
    	GetDatabase    []gax.CallOption
    	ListDatabases  []gax.CallOption
    	CreateTable    []gax.CallOption
    	DeleteTable    []gax.CallOption
    	UpdateTable    []gax.CallOption
    	RenameTable    []gax.CallOption
    	GetTable       []gax.CallOption
    	ListTables     []gax.CallOption
    	CreateLock     []gax.CallOption
    	DeleteLock     []gax.CallOption
    	CheckLock      []gax.CallOption
    	ListLocks      []gax.CallOption
    }

MetastoreCallOptions contains the retry settings for each method of MetastoreClient.

## MetastoreClient
    
    
    type MetastoreClient struct {
    
    	// The call options for this service.
    	CallOptions *MetastoreCallOptions
    	// contains filtered or unexported fields
    }

MetastoreClient is a client for interacting with BigLake API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

BigLake Metastore is a serverless, highly available, multi-tenant runtime metastore for Google Cloud Data Analytics products.

The BigLake Metastore API defines the following resource model:
    
    
    A collection of Google Cloud projects: /projects/*
    
    Each project has a collection of available locations: /locations/*
    
    Each location has a collection of catalogs: /catalogs/*
    
    Each catalog has a collection of databases: /databases/*
    
    Each database has a collection of tables: /tables/*
    

### func NewMetastoreClient 
    
    
    func NewMetastoreClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*MetastoreClient, [error](https://pkg.go.dev/builtin#error))

NewMetastoreClient creates a new metastore service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

BigLake Metastore is a serverless, highly available, multi-tenant runtime metastore for Google Cloud Data Analytics products.

The BigLake Metastore API defines the following resource model:
    
    
    A collection of Google Cloud projects: /projects/*
    
    Each project has a collection of available locations: /locations/*
    
    Each location has a collection of catalogs: /catalogs/*
    
    Each catalog has a collection of databases: /databases/*
    
    Each database has a collection of tables: /tables/*
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewMetastoreRESTClient 
    
    
    func NewMetastoreRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[option](https://pkg.go.dev/google.golang.org/api/option).[ClientOption](https://pkg.go.dev/google.golang.org/api/option#ClientOption)) (*MetastoreClient, [error](https://pkg.go.dev/builtin#error))

NewMetastoreRESTClient creates a new metastore service rest client.

BigLake Metastore is a serverless, highly available, multi-tenant runtime metastore for Google Cloud Data Analytics products.

The BigLake Metastore API defines the following resource model:
    
    
    A collection of Google Cloud projects: /projects/*
    
    Each project has a collection of available locations: /locations/*
    
    Each location has a collection of catalogs: /catalogs/*
    
    Each catalog has a collection of databases: /databases/*
    
    Each database has a collection of tables: /tables/*
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*MetastoreClient) CheckLock 
    
    
    func (c *MetastoreClient) CheckLock(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[CheckLockRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_CheckLockRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Lock](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Lock), [error](https://pkg.go.dev/builtin#error))

CheckLock checks the state of a lock specified by the lock ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.CheckLockRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#CheckLockRequest.
    	}
    	resp, err := c.CheckLock(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) Close 
    
    
    func (c *MetastoreClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*MetastoreClient) Connection (deprecated)
    
    
    func (c *MetastoreClient) Connection() *[grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConn](https://pkg.go.dev/google.golang.org/grpc#ClientConn)

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*MetastoreClient) CreateCatalog 
    
    
    func (c *MetastoreClient) CreateCatalog(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[CreateCatalogRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_CreateCatalogRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Catalog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Catalog), [error](https://pkg.go.dev/builtin#error))

CreateCatalog creates a new catalog.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.CreateCatalogRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#CreateCatalogRequest.
    	}
    	resp, err := c.CreateCatalog(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) CreateDatabase 
    
    
    func (c *MetastoreClient) CreateDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[CreateDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_CreateDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Database), [error](https://pkg.go.dev/builtin#error))

CreateDatabase creates a new database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.CreateDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#CreateDatabaseRequest.
    	}
    	resp, err := c.CreateDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) CreateLock 
    
    
    func (c *MetastoreClient) CreateLock(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[CreateLockRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_CreateLockRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Lock](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Lock), [error](https://pkg.go.dev/builtin#error))

CreateLock creates a new lock.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.CreateLockRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#CreateLockRequest.
    	}
    	resp, err := c.CreateLock(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) CreateTable 
    
    
    func (c *MetastoreClient) CreateTable(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[CreateTableRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_CreateTableRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Table](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Table), [error](https://pkg.go.dev/builtin#error))

CreateTable creates a new table.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.CreateTableRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#CreateTableRequest.
    	}
    	resp, err := c.CreateTable(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) DeleteCatalog 
    
    
    func (c *MetastoreClient) DeleteCatalog(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[DeleteCatalogRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_DeleteCatalogRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Catalog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Catalog), [error](https://pkg.go.dev/builtin#error))

DeleteCatalog deletes an existing catalog specified by the catalog ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.DeleteCatalogRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#DeleteCatalogRequest.
    	}
    	resp, err := c.DeleteCatalog(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) DeleteDatabase 
    
    
    func (c *MetastoreClient) DeleteDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[DeleteDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_DeleteDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Database), [error](https://pkg.go.dev/builtin#error))

DeleteDatabase deletes an existing database specified by the database ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.DeleteDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#DeleteDatabaseRequest.
    	}
    	resp, err := c.DeleteDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) DeleteLock 
    
    
    func (c *MetastoreClient) DeleteLock(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[DeleteLockRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_DeleteLockRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteLock deletes an existing lock specified by the lock ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.DeleteLockRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#DeleteLockRequest.
    	}
    	err = c.DeleteLock(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*MetastoreClient) DeleteTable 
    
    
    func (c *MetastoreClient) DeleteTable(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[DeleteTableRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_DeleteTableRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Table](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Table), [error](https://pkg.go.dev/builtin#error))

DeleteTable deletes an existing table specified by the table ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.DeleteTableRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#DeleteTableRequest.
    	}
    	resp, err := c.DeleteTable(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) GetCatalog 
    
    
    func (c *MetastoreClient) GetCatalog(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[GetCatalogRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_GetCatalogRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Catalog](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Catalog), [error](https://pkg.go.dev/builtin#error))

GetCatalog gets the catalog specified by the resource name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.GetCatalogRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#GetCatalogRequest.
    	}
    	resp, err := c.GetCatalog(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) GetDatabase 
    
    
    func (c *MetastoreClient) GetDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[GetDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_GetDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Database), [error](https://pkg.go.dev/builtin#error))

GetDatabase gets the database specified by the resource name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.GetDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#GetDatabaseRequest.
    	}
    	resp, err := c.GetDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) GetTable 
    
    
    func (c *MetastoreClient) GetTable(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[GetTableRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_GetTableRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Table](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Table), [error](https://pkg.go.dev/builtin#error))

GetTable gets the table specified by the resource name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.GetTableRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#GetTableRequest.
    	}
    	resp, err := c.GetTable(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) ListCatalogs 
    
    
    func (c *MetastoreClient) ListCatalogs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[ListCatalogsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_ListCatalogsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CatalogIterator

ListCatalogs list all catalogs in a specified project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListCatalogsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListCatalogsRequest.
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
    		_ = it.Response.(*biglakepb.ListCatalogsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListCatalogsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListCatalogsRequest.
    	}
    	for resp, err := range c.ListCatalogs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*MetastoreClient) ListDatabases 
    
    
    func (c *MetastoreClient) ListDatabases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[ListDatabasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_ListDatabasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DatabaseIterator

ListDatabases list all databases in a specified catalog.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListDatabasesRequest.
    	}
    	it := c.ListDatabases(ctx, req)
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
    		_ = it.Response.(*biglakepb.ListDatabasesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListDatabasesRequest.
    	}
    	for resp, err := range c.ListDatabases(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*MetastoreClient) ListLocks 
    
    
    func (c *MetastoreClient) ListLocks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[ListLocksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_ListLocksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LockIterator

ListLocks list all locks in a specified database.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListLocksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListLocksRequest.
    	}
    	it := c.ListLocks(ctx, req)
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
    		_ = it.Response.(*biglakepb.ListLocksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListLocksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListLocksRequest.
    	}
    	for resp, err := range c.ListLocks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*MetastoreClient) ListTables 
    
    
    func (c *MetastoreClient) ListTables(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[ListTablesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_ListTablesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TableIterator

ListTables list all tables in a specified database.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListTablesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListTablesRequest.
    	}
    	it := c.ListTables(ctx, req)
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
    		_ = it.Response.(*biglakepb.ListTablesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.ListTablesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#ListTablesRequest.
    	}
    	for resp, err := range c.ListTables(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*MetastoreClient) RenameTable 
    
    
    func (c *MetastoreClient) RenameTable(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[RenameTableRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_RenameTableRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Table](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Table), [error](https://pkg.go.dev/builtin#error))

RenameTable renames an existing table specified by the table ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.RenameTableRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#RenameTableRequest.
    	}
    	resp, err := c.RenameTable(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) UpdateDatabase 
    
    
    func (c *MetastoreClient) UpdateDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[UpdateDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_UpdateDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Database), [error](https://pkg.go.dev/builtin#error))

UpdateDatabase updates an existing database specified by the database ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.UpdateDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#UpdateDatabaseRequest.
    	}
    	resp, err := c.UpdateDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*MetastoreClient) UpdateTable 
    
    
    func (c *MetastoreClient) UpdateTable(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[UpdateTableRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_UpdateTableRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Table](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Table), [error](https://pkg.go.dev/builtin#error))

UpdateTable updates an existing table specified by the table ID.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	biglake "cloud.google.com/go/bigquery/biglake/apiv1alpha1"
    	biglakepb "cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := biglake.[NewMetastoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_NewMetastoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1.html#cloud_google_com_go_bigquery_biglake_apiv1alpha1_MetastoreClient_Close)()
    
    	req := &biglakepb.UpdateTableRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/bigquery/biglake/apiv1alpha1/biglakepb#UpdateTableRequest.
    	}
    	resp, err := c.UpdateTable(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## TableIterator
    
    
    type TableIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*biglakepb.Table, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TableIterator manages a stream of *biglakepb.Table.

### func (*TableIterator) All 
    
    
    func (it *TableIterator) All() iter.Seq2[*biglakepb.Table, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TableIterator) Next 
    
    
    func (it *TableIterator) Next() (*[biglakepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb).[Table](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/biglake/apiv1alpha1/biglakepb#cloud_google_com_go_bigquery_biglake_apiv1alpha1_biglakepb_Table), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TableIterator) PageInfo 
    
    
    func (it *TableIterator) PageInfo() *[iterator](https://pkg.go.dev/google.golang.org/api/iterator).[PageInfo](https://pkg.go.dev/google.golang.org/api/iterator#PageInfo)

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-25 UTC."],[],[]] 
